# function(2, 3)  # = 0.28
# function(5, -5)  # = nie mozna dzielic przez 0

a = float(input('Podaj wartosc a: '))
b = float(input('Podaj wartosc b: '))


def function1(a, b):

    try:
        result = float(((a ** 2 + b) / ((a + b) ** 2)))
        print((f'({a} ** 2 + {b}) / (({a} + {b}) ** 2) = {result}'))
    except ZeroDivisionError:
        print(f'Error, U are dividing by zero!')


function1(a, b)

'''

Obliczyc wartosc wyrazenia((a^2+b)/((a+b)^2)) wartosci wczytywane z klawiatury
a i b to float
zabezpieczyc przed - i 0

'''
