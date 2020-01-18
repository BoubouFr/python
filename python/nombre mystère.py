#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Merwane
#
# Created:     21/09/2019
# Copyright:   (c) Merwane 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def jouer(n,var):

    if var < n : # Si n (le nombre) qu'on a choisit est inférieur au nombre mystère.

        print("trop bas") # On va afficher un message (print) comme quoi le chiffre est trop bas.
        resultat=False

    elif var == n: # Si le nombre qu'on aura choisit correspond au nombre que l'ordinateur a chosit.

        print("Bravo !") # Si le chiffre est bon la console va afficher "Bravo".
        resultat=True # On arrete le code.

    else : # Sinon

        print("trop haut") # On va afficher que le nombre qu'on aura choisit est trop haut.
        resultat=False
    return resultat





from random import *
n=randint(0, 10)  # Cette ligne nous servira à faire choisir à l'ordinateur chiffre entre 0-10(compris)
gagne=False
while gagne==False:
    var = input("Entrez un nombre") # l'affichage du texte pour insérer le chiffre
    var = int(var)
    gagne=jouer(n,var)


