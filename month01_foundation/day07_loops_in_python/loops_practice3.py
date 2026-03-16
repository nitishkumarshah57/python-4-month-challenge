# Day 07: loops in python
# Topic: looping through lists, if/else logic, and .append()

scores = [45,85,92,30,71,15,100]
passed = []
failed = []
for score in scores:
    if score >= 50:
        passed.append(score)
    else:
        failed.append(score)

print(passed)
print(failed)            