# import mapRenderer
import os
import character
import Race
import RPGClass

# mapRenderer.mapPainter()

#Introduktion til Luminos
text =  """
In the realm of Luminos, a land shrouded in the mists of ancient magic and surrounded by untamed wilderness,
three distinct races coexist – Humans, Elves, and Dwarves. For centuries.
They have shared the blessings of their fertile lands, harnessed the power of arcane forces, and built great cities that touched the skies.
"""



def startAnswer(answer):
    accpetableAnswer = ["yes"]
    while start.lower() not in accpetableAnswer:
        print("You have to be ready")
    start = input("are you ready for an adventure?")

class Character:
    def __init__ (self, name, race, RPGClass):
        self.name = name
        self.race = race
        self.RPGClass = RPGClass


def __str(self):
    return (f"Charecter: {self.name}\nRace: {self.race}\nRPGClass: {self.RPGClass}")

def create_Character():
    print("Welcome to Character creation!")
    name = input("Enter your name: ")
    while True:
        print("Races avallable: ")
        for race_name in RPGClass.classes:
            print(race_name)
            race = input(f"Enter your race: [Dwarf, Human or Elf] ")
    RPGClass = input("Enter your Class: [Warrior, Mage or Artcher] ")



    player = character.character("player", name, race, RPGClass)
    return player

print(text)

name = input("What is your name? ")
print(f"Nice to meeet you {name}")
start = input("Are you ready for the adventure if of your life? ")

player = create_Character()



