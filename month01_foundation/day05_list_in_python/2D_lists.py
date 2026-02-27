# Day 05: list in python
# Topic : 2D lists(lists inside lists), if/else, indexing & input
cinema = [
    ["0","0","0"],
    ["0","x","0"],
    ["x","x","0"]
]
row_number = int(input("enter the row number(0-2):"))
seat_number = int(input("enter the seat number(0-2):"))
if cinema[row_number][seat_number] == "x":
              print("Sorry,that seat is already taken!"  )
else:
        cinema[row_number][seat_number] = "x"
        print("Seat Successfully Booked!")
        print(f"Updated Cinema:{cinema}")