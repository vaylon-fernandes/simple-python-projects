def check_input(word):
    if word.isdigit():
        print("ENTER A WORD NOT A NUMBER!!!!")
    else:
        return word


def is_pallindrome(word):
    return word == word[::-1]


print("Welcome To the Pallindrome Checker APP")

while True:
    user_input = input("Enter a word")

    if is_pallindrome(user_input):
        print(f"The word {user_input} is a pallindrome!!!")
    else:
        print(f"The word {user_input} is not a pallindrome...")

    check_another = input("Do you want to check another word? (Y/N)").upper()

    run_again = True if check_another == "Y" else False

    if run_again:
        continue
    else:
        print("Bye! Hope to see you again")
        break
