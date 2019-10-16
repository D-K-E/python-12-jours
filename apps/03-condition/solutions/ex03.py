"""
Solution to Exercice 03
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os


if __name__ == "__main__":
    fpath = os.path.join("assets", "ex03.txt")
    mot = input("Entrez un mot: ").strip()
    motsize = len(mot) + 3  # pour être sur d'inclure le mot 
    continue_afficher = True
    with open(fpath, "r", encoding="utf-8", newline="\n") as fd:
        while continue_afficher is True:
            partie = fd.read(motsize)
            if not partie:
                continue_afficher = False
                print("--- Texte Fini -----")
            elif mot in partie:
                print("-------------------")
                print(partie)
                print("-------------------")
                continue_afficher = False
            else:
                print(partie)
    print("Done!")
