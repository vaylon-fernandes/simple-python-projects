print("Welcome to the temperature conversion app\n")

farenheit = float(input("Enter temperature in Farenheits: "))

celsius = (farenheit - 32)*(5/9)
kelvin  = (celsius + 273.15)

celsius = round(celsius,4)
kelvin = round(kelvin,4)

print("Temperature in Farenheits: ",farenheit)
print("Temperature in Celsius:    ",celsius)
print("Temperature in Kelvin:     ",kelvin)
