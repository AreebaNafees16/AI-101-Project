# Main function to iterate through numbers 0 to 9 and check if they are odd or even
def main():
    for i in range(10):
        if is_odd(i):  # Check if the number is odd
            print("odd")
        else:
            print("even")


# Function to determine if a given integer is odd
def is_odd(value: int):
    remainder = value % 2  # Calculate the remainder when dividing by 2
    return remainder == 1  # Return True if remainder is 1 (odd), otherwise False


# Entry point of the script
if __name__ == "__main__":
    main()