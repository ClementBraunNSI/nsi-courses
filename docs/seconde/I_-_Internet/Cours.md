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

# 📚 Internet

<div class="course-container">
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">Point historique</h3>
        <div class="course-content">
            La création d'Internet date du début des années 1960. L'idée était de relier divers machines pour envoyer des données, à l'origine des travaux issus de laboratoires ou des universités.<br><br>A l'époque, le projet initial s'appelait ARPANET et était un projet détenu par la Défense des États-Unis chapeauté Robert Kahn à la Defense Advanced Research Projects Agency.<br>Le premier objectif était de relier les universités de Stanford, de Los Angeles et celle de l'Utah.<br><br>Ce n'est que le 20 septembre 1969 que la première communication voit le jour entre l'université de Californie et celle de Stanford.<br>Le premier message transmis de l'Histoire était *login*.<br><br>![arpa](img/arpanet.jpeg)<br><br>À la suite de cela, dans les années 70-80, des normalismes de communication ont vu le jour. On appelle cet ensemble de règles à respecter des <strong>protocoles</strong>.<br>La manière de communiquer pour les machines est découpées en diverses étapes.<br>Ces diverses étapes sont catégorisées dans un modèle : le modèle TCP-IP qui explique chaque étape de la communication.<br>Chaque étape (ou couche) du modèle TCP-IP correspond à divers protocoles.<br><br>Dans les années 1980, le fameux <strong>protocole TCP/IPv4</strong> a vu le jour. Il est installé en 1983 sur ARPANET, la même année où ont vu le jour les règles des systèmes de nom de domaine (DNS).<br><br>Les années 1990 ont permis de faire voir le jour à une des plus grandes technologies jamais créée par l'être humain : le WEB, créé au CERN (en Suisse) par Tim Berners-Lee et Robert Cailliau.<br><br>![tblrc](img/tblrc.jpeg)<br><br>Depuis, Internet permet de relier plus de 3 à 4 milliards d'internautes pour s'envoyer des mails, des fichiers ou accéder à une quantité de données incommensurable à l'aide de plusieurs applications dépendant de protocoles.<br>Par exemple, il existe des applications de mail (protocole POP), d'échange de fichier (FTP) ou de navigation sur des pages (WEB).<br><br>![map](img/geo-mercator.svg)<br><br>En clair, <strong>Internet est un réseau informatique à échelle mondiale sur lequel de nombreuses applications sont basées.</strong>
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Notion de réseaux</h3>
        <div class="course-content">
            ### Définitions<br><br>Un <strong>réseau informatique</strong> est un ensemble de machines reliées, par différents moyens, qui communiquent entre elles pour échanger des données ou des informations.<br><br>On retrouve un certain nombre d'éléments sur un réseau informatique qui ont chacun leur propre rôle.<br><br>### Les éléments d'un réseau<br><br>Pour qu'un réseau fonctionne, il faut des éléments le constituant.<br>On retrouve :<br><br>| élément  | rôle                                                               | exemple                                      |<br>|----------|--------------------------------------------------------------------|----------------------------------------------|<br>| Machines | Élément qui cherche à communiquer, envoyer ou recevoir des données | ordinateur, tablettes, consoles, smartphones |<br>| Switch   | Élément qui relie de manière locale des machines                   | box internet, switch RJ45                    |<br>| Routeur  | Élément qui permet de relier un réseau local à Internet ou d'autres réseaux | Box internet, routeur spécifique    |<br>| Cables, Ondes | Élément qui permet de relier les diverses machines au Switch ou au routeur| Câble Ethernet, Fibre optique, WiFi|<br><br>On a défini dans les rôles divers types de réseaux.<br><br>On parle de réseau <strong>local</strong> lorsque dans un réseau, divers machines peuvent communiquer directement entre elles sans passer par d'autres réseaux. Exemple : un réseau domestique.<br><br>On peut représenter cela de cette manière :<br>![rlinternet](img/rlinternet.png)<br><br>On dispose de machines, d'un réseau mais, comment se retrouvent-elles pour communiquer? Quelles techniques sont utilisées?
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Adressages</h3>
        <div class="course-content">
            ### Adressage de machines sur un réseau local<br><br>Une machine dispose d'une ou plusieurs <strong>cartes réseaux</strong>. Ces cartes permettent de communiquer de manière locale ou de manière globale vers Internet.<br>Ces cartes disposent de plusieurs adresses qui permettent de l'identifier sur un réseau.<br><br>De manière locale, une carte réseau dispose d'une adresse <strong>MAC (Media Access Control)</strong>.<br>Cette adresse MAC peut aussi être appelée <strong>adresse physique</strong> car elle correspond à l'adresse utilisée par le port Ethernet et le protocole Ethernet.<br><br>Cette adresse est composée de 6 blocs de 2 caractères hexadécimaux. <code>Exemple : a1:b2:c3:d4:e5:f6</code>.<br><br>La base hexadécimale correspond à une représentation en 16 caractères de chiffres ou de nombres.<br><br><strong>Rédiger le tableau de conversion hexadécimal - décimal</strong>.<br><br>### Adressage de machines sur Internet<br><br>Chaque réseau doit pouvoir être accessible et reconnaissable.<br>Sur Internet, on utilise ce que l'on appelle <strong>l'Adresse IP</strong> (pour Internet Protocole).<br><br>Une adresse IP est constituée de 4 nombres allant de 0 à 255 représenté en binaire.<br><br>Le binaire correspond à une représentation en 2 caractères de chiffres ou de nombres (0 et 1).<br><br>Par exemple : 127.0.0.1 est une adresse IP écrite en base 10, compréhensible par l'humain mais pas par l'ordinateur.<br><br>Il faut pouvoir convertir ces nombres en représentation <strong>décimale</strong> en <strong>binaire</strong>.<br><br><strong>Voir partie binaire.</strong><br><br>L'adresse IP est constituée de 2 parties :<br><br>* La partie Réseau : elle permet d'identifier un réseau sur Internet.<br>* La partie Machine : elle permet d'identifier une machine sur le réseau défini.<br><br>Pour connaître ces deux parties, on utilise ce que l'on appelle un <strong>masque</strong>.<br>Il permet de définir la répartition du nombre de bits pour la partie Réseau. On pourra en déduire le nombre de bits réservés pour la partie Machine. On peut le représenter de diverses manières :<br><br>_______________________________________________________________________________________<br>_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________<br>______________________________________________________________________________________________________________________________________________________________________________<br><br><strong>Exemple :</strong> <br><br>On dispose de l'adresse <strong>128.40.94.3</strong> qui dispose d'un masque de 16 bits.  <br>Cela correspond en binaire à $10000000.00101000.01011110.00000100_2$.  <br>Cela veut dire que le masque est $11111111.11111111.00000000.00000000_2$.  <br><br>On peut donc définir que l'adresse du serveur est <strong>128.40.0.0</strong> et que cette adresse correspond à la machine <strong>94.3</strong> de ce réseau.<br><br>!!! Warning<br>    L'adresse réseau est très importante car deux machines sont dans le même réseau si elles ont la même adresse réseau.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">La communication entre deux machines</h3>
        <div class="course-content">
            On sait comment les machines se reconnaissent sur Internet (quelle sont les adresses) mais on veut savoir surtout comment des données transitent sur Internet pour aller d'une machine à une autre.<br><br>Pour échanger des données, on ne peut pas les envoyer de but en blanc. En effet, les données sont trop volumineuses pour être envoyées d'un coup, il faut les découper. On appelle <strong>paquet</strong> une découpe d'une donnée qui doit être échangée entre deux machines.<br><br>Le protocole TCP-IP permet la communication et l'échange de données sur Internet entre une machine <strong>émettrice</strong> et une <strong>réceptrice</strong>.<br><br>Ce protocole est composé de deux protocoles :<br><br>* Le protocole TCP permet le contrôle et la sécurité de l'envoi des paquets. Il permet d'être sur qu'un paquet est arrivé à destination à l'aide <strong>d'accusés de réceptions</strong>.<br>* Le protocole IP qui permet d'identifier quelles machines sur quels réseaux communiquent à l'aide de l'adresse IP.<br><br>Le protocole TCP-IP fonctionne en plusieurs étapes :<br><br>1. Le protocole découpe la donnée à échanger en plusieurs paquets composés de 0 et de 1 d'une certaine taille donnée et numérotés.<br>2. La donnée transite pour partir de la machine de départ à la machine de destination.<br>3. Tous les paquets sont reconstruits à l'aide de leur numérotation.<br>4. Enfin, un contrôle est réalisé par la machine de réception pour s'assurer que la donnée est bien <strong>intègre</strong>, c'est à dire que la donnée est bien correcte. Si la donnée n'est pas correcte, la machine de reception demande de renvoyer les paquets "défectueux".
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Recherches : Topologie de réseaux</h3>
        <div class="course-content">
            <strong>Réaliser une recherche sur une des topologies de réseaux suivantes :</strong><br><br>* Topologie étoile<br>* Topologie anneau<br>* Topologie bus<br>* Topologie maillé (pair à pair)<br><br><strong>Quelle topologie est la plus utilisée dans un usage domestique?</strong>
        </div>
    </div>
    
</div>