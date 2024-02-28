from tkinter import *
from tkinter import ttk
import settings
import os
import lore

settings.init()

def init():
    global root
    global images

    images = {}

    root = Tk()
    root.title("Luminos")
    root.geometry(str(settings.gameWidth) + 'x' + str(settings.gameHeight))

    for image in os.listdir("images"):
        images[image] = "images/" + image
    
    introText = Label(root, text=lore.introText, font=("Helvetica", 16))
    introText.pack(pady=10)

    continueButton = 0

def chooseClass(rpgClass):
    chosenClass = rpgClass




init()
root.mainloop()