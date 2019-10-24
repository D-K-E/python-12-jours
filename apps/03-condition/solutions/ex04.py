"""
Solution to Exercice 03
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os
import sys


def print_stars(el: int) -> None:
    "imprimer le nombre avec l'équivalence d'étoile"
    stars = "".join(["*" for i in range(el)])
    impr = str(el) + " = " + stars
    print(impr)


def print_nb(arr: list):
    "Imprimer les nombres de la liste"
    if isinstance(arr, int):
        print_stars(arr)
        return
    for el in arr:
        if isinstance(el, list):
            print_nb(el)
        else:
            print_stars(el)


if __name__ == "__main__":
    MA_LISTE = [[1, 2], 3,
                [4, [5, 6], 7, [8, 9, [10, 11], 12], 13],
                14, [15, 16, [17, 18]]
                ]
    print_nb(MA_LISTE)
    print("Done")
