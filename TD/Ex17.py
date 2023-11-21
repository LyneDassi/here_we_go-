liste = [17, 38, 10, 25, 72]
#triez et affichez la liste
liste.sort()
print(liste)

#ajoutez l’élément 12 à la liste et affichez la liste
liste.append(12)
print(liste)

#renversez et affichez la liste
liste.sort(reverse = True)
print(liste)

#affichez l’indice de l’élément 17
print("L'indice de l'element 17 est de : ", liste.index(17))

#enlevez l’élément 38 et affichez la liste
liste.pop(liste.index(38))
print(liste)

#affichez la sous-liste du 2eau 3eélément
print(liste[1:3])

#affichez la sous-liste du début au 2eélément
print(liste[0:2])

#affichez la sous-liste du 3eélément à la fin de la liste
print(liste[2:])

#affichez la sous-liste complète de la liste
print(liste[:])

#affichez le dernier élément en utilisant un indiçage négatif
print(liste[-1])