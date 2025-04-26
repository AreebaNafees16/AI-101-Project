import random

# Number of sides on each die
NUM_SIDES = 6

# Function to simulate rolling two dice
def roll_dice():
    # Generate random numbers for each die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    # Calculate the total of the two dice
    total: int = die1 + die2
    # Print the total
    print("Total of two dice:", total)

# Main function to demonstrate dice rolling
def main():
    # Local variable die1 in main()
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    # Call roll_dice() three times
    roll_dice()
    roll_dice()
    roll_dice()
    # Print the value of die1 in main() after calling roll_dice()
    print("die1 in main() is: " + str(die1))

# Entry point of the program
if __name__ == "__main__":
    main()