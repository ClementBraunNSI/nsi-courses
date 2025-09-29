<style>
/* Styles modernes pour le cours Méthodes Agiles */
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
    color: #27ae60;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-left: 5px solid #27ae60;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #27ae60;
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
    color: #27ae60;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
    color: var(--md-default-fg-color);
    text-align: center;
    line-height: 1.5;
}

.methodology-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.methodology-card {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 20px;
    padding: 2rem;
    border: 2px solid rgba(46, 204, 113, 0.2);
    transition: all 0.3s ease;
}

.methodology-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(46, 204, 113, 0.2);
}

.methodology-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #27ae60;
    margin-bottom: 1rem;
    text-align: center;
}

.methodology-description {
    color: var(--md-default-fg-color);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.methodology-features {
    list-style: none;
    padding: 0;
}

.methodology-features li {
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(46, 204, 113, 0.1);
}

.methodology-features li:before {
    content: "✅ ";
    color: #27ae60;
    font-weight: bold;
}

.sprint-timeline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    overflow-x: auto;
}

.sprint-phase {
    text-align: center;
    flex: 1;
    min-width: 150px;
}

.sprint-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.sprint-name {
    font-weight: 600;
    color: #27ae60;
    margin-bottom: 0.5rem;
}

.sprint-duration {
    font-size: 0.9rem;
    color: #7f8c8d;
}

.kanban-board {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
    background: rgba(46, 204, 113, 0.05);
    padding: 2rem;
    border-radius: 15px;
}

.kanban-column {
    background: white;
    border-radius: 10px;
    padding: 1rem;
    min-height: 200px;
    border: 2px solid rgba(46, 204, 113, 0.2);
}

.kanban-header {
    font-weight: 600;
    color: #27ae60;
    text-align: center;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(46, 204, 113, 0.2);
}

.kanban-card {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 0.5rem;
    border-left: 3px solid #27ae60;
    font-size: 0.9rem;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.comparison-table th {
    background: linear-gradient(135deg, #27ae60, #2ecc71);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.comparison-table td {
    padding: 1rem;
    text-align: center;
    border-bottom: 1px solid rgba(46, 204, 113, 0.1);
}

.comparison-table tr:nth-child(even) {
    background: rgba(46, 204, 113, 0.05);
}

.comparison-table tr:hover {
    background: rgba(46, 204, 113, 0.1);
}

.ap-project-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(46, 204, 113, 0.1));
    border: 2px solid rgba(46, 204, 113, 0.3);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
}

.ap-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #27ae60;
    margin-bottom: 1rem;
    text-align: center;
}

.ap-content {
    color: var(--md-default-fg-color);
    line-height: 1.6;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.15), rgba(39, 174, 96, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    margin: 2rem 0;
    border-left: 5px solid #27ae60;
    font-weight: 500;
}

.content-text {
    color: var(--md-default-fg-color);
    line-height: 1.7;
    margin: 1.5rem 0;
    font-size: 1.1rem;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid, .methodology-grid {
        grid-template-columns: 1fr;
    }
    
    .kanban-board {
        grid-template-columns: 1fr;
    }
    
    .sprint-timeline {
        flex-direction: column;
        gap: 1rem;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🚀 Méthodes Agiles Avancées</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Gestion de projet informatique</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 L'Agilité dans les Projets Informatiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌟 Manifeste Agile</div>
        <div class="definition-content">
            Les méthodes agiles privilégient <strong>les individus et leurs interactions</strong> plutôt que les processus et les outils, <strong>des logiciels opérationnels</strong> plutôt qu'une documentation exhaustive, <strong>la collaboration avec les clients</strong> plutôt que la négociation contractuelle, et <strong>l'adaptation au changement</strong> plutôt que le suivi d'un plan.
        </div>
    </div>
    
    <div class="content-text">
        Dans le développement de projets informatiques, l'agilité permet de gérer efficacement l'incertitude, de livrer de la valeur rapidement et de s'adapter aux retours des utilisateurs et des parties prenantes.
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">👥</div>
            <div class="concept-name">Collaboration</div>
            <div class="concept-description">
                Communication constante entre l'équipe, les utilisateurs et les parties prenantes du projet.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Itération</div>
            <div class="concept-description">
                Développement par cycles courts avec livraisons fréquentes et amélioration continue.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📈</div>
            <div class="concept-name">Valeur</div>
            <div class="concept-description">
                Focus sur les fonctionnalités qui apportent le plus de valeur aux utilisateurs finaux.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Adaptation</div>
            <div class="concept-description">
                Capacité à réagir rapidement aux changements et aux retours d'expérience.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🏃‍♂️ Scrum : Framework Agile</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏆 Scrum en Action</div>
        <div class="definition-content">
            Scrum est un framework agile structuré autour de <strong>sprints</strong> (itérations de 1-4 semaines), d'<strong>événements</strong> (réunions rituelles) et d'<strong>artefacts</strong> (documents de travail). Parfait pour organiser des projets informatiques avec des livrables réguliers.
        </div>
    </div>
    
    <div class="methodology-grid">
        <div class="methodology-card">
            <div class="methodology-title">👑 Product Owner</div>
            <div class="methodology-description">
                En entreprise, c'est souvent le responsable produit ou le représentant client qui définit les besoins.
            </div>
            <ul class="methodology-features">
                <li>Définit les user stories</li>
                <li>Priorise le backlog produit</li>
                <li>Valide les fonctionnalités</li>
                <li>Interface avec les utilisateurs</li>
            </ul>
        </div>
        
        <div class="methodology-card">
            <div class="methodology-title">🎯 Scrum Master</div>
            <div class="methodology-description">
                Facilitateur du processus Scrum qui aide l'équipe à éliminer les obstacles et à s'améliorer.
            </div>
            <ul class="methodology-features">
                <li>Anime les cérémonies Scrum</li>
                <li>Résout les blocages</li>
                <li>Protège l'équipe des perturbations</li>
                <li>Coach l'équipe sur Scrum</li>
            </ul>
        </div>
        
        <div class="methodology-card">
            <div class="methodology-title">💻 Équipe de Développement</div>
            <div class="methodology-description">
                Équipe pluridisciplinaire (développeurs, testeurs, designers) qui réalise concrètement le produit.
            </div>
            <ul class="methodology-features">
                <li>Auto-organisée et pluridisciplinaire</li>
                <li>Estime et réalise les user stories</li>
                <li>Livre un incrément fonctionnel</li>
                <li>Améliore continuellement ses pratiques</li>
            </ul>
        </div>
    </div>
    
    <div class="sprint-timeline">
        <div class="sprint-phase">
            <div class="sprint-icon">📋</div>
            <div class="sprint-name">Sprint Planning</div>
            <div class="sprint-duration">4h pour 2 semaines</div>
        </div>
        <div class="sprint-phase">
            <div class="sprint-icon">🔄</div>
            <div class="sprint-name">Daily Scrum</div>
            <div class="sprint-duration">15 min/jour</div>
        </div>
        <div class="sprint-phase">
            <div class="sprint-icon">🎯</div>
            <div class="sprint-name">Sprint Review</div>
            <div class="sprint-duration">2h pour 2 semaines</div>
        </div>
        <div class="sprint-phase">
            <div class="sprint-icon">🔍</div>
            <div class="sprint-name">Retrospective</div>
            <div class="sprint-duration">1h30 pour 2 semaines</div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📋 Kanban : Visualiser le Flux</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎨 Tableau Kanban</div>
        <div class="definition-content">
            Kanban visualise le flux de travail et limite le travail en cours (WIP). Idéal pour gérer les tâches de maintenance, les bugs ou les projets avec des priorités changeantes.
        </div>
    </div>
    
    <div class="kanban-board">
        <div class="kanban-column">
            <div class="kanban-header">📝 À Faire</div>
            <div class="kanban-card">Créer la base de données</div>
            <div class="kanban-card">Concevoir l'interface utilisateur</div>
            <div class="kanban-card">Rédiger les tests unitaires</div>
        </div>
        <div class="kanban-column">
            <div class="kanban-header">🔄 En Cours</div>
            <div class="kanban-card">Développer l'API REST</div>
            <div class="kanban-card">Intégrer l'authentification</div>
        </div>
        <div class="kanban-column">
            <div class="kanban-header">✅ Terminé</div>
            <div class="kanban-card">Analyser les besoins</div>
            <div class="kanban-card">Configurer l'environnement</div>
            <div class="kanban-card">Créer le repository Git</div>
        </div>
        <div class="kanban-column">
            <div class="kanban-header">🚀 Déployé</div>
            <div class="kanban-card">Page de connexion</div>
            <div class="kanban-card">Module de gestion utilisateurs</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Limite WIP :</strong> Ne travaillez que sur 2-3 tâches maximum par personne pour éviter la dispersion et améliorer la qualité.
    </div>
</div>

<div class="concept-section">
  <h2 class="section-title">📝 User Stories</h2>
  
  <div class="definition-box">
    <div class="definition-title">📌 Définition</div>
    <div class="definition-content">
      Une <strong>user story</strong> décrit une fonctionnalité du point de vue de l’utilisateur et la valeur qu’elle apporte.
    </div>
  </div>

  <div class="content-text">
    🔹 <em>Template :</em> <code>En tant que &lt;rôle&gt;, je veux &lt;action&gt; afin de &lt;bénéfice&gt;.</code><br>
    🔹 Chaque story doit avoir des <strong>critères d’acceptation</strong> : conditions précises permettant de valider si la fonctionnalité est terminée.<br>
    🔹 Bonnes pratiques : utiliser le modèle <strong>INVEST</strong> (Indépendante, Négociable, Valorisante, Estimable, Petite, Testable).
  </div>

  <div class="highlight-fact">
    💡 Exemple : « En tant qu’étudiant, je veux ajouter une tâche avec une date limite afin d’organiser mes révisions. »<br>
    <strong>Critères d’acceptation :</strong> titre obligatoire, date sélectionnable, tâche visible dans la liste triée.
  </div>
</div>


<div class="concept-section">
  <h2 class="section-title">📂 Les Artefacts Scrum</h2>

  <div class="definition-box">
    <div class="definition-title">📋 Product Backlog</div>
    <div class="definition-content">
      Liste priorisée de toutes les fonctionnalités, améliorations et corrections. Chaque item contient : titre, description (user story), critères d’acceptation, estimation et priorité.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🗂️ Sprint Backlog</div>
    <div class="definition-content">
      Sous-ensemble du product backlog sélectionné pour un sprint, découpé en tâches techniques par l’équipe de développement.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🚀 Incrément</div>
    <div class="definition-content">
      Ensemble des éléments « Done » à la fin d’un sprint. L’incrément doit être <strong>potentiellement livrable</strong> au client.
    </div>
  </div>
</div>


<div class="concept-section">
  <h2 class="section-title">✅ Definition of Ready & Definition of Done</h2>

  <div class="definition-box">
    <div class="definition-title">📥 Definition of Ready (DoR)</div>
    <div class="definition-content">
      Une user story est prête à entrer en sprint si :  
      <ul>
        <li>Description claire et complète</li>
        <li>Critères d’acceptation définis</li>
        <li>Estimation réalisée</li>
        <li>Dépendances identifiées</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">📤 Definition of Done (DoD)</div>
    <div class="definition-content">
      Une user story est considérée comme terminée si :  
      <ul>
        <li>Code compilé et testé</li>
        <li>Tests unitaires écrits et passés</li>
        <li>Revue de code effectuée</li>
        <li>Documentation minimale ajoutée</li>
        <li>Livrable déployé en environnement de test</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 SAFe : Scaled Agile pour Grandes Organisations</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏢 Scaled Agile Framework</div>
        <div class="definition-content">
            SAFe (Scaled Agile Framework) étend l'agilité aux grandes organisations avec plusieurs équipes. Comprendre SAFe est essentiel pour travailler dans des environnements professionnels complexes.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Program Increment (PI)</div>
            <div class="concept-description">
                Cycle de 8-12 semaines synchronisant plusieurs équipes Scrum sur des objectifs communs.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🚂</div>
            <div class="concept-name">Agile Release Train</div>
            <div class="concept-description">
                Ensemble d'équipes agiles travaillant ensemble sur une solution commune avec un rythme partagé.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">PI Planning</div>
            <div class="concept-description">
                Événement de planification de 2 jours réunissant toutes les équipes pour aligner les objectifs.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Lean Portfolio</div>
            <div class="concept-description">
                Gestion stratégique des investissements et allocation des ressources selon les principes Lean.
            </div>
        </div>
    </div>
</div>