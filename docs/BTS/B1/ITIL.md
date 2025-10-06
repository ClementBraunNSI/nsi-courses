<style>
/* Styles modernes pour le cours ITIL */
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
    color: #8e44ad;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
    color: var(--md-default-fg-color);
    text-align: center;
    line-height: 1.5;
}

.dimension-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.dimension-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 20px;
    padding: 2rem;
    border: 2px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
}

.dimension-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(155, 89, 182, 0.2);
}

.dimension-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 1rem;
    text-align: center;
}

.dimension-description {
    color: var(--md-default-fg-color);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.dimension-features {
    list-style: none;
    padding: 0;
}

.dimension-features li {
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(155, 89, 182, 0.1);
}

.dimension-features li:before {
    content: "🔹 ";
    color: #8e44ad;
    font-weight: bold;
}

.svs-diagram {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
}

.svs-component {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem;
    border: 2px solid rgba(155, 89, 182, 0.3);
    display: inline-block;
    min-width: 200px;
}

.svs-title {
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 0.5rem;
}

.value-chain {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    overflow-x: auto;
}

.chain-activity {
    text-align: center;
    flex: 1;
    min-width: 150px;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    padding: 1rem;
    margin: 0 0.5rem;
    border: 2px solid rgba(155, 89, 182, 0.2);
}

.chain-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.chain-name {
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 0.5rem;
}

.chain-description {
    font-size: 0.9rem;
    color: #7f8c8d;
}

.practice-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.practice-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
}

.practice-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.practice-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.practice-icon {
    font-size: 2.5rem;
    margin-right: 1rem;
}

.practice-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #8e44ad;
}

.practice-description {
    color: var(--md-default-fg-color);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.practice-objectives {
    list-style: none;
    padding: 0;
}

.practice-objectives li {
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(155, 89, 182, 0.1);
}

.practice-objectives li:before {
    content: "✅ ";
    color: #8e44ad;
    font-weight: bold;
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

.exercise-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.1));
    border: 2px solid rgba(155, 89, 182, 0.3);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
}

.exercise-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #8e44ad;
    margin-bottom: 1rem;
    text-align: center;
}

.exercise-content {
    color: var(--md-default-fg-color);
    line-height: 1.6;
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

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid, .dimension-grid, .practice-grid {
        grid-template-columns: 1fr;
    }
    
    .value-chain {
        flex-direction: column;
        gap: 1rem;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🔧 ITIL v4 : Gestion des Services IT</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Gestion des services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Fondamentaux d'ITIL</h2>
    
    <div class="definition-box">
        <div class="definition-title">📚 Qu'est-ce qu'ITIL ?</div>
        <div class="definition-content">
            <strong>ITIL (Information Technology Infrastructure Library)</strong> est un référentiel de bonnes pratiques pour la gestion des services informatiques (ITSM). ITIL v4, lancé en 2019, se concentre sur la <strong>création de valeur</strong> pour les clients et l'organisation à travers des services IT efficaces et adaptés aux besoins métier.
        </div>
    </div>
    
    <div class="content-text">
        En entreprise, ITIL permet d'aligner les services IT sur les objectifs business, d'améliorer la satisfaction client et d'optimiser les coûts. Pour un technicien BTS SIO, maîtriser ITIL est essentiel pour comprendre comment organiser et gérer efficacement les services informatiques.
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">💼</div>
            <div class="concept-name">Valeur Métier</div>
            <div class="concept-description">
                Aligner les services IT sur les besoins business et créer de la valeur pour l'organisation.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Amélioration Continue</div>
            <div class="concept-description">
                Optimiser constamment les processus et services pour une meilleure efficacité.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">👥</div>
            <div class="concept-name">Collaboration</div>
            <div class="concept-description">
                Favoriser la coopération entre équipes IT et métier pour atteindre les objectifs communs.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Approche Holistique</div>
            <div class="concept-description">
                Vision globale intégrant personnes, processus, partenaires et technologies.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Évolution d'ITIL :</strong> ITIL v4 abandonne l'approche rigide des processus v3 pour adopter une vision plus flexible centrée sur la valeur et l'agilité.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌐 Les 4 Dimensions d'ITIL v4</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Vision Holistique</div>
        <div class="definition-content">
            ITIL v4 considère que tout service doit être analysé selon <strong>4 dimensions</strong> pour assurer sa réussite. Ces dimensions sont interdépendantes et doivent être équilibrées pour créer de la valeur.
        </div>
    </div>
    
    <div class="dimension-grid">
        <div class="dimension-card">
            <div class="dimension-title">👥 Organisations et Personnes</div>
            <div class="dimension-description">
                Cette dimension concerne la culture, les compétences, les rôles et responsabilités nécessaires pour gérer efficacement les services.
            </div>
            <ul class="dimension-features">
                <li>Structure organisationnelle et gouvernance</li>
                <li>Compétences et formations des équipes</li>
                <li>Culture d'entreprise et collaboration</li>
                <li>Gestion des talents et motivation</li>
                <li>Communication et leadership</li>
            </ul>
        </div>
        
        <div class="dimension-card">
            <div class="dimension-title">📋 Information et Technologie</div>
            <div class="dimension-description">
                Englobe les technologies, outils, systèmes d'information et données nécessaires à la fourniture des services.
            </div>
            <ul class="dimension-features">
                <li>Infrastructure IT et cloud computing</li>
                <li>Applications et logiciels métier</li>
                <li>Bases de données et gestion des données</li>
                <li>Outils de monitoring et d'automatisation</li>
                <li>Sécurité et protection des informations</li>
            </ul>
        </div>
        
        <div class="dimension-card">
            <div class="dimension-title">🤝 Partenaires et Fournisseurs</div>
            <div class="dimension-description">
                Gestion des relations avec les partenaires externes, fournisseurs et prestataires de services.
            </div>
            <ul class="dimension-features">
                <li>Stratégie de sourcing et contrats</li>
                <li>Gestion des fournisseurs et SLA</li>
                <li>Intégration des services tiers</li>
                <li>Écosystème de partenaires</li>
                <li>Gestion des risques fournisseurs</li>
            </ul>
        </div>
        
        <div class="dimension-card">
            <div class="dimension-title">🔄 Flux de Valeur et Processus</div>
            <div class="dimension-description">
                Définit comment les activités et workflows sont organisés pour créer, livrer et supporter les services.
            </div>
            <ul class="dimension-features">
                <li>Cartographie des flux de valeur</li>
                <li>Processus et procédures standardisés</li>
                <li>Métriques et indicateurs de performance</li>
                <li>Amélioration continue des processus</li>
                <li>Automatisation et optimisation</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚙️ Système de Valeur des Services (SVS)</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏗️ Architecture ITIL v4</div>
        <div class="definition-content">
            Le <strong>Service Value System (SVS)</strong> est le modèle central d'ITIL v4 qui décrit comment tous les composants et activités de l'organisation travaillent ensemble pour faciliter la création de valeur.
        </div>
    </div>
    
    <div class="svs-diagram">
        <div class="svs-component">
            <div class="svs-title">🎯 Opportunité/Demande</div>
            <div>Besoins métier et demandes clients</div>
        </div>
        
        <div style="margin: 2rem 0; font-size: 2rem; color: #8e44ad;">↓</div>
        
        <div class="svs-component">
            <div class="svs-title">🧭 Principes Directeurs</div>
            <div>7 principes pour guider les décisions</div>
        </div>
        
        <div style="margin: 2rem 0; font-size: 2rem; color: #8e44ad;">↓</div>
        
        <div class="svs-component">
            <div class="svs-title">🔗 Chaîne de Valeur des Services</div>
            <div>6 activités clés interconnectées</div>
        </div>
        
        <div style="margin: 2rem 0; font-size: 2rem; color: #8e44ad;">↓</div>
        
        <div class="svs-component">
            <div class="svs-title">💎 Valeur</div>
            <div>Services et produits livrés</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🔄 <strong>Amélioration Continue :</strong> Le SVS intègre l'amélioration continue à tous les niveaux, permettant une adaptation constante aux besoins changeants.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔗 Chaîne de Valeur des Services</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚡ 6 Activités Clés</div>
        <div class="definition-content">
            La chaîne de valeur des services définit <strong>6 activités clés</strong> qui peuvent être combinées de manière flexible pour créer différents flux de valeur selon les besoins.
        </div>
    </div>
    
    <div class="value-chain">
        <div class="chain-activity">
            <div class="chain-icon">📋</div>
            <div class="chain-name">Planifier</div>
            <div class="chain-description">Vision partagée et amélioration continue</div>
        </div>
        
        <div class="chain-activity">
            <div class="chain-icon">🔄</div>
            <div class="chain-name">Améliorer</div>
            <div class="chain-description">Performance et conformité continues</div>
        </div>
        
        <div class="chain-activity">
            <div class="chain-icon">👥</div>
            <div class="chain-name">Engager</div>
            <div class="chain-description">Relations avec parties prenantes</div>
        </div>
        
        <div class="chain-activity">
            <div class="chain-icon">🎨</div>
            <div class="chain-name">Concevoir & Transitionner</div>
            <div class="chain-description">Nouveaux services et changements</div>
        </div>
        
        <div class="chain-activity">
            <div class="chain-icon">🛠️</div>
            <div class="chain-name">Obtenir/Construire</div>
            <div class="chain-description">Composants et services</div>
        </div>
        
        <div class="chain-activity">
            <div class="chain-icon">🚀</div>
            <div class="chain-name">Livrer & Supporter</div>
            <div class="chain-description">Services aux utilisateurs</div>
        </div>
    </div>
    
    <div class="content-text">
        Ces activités ne suivent pas un ordre séquentiel rigide mais peuvent être combinées selon les besoins spécifiques de chaque flux de valeur. Par exemple, un incident critique peut déclencher directement les activités "Engager" et "Livrer & Supporter".
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛠️ Pratiques ITIL Essentielles</h2>
    
    <div class="definition-box">
        <div class="definition-title">📚 34 Pratiques ITIL v4</div>
        <div class="definition-content">
            ITIL v4 définit <strong>34 pratiques</strong> organisées en 3 catégories. Voici les pratiques les plus importantes pour un technicien BTS SIO.
        </div>
    </div>
    
    <div class="practice-grid">
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">🚨</div>
                <div class="practice-title">Gestion des Incidents</div>
            </div>
            <div class="practice-description">
                Restaurer rapidement le service normal après une interruption non planifiée, minimisant l'impact sur les activités métier.
            </div>
            <ul class="practice-objectives">
                <li>Résolution rapide des incidents</li>
                <li>Communication transparente aux utilisateurs</li>
                <li>Escalade appropriée si nécessaire</li>
                <li>Documentation et analyse post-incident</li>
            </ul>
        </div>
        
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">🎫</div>
                <div class="practice-title">Gestion des Demandes de Service</div>
            </div>
            <div class="practice-description">
                Traiter les demandes des utilisateurs pour des services standard, informations ou conseils.
            </div>
            <ul class="practice-objectives">
                <li>Catalogue de services standardisé</li>
                <li>Processus d'approbation automatisé</li>
                <li>Délais de traitement définis</li>
                <li>Self-service pour les demandes courantes</li>
            </ul>
        </div>
        
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">🔄</div>
                <div class="practice-title">Contrôle des Changements</div>
            </div>
            <div class="practice-description">
                Gérer le cycle de vie des changements pour minimiser les risques et maximiser la réussite.
            </div>
            <ul class="practice-objectives">
                <li>Évaluation des risques et impacts</li>
                <li>Processus d'approbation structuré</li>
                <li>Planification et tests des changements</li>
                <li>Retour arrière en cas de problème</li>
            </ul>
        </div>
        
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">🔍</div>
                <div class="practice-title">Gestion des Problèmes</div>
            </div>
            <div class="practice-description">
                Identifier et traiter les causes racines des incidents pour éviter leur récurrence.
            </div>
            <ul class="practice-objectives">
                <li>Analyse des causes racines</li>
                <li>Solutions permanentes aux problèmes</li>
                <li>Prévention des incidents récurrents</li>
                <li>Base de connaissances enrichie</li>
            </ul>
        </div>
        
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">📊</div>
                <div class="practice-title">Gestion des Niveaux de Service</div>
            </div>
            <div class="practice-description">
                Définir, négocier et surveiller les niveaux de service convenus avec les clients.
            </div>
            <ul class="practice-objectives">
                <li>SLA (Service Level Agreement) clairs</li>
                <li>Métriques et indicateurs de performance</li>
                <li>Rapports réguliers aux clients</li>
                <li>Amélioration continue des services</li>
            </ul>
        </div>
        
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">📋</div>
                <div class="practice-title">Gestion de la Configuration</div>
            </div>
            <div class="practice-description">
                Maintenir des informations précises sur les éléments de configuration et leurs relations.
            </div>
            <ul class="practice-objectives">
                <li>CMDB (Configuration Management Database)</li>
                <li>Inventaire complet des actifs IT</li>
                <li>Relations et dépendances mappées</li>
                <li>Contrôle des versions et changements</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Comparaison ITIL v3 vs v4</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔄 Évolution Majeure</div>
        <div class="definition-content">
            ITIL v4 représente une évolution significative par rapport à v3, adoptant une approche plus flexible et centrée sur la valeur.
        </div>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Aspect</th>
                <th>ITIL v3</th>
                <th>ITIL v4</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Approche</strong></td>
                <td>Processus rigides et séquentiels</td>
                <td>Pratiques flexibles et adaptables</td>
            </tr>
            <tr>
                <td><strong>Focus</strong></td>
                <td>Gestion des processus IT</td>
                <td>Création de valeur pour le business</td>
            </tr>
            <tr>
                <td><strong>Structure</strong></td>
                <td>5 livres (Stratégie, Conception, Transition, Exploitation, Amélioration)</td>
                <td>Système de Valeur des Services (SVS)</td>
            </tr>
            <tr>
                <td><strong>Agilité</strong></td>
                <td>Approche traditionnelle</td>
                <td>Intégration DevOps, Agile, Lean</td>
            </tr>
            <tr>
                <td><strong>Gouvernance</strong></td>
                <td>Processus centralisés</td>
                <td>Principes directeurs et gouvernance adaptative</td>
            </tr>
            <tr>
                <td><strong>Amélioration</strong></td>
                <td>CSI (Amélioration Continue des Services)</td>
                <td>Amélioration continue intégrée partout</td>
            </tr>
        </tbody>
    </table>
    
    <div class="highlight-fact">
        🚀 <strong>Modernisation :</strong> ITIL v4 s'adapte aux nouvelles réalités du cloud, de l'automatisation et des méthodes agiles tout en conservant les bonnes pratiques éprouvées.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💼 Cas Pratiques BTS SIO</h2>
    
    <div class="exercise-box">
        <div class="exercise-title">🏢 Cas d'Étude : Entreprise TechSolutions</div>
        <div class="exercise-content">
            <div class="scenario-box">
                <div class="scenario-title">📋 Contexte</div>
                <div>
                    TechSolutions est une PME de 200 employés spécialisée dans le développement logiciel. L'entreprise fait face à des problèmes récurrents :
                    <ul>
                        <li>Incidents fréquents sur l'environnement de production</li>
                        <li>Demandes utilisateurs traitées de manière anarchique</li>
                        <li>Changements non contrôlés causant des pannes</li>
                        <li>Manque de visibilité sur les niveaux de service</li>
                    </ul>
                </div>
            </div>
            
            <div class="solution-box">
                <div class="solution-title">Mise en place d'ITIL</div>
                <div>
                    <strong>1. Gestion des Incidents :</strong>
                    <ul>
                        <li>Mise en place d'un outil de ticketing (ServiceNow, GLPI)</li>
                        <li>Classification des incidents par priorité (P1 à P4)</li>
                        <li>Équipe d'astreinte pour les incidents critiques</li>
                        <li>Processus d'escalade automatique</li>
                    </ul>
                    
                    <strong>2. Catalogue de Services :</strong>
                    <ul>
                        <li>Définition des services standard (création compte, accès VPN, etc.)</li>
                        <li>Portail self-service pour les demandes courantes</li>
                        <li>Workflows d'approbation automatisés</li>
                        <li>SLA définis pour chaque type de demande</li>
                    </ul>
                    
                    <strong>3. Contrôle des Changements :</strong>
                    <ul>
                        <li>CAB (Change Advisory Board) hebdomadaire</li>
                        <li>Fenêtres de maintenance planifiées</li>
                        <li>Tests obligatoires en pré-production</li>
                        <li>Procédures de rollback documentées</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    
    <div class="exercise-box">
        <div class="exercise-title">🎯 Exercice Pratique : Incident Critique</div>
        <div class="exercise-content">
            <div class="scenario-box">
                <div class="scenario-title">🚨 Situation</div>
                <div>
                    Il est 14h30, le serveur de base de données principal tombe en panne. 150 utilisateurs ne peuvent plus accéder à l'application métier critique. Le directeur commercial a une présentation client importante à 16h.
                </div>
            </div>
            
            <strong>Questions :</strong>
            <ol>
                <li>Quelle priorité attribuez-vous à cet incident selon ITIL ?</li>
                <li>Quelles sont les premières actions à entreprendre ?</li>
                <li>Qui doit être informé et dans quels délais ?</li>
                <li>Comment organiser la résolution ?</li>
                <li>Quelles informations documenter ?</li>
            </ol>
            
            <div class="solution-box">
                <div class="solution-title">Réponse Type</div>
                <div>
                    <strong>1. Priorité P1 (Critique) :</strong> Impact élevé + Urgence élevée
                    
                    <strong>2. Actions immédiates :</strong>
                    <ul>
                        <li>Créer un ticket incident P1</li>
                        <li>Activer l'équipe d'astreinte</li>
                        <li>Évaluer les solutions de contournement</li>
                        <li>Vérifier la disponibilité du serveur de secours</li>
                    </ul>
                    
                    <strong>3. Communication :</strong>
                    <ul>
                        <li>Notification immédiate : DSI, responsables métier</li>
                        <li>Mise à jour toutes les 30 minutes</li>
                        <li>Communication utilisateurs via portail/email</li>
                    </ul>
                    
                    <strong>4. Organisation :</strong>
                    <ul>
                        <li>Incident Manager désigné</li>
                        <li>Équipe technique mobilisée</li>
                        <li>Point de situation régulier</li>
                        <li>Escalade si non résolu en 2h</li>
                    </ul>
                    
                    <strong>5. Documentation :</strong>
                    <ul>
                        <li>Chronologie détaillée des actions</li>
                        <li>Cause racine identifiée</li>
                        <li>Actions correctives et préventives</li>
                        <li>Retour d'expérience (REX)</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎓 Certification et Carrière</h2>
    
    <div class="definition-box">
        <div class="definition-title">📜 Parcours de Certification ITIL</div>
        <div class="definition-content">
            Le schéma de certification ITIL v4 offre plusieurs niveaux pour développer ses compétences en gestion des services IT.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🥉</div>
            <div class="concept-name">ITIL Foundation</div>
            <div class="concept-description">
                Niveau d'entrée couvrant les concepts clés, terminologie et principes d'ITIL v4.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🥈</div>
            <div class="concept-name">ITIL Specialist</div>
            <div class="concept-description">
                Approfondissement sur des domaines spécifiques : Create/Deliver/Support, Drive Stakeholder Value, etc.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🥇</div>
            <div class="concept-name">ITIL Strategist</div>
            <div class="concept-description">
                Niveau avancé pour les leaders IT : Direct/Plan/Improve et transformation digitale.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💎</div>
            <div class="concept-name">ITIL Master</div>
            <div class="concept-description">
                Niveau expert démontrant la capacité à appliquer ITIL dans des contextes complexes.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💼 <strong>Opportunités Carrière :</strong> Les compétences ITIL ouvrent vers des postes d'Incident Manager, Service Manager, ITSM Consultant, ou Responsable des Opérations IT.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔮 ITIL et les Tendances Actuelles</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚀 Adaptation aux Nouvelles Technologies</div>
        <div class="definition-content">
            ITIL v4 s'adapte aux évolutions technologiques et organisationnelles actuelles pour rester pertinent dans un monde IT en constante évolution.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">☁️</div>
            <div class="concept-name">Cloud Computing</div>
            <div class="concept-description">
                Adaptation des pratiques ITIL aux services cloud (IaaS, PaaS, SaaS) et à la gestion multi-cloud.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">DevOps</div>
            <div class="concept-description">
                Intégration des principes DevOps avec ITIL pour accélérer la livraison tout en maintenant la stabilité.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🤖</div>
            <div class="concept-name">Automatisation</div>
            <div class="concept-description">
                Utilisation de l'IA et de l'automatisation pour optimiser les processus ITIL et réduire les tâches manuelles.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Agilité</div>
            <div class="concept-description">
                Adoption des méthodes agiles et lean pour une gestion des services plus réactive et flexible.
            </div>
        </div>
    </div>
    
    <div class="content-text">
        L'avenir d'ITIL réside dans sa capacité à s'adapter continuellement aux nouvelles réalités technologiques tout en conservant ses principes fondamentaux de création de valeur et d'amélioration continue.
    </div>
</div>