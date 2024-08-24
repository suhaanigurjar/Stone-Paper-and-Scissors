import random


# Constants for game choices
ROCK = 1
PAPER = 2
SCISSORS = 3
CHOICES = [ROCK, PAPER, SCISSORS]
CHOICE_NAMES = ['Rock', 'Paper', 'Scissors']

def print_rules():
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
          + "Rock vs Paper -> Paper wins\n"
          + "Rock vs Scissors -> Rock wins\n"
          + "Paper vs Scissors -> Scissors wins\n")

def get_choice(player_name):
    while True:
        try:
            choice = int(input(f"{player_name}, enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): "))
            if choice in CHOICES:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(player1_choice, player2_choice):
    # Return 0 for a tie, 1 if player1 wins, and 2 if player2 (or computer) wins.
    if player1_choice == player2_choice:
        return 0
    elif (player1_choice == ROCK and player2_choice == SCISSORS) or \
         (player1_choice == PAPER and player2_choice == ROCK) or \
         (player1_choice == SCISSORS and player2_choice == PAPER):
        return 1
    else:
        return 2



def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def get_mode():
    while True:
        mode = input("Choose mode: 1 - Player vs Computer, 2 - Player vs Player: ").strip()
        if mode in ['1', '2']:
            return mode
        else:
            print("Invalid mode selected. Please choose 1 or 2.")

def play_again_menu():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Play Another Round")
        print("2. Start a New Game")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    # Declare 'mode' as global at the start of the function
    global mode

    
    # Initialize player names and scores outside the loop
    player1_name = player2_name = None
    player1_score = player2_score = 0

    while True:
        # If starting a new game, get the mode and reset scores
        if player1_name is None or player2_name is None:
            mode = get_mode()
            player1_name = input("Enter Player 1's name: ")
            player2_name = input("Enter Player 2's name: ") if mode == '2' else "Computer"
            player1_score = 0
            player2_score = 0
        print_rules()
        

        player1_choice = get_choice(player1_name)

    

        player2_choice = get_choice(player2_name) if mode == '2' else random.choice(CHOICES)

        print(f'{player1_name} choice: {CHOICE_NAMES[player1_choice - 1]}')
        print(f'{player2_name} choice: {CHOICE_NAMES[player2_choice - 1]}')

        result = determine_winner(player1_choice, player2_choice)

        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{player1_name} wins with {CHOICE_NAMES[player1_choice - 1]}!")
            player1_score += 1
        else:
            print(f"{player2_name} wins with {CHOICE_NAMES[player2_choice - 1]}!")
            player2_score += 1

        print(f"Score: {player1_name} {player1_score} - {player2_score} {player2_name}")

        
        # Show the menu after the round
        menu_choice = play_again_menu()

        if menu_choice == 1:
            continue  # Play another round with the same settings
        elif menu_choice == 2:
            player1_name = player2_name = None  # Reset names and scores
        elif menu_choice == 3:
            break  # Exit the game

    print("Thanks for playing!")

while True:
    play_game()
    break
