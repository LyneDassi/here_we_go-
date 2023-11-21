def chaine():
    chaine = str(input('entrez une chaine de caractere'))
    print('chaine: ', chaine)
    for c in chaine:
        print(c)

    liste = list(input("Entrez des elements d'une liste"))
    print("Liste: ", liste)
    for li in liste:
        print(li)


if __name__ == '__main__':
    chaine()