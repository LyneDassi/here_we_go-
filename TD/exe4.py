def saisiefiltree():
    while True:
        try:
            n = int(input('Entrez un nombre compris entre 1 et 10 '))
            if 1 <= n <= 10:
                return n
            else:
                print("Entrez un nombre compris dans l'interval 1 et 10")
        except ValueError:
            print('Entrez un entier svp')


n = saisiefiltree()
print('n= ', n)
