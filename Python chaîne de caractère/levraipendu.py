# ========== Variables ============ #
letter_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # On stocke les variables dans une liste

guessed = False  # Le mot a été trouvé

spaces = ""      # Blanks
mot_chance = []  # Placeholder
mot_chars = []  # caractères dans le mot.

mot = ""      # le mot deviné.
max_guess = None # Les chances maximum pour réussir.
cur_guess = 0 # Nombre actuel de chance c'est-à-dire 0.


# ================================= #
            # Code #

def findOccurences(s, ch):
       return [i for i, letter in enumerate(s) if letter == ch]

print("Bienvenue au jeu du pendu")

mot = input("Entrez un mot ").lower()
max_guess = int(input("Chances_maximum "))

for character in mot:
       mot_chars.append(character)
       if (character != " "):
           spaces += "_ "
           mot_chance.append("-")
       else:
           spaces += ("  ")
           mot_chance.append("  ")

print("\n" * 50)

print("Vous êtes maintenant prêt à jouer.")

print("Word: %s. " % (spaces))
while (cur_guess < max_guess) and guessed == False:
       if (mot.split() == (''.join(mot_chance)).split()):
           guessed = True
           print("Vous avez trouvez le mot")
           break;

       lettre_chance = input("SVP entrez vos lettres ").lower()
       if (len(lettre_chance) == 1):
           if (lettre_chance not in letter_bank):
               print("Vous avez dejà utilisez cette lettre") # L'afficher si une lettre a dejà été utilisée.
           else:
               if (lettre_chance in mot_chars):
                   print("%s est pas dans le mot" % lettre_chance)
                   letter_bank.remove(lettre_chance)
                   for each in findOccurences(mot, lettre_chance):
                       mot_chance[each] = lettre_chance
                   print(''.join(mot_chance))
               else:
                   print(''.join(mot_chance))
                   print("%s est pas dans le mot" % lettre_chance)
                   letter_bank.remove(lettre_chance)
                   cur_guess += 1
       else:
           if (lettre_chance == mot):
               print("Vous avez trouvé finalement le mot")
           else:
               print("Vous avez perdu")
               break;