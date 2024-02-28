from tkinter import *
from tkinter import ttk
import settings
import os
import lore

settings.init()

def init():
    global root
    global images
    global screens

    images = {}
    screens = {
        "introScreen": introScreen,
        "characterCreation": characterCreation
    }

    root = Tk()
    root.title("Luminos")
    root.geometry(str(settings.gameWidth) + 'x' + str(settings.gameHeight))

    for image in os.listdir("images"):
        images[image] = "images/" + image

def gotoScreen(currentScreen, newScreen):
    currentScreen.destroy()
    screens[newScreen]()

def characterCreation():
    print("hej")

def introScreen():
    introFrame = Frame(root)
    introFrame.pack(side="top", expand=True, fill="both")

    introText = Label(introFrame, text=lore.introText, font=("Helvetica", 16))
    introText.pack(pady=10)

    continueButton = Button(introFrame, text="Continue", command=lambda: gotoScreen(introFrame, "characterCreation"))
    continueButton.pack(pady=20)



def chooseClass(rpgClass):
    chosenClass = rpgClass


init()
introScreen()
root.mainloop()