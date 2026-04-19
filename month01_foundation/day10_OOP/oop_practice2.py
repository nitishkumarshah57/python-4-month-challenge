# day 10: oop
# Topic: class methods(function inside a class ) and modifying self attributes

class Hero:
    def __init__(self, hero_name):
        self.name = hero_name
        self.hp = 100
        self.gold = 50

    def take_damage(self, damage_amount):
        self.hp -= damage_amount
        print(f"{self.name} took {damage_amount} damage! HP is now {self.hp}.")

    def heal(self, heal_amount):
        self.hp += heal_amount
        # Fix: Indented to live safely inside the heal method
        print(f"{self.name} healed for {heal_amount}! HP is now {self.hp}.")
player1 = Hero("Nitish")
player1.take_damage(30)
player1.heal(10)