"""
Solutions Exercice 03
"""

LISTE = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


def imprimerParLigne(arr: list):
    for ligne in arr:
        print("   ".join([str(l) for l in ligne]))


def rotArr(ligne: list):
    lastEl = ligne.pop(0)
    ligne.append(lastEl)
    return ligne


def rotateArr(arr: list, rotNb: int):
    ""
    counter = 0
    while counter < rotNb:
        for i in range(len(arr)):
            ligne = arr[i]
            ligne = rotArr(ligne)
        counter += 1
    imprimerParLigne(arr)


if __name__ == "__main__":
    nb = input("Saisissez un nombre: ")
    print("liste de début: \n###############\n")
    imprimerParLigne(LISTE)
    print("\n#############\n")
    rotateArr(LISTE, int(nb))
