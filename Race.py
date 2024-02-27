class race:
    def __init__(self, description, vitMod, strMod, magMod, agiMod):
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.magMod = magMod
        self.agiMod = agiMod

humanDescription = """

"""
human = race(humanDescription, 1, 1, 1, 1)

elfDescription = """

"""
elf = race(elfDescription, 0, 0, 2, 2)


dwarfDescription = """

"""
dwarf = race(dwarfDescription, 2, 2, 0, 0)

