import temperature as temp

def displayMenu():
    print('The convert temperature program')
    print('MENU')
    print('1. F to C')
    print('2. C to F')
def convertTemp():
    option = int(input('Enter a menu option: '))
    if option == 1:
        f = int(input('Enter degrees in F: '))
        c = temp.toCelsius(f)
        c = round(c, 2)
        print('Degrees Celsius: ', c)
    elif option == 2:
        c = int(input('Enter degrees in C: '))
        f = temp.toFahrenheit(c)
        f = round(f, 2)
        print('Degrees Fahrenheit: ', f)
def main():
    displayMenu()
    again = 'y'
    while again.lower() == 'y':
        convertTemp()
        print()
        again = input('Convert another temperature? (y/n) ')

if __name__ == '__main__':
    main()
