<style>
/* Styles modernes pour le cours Internet et Réseaux */
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

.section-container {
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

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.layer-number {
    position: absolute;
    top: -10px;
    right: -10px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.layer-name {
    font-size: 1.2em;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
    padding-right: 30px;
}

.layer-description {
    color: #666;
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

.layer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.layer-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.layer-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.layer-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
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
    
    .model-grid {
        grid-template-columns: 1fr;
    }
    
    .layer-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🌐 Introduction aux réseaux</h1>
    <p class="course-subtitle">Comprendre les fondements de la communication numérique</p>
</div>

<div class="section-container">
    <h2 class="section-title">🔌 Qu'est-ce qu'un réseau internet</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Définitions Fondamentales</div>
        <div class="definition-content">
            Un <strong>réseau local</strong> est un ensemble de machines reliées entre elles qui échangent des informations en ne passant que par le routeur ou un switch.<br><br>
            Un <strong>réseau internet</strong> est un ensemble de réseaux locaux qui communiquent entre eux en passant par Internet.
        </div>
    </div>

    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">💻</div>
            <div class="model-name">Appareils Clients</div>
            <div class="model-description">
                Ordinateurs, smartphones, tablettes, consoles... Tous les appareils qui consomment ou produisent des données sur le réseau.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🏠</div>
            <div class="model-name">Objets Connectés (IoT)</div>
            <div class="model-description">
                Ensemble des objets connectés comme la domotique, capteurs intelligents, appareils électroménagers connectés.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Switch</div>
            <div class="model-description">
                Élément d'un réseau qui permet de relier les machines entre elles pour s'échanger des données dans un réseau local.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📡</div>
            <div class="model-name">Routeur</div>
            <div class="model-description">
                Élément qui permet de relier plusieurs réseaux entre eux et d'acheminer les données vers leur destination.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔗 Types de Connexions</div>
        <div class="definition-content">
            Les machines sont reliées par différents moyens de communication :
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🔌</div>
            <div class="model-name">Câbles RJ45</div>
            <div class="model-description">
                Connexion filaire standard pour les réseaux Ethernet, offrant une connexion stable et rapide.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📶</div>
            <div class="model-name">Ondes Radio</div>
            <div class="model-description">
                WiFi (Wireless Fidelity), 5G, Bluetooth... Connexions sans fil pour la mobilité et la flexibilité.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">💡</div>
            <div class="model-name">Fibre Optique</div>
            <div class="model-description">
                Transmission par signaux lumineux, offrant les débits les plus élevés pour les longues distances.
            </div>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">📋 Protocoles de Communication</div>
        <div class="definition-content">
            La communication est définie et régie par des <strong>protocoles</strong>.<br>
            Un protocole est un ensemble de règles et d'actions prédéfinies à réaliser dans un ordre précis.
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🌍 Distinction Web et Internet</h2>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🌐</div>
            <div class="model-name">Internet</div>
            <div class="model-description">
                Correspond à <strong>l'ensemble des réseaux organisés</strong> communiquant ensemble. C'est l'infrastructure physique et logique mondiale.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🕸️</div>
            <div class="model-name">Web</div>
            <div class="model-description">
                Correspond à une application d'Internet qui rend accessible des ressources grâce aux <strong>liens hypertextes</strong> (hyperliens).
            </div>
        </div>
    </div>
    
    <h3 class="section-title">🔄 Topologies de Réseaux</h3>
    
    <div class="definition-box">
        <div class="definition-title">📐 Concept de Topologie</div>
        <div class="definition-content">
            Une topologie dans les réseaux correspond à la disposition des machines dans un réseau.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">⭕</div>
            <div class="model-name">Anneau</div>
            <div class="model-description">
                Chaque machine est connectée à deux autres, formant un cercle fermé. Les données circulent dans une direction.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⭐</div>
            <div class="model-name">Étoile</div>
            <div class="model-description">
                Toutes les machines sont connectées à un point central (switch/hub). Topologie la plus utilisée domestiquement.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">Bus</div>
            <div class="model-description">
                Toutes les machines partagent un même câble de communication principal.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🌳</div>
            <div class="model-name">Hiérarchique</div>
            <div class="model-description">
                Structure arborescente avec plusieurs niveaux de connexions, du plus général au plus spécifique.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🤝</div>
            <div class="model-name">P2P (Pair-à-Pair)</div>
            <div class="model-description">
                Chaque machine peut communiquer directement avec toutes les autres sans point central.
            </div>
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🔍 Adresses MAC et IP</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Systèmes d'Adressage</div>
        <div class="definition-content">
            Pour identifier et localiser les machines sur un réseau, deux types d'adresses sont utilisés : les adresses MAC (physiques) et les adresses IP (logiques).
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">💳</div>
            <div class="model-name">Adresse MAC</div>
            <div class="model-description">
                <strong>Media Access Control</strong> - Adresse physique d'une interface de carte réseau, <strong>unique</strong> et propre à la carte.<br><br>
                <strong>Format :</strong> 6 groupes de 16 bits en hexadécimal<br>
                <strong>Exemple :</strong> a8:9f:d9:4c:5c:d9<br><br>
                <em>Le switch utilise l'adresse MAC pour retransmettre les données à la bonne machine.</em>
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🌐</div>
            <div class="model-name">Adresse IP</div>
            <div class="model-description">
                Adresse logique d'une machine sur un réseau, attribuée à la première connexion.<br><br>
                <strong>Format :</strong> 4 octets en décimal<br>
                <strong>Exemple humain :</strong> 123.32.41.74<br>
                <strong>Exemple machine :</strong> 01111011.00100000.00101001.01001010<br><br>
                <em>Permet 2³² = 4 294 967 296 adresses différentes.</em>
            </div>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">🔧 Composition d'une Adresse IP</div>
        <div class="definition-content">
            Une adresse IP est composée de deux parties :
            <ul>
                <li><strong>L'adresse du réseau</strong> : Partie commune à toutes les machines du réseau</li>
                <li><strong>L'adresse de la machine</strong> : Partie spécifique à chaque machine du réseau</li>
            </ul>
            Ces deux parties sont distinguées par le nombre de bits qui leurs sont associés.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🎭 Masque de Sous-réseau</div>
        <div class="definition-content">
            On définit un <strong>masque</strong> comme étant le nombre de bits nécessaires pour représenter l'adresse du réseau.<br>
            Pour retrouver l'adresse du réseau, on réalise une opération logique <strong>ET</strong> sur chacun des bits.<br>
            Ce masque est représenté à la fin de l'adresse IP précédée d'un / (slash), appelé notation <strong>CIDR</strong>.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💡 Exemple de Calcul d'Adresse Réseau</div>
        Adresse : 123.32.41.74/16 (16 bits pour l'adresse réseau)<br><br>
        Masque : 11111111.11111111.00000000.00000000<br>
        Adresse : 01111011.00100000.00101001.01001010<br><br>
        ET logique :<br>
        11111111.11111111.00000000.00000000<br>
        01111011.00100000.00101001.01001010<br>
        ────────────────────────────────────<br>
        01111011.00100000.00000000.00000000<br><br>
        Résultat : 123.32.0.0 (adresse du réseau)
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Adresses Réservées</strong><br>
        • L'adresse du réseau (inutilisable pour les machines)<br>
        • L'adresse de broadcast (se termine par 255, pour diffusion générale)
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Calcul du nombre de machines</strong><br>
        Nombre d'adresses disponibles = 2^(nombre de bits partie machine) - 2<br>
        Exemple : 16 bits machine → 2^16 - 2 = 65 534 machines possibles
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">📊 Classes d'Adresses IP</h2>
    
    <div class="definition-box">
        <div class="definition-title">📚 Classification Historique</div>
        <div class="definition-content">
            Historiquement, les adresses IP étaient regroupées en classes pour leur attribution à divers organismes.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🅰️</div>
            <div class="model-name">Classe A</div>
            <div class="model-description">
                <strong>Plage :</strong> 1.0.0.0 - 126.0.0.0<br>
                <strong>Réseaux :</strong> 128<br>
                <strong>Hôtes/réseau :</strong> 16 777 214<br>
                <strong>Usage :</strong> Réseaux très grands (gouvernements, grandes entreprises)
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🅱️</div>
            <div class="model-name">Classe B</div>
            <div class="model-description">
                <strong>Plage :</strong> 128.0.0.0 - 191.255.0.0<br>
                <strong>Réseaux :</strong> 16 384<br>
                <strong>Hôtes/réseau :</strong> 65 534<br>
                <strong>Usage :</strong> Réseaux moyens (universités, entreprises moyennes)
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🅲</div>
            <div class="model-name">Classe C</div>
            <div class="model-description">
                <strong>Plage :</strong> 192.0.0.0 - 223.255.255.0<br>
                <strong>Réseaux :</strong> 2 097 152<br>
                <strong>Hôtes/réseau :</strong> 254<br>
                <strong>Usage :</strong> Petits réseaux (petites entreprises)
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📡</div>
            <div class="model-name">Classe D</div>
            <div class="model-description">
                <strong>Plage :</strong> 224.0.0.0 - 239.255.255.255<br>
                <strong>Usage :</strong> Multicast (transmission vers plusieurs destinataires simultanément)
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔬</div>
            <div class="model-name">Classe E</div>
            <div class="model-description">
                <strong>Plage :</strong> 240.0.0.0 - 255.255.255.255<br>
                <strong>Usage :</strong> Réservé pour utilisations futures et expérimentales
            </div>
        </div>
    </div>

</div>

<div class="section-container">
    <h2 class="section-title">🌐 IPv6 - Évolution du Protocole</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚀 Nécessité d'IPv6</div>
        <div class="definition-content">
            Le protocole IPv4 permet de définir 2³² adresses (≈ 4 milliards). Avec l'explosion du nombre d'appareils connectés, ce nombre devient insuffisant.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">IPv4 vs IPv6</div>
            <div class="model-description">
                <strong>IPv4 :</strong> 32 bits → 2³² ≈ 4 milliards d'adresses<br>
                <strong>IPv6 :</strong> 128 bits → 2¹²⁸ ≈ 3,4 × 10³⁸ adresses<br><br>
                <strong>Format IPv6 :</strong> 8 groupes de 4 chiffres hexadécimaux<br>
                <strong>Exemple :</strong> 2001:0db8:85a3:0000:0000:8a2e:0370:7334
            </div>
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🏠 Adresses Privées</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔒 Réseaux Locaux</div>
        <div class="definition-content">
            Certaines plages d'adresses IP sont réservées pour un usage privé (réseaux locaux) et ne sont pas routées sur Internet.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🅰️</div>
            <div class="model-name">Classe A Privée</div>
            <div class="model-description">
                <strong>Plage :</strong> 10.0.0.0 à 10.255.255.255<br>
                <strong>Masque :</strong> 255.0.0.0 (/8)<br>
                <strong>Usage :</strong> Grands réseaux privés
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🅱️</div>
            <div class="model-name">Classe B Privée</div>
            <div class="model-description">
                <strong>Plage :</strong> 172.16.0.0 à 172.31.255.255<br>
                <strong>Masque :</strong> 255.240.0.0 (/12)<br>
                <strong>Usage :</strong> Réseaux privés moyens
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🅲</div>
            <div class="model-name">Classe C Privée</div>
            <div class="model-description">
                <strong>Plage :</strong> 192.168.0.0 à 192.168.255.255<br>
                <strong>Masque :</strong> 255.255.0.0 (/16)<br>
                <strong>Usage :</strong> Petits réseaux domestiques/entreprise
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Avantage des Adresses Privées</strong><br>
        Permettent aux réseaux locaux d'utiliser des adresses IP sans risquer de conflit avec les adresses publiques d'Internet.
    </div>

</div>

<div class="section-container">
    <h2 class="section-title">🏗️ Modèle TCP/IP</h2>
    
    <div class="image-container">
        <img src="Modele_IP.png" alt="Modèle TCP/IP">
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📡 Protocole de Communication</div>
        <div class="definition-content">
            Le modèle TCP/IP est un modèle en couche qui permet d'illustrer l'encapsulation des données pour permettre leur envoi, leur réception et leur traitement.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📦 Processus d'Encapsulation</div>
        <div class="definition-content">
            L'encapsulation est un concept clé du modèle TCP/IP :
            <ol>
                <li>Les données sont générées au niveau de la couche Application</li>
                <li>Chaque couche inférieure ajoute ses propres informations (en-têtes)</li>
                <li>À la réception, chaque couche retire ses informations</li>
                <li>Les données sont reconstituées dans leur état original</li>
            </ol>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Analogie Postale</strong><br>
        On peut comparer le modèle TCP/IP à un système postal :<br>
        • Couche Application = Rédaction de la lettre<br>
        • Couche Transport = Mise sous enveloppe, numérotation<br>
        • Couche Internet = Adressage, choix de l'acheminement<br>
        • Couche Accès Réseau = Distribution physique
    </div>
    
    <h3 class="section-title">🔧 Structure des Couches</h3>
    
    <div class="layer-grid">
        <div class="layer-card">
            <div class="layer-number">1</div>
            <div class="layer-name">Couche Accès Réseau</div>
            <div class="layer-description">
                Gère la transmission physique des données sur le réseau local. Combine les fonctions des couches physique et liaison de données du modèle OSI.
                <br><br>
                <strong>Fonctions :</strong><br>
                • Transmission des bits sur le support physique<br>
                • Détection et correction d'erreurs<br>
                • Contrôle d'accès au support<br>
                • Adressage physique (MAC)<br><br>
                <strong>Protocoles :</strong> Ethernet, Wi-Fi, Bluetooth
            </div>
        </div>
        
        <div class="layer-card">
            <div class="layer-number">2</div>
            <div class="layer-name">Couche Internet</div>
            <div class="layer-description">
                Responsable du routage des paquets à travers différents réseaux pour atteindre leur destination.
                <br><br>
                <strong>Fonctions :</strong><br>
                • Adressage logique (IP)<br>
                • Routage des paquets<br>
                • Fragmentation et réassemblage<br>
                • Contrôle de congestion<br><br>
                <strong>Protocoles :</strong> IP (IPv4/IPv6), ICMP, ARP
            </div>
        </div>
        
        <div class="layer-card">
            <div class="layer-number">3</div>
            <div class="layer-name">Couche Transport</div>
            <div class="layer-description">
                Assure la transmission fiable des données entre les applications.
                <br><br>
                <strong>Fonctions :</strong><br>
                • Segmentation et réassemblage des données<br>
                • Contrôle de flux<br>
                • Détection et correction d'erreurs<br>
                • Multiplexage des connexions<br><br>
                <strong>Protocoles :</strong><br>
                • <strong>TCP</strong> : Fiable, avec contrôle d'erreurs<br>
                • <strong>UDP</strong> : Rapide, sans garantie de livraison
            </div>
        </div>
        
        <div class="layer-card">
            <div class="layer-number">4</div>
            <div class="layer-name">Couche Application</div>
            <div class="layer-description">
                Fournit les services réseau directement aux applications utilisateur.
                <br><br>
                <strong>Fonctions :</strong><br>
                • Interface avec les applications<br>
                • Services de haut niveau<br>
                • Formatage et présentation des données<br><br>
                <strong>Protocoles :</strong> HTTP/HTTPS, FTP, SMTP, DNS, SSH
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">⚙️ Fonctionnement</div>
        <div class="definition-content">
            Chaque couche a sa tâche prédéfinie, notamment grâce aux protocoles qui sont en jeu.
        </div>
    </div>