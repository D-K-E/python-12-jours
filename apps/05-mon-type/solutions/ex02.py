"""
Solutions de l'exercice 02
"""
# Author: Kaan Eraslan
# License: see, LICENSE
import os

## exercice


class Etudiant:
    def __init__(self, idstr: str, note: int):
        self.note = note
        self.etu_nb = idstr


class Prof:
    def __init__(self):
        self.mentions = {
            "bien": list(range(14, 16)),
            "très bien": list(range(16, 19)),
            "admis": list(range(10, 14)),
            "parfait": list(range(19, 21)),
        }

    def eval_etu(self, etu: Etudiant):
        for mention, gamme in self.mentions.items():
            if etu.note in gamme:
                return etu.etu_nb + " a la mention " + mention
        return etu.etu_nb + "a raté"


ETUDIANTS = [Etudiant("etu15", 0), Etudiant("etu242", 12), Etudiant("etu3", 10)]

if __name__ == "__main__":
    unProf = Prof()
    for etu in ETUDIANTS:
        unProf.eval_etu(etu)

