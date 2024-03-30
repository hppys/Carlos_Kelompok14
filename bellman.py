class Cinema:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [[False for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seating(self):
        print("Current seating arrangement:")
        for row in range(self.rows):
            for seat in range(self.seats_per_row):
                if self.seats[row][seat]:
                    print("X", end=" ")  # Seat taken
                else:
                    print("_", end=" ")  # Seat available
            print()  # Newline after each row
        print()  # Empty line after displaying seating arrangement

    def book_seat(self, row, seat):
        if 0 <= row < self.rows and 0 <= seat < self.seats_per_row:
            if not self.seats[row][seat]:
                self.seats[row][seat] = True
                print(f"Seat at row {row + 1}, seat {seat + 1} is booked successfully.")
            else:
                print("Sorry, that seat is already taken.")
        else:
            print("Invalid row or seat number.")

def main():
    cinema = Cinema(5, 10)
    cinema.display_seating()

    while True:
        print("1. Display seating arrangement")
        print("2. Book a seat")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            cinema.display_seating()
        elif choice == "2":
            row = int(input("Enter row number: ")) - 1
            seat = int(input("Enter seat number: ")) - 1
            cinema.book_seat(row, seat)
        elif choice == "3":
            print("Thank you for using our system. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
