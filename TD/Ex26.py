def divise():

    Q = int(input('Entrez un entier Q: '))
    P = int(input('Entrez un entier P: '))
    if P % Q == 0:
        print('Q divise P')
    else:
        print('Q ne divise pas P')


if __name__ == '__main__':
    divise()