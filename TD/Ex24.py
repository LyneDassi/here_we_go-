def montant_HT():
    tva = 19.6
    ttc = 5500
    mht = ttc/(1+tva/100)
    return mht


if __name__ == '__main__':
    print(montant_HT())