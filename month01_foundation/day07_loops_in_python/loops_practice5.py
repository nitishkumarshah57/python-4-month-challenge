# Day 07: loops in python 
# Topic: The infinite loop(while True), break, continue, and if/eloif/else

balance = 100
while True:
    choice = input("Choose an option - (1) Balance, (2) Deposit, (3) Exit: ")

    if choice == "1":
        print(f"Your balance is ${balance}")
        
    elif choice == "2":
        deposit_amount = int(input("How much to deposit: "))
        balance += deposit_amount
        print("Deposit successful!")
        
    elif choice == "3":
        print("Goodbye!")
        break  
        
    else:
        print("Invalid choice.")
        continue                   
