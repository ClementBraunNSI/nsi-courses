<style>
/* Styles modernes pour le cours Cryptographie BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(155, 89, 182, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
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
    color: #9b59b6;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-left: 5px solid #9b59b6;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #9b59b6;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.crypto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.crypto-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.crypto-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(155, 89, 182, 0.2);
}

.crypto-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.crypto-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.crypto-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(155, 89, 182, 0.1);
    border-left: 4px solid #9b59b6;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.algorithm-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.algorithm-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
}

.algorithm-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(155, 89, 182, 0.2);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #9b59b6;
}

.code-title {
    color: #9b59b6;
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

.cipher-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.cipher-table th, .cipher-table td {
    padding: 0.8rem;
    text-align: center;
    border: 1px solid rgba(155, 89, 182, 0.2);
}

.cipher-table th {
    background: rgba(155, 89, 182, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

.blockchain-step {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.blockchain-title {
    color: #f39c12;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.3 - Cryptographie et Chiffrement</h1>
    <p class="course-subtitle">César, Vigenère, Hash et Blockchain - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Comprendre les principes fondamentaux de la cryptographie
- Implémenter les chiffrements César et Vigenère
- Utiliser les fonctions de hachage pour sécuriser les données
- Appréhender les bases de la blockchain et des cryptomonnaies

---

<div class="concept-section">
<h2 class="section-title">🔐 Fondamentaux de la cryptographie</h2>

<div class="definition-box">
<div class="definition-title">Cryptographie</div>
<div class="definition-content">
Science qui étudie les techniques de chiffrement permettant de protéger des informations en les rendant incompréhensibles sans la clé de déchiffrement appropriée.
</div>
</div>

<h3>Types de cryptographie</h3>

<div class="crypto-grid">
<div class="crypto-card">
<div class="crypto-icon">🔑</div>
<div class="crypto-name">Cryptographie symétrique</div>
<div class="crypto-description">
Utilise la même clé pour chiffrer et déchiffrer. Rapide mais nécessite un échange sécurisé de la clé.
</div>
</div>

<div class="crypto-card">
<div class="crypto-icon">🔐</div>
<div class="crypto-name">Cryptographie asymétrique</div>
<div class="crypto-description">
Utilise une paire de clés (publique/privée). Plus sécurisé pour l'échange mais plus lent.
</div>
</div>

<div class="crypto-card">
<div class="crypto-icon">🔨</div>
<div class="crypto-name">Fonctions de hachage</div>
<div class="crypto-description">
Transforment des données de taille variable en une empreinte de taille fixe. Irréversible et unique.
</div>
</div>
</div>

<div class="highlight-fact">
🔍 <strong>Principe de Kerckhoffs :</strong> La sécurité d'un système cryptographique ne doit reposer que sur le secret de la clé, jamais sur celui de l'algorithme.
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🏛️ Chiffrement de César</h2>

<div class="definition-box">
<div class="definition-title">Chiffrement de César</div>
<div class="definition-content">
Technique de chiffrement par substitution où chaque lettre du texte est remplacée par une lettre située à une position fixe dans l'alphabet (décalage).
</div>
</div>

<h3>Principe du chiffrement César</h3>

<div class="demo-box">
<div class="demo-title">Exemple avec un décalage de 3</div>
<table class="cipher-table">
<tr>
<th>Texte clair</th>
<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td>
</tr>
<tr>
<th>Texte chiffré</th>
<td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td>
</tr>
</table>
<p><strong>Exemple :</strong> "HELLO" → "KHOOR"</p>
</div>

<h3>Implémentation en Python</h3>

<div class="code-example">
<div class="code-title">Chiffrement de César en Python</div>
```python
def chiffrement_cesar(texte, decalage):
    """
    Chiffre un texte avec le chiffrement de César
    """
    resultat = ""
    
    for caractere in texte:
        if caractere.isalpha():
            # Déterminer si c'est une majuscule ou minuscule
            debut = ord('A') if caractere.isupper() else ord('a')
            
            # Appliquer le décalage avec modulo 26
            nouveau_char = chr((ord(caractere) - debut + decalage) % 26 + debut)
            resultat += nouveau_char
        else:
            # Garder les caractères non alphabétiques
            resultat += caractere
    
    return resultat

def dechiffrement_cesar(texte_chiffre, decalage):
    """
    Déchiffre un texte chiffré avec César
    """
    return chiffrement_cesar(texte_chiffre, -decalage)

# Exemple d'utilisation
message = "HELLO WORLD"
message_chiffre = chiffrement_cesar(message, 3)
print(f"Message original : {message}")
print(f"Message chiffré : {message_chiffre}")
print(f"Message déchiffré : {dechiffrement_cesar(message_chiffre, 3)}")
```
</div>

<h3>Cryptanalyse du chiffrement César</h3>

<div class="algorithm-grid">
<div class="algorithm-card">
<h4>🔍 Attaque par force brute</h4>
<p>Tester les 25 clés possibles (décalages de 1 à 25) jusqu'à obtenir un texte cohérent.</p>
</div>

<div class="algorithm-card">
<h4>📊 Analyse fréquentielle</h4>
<p>Analyser la fréquence des lettres et comparer avec les fréquences typiques de la langue.</p>
</div>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔤 Chiffrement de Vigenère</h2>

<div class="definition-box">
<div class="definition-title">Chiffrement de Vigenère</div>
<div class="definition-content">
Amélioration du chiffrement de César utilisant un mot-clé pour varier le décalage. Chaque lettre du message est chiffrée avec un décalage différent basé sur le mot-clé.
</div>
</div>

<h3>Principe du chiffrement Vigenère</h3>

<div class="demo-box">
<div class="demo-title">Exemple avec le mot-clé "KEY"</div>
<table class="cipher-table">
<tr>
<th>Message</th>
<td>H</td><td>E</td><td>L</td><td>L</td><td>O</td><td>W</td><td>O</td><td>R</td><td>L</td><td>D</td>
</tr>
<tr>
<th>Clé répétée</th>
<td>K</td><td>E</td><td>Y</td><td>K</td><td>E</td><td>Y</td><td>K</td><td>E</td><td>Y</td><td>K</td>
</tr>
<tr>
<th>Décalage</th>
<td>10</td><td>4</td><td>24</td><td>10</td><td>4</td><td>24</td><td>10</td><td>4</td><td>24</td><td>10</td>
</tr>
<tr>
<th>Résultat</th>
<td>R</td><td>I</td><td>J</td><td>V</td><td>S</td><td>U</td><td>Y</td><td>V</td><td>J</td><td>N</td>
</tr>
</table>
</div>

<h3>Implémentation en Python</h3>

<div class="code-example">
<div class="code-title">Chiffrement de Vigenère en Python</div>
```python
def chiffrement_vigenere(texte, cle):
    """
    Chiffre un texte avec le chiffrement de Vigenère
    """
    resultat = ""
    cle = cle.upper()
    index_cle = 0
    
    for caractere in texte:
        if caractere.isalpha():
            # Déterminer la base (A ou a)
            debut = ord('A') if caractere.isupper() else ord('a')
            
            # Calculer le décalage basé sur la clé
            decalage = ord(cle[index_cle % len(cle)]) - ord('A')
            
            # Appliquer le chiffrement
            nouveau_char = chr((ord(caractere.upper()) - ord('A') + decalage) % 26 + debut)
            resultat += nouveau_char
            
            index_cle += 1
        else:
            resultat += caractere
    
    return resultat

def dechiffrement_vigenere(texte_chiffre, cle):
    """
    Déchiffre un texte chiffré avec Vigenère
    """
    resultat = ""
    cle = cle.upper()
    index_cle = 0
    
    for caractere in texte_chiffre:
        if caractere.isalpha():
            debut = ord('A') if caractere.isupper() else ord('a')
            decalage = ord(cle[index_cle % len(cle)]) - ord('A')
            
            # Soustraire le décalage pour déchiffrer
            nouveau_char = chr((ord(caractere.upper()) - ord('A') - decalage) % 26 + debut)
            resultat += nouveau_char
            
            index_cle += 1
        else:
            resultat += caractere
    
    return resultat

# Exemple d'utilisation
message = "HELLO WORLD"
cle = "KEY"
message_chiffre = chiffrement_vigenere(message, cle)
print(f"Message : {message}")
print(f"Clé : {cle}")
print(f"Chiffré : {message_chiffre}")
print(f"Déchiffré : {dechiffrement_vigenere(message_chiffre, cle)}")
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔨 Fonctions de hachage</h2>

<div class="definition-box">
<div class="definition-title">Fonction de hachage cryptographique</div>
<div class="definition-content">
Fonction mathématique qui transforme des données de taille arbitraire en une chaîne de caractères de taille fixe (empreinte ou hash). Elle est irréversible et déterministe.
</div>
</div>

<h3>Propriétés des fonctions de hachage</h3>

<div class="algorithm-grid">
<div class="algorithm-card">
<h4>🔄 Déterministe</h4>
<p>La même entrée produit toujours la même sortie.</p>
</div>

<div class="algorithm-card">
<h4>⚡ Rapide</h4>
<p>Calcul efficace de l'empreinte pour toute donnée d'entrée.</p>
</div>

<div class="algorithm-card">
<h4>🌊 Effet avalanche</h4>
<p>Un petit changement dans l'entrée modifie drastiquement la sortie.</p>
</div>

<div class="algorithm-card">
<h4>🔒 Irréversible</h4>
<p>Impossible de retrouver l'entrée à partir de l'empreinte.</p>
</div>

<div class="algorithm-card">
<h4>🎯 Résistance aux collisions</h4>
<p>Très difficile de trouver deux entrées avec la même empreinte.</p>
</div>
</div>

<h3>Utilisation avec Python hashlib</h3>

<div class="code-example">
<div class="code-title">Fonctions de hachage avec hashlib</div>
```python
import hashlib

def calculer_hash(texte, algorithme='sha256'):
    """
    Calcule l'empreinte d'un texte avec l'algorithme spécifié
    """
    # Encoder le texte en bytes
    texte_bytes = texte.encode('utf-8')
    
    # Créer l'objet hash
    if algorithme == 'md5':
        hash_obj = hashlib.md5(texte_bytes)
    elif algorithme == 'sha1':
        hash_obj = hashlib.sha1(texte_bytes)
    elif algorithme == 'sha256':
        hash_obj = hashlib.sha256(texte_bytes)
    elif algorithme == 'sha512':
        hash_obj = hashlib.sha512(texte_bytes)
    else:
        raise ValueError("Algorithme non supporté")
    
    # Retourner l'empreinte en hexadécimal
    return hash_obj.hexdigest()

# Exemples d'utilisation
message = "Hello World"
print(f"Message : {message}")
print(f"MD5    : {calculer_hash(message, 'md5')}")
print(f"SHA1   : {calculer_hash(message, 'sha1')}")
print(f"SHA256 : {calculer_hash(message, 'sha256')}")
print(f"SHA512 : {calculer_hash(message, 'sha512')}")

# Démonstration de l'effet avalanche
print(f"\nEffet avalanche :")
print(f"'Hello World'  : {calculer_hash('Hello World')}")
print(f"'Hello World!' : {calculer_hash('Hello World!')}")
```
</div>

<h3>Applications des fonctions de hachage</h3>

<div class="highlight-fact">
🔧 <strong>Utilisations courantes :</strong>
<ul>
<li><strong>Stockage de mots de passe</strong> : Jamais en clair, toujours hachés</li>
<li><strong>Intégrité des données</strong> : Vérifier qu'un fichier n'a pas été modifié</li>
<li><strong>Signatures numériques</strong> : Authentification et non-répudiation</li>
<li><strong>Blockchain</strong> : Chaînage des blocs et preuve de travail</li>
<li><strong>Tables de hachage</strong> : Structures de données efficaces</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">⛓️ Introduction à la Blockchain</h2>

<div class="definition-box">
<div class="definition-title">Blockchain</div>
<div class="definition-content">
Technologie de stockage et de transmission d'informations, transparente et sécurisée, fonctionnant sans organe central de contrôle. Elle constitue une base de données distribuée et immuable.
</div>
</div>

<h3>Structure d'un bloc</h3>

<div class="blockchain-step">
<div class="blockchain-title">🧱 Composants d'un bloc</div>
<ul>
<li><strong>Hash du bloc précédent</strong> : Lien cryptographique</li>
<li><strong>Timestamp</strong> : Horodatage de création</li>
<li><strong>Données</strong> : Transactions ou informations</li>
<li><strong>Nonce</strong> : Nombre utilisé une seule fois (proof of work)</li>
<li><strong>Hash du bloc</strong> : Empreinte unique du bloc</li>
</ul>
</div>

<h3>Implémentation simple d'une blockchain</h3>

<div class="code-example">
<div class="code-title">Blockchain basique en Python</div>
```python
import hashlib
import time
import json

class Bloc:
    def __init__(self, donnees, hash_precedent):
        self.timestamp = time.time()
        self.donnees = donnees
        self.hash_precedent = hash_precedent
        self.nonce = 0
        self.hash = self.calculer_hash()
    
    def calculer_hash(self):
        """Calcule le hash du bloc"""
        contenu = f"{self.hash_precedent}{self.timestamp}{self.donnees}{self.nonce}"
        return hashlib.sha256(contenu.encode()).hexdigest()
    
    def miner_bloc(self, difficulte):
        """Mine le bloc avec une difficulté donnée (proof of work)"""
        cible = "0" * difficulte
        
        while self.hash[:difficulte] != cible:
            self.nonce += 1
            self.hash = self.calculer_hash()
        
        print(f"Bloc miné : {self.hash}")

class Blockchain:
    def __init__(self):
        self.chaine = [self.creer_bloc_genese()]
        self.difficulte = 2
    
    def creer_bloc_genese(self):
        """Crée le premier bloc de la chaîne"""
        return Bloc("Bloc Genèse", "0")
    
    def obtenir_dernier_bloc(self):
        """Retourne le dernier bloc de la chaîne"""
        return self.chaine[-1]
    
    def ajouter_bloc(self, nouveau_bloc):
        """Ajoute un nouveau bloc à la chaîne"""
        nouveau_bloc.hash_precedent = self.obtenir_dernier_bloc().hash
        nouveau_bloc.miner_bloc(self.difficulte)
        self.chaine.append(nouveau_bloc)
    
    def valider_chaine(self):
        """Vérifie l'intégrité de la blockchain"""
        for i in range(1, len(self.chaine)):
            bloc_actuel = self.chaine[i]
            bloc_precedent = self.chaine[i-1]
            
            # Vérifier le hash du bloc
            if bloc_actuel.hash != bloc_actuel.calculer_hash():
                return False
            
            # Vérifier le lien avec le bloc précédent
            if bloc_actuel.hash_precedent != bloc_precedent.hash:
                return False
        
        return True

# Exemple d'utilisation
blockchain = Blockchain()

print("Création de la blockchain...")
blockchain.ajouter_bloc(Bloc("Transaction 1: Alice -> Bob 10€", ""))
blockchain.ajouter_bloc(Bloc("Transaction 2: Bob -> Charlie 5€", ""))

print(f"\nBlockchain valide : {blockchain.valider_chaine()}")
```
</div>

<h3>Caractéristiques de la blockchain</h3>

<div class="crypto-grid">
<div class="crypto-card">
<div class="crypto-icon">🔗</div>
<div class="crypto-name">Immutabilité</div>
<div class="crypto-description">
Une fois ajoutées, les données ne peuvent plus être modifiées sans altérer toute la chaîne.
</div>
</div>

<div class="crypto-card">
<div class="crypto-icon">🌐</div>
<div class="crypto-name">Décentralisation</div>
<div class="crypto-description">
Aucune autorité centrale, le réseau est distribué entre tous les participants.
</div>
</div>

<div class="crypto-card">
<div class="crypto-icon">👁️</div>
<div class="crypto-name">Transparence</div>
<div class="crypto-description">
Toutes les transactions sont visibles et vérifiables par tous les participants.
</div>
</div>

<div class="crypto-card">
<div class="crypto-icon">🔐</div>
<div class="crypto-name">Sécurité</div>
<div class="crypto-description">
Protection cryptographique et consensus distribué pour garantir l'intégrité.
</div>
</div>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">💰 Applications et cryptomonnaies</h2>

### Domaines d'application

<div class="algorithm-grid">
<div class="algorithm-card">
<h4>💳 Cryptomonnaies</h4>
<p>Bitcoin, Ethereum, monnaies numériques décentralisées</p>
</div>

<div class="algorithm-card">
<h4>📜 Contrats intelligents</h4>
<p>Automatisation d'accords sans intermédiaire</p>
</div>

<div class="algorithm-card">
<h4>🏥 Santé</h4>
<p>Dossiers médicaux sécurisés et traçables</p>
</div>

<div class="algorithm-card">
<h4>🗳️ Vote électronique</h4>
<p>Systèmes de vote transparents et vérifiables</p>
</div>

<div class="algorithm-card">
<h4>📦 Supply Chain</h4>
<p>Traçabilité des produits de la production au consommateur</p>
</div>

<div class="algorithm-card">
<h4>🎓 Certification</h4>
<p>Diplômes et certifications infalsifiables</p>
</div>
</div>

<div class="highlight-fact">
⚡ <strong>Défis de la blockchain :</strong>
<ul>
<li><strong>Consommation énergétique</strong> : Le minage nécessite beaucoup d'énergie</li>
<li><strong>Scalabilité</strong> : Limitation du nombre de transactions par seconde</li>
<li><strong>Régulation</strong> : Cadre juridique en évolution</li>
<li><strong>Adoption</strong> : Nécessité de former les utilisateurs</li>
</ul>
</div>

</div>

---

## 📚 Pour aller plus loin

<div class="highlight-fact">
🔗 <strong>Ressources complémentaires :</strong>
<ul>
<li><strong>Cryptool</strong> : Logiciel éducatif pour la cryptographie</li>
<li><strong>Python cryptography</strong> : Bibliothèque avancée</li>
<li><strong>OpenSSL</strong> : Outils cryptographiques en ligne de commande</li>
<li><strong>Blockchain.info</strong> : Explorateur de blockchain Bitcoin</li>
</ul>
</div>

---

## ✅ Points clés à retenir

1. **César** : Chiffrement par substitution simple, facilement cassable
2. **Vigenère** : Amélioration avec mot-clé, plus résistant
3. **Hachage** : Irréversible, utilisé pour l'intégrité et l'authentification
4. **Blockchain** : Registre distribué et immuable
5. **Applications** : De la sécurisation des mots de passe aux cryptomonnaies

<div class="highlight-fact">
🎓 <strong>Prochaine étape :</strong> Dans le cours B3.4, nous étudierons la sécurité des applications web et la protection des données.
</div>