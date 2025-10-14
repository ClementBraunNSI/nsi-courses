<style>
/* Styles modernes pour le cours ITIL */
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
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #3498db;
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
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.warning-box {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.success-box {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.method-card {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(52, 152, 219, 0.2);
    transition: all 0.3s ease;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.method-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    text-align: center;
    line-height: 1.5;
}

.example-box {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(46, 204, 113, 0.2);
}

.example-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #27ae60;
    margin-bottom: 1rem;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.comparison-table th,
.comparison-table td {
    padding: 0.8rem;
    text-align: left;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.comparison-table th {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    font-weight: 600;
}

.comparison-table tr:hover {
    background: rgba(52, 152, 219, 0.1);
}

.step-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.step-card {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    border-left: 4px solid #3498db;
    transition: all 0.3s ease;
}

.step-card:hover {
    transform: translateX(5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.step-number {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-bottom: 1rem;
}

.step-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.step-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.exercise-section {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(52, 152, 219, 0.05));
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(155, 89, 182, 0.2);
}

.exercise-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #9b59b6;
    margin-bottom: 1rem;
}

.exercise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.exercise-card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
}

.exercise-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.exercise-number {
    background: linear-gradient(135deg, #9b59b6, #8e44ad);
    color: white;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

.exercise-card-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
}

.exercise-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
    overflow: hidden;
    font-size: 0.9rem;
}

.exercise-table th,
.exercise-table td {
    padding: 0.6rem;
    text-align: left;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.exercise-table th {
    background: linear-gradient(135deg, #9b59b6, #8e44ad);
    color: white;
    font-weight: 600;
}

.exercise-table tr:hover {
    background: rgba(155, 89, 182, 0.1);
}

/* Styles pour la navigation des exercices */
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

.exercise-tabs::-webkit-scrollbar {
    height: 6px;
}

.exercise-tabs::-webkit-scrollbar-track {
    background: #ecf0f1;
    border-radius: 3px;
}

.exercise-tabs::-webkit-scrollbar-thumb {
    background: #bdc3c7;
    border-radius: 3px;
}

.exercise-tabs::-webkit-scrollbar-thumb:hover {
    background: #95a5a6;
}

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
    min-width: 140px;
    font-size: 0.9rem;
    border-radius: 8px 8px 0 0;
}

.exercise-tab:hover {
    color: #3498db;
    background: rgba(52, 152, 219, 0.05);
}

.exercise-tab.active {
    color: #2980b9;
    border-bottom-color: #3498db;
    background: rgba(52, 152, 219, 0.1);
}

.exercise-content-wrapper {
    display: none;
}

.exercise-content-wrapper.active {
    display: block;
    animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.exercise-summary {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: #2c3e50;
}

/* Styles pour les sous-exercices */
.sub-exercise-navigation {
    background: rgba(52, 152, 219, 0.05);
    border-radius: 10px;
    padding: 0.5rem;
    margin: 1rem 0;
    border: 1px solid rgba(52, 152, 219, 0.1);
}

.sub-exercise-tabs {
    display: flex;
    gap: 0.3rem;
    overflow-x: auto;
    padding: 0.3rem;
    scrollbar-width: thin;
    scrollbar-color: #bdc3c7 #ecf0f1;
}

.sub-exercise-tabs::-webkit-scrollbar {
    height: 4px;
}

.sub-exercise-tabs::-webkit-scrollbar-track {
    background: #ecf0f1;
    border-radius: 2px;
}

.sub-exercise-tabs::-webkit-scrollbar-thumb {
    background: #bdc3c7;
    border-radius: 2px;
}

.sub-exercise-tab {
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(52, 152, 219, 0.2);
    padding: 0.5rem 0.8rem;
    cursor: pointer;
    font-weight: 500;
    color: #5a6c7d;
    border-radius: 6px;
    transition: all 0.3s ease;
    white-space: nowrap;
    flex-shrink: 0;
    min-width: 80px;
    font-size: 0.8rem;
    text-align: center;
}

.sub-exercise-tab:hover {
    color: #3498db;
    background: rgba(52, 152, 219, 0.1);
    border-color: #3498db;
}

.sub-exercise-tab.active {
    color: white;
    background: linear-gradient(135deg, #3498db, #2980b9);
    border-color: #2980b9;
    box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
}

.sub-exercise-content {
    display: none;
    padding: 1rem 0;
}

.sub-exercise-content.active {
    display: block;
    animation: fadeInSub 0.3s ease-in-out;
}

@keyframes fadeInSub {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .step-grid {
        grid-template-columns: 1fr;
    }
    
    .exercise-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
    
    .comparison-table,
    .exercise-table {
        font-size: 0.8rem;
    }
    
    .exercise-tabs {
        flex-direction: column;
        gap: 0.3rem;
    }
    
    .exercise-tab {
        min-width: auto;
        text-align: center;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🧭 Introduction à ITIL</h1>
    <p class="course-subtitle">Gestion des services informatiques et bonnes pratiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 De la gestion de projet à la gestion de services</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Contexte</div>
        <div class="definition-content">
            Une fois qu'un <strong>projet informatique est terminé</strong>, le travail ne s'arrête pas. Il faut <strong>maintenir</strong> le service livré, <strong>corriger les pannes</strong>, <strong>faire les mises à jour</strong> et <strong>répondre aux utilisateurs</strong>.
        </div>
    </div>
    
    <div class="example-box">
        <div class="example-title">🧠 Exemple concret</div>
        <p>Après le développement d'un site web, il faut ensuite surveiller le serveur, corriger les bugs, gérer les utilisateurs et appliquer les mises à jour de sécurité.</p>
    </div>
    
    <div class="highlight-fact">
        Cette phase s'appelle <strong>la gestion des services informatiques</strong>. C'est là qu'intervient <strong>ITIL</strong> : une collection de <strong>bonnes pratiques</strong> utilisées dans le monde entier pour <strong>organiser et améliorer les services IT</strong>.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📚 Qu'est-ce qu'ITIL ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔹 Définition</div>
        <div class="definition-content">
            <strong>ITIL</strong> (<em>Information Technology Infrastructure Library</em>) est un <strong>ensemble de bonnes pratiques (dérivés de la norme BS15000 ou ISO/CEI 20000 pour les systèmes informatiques)</strong> pour la <strong>gestion des services informatiques</strong>.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Continuité des services</div>
            <div class="concept-description">
                Assurer que les services informatiques fonctionnent de manière continue et fiable.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Réaction rapide</div>
            <div class="concept-description">
                Réagir rapidement en cas d'incident pour minimiser l'impact sur les utilisateurs.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📈</div>
            <div class="concept-name">Amélioration continue</div>
            <div class="concept-description">
                Améliorer la qualité de service sur la durée grâce à des processus optimisés.
            </div>
        </div>
    </div>
    
    <div class="success-box">
        💡 ITIL ne dit pas <em>comment</em> faire techniquement, mais <em>quoi mettre en place</em> pour qu'un service fonctionne bien au quotidien.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚖️ Gestion de projet vs Gestion de service</h2>
    
    <div class="definition-box">
        <div class="definition-title">🤝 Complémentarité</div>
        <div class="definition-content">
            Ces deux approches <strong>ne s'opposent pas</strong>, elles <strong>se complètent</strong>.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🚀</div>
            <div class="concept-name">Gestion de projet</div>
            <div class="concept-description">
                Sert à <strong>concevoir</strong> et <strong>livrer</strong> un nouveau service (ex : créer une application, un site, un outil).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔧</div>
            <div class="concept-name">Gestion de service</div>
            <div class="concept-description">
                Sert à <strong>faire vivre</strong> ce service sur la durée (maintenance, support, mises à jour…).
            </div>
        </div>
    </div>
    
    <div class="example-box">
        <div class="example-title">🧩 Exemple concret</div>
        <p>Une équipe développe une application mobile pendant 6 mois → c'est la <strong>gestion de projet</strong>.</p>
        <p>Une fois publiée sur le Play Store, il faut corriger les bugs, répondre aux utilisateurs et déployer des mises à jour → c'est la <strong>gestion de service</strong>.</p>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th><strong>Critère</strong></th>
                <th><strong>Gestion de projet</strong></th>
                <th><strong>Gestion de service (ITIL)</strong></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>🎯 <strong>Objectif</strong></td>
                <td>Créer un nouveau produit ou service</td>
                <td>Faire fonctionner et améliorer un service existant</td>
            </tr>
            <tr>
                <td>⏱️ <strong>Durée</strong></td>
                <td>Limitée (le projet a un début et une fin)</td>
                <td>Continue (le service reste actif en permanence)</td>
            </tr>
            <tr>
                <td>🧑‍💻 <strong>Acteurs principaux</strong></td>
                <td>Chef de projet, développeurs, testeurs</td>
                <td>Techniciens, administrateurs, support utilisateur</td>
            </tr>
            <tr>
                <td>🛠️ <strong>Type d'activité</strong></td>
                <td>Conception, développement, livraison</td>
                <td>Maintenance, support, mise à jour, amélioration</td>
            </tr>
            <tr>
                <td>🗓️ <strong>Période d'action</strong></td>
                <td>Avant la mise en service</td>
                <td>Après la mise en service</td>
            </tr>
            <tr>
                <td>💡 <strong>Exemple</strong></td>
                <td>Développer un site e-commerce</td>
                <td>Corriger les pannes du site, le mettre à jour</td>
            </tr>
            <tr>
                <td>⚙️ <strong>Méthodes associées</strong></td>
                <td>Gantt, PERT, Agile, Scrum</td>
                <td>ITIL, supervision, gestion d'incidents</td>
            </tr>
        </tbody>
    </table>
    
    <div class="highlight-fact">
        🧠 <strong>À retenir :</strong> La <strong>gestion de projet</strong> crée le service. <strong>ITIL</strong> fait vivre le service dans le temps.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🏗️ Les quatre dimensions d'ITIL</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏛️ Les quatre piliers</div>
        <div class="definition-content">
            ITIL considère qu'un bon service repose sur <strong>quatre piliers</strong>. Si l'un d'eux est négligé, le service devient instable.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🧑‍💼</div>
            <div class="concept-name">Organisation & personnes</div>
            <div class="concept-description">
                Les rôles, compétences et communication au sein de l'équipe. <br>
                <em>Ex : Support technique, helpdesk, chef de projet, responsables réseau.</em>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💻</div>
            <div class="concept-name">Information & technologie</div>
            <div class="concept-description">
                Les outils, logiciels et infrastructures utilisés. <br>
                <em>Ex : Serveurs, bases de données, outils de ticketing (ex : GLPI).</em>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🤝</div>
            <div class="concept-name">Partenaires & fournisseurs</div>
            <div class="concept-description">
                Les prestataires et contrats externes. <br>
                <em>Ex : Hébergeur, éditeur de logiciel, sous-traitants.</em>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Flux de valeur & processus</div>
            <div class="concept-description">
                Les méthodes et étapes de travail pour délivrer le service. <br>
                <em>Ex : Procédure de gestion des incidents, sauvegardes planifiées.</em>
            </div>
        </div>
    </div>
    
    <div class="warning-box">
        💬 <strong>Exemple :</strong> Si le serveur du lycée tombe (technologie), que personne ne sait le réparer (organisation), et que le contrat d'hébergement a expiré (fournisseur), le service est à l'arrêt. Les quatre dimensions doivent donc être équilibrées.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚙️ Les pratiques essentielles d'ITIL</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Trois pratiques clés</div>
        <div class="definition-content">
            ITIL contient de nombreuses pratiques (ou "processus"), mais voici les <strong>trois plus importantes</strong> à connaître.
        </div>
    </div>
    
    <div class="step-grid">
        <div class="step-card">
            <div class="step-number">⚡</div>
            <div class="step-title">Gestion des incidents</div>
            <div class="step-description">
                <strong>Objectif :</strong> rétablir le service le plus vite possible.<br><br>
                <strong>Exemple :</strong> L'application du client ne s'ouvre plus → on redémarre le serveur pour la remettre en ligne.<br><br>
                L'objectif n'est <strong>pas de chercher la cause profonde</strong>, mais <strong>d'aider l'utilisateur rapidement</strong>.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">🧠</div>
            <div class="step-title">Gestion des problèmes</div>
            <div class="step-description">
                <strong>Objectif :</strong> identifier la cause profonde des incidents récurrents.<br><br>
                <strong>Exemple :</strong> Le serveur tombe souvent → on découvre un bug dans la base de données. Une fois corrigé, les incidents disparaissent.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">🔁</div>
            <div class="step-title">Gestion des changements</div>
            <div class="step-description">
                <strong>Objectif :</strong> modifier un service sans créer de nouvelles pannes.<br><br>
                <strong>Exemple :</strong> Installer une nouvelle version du module de paiement → on la teste avant la mise en production.<br><br>
                Chaque changement doit être <strong>planifié, testé et validé</strong> avant déploiement.
            </div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-title">📋 Termes clés - Incidents</div>
            <div class="method-description">
                <strong>Incident :</strong> Toute interruption ou dégradation du service.<br>
                <strong>Solution temporaire :</strong> Action rapide pour rétablir le service.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">🔍 Termes clés - Problèmes</div>
            <div class="method-description">
                <strong>Problème :</strong> Cause d'un ou plusieurs incidents.<br>
                <strong>Solution définitive :</strong> Action qui élimine la cause du problème.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">🔄 Termes clés - Changements</div>
            <div class="method-description">
                <strong>Changement :</strong> Modification d'un service (mise à jour, ajout, suppression).<br>
                <strong>Validation :</strong> Étape de test et d'approbation avant déploiement.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Différence entre incidents et problèmes</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th><strong>Aspect</strong></th>
                <th><strong>Gestion des incidents</strong></th>
                <th><strong>Gestion des problèmes</strong></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>🎯 <strong>Objectif</strong></td>
                <td>Rétablir le service au plus vite</td>
                <td>Trouver et éliminer la cause racine</td>
            </tr>
            <tr>
                <td>⏱️ <strong>Urgence</strong></td>
                <td>Élevée (l'utilisateur est bloqué)</td>
                <td>Moindre (on agit après coup)</td>
            </tr>
            <tr>
                <td>🧰 <strong>Type d'action</strong></td>
                <td>Correctif immédiat (solution temporaire)</td>
                <td>Préventif (solution définitive)</td>
            </tr>
            <tr>
                <td>💬 <strong>Exemple 1</strong></td>
                <td>Le Wi-Fi du lycée ne marche plus → on redémarre la borne</td>
                <td>On découvre un bug dans le firmware → mise à jour</td>
            </tr>
            <tr>
                <td>💬 <strong>Exemple 2</strong></td>
                <td>Le site web est planté → redémarrage du serveur</td>
                <td>La base de données est mal configurée → optimisation SQL</td>
            </tr>
            <tr>
                <td>💬 <strong>Exemple 3</strong></td>
                <td>L'imprimante ne répond plus → on réinstalle le pilote</td>
                <td>Le serveur d'impression est instable → mise à jour du serveur</td>
            </tr>
        </tbody>
    </table>
    
    <div class="highlight-fact">
        🧠 <strong>À retenir :</strong> L'<strong>incident</strong> vise la <strong>rapidité</strong> : on répare vite. Le <strong>problème</strong> vise la <strong>durabilité</strong> : on empêche que ça revienne.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💼 Exemple de mise en situation</h2>
    
    <div class="example-box">
        <div class="example-title">🏢 Cas pratique d'entreprise</div>
        <p>Une entreprise héberge une application utilisée par ses clients. Un matin, les utilisateurs signalent qu'ils ne peuvent plus se connecter.</p>
        
        <div class="step-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-title">Incident</div>
                <div class="step-description">
                    Redémarrage du serveur pour rétablir le service rapidement.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-title">Problème</div>
                <div class="step-description">
                    Analyse du bug dans la base de données pour identifier la cause racine.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-title">Changement</div>
                <div class="step-description">
                    Déploiement d'un correctif testé et validé pour éviter la récurrence.
                </div>
            </div>
        </div>
    </div>
</div>

<div class="exercise-section">
    <h2 class="section-title">📝 Travaux Dirigés</h2>
    
    <div class="exercise-navigation">
        <div class="exercise-tabs">
            <button class="exercise-tab active" onclick="showExercise(1)">Exercice 1</button>
            <button class="exercise-tab" onclick="showExercise(2)">Exercice 2</button>
            <button class="exercise-tab" onclick="showExercise(3)">Exercice 3</button>
            <button class="exercise-tab" onclick="showExercise(4)">Exercice 4</button>
        </div>
        
        <!-- Exercice 1 -->
        <div id="exercise1" class="exercise-content-wrapper active">
            <div class="exercise-summary">
                <strong>Objectif :</strong> Distinguer les incidents des problèmes dans le contexte ITIL
            </div>
            
            <h3>💡 Activité d'application – Incidents et problèmes</h3>
            <p>Avant de découvrir les processus ITIL, voyons si vous savez faire la différence entre un <strong>incident</strong> (panne immédiate) et un <strong>problème</strong> (cause d'incidents répétés).</p>
            
            <!-- Navigation des sous-exercices -->
            <div class="sub-exercise-navigation">
                <div class="sub-exercise-tabs">
                    <button class="sub-exercise-tab active" onclick="showSubExercise(1, 1)">1.1</button>
                    <button class="sub-exercise-tab" onclick="showSubExercise(1, 2)">1.2</button>
                    <button class="sub-exercise-tab" onclick="showSubExercise(1, 3)">1.3</button>
                </div>
            </div>
            
            <!-- Sous-exercice 1.1 -->
            <div id="sub-exercise-1-1" class="sub-exercise-content active">
                <div class="example-box">
                    <div class="example-title">✏️ Exercice 1.1 – Incident ou problème ?</div>
                    <p>Indiquer pour chaque situation s'il s'agit d'un <strong>incident</strong> ou d'un <strong>problème</strong>.</p>
                    
                    <table class="exercise-table">
                        <thead>
                            <tr>
                                <th>Situation</th>
                                <th>Type</th>
                                <th>Justification</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>L'imprimante du service comptabilité ne fonctionne plus</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Tous les lundis matin, le serveur web est lent</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Un utilisateur ne peut plus accéder à son dossier personnel</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Analyse de la cause des pannes récurrentes du réseau</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- Sous-exercice 1.2 -->
            <div id="sub-exercise-1-2" class="sub-exercise-content">
                <div class="example-box">
                    <div class="example-title">✏️ Exercice 1.2 – Priorisation des incidents</div>
                    <p>Classer ces incidents par ordre de priorité (1 = le plus urgent, 4 = le moins urgent).</p>
                    
                    <table class="exercise-table">
                        <thead>
                            <tr>
                                <th>Incident</th>
                                <th>Impact</th>
                                <th>Urgence</th>
                                <th>Priorité</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Serveur de messagerie en panne (toute l'entreprise)</td>
                                <td>Élevé</td>
                                <td>Élevée</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Imprimante d'un bureau en panne</td>
                                <td>Faible</td>
                                <td>Faible</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Site web client inaccessible</td>
                                <td>Élevé</td>
                                <td>Élevée</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Logiciel de comptabilité lent (fin de mois)</td>
                                <td>Moyen</td>
                                <td>Élevée</td>
                                <td>_______</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- Sous-exercice 1.3 -->
            <div id="sub-exercise-1-3" class="sub-exercise-content">
                <div class="example-box">
                    <div class="example-title">✏️ Exercice 1.3 – Escalade des incidents</div>
                    <p>Pour chaque incident, indiquer le niveau d'escalade approprié.</p>
                    
                    <div class="highlight-fact">
                        <strong>Niveaux d'escalade :</strong><br>
                        • <strong>Niveau 1</strong> : Support utilisateur (helpdesk)<br>
                        • <strong>Niveau 2</strong> : Techniciens spécialisés<br>
                        • <strong>Niveau 3</strong> : Experts/Ingénieurs<br>
                        • <strong>Niveau 4</strong> : Fournisseurs externes
                    </div>
                    
                    <table class="exercise-table">
                        <thead>
                            <tr>
                                <th>Incident</th>
                                <th>Niveau d'escalade</th>
                                <th>Justification</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Mot de passe oublié</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Serveur de base de données corrompu</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Bug dans un logiciel métier</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Installation d'un nouveau logiciel</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- Exercice 2 -->
        <div id="exercise2" class="exercise-content-wrapper">
            <div class="exercise-summary">
                <strong>Objectif :</strong> Maîtriser le processus de gestion des changements ITIL
            </div>
            
            <h3>🔧 Processus de gestion des changements</h3>
            <p>Vous devez mettre en place un processus de gestion des changements pour votre organisation.</p>
            
            <!-- Navigation des sous-exercices -->
            <div class="sub-exercise-navigation">
                <div class="sub-exercise-tabs">
                    <button class="sub-exercise-tab active" onclick="showSubExercise(2, 1)">2.1</button>
                    <button class="sub-exercise-tab" onclick="showSubExercise(2, 2)">2.2</button>
                </div>
            </div>
            
            <!-- Sous-exercice 2.1 -->
            <div id="sub-exercise-2-1" class="sub-exercise-content active">
                <div class="example-box">
                    <div class="example-title">✏️ Exercice 2.1 – Étapes du changement</div>
                    <p>Remettre dans l'ordre les étapes du processus de gestion des changements :</p>
                    
                    <ul>
                        <li>☐ Évaluation des risques</li>
                        <li>☐ Demande de changement</li>
                        <li>☐ Planification du changement</li>
                        <li>☐ Approbation du changement</li>
                        <li>☐ Implémentation</li>
                        <li>☐ Révision post-implémentation</li>
                        <li>☐ Test et validation</li>
                    </ul>
                    
                    <div class="highlight-fact">
                        💡 <strong>Astuce :</strong> Pensez à la logique : on ne peut pas implémenter avant d'avoir approuvé, ni approuver avant d'avoir évalué les risques !
                    </div>
                </div>
            </div>
            
            <!-- Sous-exercice 2.2 -->
            <div id="sub-exercise-2-2" class="sub-exercise-content">
                <div class="example-box">
                    <div class="example-title">✏️ Exercice 2.2 – Types de changements</div>
                    <p>Classifier chaque changement selon son type et son niveau d'approbation requis.</p>
                    
                    <div class="highlight-fact">
                        <strong>Types de changements :</strong><br>
                        • <strong>Standard</strong> : Changement pré-approuvé, faible risque<br>
                        • <strong>Normal</strong> : Changement nécessitant une évaluation complète<br>
                        • <strong>Urgent</strong> : Changement d'urgence pour résoudre un incident critique
                    </div>
                    
                    <table class="exercise-table">
                        <thead>
                            <tr>
                                <th>Changement</th>
                                <th>Type</th>
                                <th>Niveau d'approbation</th>
                                <th>Justification</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Mise à jour de sécurité Windows</td>
                                <td>_______</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Migration vers un nouveau serveur</td>
                                <td>_______</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Redémarrage d'urgence du serveur web</td>
                                <td>_______</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Ajout d'un nouvel utilisateur</td>
                                <td>_______</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                            <tr>
                                <td>Changement d'architecture réseau</td>
                                <td>_______</td>
                                <td>_______</td>
                                <td>_______</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- Exercice 3 -->
        <div id="exercise3" class="exercise-content-wrapper">
            <div class="exercise-summary">
                <strong>Objectif :</strong> Analyser un cas pratique et proposer des solutions ITIL
            </div>
            
            <h3>📊 Analyse de cas pratique</h3>
            <p>Analyser le cas suivant et proposer une solution ITIL appropriée.</p>
            
            <div class="example-box">
                <div class="example-title">🏢 Cas d'entreprise</div>
                <p><strong>Situation :</strong> Une entreprise de 200 employés constate que :</p>
                <ul>
                    <li>Les pannes informatiques se répètent chaque semaine</li>
                    <li>Les utilisateurs appellent directement les techniciens</li>
                    <li>Aucune documentation des incidents n'existe</li>
                    <li>Les changements sont effectués sans validation</li>
                </ul>
                
                <p><strong>Questions :</strong></p>
                <ol>
                    <li>Quels processus ITIL recommander ?</li>
                    <li>Dans quel ordre les implémenter ?</li>
                    <li>Quels bénéfices attendus ?</li>
                </ol>
            </div>
            
            <div class="example-box">
                <div class="example-title">✅ Correction</div>
                
                <h4><strong>Problèmes constatés</strong></h4>
                <ul>
                    <li>Pannes répétées chaque semaine.</li>
                    <li>Appels directs aux techniciens.</li>
                    <li>Aucune documentation.</li>
                    <li>Changements non validés.</li>
                </ul>
                
                <h4><strong>Processus ITIL à mettre en place</strong></h4>
                <table class="exercise-table">
                    <thead>
                        <tr>
                            <th>Processus</th>
                            <th>Objectif principal</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Gestion des incidents</td>
                            <td>Centraliser les demandes et pannes.</td>
                        </tr>
                        <tr>
                            <td>Gestion des problèmes</td>
                            <td>Identifier et corriger les causes récurrentes.</td>
                        </tr>
                        <tr>
                            <td>Gestion des changements</td>
                            <td>Encadrer les modifications techniques.</td>
                        </tr>
                        <tr>
                            <td>Gestion des connaissances</td>
                            <td>Documenter et partager les solutions.</td>
                        </tr>
                    </tbody>
                </table>
                
                <h4><strong>Ordre de mise en œuvre</strong></h4>
                <ol>
                    <li><strong>Gestion des incidents</strong> → outil de ticketing.</li>
                    <li><strong>Gestion des problèmes</strong> → analyse des causes profondes.</li>
                    <li><strong>Gestion des changements</strong> → validation et test avant déploiement.</li>
                    <li><strong>Gestion des connaissances</strong> → documentation et retours d'expérience.</li>
                </ol>
                
                <h4><strong>Bénéfices attendus</strong></h4>
                <ul>
                    <li>Support plus efficace.</li>
                    <li>Moins de pannes récurrentes.</li>
                    <li>Changements mieux maîtrisés.</li>
                    <li>Capitalisation du savoir interne.</li>
                </ul>
                
                <div class="highlight-fact">
                    💡 <strong>L'entreprise passe d'une logique "réactive" à une gestion "préventive et organisée".</strong>
                </div>
            </div>
        </div>
        
        <!-- Exercice 4 -->
        <div id="exercise4" class="exercise-content-wrapper">
            <div class="exercise-summary">
                <strong>Objectif :</strong> Créer un plan d'implémentation ITIL complet sur le projet d'AP
            </div>
            
            <h3>🎯 Mise en pratique</h3>
            <p>Créer un plan d'implémentation ITIL pour votre organisation.</p>
            
            <div class="step-grid">
                <div class="step-card">
                    <div class="step-number">1</div>
                    <div class="step-title">Diagnostic</div>
                    <div class="step-description">
                        Évaluer la maturité actuelle de votre organisation en matière de gestion des services IT.
                    </div>
                </div>
                
                <div class="step-card">
                    <div class="step-number">2</div>
                    <div class="step-title">Priorisation</div>
                    <div class="step-description">
                        Identifier les processus ITIL les plus critiques à implémenter en premier.
                    </div>
                </div>
                
                <div class="step-card">
                    <div class="step-number">3</div>
                    <div class="step-title">Planification</div>
                    <div class="step-description">
                        Établir un calendrier d'implémentation avec des jalons mesurables.
                    </div>
                </div>
                
                <div class="step-card">
                    <div class="step-number">4</div>
                    <div class="step-title">Formation</div>
                    <div class="step-description">
                        Planifier la formation des équipes aux nouveaux processus ITIL.
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function showExercise(exerciseNumber) {
    // Hide all exercise content
    const allContent = document.querySelectorAll('.exercise-content-wrapper');
    allContent.forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all tabs
    const allTabs = document.querySelectorAll('.exercise-tab');
    allTabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected exercise content
    const selectedContent = document.getElementById(`exercise${exerciseNumber}`);
    if (selectedContent) {
        selectedContent.classList.add('active');
    }
    
    // Add active class to selected tab
    const selectedTab = document.querySelector(`[onclick="showExercise(${exerciseNumber})"]`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
}

function showSubExercise(exerciseNumber, subExerciseNumber) {
    // Hide all sub-exercise content for this exercise
    const allSubContent = document.querySelectorAll(`#exercise${exerciseNumber} .sub-exercise-content`);
    allSubContent.forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all sub-exercise tabs for this exercise
    const allSubTabs = document.querySelectorAll(`#exercise${exerciseNumber} .sub-exercise-tab`);
    allSubTabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected sub-exercise content
    const selectedSubContent = document.getElementById(`sub-exercise-${exerciseNumber}-${subExerciseNumber}`);
    if (selectedSubContent) {
        selectedSubContent.classList.add('active');
    }
    
    // Add active class to selected sub-exercise tab
    const selectedSubTab = document.querySelector(`[onclick="showSubExercise(${exerciseNumber}, ${subExerciseNumber})"]`);
    if (selectedSubTab) {
        selectedSubTab.classList.add('active');
    }
}
</script>