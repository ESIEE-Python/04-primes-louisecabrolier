"""
ce fichier permet de vérifier si un nombre est un nombre premier
"""

import math as m

#### Fonction secondaire


def isprime(p):
    """
    entrée:un entier p
    sortie:un bouléen qui dit si l'entier p est un nombre premier ou non
    """
    if p<=3:
        return True
    premier=True
    for d in range(2,1+int(m.sqrt(p))):
        if p%d==0:
            premier=False
            break
    return premier


#### Fonction principale


def main():
    # vos appels à la fonction secondaire ici
    """
    entrée: 
    sortie:
    but: appeler la fonction isprime
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
