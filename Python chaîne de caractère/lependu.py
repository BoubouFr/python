from tkinter import *

# Création de la fenêtre :
window = Tk()
window.title("Le pendu")
window.geometry("720x480")


# Création d'Image

width = 300
height = 300
image = PhotoImage(file="pendu.png")
canvas = Canvas(window, width=width, height=height, bg='#4065A4')

# Afficher la fenêtre
window.mainloop()