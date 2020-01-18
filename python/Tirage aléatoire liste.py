from random import * # L'ordinateur va choisir un nombre au hasard.
liste=[] # On crée les boules grâce à une liste.
for i in range(50): #  On crée une boucle de boules jusqu'a  49 ( 49 boules).
    liste.append(i) # On ajoute une boule dans la boucle.
shuffle(liste) # L'ordinateur va mélanger la liste.
choice(liste) # L'ordinateur va choisir un l'ordre aléatoire.
print(liste[-5:]) # L'ordinateur va afficher l'ordre de la liste aléatoire.