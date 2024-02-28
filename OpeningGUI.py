import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

# Opret hovedvinduet
root = tk.Tk()
root.title("Luminos")

magePhoto = PhotoImage(file = r"wizard.png")


# Funktion, der udføres ved at klikke på knappen
def chooseClass(rpgClass):
    chosenClass = rpgClass

def button_click():
    label.config(text="Create your character!")

    Label(root, text = 'Mage', font =('Helvetica', 22)).pack(side = TOP, pady = 20)

    mageButton = tk.Button(root, text = 'Click ME!', image = magePhoto, command=chooseClass("mage"))
    mageButton.pack(side=TOP)


button = tk.Button(text="Continue", command=button_click)
button.pack(pady=20)

# Opret en label (tekstfelt)
label = tk.Label(root, text="""In the realm of Luminos, a land shrouded in the mists of ancient magic and surrounded by untamed wilderness,
three distinct races coexisted for centuries – Humans, Elves, and Dwarves.
They have shared the blessings of their fertile lands, harnessed the power of arcane forces, and built great cities that touched the skies.
""", font=("Helvetica", 16))
label.pack(pady=10)

# Opret en knap
button = tk.Button(root, text="Continue", command=button_click)
button.pack(pady=20)

# Start hovedløkken for at vise vinduet
root.mainloop()
