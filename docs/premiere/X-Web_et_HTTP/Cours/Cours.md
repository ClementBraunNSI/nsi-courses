<style>
/* Styles pour les cours avec système de cartes */

.course-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 100%;
}

.course-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 4px solid;
    width: 100%;
    max-width: 100%;
    margin: 1rem 0;
}

.course-card.definition {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.02) 100%);
}

.course-card.definition:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.course-card.example {
    border-left-color: #2196F3;
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.02) 100%);
}

.course-card.example:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
}

.course-card.warning {
    border-left-color: #F44336;
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.02) 100%);
}

.course-card.warning:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(244, 67, 54, 0.3);
}

.course-card.tip {
    border-left-color: #FF9800;
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.02) 100%);
}

.course-card.tip:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);
}

.course-card.highlight {
    border-left-color: #9C27B0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.05) 0%, rgba(156, 39, 176, 0.02) 100%);
}

.course-card.highlight:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(156, 39, 176, 0.3);
}

.course-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.course-content {
    margin-bottom: 1rem;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.badge.definition {
    background: rgba(76, 175, 80, 0.15);
    color: #4CAF50;
}

.badge.example {
    background: rgba(33, 150, 243, 0.15);
    color: #2196F3;
}

.badge.warning {
    background: rgba(244, 67, 54, 0.15);
    color: #F44336;
}

.badge.tip {
    background: rgba(255, 152, 0, 0.15);
    color: #FF9800;
}

.badge.highlight {
    background: rgba(156, 39, 176, 0.15);
    color: #9C27B0;
}

.btn {
    background: white;
    color: #4169E1;
    border: 2px solid #4169E1;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    text-decoration: none;
}

.btn:hover {
    background: rgba(65, 105, 225, 0.1);
    border-color: #1E90FF;
    color: #1E90FF;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(65, 105, 225, 0.4);
}

.exercise-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.math-container {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.table tr:hover {
    background: #f8f9fa;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #d63384;
}

pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre code {
    background: none;
    padding: 0;
    color: #495057;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-weight: 600;
}
</style>

# 📚 Le Web et HTTP

<div class="course-container">
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">Historique et définitions</h3>
        <div class="course-content">
            Le Web (World Wide Web) a été créé en 1989 au CERN (Centre Européen pour la Recherche Nucléaire) par une équipe dirigée par <strong>Tim Berners-Lee</strong> et <strong>Robert Cailliau</strong>. L'objectif initial était de développer une application permettant l'échange de données scientifiques sur Internet.<br><br>La technologie du Web repose sur l'utilisation d'<strong>hyperliens</strong>, qui sont des liens cliquables permettant de naviguer entre différentes ressources. Ces hyperliens permettent d'accéder à des données stockées sur des <strong>serveurs</strong>, comme des pages web, des images ou tout autre type de contenu.<br><br><strong>Anecdote :</strong> La toute première page web, créée par Tim Berners-Lee, est toujours accessible à l'adresse : [première page web](http://info.cern.ch/hypertext/WWW/TheProject.html)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Architecture client-serveur</h3>
        <div class="course-content">
            Le Web fonctionne selon un modèle <strong>client-serveur</strong> :<br><br>- Le <strong>client</strong> est généralement un navigateur web (Chrome, Firefox, Safari, etc.) qui envoie des requêtes pour obtenir des ressources.<br>- Le <strong>serveur</strong> est un ordinateur qui héberge les ressources web et répond aux requêtes des clients.<br><br>Le processus de communication se déroule ainsi :<br>1. L'utilisateur saisit une URL ou clique sur un lien dans son navigateur (client)<br>2. Le client envoie une requête au serveur approprié<br>3. Le serveur traite la requête et renvoie une réponse<br>4. Le client (navigateur) interprète la réponse et affiche le contenu à l'utilisateur
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les URL et le système DNS</h3>
        <div class="course-content">
            Une <strong>URL</strong> (Uniform Resource Locator) est l'adresse qui permet de localiser une ressource sur le Web. Elle est composée de plusieurs parties :<br><br>``<code><br>protocole://sous-domaine.nom-de-domaine.extension/chemin/ressource<br></code>`<code><br><br>Exemple : </code>https://www.example.com/dossier/page.html<code><br><br>- <strong>Protocole</strong> : </code>https://<code> (indique le protocole de communication utilisé)<br>- <strong>Sous-domaine</strong> : </code>www<code> (subdivision du domaine principal)<br>- <strong>Nom de domaine</strong> : </code>example<code> (nom unique identifiant le site)<br>- <strong>Extension</strong> : </code>.com<code> (catégorie du domaine)<br>- <strong>Chemin</strong> : </code>/dossier/page.html` (localisation de la ressource sur le serveur)<br><br>Le système <strong>DNS</strong> (Domain Name System) est un service qui traduit les noms de domaine en adresses IP. Sans DNS, nous devrions mémoriser les adresses IP de chaque site web (par exemple, 172.217.20.163 pour Google).<br><br>Lorsqu'un utilisateur saisit une URL :<br>1. Le navigateur vérifie d'abord son cache local pour voir s'il connaît déjà l'adresse IP correspondante<br>2. Si non, une requête DNS est envoyée à un serveur DNS<br>3. Le serveur DNS renvoie l'adresse IP correspondante<br>4. Le navigateur peut alors établir une connexion avec le serveur web à cette adresse IP
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Le protocole HTTP</h3>
        <div class="course-content">
            <strong>HTTP</strong> (HyperText Transfer Protocol) est le protocole de communication utilisé pour échanger des informations sur le Web. Il définit comment les messages sont formatés et transmis entre clients et serveurs.<br><br>### Fonctionnement général<br><br>HTTP fonctionne selon un principe de <strong>requête-réponse</strong> :<br><br>1. Le client envoie une <strong>requête HTTP</strong> au serveur<br>2. Le serveur traite la requête et renvoie une <strong>réponse HTTP</strong><br><br>Chaque requête et réponse HTTP contient :<br>- Une <strong>ligne de départ</strong> (méthode, URL, version pour les requêtes ; version, code d'état pour les réponses)<br>- Des <strong>en-têtes</strong> (headers) contenant des métadonnées<br>- Un <strong>corps</strong> (body) optionnel contenant les données<br><br>### Les méthodes HTTP<br><br>Les principales méthodes HTTP sont :<br><br>- <strong>GET</strong> : Demande une ressource au serveur (sans modifier les données)<br>  ``<code><br>  GET /utilisateurs/profil?id=123 HTTP/1.1<br>  Host: www.example.com<br>  User-Agent: Mozilla/5.0<br>  Accept-Language: fr-FR<br>  </code>`<code><br><br>- <strong>POST</strong> : Envoie des données au serveur (pour créer ou modifier une ressource)<br>  </code>`<code><br>  POST /utilisateurs/inscription HTTP/1.1<br>  Host: www.example.com<br>  Content-Type: application/x-www-form-urlencoded<br>  Content-Length: 54<br><br>  nom=Dupont&prenom=Jean&email=jean.dupont@email.com<br>  </code>``<br><br>- <strong>PUT</strong> : Remplace complètement une ressource existante<br>- <strong>DELETE</strong> : Supprime une ressource<br><br>### Les codes de statut HTTP<br><br>Les réponses HTTP contiennent un code de statut qui indique le résultat du traitement de la requête :<br><br>- <strong>1xx</strong> : Information (la requête a été reçue et le processus continue)<br>- <strong>2xx</strong> : Succès<br>  - 200 OK : La requête a réussi<br>  - 201 Created : La ressource a été créée avec succès<br>- <strong>3xx</strong> : Redirection<br>  - 301 Moved Permanently : La ressource a été déplacée définitivement<br>  - 304 Not Modified : La ressource n'a pas été modifiée depuis la dernière requête<br>- <strong>4xx</strong> : Erreur client<br>  - 400 Bad Request : La requête est mal formée<br>  - 403 Forbidden : Accès refusé<br>  - 404 Not Found : La ressource demandée n'existe pas<br>- <strong>5xx</strong> : Erreur serveur<br>  - 500 Internal Server Error : Erreur interne du serveur<br>  - 503 Service Unavailable : Le serveur est temporairement indisponible<br><br>### HTTP et sécurité : HTTPS<br><br><strong>HTTPS</strong> (HTTP Secure) est une version sécurisée du protocole HTTP qui utilise le chiffrement SSL/TLS pour protéger les communications entre le client et le serveur.<br><br>Avantages de HTTPS :<br>- <strong>Confidentialité</strong> : Les données échangées sont chiffrées et ne peuvent pas être lues par des tiers<br>- <strong>Intégrité</strong> : Garantit que les données n'ont pas été modifiées pendant la transmission<br>- <strong>Authentification</strong> : Vérifie l'identité du serveur auquel le client se connecte<br><br>Le fonctionnement de HTTPS repose sur des certificats numériques délivrés par des autorités de certification (CA) qui attestent de l'identité du site web.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Pages Web statiques et dynamiques</h3>
        <div class="course-content">
            ### Pages Web statiques<br><br>Une <strong>page web statique</strong> est une page dont le contenu est fixe et identique pour tous les utilisateurs. Elle est généralement écrite en HTML et CSS, et son contenu ne change pas à moins que le développeur ne modifie manuellement le code source.<br><br>Caractéristiques :<br>- Contenu identique pour tous les utilisateurs<br>- Ne nécessite pas de traitement côté serveur<br>- Chargement rapide<br>- Facile à mettre en cache<br>- Idéale pour les sites informatifs qui changent rarement<br><br>### Pages Web dynamiques<br><br>Une <strong>page web dynamique</strong> est générée à la volée, souvent en fonction des actions de l'utilisateur ou d'autres paramètres. Elle utilise généralement des langages de programmation côté serveur (PHP, Python, JavaScript avec Node.js, etc.) et peut interagir avec des bases de données. <br>Exemple : <br><br>Caractéristiques :<br>- Contenu personnalisé selon l'utilisateur ou d'autres paramètres<br>- Nécessite un traitement côté serveur<br>- Peut inclure des interactions utilisateur complexes<br>- Permet la gestion de contenu, l'authentification des utilisateurs, etc.<br>- Utilisée pour les applications web, les réseaux sociaux, les sites e-commerce, etc.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Cookies et sessions</h3>
        <div class="course-content">
            ### Les cookies HTTP<br><br>Les <strong>cookies</strong> sont de petits fichiers texte stockés par le navigateur sur l'ordinateur de l'utilisateur. Ils permettent aux sites web de stocker des informations sur l'utilisateur et de les récupérer lors de visites ultérieures.<br><br>Types de cookies :<br><br>- <strong>Cookies de session</strong> : Supprimés à la fermeture du navigateur<br>- <strong>Cookies persistants</strong> : Conservés jusqu'à une date d'expiration spécifiée<br>- <strong>Cookies first-party</strong> : Créés par le site visité<br>- <strong>Cookies third-party</strong> : Créés par des domaines autres que celui visité (souvent utilisés pour le suivi publicitaire)
        </div>
    </div>
    
</div>