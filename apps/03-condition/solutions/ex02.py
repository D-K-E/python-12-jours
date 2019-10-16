"""
Solution to Exercice 02
"""
# Author: Kaan Eraslan
# License: see, LICENSE


if __name__ == "__main__":
    ETUDIANTS = {"etu15": 0, "etu242": 12, "etu3": 10,
                 "etu4135": 14, "etu345": 19, "etu61": 16, "etu887": 8}
    for etuname, note in ETUDIANTS.items():
        if 0 <= note and note <= 9:
            print(etuname, "a la mention", "non admis")
        elif 10 <= note and note <= 13:
            print(etuname, "a la mention", "admis")
        elif 14 <= note and note <= 15:
            print(etuname, "a la mention", "bien")
        elif 16 <= note and note <= 18:
            print(etuname, "a la mention", "très bien")
        elif 19 <= note and note <= 20:
            print(etuname, "a la mention", "parfait")
