"""
Solution to Exercice 01
"""
# Author: Kaan Eraslan
# License: see, LICENSE


if __name__ == "__main__":
    text = """
    Muse, chante, et dis-nous la funeste colère
    D'Achille, du héros dont Pelée est le père :
    Aux Grecs elle causa des malheurs infinis,
    Trancha de leurs guerriers les jours inaccomplis,
    Et leurs corps, par milliers, privés de sépulture,
    Des vautours et des chiens devinrent la pâture.
    Ainsi s'accomplissait la volonté des Cieux,
    Depuis qu'au camp des Grecs, un conflit malheureux
    Vint diviser Achille et le chef de l'armée."""
    saisi = input("Entrez un morceau de texte: ")
    if saisi in text:
        print("Le morceau: " + saisi + " est dans le texte")
    else:
        print("Le morceau n'est pas dans le texte")
