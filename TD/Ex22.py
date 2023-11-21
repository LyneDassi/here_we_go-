A = int(input('Entrez une annee A'))
if A % 4 == 0 and A % 100 != 0:
    print("L'annee est bissextile")
elif A % 400 == 0:
    print("L'annee est bissextile")
else:
    print("L'annee n'est pas bissextile")