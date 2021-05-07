############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random

import os

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns 
  the score calculated of the  cards """
    score = sum(cards)
    if len(cards) == 2 and score==21:
            return 0

    if (score > 21) and (11 in cards):
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare_scores(player_score, computer_score):
    """Takes the players score and 
  computer score and returns the Result"""
    if player_score == 0:
        return "You win with a Blackjack😎"

    if computer_score == 0:
        return 'Opponent wins with a Blackjack😱'

    if player_score > 21:
        return 'You went over. Opponent wins😤'

    if computer_score > 21:
        return 'Opponent went over. You win🥳'

    if player_score > computer_score:
        return 'You win.🎉'

    if player_score < computer_score:
        return 'You lose 😭'


def game_on():
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards},Current Score:{user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        there_is_a_winner_or_user_busts=user_score == 0 or computer_score == 0 or user_score > 21
        if there_is_a_winner_or_user_busts:
            game_over = True
        else:
            deal_again = input(
                "Type 'y' to get another card and 'n' to finish the game. ")
            if deal_again == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final hand: {user_cards},your final score: {user_score}")
    print(
        f"Computers Final hand: {computer_cards},Computers final score: {computer_score}"
    )

    result = compare_scores(user_score, computer_score)
    print(result)


while input('Do you want to play a game of blackjack. ').lower()=='y':
    clear_console()
    game_on()
