import random

def rock_paper_scissors():
    print("\033[1;34mWelcome to Rock, Paper, Scissors! ✊✋✌️\033[0m")
    
    player1 = input("\033[1;32mEnter your name: \033[0m")
    choices = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
    
    while True:
        print("\n\033[1;33mOptions: rock ✊, paper ✋, scissors ✌️\033[0m")
        p1_choice = input(f"\033[1;32m{player1}, enter your choice: \033[0m").lower()
        
        if p1_choice not in choices:
            print("\033[1;31mInvalid choice! Please select rock, paper, or scissors.\033[0m")
            continue
        
        p2_choice = random.choice(list(choices.keys()))
        print(f"\n{player1} chose {choices[p1_choice]} ({p1_choice})")
        print(f"Computer chose {choices[p2_choice]} ({p2_choice})")
        
        if p1_choice == p2_choice:
            print("\033[1;35mIt's a tie! 🤝\033[0m")
        elif (p1_choice == "rock" and p2_choice == "scissors") or \
             (p1_choice == "paper" and p2_choice == "rock") or \
             (p1_choice == "scissors" and p2_choice == "paper"):
            print(f"\033[1;32m{player1} wins! 🎉\033[0m")
        else:
            print("\033[1;36mComputer wins! 🤖🎉\033[0m")
        
        play_again = input("\033[1;34mDo you want to play again? (yes/no): \033[0m").lower()
        if play_again != "yes":
            print("\033[1;31mThanks for playing! 👋\033[0m")
            break

if __name__ == "__main__":
    rock_paper_scissors()
