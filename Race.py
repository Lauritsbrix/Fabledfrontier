class race:
    def __init__(self, description, vitMod, strMod, magMod, agiMod):
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.magMod = magMod
        self.agiMod = agiMod

humanDescription = "A simple and ordinary person, decent at most things but that is all"
human = race(humanDescription, 1, 1, 1, 1)

elf = race()
elf.description = "A mystical folk from the deep forest, has great magical attributes and are highly adapt."
elf.vitMod = 0
elf.strMod = 0
elf.magMod = 2
elf.agiMod = 2

dwarf = race()
dwarf.description = "Proud and brave fighters adept with heavy weapons. They have high health and strength."
dwarf.vitMod = 2
dwarf.strMod = 2
dwarf.magMod = 0
dwarf.agiMod = 0

race_info = {
    'Human': {
        'description': 'A simple and ordinary person, decent at most things but that is all',
        'stats': {'vitality': 1, 'strength': 1, 'magic': 1, 'agility': 1},
    },
    'Elf': {
        'description': 'A mystical folk from the deep forest, has great magical attributes and are highly adapt.',
        'stats': {'vitality': 0, 'strength': 0, 'magic': 2, 'agility': 2},
    },
    'Dwarf': {
        'description': 'Proud and brave fighters adept with heavy weapons. They have high health and strength.',
        'stats': {'vitality': 2, 'strength': 2, 'magic': 0, 'agility': 0},
    },
}