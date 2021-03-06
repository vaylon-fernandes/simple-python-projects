from random import choice

choices = ["Rock", "Paper", "Scissor"]

computer = choice(choices)

play_game = True
while play_game:
    player_input = input('Enter "Rock", "Paper" or "Scissor": ').title()

    if player_input not in choices:
        print("Invalid Entry. Please check your spelling")
        continue
    elif player_input == computer:
        print('Game Tied')
    elif player_input == "Rock":
        if computer == "Scissor":
            print(f"Player wins. {player_input} smashes {computer}")
        else:
            print(f"Computer wins. {computer} covers {player_input}")
    elif player_input == "Paper":
        if computer == "Rock":
            print(f"Player wins. {player_input} covers {computer}")
        else:
            print(f"Computer wins. {computer} cuts {player_input}")
    elif player_input == "Scissor":
        if computer == "Paper":
            print(f"Player wins. {player_input} cuts {computer}")
        else:
            print(f"Computer wins. {computer} smashes {player_input}")

    play_again = input("Do you want to play again? Enter (Y/N): ").upper()

    run_again = play_again == "Y"
    if run_again:
        computer = choice(choices)
    else:
        print("Bye. Hope to see you again")
        play_game = False
