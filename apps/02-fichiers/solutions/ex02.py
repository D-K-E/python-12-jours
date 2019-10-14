"""
Solution to Exercice 02
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os


if __name__ == "__main__":
    asset_path = os.path.join("assets", "ex02.txt")
    saisi = input("Entrez votre saisi: ")
    with open(asset_path, "w", encoding="utf-8", newline="\n") as fd:
        fd.write(saisi)
