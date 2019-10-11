"""
Solution de exercice 05
"""
# author: Kaan Eraslan
# license: see, LICENSE

if __name__ == "__main__":
    mylist = []
    for el in [23, 456, 8, 23, 1, 86, 44, 13]:
        mylist.append(el)
    #
    def sfncm(x):
        if x < 15:
            return x ** 2
        return x
    def sfnc(x): return x ** 2 if x < 15 else x
    # trois façons de faire la même chose
    m1 = mylist.copy()
    m1.sort(key=sfncm)
    m2 = mylist.copy()
    m2.sort(key=sfnc)
    m3 = mylist.copy()
    m3.sort(key=lambda x: x**2 if x < 15 else x)
    print(m1)
    print(m2)
    print(m3)
