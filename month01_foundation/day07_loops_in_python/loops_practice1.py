# Day 07: loops in python
# Topic: while loops, comparison operator(!=), and input

secret_pin = "1234"
user_guess = ""
while user_guess != secret_pin:
    user_guess = input("enter your 4 digit pin:")
print("Access Granted ! vault opened.")     