import math # Importing the math module for mathematical operations

def main():
    # Prompt the user to input the length of side AB
    ab: float = float(input("Enter the length of AB: "))
    # Prompt the user to input the length of side AC
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse BC using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)
    # Print the calculated length of the hypotenuse
    print(f"The length of BC (the hypotenuse) is: {str(bc)}")

# Entry point of the program
if __name__ == "__main__":
    main()