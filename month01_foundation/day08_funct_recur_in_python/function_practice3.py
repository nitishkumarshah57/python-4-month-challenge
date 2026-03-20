# Day 08: function and recursion
# Topic: Passing lists into functions and using for loops inside functions.

def calculate_damage(combo_hits):
    total_damage = 0
    for hit in combo_hits:
        total_damage += hit
    return total_damage 

player_combo = [15,20,35,50]
final_damage = calculate_damage(player_combo)
print(f"combo executed ! Total Damage:{final_damage}")   