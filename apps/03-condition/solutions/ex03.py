"""
Solution to Exercice 03
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os
import sys


def read_in_chunks(fpath: str, csize: int, mot_cherche: str):
    "lire le fichier par partie"
    with open(fpath, "r", encoding="utf-8", newline="\n") as fd:
        continue_read = True
        while continue_read:
            part = fd.read(csize)
            if not part:
                continue_read = False
                return False, None
            if mot_cherche in part:
                continue_read = False
                return True, part


if __name__ == "__main__":
    fpath = os.path.join("assets", "ex03.txt")
    mot = input("Entrez un mot: ").strip()
    chunk_size = len(mot) * 2
    for size in range(chunk_size):
        isFound, partie = read_in_chunks(fpath, size, mot)
        if isFound:
            print("-------------------")
            print(partie)
            print("-------------------")
            print("Mot trouvé!")
            print("Done!")
            sys.exit(0)
    print("Mot pas trouvé!")
    print("Done!")
