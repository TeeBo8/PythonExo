# Programme de manipulation de fichiers
from pathlib import Path
from typing import List

class GestionnaireFichiers:
    def __init__(self, nom_fichier: str = "noms.txt"):
        """Initialise le gestionnaire avec un nom de fichier"""
        self.nom_fichier = nom_fichier
        self.chemin = Path(nom_fichier)

    def ecrire_noms(self, noms: List[str]) -> None:
        """Écrit une liste de noms dans le fichier"""
        try:
            with open(self.nom_fichier, 'w', encoding='utf-8') as fichier:
                for nom in noms:
                    fichier.write(nom.strip() + '\n')
            print(f"✅ Les noms ont été écrits dans {self.nom_fichier}")
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture : {e}")

    def lire_et_afficher(self) -> None:
        """Lit le fichier et affiche les noms en majuscules"""
        try:
            if not self.chemin.exists():
                print(f"❌ Le fichier {self.nom_fichier} n'existe pas !")
                return

            print(f"\n📖 Contenu du fichier {self.nom_fichier} en majuscules :")
            print("=" * 40)
            
            with open(self.nom_fichier, 'r', encoding='utf-8') as fichier:
                for ligne in fichier:
                    nom = ligne.strip()
                    if nom:  # Ignore les lignes vides
                        print(f"👤 {nom.upper()}")
        
        except Exception as e:
            print(f"❌ Erreur lors de la lecture : {e}")

    def ajouter_nom(self, nom: str) -> None:
        """Ajoute un nouveau nom au fichier"""
        try:
            with open(self.nom_fichier, 'a', encoding='utf-8') as fichier:
                fichier.write(nom.strip() + '\n')
            print(f"✅ {nom} a été ajouté au fichier")
        except Exception as e:
            print(f"❌ Erreur lors de l'ajout : {e}")

def afficher_menu() -> None:
    """Affiche le menu principal"""
    print("\n📝 Gestionnaire de Noms 📝")
    print("1. Créer un nouveau fichier avec des noms")
    print("2. Ajouter un nom")
    print("3. Lire et afficher les noms")
    print("4. Quitter")

def main():
    gestionnaire = GestionnaireFichiers()
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix (1-4) : ")
        
        if choix == "1":
            print("\nEntrez les noms (appuyez sur Entrée deux fois pour terminer) :")
            noms = []
            while True:
                nom = input()
                if nom == "":
                    break
                noms.append(nom)
            gestionnaire.ecrire_noms(noms)
        
        elif choix == "2":
            nom = input("Entrez le nom à ajouter : ")
            if nom.strip():
                gestionnaire.ajouter_nom(nom)
            else:
                print("❌ Le nom ne peut pas être vide !")
        
        elif choix == "3":
            gestionnaire.lire_et_afficher()
        
        elif choix == "4":
            print("\n👋 Au revoir !")
            break
        
        else:
            print("❌ Choix invalide. Veuillez choisir entre 1 et 4.")

if __name__ == "__main__":
    main()

# Exemple d'utilisation :
# 1. Créer un fichier avec les noms : Marie, Pierre, Jean
# 2. Ajouter Sophie
# 3. Lire le fichier -> affichera MARIE, PIERRE, JEAN, SOPHIE 