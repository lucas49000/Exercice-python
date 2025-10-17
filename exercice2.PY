# Liste donnée
nombres = [8, 4, 6, 1, 5]

# On suppose que le plus petit est le premier élément
plus_petit = nombres[0]

# On parcourt la liste
for n in nombres:
    if n < plus_petit:
        plus_petit = n

print("Le plus petit élément est :", plus_petit)
