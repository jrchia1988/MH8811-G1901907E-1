def convert_fahrenheit(temp):
    return (float(temp)*1.8 + 32)

c=input('Pls enter temperature in Celsius:')

print('The temperate in Faherenheit is {}'.format(convert_fahrenheit(c)))
