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
</style>

<div class="course-header">
  <h1 class="course-title">🧩 Patrimoine informatique</h1>
  <p class="course-subtitle">BTS SIO • Bloc 1 — Recenser et identifier les ressources numériques</p>
</div>

<div class="concept-section">
  <h2 class="section-title">🎯 Introduction</h2>

  <div class="definition-box">
    <div class="definition-title">🔹 Définition</div>
    <div class="definition-content">
      Le <strong>patrimoine numérique</strong> regroupe toutes les ressources nécessaires au fonctionnement d’un
      système d’information : <em>matérielles</em>, <em>logicielles</em> et <em>immatérielles</em>.
    </div>
  </div>

  <div class="content-text">
    Objectif du chapitre : savoir <strong>recenser</strong> et <strong>identifier</strong> ces ressources pour garantir la
    <strong>cohérence</strong>, la <strong>disponibilité</strong> et la <strong>sécurité</strong> du SI.
  </div>

  <div class="highlight-fact">
    💡 Pourquoi recenser ? Sécurité des accès, maintenance planifiée, conformité des licences, et planification
    des évolutions du SI.
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🗂️ Typologie des ressources</h2>

  <div class="definition-box">
    <div class="definition-title">📦 Ressources matérielles</div>
    <div class="definition-content">
      Postes de travail, serveurs (fichiers, applications, messagerie), périphériques réseau (switch, routeur, firewall),
      imprimantes/scanners, stockages (NAS, disques).
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">💻 Ressources logicielles</div>
    <div class="definition-content">
      Systèmes d’exploitation, applications métiers et bureautiques, logiciels de sécurité (antivirus, monitoring),
      licences et abonnements.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🔑 Ressources immatérielles</div>
    <div class="definition-content">
      Comptes utilisateurs et groupes, droits d’accès, bases de données, documentation technique et procédures internes.
    </div>
  </div>

</div>

<div class="concept-section">
  <h2 class="section-title">📝 Méthodes d’inventaire</h2>

  <div class="definition-box">
    <div class="definition-title">🧭 Recensement manuel</div>
    <div class="definition-content">
      Inspection des équipements, vérification des logiciels installés, fiches individuelles par ressource.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">⚙️ Recensement automatisé</div>
    <div class="definition-content">
      Outils recommandés : <strong>GLPI</strong>, <strong>OCS Inventory</strong>, <strong>Spiceworks</strong>.
      Avantages : inventaire centralisé, suivi des licences, alertes.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🔄 Suivi et mise à jour</div>
    <div class="definition-content">
      Mise à jour après chaque acquisition/suppression, archivage des obsolètes, <strong>responsable du patrimoine</strong>
      désigné (projet AP ou entreprise).
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🗺️ Représentation du patrimoine</h2>

  <div class="definition-box">
    <div class="definition-title">📄 Fiches d’équipement</div>
    <div class="definition-content">
      Tableau avec colonnes : ID, Type, Modèle/Description, Utilisateur, Emplacement, Date, Garantie/Licence,
      Observations, Dépendances.
    </div>
  </div>

  <div class="content-text">
    Exemple de fiche :
  </div>

  <table>
    <thead>
      <tr>
        <th>ID</th><th>Type</th><th>Modèle / Description</th><th>Utilisateur</th><th>Emplacement</th>
        <th>Date</th><th>Garantie / Licence</th><th>Observations</th><th>Dépendances</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>001</td><td>PC</td><td>Dell Latitude 3510</td><td>Dev 1</td><td>Bureau</td>
        <td>01/02/2024</td><td>3 ans</td><td>SSD rapide, chauffe légèrement</td><td>NAS, IDE</td>
      </tr>
    </tbody>
  </table>

  <div class="definition-box">
    <div class="definition-title">📊 Cartographie du SI</div>
    <div class="definition-content">
      Identifiez les ressources principales, leurs <strong>dépendances</strong> et représentez-les (draw.io, Lucidchart…).
      Codes couleurs : bleu = matériel, vert = logiciel, jaune = immatériel.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🗃️ Modèle CMDB</div>
    <div class="definition-content">
      Base centralisée des ressources, mise à jour régulière, colonne « critique » pour l’essentiel.
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🧪 Études de cas</h2>

  <div class="exercise-navigation">
    <div class="exercise-tabs">
      <button class="exercise-tab active" onclick="showExercise(1)">🚀 Cas 1 — Start-up</button>
      <button class="exercise-tab" onclick="showExercise(2)">🏢 Cas 2 — PME</button>
      <button class="exercise-tab" onclick="showExercise(3)">🏙️ Cas 3 — Grande société</button>
    </div>

    <div class="exercise-content-wrapper active">
      <div class="scenario-box"><strong>Contexte :</strong> Start-up de 4 employés, logiciel interne de gestion client.</div>
      <ul>
        <li>Ressources : PC portables, NAS Synology DS220+, routeur/switch, VS Code & GitHub, Sage Start, imprimante.</li>
      </ul>
      <ol>
        <li>Créer un <strong>tableau d’inventaire</strong>.</li>
        <li>Identifier les <strong>ressources critiques</strong>.</li>
        <li>Proposer une <strong>organisation des sauvegardes</strong>.</li>
        <li>Identifier les <strong>dépendances</strong>.</li>
        <li>Suggérer une <strong>amélioration</strong> (maintenance/sécurité).</li>
      </ol>
    </div>

    <div class="exercise-content-wrapper">
      <div class="scenario-box"><strong>Contexte :</strong> PME de 15 employés, développement d’apps mobiles.</div>
      <ul>
        <li>Ressources : 10 PC fixes dev, 5 portables managers, DS920+, MySQL, réseau (switches+firewall), IDE/design, comptes/droits.</li>
      </ul>
      <ol>
        <li>Inventaire complet.</li>
        <li>Ressources critiques (dév/sécurité).</li>
        <li>Dépendances et <strong>cartographie</strong>.</li>
        <li>Améliorations maintenance.</li>
        <li>Risques potentiels (panne, licence…).</li>
      </ol>
    </div>

    <div class="exercise-content-wrapper">
      <div class="scenario-box"><strong>Contexte :</strong> 50 employés, projets web/mobiles simultanés.</div>
      <ul>
        <li>Ressources : 35 dev (HP G6), 15 chefs de projet/QA (Dell XPS, VPN), serveurs (DS1821+, Exchange, BDD), réseau Cisco, IDE/bureautique/design, AD/LDAP, documentation.</li>
      </ul>
      <ol>
        <li>Inventaire complet.</li>
        <li>Ressources critiques et <strong>sécurité</strong>.</li>
        <li>Dépendances, <strong>cartographie du SI</strong>.</li>
        <li>Améliorations maintenance/sécurité.</li>
        <li>Risques de perte/panne & solutions.</li>
      </ol>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">📝 TP — Inventaire du projet d’AP</h2>
  <div class="exercise-container">
    <div class="exercise-title">Objectif</div>
    <div class="content-text">Créer un inventaire complet des ressources nécessaires à votre projet d’AP.</div>

    <div class="exercise-title">Consignes</div>
    <ul class="content-text">
      <li>Lister toutes les ressources matérielles et logicielles.</li>
      <li>Identifier les ressources <strong>critiques</strong>.</li>
      <li>Décrire les <strong>dépendances</strong>.</li>
      <li>Proposer une <strong>organisation des sauvegardes</strong>.</li>
      <li>Suggérer des <strong>améliorations</strong> (maintenance/sécurité).</li>
    </ul>
  </div>
</div>

<script>
function showExercise(n) {
  const tabs = document.querySelectorAll('.exercise-tab');
  const contents = document.querySelectorAll('.exercise-content-wrapper');
  tabs.forEach((t, i) => t.classList.toggle('active', i === n - 1));
  contents.forEach((c, i) => c.classList.toggle('active', i === n - 1));
}
document.addEventListener('DOMContentLoaded', () => showExercise(1));
</script>