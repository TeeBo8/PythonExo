# Jeu de devinettes - Devinez le nombre !
import random

def jouer_partie():
    # L'ordinateur choisit un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    meilleur_score = float('inf')  # On initialise le meilleur score à l'infini

    print("\n🎮 Bienvenue dans le jeu de devinettes ! 🎮")
    print("J'ai choisi un nombre entre 1 et 100.")
    print("À vous de le deviner !")

    while True:
        # Demander un nombre à l'utilisateur
        try:
            guess = int(input("\nVotre proposition : "))
            tentatives += 1

            # Vérifier la proposition
            if guess < 1 or guess > 100:
                print("⚠️ Le nombre doit être entre 1 et 100 !")
                continue
            
            if guess < nombre_secret:
                print("📈 C'est plus haut !")
            elif guess > nombre_secret:
                print("📉 C'est plus bas !")
            else:
                print(f"\n🎉 Bravo ! Vous avez trouvé en {tentatives} tentatives ! 🎉")
                return tentatives

        except ValueError:
            print("⚠️ Veuillez entrer un nombre valide !")

# Programme principal
while True:
    score = jouer_partie()
    
    # Demander si on veut rejouer
    rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
    if rejouer != 'o':
        print("\n👋 Merci d'avoir joué ! À bientôt !")
        break

# Petite astuce : Pour gagner rapidement, utilisez la dichotomie !
# Commencez par 50, puis divisez l'intervalle en deux à chaque fois.
# Vous trouverez toujours le nombre en 7 coups maximum ! 