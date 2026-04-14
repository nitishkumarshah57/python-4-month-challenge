# day 10: oop
# Topic: Defining a class, the __init__ method and instantiating an object

class Hero:
    def __init__(self,hero_name):
        self.name = hero_name
        self.hp = 100
        self.gold = 50
user_input = input("enter your hero:") 
player1 = Hero(user_input)
print(f"A new hero name {player1.name} has arrived with {player1.hp} HP !")       