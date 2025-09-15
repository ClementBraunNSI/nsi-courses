<style>
/* Styles modernes pour le cours Incidents et Assistance */
.course-header {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(230, 126, 34, 0.05));
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
    background: linear-gradient(135deg, #e74c3c 0%, #e67e22 100%);
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
    color: #e74c3c;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(230, 126, 34, 0.05));
    border-left: 5px solid #e74c3c;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #e74c3c;
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
    border-left: 4px solid #e74c3c;
}

.code-title {
    color: #e74c3c;
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
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(230, 126, 34, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(231, 76, 60, 0.2);
    transition: all 0.3s ease;
}

.process-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.process-number {
    font-size: 2rem;
    font-weight: bold;
    color: #e74c3c;
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

.priority-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.priority-card {
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
    color: white;
}

.priority-critical {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.priority-high {
    background: linear-gradient(135deg, #f39c12, #e67e22);
}

.priority-medium {
    background: linear-gradient(135deg, #f1c40f, #f39c12);
    color: #2c3e50;
}

.priority-low {
    background: linear-gradient(135deg, #2ecc71, #27ae60);
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
    
    .priority-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🚨 Gestion des Incidents et Assistance</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Support et mise à disposition de services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Qu'est-ce qu'un incident informatique ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚨 Définition ITIL</div>
        <div class="definition-content">
            Un <strong>incident</strong> est une interruption non planifiée d'un service informatique ou une réduction de la qualité d'un service. L'objectif principal est de <strong>restaurer le service normal</strong> le plus rapidement possible.
        </div>
    </div>
     
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Interruption</div>
            <div class="concept-description">
                Arrêt complet d'un service : panne serveur, coupure réseau, application inaccessible.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📉</div>
            <div class="concept-name">Dégradation</div>
            <div class="concept-description">
                Réduction de performance : lenteur réseau, temps de réponse élevé, fonctionnalités limitées.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔧</div>
            <div class="concept-name">Dysfonctionnement</div>
            <div class="concept-description">
                Comportement anormal : erreurs applicatives, données corrompues, fonctionnalités défaillantes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">👥</div>
            <div class="concept-name">Impact Utilisateur</div>
            <div class="concept-description">
                Gêne pour les utilisateurs : impossibilité de travailler, perte de productivité, frustration.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Distinction importante :</strong> Un incident diffère d'un problème. L'incident est l'effet visible, le problème est la cause sous-jacente qui peut générer plusieurs incidents.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Classification et Priorisation</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Matrice Impact/Urgence</div>
        <div class="definition-content">
            La priorité d'un incident se détermine en croisant son <strong>impact</strong> (nombre d'utilisateurs affectés) et son <strong>urgence</strong> (délai acceptable de résolution).
        </div>
    </div>
    
    <div class="priority-grid">
        <div class="priority-card priority-critical">
            <div>🔴 CRITIQUE</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Impact élevé + Urgence élevée</div>
        </div>
        
        <div class="priority-card priority-high">
            <div>🟠 ÉLEVÉE</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Impact élevé + Urgence faible</div>
        </div>
        
        <div class="priority-card priority-medium">
            <div>🟡 MOYENNE</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Impact faible + Urgence élevée</div>
        </div>
        
        <div class="priority-card priority-low">
            <div>🟢 FAIBLE</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Impact faible + Urgence faible</div>
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">👥</div>
            <div class="concept-name">Impact</div>
            <div class="concept-description">
                <strong>Élevé :</strong> Tous les utilisateurs<br>
                <strong>Moyen :</strong> Un service/département<br>
                <strong>Faible :</strong> Utilisateur individuel
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⏰</div>
            <div class="concept-name">Urgence</div>
            <div class="concept-description">
                <strong>Élevée :</strong> Résolution immédiate<br>
                <strong>Moyenne :</strong> Résolution dans la journée<br>
                <strong>Faible :</strong> Résolution sous 48-72h
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Outils de classification :</strong> Les systèmes ITSM modernes proposent des matrices de priorité configurables et des règles automatiques de classification basées sur des mots-clés ou des critères prédéfinis.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Processus de Gestion des Incidents</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Cycle de Vie d'un Incident</div>
        <div class="definition-content">
            Le processus de gestion des incidents suit un cycle structuré depuis la <strong>détection</strong> jusqu'à la <strong>clôture</strong>, en passant par l'analyse, la résolution et la validation.
        </div>
    </div>
    
    <div class="process-grid">
        <div class="process-card">
            <div class="process-number">1</div>
            <div class="process-name">Détection</div>
            <div class="process-description">Identification et signalement de l'incident</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">2</div>
            <div class="process-name">Enregistrement</div>
            <div class="process-description">Création du ticket avec informations détaillées</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">3</div>
            <div class="process-name">Classification</div>
            <div class="process-description">Évaluation impact, urgence et priorité</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">4</div>
            <div class="process-name">Investigation</div>
            <div class="process-description">Diagnostic et recherche de solution</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">5</div>
            <div class="process-name">Résolution</div>
            <div class="process-description">Application de la solution et tests</div>
        </div>
        
        <div class="process-card">
            <div class="process-number">6</div>
            <div class="process-name">Clôture</div>
            <div class="process-description">Validation utilisateur et documentation</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Workflows automatisés :</strong> Les outils ITSM permettent de configurer des workflows avec transitions automatiques, notifications et escalades selon des règles métier personnalisables.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎧 Service Desk et Support Utilisateur</h2>
    
    <div class="definition-box">
        <div class="definition-title">📞 Point de Contact Unique</div>
        <div class="definition-content">
            Le <strong>Service Desk</strong> est le point de contact unique entre les utilisateurs et l'équipe IT. Il centralise les demandes, incidents et questions pour assurer un service cohérent et traçable.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📞</div>
            <div class="concept-name">Support Téléphonique</div>
            <div class="concept-description">
                Assistance en temps réel, résolution immédiate des problèmes simples, escalade si nécessaire.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💬</div>
            <div class="concept-name">Chat en Ligne</div>
            <div class="concept-description">
                Support instantané, partage d'écran, résolution collaborative des incidents.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎫</div>
            <div class="concept-name">Système de Tickets</div>
            <div class="concept-description">
                Traçabilité complète, suivi des demandes, historique des interventions.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔧</div>
            <div class="concept-name">Support à Distance</div>
            <div class="concept-description">
                Prise de contrôle à distance, diagnostic avancé, résolution sans déplacement.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Niveaux de support :</strong> Niveau 1 (support de base), Niveau 2 (expertise technique), Niveau 3 (spécialistes/éditeurs).
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Portails self-service :</strong> Les portails utilisateur permettent la création autonome de tickets, le suivi en temps réel et l'accès à une base de connaissances pour l'auto-résolution.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📈 Métriques et Indicateurs de Performance</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 KPI du Service Desk</div>
        <div class="definition-content">
            Les indicateurs de performance permettent de mesurer l'efficacité du support, identifier les axes d'amélioration et démontrer la valeur ajoutée du service IT.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⏱️</div>
            <div class="concept-name">Temps de Résolution</div>
            <div class="concept-description">
                <strong>MTTR :</strong> Mean Time To Repair<br>
                Temps moyen entre l'ouverture et la résolution d'un incident.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📞</div>
            <div class="concept-name">Temps de Réponse</div>
            <div class="concept-description">
                Délai entre la création du ticket et la première intervention du support.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">✅</div>
            <div class="concept-name">Taux de Résolution</div>
            <div class="concept-description">
                Pourcentage d'incidents résolus au premier niveau vs escaladés.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">😊</div>
            <div class="concept-name">Satisfaction Client</div>
            <div class="concept-description">
                Évaluation de la qualité du service par les utilisateurs finaux.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Tableaux de bord :</strong> Power BI, Grafana ou les dashboards intégrés aux outils ITSM permettent de visualiser les métriques en temps réel et de générer des rapports automatisés.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Objectifs SLA :</strong> Définissez des objectifs de niveau de service (SLA) clairs : résolution en 4h pour les incidents critiques, 24h pour les incidents élevés.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔧 Outils de Gestion des Incidents</h2>
    
    <div class="definition-box">
        <div class="definition-title">🛠️ Solutions ITSM</div>
        <div class="definition-content">
            Les outils ITSM (IT Service Management) automatisent et optimisent la gestion des incidents, du support utilisateur et des processus IT selon les bonnes pratiques ITIL.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🎫</div>
            <div class="concept-name">ServiceNow</div>
            <div class="concept-description">
                Plateforme enterprise complète avec workflows automatisés, CMDB intégrée et analytics avancés.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔧</div>
            <div class="concept-name">GLPI</div>
            <div class="concept-description">
                Solution open source française avec gestion d'inventaire, helpdesk et suivi des interventions.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Jira Service Management</div>
            <div class="concept-description">
                Outil Atlassian intégré avec Confluence, tableaux de bord personnalisables et automatisations.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💬</div>
            <div class="concept-name">Freshservice</div>
            <div class="concept-description">
                Solution cloud moderne avec IA intégrée, portail self-service et gestion multi-canal.
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Choix d'outil :</strong> Sélectionnez l'outil selon la taille de l'organisation, le budget, les intégrations nécessaires et la complexité des processus.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🤖 Automatisation et Intelligence Artificielle</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚀 Support Intelligent</div>
        <div class="definition-content">
            L'automatisation et l'IA transforment le support IT en permettant la résolution automatique d'incidents courants, la classification intelligente et l'assistance prédictive.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🤖</div>
            <div class="concept-name">Chatbots</div>
            <div class="concept-description">
                Assistance 24/7, résolution automatique des demandes simples, collecte d'informations initiales.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🧠</div>
            <div class="concept-name">Classification Auto</div>
            <div class="concept-description">
                Analyse du contenu des tickets pour classification et routage automatiques vers les bonnes équipes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔮</div>
            <div class="concept-name">Analyse Prédictive</div>
            <div class="concept-description">
                Prédiction des pannes, identification des tendances, maintenance proactive des systèmes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📚</div>
            <div class="concept-name">Base de Connaissances</div>
            <div class="concept-description">
                Suggestions automatiques de solutions, mise à jour dynamique, apprentissage continu.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Solutions IA :</strong> Microsoft Bot Framework, IBM Watson Assistant, ou des solutions intégrées comme ServiceNow Virtual Agent permettent de créer des chatbots intelligents pour le support.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>ROI de l'automatisation :</strong> L'automatisation peut résoudre 30-40% des incidents de niveau 1, libérant du temps pour les techniciens sur des tâches à plus forte valeur ajoutée.
    </div>
</div>