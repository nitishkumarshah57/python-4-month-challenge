# Day 04: operator in python
# Topic : comparison operators (>,<, ==, !=, >=, <=)

bolt_length = float(input("enter the bolt length : "))
is_perfect = bolt_length == 5.0
is_too_long = bolt_length > 5.0
is_too_short = bolt_length < 5.0
print(f"{is_perfect}, {is_too_long}, {is_too_short}")