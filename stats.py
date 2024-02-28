class stats:
    def __init__(self, health = 10, vit = 0, str = 0, mag = 0, agi = 0):
        self.health = health + vit
        self.vitality = vit
        self.strength = str
        self.magic = mag
        self.agility = agi