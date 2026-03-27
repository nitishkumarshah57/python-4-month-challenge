# day 09: file input and output in python 
# Topic: writing a file using "w" mode, variables and input

guest_name = input("please enter your name for the guestbook:")
with open("guestbook.txt","w") as file:
    file.write(guest_name)
print("Guestbook saved successfully !")    