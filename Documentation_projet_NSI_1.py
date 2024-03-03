#####################################
#   Générateur de mot de passe      #
#####################################

import base64

import time
from tkinter import *
import random
import string
from tkinter.ttk import *
"""
L'importation de modules utiles
au bon fonctionnement du programme
"""
# from PIL import Image, ImageTk


root = Tk()
root.geometry("410x285")
root.title("Générateur de mot de passe")
root.resizable(width=False, height=False)
"""
La fonction 'root' permet de parametrer la fenêtre
'root.geometry' permet de dimensionner la fenêtre
'root.title' permet de nommmer la fenêtre
'root.resizable' evite la redimension de la fenêtre
"""

##### INITIAL VARIABLES
title = StringVar()
choice = IntVar()
choicesettings = IntVar()
choicesettings_decode = IntVar()
lengthlabel = StringVar()
passlength = IntVar()
symbols = "!§$%&/()=?{[]}*+'#~,;.:-_'<>"
"""
Des variables permettant de changer le texte,
de choisir le type de mots de passes,
de choisir les paramètres,
le choix du type d'encodage et de décodage

"""
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advanced = poor + average + symbols

"""
Niveau de complexité des mots de passes
"""

# PHOTO GUI
# photo = PhotoImage(file =r"assets/images.png")


##### FUNCTIONS MAIN WINDOW

def selection():
    choice.get()
"""
fonction qui crée une zone de sélection/bouton
du niveau de complexité du mot de passe
"""

def selectionsettings_decode():
    choicesettings_decode.get()
"""
fonction qui crée une zone de sélection/bouton
de choix de parametre dans le 'Menu'
"""

def callback():
    Isum.config(text=passgen())

    print("mot de passe généré : " + Isum.cget("text"))


Isum = Label(root, text="")
Isum.pack(side=BOTTOM)

password = str(callback)
print("password :" + password)
"""
Génération du mot de passe 
"""

def savefile():
    # Fonction qui définis l'encodage du code par 2 choix : 1 & 2
    # 0 ----> Sauvegarder dans le fichier sans encodage
    # 1 ----> Sauvegarder dans le fichier avec encodage : Base64
    if choicesettings.get() == 0:
        fichier = open("password.txt", "w")
        fichier.write(Isum.cget("text") + "| | | Mot de passe généré sans options")
        fichier.close()
    elif choicesettings.get() == 1:
        fichier = open("password.txt", "wb")
        data = Isum.cget("text")
        encoded = base64.b64encode(data.encode())
        fichier.write(encoded)
        fichier.close()
"""
Fonction qui permet de générer le mot de passe
brut ou de l'encoder dans un fichier 
"""

# Password generation script - joins a" random symbol to the string for how many times set in the spinbox
def passgen():
    # Pré paramètre de la fonction :
    # difficulté : poor / average / advanced (Fonctions définis dans le début de code : InitalVariable)
    # Longueur du mot de passe : 8-24
    # Assemblage du mot de passe avec le module "random"
    global password
    # Création de la variable utilisé dans tous le programme pour afficher / récupéré ou crée la suite de charactere qui fera le mot de passe
    password = ""
    if choice.get() == 1:
        return password.join(random.sample(poor, passlength.get()))

"""
Le choix 1 est le premier niveau de complexité de mot de passe
avec seulement des lettres majuscules et minuscules
"""
    elif choice.get() == 2:
        return password.join(random.sample(average, passlength.get()))
"""
Le choix 2 permet d'ajouter des chiffres
"""
    elif choice.get() == 3:
        return password.join(random.sample(advanced, passlength.get()))
"""
Le choix 3 est le plus complexe des mot de passe avec:
des lettres majuscules et minuscules, des chiffres et des symboles
"""

# Copies the current password to the clipboard
def copytoclipboard():
    global password
    print(password)

    Isum.clipboard_clear()
    Isum.clipboard_append(Isum.cget("text"))
    Isum.update()
    print("Mot de passe copié dans le presse papier.")
"""
Cette fonction permet de copier le mot de passe généré dans le presse papier
"""

def change_text(txt):
    text.delete(0, END)
    text.insert(0, txt)
"""
Cette fonction permet d'effacer et de créer un nouveau mot de passe
qui remplace le précedent
"""

def decodetext():
    if choicesettings_decode.get() == 0:
        data_to_decode = text.get()
        decoded = base64.b64decode(data_to_decode).decode()
        Isum.config(text=decoded)
        print("Isum.config(text=decoded : ", Isum.config(text=decoded),")")  # LOG
    elif choicesettings_decode.get() == 1:
        pass
"""
Cette fonction decode la base 64 si un encodage à été choisi
"""

def create():
    global win
    ####
    win = Toplevel(root)
    win.geometry("250x125")
    win.title("Préférences d'utilisation")
    win.resizable(width=False, height=False)
    ####
    labelencode = Label(win, text="Type d'encodage :")
    labelencode.pack()
    R1Settings = Radiobutton(win, text="Sans encodage", variable=choicesettings, value=0,
                             command=selectionsettings).pack(anchor=CENTER)
    R2Settings = Radiobutton(win, text="Base64", variable=choicesettings, value=1, command=selectionsettings).pack(
        anchor=CENTER)

    ####
    labelencode = Label(win, text="Algorithme de décodage :")
    labelencode.pack()
    R1Settingsdecode = Radiobutton(win, text="Base64", variable=choicesettings_decode, value=0,
                                   command=selectionsettings_decode).pack(anchor=CENTER)

"""
Création de la fenêtre de réglage/préferences pour
encoder son mot de passe
"""
##### USER INTERFACE


# menu bar#
menubar = Menu(root)
root.config(menu=menubar)
menufichier = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menufichier)
menufichier.add_command(label="Préférences", command=create)
label = Label(root, textvariable=title).pack()
title.set("Type de mot de passe:")
"""
Création de l'interface pour l'utilisateur
"""
# conditions du mot de passe
R1 = Radiobutton(root, text="Majuscule & Minuscules", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Majuscule & Minuscules & chiffres", variable=choice, value=2, command=selection).pack(
    anchor=CENTER)
R3 = Radiobutton(root, text="Majuscule & Minuscules & chiffres & Symboles", variable=choice, value=3,
                 command=selection).pack(
    anchor=CENTER)
"""
Création des commandes de sélections de complexité de mot de passe
"""
lengthlabel.set("Longueur du mot de passe: (8-24)")
lengthtitle = Label(root, textvariable=lengthlabel).pack()

spinboxlength = Spinbox(root, from_=8, to_=24, textvariable=passlength, width=13).pack()
"""
Conditionnement de la longueur du mot de passe
"""

# BOUTONS
passgenButton = Button(root, text="Générer le mot de passe ", command=callback)
passgenButton.pack()

copyButton = Button(root, text="Copier le mot de passe au presse papier", command=copytoclipboard)
copyButton.pack(side=BOTTOM)

getpassword = Button(root, text="Decoder le mot de passe -->", command=decodetext)
getpassword.pack(side=BOTTOM)

savefilebtn = Button(root, text="Sauvegarder le mot de passe ", command=savefile)
savefilebtn.pack()
"""
Création des boutons de:
génération de mot de passe,
copie du mot de passe,
décodage du mot de passe
et sauvegarde de mot de passe
"""
# Create an Entry Widget
text = Entry(root)
text.pack()
text.place(x=120, y=185)
"""
Définition d'une zone de texte pour écrire son
propre mot de passe
"""

# Create a button to change/set the content


# SETTINGS GUI ####


def selectionsettings():
    choicesettings.get()
    print("choicesettings.get() : ", choicesettings.get())  # LOG

"""
Séléction des réglages dans le menu
"""
##END SETTINGS GUI


# btn = Button(root, text="Créer une nouvelle fenêtre", command = create)
# btn.pack(pady = 10)



# Lancement de la fenêtre principale
root.mainloop()
"""
ouverture de la fenêtre principale
"""
