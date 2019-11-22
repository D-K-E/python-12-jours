"""
Hello world for tk gui
"""
import tkinter as tk
import tkinter.ttk as ttk


class MyGui:
    def __init__(self, master):
        # mon cadre
        frame = ttk.Frame(master)
        # gestionnaire de mon cadre
        frame.pack()
        #
        # declaration de zone d'affichage de texte
        self.labelTxt = tk.StringVar()
        self.label = ttk.Label(frame, textvariable=self.labelTxt)
        self.label.pack(side=tk.TOP)

        # declaration d'un bouton
        self.hellobtn = ttk.Button(frame, text="Bonjour", command=self.dire_bonjour)
        self.hellobtn.pack(side=tk.LEFT)

        # declaration d'un autre bouton
        self.nohellobtn = ttk.Button(
            frame, text="Pas de Bonjour", command=self.pas_de_bonjour
        )
        self.nohellobtn.pack(side=tk.LEFT)

        # declaration de bouton de sortie
        self.quitbtn = ttk.Button(frame, text="Bye!", command=frame.quit)
        self.quitbtn.pack(side=tk.LEFT)

    def dire_bonjour(self):
        "afficher bonjour dans le label"
        self.labelTxt.set("Bonjour Mesdames et Messieurs")

    def pas_de_bonjour(self):
        self.labelTxt.set("Je refuse de vous saluer Mesdames et Messieurs")


if __name__ == "__main__":
    root = tk.Tk()
    myapp = MyGui(root)
    root.mainloop()
