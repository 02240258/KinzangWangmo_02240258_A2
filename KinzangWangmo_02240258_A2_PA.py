import random
import KinzangWangmo_02240258_A2_PB as pb

class GuessNumberGame:
    def __init__(self):
        self.score = 0

    def play(self):
        print("\nGuess the Number Game")
        number = random.randint(1, 10)
        tries = 0

        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                tries += 1
                if 1 <= guess <= 10:
                    if guess == number:
                        print("Correct! You guessed it.")
                        break
                    else:
                        print("Wrong guess. Try again.")
                else:
                    print("Please guess a number within the range 1 to 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            except KeyboardInterrupt:
                print("\nGame interrupted. Returning to the main menu.")
                return

        score = max(0, 10 - tries)
        self.score += score
        print("You scored:", score)


class RockPaperScissorsGame:
    def __init__(self):
        self.score = 0

    def play(self):
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
            self.score += 1
        else:
            print("You lose.")


class TriviaGame:
    def __init__(self):
        self.score = 0

    def play(self):
        print("\nTrivia Game")

        print("Question 1: What is the capital of France?")
        print("1. London  2. Berlin  3. Paris  4. Madrid")
        answer1 = input("Your answer: ")
        if answer1 == "3":
            print("Correct.")
            self.score += 1
        else:
            print("Incorrect.")

        print("Question 2: Which planet is known as the Red Planet?")
        print("1. Earth  2. Mars  3. Venus  4. Jupiter")
        answer2 = input("Your answer: ")
        if answer2 == "2":
            print("Correct.")
            self.score += 1
        else:
            print("Incorrect.")


class PokemonBinderManagerWrapper:
    def __init__(self):
        self.binder_manager = pb.BinderManager()

    def manage(self):
        print("\n--- Pokemon Card Binder Manager ---")
        while True:
            print("\nMenu:")
            print("1. Add a Pokemon card")
            print("2. Reset the binder")
            print("3. View current placements")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.binder_manager.add_card()
            elif choice == "2":
                self.binder_manager.reset_binder()
            elif choice == "3":
                self.binder_manager.view_binder()
            elif choice == "4":
                print("Exiting Pokemon Card Binder Manager. Returning to main menu.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


class GameHub:
    def __init__(self):
        self.guess_game = GuessNumberGame()
        self.rps_game = RockPaperScissorsGame()
        self.trivia_game = TriviaGame()
        self.binder_manager = PokemonBinderManagerWrapper()

    def show_scores(self):
        print("\nOverall Scores")
        print("Guess Number Game:", self.guess_game.score)
        print("Rock Paper Scissors:", self.rps_game.score)
        print("Trivia Game:", self.trivia_game.score)

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
                self.guess_game.play()
            elif choice == "2":
                self.rps_game.play()
            elif choice == "3":
                self.trivia_game.play()
            elif choice == "4":
                self.binder_manager.manage()
            elif choice == "5":
                self.show_scores()
            elif choice == "0":
                print("Goodbye! Thanks for playing.")
                break
            else:
                print("Invalid choice. Please enter a number from 0 to 5.")


if __name__ == "__main__":
    hub = GameHub()
    hub.main_menu()
