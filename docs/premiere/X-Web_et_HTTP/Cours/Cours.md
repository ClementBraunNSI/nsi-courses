<style>
/* Styles modernes pour le cours Web et HTTP */
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

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
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

.fact-content {
    color: var(--md-default-fg-color);
    font-weight: 500;
    line-height: 1.6;
}

.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.info-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.info-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
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

.methods-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.method-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-name {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #2c3e50;
}

.method-description {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 1rem;
}

.status-codes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.status-category {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.status-category:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.status-title {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.1rem;
    color: #2c3e50;
}

.status-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.status-list li {
    margin: 0.5rem 0;
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 0.85rem;
    color: #7f8c8d;
}

.status-list li:last-child {
    border-bottom: none;
}

.comparison-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.comparison-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.comparison-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.comparison-title {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #2c3e50;
}

.comparison-content {
    font-size: 0.9rem;
    color: #7f8c8d;
}

.comparison-content ul {
    margin: 0.5rem 0;
    padding-left: 1rem;
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Le Web et HTTP</h1>
    <p class="course-subtitle">Comprendre les fondements du World Wide Web</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Historique et définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌐 Naissance du Web</div>
        <div class="definition-content">
            Le Web (World Wide Web) a été créé en 1989 au CERN (Centre Européen pour la Recherche Nucléaire) par une équipe dirigée par <strong>Tim Berners-Lee</strong> et <strong>Robert Cailliau</strong>. L'objectif initial était de développer une application permettant l'échange de données scientifiques sur Internet.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔗 Les hyperliens</div>
        <div class="info-content">
            La technologie du Web repose sur l'utilisation d'<strong>hyperliens</strong>, qui sont des liens cliquables permettant de naviguer entre différentes ressources. Ces hyperliens permettent d'accéder à des données stockées sur des <strong>serveurs</strong>, comme des pages web, des images ou tout autre type de contenu.
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>💡 Anecdote :</strong> La toute première page web, créée par Tim Berners-Lee, est toujours accessible à l'adresse : <a href="http://info.cern.ch/hypertext/WWW/TheProject.html">première page web</a>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🏗️ Architecture client-serveur</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Le modèle client-serveur</div>
        <div class="definition-content">
            Le Web fonctionne selon un modèle <strong>client-serveur</strong> :
            <br><br>
            • Le <strong>client</strong> est généralement un navigateur web (Chrome, Firefox, Safari, etc.) qui envoie des requêtes pour obtenir des ressources.<br>
            • Le <strong>serveur</strong> est un ordinateur qui héberge les ressources web et répond aux requêtes des clients.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔄 Processus de communication</div>
        <div class="info-content">
            Le processus de communication se déroule ainsi :
            <ol>
                <li>L'utilisateur saisit une URL ou clique sur un lien dans son navigateur (client)</li>
                <li>Le client envoie une requête au serveur approprié</li>
                <li>Le serveur traite la requête et renvoie une réponse</li>
                <li>Le client (navigateur) interprète la réponse et affiche le contenu à l'utilisateur</li>
            </ol>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🌐 Les URL et le système DNS</h2>
    
    <div class="definition-box">
        <div class="definition-title">📍 Qu'est-ce qu'une URL ?</div>
        <div class="definition-content">
            Une <strong>URL</strong> (Uniform Resource Locator) est l'adresse qui permet de localiser une ressource sur le Web. Elle est composée de plusieurs parties :
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔗 Structure d'une URL</div>
        <pre>
protocole://sous-domaine.nom-de-domaine.extension/chemin/ressource

Exemple : https://www.example.com/dossier/page.html
        </pre>
    </div>
    
    <div class="info-box">
        <div class="info-title">🧩 Composants d'une URL</div>
        <div class="info-content">
            <ul>
                <li><strong>Protocole</strong> : <code>https://</code> (indique le protocole de communication utilisé)</li>
                <li><strong>Sous-domaine</strong> : <code>www</code> (subdivision du domaine principal)</li>
                <li><strong>Nom de domaine</strong> : <code>example</code> (nom unique identifiant le site)</li>
                <li><strong>Extension</strong> : <code>.com</code> (catégorie du domaine)</li>
                <li><strong>Chemin</strong> : <code>/dossier/page.html</code> (localisation de la ressource sur le serveur)</li>
            </ul>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🗂️ Le système DNS</div>
        <div class="definition-content">
            Le système <strong>DNS</strong> (Domain Name System) est un service qui traduit les noms de domaine en adresses IP. Sans DNS, nous devrions mémoriser les adresses IP de chaque site web (par exemple, 172.217.20.163 pour Google).
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔄 Processus de résolution DNS</div>
        <div class="info-content">
            Lorsqu'un utilisateur saisit une URL :
            <ol>
                <li>Le navigateur vérifie d'abord son cache local pour voir s'il connaît déjà l'adresse IP correspondante</li>
                <li>Si non, une requête DNS est envoyée à un serveur DNS</li>
                <li>Le serveur DNS renvoie l'adresse IP correspondante</li>
                <li>Le navigateur peut alors établir une connexion avec le serveur web à cette adresse IP</li>
            </ol>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🌐 Le protocole HTTP</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Qu'est-ce que HTTP ?</div>
        <div class="definition-content">
            <strong>HTTP</strong> (HyperText Transfer Protocol) est le protocole de communication utilisé pour échanger des informations sur le Web. Il définit comment les messages sont formatés et transmis entre clients et serveurs.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔄 Fonctionnement général</div>
        <div class="info-content">
            HTTP fonctionne selon un principe de <strong>requête-réponse</strong> :
            <ol>
                <li>Le client envoie une <strong>requête HTTP</strong> au serveur</li>
                <li>Le serveur traite la requête et renvoie une <strong>réponse HTTP</strong></li>
            </ol>
            <br>
            Chaque requête et réponse HTTP contient :
            <ul>
                <li>Une <strong>ligne de départ</strong> (méthode, URL, version pour les requêtes ; version, code d'état pour les réponses)</li>
                <li>Des <strong>en-têtes</strong> (headers) contenant des métadonnées</li>
                <li>Un <strong>corps</strong> (body) optionnel contenant les données</li>
            </ul>
        </div>
    </div>
    
    <h3 class="section-title">🛠️ Les méthodes HTTP</h3>
    
    <div class="methods-grid">
        <div class="method-card">
            <div class="method-name">🔍 GET</div>
            <div class="method-description">
                Demande une ressource au serveur (sans modifier les données)
            </div>
            <div class="code-example">
                <div class="code-title">Exemple de requête GET</div>
                <pre>
GET /utilisateurs/profil?id=123 HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept-Language: fr-FR
                </pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-name">📤 POST</div>
            <div class="method-description">
                Envoie des données au serveur (pour créer ou modifier une ressource)
            </div>
            <div class="code-example">
                <div class="code-title">Exemple de requête POST</div>
                <pre>
POST /utilisateurs/inscription HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 54

nom=Dupont&prenom=Jean&email=jean.dupont@email.com
                </pre>
            </div>
        </div>
        
        
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📊 Les codes de statut HTTP</h2>
    
    <div class="definition-box">
        <div class="definition-title">📈 Qu'est-ce qu'un code de statut ?</div>
        <div class="definition-content">
            Les réponses HTTP contiennent un code de statut qui indique le résultat du traitement de la requête.
        </div>
    </div>
    
    <div class="status-codes-grid">
        <div class="status-category">
            <div class="status-title">1xx - Information</div>
            <div class="status-list">
                <li>La requête a été reçue et le processus continue</li>
            </div>
        </div>
        
        <div class="status-category">
            <div class="status-title">2xx - Succès</div>
            <ul class="status-list">
                <li>200 OK : La requête a réussi</li>
                <li>201 Created : La ressource a été créée avec succès</li>
            </ul>
        </div>
        
        <div class="status-category">
            <div class="status-title">3xx - Redirection</div>
            <ul class="status-list">
                <li>301 Moved Permanently : La ressource a été déplacée définitivement</li>
                <li>304 Not Modified : La ressource n'a pas été modifiée depuis la dernière requête</li>
            </ul>
        </div>
        
        <div class="status-category">
            <div class="status-title">4xx - Erreur client</div>
            <ul class="status-list">
                <li>400 Bad Request : La requête est mal formée</li>
                <li>403 Forbidden : Accès refusé</li>
                <li>404 Not Found : La ressource demandée n'existe pas</li>
            </ul>
        </div>
        
        <div class="status-category">
            <div class="status-title">5xx - Erreur serveur</div>
            <ul class="status-list">
                <li>500 Internal Server Error : Erreur interne du serveur</li>
                <li>503 Service Unavailable : Le serveur est temporairement indisponible</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔒 HTTP et sécurité : HTTPS</h2>
    
    <div class="definition-box">
        <div class="definition-title">🛡️ Qu'est-ce que HTTPS ?</div>
        <div class="definition-content">
            <strong>HTTPS</strong> (HTTP Secure) est une version sécurisée du protocole HTTP qui utilise le chiffrement SSL/TLS pour protéger les communications entre le client et le serveur.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">✅ Avantages de HTTPS</div>
        <div class="info-content">
            <ul>
                <li><strong>Confidentialité</strong> : Les données échangées sont chiffrées et ne peuvent pas être lues par des tiers</li>
                <li><strong>Intégrité</strong> : Garantit que les données n'ont pas été modifiées pendant la transmission</li>
                <li><strong>Authentification</strong> : Vérifie l'identité du serveur auquel le client se connecte</li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>🔐 Certificats SSL/TLS :</strong> Le fonctionnement de HTTPS repose sur des certificats numériques délivrés par des autorités de certification (CA) qui attestent de l'identité du site web.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📄 Pages Web statiques et dynamiques</h2>
    
    <div class="comparison-grid">
        <div class="comparison-card">
            <div class="comparison-title">📄 Pages statiques</div>
            <div class="comparison-content">
                Une <strong>page web statique</strong> est une page dont le contenu est fixe et identique pour tous les utilisateurs. Elle est généralement écrite en HTML et CSS, et son contenu ne change pas à moins que le développeur ne modifie manuellement le code source.
                <br><br>
                <strong>Caractéristiques :</strong>
                <ul>
                    <li>Contenu identique pour tous les utilisateurs</li>
                    <li>Ne nécessite pas de traitement côté serveur</li>
                    <li>Chargement rapide</li>
                    <li>Facile à mettre en cache</li>
                    <li>Idéale pour les sites informatifs qui changent rarement</li>
                </ul>
            </div>
        </div>
        
        <div class="comparison-card">
            <div class="comparison-title">⚡ Pages dynamiques</div>
            <div class="comparison-content">
                Une <strong>page web dynamique</strong> est générée à la volée, souvent en fonction des actions de l'utilisateur ou d'autres paramètres. Elle utilise généralement des langages de programmation côté serveur (PHP, Python, JavaScript avec Node.js, etc.) et peut interagir avec des bases de données.
                <br><br>
                <strong>Caractéristiques :</strong>
                <ul>
                    <li>Contenu personnalisé selon l'utilisateur ou d'autres paramètres</li>
                    <li>Nécessite un traitement côté serveur</li>
                    <li>Peut inclure des interactions utilisateur complexes</li>
                    <li>Permet la gestion de contenu, l'authentification des utilisateurs, etc.</li>
                    <li>Utilisée pour les applications web, les réseaux sociaux, les sites e-commerce, etc.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🍪 Cookies et sessions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🍪 Les cookies HTTP</div>
        <div class="definition-content">
            Les <strong>cookies</strong> sont de petits fichiers texte stockés par le navigateur sur l'ordinateur de l'utilisateur. Ils permettent aux sites web de stocker des informations sur l'utilisateur et de les récupérer lors de visites ultérieures.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🏷️ Types de cookies</div>
        <div class="info-content">
            <ul>
                <li><strong>Cookies de session</strong> : Supprimés à la fermeture du navigateur</li>
                <li><strong>Cookies persistants</strong> : Conservés jusqu'à une date d'expiration spécifiée</li>
                <li><strong>Cookies first-party</strong> : Créés par le site visité</li>
                <li><strong>Cookies third-party</strong> : Créés par des domaines autres que celui visité (souvent utilisés pour le suivi publicitaire)</li>
            </ul>
        </div>
    </div>
</div>

</body>
</html>