"""
Solution de exercice 03
"""
# author: Kaan Eraslan
# license: see, LICENSE


if __name__ == "__main__":
    str1 = "une maison"
    str2 = "très petite"
    print(str2 + str1)
    print(str1 + str2)
    str1 = "une {0} maison"
    print(str1.format(str2))
