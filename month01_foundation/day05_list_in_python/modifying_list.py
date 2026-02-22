# Day 05: list in python
# Topic: modifying lisgt using append
backpack = ["Sword", "Shield","Potion"]
new_item = input("name the new item found:")
backpack.append(new_item)
backpack[1]="Broken Shield"
print("Updated inventory",backpack)
print("Total item:",len(backpack))