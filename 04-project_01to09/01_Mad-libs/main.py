# def mad_libs():
#     print("Welcome to Mad Libs! Fill in the blanks to create a fun story.")
    
#     noun1 = input("Enter a noun (e.g., car, apple, house): ")
#     noun2 = input("Enter another noun (e.g., book, phone, tree): ")
#     verb1 = input("Enter a verb (e.g., run, jump, swim): ")
#     verb2 = input("Enter another verb (e.g., sing, dance, write): ")
#     adjective1 = input("Enter an adjective (e.g., happy, blue, tall): ")
#     adjective2 = input("Enter another adjective (e.g., shiny, rough, strong): ")
#     adverb = input("Enter an adverb (e.g., quickly, loudly, carefully): ")
#     place = input("Enter a place: ")
#     person = input("Enter a person's name: ")
#     animal = input("Enter an animal: ")
    
#     story = f"One day, {person} was walking through {place} when they saw a {adjective1} {animal}. The {animal} decided to {verb1} {adverb}, which made {person} laugh. \
#     Nearby, a {adjective2} {noun1} was trying to {verb2} a {noun2}, but it was too difficult. Everyone watching had a great time!"
    
#     print("\nHere is your Mad Libs story:")
#     print(story)
    
# if __name__ == "__main__":
#     mad_libs()


def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create a fun story.")
    
    noun1 = input("Enter a noun (e.g., car, apple, house): ")
    noun2 = input("Enter another noun (e.g., book, phone, tree): ")
    verb1 = input("Enter a verb (e.g., run, jump, swim): ")
    verb2 = input("Enter another verb (e.g., sing, dance, write): ")
    verb3 = input("Enter one more verb (e.g., eat, fly, climb): ")
    adjective1 = input("Enter an adjective (e.g., happy, blue, tall): ")
    adjective2 = input("Enter another adjective (e.g., shiny, rough, strong): ")
    adjective3 = input("Enter one more adjective (e.g., smelly, gigantic, funny): ")
    adverb = input("Enter an adverb (e.g., quickly, loudly, carefully): ")
    adverb2 = input("Enter another adverb (e.g., lazily, silently, awkwardly): ")
    place = input("Enter a place: ")
    person = input("Enter a person's name: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    emotion = input("Enter an emotion (e.g., happy, sad, excited): ")
    
    story = f"One day, {person} was walking through {place} when they saw a {adjective1} {animal} sitting on top of a {adjective2} {noun1}. \
    The {animal} suddenly decided to {verb1} {adverb}, knocking over a giant stack of {noun2}. \
    Just then, a {adjective3} squirrel appeared out of nowhere and started to {verb2} {adverb2}, making everyone in the area burst into laughter. \
    Nearby, a group of tourists were trying to {verb3} while eating {food}, but they were so distracted by the chaos that they fell over. \
    {person} couldn't stop laughing, and by the end of the day, they felt extremely {emotion}. It was truly a day to remember!"
    
    print("\nHere is your Mad Libs story:")
    print(story)
    
if __name__ == "__main__":
    mad_libs()
