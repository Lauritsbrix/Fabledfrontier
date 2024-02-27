class Inventory:
    def __init__(self):
        self.items = {}

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
            # Implement usage logic here
            print(f"You used {quantity} {item}.")
            self.remove_item(item, quantity)
        else:
            print(f"You don't have any {item}.")

    def equip_item(self, item):
        if item in self.items:
            # Implement equip logic here
            print(f"You equipped {item}.")
        else:
            print(f"You don't have any {item}.")

# Example usage
inventory = Inventory()
inventory.add_item("Sword")
inventory.add_item("Potion", 5)
inventory.display_inventory()

# Using and equipping items
inventory.use_item("Potion")
inventory.equip_item("Sword")
inventory.display_inventory()
