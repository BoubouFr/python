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


def table2() : # On crée une fonction
    print("table de multiplication par 2") # On affiche le texte de la table de 2
    for j in range (21) : # jusqu'à 21 ( Attention 21 comprend le 0)
        a=j*2
        print(j,"*2=",a) # On affiche sa table de multiplication
    return

table2() # On ferme la fonction

