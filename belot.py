#ex4
import random

dico_points_sans_atouts = {
    ""
    "7": 0,
    "8": 0,
    "9": 0,
    "V": 2,
    "D": 3,
    "R": 4,
    "d": 10,
    "A": 11
}

jeu_cartes = ["7", "8", "9", "d", "V", "D", "R", "A"] * 4

main = random.sample(jeu_cartes, k=8)

print(f"La main est {main}.\n")

total_points = 0
for carte in main:
    points = dico_points_sans_atouts[carte]
    print(f"{carte} --> {points} points")
    total_points += points

print(f"\nLe nombre total de points de la main est {total_points}.")
