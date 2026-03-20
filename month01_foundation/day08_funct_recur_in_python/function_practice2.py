# Day 08: function and recursion
# Topic: multiple parameter and internal logic(if/else)

def check_entry(age,is_vip):
    if is_vip is True:
        return True
    elif age >= 18 :
        return True
    else:
        return False
person1 = check_entry(20,False)
person2 = check_entry(16,True)
person3 = check_entry(15,False) 
print(person1)
print(person2)
print(person3)
