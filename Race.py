class race:
    def __init__(self, name, description, vitMod, strMod, magMod, agiMod):
        self.name = name
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.magMod = magMod
        self.agiMod = agiMod

races = {}

humanDescription = """Humans: With their ambition and resilience, Humans have built mighty kingdoms and sprawling cities.
They are skilled in the arts of war and diplomacy, often at the forefront of facing external threats.
"""
human = race("human", humanDescription, 1, 1, 1, 1)
races[human.name] = human

elfDescription = """Elves: Gifted with an innate connection to nature and magic, Elves are the stewards of the ancient forests.
Their agility, grace, and mastery over the arcane arts make them formidable allies against the encroaching darkness.
"""
elf = race("elf", elfDescription, 0, 0, 2, 2)
races[elf.name] = elf

dwarfDescription = """Dwarves: Deep within the mountains, the Dwarves have crafted grand underground cities filled with intricate tunnels and majestic halls.
Masters of craftsmanship and metallurgy, Dwarves provide the strength and resilience needed for the world's defense.
"""
dwarf = race("dwarf", dwarfDescription, 2, 2, 0, 0)
races[dwarf.name] = dwarf

