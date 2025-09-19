<style>
/* Styles modernes pour le cours Cybersécurité BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(220, 38, 127, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #dc267f 0%, #ff6b6b 100%);
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
    color: #dc267f;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    border-left: 5px solid #dc267f;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #dc267f;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.concept-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.concept-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(220, 38, 127, 0.1);
    border-left: 4px solid #dc267f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.security-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.security-card {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(220, 38, 127, 0.2);
    transition: all 0.3s ease;
}

.security-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(220, 38, 127, 0.2);
}

.risk-matrix {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1rem;
    margin: 2rem 0;
    text-align: center;
}

.risk-cell {
    padding: 1rem;
    border-radius: 8px;
    font-weight: 600;
    color: white;
}

.risk-low { background: #27ae60; }
.risk-medium { background: #f39c12; }
.risk-high { background: #e74c3c; }
.risk-critical { background: #8e44ad; }

.ebios-step {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.ebios-title {
    color: #3498db;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.custom-h3 {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.9), rgba(255, 107, 107, 0.8));
    color: white;
    padding: 1.2rem 2rem;
    border-radius: 15px;
    margin: 2.5rem 0 1.5rem 0;
    font-size: 1.4rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    box-shadow: 0 8px 20px rgba(220, 38, 127, 0.3);
    border: 1px solid rgba(220, 38, 127, 0.3);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.custom-h3:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(220, 38, 127, 0.4);
}

.custom-h4 {
    background: rgba(220, 38, 127, 0.1);
    color: #2c3e50;
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    border-left: 4px solid #dc267f;
    box-shadow: 0 4px 15px rgba(220, 38, 127, 0.1);
    transition: all 0.3s ease;
}

.custom-h4:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(220, 38, 127, 0.2);
    background: rgba(220, 38, 127, 0.15);
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.1 - Fondamentaux de la Cybersécurité</h1>
    <p class="course-subtitle">Risques, menaces et méthode EBIOS - BTS SIO</p>
</div>

---

<div class="concept-section">
<h2 class="section-title">🔐 Les fondamentaux de la cybersécurité</h2>

<div class="definition-box">
<div class="definition-title">Cybersécurité</div>
<div class="definition-content">
La cybersécurité est l'ensemble des technologies, processus et pratiques conçus pour protéger les réseaux, appareils, programmes et données contre les attaques, dommages ou accès non autorisés.
</div>
</div>

<h3 class="custom-h3">🔐 Les trois piliers de la sécurité informatique</h3>

<div class="concept-grid">
<div class="concept-card">
<div class="concept-icon">🔒</div>
<div class="concept-name">Confidentialité</div>
<div class="concept-description">
Garantir que l'information n'est accessible qu'aux personnes autorisées. Protection contre la divulgation non autorisée.
</div>
</div>

<div class="concept-card">
<div class="concept-icon">✅</div>
<div class="concept-name">Intégrité</div>
<div class="concept-description">
Assurer que l'information n'a pas été modifiée de manière non autorisée. Protection contre l'altération des données.
</div>
</div>

<div class="concept-card">
<div class="concept-icon">🌐</div>
<div class="concept-name">Disponibilité</div>
<div class="concept-description">
Garantir l'accès aux informations et services quand ils sont nécessaires. Protection contre les interruptions de service.
</div>
</div>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">⚠️ Risques et menaces</h2>

<div class="definition-box">
<div class="definition-title">Distinction fondamentale</div>
<div class="definition-content">
<strong>Risque :</strong> Probabilité qu'une menace exploite une vulnérabilité et cause un dommage<br>
<strong>Menace :</strong> Cause potentielle d'un incident indésirable<br>
<strong>Vulnérabilité :</strong> Faiblesse qui peut être exploitée par une menace
</div>
</div>

<h3>Types de menaces</h3>

<div class="security-grid">
<div class="security-card">
<h4>🎭 Menaces humaines</h4>
<ul>
<li>Attaquants externes (hackers)</li>
<li>Employés malveillants</li>
<li>Erreurs humaines</li>
<li>Ingénierie sociale</li>
</ul>
</div>

<div class="security-card">
<h4>💻 Menaces techniques</h4>
<ul>
<li>Malwares (virus, trojans)</li>
<li>Failles logicielles</li>
<li>Attaques réseau</li>
<li>Défaillances système</li>
</ul>
</div>

<div class="security-card">
<h4>🌍 Menaces environnementales</h4>
<ul>
<li>Catastrophes naturelles</li>
<li>Pannes électriques</li>
<li>Incendies</li>
<li>Dégâts des eaux</li>
</ul>
</div>

<div class="security-card">
<h4>⚖️ Menaces légales</h4>
<ul>
<li>Non-conformité RGPD</li>
<li>Violations contractuelles</li>
<li>Sanctions réglementaires</li>
<li>Litiges juridiques</li>
</ul>
</div>
</div>

<div class="highlight-fact">
💡 <strong>Fait important :</strong> 95% des cyberattaques réussies sont dues à une erreur humaine. La sensibilisation des utilisateurs est donc cruciale.
</div>

</div>

---

## 📚 Points de cours essentiels

<div class="concept-section">

<h3 class="custom-h3">🌍 Axe 1 - Les enjeux de la cybersécurité</h3>

<div class="definition-box">
<div class="definition-content">
La cybersécurité est un enjeu majeur pour les entreprises car une attaque peut avoir des conséquences graves :
</div>
</div>

<div class="security-grid">
<div class="security-card">
<h4>💰 Conséquences financières</h4>
<ul>
<li>Perte d'argent directe</li>
<li>Paiement de rançons</li>
<li>Perte de clients et de revenus</li>
<li>Coûts de remédiation et de récupération</li>
<li>Arrêt de production</li>
<li>Frais juridiques et d'expertise</li>
</ul>
</div>

<div class="security-card">
<h4>📉 Conséquences réputationnelles</h4>
<ul>
<li>Perte de confiance des utilisateurs</li>
<li>Détérioration de l'image de marque</li>
<li>Impact sur les partenaires commerciaux</li>
<li>Couverture médiatique négative</li>
<li>Perte de compétitivité</li>
<li>Difficultés de recrutement</li>
</ul>
</div>

<div class="security-card">
<h4>⚖️ Conséquences juridiques</h4>
<ul>
<li>Sanctions RGPD (jusqu'à 4% du CA)</li>
<li>Poursuites judiciaires</li>
<li>Amendes réglementaires</li>
<li>Responsabilité civile et pénale</li>
<li>Obligations de notification</li>
<li>Audits et contrôles renforcés</li>
</ul>
</div>
</div>

<div class="highlight-fact">
👉 <strong>Exemple concret :</strong> En 2017, l'attaque WannaCry a paralysé des hôpitaux en Europe et a coûté des millions d'euros. Le NHS britannique a estimé ses pertes à plus de 100 millions d'euros.
</div>

<h3 class="custom-h3">⚖️ Axe 2 - Le cadre légal et normatif</h3>

<div class="definition-box">
<div class="definition-content">
Pour protéger les données, les entreprises doivent respecter un cadre légal et normatif strict :
</div>
</div>

<div class="security-grid">
<div class="security-card">
<h4>🇪🇺 RGPD (Règlement Général sur la Protection des Données)</h4>
<p><strong>Règlement européen qui protège les données personnelles</strong></p>
<ul>
<li>Consentement explicite et éclairé</li>
<li>Droit à l'oubli et à la portabilité</li>
<li>Notification des violations sous 72h</li>
<li>Amendes jusqu'à 4% du CA mondial</li>
<li>Désignation d'un DPO si nécessaire</li>
<li>Privacy by design</li>
</ul>
</div>

<div class="security-card">
<h4>🇫🇷 ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)</h4>
<p><strong>Organisme français qui définit les bonnes pratiques de sécurité</strong></p>
<ul>
<li>Guides de sécurité sectoriels</li>
<li>Certification des produits de sécurité</li>
<li>Veille sur les menaces cyber</li>
<li>Formation et sensibilisation</li>
<li>Réponse aux incidents majeurs</li>
<li>Référentiels de sécurité</li>
</ul>
</div>

<div class="security-card">
<h4>🌐 ISO 27001</h4>
<p><strong>Norme internationale pour gérer la sécurité des systèmes d'information</strong></p>
<ul>
<li>Système de management de la sécurité</li>
<li>Analyse des risques obligatoire</li>
<li>Amélioration continue (PDCA)</li>
<li>Certification par tierce partie</li>
<li>114 mesures de sécurité</li>
<li>Audits réguliers</li>
</ul>
</div>
</div>

<h3 class="custom-h3">💥 Axe 3 - Exemples d'attaques</h3>

<div class="definition-box">
<div class="definition-content">
Quelques attaques courantes à connaître absolument :
</div>
</div>

<div class="security-grid">
<div class="security-card">
<h4>🎣 Phishing (Hameçonnage)</h4>
<p><strong>Mails frauduleux qui volent vos identifiants</strong></p>
<ul>
<li>Usurpation d'identité d'organismes connus</li>
<li>Sites web factices (spoofing)</li>
<li>Vol de credentials et données sensibles</li>
<li>Ingénierie sociale sophistiquée</li>
<li>Spear phishing (ciblé)</li>
<li>Taux de réussite : 30% des utilisateurs</li>
</ul>
</div>

<div class="security-card">
<h4>🔒 Ransomware (Rançongiciel)</h4>
<p><strong>Virus qui bloque les fichiers et demande une rançon</strong></p>
<ul>
<li>Chiffrement des données critiques</li>
<li>Demande de rançon en cryptomonnaie</li>
<li>Propagation réseau (mouvement latéral)</li>
<li>Paralysie totale de l'activité</li>
<li>Double extorsion (vol + chiffrement)</li>
<li>Coût moyen : 4,5 millions d'euros</li>
</ul>
</div>

<div class="security-card">
<h4>🌊 DDoS (Déni de Service Distribué)</h4>
<p><strong>Attaque qui rend un service inaccessible</strong></p>
<ul>
<li>Saturation des serveurs et bande passante</li>
<li>Déni de service pour les utilisateurs légitimes</li>
<li>Réseaux de bots (botnets)</li>
<li>Impact direct sur la disponibilité</li>
<li>Attaques volumétriques ou applicatives</li>
<li>Durée moyenne : 4 heures</li>
</ul>
</div>

<div class="security-card">
<h4>💉 Injection SQL</h4>
<p><strong>Attaque qui permet d'accéder aux bases de données</strong></p>
<ul>
<li>Exploitation des formulaires web</li>
<li>Accès non autorisé aux données</li>
<li>Modification ou suppression de données</li>
<li>Escalade de privilèges</li>
<li>Contournement de l'authentification</li>
<li>Impact : vol de données massif</li>
</ul>
</div>
</div>

<h3 class="custom-h3">📊 Axe 4 - Calcul du risque (détaillé)</h3>

<div class="definition-box">
<div class="definition-title">Formule fondamentale du risque</div>
<div class="definition-content">
<strong>Risque = Probabilité × Impact × Vulnérabilité</strong><br>
<em>Version simplifiée : Risque = Probabilité × Impact</em>
</div>
</div>

<h4 class="custom-h4">📈 Évaluation de la Probabilité</h4>

<div class="security-grid">
<div class="security-card">
<h4>Échelle de Probabilité</h4>
<ul>
<li><strong>Très faible (1)</strong> : < 5% - Événement exceptionnel</li>
<li><strong>Faible (2)</strong> : 5-25% - Événement rare</li>
<li><strong>Moyenne (3)</strong> : 25-75% - Événement possible</li>
<li><strong>Élevée (4)</strong> : 75-95% - Événement probable</li>
<li><strong>Très élevée (5)</strong> : > 95% - Événement quasi certain</li>
</ul>
</div>

<div class="security-card">
<h4>Facteurs influençant la probabilité</h4>
<ul>
<li>Historique des incidents</li>
<li>Niveau de menace sectoriel</li>
<li>Attractivité de la cible</li>
<li>Mesures de protection en place</li>
<li>Contexte géopolitique</li>
<li>Vulnérabilités connues</li>
</ul>
</div>
</div>

<h4 class="custom-h4">💥 Évaluation de l'Impact</h4>

<div class="security-grid">
<div class="security-card">
<h4>Échelle d'Impact</h4>
<ul>
<li><strong>Négligeable (1)</strong> : < 10k€ - Impact minimal</li>
<li><strong>Mineur (2)</strong> : 10k-100k€ - Impact limité</li>
<li><strong>Majeur (3)</strong> : 100k-1M€ - Impact significatif</li>
<li><strong>Critique (4)</strong> : 1M-10M€ - Impact grave</li>
<li><strong>Catastrophique (5)</strong> : > 10M€ - Impact majeur</li>
</ul>
</div>

<div class="security-card">
<h4>Types d'impacts à évaluer</h4>
<ul>
<li><strong>Financier</strong> : Pertes directes et indirectes</li>
<li><strong>Opérationnel</strong> : Arrêt d'activité</li>
<li><strong>Réputationnel</strong> : Image de marque</li>
<li><strong>Juridique</strong> : Sanctions et amendes</li>
<li><strong>Humain</strong> : Sécurité des personnes</li>
<li><strong>Stratégique</strong> : Avantage concurrentiel</li>
</ul>
</div>
</div>

<h4 class="custom-h4">🧮 Matrice de Risque</h4>

<div class="risk-matrix">
<div class="risk-cell" style="background: #34495e; color: white;"><strong>Impact →<br>Probabilité ↓</strong></div>
<div class="risk-cell" style="background: #34495e; color: white;"><strong>Négligeable</strong></div>
<div class="risk-cell" style="background: #34495e; color: white;"><strong>Mineur</strong></div>
<div class="risk-cell" style="background: #34495e; color: white;"><strong>Majeur</strong></div>
<div class="risk-cell" style="background: #34495e; color: white;"><strong>Critique</strong></div>

<div class="risk-cell" style="background: #34495e; color: white;"><strong>Très faible</strong></div>
<div class="risk-cell risk-low">FAIBLE<br>(1×1=1)</div>
<div class="risk-cell risk-low">FAIBLE<br>(1×2=2)</div>
<div class="risk-cell risk-medium">MOYEN<br>(1×3=3)</div>
<div class="risk-cell risk-medium">MOYEN<br>(1×4=4)</div>

<div class="risk-cell" style="background: #34495e; color: white;"><strong>Faible</strong></div>
<div class="risk-cell risk-low">FAIBLE<br>(2×1=2)</div>
<div class="risk-cell risk-medium">MOYEN<br>(2×2=4)</div>
<div class="risk-cell risk-medium">MOYEN<br>(2×3=6)</div>
<div class="risk-cell risk-high">ÉLEVÉ<br>(2×4=8)</div>

<div class="risk-cell" style="background: #34495e; color: white;"><strong>Moyenne</strong></div>
<div class="risk-cell risk-medium">MOYEN<br>(3×1=3)</div>
<div class="risk-cell risk-medium">MOYEN<br>(3×2=6)</div>
<div class="risk-cell risk-high">ÉLEVÉ<br>(3×3=9)</div>
<div class="risk-cell risk-high">ÉLEVÉ<br>(3×4=12)</div>

<div class="risk-cell" style="background: #34495e; color: white;"><strong>Élevée</strong></div>
<div class="risk-cell risk-medium">MOYEN<br>(4×1=4)</div>
<div class="risk-cell risk-high">ÉLEVÉ<br>(4×2=8)</div>
<div class="risk-cell risk-high">ÉLEVÉ<br>(4×3=12)</div>
<div class="risk-cell risk-critical">CRITIQUE<br>(4×4=16)</div>
</div>

<h4 class="custom-h4">🎯 Exemple de calcul détaillé</h4>

<div class="highlight-fact">
<strong>📋 Scénario : Attaque ransomware sur une PME de 50 employés</strong><br><br>

<strong>🔍 Analyse des composants :</strong><br>
• <strong>Menace :</strong> Groupe de cybercriminels spécialisé en ransomware<br>
• <strong>Vulnérabilité :</strong> Absence de sauvegarde hors ligne + utilisateurs non sensibilisés<br>
• <strong>Actif :</strong> Système d'information complet (serveurs, postes, données)<br><br>

<strong>📊 Évaluation :</strong><br>
• <strong>Probabilité :</strong> Élevée (4/5) - Secteur ciblé, vulnérabilités connues<br>
• <strong>Impact financier :</strong> Critique (4/5) - 500k€ (arrêt 2 semaines + rançon + remédiation)<br>
• <strong>Impact réputationnel :</strong> Majeur (3/5) - Perte de confiance clients<br>
• <strong>Impact opérationnel :</strong> Critique (4/5) - Arrêt total d'activité<br><br>

<strong>🧮 Calcul du risque :</strong><br>
<strong>Risque = 4 × 4 = 16 → CRITIQUE</strong><br><br>

<strong>⚡ Actions prioritaires :</strong><br>
1. Mise en place de sauvegardes 3-2-1<br>
2. Formation anti-phishing des utilisateurs<br>
3. Segmentation réseau<br>
4. Plan de continuité d'activité
</div>

<h3 class="custom-h3">🔎 Axe 5 - Introduction à la méthode EBIOS</h3>

<div class="definition-box">
<div class="definition-content">
<strong>EBIOS Risk Manager</strong> est une méthode française d'analyse des risques développée par l'ANSSI. Elle permet une approche structurée et complète de l'évaluation des risques cyber.
</div>
</div>

<div class="ebios-step">
<div class="ebios-title">🎯 Atelier 1 : Définir le contexte</div>
<strong>Objectif :</strong> Quels actifs protéger ?<br>
• Identifier les biens essentiels (données, processus, fonctions)<br>
• Cartographier les biens supports (matériels, logiciels, réseaux)<br>
• Définir le périmètre d'étude<br>
• Identifier les parties prenantes
</div>

<div class="ebios-step">
<div class="ebios-title">⚠️ Atelier 2 : Identifier les événements redoutés</div>
<strong>Objectif :</strong> Quels sont les impacts que l'on veut éviter ?<br>
• Définir les événements redoutés sur les biens essentiels<br>
• Évaluer les impacts potentiels<br>
• Prioriser selon la gravité<br>
• Établir les seuils d'acceptabilité
</div>

<div class="ebios-step">
<div class="ebios-title">🎭 Atelier 3 : Étudier les scénarios de menace</div>
<strong>Objectif :</strong> Comment les attaquants peuvent-ils procéder ?<br>
• Identifier les sources de menaces<br>
• Analyser leurs motivations et capacités<br>
• Modéliser les scénarios d'attaque<br>
• Évaluer la vraisemblance des scénarios
</div>

<div class="ebios-step">
<div class="ebios-title">🛡️ Atelier 4 : Identifier les mesures de sécurité</div>
<strong>Objectif :</strong> Quelles protections sont déjà en place ?<br>
• Inventorier les mesures existantes<br>
• Évaluer leur efficacité<br>
• Identifier les lacunes<br>
• Proposer des mesures complémentaires
</div>

<div class="ebios-step">
<div class="ebios-title">📈 Atelier 5 : Évaluer le risque et proposer des solutions</div>
<strong>Objectif :</strong> Calculer le risque résiduel et définir un plan d'action<br>
• Calculer les risques résiduels<br>
• Comparer aux seuils d'acceptabilité<br>
• Proposer un plan de traitement<br>
• Planifier la mise en œuvre et le suivi
</div>

<h3 class="custom-h3">✅ Axe 6 - Bonnes pratiques essentielles</h3>

<div class="definition-box">
<div class="definition-content">
Quelques gestes simples mais cruciaux pour renforcer la sécurité de votre organisation :
</div>
</div>

<div class="security-grid">
<div class="security-card">
<h4>🔄 Mises à jour et correctifs</h4>
<ul>
<li>Mettre à jour régulièrement les logiciels et systèmes</li>
<li>Appliquer les correctifs de sécurité en priorité</li>
<li>Maintenir un inventaire des versions</li>
<li>Automatiser les mises à jour quand possible</li>
<li>Tester avant déploiement en production</li>
<li>Planifier les fenêtres de maintenance</li>
</ul>
</div>

<div class="security-card">
<h4>🔐 Authentification forte</h4>
<ul>
<li>Utiliser des mots de passe forts et uniques</li>
<li>Activer l'authentification à deux facteurs (MFA)</li>
<li>Déployer un gestionnaire de mots de passe</li>
<li>Renouveler régulièrement les credentials</li>
<li>Implémenter l'authentification unique (SSO)</li>
<li>Surveiller les tentatives de connexion</li>
</ul>
</div>

<div class="security-card">
<h4>💾 Sauvegardes et restauration</h4>
<ul>
<li>Sauvegarder régulièrement les données critiques</li>
<li>Appliquer la règle 3-2-1 (3 copies, 2 supports, 1 hors site)</li>
<li>Tester régulièrement les restaurations</li>
<li>Chiffrer les sauvegardes</li>
<li>Automatiser les processus</li>
<li>Documenter les procédures</li>
</ul>
</div>

<div class="security-card">
<h4>👥 Sensibilisation et formation</h4>
<ul>
<li>Former les utilisateurs au phishing</li>
<li>Organiser des campagnes de sensibilisation</li>
<li>Réaliser des simulations d'attaques</li>
<li>Développer une culture de la sécurité</li>
<li>Mettre à jour régulièrement les formations</li>
<li>Mesurer l'efficacité des actions</li>
</ul>
</div>

<div class="security-card">
<h4>🔒 Principe du moindre privilège</h4>
<ul>
<li>Ne donner que les droits strictement nécessaires</li>
<li>Réviser régulièrement les accès</li>
<li>Séparer les environnements (dev/test/prod)</li>
<li>Implémenter un contrôle d'accès strict</li>
<li>Surveiller les activités privilégiées</li>
<li>Automatiser la gestion des droits</li>
</ul>
</div>

<div class="security-card">
<h4>🔍 Surveillance et détection</h4>
<ul>
<li>Déployer des outils de monitoring</li>
<li>Analyser les logs de sécurité</li>
<li>Mettre en place des alertes</li>
<li>Effectuer des audits réguliers</li>
<li>Utiliser l'intelligence artificielle</li>
<li>Maintenir une veille sur les menaces</li>
</ul>
</div>
</div>

</div>

---
