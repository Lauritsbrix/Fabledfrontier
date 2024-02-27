class RPGClass:
    def __init__(self, description, vitMod, strMod, magMod, agiMod):
        self.description= ""
        self.vitMod= vitMod
        self.strMod= strMod
        self.magMod= magMod
        self.agiMod= agiMod


warriorDescription ="Masters of melee combat, Warriors charge into battle with robust armor,\nabsorbing blows and delivering devastating strikes—a symbol of unyielding strength and courage."
mageDescription = "Wielding arcane powers, Mages command the elements and cast spells from a distance,\nmanipulating reality with ancient knowledge and unleashing powerful magical forces."
archerDesription = "Masters of precision, Archers excel in ranged combat,\nexpertly wielding bows to strike from a distance with unmatched accuracy and agility on the Fabled Frontier."

Mage = RPGClass(mageDescription, 0,0,3,0)
Warrior = RPGClass(warriorDescription, 2,1,0,0)
Archer = RPGClass(archerDesription, 0,0,0,3)

