inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Finding out how many items in warehouse inventory
inventory_len = len(inventory)

# Selecting first element in inventory and saving it to first
first = inventory[0]

# Selecting the last element from the inventory
last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")

inventory.sort()

inventory = sorted("twin bed")
print(inventory)

print(removed_item)

print(twin_beds)


# John Stewart | Review of Lists Python | Codecademy| 14/09/2022








