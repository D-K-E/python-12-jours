"""
Solutions Exercice 05
"""
import os
import json
import urllib.request as req


def lireLiens(chemin: str) -> list:
    with open(chemin, "r", encoding="utf-8") as fd:
        liens = fd.readlines()
    return liens


def enregistreJson(data: dict, chemin: str) -> None:
    "enregistre le json au chemin"
    with open(chemin, "w", encoding="utf-8", newline="\n") as fd:
        monjson = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
        fd.write(monjson)
    return


def telechargeJson(lien: str) -> dict:
    "telecharge le json et transforme le a une dictionnaire"
    with req.urlopen(lien) as li:
        data = li.read()
        data = json.loads(data)
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
    liens_chemin = os.path.join("solutions", "liens-json.txt")
    imd = os.path.join("solutions", "json")
    mjpath = os.path.join(imd, "mes-dictionnaire.txt")
    supprimerLeContenuFichier_proc(mjpath)
    liens = lireLiens(liens_chemin)
    for indice, lien in enumerate(liens):
        jpath = "pleiades-" + str(indice) + ".json"
        jpath = os.path.join(imd, jpath)
        ajouterLienAuFichier_proc(jpath, mjpath)
        jdata = telechargeJson(lien)
        mdata = {}
        mdata["titre"] = jdata["title"]
        mdata["zone"] = jdata["bbox"]
        mdata["point"] = jdata["reprPoint"]
        mdata["info"] = jdata["description"]
        mdata["pleiadesId"] = jdata["id"]
        enregistreJson(mdata, jpath)
    print("Done!")
