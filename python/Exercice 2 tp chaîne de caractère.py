a="Essaie de deviner ou est la lettre e " # chaîne de caractère
letter="e"
i=0

while i<len(a):
    if a[i] == letter:
         print("e est présent au caractère n°", i+1) # Si il y a le caractère e afficher "e est présent au caractère n°"
    else:
        print("e est absent au caractère n°", i+1) # Sinon afficher " e est absent au caractère n° "
    i=i+1