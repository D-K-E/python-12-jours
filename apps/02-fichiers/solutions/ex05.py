"""
Solution to Exercice 05
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os

if __name__ == "__main__":
    print("Salut ceux qui pensent avec des mots clés")
    delimit = input("Entrez votre délimiteur: ")
    mots = input("Entrez les mots avec le délimiteur: ")
    if delimit not in mots:
        raise ValueError(
            "Les mots ne contiennent pas le délimiteur: " + mots
        )
    #
    savepath = os.path.join("assets", "ex05-mes-mots-clés.txt")
    mots_separer = mots.split(delimit)
    mots_espace = " ".join(mots_separer)
    with open(savepath, "w", encoding="utf-8", newline="\n") as fd:
        fd.write("Mes Mots Clés")
        fd.write("\n")
        fd.write(mots)
        fd.write("\n")
        fd.write(mots_espace)
        fd.write("\n")
        fd.write(mots_separer.pop(0))
        for mot in mots_separer:
            fd.write("\n")
            fd.write(mot)
    print("Les mots sont enregistrés")
