def main():
    # Anton's age is given as 21
    anton: int = 21

    # Beth's age is 6 years older than Anton's age
    beth: int = 6 + anton

    # Chen's age is 20 years older than Beth's age
    chen: int = 20 + beth

    # Drew's age is the sum of Chen's and Anton's ages
    drew: int = chen + anton

    # Ethan's age is the same as Chen's age
    ethan: int = chen

    # Print the ages of all individuals
    print("Anton is " + str(anton) + " years old.")
    print("Beth is " + str(beth) + " years old.")
    print("Chen is " + str(chen) + " years old.")
    print("Drew is " + str(drew) + " years old.")
    print("Ethan is " + str(ethan) + " years old.")


if __name__ == "__main__":
    main()