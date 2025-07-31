# 📚 Le Web et HTTP

## Historique et définitions

> **📚 Historique**

Le Web (World Wide Web) a été créé en 1989 au CERN (Centre Européen pour la Recherche Nucléaire) par une équipe dirigée par **Tim Berners-Lee** et **Robert Cailliau**. L'objectif initial était de développer une application permettant l'échange de données scientifiques sur Internet.

La technologie du Web repose sur l'utilisation d'**hyperliens**, qui sont des liens cliquables permettant de naviguer entre différentes ressources. Ces hyperliens permettent d'accéder à des données stockées sur des **serveurs**, comme des pages web, des images ou tout autre type de contenu.

**Anecdote :** La toute première page web, créée par Tim Berners-Lee, est toujours accessible à l'adresse : [première page web](http://info.cern.ch/hypertext/WWW/TheProject.html)

## Architecture client-serveur

> **📖 Définition**

Le Web fonctionne selon un modèle **client-serveur** :

- Le **client** est généralement un navigateur web (Chrome, Firefox, Safari, etc.) qui envoie des requêtes pour obtenir des ressources.
- Le **serveur** est un ordinateur qui héberge les ressources web et répond aux requêtes des clients.

Le processus de communication se déroule ainsi :
1. L'utilisateur saisit une URL ou clique sur un lien dans son navigateur (client)
2. Le client envoie une requête au serveur approprié
3. Le serveur traite la requête et renvoie une réponse
4. Le client (navigateur) interprète la réponse et affiche le contenu à l'utilisateur

## Les URL et le système DNS

> **📖 Définition**

Une **URL** (Uniform Resource Locator) est l'adresse qui permet de localiser une ressource sur le Web. Elle est composée de plusieurs parties :

```
protocole://sous-domaine.nom-de-domaine.extension/chemin/ressource
```

Exemple : `https://www.example.com/dossier/page.html`

- **Protocole** : `https://` (indique le protocole de communication utilisé)
- **Sous-domaine** : `www` (subdivision du domaine principal)
- **Nom de domaine** : `example` (nom unique identifiant le site)
- **Extension** : `.com` (catégorie du domaine)
- **Chemin** : `/dossier/page.html` (localisation de la ressource sur le serveur)

Le système **DNS** (Domain Name System) est un service qui traduit les noms de domaine en adresses IP. Sans DNS, nous devrions mémoriser les adresses IP de chaque site web (par exemple, 172.217.20.163 pour Google).

Lorsqu'un utilisateur saisit une URL :
1. Le navigateur vérifie d'abord son cache local pour voir s'il connaît déjà l'adresse IP correspondante
2. Si non, une requête DNS est envoyée à un serveur DNS
3. Le serveur DNS renvoie l'adresse IP correspondante
4. Le navigateur peut alors établir une connexion avec le serveur web à cette adresse IP

## Le protocole HTTP

> **📖 Définition**

**HTTP** (HyperText Transfer Protocol) est le protocole de communication utilisé pour échanger des informations sur le Web. Il définit comment les messages sont formatés et transmis entre clients et serveurs.

### Fonctionnement général

HTTP fonctionne selon un principe de **requête-réponse** :

1. Le client envoie une **requête HTTP** au serveur
2. Le serveur traite la requête et renvoie une **réponse HTTP**

Chaque requête et réponse HTTP contient :
- Une **ligne de départ** (méthode, URL, version pour les requêtes ; version, code d'état pour les réponses)
- Des **en-têtes** (headers) contenant des métadonnées
- Un **corps** (body) optionnel contenant les données

### Les méthodes HTTP

Les principales méthodes HTTP sont :

- **GET** : Demande une ressource au serveur (sans modifier les données)
  ```
  GET /utilisateurs/profil?id=123 HTTP/1.1
  Host: www.example.com
  User-Agent: Mozilla/5.0
  Accept-Language: fr-FR
  ```

- **POST** : Envoie des données au serveur (pour créer ou modifier une ressource)
  ```
  POST /utilisateurs/inscription HTTP/1.1
  Host: www.example.com
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 54

  nom=Dupont&prenom=Jean&email=jean.dupont@email.com
  ```

- **PUT** : Remplace complètement une ressource existante
- **DELETE** : Supprime une ressource

### Les codes de statut HTTP

Les réponses HTTP contiennent un code de statut qui indique le résultat du traitement de la requête :

- **1xx** : Information (la requête a été reçue et le processus continue)
- **2xx** : Succès
  - 200 OK : La requête a réussi
  - 201 Created : La ressource a été créée avec succès
- **3xx** : Redirection
  - 301 Moved Permanently : La ressource a été déplacée définitivement
  - 304 Not Modified : La ressource n'a pas été modifiée depuis la dernière requête
- **4xx** : Erreur client
  - 400 Bad Request : La requête est mal formée
  - 403 Forbidden : Accès refusé
  - 404 Not Found : La ressource demandée n'existe pas
- **5xx** : Erreur serveur
  - 500 Internal Server Error : Erreur interne du serveur
  - 503 Service Unavailable : Le serveur est temporairement indisponible

### HTTP et sécurité : HTTPS

**HTTPS** (HTTP Secure) est une version sécurisée du protocole HTTP qui utilise le chiffrement SSL/TLS pour protéger les communications entre le client et le serveur.

Avantages de HTTPS :
- **Confidentialité** : Les données échangées sont chiffrées et ne peuvent pas être lues par des tiers
- **Intégrité** : Garantit que les données n'ont pas été modifiées pendant la transmission
- **Authentification** : Vérifie l'identité du serveur auquel le client se connecte

Le fonctionnement de HTTPS repose sur des certificats numériques délivrés par des autorités de certification (CA) qui attestent de l'identité du site web.

## Pages Web statiques et dynamiques

> **📖 Définition**

### Pages Web statiques

Une **page web statique** est une page dont le contenu est fixe et identique pour tous les utilisateurs. Elle est généralement écrite en HTML et CSS, et son contenu ne change pas à moins que le développeur ne modifie manuellement le code source.

Caractéristiques :
- Contenu identique pour tous les utilisateurs
- Ne nécessite pas de traitement côté serveur
- Chargement rapide
- Facile à mettre en cache
- Idéale pour les sites informatifs qui changent rarement

### Pages Web dynamiques

Une **page web dynamique** est générée à la volée, souvent en fonction des actions de l'utilisateur ou d'autres paramètres. Elle utilise généralement des langages de programmation côté serveur (PHP, Python, JavaScript avec Node.js, etc.) et peut interagir avec des bases de données.

Caractéristiques :
- Contenu personnalisé selon l'utilisateur ou d'autres paramètres
- Nécessite un traitement côté serveur
- Peut inclure des interactions utilisateur complexes
- Permet la gestion de contenu, l'authentification des utilisateurs, etc.
- Utilisée pour les applications web, les réseaux sociaux, les sites e-commerce, etc.

## Cookies et sessions

> **📖 Définition**

### Les cookies HTTP

Les **cookies** sont de petits fichiers texte stockés par le navigateur sur l'ordinateur de l'utilisateur. Ils permettent aux sites web de stocker des informations sur l'utilisateur et de les récupérer lors de visites ultérieures.

Types de cookies :

- **Cookies de session** : Supprimés à la fermeture du navigateur
- **Cookies persistants** : Conservés jusqu'à une date d'expiration spécifiée
- **Cookies first-party** : Créés par le site visité
- **Cookies third-party** : Créés par des domaines autres que celui visité (souvent utilisés pour le suivi publicitaire)