<style>
/* Styles modernes pour le cours Gestion du patrimoine informatique */
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

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #3498db;
}

.code-title {
    color: #3498db;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
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
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
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
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">💼 Gestion du Patrimoine Informatique</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Support et mise à disposition de services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Qu'est-ce que le patrimoine informatique ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Définition Fondamentale</div>
        <div class="definition-content">
            Le <strong>patrimoine informatique</strong> désigne l'ensemble des ressources matérielles et logicielles d'une organisation, incluant les équipements, les applications, les données et les infrastructures réseau.
        </div>
    </div>
     
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">💻</div>
            <div class="concept-name">Matériel</div>
            <div class="concept-description">
                Ordinateurs, serveurs, équipements réseau, périphériques, composants électroniques et infrastructures physiques.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💿</div>
            <div class="concept-name">Logiciels</div>
            <div class="concept-description">
                Systèmes d'exploitation, applications métier, outils de développement, licences et mises à jour.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Données</div>
            <div class="concept-description">
                Bases de données, fichiers, configurations, sauvegardes et informations critiques de l'entreprise.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌐</div>
            <div class="concept-name">Infrastructure</div>
            <div class="concept-description">
                Réseaux, serveurs, systèmes de stockage, solutions cloud et architectures distribuées.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📋 Inventaire et Documentation</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Objectifs de l'Inventaire</div>
        <div class="definition-content">
            L'inventaire informatique permet de <strong>recenser</strong>, <strong>documenter</strong> et <strong>suivre</strong> tous les éléments du patrimoine pour optimiser la gestion, réduire les coûts et assurer la conformité.
        </div>
    </div>
    
    <div class="process-grid">
        <div class="process-card">
            <div class="process-number">1</div>
            <div class="process-name">Identification</div>
            <div class="process-description">Recenser tous les équipements et logiciels</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">2</div>
            <div class="process-name">Caractérisation</div>
            <div class="process-description">Documenter les spécifications techniques</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">3</div>
            <div class="process-name">Localisation</div>
            <div class="process-description">Identifier l'emplacement physique ou logique</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">4</div>
            <div class="process-name">Valorisation</div>
            <div class="process-description">Évaluer la valeur financière et stratégique</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Outils d'inventaire :</strong> Utilisez des solutions comme GLPI, OCS Inventory, Lansweeper ou des scripts personnalisés pour automatiser la collecte d'informations sur votre parc informatique.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Bonnes pratiques :</strong> Automatisez l'inventaire avec des outils comme GLPI, OCS Inventory ou des scripts PowerShell pour maintenir des données à jour en temps réel.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 Gestion des Configurations (CMDB)</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Configuration Management Database</div>
        <div class="definition-content">
            Une <strong>CMDB</strong> est une base de données centralisée qui stocke les informations sur tous les éléments de configuration (CI) et leurs relations dans l'infrastructure IT.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Relations</div>
            <div class="concept-description">
                Cartographie des dépendances entre applications, serveurs, bases de données et services métier.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📈</div>
            <div class="concept-name">Traçabilité</div>
            <div class="concept-description">
                Suivi des changements, historique des modifications et impact des évolutions.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Automatisation</div>
            <div class="concept-description">
                Découverte automatique des assets et mise à jour en temps réel des configurations.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Solutions CMDB :</strong> ServiceNow, BMC Remedy, ManageEngine ServiceDesk Plus ou des solutions open source comme iTop permettent de centraliser et gérer les informations de configuration.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Gestion des Licences</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚖️ Conformité Légale</div>
        <div class="definition-content">
            La gestion des licences logicielles assure la <strong>conformité légale</strong>, optimise les coûts et évite les risques juridiques liés à l'utilisation non autorisée de logiciels.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📜</div>
            <div class="concept-name">Types de Licences</div>
            <div class="concept-description">
                Propriétaires, open source, SaaS, par utilisateur, par processeur, volume, OEM.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📈</div>
            <div class="concept-name">Suivi d'Utilisation</div>
            <div class="concept-description">
                Monitoring des installations, utilisations effectives et respect des termes contractuels.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💰</div>
            <div class="concept-name">Optimisation</div>
            <div class="concept-description">
                Réduction des coûts par la rationalisation et la négociation de contrats groupés.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Risques :</strong> L'utilisation de logiciels sans licence appropriée peut entraîner des amendes importantes, des poursuites judiciaires et une atteinte à la réputation de l'entreprise.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Outils d'audit :</strong> Microsoft VAMT, Flexera FlexNet Manager, Snow License Manager ou des audits manuels réguliers permettent de maintenir la conformité des licences.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Cycle de Vie des Équipements</h2>
    
    <div class="definition-box">
        <div class="definition-title">⏰ Gestion du Cycle de Vie</div>
        <div class="definition-content">
            Le cycle de vie des équipements informatiques comprend les phases d'<strong>acquisition</strong>, <strong>déploiement</strong>, <strong>maintenance</strong>, <strong>évolution</strong> et <strong>fin de vie</strong>.
        </div>
    </div>
    
    <div class="process-grid">
        <div class="process-card">
            <div class="process-number">📦</div>
            <div class="process-name">Acquisition</div>
            <div class="process-description">Achat, réception et enregistrement dans l'inventaire</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🚀</div>
            <div class="process-name">Déploiement</div>
            <div class="process-description">Installation, configuration et mise en service</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">🔧</div>
            <div class="process-name">Maintenance</div>
            <div class="process-description">Support, mises à jour et réparations</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">📈</div>
            <div class="process-name">Évolution</div>
            <div class="process-description">Upgrades, migrations et améliorations</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">♻️</div>
            <div class="process-name">Fin de Vie</div>
            <div class="process-description">Décommissionnement, effacement et recyclage</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Planification :</strong> Anticipez le renouvellement des équipements en surveillant les indicateurs de performance, l'âge des matériels et les évolutions technologiques.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛡️ Sécurité du Patrimoine</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔒 Protection des Assets</div>
        <div class="definition-content">
            La sécurité du patrimoine informatique implique la protection physique et logique des équipements, données et infrastructures contre les menaces internes et externes.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏢</div>
            <div class="concept-name">Sécurité Physique</div>
            <div class="concept-description">
                Contrôle d'accès, surveillance, protection contre les sinistres et sécurisation des locaux techniques.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💻</div>
            <div class="concept-name">Sécurité Logique</div>
            <div class="concept-description">
                Authentification, chiffrement, antivirus, pare-feu et gestion des droits d'accès.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">Conformité</div>
            <div class="concept-description">
                Respect des normes ISO 27001, RGPD, SOX et autres réglementations sectorielles.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Attention :</strong> Un patrimoine mal sécurisé expose l'organisation à des risques de vol de données, d'espionnage industriel et de non-conformité réglementaire.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📈 Indicateurs et Tableaux de Bord</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Pilotage par les Métriques</div>
        <div class="definition-content">
            Les indicateurs de performance (KPI) permettent de mesurer l'efficacité de la gestion du patrimoine et d'identifier les axes d'amélioration.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">💰</div>
            <div class="concept-name">Coût Total (TCO)</div>
            <div class="concept-description">
                Acquisition + maintenance + support + formation + fin de vie sur la durée de vie complète.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Disponibilité</div>
            <div class="concept-description">
                Taux de disponibilité des services, MTBF (temps moyen entre pannes) et MTTR (temps de réparation).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Utilisation</div>
            <div class="concept-description">
                Taux d'utilisation des ressources, licences inutilisées et optimisation des capacités.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Outils de reporting :</strong> Microsoft Power BI, Tableau, QlikView ou des solutions intégrées dans les ITSM permettent de créer des tableaux de bord personnalisés pour le suivi des métriques.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Tableau de bord :</strong> Utilisez des outils comme Power BI, Grafana ou des dashboards personnalisés pour visualiser les métriques en temps réel et faciliter la prise de décision.
    </div>
</div>