def is_even(num):
    return True if num%2==0 else False

print('Welcome to the odd or even number checker app')

end=False
while not end:
    num=int(input('Which number did you have in mind?: '))
    if is_even(num):
        print('Thats an even number.')
    else:
        print('Thats an odd number.')
    
    run_again=input('Have another number? (Y/N)').upper()
    
    if run_again=='N':
        print('Bye. Hope to see you again.')
        end=True