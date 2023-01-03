"""
guideline :
Composantes connexes d'un graphe

Défintion:
Une partie A C G d'un graphe est appelée composante connexe, si pour tout couple de sommets (u,v) de A, il
existe un chemin de u à v. Un graphe est dit connexe lorsqu'il a une unique composante connexe.

Application:
Considérons une photo prise à la verticale d'un dé sur une table. On veut déterminer facilement le nombre de
points sur lą face exposée. Pour cela, on réduit le nombre de couleurs de l'image avec un seuil de niveau de
gis pour obtenir une image en noir et blanc, de façon que chaque point du dé corresponde à une composante conuexe.

On considère une grille de n x m pixels de valeurs 1 (pour coder la couleur blanche) et 0 (pour coder la couleur
noire). Cette grille sera implémentée par une liste de listes grille.
Ainsi grille[i] [j] a pour valeur 1 si le pixel codé est blanc, 0 si le pixel codé est noir.

Algorithme par un parcours en profondeur :
Pour en profondeur partant d'un sommet u explore tous les sommets atteignables depuis u et seulement
eux, donc exactement la composante connexe contenant u. On utilise le numéro de la composante courante
comme marque de visite.
1. Écrire une fonction dfs_grille récursive prenant en arguments la liste de listes grille, deux entiers i
et j tels que grille[i][j] est le sommet de départ d'un graphe, marque est le numéro de la composante
connexe de couleur noire en-cours d'étude et libre est la couleur du pixel à marquer (0 ou 1).
Cette fonction ne retourne rien mais modife grille[i][j] lorsque grille[i][j] code un pixel noir par
le numéro de la composante connexe en cours d'étude. Ce numéro est un entier de valeur minimale 2.

sources :
- https://fr.wikipedia.org/wiki/Graphe_connexe
- https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur
"""

from PIL import Image
import requests

def lien(n):
    return f"https://irem.univ-rouen.fr/sites/irem.univ-rouen.fr/files/groupes/Images_Mentales_et_TICE/jean-luc.de-seegner%40ac-rouen.fr/Programmation_au_college/D6_-_{n}.png"

def dfs_grille(grille, i, j, marque, libre = 0):
    grille[i][j] = marque
    for n_i in range(i-1,i+2):
        for n_j in range(j-1,j+2):
            if grille[n_i][n_j] == libre:
                dfs_grille(grille, n_i, n_j, marque, libre)

def nbre_comp_connexes(grille, libre):
    marque = 1
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == libre:
                marque += 1
                dfs_grille(grille, i, j, marque, libre)
    return marque - 1

for n in range(1,7):
    with open("des.png","wb") as file:
        r = requests.get(lien(n))
        while not r.ok:
            r = requests.get(lien(n))
        file.write(r.content)

    image = Image.open("des.png")
    px = image.load()

    grille = []
    for i in range(image.size[0]):
        grille.append([])
        for j in range(image.size[1]):
            if sum(px[i,j])/3 < 125:
                grille[-1].append(0)
            else:
                grille[-1].append(1)
                
    print(n, nbre_comp_connexes(grille, 0))
