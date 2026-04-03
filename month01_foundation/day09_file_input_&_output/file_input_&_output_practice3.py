# day 09: file input and output in python 
# Topic: Append mode("a"), the newline character(\n),and while loops

with open("captains_log.txt","a") as file:
    while True:
        log_entry = input("enter log entry(or type 'stop' to finish):")
        if log_entry == "stop":
            break
        else:
            file.write(log_entry + "\n")
print("captain's log saved")            
