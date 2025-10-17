#ex1
dico_notes = {"math": 14, "programmation": 12, "anglais": 16, "biologie": 10, "sport": 19} 
somme = 0   
nb = 0
for ligne in dico_notes.values():
    somme += float(ligne)
    nb += 1
moyenne = somme / nb
print("Moyenne =", moyenne)




dico_sans_bio = dico_notes.copy()
del dico_sans_bio["biologie"]

moyenne_sans_bio = sum(dico_sans_bio.values()) / len(dico_sans_bio)
print(f"Moyenne sans biologie : {moyenne_sans_bio:.2f}")

#ex2
animaux = [("chien", 3), ("chat", 4), ("souris", 16)]

for animal, nombre in animaux:
    print(animal, nombre)

#ex3
s = {
    "Alice": {"math": (15, 4), "info": (18, 4), "anglais": (12, 2)},
    "Bob": {"math": (10, 4), "info": (14, 4), "anglais": (11, 2)},
    "Chloé": {"math": (17, 4), "info": (19, 4), "anglais": (15, 2)},
    "David": {"math": (8, 4), "info": (9, 4), "anglais": (10, 2)}
}


moyennes = {}
for nom, matieres in s.items():
    total_points = 0
    total_coeff = 0
    for note, coeff in matieres.values():
        total_points += note * coeff
        total_coeff += coeff
    moyennes[nom] = total_points / total_coeff


meilleur = max(moyennes, key=moyennes.get)

moyenne_globale = sum(moyennes.values()) / len(moyennes)


admis = {nom: moy for nom, moy in moyennes.items() if moy >= 12}

admis_tries = dict(sorted(admis.items(), key=lambda x: x[1], reverse=True))


print("Moyennes de chaque étudiant :")
for nom, moy in moyennes.items():
    print(f"  {nom} : {moy:.2f}")

print(f"\nMeilleur étudiant : {meilleur} ({moyennes[meilleur]:.2f})")
print(f"\nMoyenne globale du groupe : {moyenne_globale:.2f}")

print("\nÉtudiants avec moyenne ≥ 12 triés décroissant :")
for nom, moy in admis_tries.items():
    print(f"  {nom} : {moy:.2f}")

