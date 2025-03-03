# Programme de calculatrice simple

# Demande des nombres à l'utilisateur
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")

# Calcul selon l'opération choisie
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Vérification de la division par zéro
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        print("Erreur : Division par zéro impossible!")
        exit()
else:
    print("Opération non valide!")
    exit()

# Affichage du résultat
print(f"{nombre1} {operation} {nombre2} = {resultat}") 

 # input() permet de demander une saisie à l'utilisateur
 # float() convertit la saisie (qui est toujours une chaîne de caractères) en nombre décimal
 # Les variables nombre1 et nombre2 stockent les nombres
 # La variable operation stocke l'opérateur choisi
 # Structure conditionnelle :
 # if/elif/else permet de choisir l'opération à effectuer
 # Chacune des opérations est gérée séparément
 # Une vérification spéciale est faite pour la division par zéro
 # Si l'opération n'est pas reconnue, un message d'erreur s'affiche
 # La fonction exit() arrête le programme en cas d'erreur
 # Affichage du résultat :
 # Utilisation d'une f-string (format string) pour un affichage élégant
 # Le résultat inclut l'opération choisie
 
 
