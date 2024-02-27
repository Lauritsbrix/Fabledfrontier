import os

GAME_WIDTH = 120
GAME_HEIGHT = 20



def mapPainter():
    templateFile = open('maps/templateFile', 'w')
    screenLine = ""
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if x == 0 or x == GAME_WIDTH - 1:
                    screenLine += "|"
            elif y == 2 or y == GAME_HEIGHT - 1:
                screenLine += "-"
            else:
                screenLine += " "
        
        if y < GAME_HEIGHT:
            screenLine += "\n"
    
    os.system('cls')
    templateFile.write(screenLine)
    templateFile.close()
    print(screenLine)

mapPainter()