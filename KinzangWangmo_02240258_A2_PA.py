import random

class GameHub:
    def __init__(self):
        self.guess_score = 0
        self.rps_score = 0
        self.trivia_score = 0
        self.binder = []

    def guess_number_game(self):
        print("\nGuess the Number Game")
        number = random.randint(1, 10)
        tries = 0

        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                tries += 1
                if guess == number:
                    print("Correct! You guessed it.")
                    break
                else:
                    print("Wrong guess. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        score = max(0, 10 - tries)
        self.guess_score += score
        print("You scored:", score)

    def rock_paper_scissors_game(self):
        print("\nRock Paper Scissors Game")
        options = ["rock", "paper", "scissors"]
        computer = random.choice(options)
        
        user = input("Choose rock, paper or scissors: ").lower()
        if user not in options:
            print("Invalid choice.")
            return
        
        print("Computer chose:", computer)
        if user == computer:
            print("It's a tie.")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
            self.rps_score += 1
        else:
            print("You lose.")

    def trivia_game(self):
        print("\nTrivia Game")

        print("Question 1: What is the capital of France?")
        print("1. London  2. Berlin  3. Paris  4. Madrid")
        answer1 = input("Your answer: ")
        if answer1 == "3":
            print("Correct.")
            self.trivia_score += 1
        else:
            print("Incorrect.")

        print("Question 2: Which planet is known as the Red Planet?")
        print("1. Earth  2. Mars  3. Venus  4. Jupiter")
        answer2 = input("Your answer: ")
        if answer2 == "2":
            print("Correct.")
            self.trivia_score += 1
        else:
            print("Incorrect.")

    def pokemon_binder_manager(self):
        while True:
            print("\nPokemon Binder Manager")
            print("1. Add card")
            print("2. Reset binder")
            print("3. View binder")
            print("4. Go back to main menu")

            choice = input("Enter choice: ")
            if choice == "1":
                name = input("Enter card name: ")
                self.binder.append(name)
                print("Card added.")
            elif choice == "2":
                self.binder.clear()
                print("Binder reset.")
            elif choice == "3":
                if not self.binder:
                    print("Binder is empty.")
                else:
                    print("Cards in binder:")
                    for card in self.binder:
                        print("-", card)
            elif choice == "4":
                break
            else:
                print("Invalid option.")

    def show_scores(self):
        print("\nOverall Scores")
        print("Guess Number Game:", self.guess_score)
        print("Rock Paper Scissors:", self.rps_score)
        print("Trivia Game:", self.trivia_score)

    def main_menu(self):
        while True:
            print("\nGame Hub Menu")
            print("1. Guess Number Game")
            print("2. Rock Paper Scissors")
            print("3. Trivia Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Show Overall Scores")
            print("0. Exit")

            choice = input("Enter your choice (0-5): ")

            if choice == "1":
                self.guess_number_game()
            elif choice == "2":
                self.rock_paper_scissors_game()
            elif choice == "3":
                self.trivia_game()
            elif choice == "4":
                self.pokemon_binder_manager()
            elif choice == "5":
                self.show_scores()
            elif choice == "0":
                print("Goodbye! Thanks for playing.")
                break
            else:
                print("Invalid choice. Please enter a number from 0 to 5.")

# Run the program
if __name__ == "__main__":
    hub = GameHub()
    hub.main_menu()
