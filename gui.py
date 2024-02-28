from tkinter import *
from tkinter import ttk
import settings
import os
import lore

settings.init()

def init():
    global root
    global images

    root = Tk()
    root.title("Luminos")
    root.geometry(str(settings.gameWidth) + 'x' + str(settings.gameHeight))

    for image in os.listdir("images"):
        images[image] = "images/" + image
    
    introText = Label(root, text=lore.introText)

def chooseClass(rpgClass):
    chosenClass = rpgClass




init()
root.mainloop()