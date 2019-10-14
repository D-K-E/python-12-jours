"""
Solution to Exercice 04
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os


if __name__ == "__main__":
    asset_path = os.path.join("assets", "ex04.txt")
    with open(asset_path, "r", encoding="utf-8", newline="\n") as fd:
        lignes = fd.readlines()
        skip = False
        for ligne in lignes:
            if not skip:
                skip = True
                print(ligne)
            else:
                skip = False
