"""
Solutions Exercice 04
"""
import os
import urllib.request as req


def lireLiens(chemin: str) -> list:
    with open(chemin, "r", encoding="utf-8") as fd:
        liens = fd.readlines()
    return liens


def enregistreImage(data: bytes, chemin: str) -> None:
    "enregistre l'image au chemin"
    with open(chemin, "wb") as fd:
        fd.write(data)
    return


def telechargeImage(lien: str) -> bytes:
    "telecharge l'image et cree un chemin"
    with req.urlopen(lien) as li:
        data = li.read()
    return data


def ajouterLienAuFichier_proc(lien: str, cheminFichier: str) -> None:
    with open(cheminFichier, "a", encoding="utf-8") as fd:
        fd.write("\n" + lien)
    return


def supprimerLeContenuFichier_proc(cheminFichier: str) -> None:
    with open(cheminFichier, "w", encoding="utf-8") as fd:
        fd.write("")
    return


if __name__ == "__main__":
    liens_chemin = os.path.join("solutions", "liens-image.txt")
    imd = os.path.join("solutions", "image")
    mimgpath = os.path.join(imd, "mes-image.txt")
    supprimerLeContenuFichier_proc(mimgpath)
    liens = lireLiens(liens_chemin)
    for indice, lien in enumerate(liens):
        impath = "img-" + str(indice) + ".jpg"
        impath = os.path.join(imd, impath)
        ajouterLienAuFichier_proc(impath, mimgpath)
        imdata = telechargeImage(lien)
        enregistreImage(imdata, impath)
    print("Done!")
