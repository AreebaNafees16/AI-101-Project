import random
from hangman_visual import lives_visual_dict

lives_visual_dict = {
    0: """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========
    """,
    1: """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========
    """,
    2: """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========
    """,
    3: """
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
    """,
    4: """
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
    """,
    5: """
        +---+
        |   |
        O   |
            |
            |
            |
      =========
    """,
    6: """
        +---+
        |   |
            |
            |
            |
            |
      =========
    """,
    7: """
            
            
            
            
            
            
      =========
    """,
}

def choose_word():
    words = ["python", "developer", "hangman", "challenge", "coding", "algorithm", "jump", ""]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time!")
    
    while attempts > 0:
        print(lives_visual_dict[attempts])
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
            
    if attempts == 0:
        print(lives_visual_dict[attempts])
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()






