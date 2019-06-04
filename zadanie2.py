a = float(input('Podaj wartosc a: '))
b = float(input('Podaj wartosc b: '))
c = float(input('Podaj wartosc c: '))


def funkcja2(a, b, c):

    try:
        if c > 0:
            result1 = float(a ** 2 + b)
            print(f'({a} ** 2 + {b}) = {result1}')
        if c < 0:
            result2 = float(a - (b ** 2))
            print(f'({a} - ({b} ** 2)) = {result2}')
        if c == 0:
            result3 = float(1 / (a - b))
            print(f'(1 / ({a} - {b})) = {result3}')
    except ZeroDivisionError:
        print('Nie mozna dzielic przez 0!')


funkcja2(a, b, c)
