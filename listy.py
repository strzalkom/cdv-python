programowanie = ['Python', 'C#', 'JS', 'PHP', 'Java']
print(programowanie)
print(type(programowanie))
pierwszy = programowanie[0]
print('Pierwszy jezyk programowania: ' + pierwszy)

trzyElementy = programowanie[0:3]
print('Trzy jezyki programowania: ', trzyElementy)

ostatniElement= programowanie[-1]
print('Ostatni jezyk programowania: ',ostatniElement)

#dodanie nowego elementu do listy
programowanie.append('Python')
print(programowanie)

#zliczanie elementow w liscie
ile = programowanie.count('Python')
print(f'Python wystepuje {ile} razy')

#ilosc elementow w liscie
iloscElem = len(programowanie)
print ('\nIlosc elementow w liscie: ')
print (iloscElem)

#laczenie list
print(f'\n\n{programowanie}')
inneJezyki = ['c', 'c++']
print('Polaczenie list')
programowanie.extend(inneJezyki)
print(programowanie)

#wyczyszczenie listy
nowa = programowanie
print(f'Nowa lista: {nowa} ')
nowa.clear()
print(f'Nowa lista po wyczyszczeniu: {nowa} ')
print(f'lista programowanie po wyczyszczeniu: {programowanie} ')
