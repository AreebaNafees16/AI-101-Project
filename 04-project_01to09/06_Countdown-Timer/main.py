import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

# User input for countdown time
try:
    seconds = int(input("Enter countdown time in seconds: "))
    countdown(seconds)
except ValueError:
    print("Please enter a valid number!")
