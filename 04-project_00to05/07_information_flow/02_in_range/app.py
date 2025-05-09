def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False


def main():
    # Example calls to test the function
    print(in_range(5, 1, 10))   # True
    print(in_range(0, 1, 10))   # False
    print(in_range(10, 1, 10))  # True
    print(in_range(1, 1, 10))   # True


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
