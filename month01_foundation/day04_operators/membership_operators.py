# Day 04: operators in python
# Topic : membership operators(in,not in )
vip_list = "Nitish, Alice, Bob, Charlie, Danny"
banned_list = "Charlie, Danny"
user_name = input("enter your name:")
clean_name = user_name.strip().title()
is_vip = clean_name in vip_list
is_not_banned = clean_name not in banned_list
access_granted = is_vip and is_not_banned
print(f" Is VIP : {is_vip}")
print(f"Is Not Banned : {is_not_banned}")
print(f" Access Granted : {access_granted}")