# przekazywanie argumentow przez referencje (firma snp poland suchy las szuk )
def show(name):
    print(f'Przed modyfikacja: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Id po modyfikacji: {id(name)}')


data = ['Anna', 'Agnieszka', 'Andrzej']
print(f'Przed wywolaniem funkcji show: {data}')
print(f'Id obiektu show: {id(data)}')
print()
show(data)
print(f'Po wywolaniu funkcji show: {data}')


# słownik
print('Słownik: ')
data1 = {0: 'Artur', 1: 'Andrzej'}
print(f'Id przed modyfikacja: {id(data1)}')
show(data1)


# przekazywanie argumentow przez wartosc
print('\n\n')


def show1(city):
    print(f'Przed modyfikacja: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    print(f'Po modyfikacji: {city}')
    print(f'Id po modyfikacji: {id(city)}')


miasto = ['Gniezno', 'Poznan']


print(f'Przed wywolaniem funkcji show1", {miasto}')
print(f'Id po modyfikacji show1" {id(miasto)}')
show1(list(miasto))
print(f'Po wywolaniu funkcji show1:  {miasto}')


# Słownik
miasto1 = {
    0: 'Gniezno',
    1: 'Poznań'
}

print(f'\n\nPrzed wywolaniem funkcji show1" {miasto1}')
print(f'Id miasto show1 {id(miasto1)}')
show1(dict(miasto1))
print(f'Po wywolaniu funkcji show1: {miasto1}')


# try except


def div(x, y):
    try:
        result = x / y
        print(f'{x} / {y} = {result}')
    except ZeroDivisionError:
        print('Error, you are dividing by zero!')


div(2, 0)
div(2, 5)
