"""
Solution de exercice 06
"""
# author: Kaan Eraslan
# license: see, LICENSE

def poly_sum(arr: list):
    "Comptez la somme d'une liste"
    count = 0
    for a in arr:
        if isinstance(a, (int, float)):
            count += a
    return count


if __name__ == "__main__":
    mylist = [1, 53, 1.3, 4.8, "a", 42j, "oro", ["a", "r"], {"p": 'oo'}]
    print(str(poly_sum(mylist)))
