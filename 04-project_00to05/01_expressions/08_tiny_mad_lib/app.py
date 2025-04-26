# Define the starting part of the sentence as a constant string
SENTENCE_START: str = (
    "Panaversity is fun. I learned to program and used Python to make my "
)

# Main function to execute the Mad Libs game
def main():
    # Prompt the user to input an adjective
    adjective: str = input("Please type an adjective and press enter. ")
    # Prompt the user to input a noun
    noun: str = input("Please type a noun and press enter. ")
    # Prompt the user to input a verb
    verb: str = input("Please type a verb and press enter. ")

    # Print the completed sentence by combining the inputs with the starting sentence
    print(f"{SENTENCE_START + adjective} {noun} {verb}!.")

# Entry point of the program
if __name__ == "__main__":
    main()