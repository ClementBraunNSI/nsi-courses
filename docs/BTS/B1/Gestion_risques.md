<style>
/* Styles modernes pour le cours Gestion des Risques */
.course-header {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(231, 76, 60, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
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
    color: #c0392b;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    border-left: 5px solid #c0392b;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #c0392b;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

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
    background: linear-gradient(135deg, #c0392b, #e74c3c);
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
    background: rgba(231, 76, 60, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    color: #c0392b;
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

.risk-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.risk-card {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    border-radius: 20px;
    padding: 2rem;
    border: 2px solid rgba(231, 76, 60, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.risk-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(231, 76, 60, 0.2);
}

.risk-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.risk-icon {
    font-size: 2.5rem;
    margin-right: 1rem;
}

.risk-name {
    font-size: 1.4rem;
    font-weight: 600;
    color: #c0392b;
}

.risk-level {
    font-size: 0.9rem;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    margin-left: auto;
    font-weight: 600;
}

.risk-description {
    color: var(--md-default-fg-color);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.risk-impacts {
    list-style: none;
    padding: 0;
    margin-bottom: 1.5rem;
}

.risk-impacts li {
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(231, 76, 60, 0.1);
}

.risk-impacts li:before {
    content: "⚠️ ";
    color: #c0392b;
    font-weight: bold;
}

.mitigation-box {
    background: rgba(231, 76, 60, 0.1);
    border-radius: 10px;
    padding: 1rem;
    margin-top: 1rem;
}

.mitigation-title {
    font-weight: 600;
    color: #c0392b;
    margin-bottom: 0.5rem;
}

.process-flow {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.05), rgba(192, 57, 43, 0.02));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
}

.flow-steps {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.flow-step {
    background: linear-gradient(135deg, #c0392b, #e74c3c);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    flex: 1;
    min-width: 150px;
    position: relative;
}

.flow-step-number {
    background: rgba(255, 255, 255, 0.2);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem;
    font-weight: 600;
}

.flow-step-title {
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.flow-arrow {
    font-size: 2rem;
    color: #c0392b;
    align-self: center;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.15), rgba(192, 57, 43, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    margin: 2rem 0;
    border-left: 5px solid #c0392b;
    font-weight: 500;
}

.content-text {
    color: var(--md-default-fg-color);
    line-height: 1.7;
    margin: 1.5rem 0;
    font-size: 1.1rem;
}

.risk-register-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.risk-register-table th {
    background: linear-gradient(135deg, #c0392b, #e74c3c);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.risk-register-table td {
    padding: 1rem;
    text-align: center;
    border-bottom: 1px solid rgba(231, 76, 60, 0.1);
}

.risk-register-table tr:nth-child(even) {
    background: rgba(231, 76, 60, 0.05);
}

.risk-register-table tr:hover {
    background: rgba(231, 76, 60, 0.1);
}

.probability-scale {
    display: flex;
    justify-content: space-between;
    margin: 2rem 0;
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.probability-item {
    text-align: center;
    flex: 1;
    padding: 1rem;
    border-radius: 10px;
    margin: 0 0.5rem;
    color: white;
    font-weight: 600;
}

.prob-1 { background: linear-gradient(135deg, #27ae60, #2ecc71); }
.prob-2 { background: linear-gradient(135deg, #f1c40f, #f39c12); }
.prob-3 { background: linear-gradient(135deg, #e67e22, #d35400); }
.prob-4 { background: linear-gradient(135deg, #e74c3c, #c0392b); }
.prob-5 { background: linear-gradient(135deg, #8e44ad, #9b59b6); }

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .risk-grid {
        grid-template-columns: 1fr;
    }
    
    .flow-steps {
        flex-direction: column;
    }
    
    .flow-arrow {
        transform: rotate(90deg);
    }
    
    .matrix-grid {
        grid-template-columns: 80px repeat(3, 1fr);
        grid-template-rows: 40px repeat(3, 50px);
    }
    
    .probability-scale {
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .course-header {
        padding: 2rem;
    }
}
.git-note {
    background: rgba(52, 152, 219, 0.1);
    border-left: 3px solid #3498db;
    padding: 0.8rem;
    margin: 0.5rem 0;
    border-radius: 5px;
    font-style: italic;
    color: #2c3e50;
}

/* Styles pour les exercices de TD */
.td-section {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(41, 128, 185, 0.05));
    border-radius: 20px;
    padding: 2rem;
    margin: 3rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
}

.td-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #2980b9;
    margin-bottom: 2rem;
    text-align: center;
}

.exercise-container {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #3498db;
}

.exercise-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.exercise-icon {
    font-size: 2rem;
    margin-right: 1rem;
}

.exercise-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2980b9;
}

.exercise-content {
    color: #2c3e50;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.scenario-box {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f39c12;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.scenario-title {
    font-weight: 600;
    color: #e67e22;
    margin-bottom: 1rem;
}

.calculation-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.calculation-table th {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.calculation-table td {
    padding: 1rem;
    border-bottom: 1px solid #ecf0f1;
}

.calculation-table tr:nth-child(even) {
    background: rgba(52, 152, 219, 0.05);
}

.solution-box {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #27ae60;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.solution-title {
    font-weight: 600;
    color: #27ae60;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

.solution-title::before {
    content: "✓";
    margin-right: 0.5rem;
    font-size: 1.2rem;
}

.formula-box {
    background: rgba(155, 89, 182, 0.1);
    border: 2px solid #9b59b6;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    text-align: center;
    font-family: 'Courier New', monospace;
    font-weight: 600;
    color: #8e44ad;
}

.risk-level-indicator {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9rem;
    margin: 0.2rem;
}

.risk-level-low {
    background: rgba(46, 204, 113, 0.2);
    color: #27ae60;
    border: 1px solid #27ae60;
}

.risk-level-medium {
    background: rgba(241, 196, 15, 0.2);
    color: #f39c12;
    border: 1px solid #f39c12;
}

.risk-level-high {
    background: rgba(231, 76, 60, 0.2);
    color: #e74c3c;
    border: 1px solid #e74c3c;
}

.risk-level-critical {
    background: rgba(142, 68, 173, 0.2);
    color: #8e44ad;
    border: 1px solid #8e44ad;
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
}

.exercise-tab {
    background: none;
    border: none;
    padding: 1rem 1.5rem;
    cursor: pointer;
    font-weight: 600;
    color: #7f8c8d;
    border-bottom: 3px solid transparent;
    transition: all 0.3s ease;
    white-space: nowrap;
    min-width: 150px;
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
</style>

<div class="course-header">
    <h1 class="course-title">⚠️ Gestion des Risques</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Gestion des risques en projet informatique</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Fondamentaux de la Gestion des Risques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Qu'est-ce qu'un Risque Projet ?</div>
        <div class="definition-content">
            Un risque projet est un <strong>événement incertain</strong> qui, s'il se produit, peut avoir un <strong>impact positif ou négatif</strong> sur les objectifs du projet (délais, coûts, qualité, périmètre). La gestion des risques consiste à les <strong>identifier</strong>, les <strong>analyser</strong>, les <strong>traiter</strong> et les <strong>surveiller</strong>.
        </div>
    </div>
    
    <div class="content-text">
        En gestion de projet informatique, la gestion des risques est cruciale pour anticiper les problèmes et assurer le succès des projets. Elle démontre la maturité professionnelle et la capacité à gérer l'incertitude dans un environnement technologique complexe.
    </div>
    
    <div class="process-flow">
        <div class="flow-steps">
            <div class="flow-step">
                <div class="flow-step-number">1</div>
                <div class="flow-step-title">Identification</div>
                <div>Détecter les risques potentiels</div>
            </div>
            <div class="flow-arrow">→</div>
            <div class="flow-step">
                <div class="flow-step-number">2</div>
                <div class="flow-step-title">Analyse</div>
                <div>Évaluer probabilité et impact</div>
            </div>
            <div class="flow-arrow">→</div>
            <div class="flow-step">
                <div class="flow-step-number">3</div>
                <div class="flow-step-title">Traitement</div>
                <div>Définir les stratégies</div>
            </div>
            <div class="flow-arrow">→</div>
            <div class="flow-step">
                <div class="flow-step-number">4</div>
                <div class="flow-step-title">Surveillance</div>
                <div>Suivre et contrôler</div>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Matrice des Risques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Évaluation Probabilité × Impact</div>
        <div class="definition-content">
            La matrice des risques permet de <strong>prioriser</strong> les risques en croisant leur <strong>probabilité d'occurrence</strong> avec leur <strong>impact</strong> sur le projet. Cette visualisation aide à concentrer les efforts sur les risques les plus critiques.
        </div>
    </div>
    
    <div class="risk-matrix">
        <div class="matrix-grid">
            <div class="matrix-header">Impact →<br>Probabilité ↓</div>
            <div class="matrix-header">Très Faible</div>
            <div class="matrix-header">Faible</div>
            <div class="matrix-header">Moyen</div>
            <div class="matrix-header">Fort</div>
            <div class="matrix-header">Très Fort</div>
            
            <div class="matrix-label">Très Forte (5)</div>
            <div class="matrix-cell risk-medium">Moyen</div>
            <div class="matrix-cell risk-high">Élevé</div>
            <div class="matrix-cell risk-high">Élevé</div>
            <div class="matrix-cell risk-critical">Critique</div>
            <div class="matrix-cell risk-critical">Critique</div>
            
            <div class="matrix-label">Forte (4)</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-medium">Moyen</div>
            <div class="matrix-cell risk-high">Élevé</div>
            <div class="matrix-cell risk-high">Élevé</div>
            <div class="matrix-cell risk-critical">Critique</div>
            
            <div class="matrix-label">Moyenne (3)</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-medium">Moyen</div>
            <div class="matrix-cell risk-high">Élevé</div>
            <div class="matrix-cell risk-high">Élevé</div>
            
            <div class="matrix-label">Faible (2)</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-medium">Moyen</div>
            <div class="matrix-cell risk-high">Élevé</div>
            
            <div class="matrix-label">Très Faible (1)</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-low">Faible</div>
            <div class="matrix-cell risk-medium">Moyen</div>
        </div>
    </div>
    
    <div class="probability-scale">
        <div class="probability-item prob-1">
            <div>1 - Très Faible</div>
            <div>< 10%</div>
        </div>
        <div class="probability-item prob-2">
            <div>2 - Faible</div>
            <div>10-30%</div>
        </div>
        <div class="probability-item prob-3">
            <div>3 - Moyenne</div>
            <div>30-50%</div>
        </div>
        <div class="probability-item prob-4">
            <div>4 - Forte</div>
            <div>50-70%</div>
        </div>
        <div class="probability-item prob-5">
            <div>5 - Très Forte</div>
            <div>> 70%</div>
        </div>
    </div>
</div>

<div class="td-section">
    <h2 class="td-title">📝 Travaux Dirigés : Calcul de Risques</h2>
    
    <div class="exercise-navigation">
        <div class="exercise-tabs">
            <button class="exercise-tab active" onclick="showExercise(1)">
                🎯 Exercice 1 - E-commerce
            </button>
            <button class="exercise-tab" onclick="showExercise(2)">
                📱 Exercice 2 - App Mobile
            </button>
            <button class="exercise-tab" onclick="showExercise(3)">
                🌐 Exercice 3 - Site Web
            </button>
        </div>
        
        <div id="exercise1" class="exercise-content-wrapper active">
            <div class="exercise-summary">
                <strong>Contexte :</strong> Développement d'une plateforme e-commerce (6 mois, 150k€, 8 développeurs)
            </div>
            <div class="exercise-container">
        <div class="exercise-header">
            <div class="exercise-icon">🎯</div>
            <div class="exercise-title">Exercice 1 : Évaluation de Risques Projet E-commerce</div>
        </div>
        
        <div class="exercise-content">
            Vous êtes chef de projet pour le développement d'une plateforme e-commerce. Analysez les risques suivants et calculez leur criticité.
        </div>
        
        <div class="scenario-box">
            <div class="scenario-title">📋 Contexte du projet :</div>
            <ul>
                <li><strong>Durée :</strong> 6 mois</li>
                <li><strong>Budget :</strong> 150 000 €</li>
                <li><strong>Équipe :</strong> 8 développeurs</li>
                <li><strong>Deadline :</strong> Lancement pour les fêtes de fin d'année</li>
            </ul>
        </div>
        
        <table class="calculation-table">
            <thead>
                <tr>
                    <th>Risque Identifié</th>
                    <th>Probabilité (1-5)</th>
                    <th>Impact (1-5)</th>
                    <th>Criticité</th>
                    <th>Niveau</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Retard de livraison des API externes</td>
                    <td>3</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Départ d'un développeur senior</td>
                    <td>2</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Problème de performance sous charge</td>
                    <td>4</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Changement des exigences client</td>
                    <td>4</td>
                    <td>3</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Faille de sécurité découverte</td>
                    <td>2</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
            </tbody>
        </table>
        
        <div class="formula-box">
            Criticité = Probabilité × Impact
        </div>
            </div>
        </div>
        
        <div id="exercise2" class="exercise-content-wrapper">
            <div class="exercise-summary">
                <strong>Contexte :</strong> Application mobile de gestion de tâches (4 mois, 80k€, équipe mixte)
            </div>
            <div class="exercise-container">
        <div class="exercise-header">
            <div class="exercise-icon">📱</div>
            <div class="exercise-title">Exercice 2 : Évaluation de Risques Application Mobile</div>
        </div>
        
        <div class="exercise-content">
            Vous dirigez le développement d'une application mobile de gestion de tâches pour une startup. Évaluez les risques suivants et calculez leur criticité.
        </div>
        
        <div class="scenario-box">
            <div class="scenario-title">📋 Contexte du projet :</div>
            <ul>
                <li><strong>Durée :</strong> 4 mois</li>
                <li><strong>Budget :</strong> 80 000 €</li>
                <li><strong>Équipe :</strong> 5 développeurs (3 juniors, 2 seniors)</li>
                <li><strong>Plateformes :</strong> iOS et Android</li>
                <li><strong>Objectif :</strong> 10 000 utilisateurs en 6 mois</li>
            </ul>
        </div>
        
        <table class="calculation-table">
            <thead>
                <tr>
                    <th>Risque Identifié</th>
                    <th>Probabilité (1-5)</th>
                    <th>Impact (1-5)</th>
                    <th>Criticité</th>
                    <th>Niveau</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Rejet de l'app par l'App Store</td>
                    <td>2</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Problèmes de compatibilité entre versions iOS/Android</td>
                    <td>4</td>
                    <td>3</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Manque d'expérience de l'équipe en développement mobile</td>
                    <td>3</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Changement des guidelines des stores</td>
                    <td>3</td>
                    <td>3</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Problèmes de performance sur anciens appareils</td>
                    <td>4</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Concurrence avec une app similaire lancée avant</td>
                    <td>3</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
            </tbody>
        </table>
        
        <div class="formula-box">
            Criticité = Probabilité × Impact
        </div>
            </div>
        </div>
        
        <div id="exercise3" class="exercise-content-wrapper">
            <div class="exercise-summary">
                <strong>Contexte :</strong> Refonte site web universitaire (8 mois, 200k€, 25k utilisateurs)
            </div>
            <div class="exercise-container">
        <div class="exercise-header">
            <div class="exercise-icon">🌐</div>
            <div class="exercise-title">Exercice 3 : Évaluation de Risques Site Web Institutionnel</div>
        </div>
        
        <div class="exercise-content">
            Vous êtes responsable de la refonte du site web d'une université. Analysez les risques suivants et calculez leur criticité.
        </div>
        
        <div class="scenario-box">
            <div class="scenario-title">📋 Contexte du projet :</div>
            <ul>
                <li><strong>Durée :</strong> 8 mois</li>
                <li><strong>Budget :</strong> 200 000 €</li>
                <li><strong>Équipe :</strong> 6 développeurs + 2 designers</li>
                <li><strong>Utilisateurs :</strong> 25 000 étudiants et 2 000 enseignants</li>
                <li><strong>Contrainte :</strong> Mise en ligne avant la rentrée</li>
            </ul>
        </div>
        
        <table class="calculation-table">
            <thead>
                <tr>
                    <th>Risque Identifié</th>
                    <th>Probabilité (1-5)</th>
                    <th>Impact (1-5)</th>
                    <th>Criticité</th>
                    <th>Niveau</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Retard dans la migration des données existantes</td>
                    <td>3</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Non-conformité aux normes d'accessibilité</td>
                    <td>2</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Surcharge du serveur lors de la rentrée</td>
                    <td>4</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Résistance au changement des utilisateurs</td>
                    <td>4</td>
                    <td>2</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Problèmes d'intégration avec le système d'information</td>
                    <td>3</td>
                    <td>4</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
                <tr>
                    <td>Attaque de sécurité pendant la migration</td>
                    <td>2</td>
                    <td>5</td>
                    <td>?</td>
                    <td>?</td>
                </tr>
            </tbody>
        </table>
        
        <div class="formula-box">
            Criticité = Probabilité × Impact
        </div>
            </div>
        </div>
    </div>
</div>

<script>
function showExercise(exerciseNumber) {
    // Masquer tous les exercices en retirant la classe active
    const exercises = document.querySelectorAll('.exercise-content-wrapper');
    exercises.forEach(ex => ex.classList.remove('active'));
    
    // Retirer la classe active de tous les onglets
    const tabs = document.querySelectorAll('.exercise-tab');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher l'exercice sélectionné en ajoutant la classe active
    const selectedExercise = document.getElementById('exercise' + exerciseNumber);
    if (selectedExercise) {
        selectedExercise.classList.add('active');
    }
    
    // Activer l'onglet correspondant
    const selectedTab = document.querySelector(`[onclick="showExercise(${exerciseNumber})"]`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
}

// Afficher l'exercice 1 par défaut
document.addEventListener('DOMContentLoaded', function() {
    showExercise(1);
});
</script>

<div class="concept-section">
    <h2 class="section-title">🚨 Risques Typiques en Projet Informatique</h2>
    
    <div class="risk-grid">
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">💻</div>
                <div>
                    <div class="risk-name">Risques Techniques</div>
                    <div class="risk-level risk-high">Élevé</div>
                </div>
            </div>
            <div class="risk-description">
                Problèmes liés aux technologies, architectures ou compétences techniques de l'équipe.
            </div>
            <ul class="risk-impacts">
                <li>Choix technologique inadapté</li>
                <li>Complexité sous-estimée</li>
                <li>Manque de compétences</li>
                <li>Problèmes d'intégration</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Prototypage précoce<br>
                • Formation de l'équipe<br>
                • Revues techniques régulières<br>
                • Architecture modulaire
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">📅</div>
                <div>
                    <div class="risk-name">Risques Planning</div>
                    <div class="risk-level risk-high">Élevé</div>
                </div>
            </div>
            <div class="risk-description">
                Dépassements de délais dus à une mauvaise estimation ou à des imprévus.
            </div>
            <ul class="risk-impacts">
                <li>Estimations optimistes</li>
                <li>Dépendances non identifiées</li>
                <li>Scope creep</li>
                <li>Ressources indisponibles</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Estimation par analogie<br>
                • Buffers de sécurité<br>
                • Jalons intermédiaires<br>
                • Gestion du périmètre
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">👥</div>
                <div>
                    <div class="risk-name">Risques Humains</div>
                    <div class="risk-level risk-medium">Moyen</div>
                </div>
            </div>
            <div class="risk-description">
                Problèmes liés à l'équipe, la communication ou la motivation.
            </div>
            <ul class="risk-impacts">
                <li>Départ d'un membre clé</li>
                <li>Conflits dans l'équipe</li>
                <li>Manque de motivation</li>
                <li>Communication défaillante</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Documentation du savoir<br>
                • Team building<br>
                • Communication régulière<br>
                • Reconnaissance des efforts
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🔒</div>
                <div>
                    <div class="risk-name">Risques Sécurité</div>
                    <div class="risk-level risk-critical">Critique</div>
                </div>
            </div>
            <div class="risk-description">
                Vulnérabilités de sécurité pouvant compromettre le système ou les données.
            </div>
            <ul class="risk-impacts">
                <li>Failles de sécurité</li>
                <li>Perte de données</li>
                <li>Accès non autorisés</li>
                <li>Non-conformité RGPD</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Audit de sécurité<br>
                • Tests de pénétration<br>
                • Chiffrement des données<br>
                • Formation sécurité
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">💰</div>
                <div>
                    <div class="risk-name">Risques Budgétaires</div>
                    <div class="risk-level risk-medium">Moyen</div>
                </div>
            </div>
            <div class="risk-description">
                Dépassements de coûts ou contraintes budgétaires impactant le projet.
            </div>
            <ul class="risk-impacts">
                <li>Coûts sous-estimés</li>
                <li>Licences logicielles</li>
                <li>Infrastructure cloud</li>
                <li>Ressources externes</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Estimation détaillée<br>
                • Suivi des coûts<br>
                • Solutions alternatives<br>
                • Négociation fournisseurs
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🏢</div>
                <div>
                    <div class="risk-name">Risques Organisationnels</div>
                    <div class="risk-level risk-medium">Moyen</div>
                </div>
            </div>
            <div class="risk-description">
                Changements dans l'organisation ou les priorités affectant le projet.
            </div>
            <ul class="risk-impacts">
                <li>Changement de sponsor</li>
                <li>Réorganisation</li>
                <li>Nouvelles priorités</li>
                <li>Changement de stratégie</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Stratégies de mitigation :</div>
                • Engagement des parties prenantes<br>
                • Communication régulière<br>
                • Flexibilité du projet<br>
                • Valeur business claire
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛡️ Stratégies de Traitement des Risques</h2>
    
    <div class="risk-grid">
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🚫</div>
                <div>
                    <div class="risk-name">Évitement</div>
                    <div class="risk-level risk-low">Préventif</div>
                </div>
            </div>
            <div class="risk-description">
                Éliminer complètement le risque en modifiant le plan de projet ou en changeant d'approche.
            </div>
            <ul class="risk-impacts">
                <li>Changer de technologie</li>
                <li>Modifier le périmètre</li>
                <li>Choisir un autre fournisseur</li>
                <li>Simplifier l'architecture</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Exemple pratique :</div>
                Éviter l'utilisation d'une technologie expérimentale en choisissant une solution éprouvée.
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🔄</div>
                <div>
                    <div class="risk-name">Transfert</div>
                    <div class="risk-level risk-medium">Délégation</div>
                </div>
            </div>
            <div class="risk-description">
                Transférer la responsabilité du risque à une tierce partie (assurance, sous-traitant, etc.).
            </div>
            <ul class="risk-impacts">
                <li>Sous-traitance spécialisée</li>
                <li>Assurance projet</li>
                <li>Garanties fournisseur</li>
                <li>Contrats de service</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Exemple pratique :</div>
                Utiliser un service cloud managé pour transférer les risques d'infrastructure.
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🛠️</div>
                <div>
                    <div class="risk-name">Atténuation</div>
                    <div class="risk-level risk-high">Réduction</div>
                </div>
            </div>
            <div class="risk-description">
                Réduire la probabilité d'occurrence ou l'impact du risque par des actions préventives.
            </div>
            <ul class="risk-impacts">
                <li>Formation de l'équipe</li>
                <li>Tests supplémentaires</li>
                <li>Prototypage</li>
                <li>Revues de code</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Exemple pratique :</div>
                Mettre en place des tests automatisés pour réduire le risque de bugs en production.
            </div>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">✅</div>
                <div>
                    <div class="risk-name">Acceptation</div>
                    <div class="risk-level risk-low">Surveillance</div>
                </div>
            </div>
            <div class="risk-description">
                Accepter le risque en connaissance de cause et prévoir des plans de contingence.
            </div>
            <ul class="risk-impacts">
                <li>Surveillance active</li>
                <li>Plans de contingence</li>
                <li>Budgets de réserve</li>
                <li>Escalade définie</li>
            </ul>
            <div class="mitigation-box">
                <div class="mitigation-title">Exemple pratique :</div>
                Accepter le risque de retard mineur et prévoir un buffer dans le planning.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 Outils et Techniques</h2>
    
    <div class="risk-grid">
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🧠</div>
                <div>
                    <div class="risk-name">Brainstorming</div>
                </div>
            </div>
            <div class="risk-description">
                Session créative pour identifier les risques avec toute l'équipe.
            </div>
            <ul class="risk-impacts">
                <li>Diversité des perspectives</li>
                <li>Créativité collective</li>
                <li>Engagement de l'équipe</li>
                <li>Identification exhaustive</li>
            </ul>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🎯</div>
                <div>
                    <div class="risk-name">Analyse SWOT</div>
                </div>
            </div>
            <div class="risk-description">
                Analyse des Forces, Faiblesses, Opportunités et Menaces du projet.
            </div>
            <ul class="risk-impacts">
                <li>Vision globale du projet</li>
                <li>Identification des menaces</li>
                <li>Opportunités à saisir</li>
                <li>Analyse structurée</li>
            </ul>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">🔍</div>
                <div>
                    <div class="risk-name">Analyse des Causes</div>
                </div>
            </div>
            <div class="risk-description">
                Technique des "5 Pourquoi" pour identifier les causes racines des risques.
            </div>
            <ul class="risk-impacts">
                <li>Identification des causes profondes</li>
                <li>Prévention efficace</li>
                <li>Solutions durables</li>
                <li>Apprentissage organisationnel</li>
            </ul>
        </div>
        
        <div class="risk-card">
            <div class="risk-header">
                <div class="risk-icon">📈</div>
                <div>
                    <div class="risk-name">Simulation Monte Carlo</div>
                </div>
            </div>
            <div class="risk-description">
                Modélisation probabiliste pour évaluer l'impact cumulé des risques.
            </div>
            <ul class="risk-impacts">
                <li>Analyse quantitative</li>
                <li>Scénarios multiples</li>
                <li>Probabilités d'occurrence</li>
                <li>Aide à la décision</li>
            </ul>
        </div>
    </div>
</div>