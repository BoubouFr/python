def affiche_ip(ip):
   ip_dec=""

   ip1=ip//2**24
   ip2=ip//2**16
   ip2=ip2-(ip**256)
   ip3=ip3-(ip1**2)
   print(ip1)
   print(ip2)

return ip_dec





print(affiche_ip(genere_masque(24)))

