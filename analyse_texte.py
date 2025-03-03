# Programme d'analyse de texte
from collections import Counter

def analyser_texte(texte):
    # Analyse basique
    nb_caracteres = len(texte)
    nb_mots = len(texte.split())
    
    # Analyse des caractères (en excluant les espaces)
    caracteres = [c.lower() for c in texte if c.strip()]
    freq_caracteres = Counter(caracteres)
    
    # Trouver les 3 caractères les plus fréquents
    caracteres_frequents = freq_caracteres.most_common(3)
    
    # Calculer le nombre de phrases (en comptant les . ! ?)
    nb_phrases = sum(1 for c in texte if c in '.!?')
    
    # Affichage des résultats
    print("\n📊 Analyse de votre texte 📊")
    print("=" * 30)
    print(f"📝 Nombre de mots : {nb_mots}")
    print(f"📏 Nombre de caractères : {nb_caracteres}")
    print(f"📚 Nombre de phrases : {nb_phrases}")
    
    # Affichage des caractères les plus fréquents
    print("\n🔤 Caractères les plus fréquents :")
    for char, freq in caracteres_frequents:
        print(f"   '{char}' : {freq} fois")
    
    # Statistiques supplémentaires
    print("\n📈 Statistiques supplémentaires :")
    print(f"📊 Longueur moyenne des mots : {sum(len(mot) for mot in texte.split()) / nb_mots:.1f} caractères")
    
    # Bonus : Détection des palindromes dans les mots
    palindromes = [mot for mot in texte.split() if mot.lower() == mot.lower()[::-1] and len(mot) > 1]
    if palindromes:
        print("\n🎯 Palindromes trouvés :")
        print("   " + ", ".join(palindromes))

# Programme principal
while True:
    print("\n✨ Bienvenue dans l'analyseur de texte ✨")
    texte = input("Entrez votre texte (ou 'q' pour quitter) : ")
    
    if texte.lower() == 'q':
        print("\n👋 Au revoir !")
        break
    
    if not texte.strip():
        print("⚠️ Le texte ne peut pas être vide !")
        continue
        
    analyser_texte(texte)

# Exemples de textes à tester :
# - "Le radar détecte un kayak qui fait la course avec un bob !"
# - "Python est un langage de programmation fascinant !"
# - "Madam, I'm Adam." 