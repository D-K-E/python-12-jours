"""
Solutions de l'exercice 01
"""
# Author: Kaan Eraslan
# License: see, LICENSE
import os

## exercice

class FileIO:
    def __init__(self, chemin: str):
        self.chemin = chemin
        self.txt = ""

    def io_op(self, estqLire=False):
        if estqLire:
            with open(self.chemin, "r", encoding="utf-8", newline="\n") as fd:
                self.txt = fd.read()
        else:
            with open(self.chemin, "w", encoding="utf-8", newline="\n") as fd:
                fd.write(self.txt)




class FileReader(FileIO):
    def __init__(self, chemin: str):
        super().__init__(chemin=chemin)
    
    def imprimer_text(self):
        self.io_op(estqLire=True)
        print(self.txt)

class FileWriter(FileIO):
    def __init__(self, chemin: str):
        super().__init__(chemin)

    def enregistrer(self, mot: str):
        self.txt = mot
        self.io_op(estqLire=False)

