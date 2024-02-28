from tkinter import *
from tkinter import ttk
import settings

settings.init()

root = Tk()
root.geometry(str(settings.gameWidth) + 'x' + str(settings.gameHeight))
# frame = ttk.Frame(root, width=GAME_WIDTH, height=GAME_HEIGHT)


root.mainloop()