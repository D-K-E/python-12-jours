"""
Solutions Exercice 02
"""

LISTE = [1, 2, 3, 4, 5, 6, 7, 8]


def rotateArr(arr: list, rotNb: int):
    ""
    counter = 0
    while counter < rotNb:
        lastEl = arr.pop(0)
        arr.append(lastEl)
        counter += 1
    print(' '.join([str(a) for a in arr]))


if __name__ == "__main__":
    nb = input("Saisissez un nombre: ")
    rotateArr(LISTE, int(nb))
