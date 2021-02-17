print("Multiplication Table/Exponential Table")

name = input("Enter your Name:  ").title().strip()

num = float(input("What number would you like to work with?: "))

#multiplication Table

mul = 0
print(f"Multiplication Table for {num} is :\n")

for i in range(1,10):
    i = float(i)
    mul = i*num
    mul = round(mul,4)
    print(f"\t{i} * {num} = {mul}")
    
#Exponent table

exp = 0
print(f"\nExponent Table for {num} is :\n")
for i in range(1,10):
    exp = num**i
    exp = round(exp,4)
    print(f"\t{num} ** {i} = {exp}")
    
print(name.capitalize()+" math is cool".upper())
print(f"\t{name} math is cool")
