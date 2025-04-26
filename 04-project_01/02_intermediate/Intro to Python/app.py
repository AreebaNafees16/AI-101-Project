# Dictionary containing planets and their gravity as a percentage of Earth's gravity
planets = {
    "mercury": 37.6,
    "venus": 88.9,
    "mars": 37.8,
    "jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}

# Main function to calculate equivalent weight on another planet
def main():
    # Prompt user to input their weight on Earth
    user_input = int(input("Enter your weight in Earth: "))
    # Prompt user to input the name of a planet
    planet = input("Enter a planet: ").lower()

    # Validate the planet input until a valid planet is entered
    while planet not in planets:
        planet = input("Enter a valid planet: ").lower()

    # Calculate the equivalent weight on the selected planet
    conversion = (planets[planet] / 100) * user_input
    # Round the result to 2 decimal places
    rounded_val = round(conversion, 2)
    # Display the equivalent weight on the selected planet
    print(f"The equivalent weight on {planet} is: {rounded_val}")

# Entry point of the program
if __name__ == "__main__":
    main()