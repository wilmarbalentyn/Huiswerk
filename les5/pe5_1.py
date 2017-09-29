def table():
    for i in range(-30, 50, 10):
        print('{} {:30} '.format(convert(i), (i)))

def convert(_celsius):
    _fahrenheit = (_celsius * 1.8) + 32
    return(_fahrenheit)

celsius = float(input('Wat is de celsius: '))
fahrenheit = convert(celsius)

print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius, fahrenheit))

table()