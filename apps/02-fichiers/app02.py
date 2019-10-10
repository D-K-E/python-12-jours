""" Deuxième application pour illustrer les étapes de développement d'un
programme.

Pour le paradigme batisseur/fondateur qu'on adopte ici, veuillez consulter:

Ayeva, Kamon, and Sakis Kasampalis. Mastering Python Design Patterns.
Birmingham, 2018, 24 - 37.  """

import math
from lxml import etree


class DocumentBuilder:
    "Document builder"
    class Document:
        "Document contenant les propriétés d'un document"

        def __init__(self, filepath: str):
            self.path = filepath
            with open(filepath, "r", encoding="utf-8") as fp:
                data = fp.read()
                lines = fp.readlines()
            self.data = data
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
            strip_data = self.data.strip(self.stopchars)
            self.words = strip_data.split(self.splitword)
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

    class TeiDocument(Document):
        "Un document de type xml"

        def __init__(self, fpath: str):
            super().__init__(fpath)
            self.tei = etree.fromstring(self.data)

        def set_words(self):
            "Obtenir une liste de mot du document"
            self.words = [word.text for word in self.tei.iter(
                "w") if "text" in word]
            self.words = [word for word in self.words if word not in
                          self.stopwords]

    def build_doc(self, filepath: str):
        "Construit le document en fonction d'extension de chemin"
        assert isinstance(filepath, str)
        if filepath.endswith('xml'):
            self.doc = self.TeiDocument(filepath)
        elif filepath.endswith("txt"):
            self.doc = self.Document(filepath)
        else:
            raise ValueError("Unkown extension on filepath: " + filepath)

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
            words = set(doc.words)
            for word in words:
                terms.append(word)
        self.terms = list(set(terms))

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
        self.tf_idf_terms = tf_idf_terms


if __name__ == "__main__":
    with open("stopchars.txt", "r", encoding="utf-8", newline="\n") as fd:
        stopchars = fd.readlines()
        stopchars = stopchars[2] # parce que les deux premiers lignes sont
        # des references
    #
    with open("stopwordsLat.txt", "r", encoding="utf-8", newline="\n") as fd:
        stopwordslat = fd.readlines()
        stopwordslat = stopwordslat[2:]

    with open("stopwordsGr.txt", "r", encoding="utf-8", newline="\n") as fd:
        stopwordsgr = fd.readlines()
        stopwordsgr = stopwordsgr[2:]
