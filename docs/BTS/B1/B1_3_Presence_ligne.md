<style>
/* Styles modernes pour le cours Présence en Ligne */
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

.danger-fact {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.platform-showcase {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 2rem 0;
    justify-content: center;
}

.platform-badge {
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: 600;
    color: white;
    font-size: 0.9rem;
}

.platform-linkedin { background: linear-gradient(135deg, #0077b5, #42a5f5); }
.platform-twitter { background: linear-gradient(135deg, #1da1f2, #64b5f6); }
.platform-facebook { background: linear-gradient(135deg, #1877f2, #42a5f5); }
.platform-instagram { background: linear-gradient(135deg, #e4405f, #f06292); }
.platform-youtube { background: linear-gradient(135deg, #ff0000, #ff5722); }
.platform-tiktok { background: linear-gradient(135deg, #000000, #424242); }

.strategy-section {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(5px);
}

.strategy-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.content-text {
    color: #34495e;
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 1.5rem;
    text-align: justify;
}

.example-box {
    background: rgba(52, 152, 219, 0.05);
    border: 1px solid rgba(52, 152, 219, 0.2);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.example-title {
    font-weight: 600;
    color: #3498db;
    margin-bottom: 1rem;
}

.metrics-showcase {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.metric-item {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    border: 1px solid rgba(52, 152, 219, 0.2);
}

.metric-value {
    font-size: 1.5rem;
    font-weight: bold;
    color: #3498db;
    margin-bottom: 0.5rem;
}

.metric-label {
    color: #7f8c8d;
    font-size: 0.8rem;
    font-weight: 500;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .platform-showcase {
        flex-direction: column;
        align-items: center;
    }
    
    .metrics-showcase {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🌐 Présence en Ligne et E-réputation</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Support et mise à disposition de services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Comprendre la Présence Numérique</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌍 Qu'est-ce que la Présence en Ligne ?</div>
        <div class="definition-content">
            La présence en ligne représente l'ensemble des traces numériques qu'une personne ou une organisation laisse sur Internet. Cette empreinte digitale se compose de tous les contenus, interactions et informations visibles sur le web qui contribuent à forger une identité numérique unique et durable.
        </div>
    </div>
    
    <div class="content-text">
        Dans le contexte professionnel du BTS SIO, la maîtrise de la présence en ligne devient cruciale. Chaque publication, commentaire, photo ou interaction contribue à construire une réputation qui peut influencer les opportunités de carrière, les relations professionnelles et la crédibilité dans le domaine informatique.
    </div>
    
    <div class="content-text">
        La présence numérique ne se limite pas aux réseaux sociaux traditionnels. Elle englobe également les forums techniques, les plateformes de développement comme GitHub, les blogs professionnels, les contributions à des projets open source, et même les commentaires laissés sur des articles spécialisés. Pour un futur professionnel de l'informatique, cette présence peut devenir un véritable portfolio numérique.
    </div>
    
    <div class="platform-showcase">
        <span class="platform-badge platform-linkedin">💼 LinkedIn</span>
        <span class="platform-badge platform-twitter">🐦 Twitter/X</span>
        <span class="platform-badge platform-facebook">👥 Facebook</span>
        <span class="platform-badge platform-instagram">📸 Instagram</span>
        <span class="platform-badge platform-youtube">🎥 YouTube</span>
        <span class="platform-badge platform-tiktok">🎵 TikTok</span>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Permanence du numérique :</strong> Tout ce qui est publié en ligne peut être archivé, partagé et resurgir des années plus tard. La règle d'or est de ne jamais publier quelque chose que vous ne voudriez pas voir affiché sur un panneau publicitaire.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🏆 L'E-réputation : Un Capital à Préserver</h2>
    
    <div class="definition-box">
        <div class="definition-title">⭐ Définition de l'E-réputation</div>
        <div class="definition-content">
            L'e-réputation correspond à la perception qu'ont les internautes d'une personne, d'une marque ou d'une organisation, basée sur l'ensemble des informations disponibles en ligne. Cette réputation numérique influence directement la confiance, la crédibilité et les opportunités professionnelles.
        </div>
    </div>
    
    <div class="content-text">
        Pour un professionnel de l'informatique, l'e-réputation revêt une importance particulière. Les recruteurs consultent systématiquement les profils en ligne des candidats, et une réputation positive peut faire la différence lors d'un processus de recrutement. À l'inverse, des contenus inappropriés ou des prises de position controversées peuvent compromettre des opportunités professionnelles.
    </div>
    
    <div class="content-text">
        L'e-réputation se construit progressivement à travers chaque interaction en ligne. Elle peut évoluer rapidement, particulièrement en cas de crise ou de polémique. La vitesse de propagation de l'information sur Internet amplifie considérablement l'impact des événements, qu'ils soient positifs ou négatifs.
    </div>
    
    <div class="example-box">
        <div class="example-title">💡 Exemple concret</div>
        Un développeur qui partage régulièrement ses connaissances techniques sur LinkedIn, contribue à des projets open source sur GitHub et participe constructivement à des discussions sur Stack Overflow construit progressivement une réputation d'expert dans son domaine. Cette réputation peut lui ouvrir des portes pour des postes à responsabilités ou des missions de consulting.
    </div>
    
    <div class="danger-fact">
        🚨 <strong>Risques majeurs :</strong> Une e-réputation dégradée peut entraîner des refus d'embauche, des pertes de contrats, une diminution de la crédibilité professionnelle et des difficultés à établir des partenariats.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📱 Stratégies de Présence Professionnelle</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Approche Stratégique de la Communication</div>
        <div class="definition-content">
            Une présence en ligne efficace nécessite une approche réfléchie et cohérente. Il ne s'agit pas simplement d'être présent sur toutes les plateformes, mais de choisir les canaux appropriés et d'adapter le message à chaque audience.
        </div>
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">📝 Création de Contenu de Qualité</div>
        <div class="content-text">
            La production de contenu original et pertinent constitue le pilier d'une présence en ligne réussie. Pour un professionnel de l'informatique, cela peut prendre la forme d'articles techniques, de tutoriels, de retours d'expérience sur des projets, ou de analyses de nouvelles technologies. L'objectif est de démontrer son expertise tout en apportant de la valeur à la communauté.
        </div>
        
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">💬 Engagement et Interaction</div>
        <div class="content-text">
            L'interaction avec la communauté professionnelle est cruciale pour développer un réseau et renforcer sa visibilité. Cela implique de répondre aux commentaires, de participer à des discussions, de partager et commenter les contenus d'autres professionnels, et de contribuer à des groupes spécialisés. La création d'un réseau professionnel peut être bénéfique et différencier plusieurs dossiers lors d'une campagne de rectrutement.
        </div>
        
        <div class="content-text">
            L'engagement doit être authentique et constructif. Il ne s'agit pas de multiplier les interactions superficielles, mais d'apporter une réelle valeur ajoutée aux conversations. Une approche respectueuse et professionnelle dans tous les échanges contribue à construire une réputation positive.
        </div>
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">📊 Mesure et Optimisation</div>
        <div class="content-text">
            Le suivi des performances permet d'ajuster la stratégie de présence en ligne. Les métriques importantes incluent la portée des publications, le taux d'engagement, la croissance de l'audience, et surtout la qualité des interactions générées.
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛡️ Protection et Gestion des Risques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔒 Sécurisation de l'Identité Numérique</div>
        <div class="definition-content">
            La protection de l'identité numérique implique la mise en place de mesures préventives pour éviter l'usurpation d'identité, la diffusion de fausses informations, et la compromission des comptes professionnels.
        </div>
    </div>
    
    <div class="content-text">
        La sécurisation des comptes constitue la première ligne de défense. L'utilisation de mots de passe robustes et uniques pour chaque plateforme (ou l'utilisation d'un gestionnaire de mots de passe), l'activation de l'authentification à deux facteurs, et la vérification régulière des paramètres de confidentialité sont des pratiques essentielles.
    </div>
    
    <div class="content-text">
        La veille sur sa propre réputation permet de détecter rapidement les mentions négatives ou les tentatives d'usurpation d'identité. Des outils de monitoring peuvent alerter en cas de nouvelle mention du nom ou de l'entreprise sur le web, permettant une réaction rapide en cas de problème.
    </div>
    
    <div class="example-box">
        <div class="example-title">🔍 Techniques de Veille</div>
        La mise en place d'alertes Google sur son nom et celui de son entreprise permet de surveiller les nouvelles mentions.
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">🚨 Gestion de Crise</div>
        
        <div class="content-text">
            La transparence et l'authenticité sont généralement les meilleures approches en cas de crise. Reconnaître ses erreurs, présenter des excuses sincères si nécessaire, et expliquer les mesures correctives mises en place contribuent souvent à limiter les dégâts et parfois même à renforcer la confiance.
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Règle de base :</strong> En cas de polémique, évitez les réactions à chaud. Prenez le temps de réfléchir à une réponse appropriée et, si nécessaire, faites-vous accompagner par des professionnels de la communication.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📈 Optimisation pour les Moteurs de Recherche</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 SEO Personnel et Professionnel</div>
        <div class="definition-content">
            L'optimisation pour les moteurs de recherche (SEO) appliquée à l'identité numérique vise à contrôler les résultats qui apparaissent lors d'une recherche sur son nom ou celui de son entreprise.
        </div>
    </div>
    
    <div class="content-text">
        La création et l'optimisation de profils professionnels sur les principales plateformes (LinkedIn, GitHub pour les développeurs) permettent de contrôler les premiers résultats de recherche. Ces profils doivent être complets, régulièrement mis à jour, et optimisés avec les mots-clés pertinents du secteur d'activité.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Présence Professionnelle Spécialisée</h2>
    
    <div class="definition-box">
        <div class="definition-title">💼 Plateformes Métier pour l'Informatique</div>
        <div class="definition-content">
            Pour les professionnels de l'informatique, certaines plateformes spécialisées sont incontournables pour développer une présence professionnelle crédible et établir son expertise technique.
        </div>
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">🔧 GitHub : Portfolio de Développeur</div>
        <div class="content-text">
            GitHub constitue le CV technique de référence pour tout développeur. Un profil GitHub bien entretenu, avec des projets variés, une activité régulière et des contributions à des projets open source, démontre concrètement les compétences techniques et l'engagement dans la communauté de développement.
        </div>
        
        <div class="content-text">
            La qualité du code, la documentation des projets, et la régularité des contributions sont scrutées par les recruteurs techniques. Un historique de commits régulier et des projets bien documentés témoignent du professionnalisme et de la rigueur du développeur.
        </div>
    </div>
    
    <div class="strategy-section">
        <div class="strategy-title">💡 Stack Overflow : Expertise Reconnue</div>
        <div class="content-text">
            La participation active à Stack Overflow, en répondant aux questions techniques et en posant des questions pertinentes, permet de démontrer son expertise et sa capacité à résoudre des problèmes complexes. Un score élevé et des réponses bien notées constituent une reconnaissance par les pairs.
        </div>
    </div>
</div>