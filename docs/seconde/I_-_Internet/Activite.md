<style>
.activity-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.activity-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.activity-title {
    color: #667eea;
    font-size: 2rem;
    margin-bottom: 1rem;
    font-weight: bold;
}

.activity-description {
    color: #7f8c8d;
    font-size: 1.1rem;
    line-height: 1.6;
}

.section-container {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.section-title {
    color: #667eea;
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.mode-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.mode-card {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
    text-align: center;
}

.mode-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
}

.mode-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.mode-title {
    color: #667eea;
    font-weight: bold;
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.mode-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.4;
}

.image-container {
    text-align: center;
    margin: 2rem 0;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.question-list {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.question-item {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(139, 195, 74, 0.05));
    border-left: 4px solid #4caf50;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    transition: all 0.3s ease;
}

.question-item:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}

.question-number {
    color: #4caf50;
    font-weight: bold;
    margin-right: 0.5rem;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.05));
    border-left: 5px solid #ffc107;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.definition-box {
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.1), rgba(233, 30, 99, 0.05));
    border-left: 5px solid #9c27b0;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    color: #9c27b0;
    font-weight: bold;
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    line-height: 1.6;
}

@media (max-width: 768px) {
    .mode-grid {
        grid-template-columns: 1fr;
    }
}
</style>

<div class="activity-section">
    <div class="activity-header">
        <h1 class="activity-title">🌐 Simulation d'un Réseau Informatique</h1>
        <p class="activity-description">
            Découvrez la construction et le fonctionnement des réseaux informatiques grâce au logiciel 
            <strong>Filius</strong>, un simulateur puissant pour comprendre les échanges de données.
        </p>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Objectif de l'activité</div>
        <div class="definition-content">
            Maîtriser la création de <strong>réseaux</strong> et <strong>sous-réseaux</strong> en simulant 
            le comportement des paquets de données avec le logiciel Filius.
        </div>
    </div>
    
    <div class="section-container">
        <h2 class="section-title">
            🔧 Approche du logiciel Filius
        </h2>
        
        <div class="image-container">
            <img src="../img/notice_filius.png" alt="Interface Filius" />
        </div>
        
        <div class="highlight-fact">
            💡 <strong>Le logiciel Filius possède 3 modes de fonctionnement :</strong>
        </div>
        
        <div class="image-container">
            <img src="../img/modes_filius.png" alt="Modes Filius" />
        </div>
        
        <div class="mode-grid">
            <div class="mode-card">
                <div class="mode-icon">✏️</div>
                <div class="mode-title">Annotation</div>
                <div class="mode-description">
                    Permet d'annoter le schéma réseau pour une meilleure compréhension
                </div>
            </div>
            
            <div class="mode-card">
                <div class="mode-icon">🔨</div>
                <div class="mode-title">Construction</div>
                <div class="mode-description">
                    Permet d'ajouter des éléments (ordinateurs, routeurs, câbles) sur le schéma
                </div>
            </div>
            
            <div class="mode-card">
                <div class="mode-icon">▶️</div>
                <div class="mode-title">Lecture</div>
                <div class="mode-description">
                    Permet d'utiliser la simulation pour étudier les échanges de données en temps réel
                </div>
            </div>
        </div>
    </div>
    
    <div class="section-container">
        <h2 class="section-title">
            🏗️ Construction d'un réseau simple
        </h2>
        
        <div class="image-container">
            <img src="../img/s1.png" alt="Schéma réseau simple" />
        </div>
        
        <div class="question-list">
            <div class="question-item">
                <span class="question-number">1.</span>
                Quels sont les éléments de ce réseau ?
            </div>
            
            <div class="question-item">
                <span class="question-number">2.</span>
                À quoi sert le routeur dans cette configuration ?
            </div>
            
            <div class="question-item">
                <span class="question-number">3.</span>
                Dans quels réseaux sont les ordinateurs 1 et 2 ? 
                <br><em>(Indication : pour les 2 réseaux, la partie réseau est définie sur 3 octets)</em>
            </div>
        </div>
    </div>
    
    <div class="section-container">
        <h2 class="section-title">
            🚀 Un réseau plus étoffé
        </h2>
        
        <div class="highlight-fact">
            📈 <strong>Évolution :</strong> Après avoir compris le fonctionnement de base de Filius, 
            nous allons maintenant étoffer le réseau précédent pour une configuration plus complexe.
        </div>
        
        <div class="image-container">
            <img src="../img/s2.png" alt="Schéma réseau étoffé" />
        </div>
        
        <div class="question-list">
            <div class="question-item">
                <span class="question-number">1.</span>
                À quelle propriété du routeur faut-il veiller pour réaliser ce schéma ?
            </div>
            
            <div class="question-item">
                <span class="question-number">2.</span>
                Réaliser le schéma ci-dessus en utilisant le mode construction de Filius.
            </div>
        </div>
        
        <div class="definition-box">
            <div class="definition-title">🎯 Objectif pratique</div>
            <div class="definition-content">
                Cette activité vous permettra de comprendre concrètement comment les <strong>routeurs</strong> 
                interconnectent différents réseaux et gèrent le routage des paquets de données.
            </div>
        </div>
    </div>
</div>