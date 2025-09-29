<style>
.budget-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 20px;
    margin: 15px 0;
    color: white;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.cost-breakdown {
    background: #f8f9fa;
    border-left: 4px solid #28a745;
    padding: 15px;
    margin: 10px 0;
    border-radius: 0 8px 8px 0;
}

.budget-formula {
    background: linear-gradient(45deg, #ff6b6b, #feca57);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    margin: 15px 0;
}

.roi-indicator {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 20px;
    font-weight: bold;
    margin: 5px;
}

.roi-positive { background: #d4edda; color: #155724; }
.roi-negative { background: #f8d7da; color: #721c24; }
.roi-neutral { background: #fff3cd; color: #856404; }

.budget-timeline {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 20px 0;
}

.phase-cost {
    background: white;
    color: #333;
    padding: 10px;
    margin: 5px 0;
    border-radius: 8px;
    border-left: 5px solid #667eea;
}

.warning-box {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 15px;
    margin: 15px 0;
}

.success-box {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    border-radius: 8px;
    padding: 15px;
    margin: 15px 0;
}

.budget-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.budget-table th {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 15px;
    text-align: left;
}

.budget-table td {
    padding: 12px 15px;
    border-bottom: 1px solid #eee;
}

.budget-table tr:hover {
    background: #f8f9fa;
}

.cost-category {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 0.9em;
    font-weight: bold;
    margin: 2px;
}

.cat-personnel { background: #e3f2fd; color: #1976d2; }
.cat-materiel { background: #f3e5f5; color: #7b1fa2; }
.cat-logiciel { background: #e8f5e8; color: #388e3c; }
.cat-formation { background: #fff3e0; color: #f57c00; }
.cat-maintenance { background: #fce4ec; color: #c2185b; }

.budget-chart {
    background: white;
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}

.progress-bar {
    width: 100%;
    height: 20px;
    background: #e9ecef;
    border-radius: 10px;
    overflow: hidden;
    margin: 10px 0;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #28a745, #20c997);
    transition: width 0.3s ease;
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin: 20px 0;
}

.kpi-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border-top: 4px solid #667eea;
}

.kpi-value {
    font-size: 2em;
    font-weight: bold;
    color: #667eea;
    margin: 10px 0;
}

.exercise-container {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border-radius: 15px;
    padding: 25px;
    margin: 25px 0;
    color: white;
}

.exercise-title {
    font-size: 1.3em;
    font-weight: bold;
    margin-bottom: 15px;
    text-align: center;
}

.scenario-box {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    backdrop-filter: blur(10px);
}
</style>

# B1.9 - Gestion Budgétaire des Projets Informatiques 💰

<div class="budget-card">
<h2>🎯 Objectifs du Chapitre</h2>
<ul>
<li><strong>Comprendre</strong> les enjeux de la gestion budgétaire en informatique</li>
<li><strong>Maîtriser</strong> les méthodes d'estimation des coûts</li>
<li><strong>Analyser</strong> la rentabilité des projets (ROI, VAN, TRI)</li>
<li><strong>Gérer</strong> les budgets tout au long du cycle de vie</li>
<li><strong>Optimiser</strong> les coûts et contrôler les dérives</li>
</ul>
</div>

## 📊 Introduction à la Gestion Budgétaire

### Pourquoi la Gestion Budgétaire est Cruciale ?

<div class="warning-box">
<strong>⚠️ Statistiques Alarmantes</strong><br>
• 70% des projets informatiques dépassent leur budget initial<br>
• 45% des projets coûtent plus de 200% du budget prévu<br>
• Les dépassements moyens sont de 27% en temps et 56% en budget
</div>

### Les Enjeux Financiers

1. **Contraintes Budgétaires**
   - Budgets limités des organisations
   - Concurrence entre projets
   - Justification des investissements

2. **Risques Financiers**
   - Dépassements de coûts
   - Retours sur investissement insuffisants
   - Impact sur la trésorerie

3. **Opportunités**
   - Optimisation des ressources
   - Amélioration de la compétitivité
   - Innovation technologique

## 💡 Composantes du Budget Informatique

### Structure Générale des Coûts

<div class="cost-breakdown">
<h4>🏗️ Coûts de Développement (60-70%)</h4>
<ul>
<li><span class="cat-personnel">Personnel</span> : Salaires, charges sociales, formations</li>
<li><span class="cat-materiel">Matériel</span> : Serveurs, postes de travail, équipements réseau</li>
<li><span class="cat-logiciel">Logiciels</span> : Licences, outils de développement, bases de données</li>
</ul>
</div>

<div class="cost-breakdown">
<h4>🔧 Coûts d'Exploitation (20-30%)</h4>
<ul>
<li><span class="cat-maintenance">Maintenance</span> : Corrective, évolutive, préventive</li>
<li><span class="cat-formation">Support</span> : Assistance utilisateurs, documentation</li>
<li><span class="cat-materiel">Infrastructure</span> : Hébergement, sauvegardes, sécurité</li>
</ul>
</div>

<div class="cost-breakdown">
<h4>📚 Coûts Annexes (10-20%)</h4>
<ul>
<li><span class="cat-formation">Formation</span> : Utilisateurs finaux, équipes techniques</li>
<li><span class="cat-personnel">Gestion</span> : Chef de projet, coordination, reporting</li>
<li><span class="cat-logiciel">Qualité</span> : Tests, audits, certifications</li>
</ul>
</div>

### Répartition Temporelle des Coûts

<div class="budget-timeline">
<h4>📅 Phases et Coûts Associés</h4>

<div class="phase-cost">
<strong>Phase 1 - Analyse (10-15%)</strong><br>
Étude de faisabilité, spécifications, architecture
</div>

<div class="phase-cost">
<strong>Phase 2 - Développement (50-60%)</strong><br>
Programmation, tests unitaires, intégration
</div>

<div class="phase-cost">
<strong>Phase 3 - Déploiement (15-20%)</strong><br>
Installation, migration, formation utilisateurs
</div>

<div class="phase-cost">
<strong>Phase 4 - Maintenance (15-25%)</strong><br>
Support, évolutions, corrections (par an)
</div>
</div>

## 📈 Méthodes d'Estimation des Coûts

### 1. Estimation par Analogie

<div class="success-box">
<strong>✅ Principe</strong><br>
Utiliser des projets similaires réalisés précédemment comme référence pour estimer les coûts du nouveau projet.
</div>

**Avantages :**
- Rapide à mettre en œuvre
- Basée sur l'expérience réelle
- Peu coûteuse

**Inconvénients :**
- Nécessite une base de données historique
- Peut être imprécise si les projets diffèrent
- Subjective

**Exemple d'Application :**
```
Projet A (réalisé) : Site e-commerce - 150 000€ - 8 mois
Projet B (à estimer) : Site e-commerce + mobile

Estimation : 150 000€ × 1,3 (facteur mobile) = 195 000€
```

### 2. Estimation Paramétrique

<div class="budget-formula">
Coût = Taille × Productivité × Facteurs d'Ajustement
</div>

**Méthode COCOMO (COnstructive COst MOdel) :**

<table class="budget-table">
<thead>
<tr>
<th>Type de Projet</th>
<th>Formule de Base</th>
<th>Facteur de Complexité</th>
</tr>
</thead>
<tbody>
<tr>
<td>Simple (Organique)</td>
<td>Effort = 2,4 × (KLOC)^1,05</td>
<td>1,0 - 1,2</td>
</tr>
<tr>
<td>Moyen (Semi-détaché)</td>
<td>Effort = 3,0 × (KLOC)^1,12</td>
<td>1,2 - 1,5</td>
</tr>
<tr>
<td>Complexe (Embarqué)</td>
<td>Effort = 3,6 × (KLOC)^1,20</td>
<td>1,5 - 2,0</td>
</tr>
</tbody>
</table>

*KLOC = Milliers de Lignes de Code*

### 3. Estimation Bottom-Up

**Processus :**
1. Décomposer le projet en tâches élémentaires
2. Estimer chaque tâche individuellement
3. Agréger les estimations
4. Ajouter les marges de sécurité

<div class="kpi-grid">
<div class="kpi-card">
<h4>Tâche 1</h4>
<div class="kpi-value">15j</div>
<p>Interface utilisateur</p>
</div>
<div class="kpi-card">
<h4>Tâche 2</h4>
<div class="kpi-value">25j</div>
<p>Base de données</p>
</div>
<div class="kpi-card">
<h4>Tâche 3</h4>
<div class="kpi-value">20j</div>
<p>API Backend</p>
</div>
<div class="kpi-card">
<h4>Total</h4>
<div class="kpi-value">60j</div>
<p>+ 20% marge = 72j</p>
</div>
</div>

### 4. Estimation par Points de Fonction

**Principe :** Mesurer la taille fonctionnelle du logiciel

<table class="budget-table">
<thead>
<tr>
<th>Élément</th>
<th>Complexité Simple</th>
<th>Complexité Moyenne</th>
<th>Complexité Élevée</th>
</tr>
</thead>
<tbody>
<tr>
<td>Entrées externes</td>
<td>3 points</td>
<td>4 points</td>
<td>6 points</td>
</tr>
<tr>
<td>Sorties externes</td>
<td>4 points</td>
<td>5 points</td>
<td>7 points</td>
</tr>
<tr>
<td>Fichiers logiques</td>
<td>7 points</td>
<td>10 points</td>
<td>15 points</td>
</tr>
<tr>
<td>Interfaces externes</td>
<td>5 points</td>
<td>7 points</td>
<td>10 points</td>
</tr>
<tr>
<td>Requêtes externes</td>
<td>3 points</td>
<td>4 points</td>
<td>6 points</td>
</tr>
</tbody>
</table>

## 💰 Analyse de Rentabilité

### 1. Retour sur Investissement (ROI)

<div class="budget-formula">
ROI = (Bénéfices - Coûts) / Coûts × 100
</div>

**Exemple :**
- Coût du projet : 200 000€
- Bénéfices annuels : 80 000€
- ROI = (80 000 - 200 000) / 200 000 × 100 = -60% (première année)
- ROI sur 3 ans = (240 000 - 200 000) / 200 000 × 100 = 20%

<div class="kpi-grid">
<div class="kpi-card">
<div class="roi-indicator roi-negative">ROI < 0%</div>
<p>Projet non rentable</p>
</div>
<div class="kpi-card">
<div class="roi-indicator roi-neutral">ROI 0-15%</div>
<p>Rentabilité faible</p>
</div>
<div class="kpi-card">
<div class="roi-indicator roi-positive">ROI > 15%</div>
<p>Projet rentable</p>
</div>
</div>

### 2. Valeur Actuelle Nette (VAN)

<div class="budget-formula">
VAN = Σ [Flux de trésorerie / (1 + taux d'actualisation)^n] - Investissement initial
</div>

**Interprétation :**
- VAN > 0 : Projet créateur de valeur
- VAN = 0 : Projet neutre
- VAN < 0 : Projet destructeur de valeur

### 3. Taux de Rentabilité Interne (TRI)

Le TRI est le taux d'actualisation qui annule la VAN.

**Critère de décision :**
- TRI > Coût du capital : Projet acceptable
- TRI < Coût du capital : Projet à rejeter

## 📊 Suivi et Contrôle Budgétaire

### Indicateurs de Performance

<div class="kpi-grid">
<div class="kpi-card">
<h4>CPI</h4>
<div class="kpi-value">0.85</div>
<p>Cost Performance Index<br>(Valeur acquise / Coût réel)</p>
</div>
<div class="kpi-card">
<h4>SPI</h4>
<div class="kpi-value">1.12</div>
<p>Schedule Performance Index<br>(Valeur acquise / Valeur planifiée)</p>
</div>
<div class="kpi-card">
<h4>EAC</h4>
<div class="kpi-value">235k€</div>
<p>Estimate at Completion<br>(Coût final estimé)</p>
</div>
<div class="kpi-card">
<h4>VAR</h4>
<div class="kpi-value">-15k€</div>
<p>Cost Variance<br>(Valeur acquise - Coût réel)</p>
</div>
</div>

### Méthode de la Valeur Acquise (Earned Value)

<div class="budget-chart">
<h4>📈 Courbes de Suivi Budgétaire</h4>
<div class="progress-bar">
<div class="progress-fill" style="width: 65%;"></div>
</div>
<p><strong>Avancement :</strong> 65% - <strong>Budget consommé :</strong> 75% - <strong>Écart :</strong> -10%</p>
</div>

**Formules Clés :**
- **Valeur Planifiée (PV)** : Budget prévu pour le travail planifié
- **Valeur Acquise (EV)** : Budget prévu pour le travail réalisé
- **Coût Réel (AC)** : Coût réel du travail réalisé

### Tableau de Bord Budgétaire

<table class="budget-table">
<thead>
<tr>
<th>Phase</th>
<th>Budget Initial</th>
<th>Budget Révisé</th>
<th>Coût Réel</th>
<th>Écart</th>
<th>% Avancement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Analyse</td>
<td>25 000€</td>
<td>25 000€</td>
<td>23 500€</td>
<td style="color: green;">+1 500€</td>
<td>100%</td>
</tr>
<tr>
<td>Développement</td>
<td>120 000€</td>
<td>135 000€</td>
<td>95 000€</td>
<td style="color: orange;">-40 000€</td>
<td>65%</td>
</tr>
<tr>
<td>Tests</td>
<td>30 000€</td>
<td>30 000€</td>
<td>0€</td>
<td>0€</td>
<td>0%</td>
</tr>
<tr>
<td>Déploiement</td>
<td>25 000€</td>
<td>25 000€</td>
<td>0€</td>
<td>0€</td>
<td>0%</td>
</tr>
</tbody>
</table>

## 🎯 Optimisation des Coûts

### Stratégies de Réduction des Coûts

1. **Optimisation des Ressources Humaines**
   - Externalisation sélective (offshore, nearshore)
   - Mutualisation des compétences
   - Formation vs recrutement

2. **Choix Technologiques**
   - Open Source vs solutions propriétaires
   - Cloud vs infrastructure on-premise
   - Solutions SaaS vs développement spécifique

3. **Méthodologies Agiles**
   - Livraisons itératives
   - Feedback rapide
   - Réduction des risques

### Analyse Make vs Buy

<table class="budget-table">
<thead>
<tr>
<th>Critère</th>
<th>Développement Interne</th>
<th>Achat de Solution</th>
<th>Externalisation</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Coût Initial</strong></td>
<td>Élevé</td>
<td>Moyen</td>
<td>Variable</td>
</tr>
<tr>
<td><strong>Délai</strong></td>
<td>Long</td>
<td>Court</td>
<td>Moyen</td>
</tr>
<tr>
<td><strong>Contrôle</strong></td>
<td>Total</td>
<td>Limité</td>
<td>Partagé</td>
</tr>
<tr>
<td><strong>Maintenance</strong></td>
<td>Interne</td>
<td>Éditeur</td>
<td>Prestataire</td>
</tr>
<tr>
<td><strong>Évolutivité</strong></td>
<td>Maximale</td>
<td>Limitée</td>
<td>Négociable</td>
</tr>
</tbody>
</table>

## 🚨 Gestion des Risques Budgétaires

### Principaux Risques

<div class="warning-box">
<strong>⚠️ Risques Techniques</strong><br>
• Sous-estimation de la complexité<br>
• Changements technologiques<br>
• Problèmes d'intégration<br>
• Performance insuffisante
</div>

<div class="warning-box">
<strong>⚠️ Risques Organisationnels</strong><br>
• Changements de périmètre<br>
• Disponibilité des ressources<br>
• Turnover de l'équipe<br>
• Conflits de priorités
</div>

<div class="warning-box">
<strong>⚠️ Risques Externes</strong><br>
• Évolution réglementaire<br>
• Concurrence<br>
• Crise économique<br>
• Obsolescence technologique
</div>

### Stratégies de Mitigation

1. **Provisions pour Risques**
   - 10-15% pour projets simples
   - 20-30% pour projets complexes
   - 40-50% pour projets innovants

2. **Contrats à Risques Partagés**
   - Forfait avec clauses de révision
   - Régie avec plafond
   - Partenariat gain/pain sharing

3. **Assurances Projet**
   - Assurance responsabilité civile
   - Assurance perte d'exploitation
   - Garanties de performance

## 📋 Exercices Pratiques

<div class="exercise-container">
<div class="exercise-title">🎯 Exercice 1 : Estimation de Coûts</div>

<div class="scenario-box">
<strong>Contexte :</strong> Développement d'une application mobile de gestion de stock pour une PME.

<strong>Données :</strong>
- Équipe : 1 chef de projet (600€/jour), 2 développeurs (450€/jour), 1 testeur (350€/jour)
- Durée estimée : 4 mois
- Matériel : 15 000€
- Licences : 8 000€
- Formation : 5 000€

<strong>Questions :</strong>
1. Calculez le coût total du projet
2. Répartissez les coûts par catégorie
3. Proposez une provision pour risques
4. Calculez le coût journalier de l'équipe
</div>
</div>

<div class="exercise-container">
<div class="exercise-title">🎯 Exercice 2 : Analyse ROI</div>

<div class="scenario-box">
<strong>Contexte :</strong> Mise en place d'un ERP pour automatiser les processus comptables.

<strong>Données :</strong>
- Coût du projet : 350 000€
- Économies annuelles : 120 000€
- Coûts de maintenance annuels : 25 000€
- Durée de vie : 7 ans
- Taux d'actualisation : 8%

<strong>Questions :</strong>
1. Calculez le ROI sur 3 ans
2. Calculez la VAN du projet
3. Déterminez le délai de retour sur investissement
4. Analysez la rentabilité du projet
</div>
</div>

<div class="exercise-container">
<div class="exercise-title">🎯 Exercice 3 : Suivi Budgétaire</div>

<div class="scenario-box">
<strong>Contexte :</strong> Projet de refonte de site web en cours.

<strong>Données à la semaine 12 :</strong>
- Budget total : 180 000€
- Avancement planifié : 60%
- Avancement réel : 55%
- Coût réel : 115 000€

<strong>Questions :</strong>
1. Calculez la valeur planifiée (PV)
2. Calculez la valeur acquise (EV)
3. Calculez les indices CPI et SPI
4. Estimez le coût final (EAC)
5. Proposez des actions correctives
</div>
</div>

## 🔧 Outils de Gestion Budgétaire

### Logiciels Spécialisés

<table class="budget-table">
<thead>
<tr>
<th>Outil</th>
<th>Type</th>
<th>Fonctionnalités Clés</th>
<th>Prix</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Microsoft Project</strong></td>
<td>Gestion de projet</td>
<td>Planification, suivi coûts, rapports</td>
<td>20-55€/mois</td>
</tr>
<tr>
<td><strong>Jira + Tempo</strong></td>
<td>Agile + Timesheet</td>
<td>Suivi temps, budgets, facturation</td>
<td>10-15€/mois</td>
</tr>
<tr>
<td><strong>Smartsheet</strong></td>
<td>Collaboration</td>
<td>Tableaux de bord, automatisation</td>
<td>14-25€/mois</td>
</tr>
<tr>
<td><strong>Monday.com</strong></td>
<td>Gestion travail</td>
<td>Suivi budgets, ressources, temps</td>
<td>8-24€/mois</td>
</tr>
</tbody>
</table>

### Tableaux de Bord Excel

**Modèles Recommandés :**
- Suivi budgétaire par phase
- Analyse de rentabilité
- Tableau de bord des risques
- Reporting mensuel

## 📚 Bonnes Pratiques

### 1. Estimation

<div class="success-box">
<strong>✅ Recommandations</strong><br>
• Utiliser plusieurs méthodes d'estimation<br>
• Impliquer l'équipe technique dans l'estimation<br>
• Documenter les hypothèses<br>
• Réviser régulièrement les estimations
</div>

### 2. Suivi

<div class="success-box">
<strong>✅ Recommandations</strong><br>
• Mettre en place un reporting hebdomadaire<br>
• Utiliser des indicateurs visuels<br>
• Anticiper les dérives<br>
• Communiquer transparence sur les écarts
</div>

### 3. Optimisation

<div class="success-box">
<strong>✅ Recommandations</strong><br>
• Analyser les coûts cachés<br>
• Négocier les contrats fournisseurs<br>
• Mutualiser les ressources<br>
• Capitaliser sur l'expérience
</div>

## 🎓 Points Clés à Retenir

<div class="budget-card">
<h3>💡 Synthèse du Chapitre</h3>
<ul>
<li><strong>Estimation :</strong> Utiliser des méthodes complémentaires et prévoir des marges</li>
<li><strong>Analyse :</strong> Évaluer la rentabilité avec ROI, VAN et TRI</li>
<li><strong>Suivi :</strong> Mettre en place des indicateurs de performance (CPI, SPI)</li>
<li><strong>Optimisation :</strong> Rechercher l'équilibre coût/qualité/délai</li>
<li><strong>Risques :</strong> Anticiper et provisionner les risques budgétaires</li>
</ul>
</div>

---

## 📖 Ressources Complémentaires

- **PMBOK Guide** - Project Management Institute
- **COCOMO II Model** - Barry Boehm
- **Function Point Analysis** - IFPUG
- **Earned Value Management** - PMI Practice Standard

---

*Cours BTS SIO 1 - Gestion Budgétaire - Version 2024*