<style>
/* Styles modernes B1 – alignés avec Chemin Critique, Gestion de Projet, Gestion des Risques, ITIL */
.course-header {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
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
    color: #3498db;
    margin-bottom: 1.5rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 0.8rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.05rem;
    line-height: 1.6;
}

.content-text {
    color: var(--md-default-fg-color);
    line-height: 1.7;
    margin: 1.2rem 0;
    font-size: 1.05rem;
}

.highlight-fact {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.warning-fact {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.scenario-box {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f39c12;
    border-radius: 8px;
    padding: 1.2rem;
    margin: 1rem 0;
}

.exercise-container {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #3498db;
}

.exercise-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2980b9;
    margin-bottom: 1rem;
}

/* Navigation d’exercices – alignée avec Gestion_risques et ITIL */
.exercise-navigation {
    background: white;
    border-radius: 15px;
    padding: 1rem;
    margin: 2rem 0;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}
.exercise-tabs {
    display: flex;
    border-bottom: 2px solid #ecf0f1;
    margin-bottom: 1rem;
    overflow-x: auto;
    gap: 0.5rem;
    padding-bottom: 0.5rem;
    scrollbar-width: thin;
    scrollbar-color: #bdc3c7 #ecf0f1;
}
.exercise-tabs::-webkit-scrollbar { height: 6px; }
.exercise-tabs::-webkit-scrollbar-track { background: #ecf0f1; border-radius: 3px; }
.exercise-tabs::-webkit-scrollbar-thumb { background: #bdc3c7; border-radius: 3px; }
.exercise-tabs::-webkit-scrollbar-thumb:hover { background: #95a5a6; }
.exercise-tab {
    background: none;
    border: none;
    padding: 0.8rem 1.2rem;
    cursor: pointer;
    font-weight: 600;
    color: #7f8c8d;
    border-bottom: 3px solid transparent;
    transition: all 0.3s ease;
    white-space: nowrap;
    flex-shrink: 0;
    min-width: 160px;
    font-size: 0.95rem;
    border-radius: 8px 8px 0 0;
}
.exercise-tab:hover { color: #3498db; background: rgba(52, 152, 219, 0.05); }
.exercise-tab.active { color: #2980b9; border-bottom-color: #3498db; background: rgba(52, 152, 219, 0.1); }
.exercise-content-wrapper { display: none; }
.exercise-content-wrapper.active { display: block; animation: fadeIn 0.3s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 768px) {
    .course-title { font-size: 2rem; }
    .course-header { padding: 2rem; }
}
/* Titres H3 stylisés (pour sous-sections) */
h3.subsection-title {
    font-size: 1.6rem;
    font-weight: 600;
    color: #3498db;
    margin: 1.5rem 0 0.8rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid rgba(52, 152, 219, 0.25);
}

/* Titres H4 stylisés (pour sous-sous-sections) */
h4.subsubsection-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 1.2rem 0 0.6rem 0;
    padding-bottom: 0.3rem;
    border-bottom: 1px dashed rgba(44, 62, 80, 0.3);
}

/* Tableaux d'exercices */
.exercise-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 8px;
    overflow: hidden;
}
.exercise-table th, .exercise-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(52, 152, 219, 0.2);
}
.exercise-table th {
    background: rgba(52, 152, 219, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

/* Matrice des risques – reprise depuis Gestion_risques (B1) */
.risk-matrix {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
}
.matrix-grid {
    display: grid;
    grid-template-columns: 120px repeat(5, 1fr);
    grid-template-rows: 60px repeat(5, 60px);
    gap: 2px;
    max-width: 650px;
    margin: 0 auto;
}
.matrix-header {
    background: linear-gradient(135deg, #3498db, #9b59b6);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    border-radius: 5px;
    font-size: 0.9rem;
    text-align: center;
    line-height: 1.2;
}
.matrix-header:first-child {
    background: linear-gradient(135deg, #2c3e50, #34495e);
    font-size: 0.8rem;
    padding: 0.5rem;
}
.matrix-label {
    background: rgba(52, 152, 219, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    color: #3498db;
    border-radius: 5px;
}
.matrix-cell {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 5px;
    font-weight: 600;
    color: white;
    font-size: 0.9rem;
}
.risk-low { background: linear-gradient(135deg, #27ae60, #2ecc71); }
.risk-medium { background: linear-gradient(135deg, #f39c12, #e67e22); }
.risk-high { background: linear-gradient(135deg, #e74c3c, #c0392b); }
.risk-critical { background: linear-gradient(135deg, #8e44ad, #9b59b6); }
</style>

<div class="course-header">
  <h1 class="course-title">🛡️ B3.1 — Fondamentaux de la cybersécurité</h1>
  <p class="course-subtitle">BTS SIO • Bloc 3 — Concepts et mises en pratique</p>
</div>

<div class="concept-section">
  <h2 class="section-title">🎯 Le périmètre : qu'est-ce qu'un Système d'Information (SI) ?</h2>

  <div class="definition-box">
    <div class="definition-title">🔹 Définition</div>
    <div class="definition-content">
      Un <strong>Système d'Information (SI)</strong> regroupe l'ensemble des ressources (matérielles, logicielles, humaines, procédurales et informationnelles) qui permettent de collecter, traiter, stocker et diffuser des informations au sein d'une organisation.
      <br/><br/>
      Le SI est au cœur du fonctionnement d'une entreprise moderne. Sa protection est donc essentielle pour assurer la continuité d'activité.
    </div>
  </div>

<h3 class="subsection-title">1.2 Typologie des actifs</h3>

<div class="content-text"><p>Un actif est un élément du SI ayant de la valeur pour l'organisation. On distingue plusieurs types d'actifs :</p></div>

<div class="definition-box">
  <div class="definition-title">Actifs matériels</div>
  <div class="definition-content content-text">
    <ul>
      <li>Postes de travail (ordinateurs, laptops)</li>
      <li>Serveurs (physiques ou virtuels)</li>
      <li>Équipements réseau (routeurs, switches, pare-feu)</li>
      <li>Baies de stockage (NAS, SAN)</li>
      <li>Équipements périphériques (imprimantes, scanners)</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Actifs logiciels</div>
  <div class="definition-content content-text">
    <ul>
      <li>Systèmes d'exploitation (Windows, Linux, macOS)</li>
      <li>Applications métiers (ERP, CRM, logiciels spécifiques)</li>
      <li>Bases de données (MySQL, PostgreSQL, Oracle)</li>
      <li>Logiciels de sécurité (antivirus, pare-feu logiciels)</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Actifs informationnels</div>
  <div class="definition-content content-text">
    <ul>
      <li>Données clients et prospects</li>
      <li>Données financières et comptables</li>
      <li>Secrets industriels et brevets</li>
      <li>Documents RH et données personnelles des employés</li>
      <li>Code source et propriété intellectuelle</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Actifs humains</div>
  <div class="definition-content content-text">
    <ul>
      <li>Utilisateurs finaux</li>
      <li>Administrateurs systèmes et réseaux</li>
      <li>Développeurs</li>
      <li>Prestataires externes</li>
      <li>Direction</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Actifs immatériels</div>
  <div class="definition-content content-text">
    <ul>
      <li>Réputation et image de marque</li>
      <li>Licences et contrats</li>
      <li>Processus métiers</li>
      <li>Savoir-faire et compétences</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">1.3 Notion de criticité</h3>

<div class="definition-box">
  <div class="definition-title">Criticité des actifs</div>
  <div class="definition-content content-text">
    <p>Tous les actifs n'ont pas la même importance. La <strong>criticité</strong> d'un actif dépend de :</p>
    <ul>
      <li>Son importance pour le fonctionnement de l'organisation</li>
      <li>La sensibilité des données qu'il contient</li>
      <li>L'impact de sa compromission ou indisponibilité</li>
      <li>Sa valeur financière</li>
    </ul>
  </div>
</div>

<div class="highlight-fact">💡 Exemple : Le serveur de base de données clients d'un site e-commerce est plus critique qu'un poste de travail d'un stagiaire.</div>



</div>

<div class="exercise-container">
  <div class="exercise-title">📝 EXERCICE 1 : Identification et classification des actifs</div>
  <div class="content-text">
    <p><strong>Contexte :</strong> La société TechStore est une PME de 30 salariés qui vend du matériel informatique en ligne.</p>
    <p>Elle possède un site e-commerce développé en interne, gère une base de données clients, et dispose d’un réseau informatique interne.</p>
    <p>Votre mission est d’analyser les actifs de l’entreprise et de les classer selon leur criticité (1 = le plus critique).</p>
  </div>

  <div class="exercise-title">Consignes</div>
  <ol class="content-text">
    <li>Pour chaque actif, indiquer sa catégorie (matériel, logiciel, informationnel, humain, immatériel)</li>
    <li>Classer par ordre de criticité (1 = le plus critique, 12 = le moins critique)</li>
    <li>Justifier le classement des 3 actifs les plus critiques</li>
  </ol>

  <div class="exercise-title">Format de réponse attendu</div>
  <table class="exercise-table">
    <thead>
      <tr>
        <th>N°</th>
        <th>Actif</th>
        <th>Catégorie</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>Serveur hébergeant le site e-commerce</td><td></td></tr>
      <tr><td>2</td><td>Base de données clients (informations personnelles et historiques d’achat)</td><td></td></tr>
      <tr><td>3</td><td>Site web e-commerce (application développée en interne)</td><td></td></tr>
      <tr><td>4</td><td>Ordinateurs des employés (postes de travail)</td><td></td></tr>
      <tr><td>5</td><td>Responsable informatique (administrateur réseau/système)</td><td></td></tr>
      <tr><td>6</td><td>Réputation et avis clients sur Internet</td><td></td></tr>
      <tr><td>7</td><td>Fichier comptable annuel (bilan, factures, salaires)</td><td></td></tr>
      <tr><td>8</td><td>Routeur et pare-feu de l’entreprise</td><td></td></tr>
      <tr><td>9</td><td>Logiciel de gestion des stocks</td><td></td></tr>
      <tr><td>10</td><td>Employé du service client</td><td></td></tr>
      <tr><td>11</td><td>Nom de domaine "techstore.fr"</td><td></td></tr>
      <tr><td>12</td><td>Données de connexion (identifiants employés)</td><td></td></tr>
    </tbody>
  </table>
</div>



<div class="concept-section">
  <h2 class="section-title">🔒 Les trois piliers de la sécurité : Confidentialité – Intégrité – Disponibilité (CIA)</h2>

<div class="content-text"><p>La sécurité informatique repose sur trois piliers fondamentaux, souvent appelés <strong>triade CIA</strong> :</p></div>

<div class="definition-box">
  <div class="definition-title">🔐 2.1 Confidentialité</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> La confidentialité garantit que l'information n'est accessible qu'aux personnes autorisées.</p>
    <p><strong>Objectif :</strong> Protéger contre la divulgation non autorisée d'informations.</p>
    <p><strong>Exemples de mesures :</strong></p>
    <ul>
      <li>Chiffrement des données (au repos et en transit)</li>
      <li>Contrôle d'accès (authentification, autorisation)</li>
      <li>Classification des données</li>
      <li>VPN pour les accès distants</li>
    </ul>
  </div>
  <div class="highlight-fact">💡 Exemple de violation : Un employé malveillant copie la base de données clients sur une clé USB et la vend à un concurrent.</div>
</div>

<div class="definition-box">
  <div class="definition-title">🧱 2.2 Intégrité</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> L'intégrité assure que l'information n'a pas été modifiée de manière non autorisée ou accidentelle.</p>
    <p><strong>Objectif :</strong> Protéger contre l'altération des données.</p>
    <p><strong>Exemples de mesures :</strong></p>
    <ul>
      <li>Fonctions de hachage (SHA-256, MD5)</li>
      <li>Signatures numériques</li>
      <li>Contrôles d'accès en écriture</li>
      <li>Journalisation (logs)</li>
      <li>Sauvegardes régulières</li>
    </ul>
  </div>
  <div class="highlight-fact">💡 Exemple de violation : Un attaquant modifie les prix des produits dans la base de données d'un site e-commerce.</div>
</div>

<div class="definition-box">
  <div class="definition-title">⚙️ 2.3 Disponibilité</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> La disponibilité garantit que les services et données sont accessibles quand nécessaire.</p>
    <p><strong>Objectif :</strong> Protéger contre les interruptions de service.</p>
    <p><strong>Exemples de mesures :</strong></p>
    <ul>
      <li>Sauvegardes et restaurations testées</li>
      <li>Redondance des systèmes (serveurs, liens réseau)</li>
      <li>Plan de Reprise d'Activité (PRA) / Plan de Continuité d'Activité (PCA)</li>
      <li>Protection contre les attaques DDoS</li>
      <li>Maintenance préventive</li>
    </ul>
  </div>
  <div class="highlight-fact">💡 Exemple de violation : Une attaque DDoS rend le site web d'une banque inaccessible pendant plusieurs heures.</div>
</div>

</div>
<h3 class="subsection-title">2.4 Autres propriétés de sécurité</h3>

<div class="definition-box">
  <div class="definition-title">Propriétés complémentaires</div>
  <div class="definition-content content-text">
    <p>Bien que la triade CIA soit fondamentale, d'autres propriétés sont importantes :</p>
    <ul>
      <li><strong>Traçabilité (Auditabilité)</strong> : capacité à retracer les actions effectuées.</li>
      <li><strong>Non-répudiation</strong> : chaque action ne peut être niée par un tiers.</li>
      <li><strong>Authenticité</strong> : garantie de l'identité d'une entité.</li>
      <li><strong>Preuve</strong> : capacité à démontrer qu'un événement s'est produit.</li>
    </ul>
  </div>
</div>



<div class="exercise-container">
  <div class="exercise-title">📝 EXERCICE 2 : Association piliers CIA et scénarios</div>
  <div class="exercise-title">Consigne</div>
  <div class="content-text"><p>Pour chaque scénario, identifier quel(s) pilier(s) de la triade CIA est/sont compromis. Justifier la réponse.</p></div>

  <div class="exercise-title">Scénarios</div>
  <ol class="content-text">
    <li>Un ransomware chiffre tous les fichiers d'un serveur de fichiers partagés. Les employés ne peuvent plus accéder à leurs documents de travail.</li>
    <li>Un administrateur système modifie accidentellement la configuration d'un routeur, ce qui entraîne des pertes de paquets et des erreurs de transmission.</li>
    <li>Un pirate informatique intercepte les communications entre un client et le serveur web d'une banque en ligne, et récupère les identifiants de connexion.</li>
    <li>Une panne électrique prolongée met hors service le datacenter d'une entreprise pendant 8 heures.</li>
    <li>Un employé mécontent modifie les adresses de livraison dans la base de données avant de quitter l'entreprise.</li>
    <li>Un mail contenant des informations confidentielles sur un projet est envoyé par erreur à tous les employés au lieu d'être envoyé uniquement à l'équipe projet.</li>
  </ol>

  <div class="exercise-title">Format de réponse attendu</div>
  <table class="exercise-table">
    <thead>
      <tr>
        <th>Scénario</th>
        <th>Pilier(s) compromis</th>
        <th>Justification</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>...</td><td>...</td></tr>
    </tbody>
  </table>
</div>



<div class="concept-section">
  <h2 class="section-title">⚠️ Menaces, vulnérabilités, incidents et risques</h2>

<h3 class="subsection-title">3.1 Définitions</h3>

<div class="definition-box">
  <div class="definition-title">⚠️ Menace</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> Une menace est un événement (intentionnel ou accidentel) susceptible d'exploiter une vulnérabilité et de causer un dommage.</p>
    <p><strong>Types de menaces :</strong></p>
    <ul>
      <li><strong>Menaces humaines intentionnelles</strong> : attaquants externes (hackers), employés malveillants, cybercriminels, espionnage industriel</li>
      <li><strong>Menaces humaines non intentionnelles</strong> : erreurs humaines, négligence, mauvaise manipulation</li>
      <li><strong>Menaces techniques</strong> : malwares (virus, trojans, ransomware), failles logicielles, défaillances matérielles</li>
      <li><strong>Menaces environnementales</strong> : catastrophes naturelles (inondations, incendies), pannes électriques, dégâts des eaux</li>
    </ul>
  </div>
  <div class="highlight-fact">💡 Exemple : Un groupe de cybercriminels spécialisé dans le ransomware.</div>
</div>

<div class="definition-box">
  <div class="definition-title">🔓 Vulnérabilité</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> Une vulnérabilité est une faiblesse d'un actif susceptible d'être exploitée par une menace.</p>
    <p><strong>Types de vulnérabilités :</strong></p>
    <ul>
      <li><strong>Vulnérabilités techniques</strong> : failles logicielles non patchées (CVE), configurations par défaut, absence de chiffrement</li>
      <li><strong>Vulnérabilités organisationnelles</strong> : absence de procédures, manque de formation, absence de politique de sécurité</li>
      <li><strong>Vulnérabilités physiques</strong> : absence de contrôle d'accès physique, câblage non sécurisé</li>
      <li><strong>Vulnérabilités humaines</strong> : manque de sensibilisation, absence de vigilance</li>
    </ul>
  </div>
  <div class="highlight-fact">💡 Exemple : Un serveur Windows non patché depuis 6 mois présentant des failles de sécurité connues.</div>
</div>

<div class="definition-box">
  <div class="definition-title">🚨 Incident</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> Un incident est la réalisation effective d'une menace exploitant une vulnérabilité, entraînant un impact réel sur l'organisation.</p>
  </div>
  <div class="highlight-fact">💡 Exemple : Une attaque ransomware réussie ayant chiffré l'ensemble des serveurs de fichiers.</div>
</div>

<div class="definition-box">
  <div class="definition-title">📈 Risque</div>
  <div class="definition-content content-text">
    <p><strong>Définition :</strong> Le risque est la combinaison de la vraisemblance (probabilité) qu'un événement se produise et de son impact (gravité des conséquences).</p>
    <p><strong>Formule fondamentale :</strong></p>
    <pre><code>Risque = Vraisemblance × Impact</code></pre>
    <p><strong>Où :</strong></p>
    <ul>
      <li><strong>Vraisemblance</strong> (ou probabilité) tient compte de :
        <ul>
          <li>La présence et la motivation de la menace</li>
          <li>Les capacités de l'attaquant</li>
          <li>L'existence et la sévérité des vulnérabilités</li>
          <li>Les mesures de sécurité déjà en place</li>
        </ul>
      </li>
      <li><strong>Impact</strong> évalue les conséquences potentielles sur :
        <ul>
          <li>L'aspect financier</li>
          <li>L'aspect opérationnel</li>
          <li>L'aspect réputationnel</li>
          <li>L'aspect juridique</li>
          <li>L'aspect humain (sécurité des personnes)</li>
        </ul>
      </li>
    </ul>
  </div>
</div>
<h3 class="subsection-title">3.2 Relation entre les concepts</h3>

```
MENACE + VULNÉRABILITÉ = RISQUE POTENTIEL

Si la MENACE exploite la VULNÉRABILITÉ = INCIDENT

INCIDENT → IMPACT sur l'organisation
```

<div class="definition-box">
  <div class="definition-title">💡 Exemple concret</div>
  <div class="definition-content content-text">
    <ul>
      <li>Menace : Groupe de hackers ciblant les PME avec des ransomwares</li>
      <li>Vulnérabilité : Absence de sauvegardes hors ligne dans une PME</li>
      <li>Risque : Probabilité élevée que la PME soit victime d'un ransomware avec impact critique</li>
      <li>Incident : Attaque ransomware réussie</li>
      <li>Impact : Perte de toutes les données, arrêt d'activité, paiement de rançon</li>
    </ul>
  </div>
  
</div>



<div class="exercise-container">
  <div class="exercise-title">📝 EXERCICE 3 : Distinction menace / vulnérabilité / risque / incident</div>
  <div class="exercise-title">Consigne</div>
  <div class="content-text"><p>Pour chaque situation, identifier s'il s'agit d'une menace, d'une vulnérabilité, d'un risque ou d'un incident. Justifier.</p></div>

  <div class="exercise-title">Situations</div>
  <ol class="content-text">
    <li>Le serveur web de l'entreprise fonctionne avec une version d'Apache datant de 2018.</li>
    <li>Un groupe de hackers connu sous le nom de "DarkSide" cible les entreprises du secteur de la santé.</li>
    <li>La combinaison d'un serveur obsolète et de l'existence de groupes malveillants pourrait entraîner une compromission du système avec un impact financier de 200 000€.</li>
    <li>Un employé clique sur un lien de phishing et installe un malware sur son poste, qui se propage ensuite à 15 autres machines du réseau.</li>
    <li>Les employés n'ont jamais été formés à reconnaître les tentatives de phishing.</li>
    <li>Un concurrent tente régulièrement d'obtenir des informations confidentielles sur les projets de recherche de l'entreprise.</li>
    <li>L'entreprise pourrait subir un vol de données confidentielles par un concurrent, ce qui entraînerait une perte d'avantage concurrentiel estimée à 500 000€.</li>
    <li>Les mots de passe des comptes administrateurs sont stockés dans un fichier Excel non protégé sur un partage réseau accessible à tous.</li>
  </ol>

  <div class="exercise-title">Format de réponse attendu</div>
  <table class="exercise-table">
    <thead>
      <tr>
        <th>N°</th>
        <th>Type</th>
        <th>Justification</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>...</td><td>...</td></tr>
    </tbody>
  </table>
</div>



</div>
<div class="concept-section">
  <h2 class="section-title">4. Les enjeux de la cybersécurité</h2>

  <div class="content-text">
    <p>La cybersécurité est un enjeu majeur pour toutes les organisations, quelle que soit leur taille. Une attaque réussie peut avoir des conséquences graves et durables.</p>
  </div>

  <h3 class="subsection-title">4.1 Conséquences financières</h3>

  <div class="content-text">
    <p>Les impacts financiers d'une cyberattaque sont souvent sous-estimés et peuvent être dévastateurs :</p>
  </div>

  <div class="content-text">
    <p><strong>Coûts directs :</strong></p>
    <ul>
      <li>Perte d'argent par vol (fraude bancaire, détournement)</li>
      <li>Paiement de rançons (ransomware)</li>
      <li>Coûts de remédiation et de récupération</li>
      <li>Frais d'expertise (consultants, forensics)</li>
      <li>Frais juridiques</li>
      <li>Investissements de sécurité d'urgence</li>
    </ul>
  </div>

  <div class="content-text">
    <p><strong>Coûts indirects :</strong></p>
    <ul>
      <li>Perte de clients et de revenus</li>
      <li>Arrêt de production</li>
      <li>Perte de contrats</li>
      <li>Baisse du cours de l'action (pour les sociétés cotées)</li>
      <li>Augmentation des primes d'assurance</li>
    </ul>
  </div>

  <div class="highlight-fact">
    <p>📊 <strong>Chiffres clés :</strong></p>
    <ul>
      <li>Coût moyen d'une violation de données : <strong>4,5 millions d'euros</strong></li>
      <li>Coût moyen d'une attaque ransomware : <strong>4,5 millions d'euros</strong></li>
      <li>Temps moyen d'arrêt lors d'un ransomware : <strong>21 jours</strong></li>
      <li>60% des PME victimes d'une cyberattaque ferment dans les 6 mois</li>
    </ul>
  </div>

  <h3 class="subsection-title">4.2 Conséquences réputationnelles</h3>

  <div class="content-text">
    <p>L'impact sur l'image est souvent le plus durable :</p>
    <ul>
      <li>Perte de confiance des clients et partenaires</li>
      <li>Détérioration de l'image de marque</li>
      <li>Couverture médiatique négative</li>
      <li>Perte de compétitivité</li>
      <li>Difficultés de recrutement</li>
      <li>Méfiance des investisseurs</li>
    </ul>
  </div>

  <div class="highlight-fact">
    <p><strong>💡 Exemple :</strong> La cyber-attaque du vendredi 10 octobre 2025 paralyse totalement les systèmes informatiques de l'académie de Lille et d'Amiens. Le ransomware russe Qilin serait responsable de cette paralysie.</p>
  </div>

  <h3 class="subsection-title">4.3 Conséquences juridiques</h3>
  <div class="content-text">
    <p>Le cadre légal impose des obligations strictes :</p>
    <ul>
      <li>Sanctions RGPD (jusqu'à 4% du chiffre d'affaires mondial annuel ou 20 millions d'euros)</li>
      <li>Poursuites judiciaires par les victimes</li>
      <li>Amendes réglementaires</li>
      <li>Responsabilité civile et pénale des dirigeants</li>
      <li>Obligation de notification aux autorités (CNIL) et aux personnes concernées</li>
      <li>Audits et contrôles renforcés</li>
    </ul>
  </div>
  <div class="highlight-fact">
    <p><strong>💡 Exemple :</strong> British Airways a été condamnée à une amende de 20 millions de livres sterling en 2020 pour une violation de données affectant 400 000 clients.</p>
  </div>

  <h3 class="subsection-title">4.4 Conséquences opérationnelles</h3>
  <div class="content-text">
    <p>L'impact sur le fonctionnement peut être paralysant :</p>
    <ul>
      <li>Arrêt total ou partiel de l'activité</li>
      <li>Perte de productivité</li>
      <li>Impossibilité de livrer les clients</li>
      <li>Rupture de la chaîne d'approvisionnement</li>
      <li>Perte de données critiques</li>
    </ul>
  </div>

  <h3 class="subsection-title">4.5 Conséquences humaines</h3>
  <div class="content-text">
    <p>L'aspect humain est souvent négligé :</p>
    <ul>
      <li>Stress et anxiété des employés</li>
      <li>Licenciements suite à une fermeture</li>
      <li>Mise en danger dans certains secteurs (santé, infrastructures critiques)</li>
      <li>Atteinte à la vie privée des personnes concernées</li>
    </ul>
  </div>

  <div class="highlight-fact">
    <p><strong>💡 Exemple concret : WannaCry (2017)</strong></p>
    <ul>
      <li>Plus de 100 millions d'euros de pertes</li>
      <li>19 000 rendez-vous médicaux annulés</li>
      <li>Opérations chirurgicales reportées</li>
      <li>Ambulances détournées</li>
      <li>Mise en danger de patients</li>
    </ul>
  </div>



<div class="concept-section">
  <h2 class="section-title">5. Typologie des menaces (détaillée)</h2>

<h3 class="subsection-title">5.1 Menaces humaines intentionnelles</h3>

<div class="definition-box">
  <div class="definition-title">Attaquants externes (hackers)</div>
  <div class="definition-content content-text">
    <ul>
      <li>Script kiddies : attaquants peu qualifiés utilisant des outils existants</li>
      <li>Hacktivistes : motivés par des causes politiques ou sociales</li>
      <li>Cybercriminels : motivés par l'argent (ransomware, fraude)</li>
      <li>Concurrents : espionnage industriel</li>
    </ul>
  </div>
  
</div>

<div class="definition-box">
  <div class="definition-title">Menaces internes</div>
  <div class="definition-content content-text">
    <ul>
      <li>Employés malveillants : sabotage, vol de données, revente d'informations</li>
      <li>Employés négligents : erreurs, non-respect des procédures</li>
      <li>Anciens employés : accès non révoqués, connaissance de l'infrastructure</li>
    </ul>
  </div>
  
</div>

<h3 class="subsection-title">5.2 Menaces techniques</h3>

<div class="definition-box">
  <div class="definition-title">Malwares (logiciels malveillants)</div>
  <div class="definition-content content-text">
    <ul>
      <li>Virus : se propage en s'attachant à des fichiers</li>
      <li>Vers : se propage de manière autonome sur le réseau</li>
      <li>Trojans (chevaux de Troie) : se déguise en logiciel légitime</li>
      <li>Ransomware : chiffre les données et demande une rançon</li>
      <li>Spyware : collecte des informations à l'insu de l'utilisateur</li>
      <li>Rootkit : dissimule sa présence et donne un accès privilégié</li>
      <li>Botnet : réseau d'ordinateurs compromis contrôlés à distance</li>
    </ul>
  </div>
  
</div>

<div class="definition-box">
  <div class="definition-title">Failles et vulnérabilités logicielles</div>
  <div class="definition-content content-text">
    <ul>
      <li>Bugs dans le code</li>
      <li>Vulnérabilités zero-day (non encore corrigées)</li>
      <li>Configurations par défaut non sécurisées</li>
      <li>Logiciels obsolètes non maintenus</li>
    </ul>
  </div>
  
</div>

<div class="definition-box">
  <div class="definition-title">Attaques réseau</div>
  <div class="definition-content content-text">
    <ul>
      <li>DDoS (Distributed Denial of Service) : saturation des ressources</li>
      <li>Man-in-the-Middle (MitM) : interception des communications</li>
      <li>Sniffing : écoute du trafic réseau</li>
      <li>Spoofing : usurpation d'identité (IP, DNS, ARP)</li>
    </ul>
  </div>
  
</div>

<div class="definition-box">
  <div class="definition-title">Défaillances systèmes</div>
  <div class="definition-content content-text">
    <ul>
      <li>Pannes matérielles</li>
      <li>Bugs système</li>
      <li>Incompatibilités logicielles</li>
    </ul>
  </div>
  
</div>

<h3 class="subsection-title">5.3 Menaces environnementales</h3>

<div class="definition-box">
  <div class="definition-title">Menaces environnementales</div>
  <div class="definition-content content-text">
    <ul>
      <li>Catastrophes naturelles : inondations, tremblements de terre, tempêtes</li>
      <li>Incendies</li>
      <li>Dégâts des eaux</li>
      <li>Pannes électriques</li>
      <li>Problèmes de climatisation (surchauffe des serveurs)</li>
      <li>Pandémies (impact sur le personnel, télétravail non préparé)</li>
    </ul>
  </div>
  
</div>

<h3 class="subsection-title">5.4 Menaces légales et contractuelles</h3>

<div class="definition-box">
  <div class="definition-title">Menaces légales et contractuelles</div>
  <div class="definition-content content-text">
    <ul>
      <li>Non-conformité RGPD</li>
      <li>Violations de licences logicielles</li>
      <li>Non-respect des obligations contractuelles</li>
      <li>Changements réglementaires</li>
      <li>Litiges juridiques</li>
    </ul>
  </div>
  
</div>



<div class="exercise-container">
  <div class="exercise-title">📝 EXERCICE 4 : Classification des menaces</div>

  <div class="exercise-title">Consigne</div>
  <div class="content-text"><p>Classer chaque menace dans la catégorie appropriée (Humaine intentionnelle / Humaine non intentionnelle / Technique / Environnementale / Légale). Puis, pour chaque menace, proposer UNE mesure de protection adaptée.</p></div>

  <div class="exercise-title">Liste des menaces</div>
  <ol class="content-text">
    <li>Un développeur mécontent insère une porte dérobée dans le code source avant de quitter l'entreprise.</li>
    <li>Une secrétaire envoie par erreur un document confidentiel à un mauvais destinataire.</li>
    <li>Un ver informatique exploite une faille non patchée pour se propager sur tout le réseau de l'entreprise.</li>
    <li>Une inondation du sous-sol détruit les serveurs qui y étaient stockés.</li>
    <li>L'entreprise utilise un logiciel dont la licence a expiré, ce qui entraîne une violation contractuelle.</li>
    <li>Un groupe APT chinois tente d'accéder aux secrets industriels d'une entreprise aéronautique française.</li>
    <li>Un stagiaire configure mal le pare-feu et expose accidentellement des services internes sur Internet.</li>
    <li>Un tremblement de terre endommage le datacenter principal.</li>
    <li>La CNIL effectue un contrôle et découvre que l'entreprise ne respecte pas ses obligations RGPD.</li>
    <li>Un botnet lance une attaque DDoS massive contre le site web de l'entreprise.</li>
  </ol>

  <div class="exercise-title">Format de réponse attendu</div>
  <table class="exercise-table">
    <thead>
      <tr>
        <th>N°</th>
        <th>Catégorie</th>
        <th>Mesure de protection proposée</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>...</td><td>...</td></tr>
    </tbody>
  </table>
</div>



</div>

<div class="concept-section">
  <h2 class="section-title">6. Exemples d'attaques courantes (détaillées)</h2>

<h3 class="subsection-title">6.1 Phishing (Hameçonnage)</h3>

<div class="definition-box">
  <div class="definition-title">Description</div>
  <div class="definition-content content-text">
    <p>Technique d'ingénierie sociale visant à tromper les victimes pour qu'elles révèlent des informations sensibles (identifiants, mots de passe, données bancaires).</p>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Comment ça fonctionne</div>
  <div class="definition-content content-text">
    <ol>
      <li>L'attaquant envoie un mail frauduleux se faisant passer pour un organisme connu (banque, administration, service IT)</li>
      <li>Le mail contient un lien vers un site web factice (spoofing)</li>
      <li>La victime saisit ses identifiants sur le faux site</li>
      <li>L'attaquant récupère les identifiants et les utilise</li>
    </ol>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Variantes</div>
  <div class="definition-content content-text">
    <ul>
      <li>Spear phishing : attaque ciblée sur une personne spécifique</li>
      <li>Whaling : ciblant les dirigeants</li>
      <li>Vishing : par téléphone</li>
      <li>Smishing : par SMS</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Chiffres clés</div>
  <div class="definition-content content-text">
    <ul>
      <li>30% des utilisateurs ouvrent les mails de phishing</li>
      <li>12% cliquent sur les liens malveillants</li>
      <li>90% des violations de données commencent par un phishing</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Mesures de protection</div>
  <div class="definition-content content-text">
    <ul>
      <li>Formation et sensibilisation des utilisateurs</li>
      <li>Filtrage des mails (anti-spam, anti-phishing)</li>
      <li>Authentification multi-facteurs (MFA)</li>
      <li>Vérification des expéditeurs et des URLs</li>
      <li>Bannières d'avertissement sur les mails externes</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">6.2 Ransomware (Rançongiciel)</h3>

<div class="definition-box">
  <div class="definition-title">Description</div>
  <div class="definition-content content-text">
    <p>Logiciel malveillant qui chiffre les données de la victime et exige une rançon pour les déchiffrer.</p>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Comment ça fonctionne</div>
  <div class="definition-content content-text">
    <ol>
      <li>Infection initiale (phishing, faille RDP, clé USB infectée)</li>
      <li>Exécution du ransomware</li>
      <li>Mouvement latéral (propagation sur le réseau)</li>
      <li>Chiffrement des données</li>
      <li>Affichage de la demande de rançon (généralement en Bitcoin)</li>
      <li>Éventuellement : vol des données avant chiffrement (double extorsion)</li>
    </ol>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Chiffres clés</div>
  <div class="definition-content content-text">
    <ul>
      <li>Coût moyen : 4,5 millions d'euros</li>
      <li>Temps moyen d'arrêt : 21 jours</li>
      <li>32% des victimes paient la rançon</li>
      <li>Seulement 65% de celles qui paient récupèrent leurs données</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Exemples notables</div>
  <div class="definition-content content-text">
    <ul>
      <li>WannaCry (2017) : 300 000 ordinateurs dans 150 pays, 100M€ de pertes pour le NHS</li>
      <li>NotPetya (2017) : 10 milliards de dollars de dommages</li>
      <li>Colonial Pipeline (2021) : paralysie d'un pipeline de carburant aux USA, rançon de 4,4M$</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Mesures de protection</div>
  <div class="definition-content content-text">
    <ul>
      <li>Sauvegardes régulières (règle 3-2-1 : 3 versions dont une hors-site)</li>
      <li>Sauvegardes hors ligne et immutables</li>
      <li>Segmentation réseau</li>
      <li>Mises à jour régulières</li>
      <li>Désactivation des macros Office</li>
      <li>Restriction des droits administrateur</li>
      <li>EDR (Endpoint Detection and Response)</li>
      <li>Plan de réponse aux incidents</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">6.3 DDoS (Déni de Service Distribué)</h3>

<div class="definition-box">
  <div class="definition-title">Description</div>
  <div class="definition-content content-text">
    <p>Attaque visant à rendre un service inaccessible en le saturant de requêtes.</p>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Comment ça fonctionne</div>
  <div class="definition-content content-text">
    <ol>
      <li>L'attaquant contrôle un botnet (réseau de machines compromises)</li>
      <li>Il lance une attaque massive simultanée</li>
      <li>Le serveur cible est saturé et ne peut plus répondre aux utilisateurs légitimes</li>
    </ol>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Types d'attaques DDoS</div>
  <div class="definition-content content-text">
    <ul>
      <li>Volumétriques : saturation de la bande passante (UDP flood, DNS amplification)</li>
      <li>Protocoles : exploitation des faiblesses des protocoles (SYN flood)</li>
      <li>Applicatives : ciblage des applications web (HTTP flood)</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Chiffres clés</div>
  <div class="definition-content content-text">
    <ul>
      <li>Durée moyenne : 4 heures</li>
      <li>Coût moyen : 120 000€ par heure d'indisponibilité</li>
      <li>Taille record : 2.3 Tbps (Amazon, 2020)</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Mesures de protection</div>
  <div class="definition-content content-text">
    <ul>
      <li>Services anti-DDoS (Cloudflare, Akamai)</li>
      <li>Surdimensionnement de la bande passante</li>
      <li>CDN (Content Delivery Network)</li>
      <li>Filtrage du trafic</li>
      <li>Architectures scalables et résilientes</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">6.4 Injection SQL</h3>

<div class="definition-box">
  <div class="definition-title">Description</div>
  <div class="definition-content content-text">
    <p>Attaque exploitant les formulaires web pour injecter du code SQL malveillant et accéder à la base de données.</p>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Comment ça fonctionne</div>
  <div class="definition-content content-text">
    <ol>
      <li>L'attaquant identifie un formulaire vulnérable</li>
      <li>Il injecte du code SQL dans les champs (ex: ' OR '1'='1)</li>
      <li>La requête SQL est modifiée</li>
      <li>L'attaquant contourne l'authentification ou accède aux données</li>
    </ol>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Exemple de code vulnérable</div>
  <div class="definition-content content-text">
    <pre><code class="language-sql">SELECT * FROM users WHERE username = '$username' AND password = '$password'
    </code></pre>
    <p><strong>Injection :</strong> <code>admin' --</code> dans le champ username</p>
    <pre><code class="language-sql">SELECT * FROM users WHERE username = 'admin' --' AND password = ''
    </code></pre>
  </div>
  
</div>

<div class="definition-box">
  <div class="definition-title">Conséquences possibles</div>
  <div class="definition-content content-text">
    <ul>
      <li>Vol de données massif</li>
      <li>Modification de données</li>
      <li>Suppression de données</li>
      <li>Contournement de l'authentification</li>
      <li>Escalade de privilèges</li>
      <li>Exécution de commandes système</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Mesures de protection</div>
  <div class="definition-content content-text">
    <ul>
      <li>Requêtes préparées (prepared statements)</li>
      <li>ORM (Object-Relational Mapping)</li>
      <li>Validation et échappement des entrées</li>
      <li>Principe du moindre privilège pour les comptes BDD</li>
      <li>WAF (Web Application Firewall)</li>
      <li>Tests de sécurité réguliers</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">6.5 Autres attaques importantes</h3>

<h4 class="subsubsection-title">Attaques par force brute</h4>
Tentatives répétées de deviner un mot de passe en essayant toutes les combinaisons possibles.

<h4 class="subsubsection-title">Attaques par dictionnaire</h4>
Utilisation d'une liste de mots de passe courants.

<h4 class="subsubsection-title">Attaque de l'homme du milieu (Man-in-the-Middle)</h4>
Interception des communications entre deux parties.

<h4 class="subsubsection-title">Cross-Site Scripting (XSS)</h4>
Injection de scripts malveillants dans des pages web.

<h4 class="subsubsection-title">Zero-day</h4>
Exploitation d'une vulnérabilité inconnue avant qu'un correctif soit disponible.



<div class="exercise-container">
  <div class="exercise-title">📝 EXERCICE 5 : Étude de cas - Analyse d'une attaque</div>

  <div class="exercise-title">Contexte</div>
  <div class="content-text"><p>L'entreprise "MediCare", une clinique privée de 100 employés, a été victime d'une cyberattaque. Voici le déroulé des événements :</p></div>

  <div class="exercise-title">Chronologie</div>
  <ol class="content-text">
    <li>Jour 1, 9h30 : Un employé de la comptabilité reçoit un mail prétendant provenir du directeur financier, demandant de cliquer sur un lien pour consulter un document urgent.</li>
    <li>Jour 1, 9h35 : L'employé clique sur le lien et entre ses identifiants sur une page de connexion factice.</li>
    <li>Jour 1, 14h00 : L'attaquant utilise les identifiants volés pour se connecter au VPN de l'entreprise depuis l'étranger.</li>
    <li>Jour 1, 14h30 : L'attaquant se déplace latéralement sur le réseau et identifie les serveurs contenant les dossiers médicaux.</li>
    <li>Jour 2, 3h00 : L'attaquant déploie un ransomware qui commence à chiffrer les données.</li>
    <li>Jour 2, 8h00 : Les employés découvrent que tous les dossiers médicaux sont inaccessibles. Un message de rançon demande 500 000€ en Bitcoin.</li>
    <li>Jour 2, 8h30 : Les opérations chirurgicales de la journée doivent être annulées. Les rendez-vous médicaux ne peuvent plus être honorés.</li>
  </ol>

  <div class="exercise-title">Informations complémentaires</div>
  <ul class="content-text">
    <li>L'entreprise n'avait pas de sauvegardes récentes des dossiers médicaux</li>
    <li>L'authentification à deux facteurs n'était pas activée sur le VPN</li>
    <li>Les employés n'avaient jamais reçu de formation sur le phishing</li>
    <li>Tous les postes avaient des droits administrateur</li>
    <li>Le réseau n'était pas segmenté</li>
  </ul>

  <div class="exercise-title">Consignes</div>
  <ol class="content-text">
    <li>Identifiez le type d'attaque initial (vecteur d'entrée)</li>
    <li>Listez toutes les vulnérabilités qui ont permis à l'attaque de réussir (minimum 5)</li>
    <li>Pour chaque pilier de la triade CIA, indiquez s'il a été compromis et comment</li>
    <li>Évaluez les conséquences de cette attaque (financières, opérationnelles, juridiques, réputationnelles)</li>
    <li>Proposez 5 mesures de sécurité prioritaires qui auraient pu prévenir cette attaque</li>
    <li>L'entreprise doit-elle notifier cet incident à la CNIL ? Justifiez et dans quel délai</li>
  </ol>

  <div class="exercise-title">Format de réponse attendu</div>
  <div class="content-text"><p>Rédigez une analyse structurée répondant à chaque point.</p></div>
</div>



</div>

<div class="concept-section">
  <h2 class="section-title">7. Calcul du risque (méthodologie détaillée)</h2>

<h3 class="subsection-title">7.1 Formule fondamentale du risque</h3>

```
RISQUE = VRAISEMBLANCE × IMPACT
```

Cette formule simple permet d'évaluer et de prioriser les risques de sécurité.

<h3 class="subsection-title">7.2 Évaluation de la vraisemblance</h3>

La vraisemblance (ou probabilité) qu'une menace se réalise dépend de plusieurs facteurs :

<h4 class="subsubsection-title">Échelle de vraisemblance</h4>

<div class="definition-box">
  <div class="definition-title">Échelle de vraisemblance</div>
  <div class="definition-content content-text">
    <table class="exercise-table">
      <thead>
        <tr>
          <th>Niveau</th>
          <th>Valeur</th>
          <th>Probabilité</th>
          <th>Description</th>
          <th>Exemple</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Faible</td>
          <td>1</td>
          <td>&lt; 5%</td>
          <td>Événement exceptionnel, peu probable</td>
          <td>Attaque APT ciblée sur une petite PME</td>
        </tr>
        <tr>
          <td>Moyen</td>
          <td>2</td>
          <td>5–25%</td>
          <td>Événement rare</td>
          <td>Sabotage interne dans une entreprise avec bonne culture sécurité</td>
        </tr>
        <tr>
          <td>Élevé</td>
          <td>3</td>
          <td>25–75%</td>
          <td>Événement possible</td>
          <td>Attaque par force brute sur un service exposé</td>
        </tr>
        <tr>
          <td>Très élevé</td>
          <td>4</td>
          <td>75–95%</td>
          <td>Événement probable</td>
          <td>Phishing sur des employés non formés</td>
        </tr>
        <tr>
          <td>Critique</td>
          <td>5</td>
          <td>&gt; 95%</td>
          <td>Événement quasi certain</td>
          <td>Exploitation d'une vulnérabilité critique non patchée et publiquement connue</td>
        </tr>
      </tbody>
    </table>
  </div>
  
</div>

<h4 class="subsubsection-title">Facteurs influençant la vraisemblance</h4>

<div class="definition-box">
  <div class="definition-title">Facteurs influençant la vraisemblance</div>
  <div class="definition-content content-text">
    <ul>
      <li>Attractivité de la cible : secteur d'activité, taille, données sensibles</li>
      <li>Niveau de menace : existence de groupes actifs ciblant le secteur</li>
      <li>Vulnérabilités présentes : failles connues, configurations faibles</li>
      <li>Mesures de sécurité en place : plus elles sont efficaces, plus la vraisemblance diminue</li>
      <li>Historique des incidents : incidents passés dans l'organisation ou le secteur</li>
      <li>Contexte géopolitique : tensions internationales, conflits</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">7.3 Évaluation de l'impact</h3>

L'impact mesure la gravité des conséquences si l'événement se produit.

<h4 class="subsubsection-title">Échelle d'impact</h4>

<div class="definition-box">
  <div class="definition-title">Échelle d'impact</div>
  <div class="definition-content content-text">
    <table class="exercise-table">
      <thead>
        <tr>
          <th>Niveau</th>
          <th>Valeur</th>
          <th>Coût estimé</th>
          <th>Description</th>
          <th>Exemple</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Faible</td>
          <td>1</td>
          <td>&lt; 10 k€</td>
          <td>Impact minimal, récupération rapide</td>
          <td>Poste de travail non critique compromis</td>
        </tr>
        <tr>
          <td>Moyen</td>
          <td>2</td>
          <td>10–100 k€</td>
          <td>Impact limité, quelques heures d'interruption</td>
          <td>Serveur de test compromis</td>
        </tr>
        <tr>
          <td>Élevé</td>
          <td>3</td>
          <td>100 k€ – 1 M€</td>
          <td>Impact significatif, plusieurs jours d'interruption</td>
          <td>Fuite de données clients non sensibles</td>
        </tr>
        <tr>
          <td>Très élevé</td>
          <td>4</td>
          <td>1–10 M€</td>
          <td>Impact grave, semaines d'interruption</td>
          <td>Ransomware sur serveurs de production</td>
        </tr>
        <tr>
          <td>Critique</td>
          <td>5</td>
          <td>&gt; 10 M€</td>
          <td>Survie de l'organisation en jeu</td>
          <td>Fuite massive de données médicales</td>
        </tr>
      </tbody>
    </table>
  </div>
  
</div>

<h4 class="subsubsection-title">Types d'impacts à évaluer</h4>

<div class="definition-box">
  <div class="definition-title">Impact financier</div>
  <div class="definition-content content-text">
    <ul>
      <li>Pertes directes (vol, rançon)</li>
      <li>Coûts de remédiation</li>
      <li>Pertes d'exploitation</li>
      <li>Amendes et sanctions</li>
      <li>Frais juridiques</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Impact opérationnel</div>
  <div class="definition-content content-text">
    <ul>
      <li>Durée d'interruption des services</li>
      <li>Perte de productivité</li>
      <li>Impossibilité de livrer les clients</li>
      <li>Dégradation de la qualité de service</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Impact réputationnel</div>
  <div class="definition-content content-text">
    <ul>
      <li>Perte de confiance</li>
      <li>Couverture médiatique</li>
      <li>Perte de clients</li>
      <li>Difficulté à recruter</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Impact juridique</div>
  <div class="definition-content content-text">
    <ul>
      <li>Sanctions RGPD</li>
      <li>Poursuites judiciaires</li>
      <li>Responsabilité pénale</li>
      <li>Non-conformité réglementaire</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Impact humain</div>
  <div class="definition-content content-text">
    <ul>
      <li>Sécurité des personnes</li>
      <li>Stress des employés</li>
      <li>Atteinte à la vie privée</li>
    </ul>
  </div>
</div>

<div class="definition-box">
  <div class="definition-title">Impact stratégique</div>
  <div class="definition-content content-text">
    <ul>
      <li>Perte d'avantage concurrentiel</li>
      <li>Vol de propriété intellectuelle</li>
      <li>Perte de parts de marché</li>
    </ul>
  </div>
</div>

<div class="highlight-fact">💡 Conseil : Pour une évaluation réaliste, prenez l'impact le plus élevé parmi toutes les dimensions.</div>


<h3 class="subsection-title">7.4 Matrice des risques</h3>
<div class="risk-matrix">
  <div class="content-text">
    <p>La matrice des risques permet de visualiser la criticité d'un scénario en croisant sa <strong>probabilité</strong> (vraisemblance) et son <strong>impact</strong> (gravité). Positionnez chaque scénario sur la grille et déduisez le niveau de risque.</p>
  </div>
  <div class="matrix-grid">
    <div class="matrix-header">Probabilité ↓ / Impact →</div>
    <div class="matrix-header">Faible</div>
    <div class="matrix-header">Moyen</div>
    <div class="matrix-header">Élevé</div>
    <div class="matrix-header">Très élevé</div>
    <div class="matrix-header">Critique</div>

    <div class="matrix-label">Faible</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-medium">Moyen</div>

    <div class="matrix-label">Moyen</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-high">Élevé</div>

    <div class="matrix-label">Élevé</div>
    <div class="matrix-cell risk-low">Faible</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-high">Élevé</div>
    <div class="matrix-cell risk-high">Élevé</div>

    <div class="matrix-label">Très élevé</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-high">Élevé</div>
    <div class="matrix-cell risk-high">Élevé</div>
    <div class="matrix-cell risk-critical">Critique</div>

    <div class="matrix-label">Critique</div>
    <div class="matrix-cell risk-medium">Moyen</div>
    <div class="matrix-cell risk-high">Élevé</div>
    <div class="matrix-cell risk-high">Élevé</div>
    <div class="matrix-cell risk-critical">Critique</div>
    <div class="matrix-cell risk-critical">Critique</div>
  </div>
  <div class="content-text"><p><strong>Légende :</strong> Vert = faible, Orange = moyen, Rouge = élevé, Violet = critique.</p></div>
</div>

<h3 class="subsection-title">7.5 Calcul de risque simplifié</h3>

<div class="definition-box">
  <div class="definition-title">Principe</div>
  <div class="definition-content content-text">
    <p>Le calcul repose sur une formule unique et intuitive&nbsp;:</p>
    <pre><code>Risque = Vraisemblance × Impact</code></pre>
    <p>Attribuez une note de 1 à 5 à chaque dimension selon les définitions ci-dessous, puis lisez le niveau de risque via la grille de lecture.</p>
  </div>
  </div>

<div class="concept-section">
  <h4 class="subsubsection-title">Échelles simples (1–5)</h4>
  <div class="content-text">
    <ul>
      <li><strong>Vraisemblance (P)</strong> : 1 Faible, 2 Moyen, 3 Élevé, 4 Très élevé, 5 Critique</li>
      <li><strong>Impact (I)</strong> : 1 Faible, 2 Moyen, 3 Élevé, 4 Très élevé, 5 Critique</li>
    </ul>
  </div>
  </div>

<div class="concept-section">
  <h4 class="subsubsection-title">Lecture du résultat</h4>
  <div class="content-text">
    <ul>
      <li>1–4 → <strong>Faible</strong></li>
      <li>5–9 → <strong>Moyen</strong></li>
      <li>10–16 → <strong>Élevé</strong></li>
      <li>16–25 → <strong>Critique</strong></li>
    </ul>
  </div>
  </div>

<div class="definition-box">
  <div class="definition-title">Exemple rapide</div>
  <div class="definition-content content-text">
    <p><strong>Scénario :</strong> Indisponibilité du site web (attaque DDoS).</p>
    <p><strong>Évaluation :</strong> P = 3 (Élevée), I = 4 (Très élevé).</p>
    <pre><code>Risque = 3 × 4 = 12 → ÉLEVÉ</code></pre>
    <p><strong>Après protections</strong> (anti-DDoS, CDN) : P = 2, I = 3.</p>
    <pre><code>Risque résiduel = 2 × 3 = 6 → MOYEN</code></pre>
  </div>
  </div>



<h3 class="subsection-title">📝 EXERCICE 6 : Calcul de risque pratique</h3>

<div class="exercise-container">
  <div class="exercise-title">Contexte</div>
  <div class="content-text">
    <p>Vous êtes consultant en sécurité pour une entreprise e-commerce de 25 personnes. Le site web génère 2 millions d'euros de chiffre d'affaires annuel. Vous devez évaluer le risque d'une attaque DDoS.</p>
  </div>

  <div class="exercise-title">Informations</div>
  <div class="content-text">
    <ul>
      <li>Le site est hébergé sur un seul serveur web chez un hébergeur mutualisé</li>
      <li>Aucune protection anti-DDoS n'est en place</li>
      <li>L'hébergeur ne propose pas de service anti-DDoS</li>
      <li>Le secteur e-commerce est régulièrement visé par des attaques DDoS</li>
      <li>Une interruption de service coûterait environ 5 000€ par jour de perte de revenus</li>
      <li>En cas d'attaque DDoS, le site pourrait être inaccessible pendant 3 à 5 jours</li>
    </ul>
  </div>

  <div class="exercise-title">Consignes</div>
  <div class="content-text">
    <ol>
      <li>Identifiez la menace, les vulnérabilités et l'actif concerné</li>
      <li>Évaluez la vraisemblance (1-5) et justifiez votre choix</li>
      <li>Évaluez l'impact (1-5) en détaillant les différents types d'impacts (financier, opérationnel, réputationnel)</li>
      <li>Calculez le niveau de risque</li>
      <li>Proposez 3 mesures de sécurité avec leur coût estimé</li>
      <li>Recalculez le risque résiduel après implémentation des mesures</li>
    </ol>
  </div>

  <div class="exercise-title">Format de réponse</div>
  <div class="content-text">
    <p>Suivez le modèle simplifié ci-dessus.</p>
  </div>
</div>

</div>









<div class="concept-section">
  <h2 class="section-title">8. La méthode EBIOS Risk Manager</h2>

  <h3 class="subsection-title">8.1 Qu'est-ce qu'EBIOS Risk Manager ?</h3>
  <div class="definition-box">
    <div class="definition-title">Définition</div>
    <div class="definition-content content-text">
      <p><strong>EBIOS</strong> (Expression des Besoins et Identification des Objectifs de Sécurité) est une <strong>méthode française</strong> de gestion des risques cyber développée par l'<strong>ANSSI</strong> (Agence Nationale de la Sécurité des Systèmes d'Information).</p>
      <p><strong>Objectif :</strong> Identifier, analyser et traiter les risques de manière structurée.</p>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Points clés</div>
    <div class="definition-content content-text">
      <ul>
        <li>Gratuite et accessible sur cyber.gouv.fr</li>
        <li>Approche par scénarios d'attaque réalistes</li>
        <li>Prise en compte de l'écosystème (fournisseurs, partenaires)</li>
        <li>Langage commun entre technique et direction</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">8.2 Les 5 ateliers EBIOS</h3>
  <div class="definition-box">
    <div class="definition-title">Méthode</div>
    <div class="definition-content content-text">
      <p>La méthode se déroule en <strong>5 ateliers successifs</strong>.</p>
    </div>
  </div>

  <h4 class="subsubsection-title">Atelier 1 : Cadrage et socle de sécurité</h4>
  <div class="definition-box">
    <div class="definition-title">Question</div>
    <div class="definition-content content-text"><p>Que doit-on protéger ?</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Actions</div>
    <div class="definition-content content-text">
      <ul>
        <li>Définir le <strong>périmètre</strong> de l'étude</li>
        <li>Identifier les <strong>missions essentielles</strong> de l'organisation</li>
        <li>Lister les <strong>valeurs métier</strong> (données sensibles, services critiques)</li>
        <li>Cartographier l'<strong>écosystème</strong> (partenaires, fournisseurs)</li>
        <li>Identifier les <strong>événements redoutés</strong> (ce qu'on veut éviter)</li>
        <li>Établir le <strong>socle de sécurité</strong> (mesures minimales obligatoires)</li>
      </ul>
    </div>
  </div>
  <div class="highlight-fact"><strong>Exemple :</strong> Hôpital → Mission : soigner les patients → Valeur métier : dossiers patients → Événement redouté : indisponibilité des dossiers pendant une opération</div>

  <h4 class="subsubsection-title">Atelier 2 : Sources de risque</h4>
  <div class="definition-box">
    <div class="definition-title">Question</div>
    <div class="definition-content content-text"><p>Qui pourrait nous attaquer et pourquoi ?</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Actions</div>
    <div class="definition-content content-text">
      <ul>
        <li>Identifier les <strong>sources de risque (SR)</strong> : cybercriminels, APT, concurrents, hacktivistes</li>
        <li>Définir leurs <strong>objectifs visés (OV)</strong> : vol de données, ransomware, sabotage</li>
        <li>Évaluer leurs capacités et motivations</li>
        <li>Prioriser les couples SR/OV pertinents</li>
      </ul>
    </div>
  </div>
  <div class="highlight-fact"><strong>Exemple :</strong> Entreprise pharmaceutique → SR : Groupe APT étatique → OV : Voler les formules du vaccin</div>

  <h4 class="subsubsection-title">Atelier 3 : Scénarios stratégiques</h4>
  <div class="definition-box">
    <div class="definition-title">Question</div>
    <div class="definition-content content-text"><p>Par quels chemins pourraient-ils atteindre nos valeurs métier ?</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Objectif</div>
    <div class="definition-content content-text"><p>Acquérir une <strong>vision claire de l'écosystème</strong> et établir une <strong>cartographie du niveau de dangerosité</strong> induit par la relation avec les <strong>parties prenantes majeures</strong>.</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Actions</div>
    <div class="definition-content content-text">
      <ul>
        <li>Analyser les <strong>parties prenantes (PP)</strong> : fournisseurs, prestataires, partenaires</li>
        <li>Évaluer le <strong>niveau de dangerosité</strong> de chaque PP (exposition, accès, confiance)</li>
        <li>Construire des <strong>scénarios stratégiques</strong> : chemins d'attaque de haut niveau</li>
        <li>Concevoir à l'échelle de l'<strong>écosystème</strong> et des <strong>valeurs métier</strong></li>
        <li>Estimer la <strong>gravité</strong> de chaque scénario (impact sur les valeurs métier)</li>
      </ul>
    </div>
  </div>
  <div class="warning-fact"><strong>Important :</strong> À l'issue de cet atelier, vous pouvez déjà définir des <strong>mesures</strong> sur l'écosystème (clauses contractuelles, audits de sécurité des fournisseurs).</div>
  <div class="highlight-fact"><strong>Exemple :</strong> APT → Prestataire de maintenance (accès VPN) → Vol de données R&D ; Gravité : 4/4 ; Mesure : MFA contractuel + audit annuel</div>

  <h4 class="subsubsection-title">Atelier 4 : Scénarios opérationnels</h4>
  <div class="definition-box">
    <div class="definition-title">Question</div>
    <div class="definition-content content-text"><p>Comment techniquement ces attaques se réaliseraient-elles ?</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Objectif</div>
    <div class="definition-content content-text"><p>Construire des <strong>scénarios techniques</strong> (modes opératoires) pour réaliser les scénarios stratégiques, en se concentrant sur les <strong>biens supports critiques</strong>.</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Actions</div>
    <div class="definition-content content-text">
      <ul>
        <li>Décomposer en <strong>étapes techniques</strong></li>
        <li>Identifier les <strong>modes opératoires</strong> (phishing, CVE, mouvement latéral, exfiltration)</li>
        <li>Repérer les <strong>biens supports</strong> ciblés</li>
        <li>Lister les <strong>vulnérabilités</strong> exploitables</li>
        <li>Estimer la <strong>vraisemblance</strong> (probabilité) de chaque scénario</li>
      </ul>
    </div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Exemple de décomposition</div>
    <div class="definition-content content-text">
      <ol>
        <li><strong>Phishing du prestataire</strong> → Postes de travail → Vulnérabilité : Absence de formation → Vraisemblance : 3/4</li>
        <li><strong>Utilisation VPN volé</strong> → Serveur VPN → Vulnérabilité : Pas de MFA → Vraisemblance : 4/4</li>
        <li><strong>Mouvement latéral</strong> → Active Directory → Vulnérabilité : Réseau non segmenté → Vraisemblance : 3/4</li>
        <li><strong>Exfiltration</strong> → Serveurs de fichiers R&D → Vulnérabilité : Pas de DLP → Vraisemblance : 3/4</li>
      </ol>
    </div>
  </div>

  <h4 class="subsubsection-title">Atelier 5 : Traitement du risque</h4>
  <div class="definition-box">
    <div class="definition-title">Question</div>
    <div class="definition-content content-text"><p>Que fait-on pour réduire les risques ?</p></div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Actions</div>
    <div class="definition-content content-text">
      <ul>
        <li>Définir les <strong>mesures de sécurité</strong> pour chaque scénario opérationnel</li>
        <li>Choisir la <strong>stratégie</strong> : Réduire / Éviter / Transférer / Accepter</li>
        <li><strong>Prioriser</strong> selon coût/efficacité</li>
        <li>Établir un <strong>plan d'action</strong> avec échéancier</li>
        <li>Calculer le <strong>risque résiduel</strong></li>
        <li>Faire <strong>valider</strong> par la direction</li>
      </ul>
    </div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Exemples de mesures</div>
    <div class="definition-content content-text">
      <ul>
        <li>Formation anti‑phishing prestataire</li>
        <li>Déploiement MFA sur VPN</li>
        <li>Segmentation réseau (VLAN R&D isolé)</li>
        <li>Solution DLP + SIEM</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">9. Typologie des mesures de sécurité</h2>

Pour traiter les risques identifiés, on peut implémenter différents types de mesures de sécurité. Il est important de bien les catégoriser pour avoir une approche équilibrée.

<h3 class="subsection-title">9.1 Mesures organisationnelles</h3>

Ce sont les mesures liées aux processus, procédures et organisation humaine.

<h4 class="subsubsection-title">Politiques et documentation</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>PSSI (Politique de Sécurité des Systèmes d'Information) : document cadre définissant les règles de sécurité</li>
      <li>Chartes informatiques : règles d'usage pour les utilisateurs</li>
      <li>Procédures opérationnelles : guides pas-à-pas pour les opérations sensibles</li>
      <li>Documentation de sécurité : architecture, configurations, plans</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Gestion des ressources humaines</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Processus d'embauche : vérification des antécédents, clause de confidentialité</li>
      <li>Sensibilisation et formation : formations régulières, campagnes de communication</li>
      <li>Gestion des habilitations : attribution et revue des droits d'accès</li>
      <li>Processus de départ : révocation des accès, restitution du matériel</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Gestion des incidents</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Playbooks et procédures : réponse aux incidents types</li>
      <li>Équipe de réponse : rôles et responsabilités définis</li>
      <li>Tests et exercices : simulations d'incidents régulières</li>
      <li>Retours d'expérience : analyse post-incident</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Gouvernance</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Comité sécurité : revues régulières, décisions stratégiques</li>
      <li>Gestion des risques : revues périodiques, mise à jour des analyses</li>
      <li>Audits internes et externes : vérifications régulières de la conformité</li>
      <li>Gestion des tiers : contrôle des prestataires et sous-traitants</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">9.2 Mesures techniques (logiques)</h3>

Ce sont les mesures implémentées via des technologies.

<h4 class="subsubsection-title">Authentification et gestion des identités</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Authentification multi-facteurs (MFA) : mot de passe + OTP/app/clé FIDO</li>
      <li>Gestionnaire de mots de passe : génération et stockage sécurisé</li>
      <li>Single Sign-On (SSO) : authentification centralisée</li>
      <li>PAM (Privileged Access Management) : gestion des comptes à privilèges</li>
      <li>Politique de mots de passe : complexité, durée, historique</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Chiffrement et cryptographie</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Chiffrement au repos : disques, bases de données, fichiers</li>
      <li>Chiffrement en transit : TLS/SSL, VPN, SSH</li>
      <li>Signatures numériques : authentification et intégrité</li>
      <li>PKI (Public Key Infrastructure) : gestion des certificats</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Protection réseau</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Pare-feu (Firewall) : filtrage du trafic entrant/sortant</li>
      <li>Segmentation réseau : VLANs, DMZ, zones de confiance</li>
      <li>IDS/IPS : détection et prévention d'intrusions</li>
      <li>VPN : accès distants sécurisés</li>
      <li>Proxy : filtrage web, contrôle d'accès Internet</li>
      <li>Anti-DDoS : protection contre les attaques de déni de service</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Protection des endpoints</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Antivirus/Antimalware : détection et suppression de menaces</li>
      <li>EDR (Endpoint Detection and Response) : détection avancée</li>
      <li>Gestion des correctifs : déploiement automatisé des mises à jour</li>
      <li>Contrôle d'application : whitelisting/blacklisting</li>
      <li>Chiffrement de disque : BitLocker, FileVault</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Sauvegardes et récupération</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Stratégie 3-2-1 : 3 copies, 2 supports différents, 1 hors site</li>
      <li>Sauvegardes incrémentales et différentielles</li>
      <li>Sauvegardes hors ligne (air-gapped)</li>
      <li>Sauvegardes immutables : protection contre la modification</li>
      <li>Tests de restauration : vérification régulière</li>
      <li>PRA/PCA : plans de reprise et de continuité</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Surveillance et détection</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Logs et journalisation : collecte et centralisation</li>
      <li>SIEM (Security Information and Event Management) : corrélation d'événements</li>
      <li>Monitoring réseau : surveillance du trafic</li>
      <li>Alertes : notification en temps réel d'événements suspects</li>
      <li>Threat Intelligence : veille sur les menaces émergentes</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Contrôle d'accès</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>ACL (Access Control Lists) : listes de contrôle d'accès</li>
      <li>RBAC (Role-Based Access Control) : accès basé sur les rôles</li>
      <li>Principe du moindre privilège : droits minimaux nécessaires</li>
      <li>Séparation des environnements : dev/test/production</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">9.3 Mesures physiques</h3>

Ce sont les mesures de protection de l'infrastructure physique.

<h4 class="subsubsection-title">Contrôle d'accès physique</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Badges et cartes d'accès : identification des personnes</li>
      <li>Biométrie : empreintes digitales, reconnaissance faciale</li>
      <li>Sas de sécurité : contrôle d'entrée/sortie</li>
      <li>Agent de sécurité : surveillance humaine</li>
      <li>Registre des visiteurs : traçabilité</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Surveillance</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Vidéosurveillance (CCTV) : caméras de surveillance</li>
      <li>Alarmes : détection d'intrusion</li>
      <li>Rondes de sécurité : vérifications régulières</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Protection environnementale</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Système anti-incendie : détection, extinction automatique</li>
      <li>Contrôle climatique : température, humidité pour les serveurs</li>
      <li>UPS (onduleurs) : protection contre les coupures électriques</li>
      <li>Générateurs : alimentation de secours</li>
      <li>Détection de fuite d'eau : protection contre les dégâts des eaux</li>
    </ul>
  </div>
</div>

<h4 class="subsubsection-title">Protection du matériel</h4>
<div class="definition-box">
  <div class="definition-content content-text">
    <ul>
      <li>Baies verrouillées : armoires sécurisées pour serveurs</li>
      <li>Câbles antivol : protection des équipements mobiles</li>
      <li>Destruction sécurisée : broyage de documents, effacement de disques</li>
      <li>Salles serveurs dédiées : espaces sécurisés</li>
    </ul>
  </div>
</div>

<h3 class="subsection-title">9.4 Comment choisir les bonnes mesures ?</h3>

<div class="definition-box">
  <div class="definition-title">Principes de sélection</div>
  <div class="definition-content content-text">
    <ol>
      <li><strong>Défense en profondeur</strong> : multiplier les couches de sécurité</li>
      <li><strong>Équilibre</strong> : combiner mesures techniques, organisationnelles et physiques</li>
      <li><strong>Proportionnalité</strong> : adapter aux risques et à la criticité</li>
      <li><strong>Coût/Efficacité</strong> : prioriser selon le ROI sécurité</li>
      <li><strong>Facilité d'usage</strong> : ne pas entraver le travail des utilisateurs</li>
    </ol>
  </div>
</div>


