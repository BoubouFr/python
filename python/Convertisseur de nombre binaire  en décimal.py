# fonction conversion binaire to decimal
# converti une liste de int valant 0 ou 1 en decimal
#
def bin2dec(liste):
    liste.reverse()
    nombre =0
    poids=1
    for nbrliste in liste:
        if nbrliste == 1:
            nombre =nombre + poids
        poids=poids*2
    return nombre


liste=[1,0,1,1,1,1]
print (liste)
print(bin2dec(liste))

