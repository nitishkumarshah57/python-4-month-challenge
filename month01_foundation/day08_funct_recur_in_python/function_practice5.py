# Day 08: function and recursion 
# Topic: recursion(a function calling itself)

def countdown(number):
    if number <= 0:
        print("liftoff !")
        return
    else:
        print(number)

    countdown(number - 1)
countdown(5)        
