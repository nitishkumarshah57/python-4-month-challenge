# Day 08: functions and Recursion
# Topic: The def keyword, parameter, and return

def forge_weapon(material):
    finished_item = (f"Epic {material} sword")
    return finished_item
user_ore = input("What material do you have ?")
my_weapon = forge_weapon(user_ore)
print(my_weapon)