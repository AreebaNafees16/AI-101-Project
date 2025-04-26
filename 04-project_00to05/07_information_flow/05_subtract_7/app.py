def main():
    # Initialize a variable with the value 7
    num: int = 7
    # Call the subtract_seven function to subtract 7 from the variable
    num = subtract_seven(num)
    # Print the result, which should be zero
    print("this should be zero: ", num)

def subtract_seven(num):
    # Subtract 7 from the input number and return the result
    num = num - 7
    return num

# Entry point of the program
if __name__ == '__main__':
    main()