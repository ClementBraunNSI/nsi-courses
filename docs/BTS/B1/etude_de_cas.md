<style>
.course-header { background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 3rem; margin: 2rem 0; border: 1px solid rgba(52, 152, 219, 0.2); text-align: center; }
.course-title { font-size: 2.6rem; font-weight: 700; background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.5rem; }
.course-subtitle { color: #7f8c8d; font-size: 1.05rem; font-weight: 300; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 2rem; margin: 2rem 0; box-shadow: 0 8px 32px rgba(0,0,0,0.1); border: 1px solid rgba(255,255,255,0.2); }
.section-title { font-size: 2rem; font-weight: 600; color: #3498db; margin-bottom: 1.5rem; text-align: center; }
.concept-section p { color: var(--md-default-fg-color); font-size: 1rem; line-height: 1.7; margin: 0.4rem 0 1rem; }
.concept-section h3 { font-size: 1.25rem; font-weight: 600; color: #2c3e50; margin: 1rem 0 0.6rem; }
.concept-section h4 { font-size: 1.1rem; font-weight: 600; color: #2c3e50; margin: 0.8rem 0 0.4rem; }
.highlight-fact { background: rgba(52,152,219,0.1); border-left: 4px solid #3498db; padding: 1rem; margin: 1rem 0; border-radius: 8px; font-weight: 500; }
.table-section { background: #ffffff; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; box-shadow: 0 8px 24px rgba(0,0,0,0.08); border: 1px solid #e9ecef; }
.styled-table { width: 100%; border-collapse: collapse; border-radius: 8px; overflow: hidden; }
.styled-table th { background: linear-gradient(135deg, #3498db, #2980b9); color: #fff; padding: 0.8rem; text-align: left; font-weight: 600; }
.styled-table td { padding: 0.8rem; border-bottom: 1px solid #ecf0f1; }
.styled-table tr:nth-child(even) { background: rgba(52,152,219,0.04); }
.concept-section ul, .concept-section ol { margin: 0.4rem 0 1rem; padding-left: 1.4rem; }
.concept-section ul { list-style: disc; }
.concept-section ol { list-style: decimal; }
.concept-section li { line-height: 1.7; margin: 0.2rem 0; }
.concept-section li > ul, .concept-section li > ol { margin-top: 0.3rem; }
@media (max-width: 768px) { .course-title { font-size: 2rem; } }
</style>

<div class="course-header">
  <h1 class="course-title">Étude de cas — FuchsTechnology</h1>
  <p class="course-subtitle">BTS SIO SLAM — Bloc B1 • Durée estimée : 2 à 4 heures • Rendu attendu : Document PDF</p>
</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">0 Présentation de l'entreprise</h2>

<strong>FuchsTechnology</strong> est une entreprise de développement d'applications sur mesure comptant 25 collaborateurs. L'entreprise développe des solutions logicielles pour des clients variés (e-commerce, gestion, mobile).

<h3>0.1 Contexte actuel</h3>

FuchsTechnology fait face à plusieurs problématiques :
<ul>
  <li><strong>Parc informatique obsolète</strong> : ordinateurs de plus de 8 ans, ralentissements fréquents</li>
  <li><strong>Absence de sécurité unifiée</strong> : pas d'antivirus centralisé</li>
  <li><strong>Logiciels métiers périmés</strong> : versions non supportées</li>
  <li><strong>Nouveau projet client</strong> : une société annexe, <strong>TechStore</strong>, souhaite une application web de gestion de stock</li>
</ul>

<h3>0.2 Budget disponible</h3>

<strong>50 000 €</strong> pour le renouvellement complet du parc informatique et des licences.

</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">1 Renouvellement du parc informatique</h2>

<h3>1.1 Devis de nouveau matériel</h3>

<h4>1.1.1 Objectif</h4>
Établir un devis détaillé pour renouveler le parc informatique dans la limite du budget de 50 000 €.

<h4>1.1.2 Composition de l'équipe FuchsTechnology</h4>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Poste</th><th>Nombre</th><th>Besoins spécifiques</th></tr>
    </thead>
    <tbody>
      <tr><td>Développeurs Full-Stack</td><td>12</td><td>Stations performantes, 2 écrans</td></tr>
      <tr><td>Chef de projet</td><td>2</td><td>Station standard, mobilité</td></tr>
      <tr><td>Designers UI/UX</td><td>3</td><td>Station haute performance graphique</td></tr>
      <tr><td>Testeurs QA</td><td>4</td><td>Station standard</td></tr>
      <tr><td>Support technique</td><td>2</td><td>Station standard + outils réseau</td></tr>
      <tr><td>Direction</td><td>2</td><td>Laptops premium</td></tr>
    </tbody>
  </table>
</div>

<h4>1.1.3 Équipements à prévoir</h4>

Pour chaque collaborateur, prévoir :
<ul>
  <li><strong>Poste de travail</strong> adapté au profil</li>
  <li><strong>Écran(s)</strong> : 1 ou 2 selon le poste</li>
  <li><strong>Périphériques</strong> : clavier, souris</li>
  <li><strong>Logiciels métiers</strong> :
    <ul>
      <li>Suite Office 365 (tous)</li>
      <li>IDE (JetBrains IntelliJ IDEA ou Visual Studio Code) pour développeurs</li>
      <li>Adobe Creative Suite pour designers</li>
      <li>Outils de test (Selenium, Postman) pour QA</li>
    </ul>
  </li>
  <li><strong>Antivirus professionnel</strong> : protection centralisée (ex : Bitdefender GravityZone, Kaspersky Endpoint)</li>
  <li><strong>Serveur</strong> : 1 serveur pour hébergement interne et gestion centralisée</li>
</ul>

<h4>1.1.4 Travail à réaliser</h4>

<strong>Créer un tableau de devis détaillé</strong> comprenant :

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Catégorie</th><th>Quantité</th><th>Description</th><th>Prix unitaire HT</th><th>Prix total HT</th></tr>
    </thead>
    <tbody>
      <tr><td>Postes développeurs</td><td>12</td><td>PC fixe performant (i7, 32 GB RAM, SSD 1TB)</td><td></td><td></td></tr>
      <tr><td>Postes designers</td><td>3</td><td>PC haute performance graphique (i9, 64 GB RAM, GPU dédié)</td><td></td><td></td></tr>
      <tr><td>Postes standards</td><td>8</td><td>PC standard (i5, 16 GB RAM, SSD 512GB)</td><td></td><td></td></tr>
      <tr><td>Laptops direction</td><td>2</td><td>Laptop premium (Dell XPS ou équivalent)</td><td></td><td></td></tr>
      <tr><td>Écrans</td><td>35</td><td>Écrans 24" Full HD</td><td></td><td></td></tr>
      <tr><td>Écrans designers</td><td>3</td><td>Écrans 27" 4K</td><td></td><td></td></tr>
      <tr><td>Périphériques</td><td>25</td><td>Clavier + souris</td><td></td><td></td></tr>
      <tr><td>Licences Office 365</td><td>25</td><td>Abonnement annuel Business Premium</td><td></td><td></td></tr>
      <tr><td>Licences JetBrains</td><td>12</td><td>IntelliJ IDEA Ultimate (annuel)</td><td></td><td></td></tr>
      <tr><td>Licences Adobe CC</td><td>3</td><td>Creative Cloud All Apps (annuel)</td><td></td><td></td></tr>
      <tr><td>Antivirus entreprise</td><td>25</td><td>Licence annuelle</td><td></td><td></td></tr>
      <tr><td>Serveur</td><td>1</td><td>Serveur Dell PowerEdge ou équivalent</td><td></td><td></td></tr>
      <tr><td><strong>TOTAL HT</strong></td><td></td><td></td><td></td><td></td></tr>
      <tr><td><strong>TVA (20%)</strong></td><td></td><td></td><td></td><td></td></tr>
      <tr><td><strong>TOTAL TTC</strong></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

<div class="highlight-fact">
Les développeurs et designer sont dans un open space, le support technique dans un ensemble de bureaux à part (SC1 et SC2) et la direction à l'étage (A1, A2).
Contrainte : le total TTC ne doit pas dépasser 50 000 €.
</div>

<h3>1.2 Inventaire CMDB</h3>

<h4>1.2.1 Objectif</h4>

Réaliser un inventaire complet du patrimoine informatique existant de FuchsTechnology sous forme de CMDB (Configuration Management Database) après le renouvellement.

<h3>1.2.2 Rappel théorique - CMDB</h3>

La <strong>CMDB (Configuration Management Database)</strong> est une base de données centralisée qui contient des informations sur tous les éléments de configuration (CI - Configuration Items) du système d'information d'une organisation.

<strong>Éléments à inventorier</strong> :
<ul>
  <li><strong>Matériel</strong> : postes de travail, serveurs, périphériques, équipements réseau</li>
  <li><strong>Logiciels</strong> : applications, licences, versions</li>
  <li><strong>Services</strong> : services IT fournis aux utilisateurs</li>
  <li><strong>Relations</strong> : interdépendances entre éléments</li>
</ul>

<strong>Informations essentielles pour chaque CI</strong> :
<ul>
  <li>Identifiant unique</li>
  <li>Type et modèle</li>
  <li>Localisation</li>
  <li>Utilisateur/propriétaire</li>
  <li>Date d'acquisition</li>
  <li>État (en service, en panne, obsolète)</li>
  <li>Informations de maintenance</li>
</ul>

<h4>1.2.3 Travail à faire</h4>

Réaliser l'inventaire complet du patrimoine informatique de FuchsTechnology après le renouvellement du matériel.
Faire correspondre chaque ligne du CMDB à un équipement informatique ou à un logiciel à licence.

</div>

<div class="concept-section" markdown="1">
<h2 class="section-title">2 Planification projet — Application TechStore</h2>

<h3>2.0 Objectif</h3>
Planifier le développement de l'application de gestion de stock pour le client TechStore à l'aide d'un diagramme de Gantt.

<h3>2.1 Description du projet</h3>

<strong>TechStore</strong> souhaite une application web permettant de :
<ul>
  <li>Gérer un inventaire de produits (ajout, modification, suppression)</li>
  <li>Suivre les entrées/sorties de stock</li>
  <li>Générer des alertes de stock faible</li>
  <li>Produire des rapports d'activité</li>
  <li>Gérer les utilisateurs et leurs droits</li>
</ul>

<h3>2.2 Tâches du projet</h3>

Voici les tâches identifiées pour le projet :

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>ID</th><th>Tâche</th><th>Description</th><th>Durée (jours)</th><th>Prédécesseurs</th></tr>
    </thead>
    <tbody>
      <tr><td>A</td><td>Analyse des besoins</td><td>Entretiens client, spécifications fonctionnelles</td><td>5</td><td>-</td></tr>
      <tr><td>B</td><td>Conception base de données</td><td>Modélisation MCD/MLD</td><td>4</td><td>A</td></tr>
      <tr><td>C</td><td>Conception UI/UX</td><td>Maquettes et prototypes</td><td>6</td><td>A</td></tr>
      <tr><td>D</td><td>Validation conception</td><td>Présentation au client</td><td>2</td><td>B, C</td></tr>
      <tr><td>E</td><td>Développement Backend</td><td>API REST + base de données</td><td>12</td><td>D</td></tr>
      <tr><td>F</td><td>Développement Frontend</td><td>Interface utilisateur</td><td>10</td><td>D</td></tr>
      <tr><td>G</td><td>Module d'authentification</td><td>Gestion utilisateurs et droits</td><td>5</td><td>E</td></tr>
      <tr><td>H</td><td>Module de reporting</td><td>Génération de rapports PDF</td><td>4</td><td>E, F</td></tr>
      <tr><td>I</td><td>Intégration et tests unitaires</td><td>Tests techniques</td><td>6</td><td>E, F, G, H</td></tr>
      <tr><td>J</td><td>Tests fonctionnels</td><td>Tests avec scénarios utilisateur</td><td>5</td><td>I</td></tr>
      <tr><td>K</td><td>Corrections des anomalies</td><td>Résolution des bugs identifiés</td><td>4</td><td>J</td></tr>
      <tr><td>L</td><td>Recette client</td><td>Validation par le client</td><td>3</td><td>K</td></tr>
      <tr><td>M</td><td>Formation utilisateurs</td><td>Formation des équipes TechStore</td><td>2</td><td>L</td></tr>
      <tr><td>N</td><td>Mise en production</td><td>Déploiement final</td><td>2</td><td>M</td></tr>
    </tbody>
  </table>
</div>

<h3>2.3 Travail à réaliser</h3>

<ol>
   <li>Quelle méthodologie serait la plus adaptée pour la réalisation de ce projet en matière de gestion de projet ? Quels sont les avantages qu'elle propose ?</li>
  <li><strong>Créer un diagramme de Gantt</strong> pour ce projet :
    <ul>
      <li>Utiliser un tableur (Excel, Google Sheets) ou un outil dédié (GanttProject, ProjectLibre)</li>
      <li>Représenter toutes les tâches avec leur durée</li>
      <li>Indiquer les dépendances entre tâches</li>
      <li>Identifier visuellement les jalons importants (validation conception, recette client, mise en production)</li>
      <li>Calculer la <strong>durée totale du projet</strong></li>
    </ul>
  </li>
  <li><strong>Identifier les jalons clés</strong> :
    <ul>
      <li>Jalon 1 : Validation de la conception</li>
      <li>Jalon 2 : Fin du développement</li>
      <li>Jalon 3 : Recette client validée</li>
      <li>Jalon 4 : Mise en production</li>
    </ul>
  </li>
</ol>


</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">3 Chemin critique</h2>

<h3>3.1 Objectif</h3>
Identifier le chemin critique du projet TechStore et calculer les marges de manœuvre pour chaque tâche.

<h3>3.2 Rappel théorique</h3>

<ul>
  <li><strong>Chemin critique</strong> : séquence de tâches déterminant la durée minimale du projet</li>
  <li><strong>Marge totale</strong> : retard maximum qu'une tâche peut prendre sans retarder le projet</li>
  <li><strong>Tâche critique</strong> : tâche avec une marge totale = 0</li>
</ul>

<h3>3.3 Travail à réaliser</h3>

<ol>
  <li><strong>Tracer le réseau PERT</strong> du projet (graphe des tâches et dépendances)</li>
  <li><strong>Calculer pour chaque tâche</strong> :
    <ul>
      <li><strong>Date de début au plus tôt</strong> (calcul avant)</li>
      <li><strong>Date de début au plus tard</strong> (calcul arrière)</li>
      <li><strong>Marge totale</strong> = Date au plus tard - Date au plus tôt - Durée</li>
    </ul>
  </li>
  <li><strong>Identifier le chemin critique</strong> (tâches avec marge = 0)</li>
  <li><strong>Créer un tableau récapitulatif</strong> :</li>
</ol>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Tâche</th><th>Durée</th><th>Début au plus tôt</th><th>Début au plus tard</th><th>Marge totale</th><th>Critique ?</th></tr>
    </thead>
    <tbody>
      <tr><td>A</td><td>5</td><td>0</td><td></td><td></td><td></td></tr>
      <tr><td>B</td><td>4</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>C</td><td>6</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

<strong>5. Justification</strong> :
<ul>
  <li>Expliquer pourquoi ces tâches sont critiques</li>
  <li>Indiquer les conséquences d'un retard sur une tâche critique</li>
  <li>Proposer 2-3 mesures pour sécuriser le chemin critique</li>
</ul>

<div class="highlight-fact">Exemple : la tâche E (Développement Backend) est critique car elle détermine la durée minimale du projet. Un retard d'un jour sur cette tâche retardera automatiquement la livraison finale d'un jour. Il est recommandé d'affecter les développeurs les plus expérimentés et de prévoir des points d'avancement quotidiens.</div>

</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">4 Gestion des risques</h2>

<h3>4.1 Objectifs</h3>
<ol>
  <li>Analyser les risques liés à l'infrastructure de FuchsTechnology</li>
  <li>Analyser les risques liés au projet TechStore</li>
</ol>

<h3>4.2 Rappel — Matrice des risques</h3>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Probabilité / Impact</th><th>Négligeable (1)</th><th>Mineur (2)</th><th>Modéré (3)</th><th>Majeur (4)</th><th>Critique (5)</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Très probable (5)</strong></td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td></tr>
      <tr><td><strong>Probable (4)</strong></td><td>4</td><td>8</td><td>12</td><td>16</td><td>20</td></tr>
      <tr><td><strong>Possible (3)</strong></td><td>3</td><td>6</td><td>9</td><td>12</td><td>15</td></tr>
      <tr><td><strong>Peu probable (2)</strong></td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td></tr>
      <tr><td><strong>Rare (1)</strong></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
    </tbody>
  </table>
</div>

<strong>Niveaux de criticité</strong> :
<ul>
  <li>1-6 : Risque faible (surveillance)</li>
  <li>8-9 : Risque moyen (plan de contingence)</li>
  <li>10-16 : Risque élevé (actions préventives obligatoires)</li>
  <li>20-25 : Risque critique (traitement immédiat)</li>
</ul>

<h3>4.3 Risques infrastructurels (FuchsTechnology)</h3>

<h4>4.3.1 Travail à réaliser</h4>

Identifier <strong>au minimum 6 risques autres que ceux énoncés</strong> liés à l'infrastructure de l'entreprise et compléter le tableau :

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>ID</th><th>Risque identifié</th><th>Probabilité (1-5)</th><th>Impact (1-5)</th><th>Criticité</th><th>Stratégie</th><th>Mesures de mitigation</th></tr>
    </thead>
    <tbody>
      <tr><td>R01</td><td>Panne du serveur principal</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R02</td><td>Cyberattaque (ransomware)</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R03</td><td>Perte de données (absence de sauvegarde)</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R04</td><td>Coupure électrique prolongée</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R05</td><td>Défaillance du système antivirus</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R06</td><td>...</td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

Types de risques à considérer :
<ul>
  <li>Pannes matérielles</li>
  <li>Risques de sécurité</li>
  <li>Risques humains (départ d'un administrateur clé)</li>
  <li>Risques environnementaux (incendie, inondation)</li>
  <li>Risques réseau</li>
</ul>

Stratégies disponibles : Éviter, Transférer, Réduire, Accepter

<h3>4.4 Risques projet (Application TechStore)</h3>

<h4>4.4.1 Travail à réaliser</h4>

Identifier <strong>au minimum 6 risques autres que ceux énoncés</strong> liés au développement de l'application TechStore :

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>ID</th><th>Risque identifié</th><th>Probabilité (1-5)</th><th>Impact (1-5)</th><th>Criticité</th><th>Stratégie</th><th>Mesures de mitigation</th></tr>
    </thead>
    <tbody>
      <tr><td>R11</td><td>Dérive du périmètre fonctionnel</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R12</td><td>Départ d'un développeur clé</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R13</td><td>Sous-estimation de la complexité technique</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R14</td><td>Retard de validation client</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R15</td><td>Problèmes d'intégration API</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td>R16</td><td>...</td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

Types de risques à considérer :
<ul>
  <li>Risques techniques (choix technologiques, intégration)</li>
  <li>Risques de planning (retards, sous-estimation)</li>
  <li>Risques humains (compétences, disponibilité)</li>
  <li>Risques clients (changements de besoins, validation)</li>
  <li>Risques de sécurité applicative</li>
</ul>

<h3>4.5 Justification attendue</h3>

Pour chaque risque, justifier brièvement :
<ul>
  <li>Pourquoi cette probabilité et cet impact ?</li>
  <li>Pourquoi cette stratégie de traitement ?</li>
  <li>Comment les mesures de mitigation réduiront le risque ?</li>
</ul>

</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">5 Gestion ITIL</h2>

<h3>5.1 Objectif</h3>
Mettre en place une gestion de services ITIL pour l'application TechStore une fois mise en production.

<h3>5.2 Rappel théorique</h3>

ITIL définit les bonnes pratiques pour <strong>faire vivre un service dans la durée</strong> après sa mise en production.

<strong>Les 3 pratiques essentielles</strong> :
<ol>
  <li>Gestion des incidents : rétablir le service rapidement</li>
  <li>Gestion des problèmes : identifier et corriger les causes profondes</li>
  <li>Gestion des changements : modifier le service sans créer de pannes</li>
</ol>

<h3>5.3 Gestion des incidents</h3>

<h4>5.3.1 Travail à réaliser</h4>

<ol>
  <li><strong>Définir les niveaux de priorité</strong> des incidents pour l'application TechStore :</li>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Priorité</th><th>Impact</th><th>Urgence</th><th>Exemple</th><th>Délai de résolution cible</th></tr>
    </thead>
    <tbody>
      <tr><td>Critique</td><td>Élevé</td><td>Élevée</td><td>Application complètement inaccessible</td><td></td></tr>
      <tr><td>Élevée</td><td>Élevé</td><td>Moyenne</td><td></td><td></td></tr>
      <tr><td>Moyenne</td><td>Moyen</td><td>Moyenne</td><td></td><td></td></tr>
      <tr><td>Faible</td><td>Faible</td><td>Faible</td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

  <li><strong>Définir le processus d'escalade</strong> :</li>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Niveau</th><th>Responsable</th><th>Type d'intervention</th><th>Délai de prise en charge</th></tr>
    </thead>
    <tbody>
      <tr><td>Niveau 1</td><td>Support utilisateur (Helpdesk)</td><td></td><td></td></tr>
      <tr><td>Niveau 2</td><td>Technicien spécialisé</td><td></td><td></td></tr>
      <tr><td>Niveau 3</td><td>Expert/Développeur senior</td><td></td><td></td></tr>
      <tr><td>Niveau 4</td><td>Fournisseurs externes</td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

  <li><strong>Proposer 5 exemples d'incidents</strong> avec leur traitement :</li>
</ol>

<strong>Incident 1</strong> :
<ul>
  <li>Description :</li>
  <li>Priorité :</li>
  <li>Solution temporaire (workaround) :</li>
  <li>Niveau d'escalade :</li>
</ul>

<strong>Incident 2</strong> :
<ul>
  <li>Description :</li>
  <li>Priorité :</li>
  <li>Solution temporaire :</li>
  <li>Niveau d'escalade :</li>
</ul>

<strong>Incident n</strong> :
<ul>
  <li>Description :</li>
  <li>Priorité :</li>
  <li>Solution temporaire :</li>
  <li>Niveau d'escalade :</li>
</ul>

<h3>5.4 Gestion des problèmes</h3>

<h4>5.4.1 Travail à réaliser</h4>

Identifier <strong>5 problèmes potentiels</strong> (causes profondes récurrentes) et leur traitement :

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Problème</th><th>Incidents associés</th><th>Cause racine identifiée</th><th>Solution définitive proposée</th><th>Délai de mise en œuvre</th></tr>
    </thead>
    <tbody>
      <tr><td>Exemple : Lenteurs fréquentes de l'application</td><td>Incidents de timeout récurrents</td><td>Requêtes SQL non optimisées</td><td>Optimisation des index et requêtes</td><td>2 semaines</td></tr>
      <tr><td>1.</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>2.</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>3.</td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

<h3>5.5 Gestion des changements</h3>

<h4>5.5.1 Travail à réaliser</h4>

<ol>
  <li><strong>Définir les types de changements</strong> pour l'application TechStore :</li>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Type</th><th>Description</th><th>Niveau d'approbation</th><th>Exemple</th></tr>
    </thead>
    <tbody>
      <tr><td>Standard</td><td>Changement pré-approuvé, faible risque</td><td>Automatique</td><td>Mise à jour de sécurité mineure</td></tr>
      <tr><td>Normal</td><td>Changement nécessitant évaluation</td><td></td><td></td></tr>
      <tr><td>Urgent</td><td>Changement d'urgence suite à incident critique</td><td></td><td></td></tr>
    </tbody>
  </table>
</div>

  <li><strong>Décrire le processus de gestion des changements</strong> :</li>

Remplir les étapes manquantes et leur contenu :

<ol>
  <li><strong>Demande de changement</strong> : Qui peut demander ? Quel formulaire ?</li>
  <li><strong>Évaluation des risques</strong> : Quels critères d'évaluation ?</li>
  <li><strong>Approbation</strong> : Qui approuve selon le type ?</li>
  <li><strong>Planification</strong> : Quand effectuer le changement ?</li>
  <li><strong>Tests</strong> : Dans quel environnement tester ?</li>
  <li><strong>Implémentation</strong> : Qui réalise ? Quand ?</li>
  <li><strong>Révision post-implémentation</strong> : Vérifications à effectuer ?</li>
</ol>

  <li><strong>Proposer 3 exemples de changements</strong> avec leur processus :</li>

<strong>Changement 1</strong> : (ex : Ajout d'une nouvelle fonctionnalité)
<ul>
  <li>Type :</li>
  <li>Risques identifiés :</li>
  <li>Plan de tests :</li>
  <li>Procédure de rollback :</li>
</ul>

<strong>Changement 2</strong> :
<ul>
  <li>Type :</li>
  <li>Risques identifiés :</li>
  <li>Plan de tests :</li>
  <li>Procédure de rollback :</li>
</ul>

<strong>Changement 3</strong> :
<ul>
  <li>Type :</li>
  <li>Risques identifiés :</li>
  <li>Plan de tests :</li>
  <li>Procédure de rollback :</li>
</ul>

</ol>

</div>

---

<div class="concept-section" markdown="1">
<h2 class="section-title">6 Format du rendu</h2>

<h3>6.1 Contenu du PDF</h3>

Faire contenir au document PDF <strong>dans l'ordre</strong> :

<ol>
  <li><strong>Page de garde</strong> :
    <ul>
      <li>Titre : "Étude de cas FuchsTechnology"</li>
      <li>Vos noms et prénoms</li>
      <li>Classe : BTS SIO SLAM 2</li>
      <li>Date</li>
    </ul>
  </li>
  <li><strong>Sommaire</strong> avec pagination</li>
  <li><strong>Partie 1 : Inventaire CMDB du patrimoine informatique</strong>
    <ul>
      <li>Tableau CMDB matériel</li>
      <li>Tableau CMDB licences</li>
      <li>Explication méthodologie de projet</li>
    </ul>
  </li>
  <li><strong>Partie 2 : Diagramme de Gantt</strong>
    <ul>
      <li>Image du Gantt</li>
      <li>Durée totale du projet</li>
      <li>Jalons identifiés</li>
    </ul>
  </li>
  <li><strong>Partie 3 : Chemin critique</strong>
    <ul>
      <li>Réseau PERT ou tableau récapitulatif</li>
      <li>Identification du chemin critique</li>
      <li>Justifications et mesures de sécurisation</li>
    </ul>
  </li>
  <li><strong>Partie 4 : Gestion des risques</strong>
    <ul>
      <li>4.1 Risques infrastructurels (tableau + justifications)</li>
      <li>4.2 Risques projet (tableau + justifications)</li>
    </ul>
  </li>
  <li><strong>Partie 5 : Gestion ITIL</strong>
    <ul>
      <li>5.1 Gestion des incidents</li>
      <li>5.2 Gestion des problèmes</li>
      <li>5.3 Gestion des changements</li>
      <li>5.4 Outils et organisation</li>
    </ul>
  </li>
</ol>

<h3>6.2 Critères d'évaluation</h3>

<div class="table-section">
  <table class="styled-table">
    <thead>
      <tr><th>Critère</th><th>Points</th></tr>
    </thead>
    <tbody>
      <tr><td>Devis réaliste et respectant le budget</td><td>/3</td></tr>
      <tr><td>Inventaire CMDB complet et cohérent</td><td>/4</td></tr>
      <tr><td>Diagramme de Gantt complet et cohérent</td><td>/3</td></tr>
      <tr><td>Chemin critique correctement identifié et justifié</td><td>/3</td></tr>
      <tr><td>Analyse des risques pertinente et complète</td><td>/4</td></tr>
      <tr><td>Gestion ITIL cohérente et appliquée</td><td>/3</td></tr>
      <tr><td><strong>TOTAL</strong></td><td><strong>/20</strong></td></tr>
    </tbody>
  </table>
</div>

</div>
