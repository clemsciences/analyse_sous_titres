# -*-coding:utf-8-*-
__author__ = 'Clément'

import os
import nltk
from nltk.text import Text
import re
filename = "prometheus_sous_titres_neerlandais.txt"

with open(filename, "r") as f:

    texte_complet = f.readlines()
#lignes_texte = [texte_complet[i] for i in range(1, len(texte_complet)) if "-->" in texte_complet[i-1] and texte_complet[i+1] == "\n"]
lignes_texte = []
for i in range(1, len(texte_complet)):
    if "-->" in texte_complet[i-1] and texte_complet[i+1] == "\n":
        lignes_texte.append(texte_complet[i])
    elif "-->" in texte_complet[i-1] and texte_complet[i+2] == "\n":
        lignes_texte.extend(texte_complet[i:i+2])
        
#pour isoler le texte, je suippose que le texte voulu est entre "...-->..." et "\n"
print texte_complet[5:10]

print lignes_texte[5:10]
for i in range(len(lignes_texte)):
    lignes_texte[i] = lignes_texte[i].replace("<i>", "").replace("<b>", "").replace("</i>", "").replace("</b>", "").decode('utf8')

texte = " ".join(lignes_texte)
mots = nltk.word_tokenize(texte)
mots = [mot.lower() for mot in mots]
le_texte = Text(mots)
freq = nltk.FreqDist(le_texte)
print freq.most_common(300)

with open("vocabulaire_neerlandais_prometheus.txt", "w") as f:
    for couple in freq.most_common(5000):
        f.write((couple[0]+"\n").encode('utf8'))


with open("clean_"+filename, "w") as f:
    texte = "".join(lignes_texte)
    f.write(texte.encode('utf8'))
