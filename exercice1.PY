# Création de la liste des jours de la semaine
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# Boucle pour parcourir chaque jour
for jour in semaine:
    if jour in ["Lundi", "Mardi", "Mercredi", "Jeudi"]:
        print(jour, ": Au charbon !")
    elif jour == "Vendredi":
        print(jour, ": FREEEDOM !")
    else:  # Samedi et Dimanche
        print(jour, ": ça va geeker ")
