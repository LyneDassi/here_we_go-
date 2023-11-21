def somme():

    m = int(input('Entrez un entier non nul'))
    som = 0
    for i in range(1, m+1):
        som = som + i**5
    print("Somme= ", som)


if __name__ == '__main__':
    somme()