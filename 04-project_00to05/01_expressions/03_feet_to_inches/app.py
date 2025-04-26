# Constant representing the number of inches in a foot
INCHES_IN_FOOT: int = 12

# Main function to convert feet to inches
def main():
    # Prompt the user to enter the number of feet
    feet: float = float(input("Enter number of feet: "))
    
    # Calculate the equivalent number of inches
    inches: float = feet * INCHES_IN_FOOT
    
    # Display the result to the user
    print("That is", inches, "inches!")

# Entry point of the program
if __name__ == "__main__":
    main()