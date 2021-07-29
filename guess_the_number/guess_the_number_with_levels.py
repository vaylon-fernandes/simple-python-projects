#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo 

print(logo) 

# select a random number

random_number = random.randint(1, 100)
guesses = [0]

print("I'm thinking of a number between 1-100.Can you guess it?")

level = input("Choose level: type 'easy' or 'hard' -> ")
easy_level = level == "easy"
hard_level = level == "hard"

while True:
   
    if easy_level: 
      max_attempts = 10
    
    if hard_level: 
      max_attempts = 5 

    number_of_guesses = len(guesses) - 1
    attempts_left = max_attempts - number_of_guesses

    print(f"Attempts Left: {attempts_left}")
    guess = input("What is your guess?: ")
    invalid_entry = not guess.isdigit()

    if invalid_entry:
        print("Invalid Entry")
        print("You must only enter a number between 1-100")
        continue
    
    guess = int(guess)

    guess_out_of_range = guess < 1 or guess > 100
    if guess_out_of_range:
        print("Please enter a number between 1-100")
        continue

    correct_guess = random_number == guess
    if correct_guess:
        print(
            f'Congratulations you guessed the number!!!! It took you {number_of_guesses} guesses')
        break

    guesses.append(guess)

    current_guess_difference = abs(random_number-guess)
    previous_guess_difference = abs(random_number-guesses[-2])
    print(guesses[-2])
    # for the first guess there will be two items in the list
    # 0 at index:0, one guess at index 1
    # Hence getting the item using index -2, will return the value 0, which evaluates to false in this case,
    # and evaluate to True in all other cases

    not_first_guess = guesses[-2]
    if not_first_guess:
        getting_close = current_guess_difference < previous_guess_difference
        if getting_close:
            print('Warmer')
        else:
            print('Colder')
    else:
        guess_is_close = current_guess_difference <= 10
        if guess_is_close:
            print('Warm')
        else:
            print('Cold')
    
    attempts_left -= 1 

    attempts_over = attempts_left == 0 
    if attempts_over: 
      print(f"You are out of attempts! The correct number was {random_number}")
      break 
    
