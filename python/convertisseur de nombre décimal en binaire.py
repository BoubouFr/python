def dec2bin(nombre):
    liste=[]
    quotient=nombre
    while quotient != 0:
          reste=quotient%2
          liste.append(reste)
          quotient= quotient//2
    liste.reverse()
    if len(liste)==0:
        liste.append(0)
    return liste

reponse=int(input('Entrez un nombre décimal'))
if reponse>=0:
    print("le code binaire  de ",reponse," est: ",dec2bin(reponse))
else:
    print("ce nombre est négatif")






