import random

def puzzle_game():
    """A simple number puzzle game with multiple rounds."""
    print("=" * 50)
    print("Welcome to Number Puzzle Game!")
    print("=" * 50)
    
    score = 0
    rounds = 0
    
    while True:
        rounds += 1
        print(f"\n--- Round {rounds} ---")
        
        # Choose difficulty
        print("\nSelect difficulty:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")
        
        difficulty = input("Enter 1, 2, or 3: ").strip()
        
        if difficulty == "1":
            max_num = 50
        elif difficulty == "2":
            max_num = 100
        elif difficulty == "3":
            max_num = 200
        else:
            print("Invalid input. Setting to Easy.")
            max_num = 50
        
        # Generate random number
        secret_number = random.randint(1, max_num)
        guesses = 0
        max_guesses = 7
        
        print(f"\nI'm thinking of a number between 1 and {max_num}.")
        print(f"You have {max_guesses} tries to guess it!\n")
        
        while guesses < max_guesses:
            try:
                guess = int(input(f"Guess #{guesses + 1}: "))
                guesses += 1
                
                if guess < 1 or guess > max_num:
                    print(f"Please enter a number between 1 and {max_num}.")
                    guesses -= 1
                    continue
                
                if guess == secret_number:
                    points = max(10 - guesses, 1)
                    score += points
                    print(f"\n🎉 Correct! The number was {secret_number}!")
                    print(f"You earned {points} points! Total score: {score}")
                    break
                elif guess < secret_number:
                    print(f"Too low! Try higher. ({max_guesses - guesses} guesses left)")
                else:
                    print(f"Too high! Try lower. ({max_guesses - guesses} guesses left)")
                    
            except ValueError:
                print("Please enter a valid number.")
                guesses -= 1
        else:
            print(f"\n😢 Game Over! The number was {secret_number}.")
            print("Better luck next time!")
        
        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            break
    
    print("\n" + "=" * 50)
    print(f"Game Over! Final Score: {score}")
    print(f"Rounds Played: {rounds}")
    print("=" * 50)

if __name__ == "__main__":
    puzzle_game()
