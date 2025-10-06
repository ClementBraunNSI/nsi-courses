<style>
/* Styles modernes pour le cours Outils Sécurité BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(230, 126, 34, 0.1), rgba(211, 84, 0, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(230, 126, 34, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
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
    color: #e67e22;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(230, 126, 34, 0.1), rgba(211, 84, 0, 0.05));
    border-left: 5px solid #e67e22;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #e67e22;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.tool-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(230, 126, 34, 0.2);
}

.tool-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.tool-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.tool-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(230, 126, 34, 0.1);
    border-left: 4px solid #e67e22;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.methodology-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.methodology-card {
    background: linear-gradient(135deg, rgba(230, 126, 34, 0.1), rgba(211, 84, 0, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(230, 126, 34, 0.2);
    transition: all 0.3s ease;
}

.methodology-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(230, 126, 34, 0.2);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #e67e22;
}

.code-title {
    color: #e67e22;
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

.owasp-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.owasp-table th, .owasp-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(230, 126, 34, 0.2);
}

.owasp-table th {
    background: rgba(230, 126, 34, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

.pentest-step {
    background: rgba(155, 89, 182, 0.1);
    border-left: 4px solid #9b59b6;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.pentest-title {
    color: #9b59b6;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.burp-feature {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 6px;
}

.burp-feature-title {
    color: #3498db;
    font-weight: 600;
    margin-bottom: 0.3rem;
    font-size: 0.9rem;
}

/* Styles pour les titres h3 */
h3 {
    font-size: 1.8rem;
    font-weight: 600;
    color: #e67e22;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(230, 126, 34, 0.3);
    background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.5 - Outils et Méthodologies</h1>
    <p class="course-subtitle">OWASP, Burp Suite et Tests de Sécurité - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Utiliser les ressources et outils OWASP pour la sécurité web
- Maîtriser Burp Suite pour les tests de sécurité
- Mettre en place une méthodologie de tests de pénétration
- Analyser et documenter les vulnérabilités découvertes

---

<div class="concept-section">
<h2 class="section-title">🛡️ OWASP (Open Web Application Security Project)</h2>

<div class="definition-box">
<div class="definition-title">OWASP</div>
<div class="definition-content">
Organisation internationale à but non lucratif dédiée à l'amélioration de la sécurité des applications web. Elle fournit des ressources, outils et standards gratuits pour la communauté de la sécurité informatique.
</div>
</div>

<h3>Ressources principales OWASP</h3>

<div class="tools-grid">
<div class="tool-card">
<div class="tool-icon">🔟</div>
<div class="tool-name">OWASP Top 10</div>
<div class="tool-description">
Liste des 10 vulnérabilités web les plus critiques, mise à jour tous les 3-4 ans. Guide de référence pour les développeurs et testeurs.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">📋</div>
<div class="tool-name">ASVS</div>
<div class="tool-description">
Application Security Verification Standard - Standard de vérification de la sécurité des applications avec différents niveaux de maturité.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🧪</div>
<div class="tool-name">Testing Guide</div>
<div class="tool-description">
Guide complet de tests de sécurité des applications web avec méthodologies et techniques détaillées.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🔧</div>
<div class="tool-name">ZAP</div>
<div class="tool-description">
Zed Attack Proxy - Scanner de vulnérabilités web gratuit et open source, alternative à Burp Suite.
</div>
</div>
</div>

<h3>OWASP Top 10 - 2021</h3>

<table class="owasp-table">
<thead>
<tr>
<th>Rang</th>
<th>Vulnérabilité</th>
<th>Impact</th>
<th>Outils de détection</th>
</tr>
</thead>
<tbody>
<tr>
<td>A01</td>
<td>Broken Access Control</td>
<td>Accès non autorisé aux données</td>
<td>Burp Suite, ZAP, tests manuels</td>
</tr>
<tr>
<td>A02</td>
<td>Cryptographic Failures</td>
<td>Exposition de données sensibles</td>
<td>SSLyze, testssl.sh, Nmap</td>
</tr>
<tr>
<td>A03</td>
<td>Injection</td>
<td>Exécution de code malveillant</td>
<td>SQLMap, Burp Suite, ZAP</td>
</tr>
<tr>
<td>A04</td>
<td>Insecure Design</td>
<td>Failles architecturales</td>
<td>Revue de code, threat modeling</td>
</tr>
<tr>
<td>A05</td>
<td>Security Misconfiguration</td>
<td>Exposition de services</td>
<td>Nessus, OpenVAS, Nikto</td>
</tr>
<tr>
<td>A06</td>
<td>Vulnerable Components</td>
<td>Exploitation de CVE connues</td>
<td>OWASP Dependency Check</td>
</tr>
<tr>
<td>A07</td>
<td>Authentication Failures</td>
<td>Usurpation d'identité</td>
<td>Hydra, Burp Intruder</td>
</tr>
<tr>
<td>A08</td>
<td>Software Integrity Failures</td>
<td>Code malveillant</td>
<td>Analyse statique, SCA</td>
</tr>
<tr>
<td>A09</td>
<td>Logging Failures</td>
<td>Détection d'incidents limitée</td>
<td>Audit manuel, SIEM</td>
</tr>
<tr>
<td>A10</td>
<td>Server-Side Request Forgery</td>
<td>Accès aux ressources internes</td>
<td>Burp Suite, tests manuels</td>
</tr>
</tbody>
</table>

<h3>Installation et utilisation d'OWASP ZAP</h3>

<div class="code-example">
<div class="code-title">Installation et configuration d'OWASP ZAP</div>
```bash
# Installation sur macOS avec Homebrew
brew install --cask owasp-zap

# Installation sur Ubuntu/Debian
sudo apt update
sudo apt install zaproxy

# Installation via Docker
docker run -u zap -p 8080:8080 -p 8090:8090 \
  -v $(pwd):/zap/wrk/:rw \
  -t owasp/zap2docker-stable zap-webswing.sh

# Lancement en mode daemon (API)
zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.addrs.addr.name=.* \
  -config api.addrs.addr.regex=true

# Script Python pour automatiser ZAP
import time
from zapv2 import ZAPv2

# Configuration ZAP
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 
                     'https': 'http://127.0.0.1:8080'})

# URL cible
target = 'http://example.com'

print('Démarrage du scan passif...')
# Accéder à l'URL cible
zap.urlopen(target)
time.sleep(2)

print('Démarrage du spider...')
# Lancer le spider pour découvrir les URLs
scanid = zap.spider.scan(target)
time.sleep(2)

# Attendre la fin du spider
while int(zap.spider.status(scanid)) < 100:
    print(f'Progression spider: {zap.spider.status(scanid)}%')
    time.sleep(5)

print('Spider terminé')

print('Démarrage du scan actif...')
# Lancer le scan actif
scanid = zap.ascan.scan(target)

# Attendre la fin du scan
while int(zap.ascan.status(scanid)) < 100:
    print(f'Progression scan: {zap.ascan.status(scanid)}%')
    time.sleep(5)

print('Scan terminé')

# Récupérer les alertes
print('Alertes trouvées:')
alerts = zap.core.alerts()
for alert in alerts:
    print(f"- {alert['risk']} : {alert['alert']} dans {alert['url']}")

# Générer un rapport HTML
with open('rapport_zap.html', 'w') as f:
    f.write(zap.core.htmlreport())

print('Rapport généré: rapport_zap.html')
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔍 Burp Suite</h2>

<div class="definition-box">
<div class="definition-title">Burp Suite</div>
<div class="definition-content">
Plateforme intégrée pour les tests de sécurité des applications web. Outil de référence utilisé par les professionnels de la sécurité pour identifier et exploiter les vulnérabilités web.
</div>
</div>

<h3>Composants principaux de Burp Suite</h3>

<div class="tools-grid">
<div class="tool-card">
<div class="tool-icon">🔄</div>
<div class="tool-name">Proxy</div>
<div class="tool-description">
Intercepte et modifie le trafic HTTP/HTTPS entre le navigateur et l'application web pour analyser les requêtes et réponses.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🕷️</div>
<div class="tool-name">Spider</div>
<div class="tool-description">
Explore automatiquement l'application web pour découvrir le contenu et cartographier la surface d'attaque.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🎯</div>
<div class="tool-name">Scanner</div>
<div class="tool-description">
Effectue des tests automatisés pour identifier les vulnérabilités courantes (injection SQL, XSS, etc.).
</div>
</div>

<div class="tool-card">
<div class="tool-icon">💥</div>
<div class="tool-name">Intruder</div>
<div class="tool-description">
Outil d'attaque automatisée pour tester les paramètres avec différentes charges utiles (brute force, fuzzing).
</div>
</div>

<div class="tool-card">
<div class="tool-name">Repeater</div>
<div class="tool-description">
Permet de modifier et renvoyer manuellement des requêtes HTTP pour tester des vulnérabilités spécifiques.
</div>
</div>

<div class="tool-card">
<div class="tool-name">Sequencer</div>
<div class="tool-description">
Analyse la qualité de la randomisation des tokens de session et autres identifiants.
</div>
</div>
</div>

<h3>Configuration et utilisation de Burp Suite</h3>

<div class="demo-box">
<div class="demo-title">Configuration initiale</div>
<ol>
<li><strong>Installation :</strong> Télécharger depuis portswigger.net</li>
<li><strong>Proxy :</strong> Configurer le navigateur sur 127.0.0.1:8080</li>
<li><strong>Certificat :</strong> Installer le certificat CA de Burp pour HTTPS</li>
<li><strong>Scope :</strong> Définir le périmètre de test dans Target > Scope</li>
</ol>
</div>

<h3>Fonctionnalités avancées de Burp Suite</h3>

<div class="burp-feature">
<div class="burp-feature-title">🔍 Proxy Intercept</div>
Intercepter et modifier les requêtes en temps réel pour tester différents scénarios d'attaque.
</div>

<div class="burp-feature">
<div class="burp-feature-title">🎯 Target Sitemap</div>
Visualiser l'arborescence complète de l'application et identifier les endpoints sensibles.
</div>

<div class="burp-feature">
<div class="burp-feature-title">🔄 Match and Replace</div>
Automatiser la modification de requêtes avec des règles de remplacement.
</div>

<div class="burp-feature">
<div class="burp-feature-title">📊 Logger</div>
Enregistrer tout le trafic HTTP pour analyse ultérieure et génération de rapports.
</div>

<div class="burp-feature">
<div class="burp-feature-title">🔌 Extensions</div>
Étendre les fonctionnalités avec des plugins (BApp Store) pour des tests spécialisés.
</div>

<h3>Exemple pratique : Test d'injection SQL avec Burp</h3>

<div class="code-example">
<div class="code-title">Méthodologie de test d'injection SQL</div>
```
1. RECONNAISSANCE
   - Identifier les paramètres d'entrée (GET, POST, cookies, headers)
   - Cartographier l'application avec Spider
   - Analyser les réponses pour détecter les bases de données

2. DÉTECTION
   - Injecter des caractères spéciaux : ' " ; --
   - Observer les erreurs SQL dans les réponses
   - Tester les délais avec SLEEP() ou WAITFOR

3. EXPLOITATION
   - Déterminer le nombre de colonnes : ORDER BY 1,2,3...
   - Identifier les colonnes affichées : UNION SELECT 1,2,3...
   - Extraire les données : UNION SELECT user(),database(),version()

4. ENUMÉRATION
   - Lister les bases de données : UNION SELECT schema_name FROM information_schema.schemata
   - Lister les tables : UNION SELECT table_name FROM information_schema.tables
   - Lister les colonnes : UNION SELECT column_name FROM information_schema.columns

Exemple de payload dans Burp Intruder :
- Position : id=§1§
- Payloads :
  * 1' OR '1'='1
  * 1' UNION SELECT 1,2,3--
  * 1' AND SLEEP(5)--
  * 1'; DROP TABLE users;--
```
</div>

<h3>Extensions Burp Suite utiles</h3>

<div class="methodology-grid">
<div class="methodology-card">
<h4>🔍 SQLiPy</h4>
<p>Détection automatisée des injections SQL avec différentes techniques d'exploitation.</p>
</div>

<div class="methodology-card">
<h4>🎯 Autorize</h4>
<p>Test automatique des contrôles d'accès et détection des vulnérabilités d'autorisation.</p>
</div>

<div class="methodology-card">
<h4>📊 Logger++</h4>
<p>Logging avancé avec filtres personnalisables et export des données.</p>
</div>

<div class="methodology-card">
<h4>🔐 JWT Editor</h4>
<p>Manipulation et test des JSON Web Tokens pour identifier les failles d'authentification.</p>
</div>

<div class="methodology-card">
<h4>🌐 Param Miner</h4>
<p>Découverte de paramètres cachés et d'endpoints non documentés.</p>
</div>

<div class="methodology-card">
<h4>🔄 Turbo Intruder</h4>
<p>Attaques haute performance avec scripts Python personnalisés.</p>
</div>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🎯 Méthodologie de tests de pénétration</h2>

<div class="definition-box">
<div class="definition-title">Test de pénétration (Pentest)</div>
<div class="definition-content">
Évaluation de sécurité autorisée qui simule une attaque réelle pour identifier les vulnérabilités exploitables dans un système, une application ou un réseau.
</div>
</div>

<h3>Phases d'un test de pénétration</h3>

<div class="pentest-step">
<div class="pentest-title">1. 📋 Planification et reconnaissance</div>
<ul>
<li><strong>Définition du scope :</strong> Périmètre, objectifs, contraintes</li>
<li><strong>Reconnaissance passive :</strong> OSINT, DNS, réseaux sociaux</li>
<li><strong>Reconnaissance active :</strong> Scan de ports, énumération de services</li>
</ul>
</div>

<div class="pentest-step">
<div class="pentest-title">2. 🔍 Analyse et énumération</div>
<ul>
<li><strong>Cartographie :</strong> Architecture, technologies, versions</li>
<li><strong>Identification des services :</strong> Web, SSH, FTP, bases de données</li>
<li><strong>Analyse des applications :</strong> Fonctionnalités, authentification</li>
</ul>
</div>

<div class="pentest-step">
<div class="pentest-title">3. 🎯 Recherche de vulnérabilités</div>
<ul>
<li><strong>Scan automatisé :</strong> Nessus, OpenVAS, Burp Scanner</li>
<li><strong>Tests manuels :</strong> Injection, XSS, CSRF, logique métier</li>
<li><strong>Analyse de configuration :</strong> Permissions, chiffrement</li>
</ul>
</div>

<div class="pentest-step">
<div class="pentest-title">4. 💥 Exploitation</div>
<ul>
<li><strong>Proof of Concept :</strong> Démonstration contrôlée</li>
<li><strong>Élévation de privilèges :</strong> Accès administrateur</li>
<li><strong>Mouvement latéral :</strong> Compromission d'autres systèmes</li>
</ul>
</div>

<div class="pentest-step">
<div class="pentest-title">5. 📊 Documentation et rapport</div>
<ul>
<li><strong>Classification des risques :</strong> CVSS, impact métier</li>
<li><strong>Recommandations :</strong> Correctifs prioritaires</li>
<li><strong>Preuves :</strong> Captures d'écran, logs, payloads</li>
</ul>
</div>

<h3>Outils de reconnaissance et énumération</h3>

<div class="code-example">
<div class="code-title">Scripts de reconnaissance automatisée</div>
```bash
#!/bin/bash
# Script de reconnaissance automatisée

TARGET=$1
OUTPUT_DIR="pentest_$TARGET"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target_domain>"
    exit 1
fi

mkdir -p $OUTPUT_DIR
cd $OUTPUT_DIR

echo "[+] Démarrage de la reconnaissance pour $TARGET"

# 1. Reconnaissance DNS
echo "[+] Énumération DNS..."
dig $TARGET > dns_info.txt
nslookup $TARGET >> dns_info.txt

# Recherche de sous-domaines
echo "[+] Recherche de sous-domaines..."
sublist3r -d $TARGET -o subdomains.txt

# 2. Scan de ports
echo "[+] Scan de ports avec Nmap..."
nmap -sS -sV -O -A $TARGET -oA nmap_scan

# Scan complet des ports
nmap -p- --min-rate=1000 -T4 $TARGET -oA nmap_full_scan

# 3. Énumération web
echo "[+] Énumération des répertoires web..."
if nmap -p 80,443 $TARGET | grep -q "open"; then
    # Découverte de répertoires
    dirb http://$TARGET /usr/share/dirb/wordlists/common.txt -o dirb_results.txt
    
    # Scan avec Nikto
    nikto -h http://$TARGET -o nikto_results.txt
    
    # Énumération avec gobuster
    gobuster dir -u http://$TARGET -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster_results.txt
fi

# 4. Recherche d'informations OSINT
echo "[+] Collecte d'informations OSINT..."
# theHarvester pour emails et sous-domaines
theHarvester -d $TARGET -l 500 -b google,bing,linkedin > osint_info.txt

# 5. Analyse SSL/TLS
echo "[+] Analyse SSL/TLS..."
if nmap -p 443 $TARGET | grep -q "open"; then
    sslscan $TARGET > ssl_analysis.txt
    testssl.sh $TARGET >> ssl_analysis.txt
fi

echo "[+] Reconnaissance terminée. Résultats dans $OUTPUT_DIR"
```
</div>

<h3>Framework de test d'applications web</h3>

<div class="code-example">
<div class="code-title">Checklist de test d'application web</div>
```python
#!/usr/bin/env python3
"""
Framework de test de sécurité d'applications web
Basé sur OWASP Testing Guide v4
"""

import requests
import re
from urllib.parse import urljoin, urlparse
import time

class WebAppTester:
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session or requests.Session()
        self.vulnerabilities = []
        
        # Configuration des headers
        self.session.headers.update({
            'User-Agent': 'WebAppTester/1.0'
        })
    
    def log_vulnerability(self, vuln_type, url, description, severity='Medium'):
        """Enregistrer une vulnérabilité trouvée"""
        vuln = {
            'type': vuln_type,
            'url': url,
            'description': description,
            'severity': severity,
            'timestamp': time.time()
        }
        self.vulnerabilities.append(vuln)
        print(f"[{severity}] {vuln_type} trouvé dans {url}")
    
    def test_sql_injection(self, url, params):
        """Test d'injection SQL"""
        sql_payloads = [
            "' OR '1'='1",
            "' UNION SELECT 1,2,3--",
            "'; DROP TABLE users;--",
            "' AND SLEEP(5)--"
        ]
        
        for param in params:
            for payload in sql_payloads:
                test_params = params.copy()
                test_params[param] = payload
                
                try:
                    start_time = time.time()
                    response = self.session.get(url, params=test_params, timeout=10)
                    response_time = time.time() - start_time
                    
                    # Détection par erreur SQL
                    sql_errors = [
                        'mysql_fetch_array',
                        'ORA-01756',
                        'Microsoft OLE DB Provider',
                        'PostgreSQL query failed',
                        'SQLite/JDBCDriver'
                    ]
                    
                    for error in sql_errors:
                        if error.lower() in response.text.lower():
                            self.log_vulnerability(
                                'SQL Injection',
                                f"{url}?{param}={payload}",
                                f"Erreur SQL détectée avec payload: {payload}",
                                'High'
                            )
                    
                    # Détection par délai (time-based)
                    if 'SLEEP' in payload and response_time > 4:
                        self.log_vulnerability(
                            'Time-based SQL Injection',
                            f"{url}?{param}={payload}",
                            f"Délai de {response_time:.2f}s détecté",
                            'High'
                        )
                        
                except requests.RequestException as e:
                    print(f"Erreur lors du test SQL: {e}")
    
    def test_xss(self, url, params):
        """Test de Cross-Site Scripting"""
        xss_payloads = [
            '<script>alert("XSS")</script>',
            '"><script>alert("XSS")</script>',
            "javascript:alert('XSS')",
            '<img src=x onerror=alert("XSS")>',
            '<svg onload=alert("XSS")>'
        ]
        
        for param in params:
            for payload in xss_payloads:
                test_params = params.copy()
                test_params[param] = payload
                
                try:
                    response = self.session.get(url, params=test_params)
                    
                    # Vérifier si le payload est reflété sans échappement
                    if payload in response.text:
                        self.log_vulnerability(
                            'Reflected XSS',
                            f"{url}?{param}={payload}",
                            f"Payload XSS reflété: {payload}",
                            'High'
                        )
                        
                except requests.RequestException as e:
                    print(f"Erreur lors du test XSS: {e}")
    
    def test_directory_traversal(self, url, params):
        """Test de Directory Traversal"""
        traversal_payloads = [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32\\drivers\\etc\\hosts',
            '....//....//....//etc/passwd',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd'
        ]
        
        for param in params:
            for payload in traversal_payloads:
                test_params = params.copy()
                test_params[param] = payload
                
                try:
                    response = self.session.get(url, params=test_params)
                    
                    # Rechercher des signatures de fichiers système
                    if re.search(r'root:.*:0:0:', response.text) or \
                       'localhost' in response.text.lower():
                        self.log_vulnerability(
                            'Directory Traversal',
                            f"{url}?{param}={payload}",
                            f"Accès à des fichiers système détecté",
                            'High'
                        )
                        
                except requests.RequestException as e:
                    print(f"Erreur lors du test Directory Traversal: {e}")
    
    def test_security_headers(self, url):
        """Vérifier les en-têtes de sécurité"""
        try:
            response = self.session.get(url)
            headers = response.headers
            
            security_headers = {
                'X-Frame-Options': 'Protection contre le clickjacking',
                'X-XSS-Protection': 'Protection XSS du navigateur',
                'X-Content-Type-Options': 'Protection contre le MIME sniffing',
                'Strict-Transport-Security': 'Forcer HTTPS',
                'Content-Security-Policy': 'Politique de sécurité du contenu'
            }
            
            for header, description in security_headers.items():
                if header not in headers:
                    self.log_vulnerability(
                        'Missing Security Header',
                        url,
                        f"En-tête manquant: {header} - {description}",
                        'Low'
                    )
                    
        except requests.RequestException as e:
            print(f"Erreur lors du test des en-têtes: {e}")
    
    def run_full_test(self, test_urls):
        """Exécuter tous les tests"""
        print(f"[+] Démarrage des tests sur {self.base_url}")
        
        for url_path, params in test_urls.items():
            full_url = urljoin(self.base_url, url_path)
            print(f"[+] Test de {full_url}")
            
            # Tests de vulnérabilités
            self.test_sql_injection(full_url, params)
            self.test_xss(full_url, params)
            self.test_directory_traversal(full_url, params)
            self.test_security_headers(full_url)
        
        # Rapport final
        self.generate_report()
    
    def generate_report(self):
        """Générer un rapport des vulnérabilités"""
        print("\n" + "="*50)
        print("RAPPORT DE SÉCURITÉ")
        print("="*50)
        
        if not self.vulnerabilities:
            print("Aucune vulnérabilité détectée.")
            return
        
        # Grouper par sévérité
        by_severity = {}
        for vuln in self.vulnerabilities:
            severity = vuln['severity']
            if severity not in by_severity:
                by_severity[severity] = []
            by_severity[severity].append(vuln)
        
        # Afficher par ordre de sévérité
        for severity in ['Critical', 'High', 'Medium', 'Low']:
            if severity in by_severity:
                print(f"\n{severity.upper()} ({len(by_severity[severity])} vulnérabilités):")
                for vuln in by_severity[severity]:
                    print(f"  - {vuln['type']}: {vuln['description']}")
                    print(f"    URL: {vuln['url']}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Configuration des tests
    target_url = "http://testphp.vulnweb.com"
    
    test_endpoints = {
        "/artists.php": {"artist": "1"},
        "/search.php": {"searchFor": "test"},
        "/login.php": {"uname": "admin", "pass": "password"}
    }
    
    # Lancement des tests
    tester = WebAppTester(target_url)
    tester.run_full_test(test_endpoints)
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔧 Autres outils de sécurité</h2>

<h3>Outils de scan de vulnérabilités</h3>

<div class="tools-grid">
<div class="tool-card">
<div class="tool-icon">🔍</div>
<div class="tool-name">Nessus</div>
<div class="tool-description">
Scanner de vulnérabilités commercial avec une large base de plugins pour détecter les failles de sécurité.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🆓</div>
<div class="tool-name">OpenVAS</div>
<div class="tool-description">
Alternative open source à Nessus, scanner complet avec interface web et rapports détaillés.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🌐</div>
<div class="tool-name">Nikto</div>
<div class="tool-description">
Scanner web spécialisé dans la détection de vulnérabilités et configurations dangereuses des serveurs web.
</div>
</div>

<div class="tool-card">
<div class="tool-icon">🗂️</div>
<div class="tool-name">DirBuster</div>
<div class="tool-description">
Outil de découverte de répertoires et fichiers cachés sur les serveurs web par force brute.
</div>
</div>
</div>

<h3>Outils d'analyse de code</h3>

<div class="methodology-grid">
<div class="methodology-card">
<h4>🔍 SonarQube</h4>
<p>Analyse statique de code pour détecter les vulnérabilités, bugs et code smells.</p>
</div>

<div class="methodology-card">
<h4>🛡️ Bandit</h4>
<p>Scanner de sécurité spécialisé pour le code Python, détecte les pratiques dangereuses.</p>
</div>

<div class="methodology-card">
<h4>📦 OWASP Dependency Check</h4>
<p>Analyse les dépendances pour identifier les composants avec des vulnérabilités connues.</p>
</div>

<div class="methodology-card">
<h4>🔐 Semgrep</h4>
<p>Outil d'analyse statique multi-langages avec règles de sécurité personnalisables.</p>
</div>
</div>

<h3>Installation et utilisation d'outils de sécurité</h3>

<div class="code-example">
<div class="code-title">Installation et configuration d'outils essentiels</div>
```bash
#!/bin/bash
# Script d'installation d'outils de sécurité

echo "[+] Installation des outils de sécurité..."

# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Outils de base
sudo apt install -y nmap nikto dirb gobuster hydra john sqlmap

# Installation de Burp Suite Community
wget -O burpsuite.sh "https://portswigger.net/burp/releases/download?product=community&type=Linux"
chmod +x burpsuite.sh
sudo ./burpsuite.sh

# Installation d'OWASP ZAP
sudo apt install -y zaproxy

# Installation de Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
sudo ./msfinstall

# Outils Python
pip3 install requests beautifulsoup4 python-nmap

# Configuration de Burp Suite
echo "[+] Configuration de Burp Suite..."
mkdir -p ~/.java/.userPrefs/burp
cat > ~/.java/.userPrefs/burp/prefs.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE preferences SYSTEM "http://java.sun.com/dtd/preferences.dtd">
<preferences EXTERNAL_XML_VERSION="1.0">
  <root type="user">
    <map>
      <entry key="burp.proxy.listener.port" value="8080"/>
      <entry key="burp.proxy.listener.interface" value="127.0.0.1"/>
    </map>
  </root>
</preferences>
EOF

echo "[+] Installation terminée!"
echo "Outils installés:"
echo "- Nmap (scan de ports)"
echo "- Nikto (scan web)"
echo "- Dirb/Gobuster (découverte de répertoires)"
echo "- Hydra (brute force)"
echo "- SQLMap (injection SQL)"
echo "- Burp Suite (proxy/scanner web)"
echo "- OWASP ZAP (scanner web)"
echo "- Metasploit (framework d'exploitation)"
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">📊 Documentation et rapport</h2>

<h3>Structure d'un rapport de test de pénétration</h3>

<div class="demo-box">
<div class="demo-title">Sections principales du rapport</div>
<ol>
<li><strong>Résumé exécutif :</strong> Synthèse pour la direction</li>
<li><strong>Méthodologie :</strong> Approche et outils utilisés</li>
<li><strong>Résultats :</strong> Vulnérabilités par ordre de criticité</li>
<li><strong>Recommandations :</strong> Mesures correctives prioritaires</li>
<li><strong>Annexes :</strong> Détails techniques et preuves</li>
</ol>
</div>

### Classification des risques

<table class="owasp-table">
<thead>
<tr>
<th>Sévérité</th>
<th>Score CVSS</th>
<th>Impact</th>
<th>Délai de correction</th>
</tr>
</thead>
<tbody>
<tr style="background-color: rgba(231, 76, 60, 0.1);">
<td><strong>Critique</strong></td>
<td>9.0 - 10.0</td>
<td>Compromission totale du système</td>
<td>Immédiat (24h)</td>
</tr>
<tr style="background-color: rgba(230, 126, 34, 0.1);">
<td><strong>Élevé</strong></td>
<td>7.0 - 8.9</td>
<td>Accès non autorisé aux données</td>
<td>1 semaine</td>
</tr>
<tr style="background-color: rgba(241, 196, 15, 0.1);">
<td><strong>Moyen</strong></td>
<td>4.0 - 6.9</td>
<td>Exposition d'informations</td>
<td>1 mois</td>
</tr>
<tr style="background-color: rgba(46, 204, 113, 0.1);">
<td><strong>Faible</strong></td>
<td>0.1 - 3.9</td>
<td>Impact limité</td>
<td>3 mois</td>
</tr>
</tbody>
</table>

<div class="highlight-fact">
💡 <strong>Bonnes pratiques pour les rapports :</strong>
<ul>
<li><strong>Preuves visuelles :</strong> Captures d'écran annotées</li>
<li><strong>Reproductibilité :</strong> Steps détaillés pour reproduire</li>
<li><strong>Impact métier :</strong> Conséquences concrètes</li>
<li><strong>Solutions pratiques :</strong> Recommandations applicables</li>
<li><strong>Timeline :</strong> Priorités et délais de correction</li>
</ul>
</div>

</div>

---

## 📚 Pour aller plus loin

<div class="highlight-fact">
🔗 <strong>Ressources complémentaires :</strong>
<ul>
<li><strong>OWASP.org</strong> : Documentation et outils officiels</li>
<li><strong>PortSwigger Web Security Academy</strong> : Formation Burp Suite</li>
<li><strong>VulnHub</strong> : Machines virtuelles vulnérables pour s'entraîner</li>
<li><strong>HackTheBox</strong> : Plateforme d'entraînement au pentest</li>
<li><strong>PTES (Penetration Testing Execution Standard)</strong> : Méthodologie standardisée</li>
</ul>
</div>

---

## ✅ Points clés à retenir

1. **OWASP** : Référence incontournable pour la sécurité web
2. **Burp Suite** : Outil professionnel pour les tests d'applications web
3. **Méthodologie** : Approche structurée et documentée
4. **Automatisation** : Combiner outils automatiques et tests manuels
5. **Documentation** : Rapport détaillé avec preuves et recommandations

<div class="highlight-fact">
🎓 <strong>Prochaine étape :</strong> Dans le cours B3.6, nous aborderons la conformité réglementaire et la veille sécurité (RGPD, normes, identité numérique).
</div>