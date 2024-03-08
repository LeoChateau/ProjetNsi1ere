#!/bin/bash

# Installation de Python 3
sudo apt install python3
echo "Installation de Python 3 terminée."

# Installation de pip pour Python 3
sudo apt install python3-pip
echo "Installation de pip pour Python 3 terminée."

# Installation des modules Python avec pip
sudo pip3 install time tkinter random string tkinter.ttk
echo "Modules Python installés."

# Finis
read -p "Appuyez sur Entrée pour quitter..."
