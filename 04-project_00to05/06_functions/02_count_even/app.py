# Function to count the number of even integers in a list
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            count += 1

    # Print the count of even numbers
    print(f"There are {count} even numbers in the given numbers")


# Function to get a list of integers from the user
def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":  # Continue until the user presses enter
        lst.append(int(user_input))  # Convert input to integer and add to the list
        user_input = input("Enter an integer or press enter to stop: ")

    return lst  # Return the list of integers


# Main function to execute the program
def main():
    lst = get_list_of_ints()  # Get the list of integers from the user
    count_even(lst)  # Count and display the number of even integers


# Entry point of the program
if __name__ == "__main__":
    main()