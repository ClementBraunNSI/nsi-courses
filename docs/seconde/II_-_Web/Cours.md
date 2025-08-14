<style>
/* Styles modernes pour le cours Web */
.course-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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

.timeline-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.timeline-title {
    font-size: 2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
}

.timeline-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.timeline-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.timeline-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.timeline-year {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
}

.timeline-event {
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.timeline-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.definition-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
}

.model-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.model-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.model-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.model-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.model-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.model-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.url-structure {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.url-parts {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.url-part {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
}

.url-part-title {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 0.5rem;
}

.url-part-description {
    color: #7f8c8d;
    font-size: 0.9rem;
}

.dns-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.dns-table table {
    width: 100%;
    border-collapse: collapse;
}

.dns-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.dns-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
}

.dns-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #4299e1;
}

.code-title {
    color: #4299e1;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.method-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-type {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
}

.status-codes {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.status-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem;
    margin: 0.5rem 0;
    background: rgba(102, 126, 234, 0.05);
    border-radius: 8px;
}

.status-code {
    font-weight: bold;
    color: #667eea;
    font-family: 'Courier New', monospace;
}

.status-description {
    color: #2c3e50;
}

.pagerank-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.algorithm-card {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(255, 193, 7, 0.2);
}

.algorithm-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #f39c12;
    margin-bottom: 1rem;
    text-align: center;
}

.vote-concept {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.image-container {
    text-align: center;
    margin: 2rem 0;
}

.image-container img {
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .timeline-grid {
        grid-template-columns: 1fr;
    }
    
    .model-grid {
        grid-template-columns: 1fr;
    }
    
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .url-parts {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🌐 Web</h1>
    <p class="course-subtitle">L'évolution du World Wide Web et ses technologies fondamentales</p>
</div>

<div class="timeline-section">
    <h2 class="timeline-title">📅 L'Histoire du World Wide Web</h2>
    
    <div class="timeline-grid">
        <div class="timeline-card">
            <div class="timeline-year">1989</div>
            <div class="timeline-event">Naissance du Web</div>
            <div class="timeline-description">
                Tim Berners-Lee et Robert Cailliau créent le World Wide Web au CERN en Suisse. L'objectif : permettre l'échange de données sur Internet via des hyperliens.
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1991</div>
            <div class="timeline-event">Premier Site Web</div>
            <div class="timeline-description">
                Mise en ligne de la toute première page web au CERN, expliquant le concept du World Wide Web et comment l'utiliser.
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1993</div>
            <div class="timeline-event">Web Libre</div>
            <div class="timeline-description">
                Le CERN annonce que le Web sera libre d'utilisation pour tous, sans redevances. Cette décision révolutionnaire permet l'explosion du Web.
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">Aujourd'hui</div>
            <div class="timeline-event">Web Moderne</div>
            <div class="timeline-description">
                Plus de 1,7 milliard de sites web actifs, avec des technologies avancées permettant des applications complexes et interactives.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Concept Fondamental : Les Hyperliens</div>
        <div class="definition-content">
            La technologie du Web repose sur les <strong>hyperliens</strong> - des liens cliquables qui permettent de naviguer entre les ressources stockées sur différents serveurs à travers le monde.
        </div>
    </div>
    
    <div class="highlight-fact">
        🔗 <strong>Exemple d'hyperlien :</strong> <a href="../../index.md">Lien menant à l'accueil du site</a>
    </div>
    
    <div class="highlight-fact">
        🌍 <strong>Anecdote historique :</strong> Découvrez la <a href="http://info.cern.ch/hypertext/WWW/TheProject.html">toute première page web</a> créée par les chercheurs du CERN !
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Le Modèle Client-Serveur</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Architecture Fondamentale</div>
        <div class="definition-content">
            Le Web fonctionne selon un modèle <strong>client-serveur</strong> où les machines communiquent selon des rôles bien définis.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">💻</div>
            <div class="model-name">Client</div>
            <div class="model-description">
                Machine qui souhaite recevoir des informations ou des données. Correspond à la machine <em>réceptrice</em> dans les échanges TCP. Exemple : votre navigateur web.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🖥️</div>
            <div class="model-name">Serveur</div>
            <div class="model-description">
                Machine qui dispose d'informations et a pour rôle de les envoyer. Correspond à la machine <em>émettrice</em>. Exemple : serveur hébergeant un site web.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📡 Communication par Requêtes</div>
        <div class="definition-content">
            Les échanges entre client et serveur se font via des <strong>requêtes</strong> - des messages formalisés qui permettent de demander ou d'envoyer des données.
        </div>
    </div>
    
    <div class="image-container">
        <img src="../client_serveur.png" width = "70%" alt="Schéma du modèle client-serveur" />
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🏷️ Adresses IP et URL</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌐 De l'IP à l'URL</div>
        <div class="definition-content">
            Plutôt que de retenir des adresses IP comme <strong>216.58.214.163</strong> pour accéder à Google, nous utilisons des <strong>URL</strong> (Uniform Resource Locator) - des adresses intelligibles par l'humain.
        </div>
    </div>
    
    <div class="url-structure">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1.5rem;">🧩 Structure d'une URL</h3>
        
        <div class="code-example">
            <div class="code-title">📝 Exemple d'URL décomposée</div>
            <pre><code>https://www.google.com/search?q=exemple
│      │   │      │   │
│      │   │      │   └─ Paramètres de requête
│      │   │      └───── Chemin vers la ressource
│      │   └──────────── Nom de domaine
│      └──────────────── Sous-domaine
└─────────────────────── Protocole utilisé</code></pre>
        </div>
        
        <div class="url-parts">
            <div class="url-part">
                <div class="url-part-title">🔒 Protocole</div>
                <div class="url-part-description">http:// ou https://</div>
            </div>
            <div class="url-part">
                <div class="url-part-title">🌍 Sous-domaine</div>
                <div class="url-part-description">www (optionnel)</div>
            </div>
            <div class="url-part">
                <div class="url-part-title">🏠 Nom de domaine</div>
                <div class="url-part-description">google, facebook, etc.</div>
            </div>
            <div class="url-part">
                <div class="url-part-title">🏷️ Extension</div>
                <div class="url-part-description">.com, .fr, .org, etc.</div>
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🗂️ Serveur DNS (Domain Name Server)</div>
        <div class="definition-content">
            Le serveur DNS maintient une table de correspondance entre les adresses IP et les adresses symboliques, permettant la traduction automatique des URL en adresses IP.
        </div>
    </div>
    
    <div class="dns-table">
        <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Exemple de Table DNS</h4>
        <table>
            <thead>
                <tr>
                    <th>Site</th>
                    <th>Adresse symbolique</th>
                    <th>Adresse IP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Google</td>
                    <td>www.google.fr</td>
                    <td>172.217.20.163</td>
                </tr>
                <tr>
                    <td>YouTube</td>
                    <td>www.youtube.fr</td>
                    <td>142.250.178.142</td>
                </tr>
                <tr>
                    <td>Leboncoin</td>
                    <td>www.leboncoin.fr</td>
                    <td>18.164.52.43</td>
                </tr>
                <tr>
                    <td>Amazon</td>
                    <td>www.amazon.fr</td>
                    <td>52.95.116.113</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔍 Fonctionnement du Serveur DNS</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Résolution DNS</div>
        <div class="definition-content">
            Le serveur DNS associe une adresse symbolique avec une adresse IP. Le processus varie selon que l'adresse est déjà connue ou non.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">💾</div>
            <div class="model-name">Adresse Connue (Cache)</div>
            <div class="model-description">
                Si l'adresse symbolique est stockée dans le cache du navigateur, celui-ci utilise directement l'adresse IP correspondante sans interroger de serveur DNS externe.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Adresse Inconnue (Récursif)</div>
            <div class="model-description">
                Si l'adresse n'est pas connue, une série de requêtes récursives est lancée pour trouver le serveur DNS qui dispose de l'information recherchée.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Exemple pratique :</strong> Recherche de www.google.fr → Le navigateur utilise directement l'IP <strong>172.217.20.163</strong> si elle est en cache.
    </div>
    
    <div class="image-container">
        <img src="../dns.png" alt="Processus de résolution DNS récursive" />
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📝 Le Langage HTML</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 HTML (HyperText Markup Language)</div>
        <div class="definition-content">
            Créé en <strong>1991</strong> par <strong>Tim Berners-Lee</strong> au CERN, HTML est un langage <strong>à balises</strong> qui structure et organise le contenu des pages web.
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🏷️ Principe des Balises</div>
        <div class="definition-content">
            Les balises sont des éléments entourés de crochets angulaires (<code>&lt; &gt;</code>) qui indiquent comment le contenu doit être interprété ou affiché. Chaque élément a une balise d'ouverture et de fermeture.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple de Balise HTML</div>
        <pre><code>&lt;p&gt;Ceci est un paragraphe.&lt;/p&gt;

&lt;h1&gt;Titre principal&lt;/h1&gt;
&lt;h2&gt;Sous-titre&lt;/h2&gt;

&lt;a href="https://example.com"&gt;Lien hypertexte&lt;/a&gt;

&lt;img src="image.jpg" alt="Description de l'image" /&gt;</code></pre>
    </div>
    
    <div class="highlight-fact">
        ✨ <strong>Caractéristiques clés :</strong> Les balises ne sont pas visibles par l'utilisateur final - elles servent uniquement à structurer le document et contrôler son rendu.
    </div>
    
    <div class="highlight-fact">
        🎯 <strong>Usage :</strong> HTML permet d'ajouter une signification <strong>sémantique</strong> aux données et de contrôler la mise en forme du contenu web.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📡 Protocole HTTP</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 HTTP (HyperText Transfer Protocol)</div>
        <div class="definition-content">
            HTTP est le <strong>protocole de communication</strong> qui permet l'échange de données sur le Web selon un modèle client-serveur. Le client envoie des requêtes, le serveur répond avec des codes de statut et les ressources demandées.
        </div>
    </div>
    
    <h3 style="text-align: center; color: #667eea; margin: 2rem 0;">🔧 Les Méthodes HTTP</h3>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📥 Méthode GET</div>
            <div class="definition-content">
                Utilisée pour <strong>récupérer</strong> des informations. Ne modifie aucune donnée sur le serveur. Permet d'obtenir des pages web, images, fichiers CSS/JS, etc.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple de requête GET</div>
                <pre><code>GET /utilisateurs/profil?id=123 HTTP/1.1
Host: www.reseausocial.com
User-Agent: Mozilla/5.0
Accept-Language: fr-FR</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">📤 Méthode POST</div>
            <div class="definition-content">
                Utilisée pour <strong>envoyer</strong> des données au serveur afin de modifier des ressources. Utilisée pour les formulaires, upload de fichiers, mise à jour de profils, etc.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple de requête POST</div>
                <pre><code>POST /utilisateurs/inscription HTTP/1.1
Host: www.reseausocial.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 54

nom=Dupont&prenom=Jean&email=jean.dupont@email.com</code></pre>
            </div>
        </div>
    </div>
    
    <div class="status-codes">
        <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Codes de Statut HTTP</h4>
        
        <div class="status-item">
            <span class="status-code">200 OK</span>
            <span class="status-description">La requête a réussi</span>
        </div>
        
        <div class="status-item">
            <span class="status-code">404 Not Found</span>
            <span class="status-description">La ressource demandée n'existe pas</span>
        </div>
        
        <div class="status-item">
            <span class="status-code">500 Internal Server Error</span>
            <span class="status-description">Problème côté serveur</span>
        </div>
    </div>
    
    <div class="highlight-fact">
        🔄 <strong>Usage courant :</strong> Ces méthodes sont utilisées lors de l'envoi de formulaires ou de l'initialisation de pages par le navigateur.
    </div>
</div>

<div class="pagerank-section">
    <h2 class="section-title">🏆 L'Algorithme PageRank</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Révolution de la Recherche Web</div>
        <div class="definition-content">
            Développé par <strong>Larry Page</strong> et <strong>Sergey Brin</strong> à Stanford en 1996, PageRank révolutionne la recherche en classant les pages selon leur <strong>importance</strong> dans le réseau Internet, pas seulement leur contenu.
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🗳️ Principe du "Vote"</div>
        <div class="definition-content">
            PageRank fonctionne sur la logique de <strong>votes</strong> : une page "vote" pour une autre lorsqu'elle possède un lien vers celle-ci. Plus une page reçoit de liens, plus elle semble pertinente.
        </div>
    </div>
    
    <div class="vote-concept">
        <h4 style="color: #667eea; margin-bottom: 1rem;">⚖️ Pondération des Votes</h4>
        <p>Pour éviter les biais, certaines pages ont des votes plus importants que d'autres. Une page de haute qualité qui fait un lien vers votre site apporte plus de "poids" que de nombreux liens de faible qualité.</p>
        
        <div style="margin-top: 1rem; padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 8px;">
            <strong>💡 Analogie :</strong> Comme le maire au Loup-Garou de Thiercelieux, certaines pages ont un vote qui compte double !
        </div>
    </div>
    
    <div class="highlight-fact">
        🎯 <strong>Impact :</strong> Cette logique de calcul de pertinence est aujourd'hui utilisée par la plupart des moteurs de recherche pour classer les résultats.
    </div>
    
    <div class="highlight-fact">
        🚀 <strong>Héritage :</strong> PageRank a permis à Google de devenir le moteur de recherche dominant en proposant des résultats plus pertinents que ses concurrents.
    </div>
</div>