# Day 06: Dictionary in Python 
# Topic: Dictionaries inside Dictionaries, chained keys and if/elif/else

player = {"name":"Hero",
          "stats":{"hp":100, "mana":50},
          "equipments":{"weapon":"iron sword", "armor":"leather vest"}}
user_menu = input("What menu would you like to open ? (stats/equipments):").strip().lower()

if user_menu == "stats":
    print(player["stats"]["hp"])
    print(player["stats"]["mana"])
elif user_menu == "equipments":
    print(player["equipments"]["weapon"])
    print(player["equipments"]["armor"])
else:
    print("invalid menu option")    