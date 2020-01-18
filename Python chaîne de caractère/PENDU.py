# ========== Variables ============ #

mot="matin"
mot_liste = ['_','_','_','_','_']  # caractères dans le mot.


essais = 10



# ================================= #
            # Code #

while ('_' in mot_liste) and (essais>0):
    lettre_proposee=input("entrez une lettre")

    position=0
    for lettre in mot:
        if lettre_proposee==lettre:
            mot_liste[position]=lettre
        position=position+1
    essais=essais-1




    print (mot_liste,"Il vous reste",essais,"essais")