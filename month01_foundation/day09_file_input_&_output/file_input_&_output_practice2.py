# day 09: file input and output in python
# Topic: Reading files using "r" mode and the .read() method

with open("guestbook.txt","r") as file :
    saved_name = file.read()
print("Reading guestbook....")
print(f"welcome back to the hotel,{saved_name}!")    