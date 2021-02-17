
print('welcome  to the letter counter app')

name = input('Enter your name: ').title()

print(f'Welcome {name}. We will count the number of occurences of a letter in a sentence/message for you.')

message = input('Enter a message:')
to_count = input('which letter do you want to count the occurences of ?: ')

count = message.count(to_count) + message.count(to_count.upper())

print(f"There are {count} {to_count}'s in your message.")


