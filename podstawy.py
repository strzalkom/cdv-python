print("CDV")
print(10)
#komentarz
''' komentarz w
wielu
liniach'''

#potegowanie
potega = 2 ** 10

print(potega)

print()
#pobieranie danych z klawiatury
print("Podaj imie: ")
imie = input()
#konkatenacja +
print("Twoje imie podane z klawiatury: " + imie)
print()

nazwisko = input("Podaj nazwisko: ")
print("Twoje nazwisko podane z klwaiatury: ", nazwisko)
print()
print("Twoje pełne imię i nazwisko: ", imie,nazwisko)

'''
Użytkownik podaje z klawiatury swój wiek
wyświetl dane w formacie : Twój wiek: [] lat
'''

#ctrl+shift przenoszenie lini
#multi kursor z ctrl
print("Podaj swój wiek: ", end="")
wiek = input()
print(type(wiek))#str
print("Twój wiek: "+wiek+ " lat")
print("Twój wiek: ",wiek, "lat")


wiek1=20
print(type(wiek1))
wiek1 =str(wiek1)
print("Twój wiek: "+wiek1+" lat")
print("Twój wiek: ",wiek1, "lat")

nazwisko1= "Kowalski"
pierwszyZnak = nazwisko1[0]
print(pierwszyZnak)
dlugosc = len(nazwisko1)
print("Długość: ", dlugosc)

ostatniZnak = nazwisko1[len(nazwisko1)-1]
print("Ostatni znak:",ostatniZnak)
ostatniZnak = nazwisko1[-1]
print("Ostatni znak: ", ostatniZnak)

#konwersja
x="5"
print(type(x)) #str
x = int(x)
print(type(x)) #int
y=10
print(type(y))#int
y = y /2
print(type(y)) #float
print(y) #5.0

#zabawa stringami
nazwisko1 = "Kowalski"
print(nazwisko1[0]) #K
print(nazwisko1[0:3]) #Kow
print(nazwisko1[-2]) #k
print(nazwisko1[-2:]) #ki
print(nazwisko1[:-2]) #Kowals
print(nazwisko1[:-2:2]) #Kwl #co drugi znak
print ()
