name = input("Enter your name:")
print("Hello," + name + "!")
prompt = "\nWould you like to watch a movie? (yes/no):"
response = input(prompt)
if response.lower() =="yes":
    print("Great! Let's get started.")
    prompt = "\nWhat is your favorite movie genre? (action,comedy,drama):"
    genre = input(prompt)
    if genre.lower() == "action":
        print("you might like fast and furious")
    elif genre.lower() == 'comedy':
         print("you might like the new released blockbuster south movie 'mad square'")
    elif genre.lower() == 'drama':
         print("you might like the new released movie ' Premalu'")
# Ask for the user's age    
    prompt = "\nWhat is your age?"
    prompt += "\n(Enter a number your age):"
    age = int(input(prompt)) # Get the user's age as input
# Determine the ticket price based on age
    if age < 3:
        print("Ticket is free")
    elif 3 <= age <= 12:
        print("Ticket is $10.")
    elif 13 <= age <= 60:
        print("Ticket is $15.")
    else:
        print("Ticket is $12.")

