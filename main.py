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

""" class Character:
    def __init__ (self, name, race, rpgClass):
        self.name = name
        self.race = race
        self.rpgClass = rpgClass


    def __str(self):
        return (f"Charecter: {self.name}\nRace: {self.race}\nRPGClass: {self.rpgClass}") """

def create_Character():
    os.system('cls')
    print("Welcome to Character creation!")
    name = input("Enter your name: ")
    os.system('cls')
    while True:
        print("Races avallable: ")
        for race_name in Race.races:
            print(race_name.capitalize())
            
        race = input(f"Enter your race: [Dwarf, Human or Elf] ").lower()
        os.system('cls')

        raceChoice = Race.races[race]

        print(f"""Description: {raceChoice.description}
{raceChoice.name.capitalize()} has the following stats
HP: {10 + raceChoice.vitMod}
Strength: {1 + raceChoice.strMod}
Inteligence: {1 + raceChoice.magMod}
Agility: {1 + raceChoice.agiMod}""")
        
        input("Press enter to continue")
        os.system('cls')

        print("Classes available")
        for class_name in RPGClass.classes:
            print(class_name.capitalize())
            
        rpgClass = input("Enter your Class: [Warrior, Mage or Artcher] ")

        player = character.character("player", name, race, rpgClass)
        return player

os.system('cls')
print(text)

name = input("What is your name? ")
print()
print(f"Nice to meeet you {name}")
start = input("Are you ready for the adventure if your life? ")

player = create_Character()



