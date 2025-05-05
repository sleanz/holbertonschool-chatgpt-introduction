#!/usr/bin/python3
import sys

# Afficher tous les arguments sauf le nom du fichier Python
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
