"""
solution ex 04
"""

class Model:
    def __init__(self, nb1, nb2, op):
        self.nb1 = nb1
        self.nb2 = nb2
        self.op = op

class View:
    def __init__(self, model):
        self.model = model

    def render(self):
        nb1 = str(model.nb1)
        nb2 = str(model.nb2)
        op = str(model.op)
        res = nb1 + " " + op + " " + nb2
        return res

class Control:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def compute(self):
        nb1 = float(model.nb1)
        nb2 = float(model.nb2)
        op = str(model.op)
        if opstr == "+":
            return nb1 + nb2
        elif opstr == "-":
            return nb1 - nb2
        elif opstr == "/":
            return nb1 / nb2
        elif opstr == "*":
            return nb1 * nb2
        else:
            raise ValueError('Unknown opérator: ' + op)

    def show(self):
        res = self.compute()
        rep = self.view.render()
        return rep + " = " + str(res)
