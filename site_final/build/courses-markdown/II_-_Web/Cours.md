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

# 📚 Web

<div class="course-container">
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">Point Historique et Définitions</h3>
        <div class="course-content">
            Le WEB a été créé en 1989 au CERN (institut de recherche Suisse) par une équipe chapeautée par <strong>Tim Berners-Lee</strong> et <strong>Robert Cailliau</strong>.<br><br>Le but du projet initialement était la création d'une application qui permettrait l'échange de données sur Internet.<br><br>La technologie du WEB repose sur l'utilisation d'<strong>hyperliens</strong>. <br>Les hyperliens sont des liens cliquables souvent bleus ressemblant à cela :<br><br>[Lien menant à l'accueil du site](../../index.md)<br><br>Ces divers <strong>hyperliens</strong> permettent d'accéder à des données qui sont stockées sur des <strong>serveurs</strong>, comme des pages WEB, des images ou tout type de contenu.<br><br>Pour accéder aux différents serveurs, ces liens *"pointent"* vers les adresses IP correspondant aux différents serveurs qui détiennent ces ressources.<br><br>Pour accéder à toutes ces données, on utilise un <strong>navigateur WEB</strong>, un logiciel qui permet de traiter des demandes de données (appelées <strong>requêtes</strong>), les afficher ou réaliser certains traitement sur celles-ci.<br><br><strong>Anecdote : voici la toute première page WEB, celle créée par les chercheurs du CERN :</strong> [première page web](http://info.cern.ch/hypertext/WWW/TheProject.html)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Modèle Client - Serveur</h3>
        <div class="course-content">
            On a vu précédemment dans les échanges TCP, que deux machines communiquaient : <strong>emettrice et réceptrice.</strong><br><br>On appelle <strong>client</strong> une machine qui souhaite recevoir des informations ou des données. Cette machine correspond à la machine que l'on nommait *réceptrice*.<br><br>On appelle <strong>serveur</strong> une machine qui dispose d'informations ou de données et qui a pour rôle de les envoyer. Cette machine correspond à ce que l'on nommait *émettrice*.<br><br>Lors d'un échange entre un client et un serveur, ceux-ci émettent des échanges formalisés que l'on appelle <strong>requête</strong>.<br><br>On peut schématiser cela de cette manière : <br><br>![client_serveur](client_serveur.png)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Adresse IP et URL</h3>
        <div class="course-content">
            Il peut être fastidieux de retenir toutes les adresses IP de tous les sites que nous connaissons.<br><br>Personne n'écrit dans sa barre de recherche dans son navigateur <strong>216.58.214.163</strong> pour accéder à la page WEB associée : celle de *google.fr*<br><br>On appelle <strong>URL</strong> (<strong>U</strong>niform <strong>R</strong>essources <strong>L</strong>ocator) l'adresse d'un site WEB, adresse correspondante à l'adresse IP du serveur ou se retrouve la page mais dans des caractères intelligibles par l'être humain.<br><br>Une <strong>URL</strong> est consituée de plusieurs parties séparées par des points:<br><br>$\overbrace{\texttt{http(s)://}}^{\texttt{protocole utilisé}}\underbrace{\texttt{www}}_{\texttt{sous-domaine}}\overbrace{\texttt{google}}^{\texttt{nom de domaine}}\underbrace{\texttt{com}}_{\texttt{extension du domaine}}$<br><br>Le serveur <strong>DNS</strong> (<strong>D</strong>omain <strong>N</strong>ame <strong>S</strong>erver) possède une table de correspondance entre l'adresse IP du serveur disposant des informations et d'une adresse dite <strong>symbolique</strong> que nous pouvons retenir plus facilement.<br><br>Par exemple, nos navigateurs web possèdent des tables de ce style pour éviter de faire les mêmes requêtes tous les jours.<br><br>|Site|Adresse symbolique|Adresse IP|<br>|-|-|-|<br>|Google|www.google.fr|172.217.20.163|<br>|Youtube|www.youtube.fr|142.250.178.142|<br>|Leboncoin|www.leboncoin.fr|18.164.52.43|<br>|Amazon|www.amazon.fr|52.95.116.113|
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Fonctionnement du serveur DNS</h3>
        <div class="course-content">
            Le serveur DNS permet d'associer une adresse symbolique avec une adresse IP.<br>Pour obtenir l'adresse IP d'un serveur disposant d'une ressource que l'on cherche via une adresse symbolique, on peut distinguer plusieurs cas :<br><br>### Adresse symbolique connue dans le navigateur<br><br>Si l'adresse symbolique est déjà stockée dans le cache du navigateur (ou du système d'exploitation), celui-ci remplace envoie la requête de recherche de la ressource avec l'adresse IP qu'il connait déjà dans sa table.<br><br>Par exemple, si l'on cherche à aller sur le site www.google.fr, en dactylographiant notre adresse dans la barre de recherche, le navigateur va envoyer directement la requête de la page du site à l'adresse IP <strong>172.217.20.163</strong>.<br><br>### Adresse symbolique non connue dans le navigateur<br><br>Si l'adresse symbolique n'est pas connue par le navigateur (ou le système d'exploitation), divers requêtes sont réalisées à la suite pour trouver le bon serveur DNS qui dispose de l'adresse à chercher.<br><br>Cela va s'exécuter de manière <strong>récursive</strong>.<br><br>Admettons que nous cherchons le site <strong>windows.microsoft.com</strong><br><br>![dns](dns.png)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Le langage des pages WEB : HTML</h3>
        <div class="course-content">
            Le <strong>HTML</strong> (HyperText Markup Language) a été créé en <strong>1991</strong> par <strong>Tim Berners-Lee</strong>, alors qu'il travaillait au <strong>CERN</strong>. C'est un langage dit "<strong>à balises</strong>".<br><br>Un <strong>langage à balises</strong> est un type de langage informatique utilisé pour structurer et organiser des données en les entourant avec des <strong>balises</strong> ou <strong>tags</strong>.  <br><br>Les balises sont des éléments de texte spécifiques, généralement entourés de crochets angulaires (<code>< ></code>), qui indiquent comment le contenu doit être interprété ou affiché.<br><br>Dans un langage à balises, chaque élément est délimité par une balise d’ouverture et une balise de fermeture.  <br>Par exemple, dans <strong>HTML</strong>, la balise <code><p></code> marque le début d’un paragraphe, et la balise <code></p></code> marque sa fin :<br><br>``<code>html<br><p>Ceci est un paragraphe.</p><br></code>``<br><br>Les balises ne sont pas visibles par l’utilisateur final, elles servent à structurer le document ou à fournir des <strong>informations</strong> sur la manière dont le contenu doit être rendu.  <br><br>Les langages à balises sont souvent utilisés dans la <strong>création de documents web</strong> (comme HTML ou XML), car ils permettent d’ajouter une signification <strong>sémantique</strong> aux données et de contrôler la mise en forme ou le comportement du contenu.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">HTTP : protocole des requêtes sur le WEB</h3>
        <div class="course-content">
            <strong>HTTP</strong> (HyperText Transfer Protocol) est un <strong>protocole de communication</strong> qui permet l'échange de données ou de pages sur le <strong>WEB</strong>.  <br>Il fonctionne selon un modèle <strong>client-serveur</strong>, où un <strong>client</strong> (par exemple, un navigateur web) envoie une <strong>requête</strong> à un <strong>serveur</strong> pour accéder à une ressource, comme une page web.  <br><br>Cette requête inclut une méthode, comme <strong>GET</strong> (pour récupérer des données) ou <strong>POST</strong> (pour envoyer des données).  <br>Le <strong>serveur</strong> répond avec un <strong>code de statut</strong> (comme <strong>200 OK</strong> si tout se passe bien) et la ressource demandée, qui peut être un fichier <strong>HTML</strong>, une image, ou un autre type de contenu.  <br><br>### Les Méthodes HTTP<br>Lors d'une communication, le client utilise différentes méthodes pour interagir avec le serveur.<br><br>La <strong>méthode GET</strong> est utilisée pour récupérer des informations. Elle ne modifie aucune donnée sur le serveur et permet seulement d'obtenir des données comme des pages web, les fichiers necessaires à son affichage ou son fonctionnement etc...<br><br>``<code><br>GET /utilisateurs/profil?id=123 HTTP/1.1<br>Host: www.reseausocial.com<br>User-Agent: Mozilla/5.0<br>Accept-Language: fr-FR<br></code>`<code><br><br>La <strong>méthode POST</strong> est utilisée pour envoyer des données au serveur pour en modifier certaines ressources (informations d'un compte par exemple, envoi de fichiers etc...).<br><br></code>`<code><br>POST /utilisateurs/inscription HTTP/1.1<br>Host: www.reseausocial.com<br>Content-Type: application/x-www-form-urlencoded<br>Content-Length: 54<br><br>nom=Dupont&prenom=Jean&email=jean.dupont@email.com<br></code>``<br><br>Ces méthodes sont souvent utilisées lors de l'envoi de formulaires ou d'initialisation de la page par le navigateur.<br><br>Après chaque requête, le serveur renvoie un code de statut qui indique le résultat du traitement :<br><br>200 OK : La requête a réussi<br>404 Not Found : La ressource demandée n'existe pas<br>500 Internal Server Error : Problème côté serveur
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Page Rank</h3>
        <div class="course-content">
            Le Page Rank est un algorithme révolutionnaire développé par <strong>Larry Page</strong> et <strong>Sergey Brin</strong>, les fondateurs de Google, lors de leurs études à l'Université Stanford en 1996. L'idée était simple mais géniale : classer les pages web non pas uniquement sur leur contenu, mais sur leur importance dans le réseau Internet.<br><br>Le fonctionnement du Page Rank est simple. Il fonctionne sur la logique de "votes".<br>On considère qu'une page vote pour une autre page lorsqu'elle possède un lien vers celle-ci.<br><br><strong>Cela veut dire que plus une page possède de lien plus elle semble "pertinente".</strong><br><br>Cette logique peut paraître efficace mais si énormément de petits articles sans réelle valeur pointent vers une page moins qualitative, elle peut se retrouver plus haute qu'une page de meilleure qualité.<br><br>Pour éviter ce biais, certaines pages ont des votes plus importants que d'autres (comme le maire pour le Loup-Garou de Thiercelieux).<br><br>En calculant le nombre de votes, on peut déterminer la qualité d'une page et si elle est pertinente avec la recherche demandée. Cette logique est utilisée par la plupart des moteurs de recherches.
        </div>
    </div>
    
</div>