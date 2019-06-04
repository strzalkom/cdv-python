# zmienne globalne i lokalne

# precyzja
x = "{0:.3f}".format(5)
print(x)  # 5.000


'''
napisz funkcje, ktora jako argument przyjmuje wartosc zlotych i zamienia
dane po kursie dzisiejszym franka. Wyswietl uzytkownikowi ile frankow
kupic za podana kwote
'''


def kantor(kwota):
    kursChf = 3.81849933
    # iloscChf = kwota / kursChf
    # iloscChf = "{0:.0f}".format(iloscChf)
    iloscChf = kwota // kursChf
    print(f'Ilosc CHF: {iloscChf}')
    # zaokragla w dol


kantor(500)


# zmienna globalna
zmiennaGlobal = 10
print(f'Wartosc zmiennej globalnej: {zmiennaGlobal}')
print(f'Id zmiennej globalnej: {id(zmiennaGlobal)}')


def spr():
    global zmiennaGlobal
    zmiennaGlobal = 20
    print(f'\nWartosc zmiennej globalnej wewnatrz funkcji:{zmiennaGlobal}')
    print(f'\nId zmiennej globalnej wewnatrz funkcji:{id(zmiennaGlobal)}')


spr()

print(f'\nWartosc zmiennej globalnej wewnatrz funkcji:{zmiennaGlobal}')
print(f'\nId zmiennej globalnej wewnatrz funkcji:{id(zmiennaGlobal)}')
