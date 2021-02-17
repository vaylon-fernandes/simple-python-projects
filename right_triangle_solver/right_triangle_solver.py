from math import sqrt

print("Welcome to the right trangle solver app\n")

leg_one = float(input("Enter length of the first leg:  "))
leg_two = float(input("Enter length of the second leg: "))

#calculating hypotenuse

hypotenuse = sqrt(leg_one**2 + leg_two**2)

#calculating area

area = 0.5*leg_one*leg_two

#round results to 3 places

hypotenuse = round(hypotenuse,3)
area = round(area,3)

print(f'For a right triangle with legs of {leg_one} and {leg_two}, the hypotenuse is {hypotenuse}')

print(f'For a right triangle with legs of {leg_one} and {leg_two}, the area is {area}')
      
