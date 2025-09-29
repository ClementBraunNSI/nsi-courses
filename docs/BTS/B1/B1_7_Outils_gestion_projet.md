<style>
/* Styles modernes pour le cours Outils de Gestion de Projet */
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
    color: #8e44ad;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-left: 5px solid #8e44ad;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.tool-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.tool-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 20px;
    padding: 2rem;
    border: 2px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(155, 89, 182, 0.2);
}

.tool-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.tool-icon {
    font-size: 2.5rem;
    margin-right: 1rem;
}

.tool-name {
    font-size: 1.4rem;
    font-weight: 600;
    color: #8e44ad;
}

.tool-category {
    font-size: 0.9rem;
    color: #7f8c8d;
    background: rgba(155, 89, 182, 0.1);
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    margin-left: auto;
}

.tool-description {
    color: var(--md-default-fg-color);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.tool-features {
    list-style: none;
    padding: 0;
    margin-bottom: 1.5rem;
}

.tool-features li {
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(155, 89, 182, 0.1);
}

.tool-features li:before {
    content: "⚡ ";
    color: #8e44ad;
    font-weight: bold;
}

.tool-pricing {
    background: rgba(155, 89, 182, 0.1);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
    color: #8e44ad;
}

.gantt-chart {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
}

.gantt-header {
    display: grid;
    grid-template-columns: 200px repeat(8, 1fr);
    gap: 1px;
    margin-bottom: 1rem;
}

.gantt-cell {
    padding: 0.5rem;
    text-align: center;
    font-weight: 600;
    background: linear-gradient(135deg, #8e44ad, #9b59b6);
    color: white;
    border-radius: 5px;
}

.gantt-row {
    display: grid;
    grid-template-columns: 200px repeat(8, 1fr);
    gap: 1px;
    margin-bottom: 0.5rem;
    align-items: center;
}

.gantt-task {
    padding: 0.5rem;
    font-weight: 500;
    background: rgba(155, 89, 182, 0.1);
    border-radius: 5px;
}

.gantt-bar {
    height: 30px;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 0.8rem;
    font-weight: 600;
}

.gantt-bar-analysis { background: linear-gradient(135deg, #3498db, #2980b9); }
.gantt-bar-design { background: linear-gradient(135deg, #e74c3c, #c0392b); }
.gantt-bar-dev { background: linear-gradient(135deg, #2ecc71, #27ae60); }
.gantt-bar-test { background: linear-gradient(135deg, #f39c12, #e67e22); }

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
    background: linear-gradient(135deg, #8e44ad, #9b59b6);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.comparison-table td {
    padding: 1rem;
    text-align: center;
    border-bottom: 1px solid rgba(155, 89, 182, 0.1);
}

.comparison-table tr:nth-child(even) {
    background: rgba(155, 89, 182, 0.05);
}

.comparison-table tr:hover {
    background: rgba(155, 89, 182, 0.1);
}

.pert-diagram {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.05), rgba(142, 68, 173, 0.02));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
}

.pert-nodes {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    gap: 2rem;
}

.pert-node {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: linear-gradient(135deg, #8e44ad, #9b59b6);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    position: relative;
}

.pert-node-label {
    font-size: 0.8rem;
    margin-top: 0.5rem;
}

.pert-arrow {
    font-size: 2rem;
    color: #8e44ad;
    align-self: center;
}

.ap-integration-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.1));
    border: 2px solid rgba(155, 89, 182, 0.3);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
}

.ap-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 1rem;
    text-align: center;
}

.ap-content {
    color: var(--md-default-fg-color);
    line-height: 1.6;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.15), rgba(142, 68, 173, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    margin: 2rem 0;
    border-left: 5px solid #8e44ad;
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
    
    .tool-grid {
        grid-template-columns: 1fr;
    }
    
    .gantt-header, .gantt-row {
        grid-template-columns: 150px repeat(4, 1fr);
    }
    
    .pert-nodes {
        flex-direction: column;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🛠️ Outils de Gestion de Projet</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Maîtrise des outils professionnels pour l'AP</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Panorama des Outils de Gestion</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Écosystème des Outils</div>
        <div class="definition-content">
            Les outils de gestion de projet facilitent la <strong>planification</strong>, le <strong>suivi</strong> et la <strong>collaboration</strong> dans vos projets d'AP. Ils permettent de visualiser les tâches, gérer les ressources, suivre l'avancement et communiquer efficacement avec votre équipe et vos encadrants.
        </div>
    </div>
    
    <div class="content-text">
        Pour votre Atelier Professionnel en BTS SIO 2ème année, la maîtrise de ces outils est essentielle. Ils vous permettront de démontrer votre professionnalisme et votre capacité à gérer un projet selon les standards de l'industrie informatique.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Diagrammes de Gantt</h2>
    
    <div class="definition-box">
        <div class="definition-title">📈 Planification Temporelle</div>
        <div class="definition-content">
            Le diagramme de Gantt visualise les tâches d'un projet dans le temps, montrant les <strong>dépendances</strong>, les <strong>durées</strong> et l'<strong>avancement</strong>. Idéal pour planifier votre AP et communiquer sur les délais.
        </div>
    </div>
    
    <div class="gantt-chart">
        <div class="gantt-header">
            <div class="gantt-cell">Tâches AP</div>
            <div class="gantt-cell">S1</div>
            <div class="gantt-cell">S2</div>
            <div class="gantt-cell">S3</div>
            <div class="gantt-cell">S4</div>
            <div class="gantt-cell">S5</div>
            <div class="gantt-cell">S6</div>
            <div class="gantt-cell">S7</div>
            <div class="gantt-cell">S8</div>
        </div>
        
        <div class="gantt-row">
            <div class="gantt-task">Analyse des besoins</div>
            <div class="gantt-bar gantt-bar-analysis">Analyse</div>
            <div class="gantt-bar gantt-bar-analysis">Analyse</div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
        
        <div class="gantt-row">
            <div class="gantt-task">Conception UI/UX</div>
            <div></div>
            <div class="gantt-bar gantt-bar-design">Design</div>
            <div class="gantt-bar gantt-bar-design">Design</div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
        
        <div class="gantt-row">
            <div class="gantt-task">Développement</div>
            <div></div>
            <div></div>
            <div class="gantt-bar gantt-bar-dev">Dev</div>
            <div class="gantt-bar gantt-bar-dev">Dev</div>
            <div class="gantt-bar gantt-bar-dev">Dev</div>
            <div class="gantt-bar gantt-bar-dev">Dev</div>
            <div></div>
            <div></div>
        </div>
        
        <div class="gantt-row">
            <div class="gantt-task">Tests & Déploiement</div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div class="gantt-bar gantt-bar-test">Tests</div>
            <div class="gantt-bar gantt-bar-test">Tests</div>
            <div class="gantt-bar gantt-bar-test">Deploy</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Avantage Gantt :</strong> Visualisation claire des dépendances et identification rapide des retards potentiels sur le chemin critique.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔗 Méthode PERT</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Program Evaluation and Review Technique</div>
        <div class="definition-content">
            PERT est une méthode de gestion de projet qui utilise un <strong>réseau de tâches</strong> pour identifier le chemin critique et estimer les durées avec incertitude. Particulièrement utile pour les projets innovants d'AP.
        </div>
    </div>
    
    <div class="pert-diagram">
        <div class="pert-nodes">
            <div class="pert-node">
                <div>A</div>
                <div class="pert-node-label">Début</div>
            </div>
            <div class="pert-arrow">→</div>
            <div class="pert-node">
                <div>B</div>
                <div class="pert-node-label">Analyse</div>
            </div>
            <div class="pert-arrow">→</div>
            <div class="pert-node">
                <div>C</div>
                <div class="pert-node-label">Design</div>
            </div>
            <div class="pert-arrow">→</div>
            <div class="pert-node">
                <div>D</div>
                <div class="pert-node-label">Dev</div>
            </div>
            <div class="pert-arrow">→</div>
            <div class="pert-node">
                <div>E</div>
                <div class="pert-node-label">Tests</div>
            </div>
            <div class="pert-arrow">→</div>
            <div class="pert-node">
                <div>F</div>
                <div class="pert-node-label">Fin</div>
            </div>
        </div>
    </div>
    
    <div class="content-text">
        <strong>Calcul PERT :</strong> Durée estimée = (Optimiste + 4×Probable + Pessimiste) / 6<br>
        Exemple : Développement = (3 + 4×5 + 8) / 6 = 5,17 semaines
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛠️ Outils Recommandés pour l'AP</h2>
    
    <div class="tool-grid">
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">📋</div>
                <div>
                    <div class="tool-name">Trello</div>
                    <div class="tool-category">Kanban Simple</div>
                </div>
            </div>
            <div class="tool-description">
                Interface intuitive basée sur des cartes et des listes. Parfait pour débuter avec Kanban dans votre AP.
            </div>
            <ul class="tool-features">
                <li>Tableaux Kanban visuels</li>
                <li>Collaboration en temps réel</li>
                <li>Intégrations (GitHub, Slack)</li>
                <li>Applications mobiles</li>
            </ul>
            <div class="tool-pricing">Gratuit jusqu'à 10 équipes</div>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">🚀</div>
                <div>
                    <div class="tool-name">Jira</div>
                    <div class="tool-category">Agile Professionnel</div>
                </div>
            </div>
            <div class="tool-description">
                Outil professionnel pour Scrum et Kanban. Standard de l'industrie, excellent pour votre CV.
            </div>
            <ul class="tool-features">
                <li>Scrum et Kanban avancés</li>
                <li>Rapports et métriques</li>
                <li>Gestion des bugs</li>
                <li>Intégration DevOps complète</li>
            </ul>
            <div class="tool-pricing">Gratuit jusqu'à 10 utilisateurs</div>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">📊</div>
                <div>
                    <div class="tool-name">Microsoft Project</div>
                    <div class="tool-category">Gantt Avancé</div>
                </div>
            </div>
            <div class="tool-description">
                Référence pour les diagrammes de Gantt et la gestion de ressources. Idéal pour les projets complexes.
            </div>
            <ul class="tool-features">
                <li>Diagrammes de Gantt complets</li>
                <li>Gestion des ressources</li>
                <li>Analyse du chemin critique</li>
                <li>Rapports avancés</li>
            </ul>
            <div class="tool-pricing">Licence étudiante disponible</div>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">🐙</div>
                <div>
                    <div class="tool-name">GitHub Projects</div>
                    <div class="tool-category">Intégré Git</div>
                </div>
            </div>
            <div class="tool-description">
                Gestion de projet intégrée à votre code source. Parfait pour les projets de développement d'AP.
            </div>
            <ul class="tool-features">
                <li>Intégration native avec Git</li>
                <li>Issues et Pull Requests</li>
                <li>Tableaux Kanban</li>
                <li>Automatisations</li>
            </ul>
            <div class="tool-pricing">Gratuit pour projets publics</div>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">🎨</div>
                <div>
                    <div class="tool-name">Notion</div>
                    <div class="tool-category">Tout-en-un</div>
                </div>
            </div>
            <div class="tool-description">
                Espace de travail collaboratif combinant notes, tâches, bases de données et wiki.
            </div>
            <ul class="tool-features">
                <li>Documentation intégrée</li>
                <li>Bases de données relationnelles</li>
                <li>Templates de projet</li>
                <li>Collaboration avancée</li>
            </ul>
            <div class="tool-pricing">Gratuit pour usage personnel</div>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">💎</div>
                <div>
                    <div class="tool-name">Monday.com</div>
                    <div class="tool-category">Visuel & Flexible</div>
                </div>
            </div>
            <div class="tool-description">
                Plateforme visuelle et intuitive pour la gestion de projet avec de nombreuses vues personnalisables.
            </div>
            <ul class="tool-features">
                <li>Vues multiples (Gantt, Kanban, Timeline)</li>
                <li>Automatisations visuelles</li>
                <li>Tableaux de bord</li>
                <li>Intégrations nombreuses</li>
            </ul>
            <div class="tool-pricing">Essai gratuit 14 jours</div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚖️ Comparaison des Outils</h2>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Outil</th>
                <th>Complexité</th>
                <th>Gantt</th>
                <th>Kanban</th>
                <th>Scrum</th>
                <th>Prix Étudiant</th>
                <th>Recommandation AP</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Trello</strong></td>
                <td>Faible</td>
                <td>❌</td>
                <td>✅</td>
                <td>⚠️</td>
                <td>Gratuit</td>
                <td>Débutants, projets simples</td>
            </tr>
            <tr>
                <td><strong>Jira</strong></td>
                <td>Élevée</td>
                <td>⚠️</td>
                <td>✅</td>
                <td>✅</td>
                <td>Gratuit</td>
                <td>Projets agiles complexes</td>
            </tr>
            <tr>
                <td><strong>MS Project</strong></td>
                <td>Élevée</td>
                <td>✅</td>
                <td>❌</td>
                <td>❌</td>
                <td>Licence étudiante</td>
                <td>Projets avec contraintes temporelles</td>
            </tr>
            <tr>
                <td><strong>GitHub Projects</strong></td>
                <td>Moyenne</td>
                <td>❌</td>
                <td>✅</td>
                <td>⚠️</td>
                <td>Gratuit</td>
                <td>Projets de développement</td>
            </tr>
            <tr>
                <td><strong>Notion</strong></td>
                <td>Moyenne</td>
                <td>⚠️</td>
                <td>✅</td>
                <td>⚠️</td>
                <td>Gratuit</td>
                <td>Documentation + gestion</td>
            </tr>
            <tr>
                <td><strong>Monday.com</strong></td>
                <td>Moyenne</td>
                <td>✅</td>
                <td>✅</td>
                <td>✅</td>
                <td>Essai gratuit</td>
                <td>Équipes mixtes</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="concept-section">
    <h2 class="section-title">🎓 Intégration dans l'AP</h2>
    
    <div class="ap-integration-box">
        <div class="ap-title">🚀 Stratégie d'Adoption pour l'AP</div>
        <div class="ap-content">
            <strong>Phase 1 - Démarrage (Semaines 1-2) :</strong><br>
            • Choisir l'outil principal selon la complexité du projet<br>
            • Former l'équipe aux fonctionnalités de base<br>
            • Créer la structure initiale du projet<br><br>
            
            <strong>Phase 2 - Planification (Semaines 3-4) :</strong><br>
            • Décomposer le projet en tâches dans l'outil<br>
            • Définir les dépendances et les jalons<br>
            • Assigner les responsabilités<br><br>
            
            <strong>Phase 3 - Exécution (Semaines 5-16) :</strong><br>
            • Mise à jour quotidienne de l'avancement<br>
            • Utilisation des rapports pour le suivi<br>
            • Adaptation selon les retours d'expérience
        </div>
    </div>
    
    <div class="ap-integration-box">
        <div class="ap-title">📊 Métriques à Suivre dans l'AP</div>
        <div class="ap-content">
            • <strong>Vélocité :</strong> Nombre de points/tâches réalisées par sprint<br>
            • <strong>Burndown :</strong> Évolution du travail restant dans le temps<br>
            • <strong>Lead Time :</strong> Temps entre création et livraison d'une tâche<br>
            • <strong>Cycle Time :</strong> Temps de traitement effectif d'une tâche<br>
            • <strong>Taux de réouverture :</strong> Pourcentage de tâches rouvertes après fermeture
        </div>
    </div>
    
    <div class="highlight-fact">
        🎯 <strong>Conseil AP :</strong> Documentez votre utilisation des outils dans votre rapport de projet. Incluez des captures d'écran des tableaux de bord et expliquez comment ils ont contribué au succès du projet.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 Bonnes Pratiques</h2>
    
    <div class="tool-grid">
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">📝</div>
                <div>
                    <div class="tool-name">Définition des Tâches</div>
                </div>
            </div>
            <div class="tool-description">
                Créez des tâches claires, mesurables et avec des critères d'acceptation précis.
            </div>
            <ul class="tool-features">
                <li>Titre explicite et actionnable</li>
                <li>Description détaillée</li>
                <li>Critères d'acceptation</li>
                <li>Estimation de charge</li>
            </ul>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">🔄</div>
                <div>
                    <div class="tool-name">Mise à Jour Régulière</div>
                </div>
            </div>
            <div class="tool-description">
                Maintenez vos outils à jour pour refléter la réalité du projet.
            </div>
            <ul class="tool-features">
                <li>Mise à jour quotidienne</li>
                <li>Commentaires sur les blocages</li>
                <li>Ajustement des estimations</li>
                <li>Documentation des décisions</li>
            </ul>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">👥</div>
                <div>
                    <div class="tool-name">Collaboration Efficace</div>
                </div>
            </div>
            <div class="tool-description">
                Utilisez les fonctionnalités collaboratives pour améliorer la communication.
            </div>
            <ul class="tool-features">
                <li>Notifications pertinentes</li>
                <li>Commentaires constructifs</li>
                <li>Partage de fichiers</li>
                <li>Mentions d'équipiers</li>
            </ul>
        </div>
        
        <div class="tool-card">
            <div class="tool-header">
                <div class="tool-icon">📊</div>
                <div>
                    <div class="tool-name">Analyse et Amélioration</div>
                </div>
            </div>
            <div class="tool-description">
                Exploitez les données pour améliorer continuellement vos processus.
            </div>
            <ul class="tool-features">
                <li>Analyse des métriques</li>
                <li>Identification des goulots</li>
                <li>Rétrospectives basées sur les données</li>
                <li>Optimisation des workflows</li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        🏆 <strong>Succès de l'AP :</strong> La maîtrise des outils de gestion de projet démontre votre professionnalisme et votre capacité à travailler selon les standards de l'industrie. C'est un atout majeur pour votre insertion professionnelle et la réussite de votre projet d'Atelier Professionnel !
    </div>
</div>