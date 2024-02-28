import random

def generateID(idDict, name):
    isUnique = False
    while not isUnique:
        id = random.randint(1, 9999)
        if id not in idDict:
            isUnique = True
    
    idDict[id] = name
    return id

def addID(idDict, id, name):
    isUnique = False
    while not isUnique:
        if id not in idDict:
            isUnique = True
        else:
            id += 1
    
    idDict[id] = name
    return id
    
