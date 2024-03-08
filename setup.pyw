# Créé par louis.charles, le 08/03/2024 en Python 3.7
import time
import os
import tkinter
import tkinter.messagebox
file = open("requirements.txt", "w")
file.write("time, tkinter, random, string, tkinter.ttk, base64") # ecrire dans le fichier requirement.txt
file.close()
time.sleep(3) # attendre 3 s
cmd = "pip install -r requirements.txt" # executer une commande dans le cmd
os.system(cmd)
tkinter.messagebox.showinfo('Setup_ProjetNSI','Installation des modules nécessaire au fonctionnement du programme effectuer ') # fais une fenêtre popup pour signaler que l'execution du programme est finis