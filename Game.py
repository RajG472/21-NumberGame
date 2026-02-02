import random

# Function to display the game's instructions
def display_instructions():
    print("Welcome to the 21 Game!\nType 'exit' to quit the game at any time.\nYou can only pick numbers between 1 and 3.\nIf you're the person to reach exactly 21, you LOSE!\nThe goal of the game is to add numbers up to 21 in increments of 1, 2, or 3.\n")

# Function to get user input
def get_user_choice():
    while True:
        user_input = input("Enter a number (1, 2, or 3): ")
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            exit()
        try:
            choice = int(user_input)
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice! Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")

# Main game function
def play_game():
    total = 0
    display_instructions()

    while total < 21:
        # Get user's choice
        user_choice = get_user_choice()
        total += user_choice
        print("Total sum is now " + str(total))
        
        # Check if user has lost
        if total >= 21:
            print("You picked " + str(user_choice) + ". Total is " + str(total) + ". You LOSE!")
            break

        # Computer choice
        comp_choice = random.randint(1, 3)
        total += comp_choice
        print("Computer picked " + str(comp_choice))
        print("Total sum is now " + str(total))
        
        # Check if computer has lost
        if total >= 21:
            print("Total is " + str(total) + ". Computer LOSES!")
            break

# Start the game
play_game()
