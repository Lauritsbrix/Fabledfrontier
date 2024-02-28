import interfaceRenderer
import os
from character import character
import Race
import RPGClass
import idManager
import settings
from stats import stats

#Introduktion til Luminos
text =  """In the realm of Luminos, a land shrouded in the mists of ancient magic and surrounded by untamed wilderness,
three distinct races coexist – Humans, Elves, and Dwarves. For centuries.
They have shared the blessings of their fertile lands, harnessed the power of arcane forces, and built great cities that touched the skies.
"""

def startAnswer(answer):
    accpetableAnswer = ["yes"]
    while start.lower() not in accpetableAnswer:
        print("You have to be ready")
    start = input("are you ready for an adventure?")

def create_Character():
    os.system('cls')
    print("Welcome to Character creation!")
    name = input("Enter your name: ")

    while True:
        vitality = 1
        strength = 1
        magic = 1
        agility = 1

        raceChoice = ""
        chosenRace = False
        while not chosenRace:
            os.system('cls')
            print("Races avallable: ")
            for race_name in Race.races:
                print(race_name.capitalize())
            
            race = input(f"Enter your race: [Dwarf, Human or Elf] ").lower()
            os.system('cls')

            try:
                raceChoice = Race.races[race]

                print(f"""Description: {raceChoice.description}
{raceChoice.name.capitalize()} has the following stats
HP: {10 + raceChoice.vitMod}
Strength: {1 + raceChoice.strMod}
Inteligence: {1 + raceChoice.magMod}
Agility: {1 + raceChoice.agiMod}""")
                
                chosenRace = True
            except:
                print("You have to write either Dwarf, Human or Elf")
                input("Press enter to continue")

        vitality += raceChoice.vitMod
        strength += raceChoice.strMod
        magic += raceChoice.magMod
        agility += raceChoice.agiMod
        
        input("Press enter to continue ")
        os.system('cls')

        classChoice = ""
        chosenClass = False
        while not chosenClass:
            os.system('cls')
            print("Classes available: ")
            for class_name in RPGClass.classes:
                print(class_name.capitalize())

            rpgClass = input("Enter your Class: [Warrior, Mage or Archer] ").lower()
            os.system('cls')

            try:
                classChoice = RPGClass.classes[rpgClass]

                print(f"""Description: {classChoice.description}
{classChoice.name.capitalize()} has the following stats
HP: {10 + classChoice.vitMod}
Strength: {1 + classChoice.strMod}
Inteligence: {1 + classChoice.magMod}
Agility: {1 + classChoice.agiMod}""")
                
                chosenClass = True

            except:
                print("You have to write either Warrior, Mage or Archer")
                input("Press enter to continue")
        
        vitality += classChoice.vitMod
        strength += classChoice.strMod
        magic += classChoice.magMod
        agility += classChoice.agiMod

        input("Press enter to continue ")
        os.system('cls')

        playerStats = stats(vit=vitality, str=strength, mag=magic, agi=agility)
        player = character("player", name, race, rpgClass, ID=0, charStats=playerStats)
        return player

def initializeGame():
    settings.init()
    interfaceRenderer.init()

#TODO create game function
def game():
    pass


initializeGame()
os.system('cls')
print(text)

print()
print(f"Nice to meeet you")
start = input("Are you ready for an epic quest? ")

player = create_Character()
interfaceRenderer.paintInterface('basicInterface', player)