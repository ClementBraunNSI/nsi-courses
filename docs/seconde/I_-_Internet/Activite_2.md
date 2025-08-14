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

.step-container {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.step-title {
    color: #667eea;
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.step-number {
    background: #667eea;
    color: white;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 1.2rem;
}

.instruction-list {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.instruction-item {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid #667eea;
    transition: all 0.3s ease;
}

.instruction-item:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.instruction-number {
    color: #667eea;
    font-weight: bold;
    margin-right: 0.5rem;
}

.network-info {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #2c3e50;
}

.question-box {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(139, 195, 74, 0.05));
    border-left: 5px solid #4caf50;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.question-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    font-weight: 500;
}

.link-style {
    color: #667eea;
    text-decoration: underline;
    font-weight: bold;
}

@media (max-width: 768px) {
    .step-title {
        flex-direction: column;
        text-align: center;
    }
}
</style>

<div class="activity-section">
    <div class="activity-header">
        <h1 class="activity-title">🌐 Simulation de Serveurs WEB et DNS</h1>
        <p class="activity-description">
            Après avoir appris à créer un réseau d'ordinateurs et à gérer le routage, 
            nous allons maintenant explorer les serveurs WEB et DNS qui constituent le cœur d'Internet.
        </p>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Objectif de l'activité</div>
        <div class="definition-content">
            Comprendre le fonctionnement des <strong>serveurs WEB</strong> et <strong>DNS</strong> en simulant 
            un environnement réseau complet avec Filius.
        </div>
    </div>
    
    <div class="step-container">
        <h2 class="step-title">
            <span class="step-number">1</span>
            🔧 Création du réseau
        </h2>
        
        <div class="instruction-list">
            <div class="instruction-item">
                📋 <strong>Prérequis :</strong> Reprendre le réseau du TP précédent comme base de travail
            </div>
        </div>
    </div>
    
    <div class="step-container">
        <h2 class="step-title">
            <span class="step-number">2</span>
            🖥️ Configuration d'un serveur WEB
        </h2>
        
        <div class="instruction-list">
            <div class="instruction-item">
                <span class="instruction-number">2.1</span>
                Ajouter un ordinateur dans le réseau <span class="network-info">192.168.5.0</span> et le configurer pour y avoir accès
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">2.2</span>
                En mode lecture, ajouter le <strong>logiciel de serveur web</strong> sur l'ordinateur
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">2.3</span>
                Double-cliquer sur l'application serveur web et <strong>démarrer le serveur</strong>
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">2.4</span>
                Sur la machine <span class="network-info">192.168.1.11</span>, ajouter le logiciel de navigation internet et 
                entrer l'adresse IP du serveur web dans la barre d'adresse. La page devrait s'actualiser.
            </div>
        </div>
    </div>
    
    <div class="step-container">
        <h2 class="step-title">
            <span class="step-number">3</span>
            🌐 Configuration d'un serveur DNS
        </h2>
        
        <div class="highlight-fact">
            💡 <strong>Préparation :</strong> Ajouter une interface au routeur et créer un réseau <span class="network-info">192.168.2.11</span> avec un ordinateur
        </div>
        
        <div class="instruction-list">
            <div class="instruction-item">
                <span class="instruction-number">3.1</span>
                Sur la machine <span class="network-info">192.168.2.11</span>, ajouter l'application <strong>serveur DNS</strong> et l'ouvrir
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">3.2</span>
                Comme nom de domaine, ajouter <a href="http://www.nsi.fr" class="link-style">www.nsi.fr</a> 
                et associer l'adresse <span class="network-info">192.168.3.12</span> (notre serveur WEB)
            </div>
        </div>
        
        <div class="question-box">
            <div class="question-content">
                ❓ <strong>Question 3.3 :</strong> Est-il possible d'accéder à la page <a href="http://www.nsi.fr" class="link-style">www.nsi.fr</a> ?
            </div>
        </div>
        
        <div class="instruction-list">
            <div class="instruction-item">
                <span class="instruction-number">3.4</span>
                Ajouter l'adresse du serveur DNS pour tous les ordinateurs
            </div>
        </div>
        
        <div class="question-box">
            <div class="question-content">
                ❓ <strong>Question finale :</strong> Est-il maintenant possible d'accéder à la page ?
            </div>
        </div>
    </div>
    
    <div class="step-container">
        <h2 class="step-title">
            <span class="step-number">4</span>
            📄 Ajout de votre page web personnalisée
        </h2>
        
        <div class="instruction-list">
            <div class="instruction-item">
                <span class="instruction-number">4.1</span>
                Sur le serveur WEB, ajouter l'application <strong>explorateur de fichiers</strong>
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">4.2</span>
                Importer votre fichier <span class="network-info">index.html</span> et le placer dans le dossier <strong>webserver</strong>
            </div>
            
            <div class="instruction-item">
                <span class="instruction-number">4.3</span>
                Actualiser et tester l'accès à votre page depuis la machine <span class="network-info">192.168.1.10</span>
            </div>
        </div>
        
        <div class="highlight-fact">
            🎉 <strong>Résultat attendu :</strong> Votre page web personnalisée devrait maintenant être accessible via le nom de domaine configuré !
        </div>
    </div>
</div>


