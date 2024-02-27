class Inventory:
    def __init__(self):
        self.items = {}
        self.equipped_items = {
            "weapon": None,
            "armor": None,
            "boots": None,
            "gloves": None,
            "hat": None,
            "necklace": None,
            "earring": None,
            "ring": None
        }
        self.item_types = {
            "weapon": ["sword", "axe"],
            "armor": ["armor"],
            "boots": ["boots"],
            "gloves": ["gloves"],
            "hat": ["hat"],
            "necklace": ["necklace"],
            "earring": ["earring"],
            "ring": ["ring"],
            "potion": ["potion"],
            "food": ["food"],
            "key": ["key"],
            "trash": ["trash"]
        }

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def use_item(self, item, quantity=1):
        if item in self.items:
            print(f"You used {quantity} {item}.")
            self.remove_item(item, quantity)
        else:
            print(f"You don't have any {item}.")

    def equip_item(self, item):
        if item in self.items:
            item_type = self.get_item_type(item)
            if item_type:
                if item_type in self.equipped_items:
                    if self.equipped_items[item_type] is not None:
                        self.unequip_item(self.equipped_items[item_type])
                    self.equipped_items[item_type] = item
                    print(f"You equipped {item}.")
                    return
                elif item_type in ["potion", "food", "key", "trash"]:
                    print(f"You cannot equip {item}.")
                    return
            else:
                print(f"{item} cannot be equipped.")
        else:
            print(f"You don't have any {item}.")

    def unequip_item(self, item):
        for item_type, equipped_item in self.equipped_items.items():
            if equipped_item == item:
                self.equipped_items[item_type] = None
                self.add_item(item)
                print(f"You unequipped {item}.")
                return
        print(f"You don't have {item} equipped.")

    def get_item_type(self, item):
        for item_type, items in self.item_types.items():
            if any(keyword in item.lower() for keyword in items):
                return item_type
        return None

# Example usage
inventory = Inventory()
inventory.add_item("Sword")
inventory.add_item("Armor")
inventory.add_item("Potion")
inventory.add_item("Key")
inventory.display_inventory()

# Equipping items
inventory.equip_item("Sword")
inventory.equip_item("Armor")
inventory.equip_item("Potion")  # Should print a message indicating potions cannot be equipped

# Unequipping items
inventory.unequip_item("Armor")
inventory.display_inventory()
