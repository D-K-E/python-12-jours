""" Deuxième application pour illustrer les étapes de développement d'un
programme.

Pour le paradigme batisseur/fondateur qu'on adopte ici, veuillez consulter:

Ayeva, Kamon, and Sakis Kasampalis. Mastering Python Design Patterns.
Birmingham, 2018, 24 - 37.  """

import math
import os
import json
from lxml import etree
import pdb


class DocumentBuilder:
    "Document builder"
    class Document:
        "Document contenant les propriétés d'un document"

        def __init__(self, filepath: str):
            self.path = filepath
            ###################################################
            with open(filepath, "r", encoding="utf-8") as fp:
                data = fp.read()  # lecture entier du contenu
                lines = fp.readlines()  # lecture par ligne du contenu
            ###################################################
            self.data = data
            self.ext = self.path.split(".").pop()
            self.brut_lines = lines
            self.nb_lines = None
            self.size = len(data)
            self.stopchars = ",;:/%*$.?!§"
            self.splitword = " "
            self.stopwords = ["un", "en", "dans", "plus", "à", "vers"]
            self.word_counts = {}
            self.word_weights = {}
            self.words = []
            self.terms = set()

        def set_words(self):
            "Faire un split des mots du document"
            strip_data = "".join([c for c in self.data if c not in
                                  self.stopchars])
            self.words = strip_data.split(self.splitword)
            self.words = [word.strip() for word in self.words]
            self.words = [word for word in self.words if word and word not in
                          self.stopwords]

        def set_terms(self):
            "Place les termes pour document"
            self.terms = set(self.words)

        def set_word_counts(self):
            "Nettoyer les données et compter les mots"
            word_counts = {}
            for word in self.words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            self.word_counts = word_counts

        def set_word_weights(self):
            "Normalizer les comptes des mots avec le compte total des mots"
            weights = {}
            total_word_count = len(self.words)
            for word, count in self.word_counts.items():
                weights[word] = count / total_word_count
            self.word_weights = weights

        def set_document_properties(self):
            "Set document properties"
            self.set_words()
            self.set_terms()
            self.set_word_counts()
            self.set_word_weights()

        def __str__(self):
            return "Document at " + self.path

    class TeiDocument(Document):
        "Un document de type xml"

        def __init__(self, fpath: str):
            super().__init__(fpath)
            self.parser = etree.XMLParser(remove_blank_text=True,
                                          encoding="utf-8",
                                          ns_clean=True, recover=True)
            self.tei = etree.XML(bytes(bytearray(self.data, "utf-8")),
                                 self.parser)

        def set_words(self):
            "Obtenir une liste de mot du document"
            self.words = [word.text for word in self.tei.iter(
                "w") if word.text]
            self.words = [word for word in self.words if word not in
                          self.stopwords]

    def choose_doc(self, filepath: str):
        "Construit le document en fonction d'extension de chemin"
        assert isinstance(filepath, str)
        if filepath.endswith('xml'):
            self.doc = self.TeiDocument(filepath)
        elif filepath.endswith("txt"):
            self.doc = self.Document(filepath)
        else:
            raise ValueError("Unkown extension on filepath: " + filepath)
        return self.doc

    def set_stop_chars(self, chars: str):
        "Place les caractères à filtrer au doc"
        assert isinstance(chars, str)
        self.doc.stopchars = chars

    def set_stopwords(self, stopwords: list):
        "Place les mots d'arret à filtrer au doc"
        assert isinstance(stopwords, list)
        self.doc.stopwords = stopwords

    def set_word_split(self, char: str):
        "Place le séparateur de mots"
        assert isinstance(char, str)
        self.doc.splitword = char

    def build_doc(self, stop_chars: str, stop_words: str,
                  word_split_char: str, filepath: str):
        "Build document using given parameters"
        self.choose_doc(filepath)
        self.set_stop_chars(stop_chars)
        self.set_stopwords(stop_words)
        self.set_word_split(word_split_char)


class DocumentCollection:
    "Collection de document bati par DocumentBuilder"

    def __init__(self, docs: list):
        assert isinstance(docs, (list, tuple))
        self.collection = dict(enumerate(docs))
        self.nb_documents = len(docs)
        self.terms = []
        self.term_frequencies = {}
        self.document_frequencies = {}
        self.inverse_document_frequencies = {}
        self.tf_idf_terms = {}

    def set_terms(self):
        "Obtient les termes de collection"
        terms = []
        for doc in self.collection.values():
            doc_terms = doc.terms
            for term in doc_terms:
                terms.append(term)
        self.terms = set(terms)

    def set_term_frequency(self):
        "Obtient la fréquence de term pour la collection"
        term_counts = {}
        for term in self.terms:
            count = 0
            for doc in self.collection.values():
                if term in doc.terms:
                    doc_count = doc.word_counts[term]
                    count += doc_count
            #
            term_counts[term] = count
        self.term_frequencies = term_counts

    def set_document_frequency(self):
        "Obtient la fréquence de document pour les termes"
        doc_count = {}
        for term in self.terms:
            count = 0
            for doc in self.collection.values():
                if term in doc.terms:
                    count += 1
            doc_count[term] = count
        self.document_frequencies = doc_count

    def set_inverse_document_frequency(self):
        """
        Obtient la fréquence inverse de document pour les termes

        Le formule est pris de Manning, Christopher, Prabhakar Raghavan, and
        Hinrich Schütze. An Introduction to Information Retrieval. Cambridge,
        2009, 118 (6.7)
        """
        inverse_document_frequencies = {}
        for term, freq in self.document_frequencies.items():
            log_interior = self.nb_documents / freq
            inverse_document_frequencies[term] = math.log(log_interior)
        self.inverse_document_frequencies = inverse_document_frequencies

    def set_tf_idf_to_terms(self):
        "Place le poids tf-idf pour les termes"
        tf_idf_terms = {}
        for term in self.terms:
            tf_idf_terms[term] = {}
            idf = self.inverse_document_frequencies[term]
            for index, doc in self.collection.items():
                if term in doc.word_counts:
                    doc_term_frequency = doc.word_counts[term]
                else:
                    doc_term_frequency = 0
                tf_idf_term = doc_term_frequency * idf
                tf_idf_terms[term][index] = tf_idf_term
        #
        tf_idf_terms = self.sort_tf_idf_terms(tf_idf_terms)
        self.tf_idf_terms = tf_idf_terms

    def sort_tf_idf_terms(self, tf_idf_terms: dict):
        "sort tf idf frequencies"
        for term, doc_index_tf_idf in tf_idf_terms.items():
            tf_idf_terms[term] = None
            doc_index_tf_idf = [
                list(item) for item in doc_index_tf_idf.items()
            ]
            doc_index_tf_idf.sort(key=lambda x: x[1])
            tf_idf_terms[term] = doc_index_tf_idf
        return tf_idf_terms

    def set_collection_properties(self):
        "Collection properties"
        self.set_terms()
        self.set_term_frequency()
        self.set_document_frequency()
        self.set_inverse_document_frequency()
        self.set_tf_idf_to_terms()

    def change_doc_index_to_path(self) -> dict:
        "change document index to document path"
        tf_idf_terms = {}
        for term, doc_index_tf_idf in self.tf_idf_terms.items():
            tf_idf_terms[term] = []
            for doc_index, tf_idf in doc_index_tf_idf:
                doc = self.collection[doc_index]
                doc_path = doc.path
                tf_idf_terms[term].append([doc_path, tf_idf])
        return tf_idf_terms

    def save_tf_idf_terms(self, filepath: str):
        "save tf idf dictionary to file path"
        tf_idf_terms = self.change_doc_index_to_path()
        ################################################################
        with open(filepath, "w", encoding="utf-8", newline="\n") as fd:
            json.dump(tf_idf_terms, fd, ensure_ascii=False, indent=4)
        ################################################################

#####################################################


def read_text(chemin: str, start_line=2):
    "Read text"
    with open(chemin, "r", encoding="utf-8", newline="\n") as fd:
        txt = fd.readlines()
        txt = txt[start_line:]
        txt = [t.strip() for t in txt]
    return txt
#####################################################


def make_path(basepath: str, filenames: list):
    "make path using base path"
    return [os.path.join(basepath, filename) for filename in filenames]


if __name__ == "__main__":
    asset_path = "assets"
    filenames = ["stopchars.txt", "stopwordsLat.txt",
                 "stopwordsGr.txt", "greek-text.txt", "tei-latin.xml",
                 "collection-tf-idf.json"]
    paths = make_path(asset_path, filenames)
    ################################################################
    with open(paths[0], "r", encoding="utf-8", newline="\n") as fd:
        stopchars = fd.readlines()
        stopchars = stopchars[2]  # parce que les deux premiers lignes sont
        # des references
    #
    ################################################################
    stopwords_latin = read_text(paths[1])
    stopwords_grecque = read_text(paths[2])
    #
    text_doc_builder = DocumentBuilder()
    text_doc_builder.build_doc(filepath=paths[3],
                               stop_chars=stopchars,
                               stop_words=stopwords_grecque,
                               word_split_char=" ")
    doc_grecque = text_doc_builder.doc
    # greek text from
    # http://data.perseus.org/citations/
    # urn:cts:greekLit:tlg0560.tlg001.perseus-grc1:1
    doc_grecque.set_document_properties()
    #
    xml_doc_builder = DocumentBuilder()
    xml_doc_builder.build_doc(filepath=paths[4],
                              stop_chars=stopchars,
                              stop_words=stopwords_latin,
                              word_split_char=" ")
    doc_latin = xml_doc_builder.doc
    doc_latin.set_document_properties()
    collection = DocumentCollection(docs=[doc_grecque, doc_latin])
    collection.set_collection_properties()
    collection.save_tf_idf_terms(paths[5])
    print("Application done")
