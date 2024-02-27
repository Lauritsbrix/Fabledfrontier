class race:
    def __init__(self, description, vitMod, strMod, magMod, agiMod):
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.magMod = magMod
        self.agiMod = agiMod

humanDescription = "A simple and ordinary person, decent at most things but that is all"
human = race(humanDescription, 1, 1, 1, 1)

elfDescription = "A mystical folk from the deep forest, has great magical attributes and are highly adapt."
elf = race(elfDescription, 0, 0, 2, 2)

dwarfDescription = "Proud and brave fighters adept with heavy weapons. They have high health and strength."
dwarf = race(dwarfDescription, 2, 2, 0, 0)
