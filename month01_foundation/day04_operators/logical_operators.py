# Day 04: operators in python
# Topic : logical operators (and, or, not)

motion_detected = input("is motion detected : ")
owner_home = input("is owner home : ")
motion_detected = "yes"
owner_home = "yes"
trigger_alarm = motion_detected and not owner_home
print("alarm triggered :" , trigger_alarm)