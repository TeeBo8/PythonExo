# Programme qui génère une liste des nombres pairs entre 1 et 20

print("Les nombres pairs entre 1 et 20 sont :")

# Méthode 1 : Utilisation d'une boucle for avec range()
for nombre in range(2, 21, 2):
    print(nombre, end=" ")

# Saut de ligne pour la présentation
print("\n")

# Méthode 2 : Avec une liste en compréhension
nombres_pairs = [x for x in range(1, 21) if x % 2 == 0]
print("Autre façon de l'afficher :")
print(nombres_pairs) 

#L'utilisation de range() avec trois paramètres (début, fin, pas)
#range(2, 21, 2) génère les nombres pairs de 2 à 20
#L'opérateur modulo % pour vérifier si un nombre est pair
