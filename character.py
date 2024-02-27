from stats import stats

class character:
    def __init__(self, ID, name, race, RPGclass, charStats = "default", icon = "@"):
        self.ID = ID
        self.name = name
        #self.type = type
        #self.gender = gender
        self.race = race
        self.RPGclass = RPGclass
        self.icon = icon

        if charStats == "default":
            self.stats = stats(10, 1, 1, 1, 1)
        else:
            self.stats = charStats
