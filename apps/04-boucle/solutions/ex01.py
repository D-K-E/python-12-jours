"""
Solutions Exercice 01
"""

MATRICE = [[3, 6, 9], [86, 123, 76], [33, 56, 4]]


def diagSum(mat: list):
    "somme diagonale de matrice"
    revarr = list(reversed(mat))
    matsize = len(mat)
    fsum = 0
    for i in range(matsize):
        matr = mat[i][i]
        fsum += matr
    ksum = 0
    for i in range(matsize):
        matr = revarr[i][i]
        ksum += matr
    return fsum + ksum


if __name__ == "__main__":
    print("Matrice: ", str(MATRICE))
    print("Somme diagonale: ", str(diagSum(MATRICE)))
