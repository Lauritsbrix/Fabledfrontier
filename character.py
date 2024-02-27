from stats import stats
from idManager import generateID, addID
import settings

class character:
    def __init__(self, type, name, race, RPGclass, charStats = "default", ID = "random", icon = "@"):
        self.type = type
        self.name = name
        self.race = race
        self.RPGclass = RPGclass
        self.icon = icon

        if ID == "random":
            self.ID = generateID(settings.idIndex, type)
        else:
            self.ID = addID(settings.idIndex, ID, type)

        if charStats == "default":
            self.stats = stats(10, 1, 1, 1, 1)
        else:
            self.stats = charStats
