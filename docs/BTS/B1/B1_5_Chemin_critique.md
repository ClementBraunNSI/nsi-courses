<style>
/* Styles modernes pour le cours Chemin Critique */
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

.task-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.task-table th,
.task-table td {
    padding: 0.8rem;
    text-align: left;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.task-table th {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    font-weight: 600;
}

.example-box .task-table th {
    background: linear-gradient(135deg, #27ae60, #2ecc71);
    color: white;
    font-weight: 600;
}

.task-table tr:hover {
    background: rgba(52, 152, 219, 0.1);
}

.critical-path {
    background: rgba(231, 76, 60, 0.2);
    font-weight: bold;
    color: #c0392b;
}

.network-diagram {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    border: 2px solid rgba(52, 152, 219, 0.3);
}

.node {
    display: inline-block;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    line-height: 80px;
    margin: 0.5rem;
    font-weight: bold;
    position: relative;
}

.critical-node {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
    box-shadow: 0 0 20px rgba(231, 76, 60, 0.5);
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
    
    .course-header {
        padding: 2rem;
    }
    
    .task-table {
        font-size: 0.8rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🎯 Le Chemin Critique</h1>
    <p class="course-subtitle">Méthode de planification et d'optimisation de projets</p>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Qu'est-ce que le Chemin Critique ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Définition Fondamentale</div>
        <div class="definition-content">
            Le <strong>chemin critique</strong> est la séquence de tâches qui détermine la durée minimale d'un projet. C'est le plus long chemin en termes de temps dans le réseau de tâches du projet. Tout retard sur une tâche du chemin critique retarde l'ensemble du projet.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⏱️</div>
            <div class="concept-name">Durée du Projet</div>
            <div class="concept-description">
                Le chemin critique détermine la durée totale minimale nécessaire pour terminer le projet.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Séquence de Tâches</div>
            <div class="concept-description">
                Suite logique de tâches interdépendantes sans marge de manœuvre temporelle.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚠️</div>
            <div class="concept-name">Risque Critique</div>
            <div class="concept-description">
                Tout retard sur ces tâches impacte directement la date de fin du projet.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Focus Prioritaire</div>
            <div class="concept-description">
                Ces tâches nécessitent une attention et un suivi particuliers du chef de projet.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Concepts Clés</h2>
    
    <div class="definition-box">
        <div class="definition-title">📝 Terminologie Essentielle</div>
        <div class="definition-content">
            Pour comprendre le chemin critique, il faut maîtriser plusieurs concepts fondamentaux de la planification de projet.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-title">🎯 Tâche Critique</div>
            <div class="method-description">
                Tâche dont le retard impacte directement la date de fin du projet. Marge libre = 0.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">⏰ Marge Libre</div>
            <div class="method-description">
                Temps de retard possible d'une tâche sans affecter le début de la tâche suivante.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">📅 Marge Totale</div>
            <div class="method-description">
                Temps de retard possible d'une tâche sans affecter la date de fin du projet.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">🔄 Dépendance</div>
            <div class="method-description">
                Relation logique entre tâches : une tâche ne peut commencer qu'après la fin d'une autre.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛠️ Méthode de Calcul</h2>
    
    <div class="definition-box">
        <div class="definition-title">📐 Algorithme du Chemin Critique</div>
        <div class="definition-content">
            Le calcul du chemin critique suit une méthode rigoureuse en plusieurs étapes.
        </div>
    </div>
    
    <div class="step-grid">
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">Identifier les Tâches</div>
            <div class="step-description">
                Lister toutes les tâches du projet avec leurs durées et dépendances.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">Construire le Réseau</div>
            <div class="step-description">
                Créer le diagramme PERT avec les nœuds (tâches) et les liens (dépendances et leur durée).
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">Lister les chemins disponibles</div>
            <div class="step-description">
                Pour chaque noeud de départ, lister les chemins possibles vers le noeud de fin.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">4</div>
            <div class="step-title">Calculer les durées</div>
            <div class="step-description">
                Calculer les durées de chacun des chemins.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">6</div>
            <div class="step-title">Identifier le Chemin</div>
            <div class="step-description">
                Le chemin critique est le chemin qui a la durée la plus longue.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💼 Exemple Pratique</h2>
    
    <div class="example-box">
        <div class="example-title">🏗️ Projet : Développement d'une Application Mobile</div>
        
        <p><strong>Contexte :</strong> Une entreprise souhaite développer une application mobile. Voici les tâches identifiées :</p>
        
        <table class="task-table">
            <thead>
                <tr>
                    <th>Tâche</th>
                    <th>Description</th>
                    <th>Durée (jours)</th>
                    <th>Prédécesseurs</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>A</strong></td>
                    <td>Analyse des besoins</td>
                    <td>5</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><strong>B</strong></td>
                    <td>Conception UI/UX</td>
                    <td>8</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>C</strong></td>
                    <td>Développement Backend</td>
                    <td>15</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>D</strong></td>
                    <td>Développement Frontend</td>
                    <td>12</td>
                    <td>B</td>
                </tr>
                <tr>
                    <td><strong>E</strong></td>
                    <td>Intégration API</td>
                    <td>6</td>
                    <td>C, D</td>
                </tr>
                <tr>
                    <td><strong>F</strong></td>
                    <td>Tests et débogage</td>
                    <td>7</td>
                    <td>E</td>
                </tr>
                <tr>
                    <td><strong>G</strong></td>
                    <td>Déploiement</td>
                    <td>3</td>
                    <td>F</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Applications Pratiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">💼 Utilisation en Entreprise</div>
        <div class="definition-content">
            Le chemin critique est un outil essentiel pour les chefs de projet dans de nombreux domaines d'activité.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📱</div>
            <div class="concept-name">Projets IT</div>
            <div class="concept-description">
                Développement logiciel, déploiement d'infrastructures, migration de systèmes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏗️</div>
            <div class="concept-name">Construction</div>
            <div class="concept-description">
                Planification de chantiers, coordination des corps de métier, respect des délais.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎬</div>
            <div class="concept-name">Production</div>
            <div class="concept-description">
                Organisation d'événements, production audiovisuelle, lancement de produits.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔬</div>
            <div class="concept-name">Recherche & Développement</div>
            <div class="concept-description">
                Projets de recherche, développement de nouveaux produits, études cliniques.
            </div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-title">📊 Planification</div>
            <div class="method-description">
                Optimiser l'allocation des ressources et définir les priorités du projet.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">⏰ Suivi</div>
            <div class="method-description">
                Surveiller l'avancement et détecter rapidement les risques de retard.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">💰 Optimisation</div>
            <div class="method-description">
                Réduire les coûts en identifiant les tâches où investir en priorité.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-title">📢 Communication</div>
            <div class="method-description">
                Expliquer clairement les enjeux et priorités aux parties prenantes.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📝 Exercices Pratiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Mise en Application</div>
        <div class="definition-content">
            Testez vos connaissances avec ces trois exercices pratiques inspirés de projets informatiques réels en entreprise.
        </div>
    </div>
    
    <div class="example-box">
        <div class="example-title">🔹 Exercice 1 – Mise en place d'un serveur web</div>
        
        <p><strong>Contexte :</strong> Un projet de mise en place d'un serveur web est découpé en tâches :</p>
        
        <table class="task-table">
            <thead>
                <tr>
                    <th>Tâche</th>
                    <th>Description</th>
                    <th>Durée (jours)</th>
                    <th>Prédécesseurs</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>A</strong></td>
                    <td>Installer Linux</td>
                    <td>2</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><strong>B</strong></td>
                    <td>Configurer le réseau</td>
                    <td>1</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>C</strong></td>
                    <td>Installer Apache</td>
                    <td>2</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>D</strong></td>
                    <td>Installer la base MySQL</td>
                    <td>3</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>E</strong></td>
                    <td>Déployer le site web</td>
                    <td>2</td>
                    <td>B, C, D</td>
                </tr>
                <tr>
                    <td><strong>F</strong></td>
                    <td>Tests et validation</td>
                    <td>1</td>
                    <td>E</td>
                </tr>
            </tbody>
        </table>
        
        <div class="step-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-title">Tracez le graphe PERT</div>
                <div class="step-description">
                    Représentez les tâches et leurs dépendances sous forme de réseau.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-title">Calculez les chemins possibles</div>
                <div class="step-description">
                    Identifiez tous les chemins du début à la fin et calculez leur durée.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-title">Déterminez le chemin critique</div>
                <div class="step-description">
                    Trouvez le chemin le plus long et la durée totale du projet.
                </div>
            </div>
        </div>
    </div>
    
    <div class="example-box">
        <div class="example-title">🔹 Exercice 2 – Développement d'une application interne</div>
        
        <p><strong>Contexte :</strong> Une équipe doit développer une petite application interne. Les tâches sont :</p>
        
        <table class="task-table">
            <thead>
                <tr>
                    <th>Tâche</th>
                    <th>Description</th>
                    <th>Durée (jours)</th>
                    <th>Prédécesseurs</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>A</strong></td>
                    <td>Analyse des besoins</td>
                    <td>3</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><strong>B</strong></td>
                    <td>Conception de la maquette</td>
                    <td>4</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>C</strong></td>
                    <td>Développement Backend</td>
                    <td>6</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>D</strong></td>
                    <td>Développement Frontend</td>
                    <td>5</td>
                    <td>B</td>
                </tr>
                <tr>
                    <td><strong>E</strong></td>
                    <td>Intégration Front + Back</td>
                    <td>3</td>
                    <td>C, D</td>
                </tr>
                <tr>
                    <td><strong>F</strong></td>
                    <td>Tests utilisateurs</td>
                    <td>2</td>
                    <td>E</td>
                </tr>
                <tr>
                    <td><strong>G</strong></td>
                    <td>Mise en production</td>
                    <td>1</td>
                    <td>F</td>
                </tr>
            </tbody>
        </table>
        
        <div class="step-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-title">Construisez le graphe</div>
                <div class="step-description">
                    Représentez les dépendances entre les tâches de développement.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-title">Énumérez les chemins</div>
                <div class="step-description">
                    Calculez la durée de chaque chemin possible du projet.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-title">Identifiez le critique</div>
                <div class="step-description">
                    Trouvez le chemin critique et la durée totale.
                </div>
            </div>
        </div>
    </div>
    
    <div class="example-box">
        <div class="example-title">🔹 Exercice 3 – Sécurisation d'un réseau</div>
        
        <p><strong>Contexte :</strong> Une société décide de sécuriser son réseau :</p>
        
        <table class="task-table">
            <thead>
                <tr>
                    <th>Tâche</th>
                    <th>Description</th>
                    <th>Durée (jours)</th>
                    <th>Prédécesseurs</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>A</strong></td>
                    <td>Audit du réseau</td>
                    <td>2</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><strong>B</strong></td>
                    <td>Mise à jour des routeurs</td>
                    <td>3</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>C</strong></td>
                    <td>Installation du firewall</td>
                    <td>2</td>
                    <td>B</td>
                </tr>
                <tr>
                    <td><strong>D</strong></td>
                    <td>Installation d'un IDS</td>
                    <td>4</td>
                    <td>B</td>
                </tr>
                <tr>
                    <td><strong>E</strong></td>
                    <td>Configuration des sauvegardes</td>
                    <td>2</td>
                    <td>A</td>
                </tr>
                <tr>
                    <td><strong>F</strong></td>
                    <td>Tests de sécurité globale</td>
                    <td>3</td>
                    <td>C, D, E</td>
                </tr>
            </tbody>
        </table>
        
        <div class="step-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-title">Représentez le graphe PERT</div>
                <div class="step-description">
                    Créez le réseau des tâches de sécurisation.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-title">Calculez tous les chemins</div>
                <div class="step-description">
                    Identifiez et calculez la durée de chaque chemin possible.
                </div>
            </div>
            
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-title">Identifiez le chemin critique</div>
                <div class="step-description">
                    Trouvez le chemin le plus long et la durée totale.
                </div>
            </div>
        </div>
        
        
    </div>
</div>