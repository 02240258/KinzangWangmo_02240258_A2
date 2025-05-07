MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
ROWS = 8
COLUMNS = 8

class BinderManager:
    def __init__(self):
        # Dictionary to store the cards: {pokedex_number: (page, row, column)}
        self.binder = {}

    def calculate_position(self, pokedex_number):
        """
        Calculate the page, row, and column based on pokedex number.
        """
        index = pokedex_number - 1  # zero-based index
        page = index // CARDS_PER_PAGE + 1
        position_on_page = index % CARDS_PER_PAGE
        row = position_on_page // COLUMNS + 1
        column = position_on_page % COLUMNS + 1
        return page, row, column

    def add_card(self):
        try:
            pokedex_number = int(input("Enter Pokedex number: "))
            if not 1 <= pokedex_number <= MAX_POKEDEX:
                print(f"Invalid Pokedex number! Must be between 1 and {MAX_POKEDEX}")
                return
            if pokedex_number in self.binder:
                page, row, col = self.binder[pokedex_number]
                print(f"Page: {page}")
                print(f"Position: Row {row}, Column {col}")
                print("Status: Pokedex number already exists in the binder.")
                return
            page, row, col = self.calculate_position(pokedex_number)
            self.binder[pokedex_number] = (page, row, col)
            print(f"Page: {page}")
            print(f"Position: Row {row}, Column {col}")
            print(f"Status: Added Pokedex #{pokedex_number} to binder")
        except ValueError:
            print("Please enter a valid number.")

    def reset_binder(self):
        print("\nWARNING: This will delete ALL Pokemon cards from the binder. This action cannot be undone.")
        confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ")
        if confirm.upper() == "CONFIRM":
            self.binder.clear()
            print("The binder reset was successful! All cards have been removed.\n")
        elif confirm.upper() == "EXIT":
            print("Returning to the main menu.\n")
        else:
            print("Invalid input. Returning to main menu.\n")

    def view_binder(self):
        if not self.binder:
            print("\nCurrent Binder Contents:\nThe binder is empty.")
        else:
            print("\nCurrent Binder Contents:")
            for number in sorted(self.binder):
                page, row, col = self.binder[number]
                print(f"Pokedex #{number}:\n  Page: {page}\n  Position: Row {row}, Column {col}")
        total_cards = len(self.binder)
        percent = (total_cards / MAX_POKEDEX) * 100
        print(f"\nTotal cards in binder: {total_cards}")
        print(f"% completion: {percent:.1f}%")
        if total_cards == MAX_POKEDEX:
            print("You have caught them all !!")
        print()

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!\n")
        while True:
            print("Select option:")
            print("1. Add a Pokemon card")
            print("2. Reset the binder")
            print("3. View current placements")
            print("4. Exit\n")
            choice = input("Select option: ")
            if choice == "1":
                self.add_card()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.view_binder()
            elif choice == "4":
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid option. Please select again.\n")

# Run the program
if __name__ == "__main__":
    manager = BinderManager()
    manager.run()
