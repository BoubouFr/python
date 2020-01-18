mot="EPID" # Mot qu'on veut inverser
mot_star=""
i =0
while i < len (mot)-1:
    mot_star=mot_star+mot[i]+'*'
    i=i+1
mot_star=mot_star+mot[len(mot)-1]
print (mot_star)