# proměnná - města
mesta = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']

# kolekce ceny-destinaci
cena = [1000, 1100, 2000, 1500, 2300, 3400]

# oddělovací mezera
oddelovac = ('=' *80)

# vzhled
print(oddelovac)

# pozdrav
print('Welcome to the DESTINATION, place where people plan their trips')

# vzhled
print(oddelovac)

# seznam měst vs. cen (víceřádkový string)
print('''
1 - Prague	1000
2 - Wien	1100
3 - Brno	2000
4 - Svitavy	1500
5 - Zlin	2300
6 - Ostrava	3400
''')

# Vstup uživatele
jmeno = input('Zadej jméno: ')
prijmeni = input('Zadej příjmení: ')
narozeni = input('Zadej datum narození: ')
email = input('Zadej svoji emailovou adresu: ')
heslo = input('Zadej své heslo: ')

#Vstup2
zadej = int(input('Vyber destinaci: '))
destinace = mesta[zadej - 1]
penize = cena[zadej - 1]

#Vysledek
print('Děkuji za rezervaci ' + jmeno)
print('Tvoje rezervace je: ' + destinace)
print('Celková cena je: ' + str(penize))
