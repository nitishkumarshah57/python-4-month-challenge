# Day 06: Dictionary in Python
# Topic: Membership checking(in) and safely fetching values

vip_guests = {"Sam":5,"Arun":2,"Aditya":10,"Nitish":20}
user_name = input("what is your name:").strip().title()
if user_name in vip_guests :
    print(f"Welcome Back, {user_name}! You have {vip_guests[user_name]} drink credits.")

else:
    print("Sorry, You are not on the vip list.")    

