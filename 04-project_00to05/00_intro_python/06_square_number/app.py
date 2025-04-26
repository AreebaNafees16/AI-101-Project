# This program calculates the square of a given number

def main():
    # Prompt the user to input a number and convert it to a float
    num: float = float(input("Type a number to for its square: "))
    
    # Calculate the square of the number and print the result
    print(f"{str(num)} square is {str(num**2)}")


# Entry point of the program
if __name__ == "__main__":
    main()