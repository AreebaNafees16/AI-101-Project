import random
import string

print("Welcome To Your Password Generator")

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#~$=*%&^~"
    return ''.join(random.choice(characters) for _ in range(length))

# Get user input
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("How long should each password be? "))

# Generate and display passwords
for i in range(num_passwords):
    print(f"Password {i + 1}: {generate_password(password_length)}")
