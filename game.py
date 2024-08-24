import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

def get_choice(player_num):
    while True:
        try:
            choice = int(input(f"Player {player_num}, enter your choice (1, 2, or 3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_choice_name(choice, choice_mapping):
    return choice_mapping[choice - 1]

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "DRAW"
    if (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 1):
        return 'Paper'
    if (choice1 == 1 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
        return 'Rock'
    if (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 2):
        return 'Scissors'

while True:
    mode = input("Choose mode: 1 - Player vs Computer, 2 - Player vs Player: ")
    if mode == '1':
        print("Player vs Computer mode selected.")
        player_choice = get_choice(1)
        choice_mapping = ['Rock', 'Paper', 'Scissors']
        player_choice_name = get_choice_name(player_choice, choice_mapping)
        
        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice, choice_mapping)

        print(f'Player choice: {player_choice_name}')
        print(f'Computer choice: {comp_choice_name}')

        result = determine_winner(player_choice, comp_choice)

        if result == "DRAW":
            print("It's a tie!")
        elif result == player_choice_name:
            print("Player wins!")
        else:
            print("Computer wins!")

    elif mode == '2':
        print("Player vs Player mode selected.")
        
        choices = ['Rock', 'Paper', 'Scissors']
        choice_mapping = random.sample(choices, len(choices))
        
        player1_choice = get_choice(1)
        player2_choice = get_choice(2)
        player1_choice_name = get_choice_name(player1_choice, choice_mapping)
        player2_choice_name = get_choice_name(player2_choice, choice_mapping)

        print(f'Player 1 choice: {player1_choice_name}')
        print(f'Player 2 choice: {player2_choice_name}')

        result = determine_winner(player1_choice, player2_choice)

        if result == "DRAW":
            print("It's a tie!")
        elif result == player1_choice_name:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    else:
        print("Invalid mode selected. Please choose 1 or 2.")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!")
