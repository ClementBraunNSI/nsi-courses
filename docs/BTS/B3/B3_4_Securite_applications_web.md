<style>
/* Styles modernes pour le cours Sécurité Web BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(46, 204, 113, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.concept-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #2ecc71;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-left: 5px solid #2ecc71;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #2ecc71;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.security-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.security-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.security-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(46, 204, 113, 0.2);
}

.security-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.security-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.security-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.protocol-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.protocol-card {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(46, 204, 113, 0.2);
    transition: all 0.3s ease;
}

.protocol-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(46, 204, 113, 0.2);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #2ecc71;
}

.code-title {
    color: #2ecc71;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.demo-box {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.demo-title {
    color: #3498db;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.vulnerability-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.vulnerability-table th, .vulnerability-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(46, 204, 113, 0.2);
}

.vulnerability-table th {
    background: rgba(46, 204, 113, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

.auth-step {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.auth-title {
    color: #f39c12;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.gdpr-box {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.gdpr-title {
    color: #e74c3c;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* Styles pour les titres h3 */
h3 {
    font-size: 1.8rem;
    font-weight: 600;
    color: #2ecc71;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(46, 204, 113, 0.3);
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.4 - Sécurité des Applications Web</h1>
    <p class="course-subtitle">Protection des données et sécurisation des services - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Comprendre les protocoles de sécurisation web (HTTPS, TLS)
- Implémenter des mécanismes d'authentification et d'autorisation
- Protéger les données personnelles selon le RGPD
- Sécuriser les communications et les sessions utilisateur

---

<div class="concept-section">
<h2 class="section-title">🔒 Protocoles de sécurisation</h2>

<div class="definition-box">
<div class="definition-title">HTTPS (HyperText Transfer Protocol Secure)</div>
<div class="definition-content">
Version sécurisée du protocole HTTP utilisant TLS/SSL pour chiffrer les communications entre le client et le serveur, garantissant confidentialité, intégrité et authentification.
</div>
</div>

<h3>Comparaison HTTP vs HTTPS</h3>

<div class="security-grid">
<div class="security-card">
<div class="security-icon">🔓</div>
<div class="security-name">HTTP</div>
<div class="security-description">
<ul>
<li>Port 80</li>
<li>Données en clair</li>
<li>Vulnérable aux écoutes</li>
<li>Pas d'authentification du serveur</li>
<li>Risque de modification des données</li>
</ul>
</div>
</div>

<div class="security-card">
<div class="security-icon">🔒</div>
<div class="security-name">HTTPS</div>
<div class="security-description">
<ul>
<li>Port 443</li>
<li>Données chiffrées</li>
<li>Protection contre l'écoute</li>
<li>Certificat serveur</li>
<li>Intégrité des données garantie</li>
</ul>
</div>
</div>
</div>

<h3>Processus de connexion TLS</h3>

<div class="auth-step">
<div class="auth-title">1. Client Hello</div>
Le client envoie sa version TLS, les algorithmes supportés et un nombre aléatoire.
</div>

<div class="auth-step">
<div class="auth-title">2. Server Hello</div>
Le serveur répond avec sa version TLS, l'algorithme choisi, son certificat et un nombre aléatoire.
</div>

<div class="auth-step">
<div class="auth-title">3. Vérification du certificat</div>
Le client vérifie la validité du certificat serveur auprès d'une autorité de certification.
</div>

<div class="auth-step">
<div class="auth-title">4. Échange de clés</div>
Génération d'une clé de session symétrique pour chiffrer les communications.
</div>

<div class="auth-step">
<div class="auth-title">5. Communication sécurisée</div>
Toutes les données sont chiffrées avec la clé de session.
</div>

<h3>Configuration HTTPS avec Python Flask</h3>

<div class="code-example">
<div class="code-title">Serveur Flask avec HTTPS</div>
```python
from flask import Flask, request, session, redirect, url_for
import ssl

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_tres_longue_et_aleatoire'

@app.route('/')
def index():
    return '''
    <h1>Serveur HTTPS sécurisé</h1>
    <p>Cette connexion est chiffrée !</p>
    <a href="/login">Se connecter</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vérification sécurisée (à implémenter)
        if verify_credentials(username, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Identifiants incorrects', 401
    
    return '''
    <form method="post">
        <input type="text" name="username" placeholder="Nom d'utilisateur" required>
        <input type="password" name="password" placeholder="Mot de passe" required>
        <button type="submit">Se connecter</button>
    </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f'Bienvenue {session["user"]} !'

def verify_credentials(username, password):
    # Implémentation sécurisée avec hachage
    # Ne jamais stocker les mots de passe en clair !
    return True  # Exemple simplifié

if __name__ == '__main__':
    # Configuration SSL/TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('certificat.pem', 'cle_privee.pem')
    
    app.run(host='0.0.0.0', port=443, ssl_context=context, debug=False)
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔐 Authentification et autorisation</h2>

<div class="definition-box">
<div class="definition-title">Authentification vs Autorisation</div>
<div class="definition-content">
<strong>Authentification :</strong> Vérifier l'identité de l'utilisateur ("Qui êtes-vous ?")
<br><strong>Autorisation :</strong> Vérifier les permissions de l'utilisateur ("Que pouvez-vous faire ?")
</div>
</div>

<h3>Méthodes d'authentification</h3>

<div class="protocol-grid">
<div class="protocol-card">
<h4>🔑 Authentification basique</h4>
<p>Nom d'utilisateur et mot de passe. Simple mais nécessite HTTPS.</p>
</div>

<div class="protocol-card">
<h3>🎫 Authentification par token</h3>
<p>JWT (JSON Web Token) pour les API et applications modernes.</p>
</div>

<div class="protocol-card">
<h3>📱 Authentification multi-facteurs (MFA)</h3>
<p>Combinaison de plusieurs facteurs : mot de passe + SMS/app.</p>
</div>

<div class="protocol-card">
<h3>🔗 OAuth 2.0</h3>
<p>Délégation d'authentification via des services tiers (Google, Facebook).</p>
</div>
</div>

<h3>Implémentation sécurisée des mots de passe</h3>

<div class="code-example">
<div class="code-title">Gestion sécurisée des mots de passe</div>
```python
import hashlib
import secrets
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

class UserManager:
    def __init__(self):
        self.users = {}  # En production : base de données
    
    def hash_password_bcrypt(self, password):
        """Hachage sécurisé avec bcrypt (recommandé)"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
    
    def verify_password_bcrypt(self, password, hashed):
        """Vérification avec bcrypt"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    
    def hash_password_werkzeug(self, password):
        """Alternative avec Werkzeug"""
        return generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    
    def verify_password_werkzeug(self, password, hashed):
        """Vérification avec Werkzeug"""
        return check_password_hash(hashed, password)
    
    def create_user(self, username, password, email):
        """Créer un nouvel utilisateur"""
        if username in self.users:
            raise ValueError("Utilisateur déjà existant")
        
        # Validation du mot de passe
        if not self.is_strong_password(password):
            raise ValueError("Mot de passe trop faible")
        
        # Hachage sécurisé
        hashed_password = self.hash_password_bcrypt(password)
        
        self.users[username] = {
            'password_hash': hashed_password,
            'email': email,
            'created_at': datetime.now(),
            'last_login': None,
            'failed_attempts': 0,
            'locked_until': None
        }
        
        return True
    
    def authenticate(self, username, password):
        """Authentifier un utilisateur"""
        user = self.users.get(username)
        if not user:
            return False
        
        # Vérifier si le compte est verrouillé
        if user['locked_until'] and datetime.now() < user['locked_until']:
            raise Exception("Compte temporairement verrouillé")
        
        # Vérifier le mot de passe
        if self.verify_password_bcrypt(password, user['password_hash']):
            # Réinitialiser les tentatives échouées
            user['failed_attempts'] = 0
            user['locked_until'] = None
            user['last_login'] = datetime.now()
            return True
        else:
            # Incrémenter les tentatives échouées
            user['failed_attempts'] += 1
            
            # Verrouiller après 5 tentatives
            if user['failed_attempts'] >= 5:
                user['locked_until'] = datetime.now() + timedelta(minutes=30)
            
            return False
    
    def is_strong_password(self, password):
        """Vérifier la force du mot de passe"""
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        return has_upper and has_lower and has_digit and has_special

# Exemple d'utilisation
user_manager = UserManager()

try:
    user_manager.create_user("alice", "MonMotDePasse123!", "alice@example.com")
    print("Utilisateur créé avec succès")
    
    if user_manager.authenticate("alice", "MonMotDePasse123!"):
        print("Authentification réussie")
    else:
        print("Échec de l'authentification")
        
except ValueError as e:
    print(f"Erreur : {e}")
```
</div>

<h3>Gestion des sessions sécurisées</h3>

<div class="code-example">
<div class="code-title">Sessions sécurisées avec Flask</div>
```python
from flask import Flask, session, request, jsonify
import secrets
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Clé aléatoire sécurisée

# Configuration sécurisée des sessions
app.config.update(
    SESSION_COOKIE_SECURE=True,      # HTTPS uniquement
    SESSION_COOKIE_HTTPONLY=True,    # Pas d'accès JavaScript
    SESSION_COOKIE_SAMESITE='Lax',   # Protection CSRF
    PERMANENT_SESSION_LIFETIME=1800  # 30 minutes
)

class SessionManager:
    def __init__(self):
        self.active_sessions = {}
    
    def create_session(self, user_id):
        """Créer une nouvelle session"""
        session_id = secrets.token_urlsafe(32)
        session_data = {
            'user_id': user_id,
            'created_at': time.time(),
            'last_activity': time.time(),
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent', '')
        }
        
        self.active_sessions[session_id] = session_data
        session['session_id'] = session_id
        session.permanent = True
        
        return session_id
    
    def validate_session(self, session_id):
        """Valider une session existante"""
        if session_id not in self.active_sessions:
            return False
        
        session_data = self.active_sessions[session_id]
        current_time = time.time()
        
        # Vérifier l'expiration (30 minutes d'inactivité)
        if current_time - session_data['last_activity'] > 1800:
            self.destroy_session(session_id)
            return False
        
        # Vérifier l'IP (optionnel, peut poser problème avec les proxies)
        if session_data['ip_address'] != request.remote_addr:
            # Log de sécurité
            print(f"Changement d'IP détecté pour la session {session_id}")
        
        # Mettre à jour l'activité
        session_data['last_activity'] = current_time
        return True
    
    def destroy_session(self, session_id):
        """Détruire une session"""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
        
        session.clear()
    
    def get_user_id(self, session_id):
        """Récupérer l'ID utilisateur d'une session"""
        if session_id in self.active_sessions:
            return self.active_sessions[session_id]['user_id']
        return None

session_manager = SessionManager()

@app.before_request
def check_session():
    """Vérifier la session avant chaque requête"""
    if request.endpoint in ['login', 'static']:
        return  # Pas de vérification pour ces endpoints
    
    session_id = session.get('session_id')
    if not session_id or not session_manager.validate_session(session_id):
        return jsonify({'error': 'Session invalide'}), 401

@app.route('/logout')
def logout():
    """Déconnexion sécurisée"""
    session_id = session.get('session_id')
    if session_id:
        session_manager.destroy_session(session_id)
    
    return jsonify({'message': 'Déconnexion réussie'})
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🛡️ Protection contre les vulnérabilités web</h2>

<h3>Top 10 OWASP des vulnérabilités</h3>

<table class="vulnerability-table">
<thead>
<tr>
<th>Rang</th>
<th>Vulnérabilité</th>
<th>Description</th>
<th>Protection</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Injection</td>
<td>SQL, NoSQL, LDAP injection</td>
<td>Requêtes préparées, validation</td>
</tr>
<tr>
<td>2</td>
<td>Authentification cassée</td>
<td>Sessions, mots de passe faibles</td>
<td>MFA, sessions sécurisées</td>
</tr>
<tr>
<td>3</td>
<td>Exposition de données</td>
<td>Données sensibles non protégées</td>
<td>Chiffrement, HTTPS</td>
</tr>
<tr>
<td>4</td>
<td>XXE</td>
<td>XML External Entity</td>
<td>Désactiver les entités externes</td>
</tr>
<tr>
<td>5</td>
<td>Contrôle d'accès cassé</td>
<td>Autorisations mal configurées</td>
<td>Principe du moindre privilège</td>
</tr>
<tr>
<td>6</td>
<td>Configuration de sécurité</td>
<td>Paramètres par défaut non sécurisés</td>
<td>Durcissement, mise à jour</td>
</tr>
<tr>
<td>7</td>
<td>XSS</td>
<td>Cross-Site Scripting</td>
<td>Échappement, CSP</td>
</tr>
<tr>
<td>8</td>
<td>Désérialisation</td>
<td>Objets non fiables</td>
<td>Validation, signature</td>
</tr>
<tr>
<td>9</td>
<td>Composants vulnérables</td>
<td>Bibliothèques obsolètes</td>
<td>Mise à jour régulière</td>
</tr>
<tr>
<td>10</td>
<td>Logging insuffisant</td>
<td>Détection d'incidents limitée</td>
<td>Logs détaillés, monitoring</td>
</tr>
</tbody>
</table>

<h3>Protection contre les injections SQL</h3>

<div class="code-example">
<div class="code-title">Prévention des injections SQL</div>
```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialiser la base de données"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user'
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_user_vulnerable(self, username):
        """VULNÉRABLE - Ne jamais faire cela !"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # DANGER : Injection SQL possible
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        
        result = cursor.fetchone()
        conn.close()
        return result
    
    def get_user_secure(self, username):
        """SÉCURISÉ - Utilisation de requêtes préparées"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Sécurisé : paramètres liés
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        
        result = cursor.fetchone()
        conn.close()
        return result
    
    def search_users_secure(self, search_term, role=None):
        """Recherche sécurisée avec paramètres multiples"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, role FROM users WHERE username LIKE ?"
        params = [f"%{search_term}%"]
        
        if role:
            query += " AND role = ?"
            params.append(role)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        
        return results

db = DatabaseManager('app.db')

@app.route('/user/<username>')
def get_user(username):
    """Endpoint sécurisé pour récupérer un utilisateur"""
    # Validation d'entrée
    if not username or len(username) > 50:
        return jsonify({'error': 'Nom d'utilisateur invalide'}), 400
    
    # Utilisation de la méthode sécurisée
    user = db.get_user_secure(username)
    
    if user:
        return jsonify({
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'role': user[4]
        })
    else:
        return jsonify({'error': 'Utilisateur non trouvé'}), 404

@app.route('/search')
def search_users():
    """Recherche d'utilisateurs avec validation"""
    search_term = request.args.get('q', '').strip()
    role = request.args.get('role', '').strip()
    
    # Validation des paramètres
    if not search_term or len(search_term) < 2:
        return jsonify({'error': 'Terme de recherche trop court'}), 400
    
    if role and role not in ['user', 'admin', 'moderator']:
        return jsonify({'error': 'Rôle invalide'}), 400
    
    results = db.search_users_secure(search_term, role)
    
    return jsonify({
        'users': [
            {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'role': user[3]
            }
            for user in results
        ]
    })
```
</div>

<h3>Protection XSS et CSP</h3>

<div class="code-example">
<div class="code-title">Protection contre XSS</div>
```python
from flask import Flask, render_template_string, request, escape
from markupsafe import Markup
import html
import re

app = Flask(__name__)

class XSSProtection:
    @staticmethod
    def sanitize_input(user_input):
        """Nettoyer les entrées utilisateur"""
        if not user_input:
            return ""
        
        # Échapper les caractères HTML
        sanitized = html.escape(user_input)
        
        # Supprimer les scripts potentiels
        sanitized = re.sub(r'<script[^>]*>.*?</script>', '', sanitized, flags=re.IGNORECASE | re.DOTALL)
        
        return sanitized
    
    @staticmethod
    def validate_url(url):
        """Valider une URL pour éviter les redirections malveillantes"""
        if not url:
            return False
        
        # Autoriser seulement les URLs relatives ou HTTPS
        if url.startswith('/') or url.startswith('https://'):
            return True
        
        return False

@app.route('/comment', methods=['POST'])
def add_comment():
    """Ajouter un commentaire avec protection XSS"""
    comment = request.form.get('comment', '')
    
    # Nettoyer l'entrée
    clean_comment = XSSProtection.sanitize_input(comment)
    
    # Validation supplémentaire
    if len(clean_comment) > 1000:
        return "Commentaire trop long", 400
    
    # Sauvegarder en base (exemple)
    # db.save_comment(clean_comment)
    
    return f"Commentaire ajouté : {clean_comment}"

@app.after_request
def add_security_headers(response):
    """Ajouter des en-têtes de sécurité"""
    # Content Security Policy
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none';"
    )
    
    # Autres en-têtes de sécurité
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    return response
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔐 Protection des données personnelles</h2>

<div class="definition-box">
<div class="definition-title">RGPD (Règlement Général sur la Protection des Données)</div>
<div class="definition-content">
Règlement européen entré en vigueur en 2018, qui encadre le traitement des données personnelles et renforce les droits des individus sur leurs données.
</div>
</div>

<h3>Principes fondamentaux du RGPD</h3>

<div class="gdpr-box">
<div class="gdpr-title">🎯 Finalité</div>
Les données doivent être collectées pour des finalités déterminées, explicites et légitimes.
</div>

<div class="gdpr-box">
<div class="gdpr-title">📏 Minimisation</div>
Collecter uniquement les données nécessaires à la finalité poursuivie.
</div>

<div class="gdpr-box">
<div class="gdpr-title">⏰ Conservation limitée</div>
Les données ne doivent pas être conservées plus longtemps que nécessaire.
</div>

<div class="gdpr-box">
<div class="gdpr-title">🔒 Sécurité</div>
Mettre en place des mesures techniques et organisationnelles appropriées.
</div>

<h3>Droits des personnes concernées</h3>

<div class="security-grid">
<div class="security-card">
<div class="security-icon">ℹ️</div>
<div class="security-name">Droit à l'information</div>
<div class="security-description">
Être informé de la collecte et du traitement de ses données personnelles.
</div>
</div>

<div class="security-card">
<div class="security-icon">👁️</div>
<div class="security-name">Droit d'accès</div>
<div class="security-description">
Obtenir une copie de ses données personnelles et des informations sur leur traitement.
</div>
</div>

<div class="security-card">
<div class="security-icon">✏️</div>
<div class="security-name">Droit de rectification</div>
<div class="security-description">
Demander la correction de données inexactes ou incomplètes.
</div>
</div>

<div class="security-card">
<div class="security-icon">🗑️</div>
<div class="security-name">Droit à l'effacement</div>
<div class="security-description">
Demander la suppression de ses données dans certaines conditions.
</div>
</div>

<div class="security-card">
<div class="security-icon">📦</div>
<div class="security-name">Droit à la portabilité</div>
<div class="security-description">
Récupérer ses données dans un format structuré et les transférer.
</div>
</div>

<div class="security-card">
<div class="security-icon">🚫</div>
<div class="security-name">Droit d'opposition</div>
<div class="security-description">
S'opposer au traitement de ses données pour des raisons légitimes.
</div>
</div>
</div>

<h3>Implémentation RGPD en Python</h3>

<div class="code-example">
<div class="code-title">Gestion RGPD avec Python</div>
```python
from datetime import datetime, timedelta
import json
import hashlib

class GDPRManager:
    def __init__(self):
        self.data_retention_policies = {
            'user_logs': timedelta(days=365),
            'marketing_data': timedelta(days=1095),  # 3 ans
            'financial_data': timedelta(days=2555),  # 7 ans
            'session_data': timedelta(hours=24)
        }
        
        self.consent_records = {}
        self.data_processing_log = []
    
    def record_consent(self, user_id, purpose, consent_given, ip_address):
        """Enregistrer le consentement utilisateur"""
        consent_record = {
            'user_id': user_id,
            'purpose': purpose,
            'consent_given': consent_given,
            'timestamp': datetime.now().isoformat(),
            'ip_address': self.hash_ip(ip_address),
            'version': '1.0'  # Version de la politique de confidentialité
        }
        
        if user_id not in self.consent_records:
            self.consent_records[user_id] = []
        
        self.consent_records[user_id].append(consent_record)
        
        # Log de l'activité
        self.log_data_processing(user_id, 'consent_recorded', purpose)
    
    def hash_ip(self, ip_address):
        """Hasher l'adresse IP pour la pseudonymisation"""
        return hashlib.sha256(ip_address.encode()).hexdigest()[:16]
    
    def log_data_processing(self, user_id, action, purpose, data_type=None):
        """Logger les activités de traitement de données"""
        log_entry = {
            'user_id': user_id,
            'action': action,
            'purpose': purpose,
            'data_type': data_type,
            'timestamp': datetime.now().isoformat(),
            'processor': 'system'
        }
        
        self.data_processing_log.append(log_entry)
    
    def export_user_data(self, user_id):
        """Exporter toutes les données d'un utilisateur (portabilité)"""
        user_data = {
            'user_id': user_id,
            'export_date': datetime.now().isoformat(),
            'consent_records': self.consent_records.get(user_id, []),
            'processing_log': [
                log for log in self.data_processing_log 
                if log['user_id'] == user_id
            ]
        }
        
        # Ajouter d'autres données utilisateur depuis la base
        # user_data.update(self.get_user_profile(user_id))
        # user_data.update(self.get_user_orders(user_id))
        
        self.log_data_processing(user_id, 'data_exported', 'user_request')
        
        return json.dumps(user_data, indent=2, ensure_ascii=False)
    
    def delete_user_data(self, user_id, reason='user_request'):
        """Supprimer les données d'un utilisateur (droit à l'effacement)"""
        # Vérifier si la suppression est autorisée
        if not self.can_delete_user_data(user_id, reason):
            raise Exception("Suppression non autorisée pour des raisons légales")
        
        # Supprimer les données personnelles
        # self.delete_user_profile(user_id)
        # self.anonymize_user_orders(user_id)
        
        # Conserver les logs de consentement (obligation légale)
        self.log_data_processing(user_id, 'data_deleted', reason)
        
        return True
    
    def can_delete_user_data(self, user_id, reason):
        """Vérifier si les données peuvent être supprimées"""
        # Vérifier les obligations légales de conservation
        # Par exemple, données financières à conserver 7 ans
        
        # Vérifier s'il y a des litiges en cours
        # if self.has_pending_legal_case(user_id):
        #     return False
        
        return True
    
    def anonymize_expired_data(self):
        """Anonymiser les données expirées selon les politiques de rétention"""
        current_time = datetime.now()
        
        for data_type, retention_period in self.data_retention_policies.items():
            expiry_date = current_time - retention_period
            
            # Identifier et anonymiser les données expirées
            # self.anonymize_data_by_type(data_type, expiry_date)
            
            print(f"Données {data_type} antérieures à {expiry_date} anonymisées")
    
    def generate_privacy_report(self, user_id):
        """Générer un rapport de confidentialité pour un utilisateur"""
        consent_history = self.consent_records.get(user_id, [])
        processing_activities = [
            log for log in self.data_processing_log 
            if log['user_id'] == user_id
        ]
        
        report = {
            'user_id': user_id,
            'report_date': datetime.now().isoformat(),
            'active_consents': [
                consent for consent in consent_history 
                if consent['consent_given']
            ],
            'data_processing_summary': {
                'total_activities': len(processing_activities),
                'last_activity': max(
                    (log['timestamp'] for log in processing_activities), 
                    default='Aucune activité'
                )
            },
            'retention_status': self.get_retention_status(user_id)
        }
        
        return report
    
    def get_retention_status(self, user_id):
        """Obtenir le statut de rétention des données"""
        # Calculer quand les différents types de données expireront
        current_time = datetime.now()
        
        status = {}
        for data_type, retention_period in self.data_retention_policies.items():
            # En pratique, récupérer la date de création des données
            # creation_date = self.get_data_creation_date(user_id, data_type)
            # expiry_date = creation_date + retention_period
            
            status[data_type] = {
                'retention_period_days': retention_period.days,
                'status': 'active'  # ou 'expired', 'anonymized'
            }
        
        return status

# Exemple d'utilisation
gdpr_manager = GDPRManager()

# Enregistrer un consentement
gdpr_manager.record_consent(
    user_id='user123',
    purpose='marketing',
    consent_given=True,
    ip_address='192.168.1.1'
)

# Exporter les données d'un utilisateur
user_data_export = gdpr_manager.export_user_data('user123')
print("Données exportées :", user_data_export)

# Générer un rapport de confidentialité
privacy_report = gdpr_manager.generate_privacy_report('user123')
print("Rapport de confidentialité :", privacy_report)
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔍 Monitoring et détection d'incidents</h2>

<h3>Mise en place de logs de sécurité</h3>

<div class="code-example">
<div class="code-title">Système de logging sécurisé</div>
```python
import logging
import json
from datetime import datetime
from flask import request, g
import hashlib

class SecurityLogger:
    def __init__(self, log_file='security.log'):
        self.logger = logging.getLogger('security')
        self.logger.setLevel(logging.INFO)
        
        # Handler pour fichier
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Format JSON pour faciliter l'analyse
        formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
    
    def log_security_event(self, event_type, user_id=None, details=None, severity='INFO'):
        """Logger un événement de sécurité"""
        event = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'severity': severity,
            'user_id': user_id,
            'ip_address': self.get_client_ip(),
            'user_agent': request.headers.get('User-Agent', ''),
            'endpoint': request.endpoint,
            'method': request.method,
            'details': details or {}
        }
        
        self.logger.info(json.dumps(event))
    
    def get_client_ip(self):
        """Obtenir l'IP du client en tenant compte des proxies"""
        if request.headers.get('X-Forwarded-For'):
            return request.headers.get('X-Forwarded-For').split(',')[0].strip()
        elif request.headers.get('X-Real-IP'):
            return request.headers.get('X-Real-IP')
        else:
            return request.remote_addr
    
    def log_login_attempt(self, username, success, reason=None):
        """Logger une tentative de connexion"""
        self.log_security_event(
            event_type='login_attempt',
            user_id=username,
            details={
                'success': success,
                'reason': reason
            },
            severity='WARNING' if not success else 'INFO'
        )
    
    def log_permission_denied(self, user_id, resource, action):
        """Logger un accès refusé"""
        self.log_security_event(
            event_type='permission_denied',
            user_id=user_id,
            details={
                'resource': resource,
                'action': action
            },
            severity='WARNING'
        )
    
    def log_suspicious_activity(self, user_id, activity_type, details):
        """Logger une activité suspecte"""
        self.log_security_event(
            event_type='suspicious_activity',
            user_id=user_id,
            details={
                'activity_type': activity_type,
                'details': details
            },
            severity='CRITICAL'
        )

# Intégration avec Flask
security_logger = SecurityLogger()

@app.before_request
def log_request():
    """Logger les requêtes sensibles"""
    sensitive_endpoints = ['login', 'admin', 'api']
    
    if any(endpoint in request.endpoint for endpoint in sensitive_endpoints):
        security_logger.log_security_event(
            event_type='sensitive_endpoint_access',
            details={'endpoint': request.endpoint}
        )

@app.after_request
def log_response(response):
    """Logger les réponses d'erreur"""
    if response.status_code >= 400:
        security_logger.log_security_event(
            event_type='error_response',
            details={
                'status_code': response.status_code,
                'endpoint': request.endpoint
            },
            severity='WARNING' if response.status_code < 500 else 'ERROR'
        )
    
    return response
```
</div>

</div>

---

## 📚 Pour aller plus loin

<div class="highlight-fact">
🔗 <strong>Ressources complémentaires :</strong>
<ul>
<li><strong>OWASP Top 10</strong> : Guide des vulnérabilités web les plus critiques</li>
<li><strong>Let's Encrypt</strong> : Certificats SSL/TLS gratuits</li>
<li><strong>CNIL</strong> : Guide RGPD et protection des données</li>
<li><strong>Mozilla Observatory</strong> : Test de sécurité des sites web</li>
<li><strong>Burp Suite</strong> : Outil de test de sécurité des applications web</li>
</ul>
</div>

---

## ✅ Points clés à retenir

1. **HTTPS** : Obligatoire pour protéger les communications
2. **Authentification forte** : MFA, sessions sécurisées, mots de passe robustes
3. **Protection XSS/CSRF** : Validation, échappement, CSP
4. **RGPD** : Consentement, droits des utilisateurs, minimisation des données
5. **Monitoring** : Logs de sécurité, détection d'incidents

<div class="highlight-fact">
🎓 <strong>Prochaine étape :</strong> Dans le cours B3.5, nous découvrirons les outils et méthodologies de sécurité (OWASP, Burp Suite, tests de pénétration).
</div>