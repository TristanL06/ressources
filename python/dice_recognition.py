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
