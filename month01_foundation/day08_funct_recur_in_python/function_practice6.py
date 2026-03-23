# Day 08: function and recursion
# Topic: recursion with return values(math)

def spell_power(level):
    if level == 1:
        return 1
    else: 
        return level*spell_power(level - 1)
damage = spell_power(5)   
print(f"A level 5 spell deals {damage} damage !")