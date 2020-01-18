def genere_masque(cidr):
    masque = 0
    for i in range (cidr):
        masque = masque + 2** (31-i)
        return masque

print(hex(genere_masque(16)))