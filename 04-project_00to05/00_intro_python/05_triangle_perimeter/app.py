def main():
    # Prompt the user to input the length of the first side of the triangle
    side1: float = float(input("What is the length of first side? "))
    
    # Prompt the user to input the length of the second side of the triangle
    side2: float = float(input("What is the length of second side? "))
    
    # Prompt the user to input the length of the third side of the triangle
    side3: float = float(input("What is the length of third side? "))

    # Calculate and display the perimeter of the triangle
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


# Entry point of the program
if __name__ == "__main__":
    main()