'''Uzytkownik podaje z klawiatury
marka, model, pojemnosc, predkoscMax
utworz funkcje ktora pobierze dane od uzytkownika i przypisze do slownika
utworz druga funkcje wyswietlajaca dane w formacie
Marka:
Model:
Pojemnosc:
Predkosc maks:
'''


print("\n Wpisz 4 parametry samochodu : ")

dane = {
    'marka': input('\nPodaj marke samochodu '),
    'model': input('\nPodaj model samochodu '),
    'pojemnosc': input('\nPodaj pojemnosc samochodu '),
    'predkoscMax': input('\nPodaj predkoscMax ')
}
print(dane)

samochod = {
    'marka': 'VW',
    'model': 'Golf',
    'pojemnosc': 5,
    'predkoscMax': 150
}

print(samochod)
