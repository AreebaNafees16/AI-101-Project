def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    lower_bound = 1
    upper_bound = 10
    
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    while True:
        try:
            secret_number = int(input(f"{player1}, enter a number between {lower_bound} and {upper_bound} for {player2} to guess (hidden input recommended): "))
            if secret_number < lower_bound or secret_number > upper_bound:
                print(f"Please enter a number within the range {lower_bound}-{upper_bound}.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("\n" * 50)  # Clear the screen to hide the number
    print(f"{player2}, it's your turn to guess!")
    attempts = 0
    
    while True:
        try:
            user_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1
            
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please enter a number within the range {lower_bound}-{upper_bound}.")
                continue
            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations, {player2}! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
