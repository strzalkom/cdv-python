def witaj():
	print('Witaj!', end= ' ')
	print('Janusz')

	witaj()

	def wyswietlWiek(wiek):
	print(f'Twoj wiek: {wiek}')
	wyswietlWiek(23)

	def iloczyn(a,b):
		return a*b
	print(iloczyn(3,4))

	def iloraz(a,b):
		return a/b
	x = iloraz(4,5)
	print(f'Iloraz wynosi: {x}')
	print(type(x))

	'''Uzytkownik podaje z klawiatury
	marka, model, pojemnosc, predkoscMax
	utworz funkcje ktora pobierze dane od uzytkownika i przypisze do slownika
	utworz druga funkcje wyswietlajaca dane w formacie
	Marka:
	Model:
	Pojemnosc:
	Predkosc maks:
	'''
