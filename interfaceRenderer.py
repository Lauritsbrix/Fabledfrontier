import os
from character import character
from stats import stats

GAME_WIDTH = 120
GAME_HEIGHT = 20

interfaceFiles = {}
interfaces = {}

for interface in os.listdir("interfaces"):
    interfaceFiles[interface] = "interfaces/" + interface

def initInterfaceDict(interfaceDict):
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            interfaceDict[(x, y)] = "x"

def getInterfaceDictFromFile(file):
    file = open(file, 'r')
    content = file.readlines()
    interfaceDict = {}

    y = 0
    for line in range(len(content)):
        x = 0
        for char in content[line]:
            interfaceDict[(x, y)] = char
            x += 1
        y += 1
    
    file.close()
    return interfaceDict

def addElementToInterface(interfaceDict, x, y, element):
    pass

def paintInterface(interface, player):
    interfaceDict = interfaces[interface]
    screenLine = ""
    y = 0
    while y < GAME_HEIGHT:
        x = 0
        while x < GAME_WIDTH:
            if interfaceDict[(x, y)] == 'n':
                nameString = "Name:   " + player.name.capitalize()
                screenLine += nameString
                x += len(nameString)
            elif interfaceDict[(x, y)] == 'h':
                healthString = "Health: " + str(player.stats.health)
                screenLine += healthString
                x += len(healthString)
            else:
                screenLine += interfaceDict[(x, y)]
                x += 1

        if y < GAME_HEIGHT:
            screenLine += "\n"
        
        y += 1
    
    os.system('cls')
    print(screenLine)


def createTemplateInterface():
    templateFile = open('interfaces/templateFile', 'w')
    screenLine = ""
    for y in range(GAME_HEIGHT):
        currentY = y
        for x in range(GAME_WIDTH):
            currentX = x
            if currentX == 0 or currentX == GAME_WIDTH - 1:
                screenLine += "|"
            elif currentX == 3 and currentY == 1:
                screenLine += "health"
                currentX += 6
            elif currentY == 2:
                screenLine += "-"
            elif currentY == GAME_HEIGHT - 1:
                screenLine += "_"
            else:
                screenLine += " "
        
        if currentY < GAME_HEIGHT:
            screenLine += "\n"
    
    os.system('cls')
    templateFile.write(screenLine)
    templateFile.close()
    print(screenLine)

def initInterfacesDict(interfacesDict, interfaceFiles):
    for interfaceFile in interfaceFiles:
        tempInterfaceDict = getInterfaceDictFromFile(interfaceFiles[interfaceFile])
        interfacesDict[interfaceFile] = tempInterfaceDict

def init():
    initInterfacesDict(interfaces, interfaceFiles)

# paintInterface('basicInterface', player)