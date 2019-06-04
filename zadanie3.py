a = float(input('Wprowadz wartosc a: '))
b = float(input('Wprowadz wartosc b: '))


def nwd(a, b):

    while b > 0:
        c = a % b
        a = b
        b = c
    return a


x = nwd(a, b)
print(f'NWD {a} oraz {b} wynosi {x}')
