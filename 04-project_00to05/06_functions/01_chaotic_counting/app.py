import random

# The likelihood (out of 10) that the counting will stop at any given step
DONE_LIKELIHOOD = 8


def chaotic_counting():
    """
    Counts from 1 to 10, but may stop prematurely based on a random condition.
    """
    for i in range(10):
        curr_num = i + 1
        if done():  # Check if the counting should stop
            return
        print(curr_num)  # Print the current number


def done():
    """
    Determines whether the counting should stop based on a random number.
    Returns True if the random number exceeds the DONE_LIKELIHOOD, otherwise False.
    """
    if random.randint(1, 10) > DONE_LIKELIHOOD:
        return True
    return False


def main():
    """
    Main function to execute the chaotic counting process.
    """
    print(
        "I'm going to count until 10 or until I feel like stopping, whichever comes first."
    )
    chaotic_counting()
    print("I'm done")


if __name__ == "__main__":
    main()