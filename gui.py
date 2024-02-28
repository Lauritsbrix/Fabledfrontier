from tkinter import *
from tkinter import ttk
import settings

settings.init()

def init():
    global root
    root = Tk()
    root.geometry(str(settings.gameWidth) + 'x' + str(settings.gameHeight))

init()
root.mainloop()