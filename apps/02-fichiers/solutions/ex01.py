"""
Solution to Exercice 01
"""
# Author: Kaan Eraslan
# License: see, LICENSE
import os


if __name__ == "__main__":
    asset_path = os.path.join("assets", "ex01.txt")
    with open(asset_path, "r", encoding="utf-8", newline="\n") as fd:
        txt = fd.read()
        print(txt)
