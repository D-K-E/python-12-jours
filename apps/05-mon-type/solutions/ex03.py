"""
solutions ex 03
"""
import os
import urllib.request as req

class FileDealer:
    def __init__(self):
        pass

    @staticmethod
    def liens(chemin: str):
        with open(chemin, "r", encoding="utf-8") as fd:
            liens = fd.readlines()
        return liens

    @staticmethod
    def saveData(data, chemin):
        with open(chemin, "wb") as fd:
            fd.write(data)
        return

    @staticmethod
    def addLigne(ligne, chemin):
        with open(chemin, "a", encoding="utf-8") as fd:
            fd.write("\n" + ligne)
        return



class Lien:
    def __init__(self, lien: str):
        self.lien = lien

    def read(self) -> bytes:
        "telecharge l'image et cree un chemin"
        with req.urlopen(self.lien) as li:
    	    data = li.read()
        return data

if __name__ == "__main__":
    liens_chemin = os.path.join("solutions", "liens-image.txt")
    imd = os.path.join("solutions", "image")
    mimgpath = os.path.join(imd, "mes-image.txt")
    liens = FileDealer.liens(liens_chemin)
    for indice, lien in enumerate(liens):
        impath = "img-" + str(indice) + ".jpg"
        impath = os.path.join(imd, impath)
        maLien = Lien(lien)
        imdata = maLien.read()
        FileDealer.saveData(imdata, impath)
        FileDealer.addLigne(impath, mimgpath
