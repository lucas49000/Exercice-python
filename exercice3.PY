# Notes de l'étudiant
notes = [14, 9, 13, 15, 12]

# Calcul des infos demandées
note_max = max(notes)
note_min = min(notes)
moyenne = sum(notes) / len(notes)

# Affichage
print("Note maximum :", note_max)
print("Note minimum :", note_min)
print("Moyenne :", format(moyenne, ".2f"))

# Attribution de la mention
if 10 <= moyenne < 12:
    mention = "Passable"
elif 12 <= moyenne < 14:
    mention = "Assez bien"
elif moyenne >= 14:
    mention = "Bien"
else:
    mention = "Insuffisant"

print("Mention :", mention)
