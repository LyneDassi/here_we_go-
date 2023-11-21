def racine():
    import math
    a = input('Entrez un nombre ')
    try:
        a = float(a)
        if (a >= 0) :
            print('La racine du nombre est de', math.sqrt(a))
        else :
            print('Veuillez saisir un nombre superieur ou egal a zero')
    except ValueError:
        print("Donnez un nombre valide")


if __name__ == '__main__':
    racine()


def comparaison():
    a = input('\n\nEntrez le premier mot')
    b = input('Entrez le deuxieme mot')
    pp = a if len(a) < len(b) else b
    print('Le plus petit mot est: ', pp)


if __name__ == '__main__':
    comparaison()

def seuil():
    pseuil = 2.3
    vseuil = 7.41
    pression = float(input('Saisir la pression : '))
    volume = float(input('Saisir le volume : '))
    if volume > vseuil and pression > pseuil:
        exit()
    elif pression > pseuil and volume <= vseuil:
        print("Augmenter le volume de l'enceinte")

    elif volume > vseuil and pression <= pseuil:
        print("Diminuer le volume de l'enceinte")

    else:
        print('Tout va bien')
    print('Volume = ', volume)
    print('Pression = ', pression)


if __name__ == '__main__':
    seuil()