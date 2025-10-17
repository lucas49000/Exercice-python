# Script : moyenne_notes.py

# On lit le fichier contenant les notes
with open("notes.txt", "r") as fichier:
    lignes = fichier.readlines()

# On convertit chaque ligne en float et on les stocke dans une liste
notes = []
for ligne in lignes:
    try:
        note = float(ligne.strip())  # strip enlève les espaces et \n
        notes.append(note)
    except ValueError:
        # si une ligne n'est pas un nombre, on l'ignore
        print(f"Ligne ignorée : '{ligne.strip()}'")

# Vérifie qu'on a bien des notes
if len(notes) > 0:
    moyenne = sum(notes) / len(notes)
    print(f"La moyenne des notes est : {moyenne:.2f}")
else:
    print("Aucune note valide trouvée dans le fichier.")
