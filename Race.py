class race:
    def __init__(self, description, vitMod, strMod, magMod, agiMod):
        self.description = description
        self.vitMod = vitMod
        self.strMod = strMod
        self.magMod = magMod
        self.agiMod = agiMod

humanDescription = """
Humans: With their ambition and resilience, Humans have built mighty kingdoms and sprawling cities.
They are skilled in the arts of war and diplomacy, often at the forefront of facing external threats.

"""
human = race(humanDescription, 1, 1, 1, 1)

elfDescription = """
Elves: Gifted with an innate connection to nature and magic, Elves are the stewards of the ancient forests.
Their agility, grace, and mastery over the arcane arts make them formidable allies against the encroaching darkness.

"""
elf = race(elfDescription, 0, 0, 2, 2)


dwarfDescription = """
Dwarves: Deep within the mountains, the Dwarves have crafted grand underground cities filled with intricate tunnels and majestic halls.
Masters of craftsmanship and metallurgy, Dwarves provide the strength and resilience needed for the world's defense.
"""
dwarf = race(dwarfDescription, 2, 2, 0, 0)

