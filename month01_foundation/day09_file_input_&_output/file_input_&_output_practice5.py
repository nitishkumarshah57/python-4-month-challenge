# Day 09: file input and output in python
# Topic: writing Dictionaries to files, function, and .items()

def save_game(player_data):
    with open("savegame.txt","w") as file:
        for stat, value in player_data.items():
            file.write(f"{stat},{value} \n")
hero = {"Name":"Arthur","level":10,"HP":150}
save_game(hero)
print("Game saved successfully ! ")            