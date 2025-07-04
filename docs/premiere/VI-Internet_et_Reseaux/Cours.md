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

# 📚 🌐 Introduction aux réseaux

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">🔌 Qu'est ce qu'un réseau internet</h3>
        <div class="course-content">
            Un <strong>réseau local</strong> est un ensemble de machines reliées entre elles qui échangent des informations en ne passant que par le routeur ou un switch.<br><br>Un <strong>réseau internet</strong> est un ensemble de réseaux locaux qui communiquent entre eux en passant par Internet.<br><br>Dans un réseau, on retrouve un certain nombre de machines : <br><br>- 💻 Des ordinateurs, smartphones, tablettes, consoles ...<br>- 🏠 IOT : ensemble des objets connectés (par exemple : domotique)<br>- 🔄 Un (ou plusieurs) switchs est un élément d'un réseau qui permet de relier les machines entre elles pour s'échanger des données dans un réseau local.<br>- 📡 un routeur (ou plusieurs) routeur est un élément qui permet de relier plusieurs réseaux entre eux.<br><br>Ces machines sont reliées par :  <br><br>- 🔌 des câbles (RJ45)<br>- 📶 Ondes (exemple : WiFi (Wireless Fidelity) ou 5G)<br>- 💡 par fibre optique<br><br>La communication est définie et régie par des protocoles. <br>Un protocole est un ensemble de règles et d'actions prédéfinies à réaliser dans un ordre précis. <br><br>### 🌍 Distinction Web et Internet<br><br>Internet correspond à <strong>l'ensemble des réseaux organisés</strong> communiquant ensemble.<br><br>Le Web correspond à une application d'Internet qui rend accessible des ressources grâce aux <strong>liens hypertextes</strong> (que l'on nomme usellement hyperliens).<br><br>#### 🔄 Topologies de réseaux<br><br>Une topologie dans les réseaux correspond à la disposition des machines dans un réseau. <br><br>On en distingue plusieurs :  <br><br>- ⭕ Anneau<br>- ⭐ Étoile (en général celui utilisé de manière domestique)<br>- 📊 Bus<br>- 🌳 Hierarchique<br>- 🤝 P2P
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">🔍 Adresse MAC et IP</h3>
        <div class="course-content">
            ### 💳 Adresse MAC<br><br>Une adresse MAC (Media Access Control) correspond à l'adresse physique d'une interface d'une carte Réseau qui est <strong>unique</strong> et propre à la carte.<br>Elle est constituée d'un ensemble de 6 groupes de 16 bits représentés en hexadécimal.<br>Exemple : a8:9f:d9:4c:5c:d9<br><strong>Remarque : Un ordinateur possède une carte réseau qui a plusieurs interfaces.</strong><br><br>Le switch dans un réseau utilise l'adresse MAC de la carte réseau pour retransmettre les données à la bonne machine.<br><br>### 🌐 Adresse IP<br><br>L'adresse IP est l'adresse d'une machine sur un réseau. Elle est attribuée à la première connexion de la machine sur le réseau.<br><br>Elle est constituée d'un ensemble de 4 octects représentés en décimal ou pour la machine leur représentation en binaire.<br>Exemple : $123.32.41.74_2$ pour les humains et $01111011.00100000.00101001.01001010_2$ pour les machines.<br><br>Grâce à ce modèle on peut définir $2^24$ adresse différentes, soient $4 294 967 296$ adresses différentes.<br><br>Une adresse IP est composée de deux choses :<br><br>- Une partie correspondant à l'adresse réseau, c'est à dire à quel réseau elle est rattachée.<br>- Une partie machine qui correspond au numéro de la machine dans le réseau précédemment choisi.<br><br>Ces deux parties sont distinguées dans l'adresse par le nombre de bits qui leurs sont associés.<br><br>On définit un <strong>masque</strong> comme étant le nombre de bits nécessaires pour représenter l'adresse du réseau.<br>En général, pour retrouver l'adresse du réseau d'une machine à l'aide de son adresse IP, on réalise une opération logique <strong>ET</strong> sur chacun des bits.<br>Ce masque est représenté à la fin de l'adresse IP précédée d'un / (slash), on appelle cela la notation <strong>CIDR</strong> de l'adresse.<br><br>Exemple :<br>On dispose de l'adresse 123.32.41.74/16.<br>Cela veut dire qu'il y a 16 bits réservés pour représenter l'adresse réseau.<br><br>On a alors le masque suivant : $11111111.11111111.00000000.00000000_2$ et l'adresse suivante $01111011.00100000.00101001.01001010_2$.<br><br>Pour retrouver l'adresse réseau, on réalise une opération <strong>ET logique</strong> (+ ou &) sur les deux adresses.<br><br>$~~~~11111111.11111111.00000000.00000000_2\newline\And~01111011.00100000.00101001.01001010_2\newline~~~~01111011.00100000.00000000.00000000_2$<br><br>On retrouve l'adresse du réseau qui est 123.32.0.0.<br><br>!!! danger Adresses réservées<br>    Il existe diverses adresse d'un réseau qui sont réservées.<br>    On a :<br>    - L'adresse du réseau, explicitée précédemment qui est inutilisable.<br>    - L'adresse de multiplexage (ou broadcast) qui se termine par 255.  <br>        Celle-ci sert à l'envoi de messages sur le réseau entier, donc réservée.<br><br>On peut définir un certain nombre de machines pour un réseau et cela est défini par le nombre de bits réservés à la partie machine (moins les 2 précédemment citées).<br><br>!!! Tip Calculer le nombre de machines d'un réseau<br>    On peut calculer le nombre d'adresses disponibles facilement : $\texttt{nombre d'adresses disponibles} = 2^{\texttt{nombre de bits de la partie machine}}-2$.<br><br>Pour notre exemple, on sait que l'on a 16 bits réservés à l'identification de machines, cela revient à $2^{16}-2 = 65536 - 2=  65534$ machines possibles.<br><br>Historiquement, on regroupait les adresses IP dans des classes pour les attribuer à divers organismes.<br><br>#### Classes d'adresses IP<br><br>| Classe | Plage d'adresses            | Nombre de réseaux | Nombre d'hôtes par réseau | Utilisation                            |<br>|--------|-----------------------------|-------------------|---------------------------|----------------------------------------|<br>| A      | 1.0.0.0 - 126.0.0.0         | 128               | 16 777 214                | Principalement pour des réseaux très grands comme les gouvernements ou les grandes entreprises. |<br>| B      | 128.0.0.0 - 191.255.0.0     | 16 384            | 65 534                    | Pour des réseaux de taille moyenne comme les universités ou les entreprises de taille moyenne. |<br>| C      | 192.0.0.0 - 223.255.255.0   | 2 097 152         | 254                       | Pour des petits réseaux comme les petites entreprises. |<br>| D      | 224.0.0.0 - 239.255.255.255 | -                 | -                         | Pour le multicast (transmission de données à plusieurs destinataires simultanément). |<br>| E      | 240.0.0.0 - 255.255.255.255 | -                 | -                         | Réservé pour des utilisations futures et des fins expérimentales. |<br><br>#### IPv6<br><br>L'adresse IPv6 est composée d'un ensemble de 8 groupes de 4 symboles en hexadécimal.<br>Un symbole hexadécimal est composé de 4 bits.<br>Cela revient à $2^{8*16} = 2^{128} \approx 3.40 \times 10^{38}$ adresses différentes.<br><br>### Modèle TCP/IP<br><br><img src="Modele_IP.png" align='center' width = 50% /><br><br>Le modèle TCP/IP est un modèle en couche qui permet d'illustrer l'encapsulation des données pour permettre leur envoi, leur réception et leur traitement.<br><br>#### Processus d'Encapsulation<br><br>L'encapsulation est un concept clé du modèle TCP/IP :<br><br>1. Les données sont générées au niveau de la couche Application<br>2. Chaque couche inférieure ajoute ses propres informations (en-têtes)<br>3. À la réception, chaque couche retire ses informations<br>4. Les données sont reconstituées dans leur état original<br><br>!!! tip Analogie Postale<br>    On peut comparer le modèle TCP/IP à un système postal :<br>    - Couche Application = Rédaction de la lettre<br>    - Couche Transport = Mise sous enveloppe, numérotation<br>    - Couche Internet = Adressage, choix de l'acheminement<br>    - Couche Accès Réseau = Distribution physique<br><br>#### Structure des Couches<br><br>Chaque couche a sa tâche prédéfinie, notamment grâce aux protocoles qui sont en jeu.<br><br>##### Couche Accès Réseau<br><br>La couche accès réseau explicite la liaison entre les machines de manière physique (câbles, WiFi...) et la réception des données brutes (bits, ondes lumineuses, signal analogique) aux machines via les switchs ou les routeurs grâce aux adresses physiques (MAC).<br><br>##### Couche Internet<br><br>La couche Internet assure le routage des paquets de données. Elle utilise les adresses IP pour identifier et acheminer les paquets entre différents réseaux. Les protocoles principaux de cette couche sont :<br><br>- IP (Internet Protocol) pour l'adressage et le routage<br>- ICMP (Internet Control Message Protocol) pour les messages de contrôle et de diagnostic<br><br>##### Couche Transport <br><br>Cette couche garantit la qualité et la fiabilité de la transmission des données. Deux protocoles principaux existent :<br><br>- TCP (Transmission Control Protocol) <br>    - Offre une transmission fiable<br>    - Garantit l'ordre et l'intégrité des données<br>    - Adapté aux transmissions nécessitant une précision (web, emails)<br><br>- UDP (User Datagram Protocol)<br>    - Transmission rapide<br>    - Sans garantie de réception<br>    - Utilisé pour les flux temps réel (streaming, jeux en ligne)<br><br>##### Couche Application<br><br>C'est la couche la plus haute qui gère les protocoles spécifiques aux applications. Quelques exemples de protocoles :<br><br>- HTTP/HTTPS pour le web<br>- FTP pour le transfert de fichiers<br>- SMTP pour les emails<br>- DNS pour la résolution de noms de domaine
        </div>
    </div>
    
</div>