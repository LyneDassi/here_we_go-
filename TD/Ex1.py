def vitesse():
    distance = 19.7
    temps = 6.892
    vitesse = round(distance / temps, 1)
    # vitesse = (d/t){0:.1f}.format(vitesse)
    print('La vitesse est de', vitesse, 'm/s')


if __name__ == '__main__':
    vitesse()

def nom_age():
    # Saisir l'age et le nom avec l'instruction input() et afficher
    nom = input('Entrez votre nom: ')
    age = int(input('Entrez votre age: '))
    print('Nom: ' + nom + '\nAge: ', age)

if __name__ == '__main__':
    nom_age()