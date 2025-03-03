# Programme qui vérifie si un mot est un palindrome

def est_palindrome(mot):
    # Convertir en minuscules et enlever les espaces
    mot = mot.lower().replace(" ", "")
    
    # Méthode 1 : Avec le slicing de Python
    return mot == mot[::-1]

    # Note : mot[::-1] est une façon élégante de renverser une chaîne en Python
    # Le -1 signifie qu'on lit les caractères de droite à gauche

# Programme principal
while True:
    # Demander un mot à l'utilisateur
    mot_utilisateur = input("\nEntrez un mot (ou 'q' pour quitter) : ")
    
    # Condition de sortie
    if mot_utilisateur.lower() == 'q':
        print("Au revoir !")
        break
    
    # Vérifier si c'est un palindrome
    if est_palindrome(mot_utilisateur):
        print(f"'{mot_utilisateur}' est un palindrome ! ✨")
    else:
        print(f"'{mot_utilisateur}' n'est pas un palindrome.")
        print(f"À l'envers, cela donne : {mot_utilisateur[::-1]}")

# Exemples de palindromes à essayer :
# - kayak
# - radar
# - elle
# - été
# - À l'étape épatela
# - Engage le jeu que je le gagne 