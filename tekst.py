tekst = "Anna, paweł, JulIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista)) #list

imie1 = lista[0] #Anna
print(imie1)

imieDuza = imie1.upper()
print(imieDuza) #ANNA

imieMala = imie1.lower()
print(imieMala) #anna

#sprawdzanie zawartości
nazwisko ="" #jak tu cos bedzie wpisane to true
print(nazwisko.isalpha()) #false
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true dla zawartosci false dla niczego oraz spacji

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyswietlanie lancucha znakow
#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)
new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "kwiecien"
dzien = 1
print("\nData: ", end="")
print(dzien,miesiac,rok, sep="-")
print("\nData: ", end="")
print(dzien,miesiac,rok)

s
