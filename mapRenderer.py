import os

GAME_WIDTH = 120
GAME_HEIGHT = 20

def mapPainter():
    templateFile = open('maps/templateFile', 'w')
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

mapPainter()