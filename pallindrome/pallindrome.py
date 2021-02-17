def check_input(word):
    if word.isdigit():
        print("ENTER A WORD NOT A NUMBER!!!!")
    else:
        return word
    
def is_pallindrome(word):  
    return word == word[::-1]   

print("Welcome To the Pallindrome Checker APP")
user_input = input("Enter a word")

while True:
if is_pallindrome(user_input):
    print(f"The word {user_input} is a pallindrome!!!")
else:
    print(f"The word {user_input} is not a pallindrome...")
    
