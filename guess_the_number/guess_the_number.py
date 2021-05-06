import random
# select a random number
random_number = random.randint(1, 100)
guesses = [0]

print("I'm thinking of a number between 1-100.Can you guess it?")
while True:
    guess = input("What is your guess?: ")
    invalid_entry = not guess.isdigit()

    if invalid_entry:
        print("Invalid Entry")
        print("You must only enter a number between 1-100")
        continue

    guess = int(guess)
    number_of_guesses = len(guesses)

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

    # for the first guess there will be two items in the list
    # 0 at index:0, one guess at index 1
    # Hence getting the item using index -2, will return the value 0, which evaluates to false in this case,
    # and evaluate to false in all other cases
    first_guess = guesses[-2]
    if first_guess:
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
