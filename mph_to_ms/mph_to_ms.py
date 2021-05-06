print("Welocome to the MPH to MPS conversion app\n")
'''
conversion
1 mile = 1.6093 km
1 km = 1000 m
1 mile = 1,609.3 m
1 hr = 60 min * 60 secs = 3600 secs
multiplying factor = 1,609.3/3600 = 0.447027778
'''

speed_mph = float(input('Enter your speed in Miles per Hour (mph): '))

speed_mps = speed_mph*0.4470277778

rounded_speed = round(speed_mps, 2)
print(f'Your speed is {rounded_speed} m/s')
