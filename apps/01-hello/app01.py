""" Première application pour illustrer les étapes de développement d'un
programme.

Pour le paradigme MVC qu'on adopte ici, veuillez consulter:

Ayeva, Kamon, and Sakis Kasampalis. Mastering Python Design Patterns.
Birmingham, 2018, 84 - 91.
"""

# Déclaration des paquets

# fin de déclaration des paquets


# Déclaration de modèle.

MODEL = {"nombre1": "", "nombre2": "",
         "operateur": ""}

# fin de déclaration de modèle.

# déclaration de vue

def render_model(model_normal: dict):
    "Transformer le model à une représentation plus"
    nb1 = str(model_normal["nombre1"])
    nb2 = str(model_normal["nombre2"])
    opstr = str(model_normal["operateur"])
    res = " ".join([nb1, opstr, nb2])
    return res


VIEW = {"render": render_model, "model": MODEL}

# fin de déclaration de vue
# déclaration de contrôleur

def compute_model_result(model_normal: dict):
    "Calculer le résultat des éléments de modèle"
    opstr = model_normal["operateur"]
    nb1 = float(model_normal["nombre1"])
    nb2 = float(model_normal["nombre2"])
    if opstr == "+":
        return nb1 + nb2
    elif opstr == "-":
        return nb1 - nb2
    elif opstr == "/":
        return nb1 / nb2
    elif opstr == "*":
        return nb1 * nb2
    else:
        raise ValueError('Unknown opérator: ' + model_normal["operateur"])


def show_model_result(view: dict, model_normal: dict):
    "show model result"
    res = compute_model_result(model_normal)
    model_str = view["render"](model_normal)
    return model_str + " = " + str(res)


CONTROL = {"show": show_model_result, "view": VIEW, "model": MODEL}

# fin de déclaration de contrôleur

if __name__ == "__main__":
    # point d'entrée du programme
    nb1str = input("Entrez le premier nombre: ")
    nb2str = input("Entrez le deuxième nombre: ")
    opstr = input("Entrez l'opérateur [+,-,/,*]: ")
    MODEL["nombre1"] = nb1str
    MODEL["nombre2"] = nb2str
    MODEL["operateur"] = opstr
    VIEW["model"] = MODEL
    CONTROL["view"] = VIEW
    CONTROL["model"] = MODEL
    print(CONTROL["show"](CONTROL["view"], CONTROL["model"]))
    # fin d'exécution
