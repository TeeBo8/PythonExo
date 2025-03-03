# Programme de gestion de catalogue de produits avec JSON
import json
from typing import List, Dict, Any
from pathlib import Path

# Données de exemple (simulation d'une API)
CATALOGUE_INITIAL = {
    "produits": [
        {
            "id": 1,
            "nom": "Ordinateur portable",
            "type": "électronique",
            "prix": 999.99,
            "stock": 15,
            "caracteristiques": {
                "marque": "TechPro",
                "ram": "16GB",
                "stockage": "512GB SSD"
            }
        },
        {
            "id": 2,
            "nom": "Smartphone",
            "type": "électronique",
            "prix": 699.99,
            "stock": 25,
            "caracteristiques": {
                "marque": "PhonePro",
                "ram": "8GB",
                "stockage": "128GB"
            }
        },
        {
            "id": 3,
            "nom": "T-shirt",
            "type": "vêtement",
            "prix": 19.99,
            "stock": 100,
            "caracteristiques": {
                "taille": "M",
                "couleur": "Bleu",
                "matière": "Coton"
            }
        },
        {
            "id": 4,
            "nom": "Chaussures de sport",
            "type": "vêtement",
            "prix": 89.99,
            "stock": 45,
            "caracteristiques": {
                "taille": "42",
                "couleur": "Noir",
                "type": "Running"
            }
        },
        {
            "id": 5,
            "nom": "Café en grains",
            "type": "alimentaire",
            "prix": 12.99,
            "stock": 200,
            "caracteristiques": {
                "origine": "Colombie",
                "torréfaction": "Moyenne",
                "poids": "1kg"
            }
        }
    ]
}

class CatalogueProduits:
    def __init__(self, fichier: str = "catalogue.json"):
        """Initialise le catalogue avec un fichier JSON"""
        self.fichier = Path(fichier)
        self.charger_ou_creer_catalogue()

    def charger_ou_creer_catalogue(self) -> None:
        """Charge le catalogue depuis le fichier ou crée un nouveau"""
        if not self.fichier.exists():
            self.sauvegarder_catalogue(CATALOGUE_INITIAL)
        self.catalogue = self.charger_catalogue()

    def charger_catalogue(self) -> Dict[str, List[Dict[str, Any]]]:
        """Charge le catalogue depuis le fichier JSON"""
        try:
            with open(self.fichier, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Erreur lors du chargement : {e}")
            return CATALOGUE_INITIAL

    def sauvegarder_catalogue(self, donnees: Dict[str, List[Dict[str, Any]]]) -> None:
        """Sauvegarde le catalogue dans le fichier JSON"""
        try:
            with open(self.fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
            print("✅ Catalogue sauvegardé avec succès")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")

    def filtrer_par_type(self, type_produit: str) -> List[Dict[str, Any]]:
        """Filtre les produits par type"""
        return [p for p in self.catalogue["produits"] if p["type"].lower() == type_produit.lower()]

    def filtrer_par_prix(self, prix_max: float) -> List[Dict[str, Any]]:
        """Filtre les produits par prix maximum"""
        return [p for p in self.catalogue["produits"] if p["prix"] <= prix_max]

    def rechercher_produit(self, terme: str) -> List[Dict[str, Any]]:
        """Recherche un produit par nom"""
        terme = terme.lower()
        return [p for p in self.catalogue["produits"] if terme in p["nom"].lower()]

    def afficher_produits(self, produits: List[Dict[str, Any]]) -> None:
        """Affiche une liste de produits de manière formatée"""
        if not produits:
            print("❌ Aucun produit trouvé")
            return

        print("\n📦 Résultats de la recherche :")
        print("=" * 50)
        for produit in produits:
            print(f"\n🏷️  {produit['nom']} (ID: {produit['id']})")
            print(f"📝 Type: {produit['type']}")
            print(f"💰 Prix: {produit['prix']}€")
            print(f"📦 Stock: {produit['stock']}")
            print("✨ Caractéristiques:")
            for cle, valeur in produit['caracteristiques'].items():
                print(f"   - {cle}: {valeur}")
            print("-" * 30)

def afficher_menu() -> None:
    """Affiche le menu principal"""
    print("\n🛍️  Catalogue de Produits 🛍️")
    print("1. Voir tous les produits")
    print("2. Filtrer par type")
    print("3. Filtrer par prix maximum")
    print("4. Rechercher un produit")
    print("5. Quitter")

def main():
    catalogue = CatalogueProduits()
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix (1-5) : ")
        
        if choix == "1":
            catalogue.afficher_produits(catalogue.catalogue["produits"])
        
        elif choix == "2":
            type_produit = input("Entrez le type de produit (électronique, vêtement, alimentaire) : ")
            produits = catalogue.filtrer_par_type(type_produit)
            catalogue.afficher_produits(produits)
        
        elif choix == "3":
            try:
                prix_max = float(input("Entrez le prix maximum : "))
                produits = catalogue.filtrer_par_prix(prix_max)
                catalogue.afficher_produits(produits)
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
        
        elif choix == "4":
            terme = input("Entrez le terme à rechercher : ")
            produits = catalogue.rechercher_produit(terme)
            catalogue.afficher_produits(produits)
        
        elif choix == "5":
            print("\n👋 Au revoir !")
            break
        
        else:
            print("❌ Choix invalide. Veuillez choisir entre 1 et 5.")

if __name__ == "__main__":
    main()

# Exemple d'utilisation :
# 1. Voir tous les produits
# 2. Filtrer les produits électroniques
# 3. Filtrer les produits moins chers que 100€
# 4. Rechercher "sport" dans les noms 