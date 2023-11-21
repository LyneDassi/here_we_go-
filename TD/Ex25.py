try:
    n = int(input('Saisissez un nombre'))
    if n % 2 != 0:
        print('Le nombre est impair')
    else:
        print('Le nombre est pair')
except ValueError:
    print('Veuillez entrer un entier valide')