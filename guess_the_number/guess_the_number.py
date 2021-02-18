import random
# select a random number
random_number=random.randint(0, 100)
guesses=[0]

while True:
    guess=int(input("I'm thinking of a number between 1-100.Can you guess it?\nWhat is your guess?: "))
    number_of_guesses=len(guesses)
    if random_number==guess:
        print(f'Congratulations you guessed the number!!!! It took you {number_of_guesses} guesses')
        break
    guesses.append(guess)
    
    current_guess_difference=abs(random_number-guess)
    previous_guess_difference=abs(random_number-guesses[-2])
    
    if guesses[-2]:
        if current_guess_difference<previous_guess_difference:
            print('Warmer')
        else:
            print('Colder')
    else:
        if current_guess_difference<=10:
            print('Warm')
        else:
            print('Cold')