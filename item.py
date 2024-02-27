class item:
    def __init__(self, name, description, vitMod = 0, strMod = 0, intMod = 0, agiMod = 0):
        self.name = name
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.intMod = intMod
        self.agiMod = agiMod

healthPotion = item("Health Potion", "Heals you 5 HP", vitMod=5)