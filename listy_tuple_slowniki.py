#listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile = programowanie.count('PHP')
print(f'Ile razy jest PHP: {ile}')

#tuple
imiona = ('Julia', 'Anna', 'Tomek')
print(imiona)
print(type(imiona))
#w tuple dodajemy nawiasy () nie da sie modyfikowac liste tak. Tuple sa szybsze niz listy. Listy w []
pierwszy = imiona[0]
print(pierwszy)

#slowniki
osoba = {
	'imie': 'Julia',
	'nazwisko': 'Kowalska',
	'wiek':23
}

print(osoba)
print(type(osoba))
print(osoba['imie'])
print(osoba.keys())
print(osoba.get('wzrost', 'brak danych dla wzrostu'))

#slownik
#utworzyc slownik i przypisac mu trzy imiona z klawiatury Imie1:... Imie2:...

print("\n Podaj trzy imiona: ")

imie = {
	'Imie1': input('\nPodaj pierwsze imie: '),
	'Imie2': input('\nPodaj drugie imie '),
	'Imie3': input('\nPodaj trzecie imie ')
}

print(imie)
