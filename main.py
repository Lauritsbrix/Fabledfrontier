import mapRenderer
import os

# mapRenderer.mapPainter()

#Introduktion til Luminos
text =  """
In the realm of Luminos, a land shrouded in the mists of ancient magic and surrounded by untamed wilderness,
three distinct races coexist – Humans, Elves, and Dwarves. For centuries.
They have shared the blessings of their fertile lands, harnessed the power of arcane forces, and built great cities that touched the skies.
"""

print(text)

name = input("What is your name? ")
print(f"Nice to meeet you {name}")
start = input("Are you ready for the adventure if your life? ")

def startCon(start):
    accpetableAnswer = ["ja"]
    while start.lower() not in accpetableAnswer:
        print("You have to be ready")
    start = input("are you ready for an adventure?")
