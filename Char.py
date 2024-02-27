class RPGCharacter:
    def __init__(self, name, race, character_class, health, attack_damage, defense):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.health = health
        self.attack_damage = attack_damage
        self.defense = defense

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nClass: {self.character_class}\nHealth: {self.health}\nAttack: {self.attack_damage}\nDefense: {self.defense}"

player = RPGCharacter("Gjarle", health=10)

def create_character():
    print("Character Creation")
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    character_class = input("Enter character class: ")
    health = int(input("Enter health points: "))
    attack_damage = int(input("Enter attack damage: "))
    defense = int(input("Enter defense points: "))

    new_character = RPGCharacter(name, race, character_class, health, attack_damage, defense)
    return new_character

# Example usage
player = create_character()
print("\nCharacter Created:\n", player)