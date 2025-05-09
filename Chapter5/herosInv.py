# Heros Inventory

# creat a list with some items

inventory = ['sword', 'armor', 'shield', 'potion']

print("Your items: ")
for item in inventory:
    print(item)

input("\nPress Enter to continue...")

# get the length of a list
print("You have", len(inventory), "items in your possession")

input("\nPress Enter to continue...")

# test for membership
if "healing potion" in inventory:
        print("You will live to fight another day")

# display one i tem throuigh an index
index = int(input("\nEnter the index number for an item in iventory: "))

print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))

print("Inventory[", start, ":", finish, " ] is", end=" ")
print(inventory[start:finish])