# Serveur HTTP simple avec Python
import http.server
import socketserver
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import json

# HTML template pour la page d'accueil
PAGE_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Serveur Python</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .info {
            background-color: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .api-section {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Bienvenue sur mon Serveur Python !</h1>
        
        <div class="info">
            <h2>ℹ️ Informations</h2>
            <p>Date et heure : <strong>{datetime}</strong></p>
            <p>Chemin demandé : <strong>{path}</strong></p>
            <p>Méthode HTTP : <strong>{method}</strong></p>
        </div>

        <div class="api-section">
            <h2>🔌 API Endpoints disponibles</h2>
            <ul>
                <li><code>/</code> - Cette page d'accueil</li>
                <li><code>/api/hello?name=Thibault</code> - Salutation personnalisée (exemple simple)</li>
                <li><code>/api/hello?name=Thibault%20%F0%9F%9A%80</code> - Salutation avec caractères spéciaux (encodé en URL)</li>
                <li><code>/api/time</code> - Heure actuelle au format JSON</li>
            </ul>
        </div>

        <div class="footer">
            <p>Serveur créé avec Python {python_version} 🐍</p>
        </div>
    </div>
</body>
</html>
"""

class MonServeurHTTP(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Gère les requêtes GET"""
        # Parse l'URL
        url = urlparse(self.path)
        chemin = url.path
        parametres = parse_qs(url.query)

        # Route pour l'API hello
        if chemin == "/api/hello":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            nom = parametres.get('name', ['Visiteur'])[0]
            reponse = {
                "message": f"Bonjour, {nom} !",
                "timestamp": datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(reponse, ensure_ascii=False).encode('utf-8'))
            return

        # Route pour l'API time
        elif chemin == "/api/time":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            reponse = {
                "datetime": datetime.now().isoformat(),
                "timestamp": datetime.now().timestamp()
            }
            self.wfile.write(json.dumps(reponse, ensure_ascii=False).encode('utf-8'))
            return

        # Page d'accueil par défaut
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Prépare le contenu de la page
        page = PAGE_HTML.format(
            datetime=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            path=self.path,
            method=self.command,
            python_version=".".join(map(str, __import__('sys').version_info[:3]))
        )
        
        self.wfile.write(page.encode('utf-8'))

def demarrer_serveur(port=8000):
    """Démarre le serveur sur le port spécifié"""
    try:
        with socketserver.TCPServer(("", port), MonServeurHTTP) as httpd:
            print(f"🌐 Serveur démarré sur le port {port}")
            print(f"👉 Ouvrez votre navigateur à l'adresse : http://localhost:{port}")
            print("📝 Logs du serveur :")
            print("=" * 50)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Arrêt du serveur...")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    demarrer_serveur()

# Pour tester :
# 1. Lancer le serveur : python serveur_http.py
# 2. Ouvrir un navigateur et aller sur : http://localhost:8000
# 3. Tester l'API : http://localhost:8000/api/hello?name=Alice
# 4. Voir l'heure : http://localhost:8000/api/time 