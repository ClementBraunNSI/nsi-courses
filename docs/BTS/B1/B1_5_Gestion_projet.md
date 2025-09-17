<style>
/* Styles modernes pour le cours Gestion de Projet */
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

.process-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.process-card {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(52, 152, 219, 0.2);
    transition: all 0.3s ease;
}

.process-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.process-number {
    font-size: 2rem;
    font-weight: bold;
    color: #3498db;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Courier New', monospace;
}

.process-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 0.5rem;
}

.process-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    text-align: center;
}

.methodology-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.methodology-card {
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    color: white;
    position: relative;
    overflow: hidden;
}

.methodology-v {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.methodology-agile {
    background: linear-gradient(135deg, #2ecc71, #27ae60);
}

.methodology-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.methodology-description {
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.methodology-features {
    text-align: left;
    font-size: 0.9rem;
}

.gantt-example {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid #e9ecef;
}

.gantt-title {
    color: #3498db;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    text-align: center;
}

.gantt-chart {
    display: grid;
    grid-template-columns: 200px repeat(12, 1fr);
    gap: 1px;
    background: #dee2e6;
    border-radius: 8px;
    overflow: hidden;
}

.gantt-header {
    background: #3498db;
    color: white;
    padding: 0.5rem;
    font-weight: 600;
    text-align: center;
    font-size: 0.8rem;
}

.gantt-task {
    background: #ffffff;
    padding: 0.5rem;
    font-weight: 500;
    font-size: 0.8rem;
}

.gantt-cell {
    background: #ffffff;
    padding: 0.5rem;
    text-align: center;
}

.gantt-bar {
    background: linear-gradient(135deg, #3498db, #2980b9);
    height: 20px;
    border-radius: 4px;
    margin: 2px 0;
}

.gantt-milestone {
    background: #e74c3c;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin: 2px auto;
}

.role-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.role-card {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(52, 152, 219, 0.2);
    transition: all 0.3s ease;
}

.role-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.role-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 0.5rem;
    text-align: center;
}

.role-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.git-workflow {
    background: #2c3e50;
    color: #ecf0f1;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    font-family: 'Courier New', monospace;
}

.git-title {
    color: #3498db;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    text-align: center;
}

.git-command {
    background: #34495e;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    margin: 0.5rem 0;
    border-left: 3px solid #3498db;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .process-grid {
        grid-template-columns: 1fr;
    }
    
    .methodology-grid {
        grid-template-columns: 1fr;
    }
    
    .role-grid {
        grid-template-columns: 1fr;
    }
    
    .gantt-chart {
        grid-template-columns: 150px repeat(6, 1fr);
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📊 Gestion de Projet Informatique</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Support et mise à disposition de services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Fondamentaux de la Gestion de Projet</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Qu'est-ce qu'un Projet ?</div>
        <div class="definition-content">
            Un <strong>projet</strong> est un ensemble d'activités temporaires, uniques et coordonnées, visant à atteindre un objectif spécifique dans un délai déterminé avec des ressources limitées. Il se caractérise par un début et une fin clairement définis.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Objectif Défini</div>
            <div class="concept-description">
                Résultat attendu clairement spécifié, mesurable et atteignable dans le temps imparti.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⏰</div>
            <div class="concept-name">Temporalité</div>
            <div class="concept-description">
                Durée limitée avec une date de début et une date de fin précises.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Unicité</div>
            <div class="concept-description">
                Chaque projet est unique et produit un livrable ou service spécifique.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💰</div>
            <div class="concept-name">Ressources Limitées</div>
            <div class="concept-description">
                Budget, équipe et moyens techniques définis et contraints.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Triangle de la gestion de projet :</strong> Qualité, Délai, Coût - modifier l'un impacte nécessairement les deux autres.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">👥 Rôles et Responsabilités</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏗️ Équipe Projet</div>
        <div class="definition-content">
            Une équipe projet efficace réunit des <strong>compétences complémentaires</strong> et des rôles clairement définis pour atteindre les objectifs dans les meilleures conditions.
        </div>
    </div>
    
    <div class="role-grid">
        <div class="role-card">
            <div class="role-title">🎯 Chef de Projet</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Planification et coordination générale<br>
                • Gestion des risques et des délais<br>
                • Communication avec les parties prenantes<br>
                • Suivi budgétaire et reporting
            </div>
        </div>
        
        <div class="role-card">
            <div class="role-title">💼 Product Owner</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Définition des besoins fonctionnels<br>
                • Priorisation des fonctionnalités<br>
                • Validation des livrables<br>
                • Interface avec les utilisateurs finaux
            </div>
        </div>
        
        <div class="role-card">
            <div class="role-title">🏗️ Scrum Master</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Animation des cérémonies agiles<br>
                • Facilitation et résolution d'obstacles<br>
                • Coaching de l'équipe<br>
                • Garant de la méthodologie
            </div>
        </div>
        
        <div class="role-card">
            <div class="role-title">💻 Développeurs</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Conception et développement<br>
                • Tests unitaires et intégration<br>
                • Documentation technique<br>
                • Estimation des charges
            </div>
        </div>
        
        <div class="role-card">
            <div class="role-title">🧪 Testeurs/QA</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Conception des plans de tests<br>
                • Exécution des tests fonctionnels<br>
                • Détection et signalement des anomalies<br>
                • Validation de la qualité
            </div>
        </div>
        
        <div class="role-card">
            <div class="role-title">🎨 UX/UI Designer</div>
            <div class="role-description">
                <strong>Responsabilités :</strong><br>
                • Conception de l'expérience utilisateur<br>
                • Création des maquettes et prototypes<br>
                • Tests d'utilisabilité<br>
                • Respect des standards d'accessibilité
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Communication :</strong> La réussite d'un projet dépend principalement de la qualité de la communication entre les membres de l'équipe.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📈 Diagramme de Gantt</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Outil de Planification</div>
        <div class="definition-content">
            Le <strong>diagramme de Gantt</strong> est un outil graphique de planification qui représente les tâches d'un projet dans le temps, leurs dépendances et l'avancement des travaux.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📅</div>
            <div class="concept-name">Planification Temporelle</div>
            <div class="concept-description">
                Visualisation claire des dates de début et fin de chaque tâche sur une échelle de temps.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Dépendances</div>
            <div class="concept-description">
                Identification des liens entre tâches : antériorité, simultanéité, succession.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Suivi d'Avancement</div>
            <div class="concept-description">
                Comparaison entre planifié et réalisé, identification des retards et ajustements.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Chemin Critique</div>
            <div class="concept-description">
                Séquence de tâches déterminant la durée minimale du projet.
            </div>
        </div>
    </div>
    
    <div class="gantt-example">
        <div class="gantt-title">📊 Exemple : Projet de Développement d'Application Web</div>
        <div class="gantt-chart">
            <div class="gantt-header">Tâches</div>
            <div class="gantt-header">S1</div>
            <div class="gantt-header">S2</div>
            <div class="gantt-header">S3</div>
            <div class="gantt-header">S4</div>
            <div class="gantt-header">S5</div>
            <div class="gantt-header">S6</div>
            <div class="gantt-header">S7</div>
            <div class="gantt-header">S8</div>
            <div class="gantt-header">S9</div>
            <div class="gantt-header">S10</div>
            <div class="gantt-header">S11</div>
            <div class="gantt-header">S12</div>
            
            <div class="gantt-task">Analyse des besoins</div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Conception UX/UI</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Développement Backend</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Développement Frontend</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Tests et Intégration</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Déploiement</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-bar"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            
            <div class="gantt-task">Jalons</div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-milestone"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-milestone"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-milestone"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"><div class="gantt-milestone"></div></div>
            <div class="gantt-cell"></div>
            <div class="gantt-cell"></div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Outils recommandés :</strong> Microsoft Project, GanttProject (gratuit), Trello, Asana, ou des solutions intégrées comme Azure DevOps.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🏁 Jalons (Milestones)</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Points de Contrôle</div>
        <div class="definition-content">
            Les <strong>jalons</strong> sont des événements clés du projet qui marquent l'achèvement d'une phase importante ou la livraison d'un résultat majeur. Ils permettent de mesurer l'avancement et de valider la conformité.
        </div>
    </div>
    
    <div class="process-grid">
        <div class="process-card">
            <div class="process-number">🚀</div>
            <div class="process-name">Lancement Projet</div>
            <div class="process-description">Validation du cahier des charges et démarrage officiel</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">📋</div>
            <div class="process-name">Fin d'Analyse</div>
            <div class="process-description">Spécifications fonctionnelles validées par le client</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🎨</div>
            <div class="process-name">Maquettes Validées</div>
            <div class="process-description">Design et ergonomie approuvés par les utilisateurs</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">⚙️</div>
            <div class="process-name">Prototype Fonctionnel</div>
            <div class="process-description">Version de démonstration des fonctionnalités clés</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🧪</div>
            <div class="process-name">Tests Validés</div>
            <div class="process-description">Recette utilisateur réussie et anomalies corrigées</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🎉</div>
            <div class="process-name">Mise en Production</div>
            <div class="process-description">Déploiement réussi et formation utilisateurs terminée</div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Critères SMART :</strong> Chaque jalon doit être Spécifique, Mesurable, Atteignable, Réaliste et Temporellement défini.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Méthodologies de Gestion de Projet</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚖️ Approches Complémentaires</div>
        <div class="definition-content">
            Les méthodologies de gestion de projet offrent des <strong>cadres structurés</strong> pour organiser, planifier et exécuter les projets selon leur nature, complexité et contraintes.
        </div>
    </div>
    
    <div class="methodology-grid">
        <div class="methodology-card methodology-v">
            <div class="methodology-title">📐 Méthode en V</div>
            <div class="methodology-description">
                Approche séquentielle où chaque phase de développement correspond à une phase de test. Idéale pour les projets avec des exigences stables et bien définies.
            </div>
            <div class="methodology-features">
                <strong>✅ Avantages :</strong><br>
                • Structure claire et prévisible<br>
                • Documentation complète<br>
                • Contrôle qualité rigoureux<br>
                • Adapté aux projets critiques<br><br>
                <strong>❌ Inconvénients :</strong><br>
                • Peu flexible aux changements<br>
                • Feedback tardif du client<br>
                • Risque de dérive des coûts
            </div>
        </div>
        
        <div class="methodology-card methodology-agile">
            <div class="methodology-title">🏃 Méthode Agile</div>
            <div class="methodology-description">
                Approche itérative et collaborative privilégiant l'adaptation au changement et la livraison continue de valeur. Basée sur des cycles courts (sprints).
            </div>
            <div class="methodology-features">
                <strong>✅ Avantages :</strong><br>
                • Flexibilité et adaptabilité<br>
                • Feedback client régulier<br>
                • Livraisons fréquentes<br>
                • Collaboration renforcée<br><br>
                <strong>❌ Inconvénients :</strong><br>
                • Moins de documentation<br>
                • Difficulté d'estimation<br>
                • Nécessite une équipe expérimentée
            </div>
        </div>
    </div>
    
    <div class="process-grid">
        <div class="process-card">
            <div class="process-number">📋</div>
            <div class="process-name">Scrum</div>
            <div class="process-description">Framework agile avec sprints de 2-4 semaines, cérémonies définies et rôles spécifiques</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🔄</div>
            <div class="process-name">Kanban</div>
            <div class="process-description">Méthode visuelle de gestion des flux avec limitation du travail en cours</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🚀</div>
            <div class="process-name">DevOps</div>
            <div class="process-description">Intégration des équipes développement et opérations pour l'automatisation</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">📐</div>
            <div class="process-name">Cycle en V</div>
            <div class="process-description">Modèle séquentiel avec phases de test correspondant aux phases de développement</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Choix de méthodologie :</strong> Agile pour l'innovation et l'incertitude, V pour la stabilité et la conformité réglementaire.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 Versionning avec Git</h2>
    
    <div class="definition-box">
        <div class="definition-title">📚 Gestion des Versions</div>
        <div class="definition-content">
            <strong>Git</strong> est un système de contrôle de version distribué qui permet de suivre les modifications du code, collaborer efficacement et gérer les différentes versions d'un projet.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🌿</div>
            <div class="concept-name">Branches</div>
            <div class="concept-description">
                Lignes de développement parallèles permettant de travailler sur différentes fonctionnalités simultanément.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💾</div>
            <div class="concept-name">Commits</div>
            <div class="concept-description">
                Instantanés du code à un moment donné avec description des modifications apportées.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Merge</div>
            <div class="concept-description">
                Fusion de branches pour intégrer les développements dans la branche principale.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏷️</div>
            <div class="concept-name">Tags</div>
            <div class="concept-description">
                Marqueurs pour identifier les versions stables et les releases du projet.
            </div>
        </div>
    </div>
    
    <div class="git-workflow">
        <div class="git-title">🔧 Workflow Git Standard</div>
        
        <div class="git-command"># Cloner le repository</div>
        <div class="git-command">git clone https://github.com/username/project.git</div>
        
        <div class="git-command"># Créer une nouvelle branche pour une fonctionnalité</div>
        <div class="git-command">git checkout -b feature/nouvelle-fonctionnalite</div>
        
        <div class="git-command"># Ajouter les modifications</div>
        <div class="git-command">git add .</div>
        
        <div class="git-command"># Commiter avec un message descriptif</div>
        <div class="git-command">git commit -m "feat: ajout de la fonctionnalité X"</div>
        
        <div class="git-command"># Pousser la branche vers le repository distant</div>
        <div class="git-command">git push origin feature/nouvelle-fonctionnalite</div>
        
        <div class="git-command"># Créer une Pull Request pour review</div>
        <div class="git-command"># Via l'interface GitHub/GitLab</div>
        
        <div class="git-command"># Après validation, merger dans main</div>
        <div class="git-command">git checkout main</div>
        <div class="git-command">git pull origin main</div>
        <div class="git-command">git merge feature/nouvelle-fonctionnalite</div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🌿</div>
            <div class="concept-name">GitFlow</div>
            <div class="concept-description">
                Modèle de branches avec main, develop, feature, release et hotfix pour projets complexes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🚀</div>
            <div class="concept-name">GitHub Flow</div>
            <div class="concept-description">
                Workflow simplifié avec main et branches de fonctionnalités pour déploiement continu.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">CI/CD</div>
            <div class="concept-description">
                Intégration et déploiement continus automatisés via GitHub Actions, GitLab CI.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📝</div>
            <div class="concept-name">Conventional Commits</div>
            <div class="concept-description">
                Convention de nommage des commits : feat, fix, docs, style, refactor, test.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Bonnes pratiques :</strong> Commits atomiques (le moins de mots possibles), messages clairs, branches courtes, reviews systématiques, tests automatisés.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Suivi et Contrôle de Projet</h2>
    
    <div class="definition-box">
        <div class="definition-title">📈 Pilotage de Projet</div>
        <div class="definition-content">
            Le suivi de projet consiste à <strong>mesurer l'avancement</strong>, identifier les écarts par rapport au plan initial et prendre les actions correctives nécessaires pour respecter les objectifs.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Indicateurs KPI</div>
            <div class="concept-description">
                Métriques de performance : vélocité, taux de défauts, respect des délais.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💰</div>
            <div class="concept-name">Suivi Budgétaire</div>
            <div class="concept-description">
                Contrôle des coûts réels vs prévisionnels, analyse des écarts et projections.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚠️</div>
            <div class="concept-name">Gestion des Risques</div>
            <div class="concept-description">
                Identification, évaluation et mitigation des risques techniques, humains et organisationnels.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📢</div>
            <div class="concept-name">Communication</div>
            <div class="concept-description">
                Reporting régulier, réunions de suivi, tableaux de bord et communication avec les parties prenantes.
            </div>
        </div>
    </div>
</div>