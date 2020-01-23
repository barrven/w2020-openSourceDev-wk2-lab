"""
Convert temp values
2020-1-23
"""

def toCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def toFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def main():
    for temp in range(0, 201, 40):
        print(temp, 'Fahrenheit = ', round(toCelsius(temp), 2), 'Celsius')
    for temp in range(0, 100, 80):
        print(temp, 'Celsius = ', round(toFahrenheit(temp), 2), 'Fahrenheit')
