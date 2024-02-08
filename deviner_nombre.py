import random

#Choix du nombre aléatoire par l'ordinateur
nombre_choisi=random.randint(1,6)

#Initialisation du résultat qui passera à 1 si l'utilisateur trouve le bon nombre
r = 0

#Boucler 3 fois, pour que l'utilisateur ait 3 tentatives
for i in range(3):
    # Choix du nombre de l'utilisateur
    nombre_propose = int(input('Saisir un nombre :'))

    #Les trois posibilités de retour à l'utilisateur
    if nombre_propose == nombre_choisi:
        r = 1
        break
    elif nombre_propose > nombre_choisi:
        print("Le nombre que vous avez proposé est supérieur à celui que j'ai choisi ")
    elif nombre_propose < nombre_choisi:
        print("Le nombre que vous avez proposé est inférieur à celui que j'ai choisi ")

#L'utilisateur trouve le bon numéro
if r == 1:
    print("Bravo, vous avez trouvé le bon numéro")
    print(f"Le bon numéro était {nombre_choisi}")

#L'utilisateur ne trouve aps le numéro au bout des 3 tentatives
else:
    print("Dommage, vous n'avez pas trouvé le bon numéro")
    print(f"Le bon numéro était {nombre_choisi}")