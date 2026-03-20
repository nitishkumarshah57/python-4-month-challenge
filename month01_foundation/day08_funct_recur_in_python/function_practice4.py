# Day 08: function and recursion:
# Topic: passing dictionaries into functions and using multiple 

def get_weakness(monster_name,database):
    if monster_name in database:
        return database[monster_name]
    else:
        return("unknown entity")

game_monster  = {"Goblin":"Fire","Troll":"Acid","Ice dragon":"Fire"}
user_input = input("what monster are you targeting:").title()
monster_weakness = get_weakness(user_input,game_monster) 
print(f"Target weakness:{monster_weakness}")   