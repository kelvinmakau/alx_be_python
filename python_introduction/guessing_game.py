import random

def guess_the_number_game():
    print("🎯 Welcome to the Guess the Number Game!")
    
    while True:
        secret_number = random.randint(1, 10)
        guess_count = 0
        guessed_correctly = False

        while not guessed_correctly:
            try:
                guess = int(input("\nEnter your guess (1 to 10): "))
                guess_count += 1

                match guess:
                    case _ if guess == secret_number:
                        print(f"🎉 Congratulations, you guessed it! The number was {secret_number}.")
                        print(f"🔢 You took {guess_count} guess(es).")
                        guessed_correctly = True
                    case _ if guess > secret_number:
                        print("📈 Oops, your guess is a bit high. Try again!")
                    case _ if guess < secret_number:
                        print("📉 Nope, your guess is a bit low. Give it another shot!")
            except ValueError:
                print("⚠️ Please enter a valid number!")

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! See you next time.")
            break

# Run the game
guess_the_number_game()
