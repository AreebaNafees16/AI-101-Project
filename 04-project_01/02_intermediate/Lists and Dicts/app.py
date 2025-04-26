def main():
    print("=== Problem #1: List Practice ===")
    # Create a list called `fruit_list`
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

    print("\n=== Problem #2: Index Game ===")
    play_game()


# Functions for Problem #2

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Index out of range."


def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Modified list: {my_list}"
    else:
        return "Index out of range."


def slice_list(my_list, start, end):
    # Handle negative or out-of-bound indices gracefully
    start = max(0, start)
    end = min(len(my_list), end)
    return f"Sliced list: {my_list[start:end]}"


def play_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']
    print("Your list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the combined program
main()
