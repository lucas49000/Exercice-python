# Ex5 - exemple avec une matrice 2x2
matrix = [
    [10, 20],
    [30, 40]
]

rows = len(matrix)
cols = len(matrix[0])  # pour une matrice carrée rows == cols

for i in range(rows):            # i = indice de ligne (0..rows-1)
    for j in range(cols):        # j = indice de colonne (0..cols-1)
        value = matrix[i][j]
        # si on veut afficher en comptage humain (ligne 1,2 ...), on ajoute +1
        print(f"Ligne {i+1}, Colonne {j+1} -> valeur = {value}")
