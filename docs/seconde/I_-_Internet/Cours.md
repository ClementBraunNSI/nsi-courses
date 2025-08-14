<style>
/* Styles modernes pour le cours Internet */
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
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🌐 Internet</h1>
    <p class="course-subtitle">L'histoire et le fonctionnement du réseau mondial</p>
</div>

<div class="timeline-section">
    <h2 class="timeline-title">📅 L'Histoire d'Internet : Des Pionniers à la Révolution Mondiale</h2>
    
    <div class="timeline-grid">
        <div class="timeline-card">
            <div class="timeline-year">1960s</div>
            <div class="timeline-event">Les Pionniers d'ARPANET</div>
            <div class="timeline-description">
                L'idée révolutionnaire de relier des machines pour échanger des données naît dans les laboratoires et universités. Robert Kahn dirige le projet ARPANET pour la Defense Advanced Research Projects Agency.
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1969</div>
            <div class="timeline-event">Premier Message de l'Histoire</div>
            <div class="timeline-description">
                Le 20 septembre 1969, la première communication voit le jour entre l'université de Californie et Stanford. Le premier message transmis était simplement "login".
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1970-80s</div>
            <div class="timeline-event">Naissance des Protocoles</div>
            <div class="timeline-description">
                Développement des règles de communication appelées "protocoles". Ces normes permettent aux machines de communiquer de manière standardisée.
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1983</div>
            <div class="timeline-event">Révolution TCP/IP</div>
            <div class="timeline-description">
                Installation du protocole TCP/IPv4 sur ARPANET. Création simultanée des règles des systèmes de nom de domaine (DNS).
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">1990s</div>
            <div class="timeline-event">Explosion du Web</div>
            <div class="timeline-description">
                Tim Berners-Lee et Robert Cailliau créent le World Wide Web au CERN en Suisse, révolutionnant l'accès à l'information.
            </div>
            <div class="image-container">
                <img src="../img/tblrc.jpeg" alt="Tim Berners-Lee et Robert Cailliau" />
            </div>
        </div>
        
        <div class="timeline-card">
            <div class="timeline-year">Aujourd'hui</div>
            <div class="timeline-event">Internet Mondial</div>
            <div class="timeline-description">
                Plus de 4 milliards d'internautes connectés, échangeant emails, fichiers et accédant à une quantité incommensurable de données.
            </div>
        </div>
    </div>
    
    <div class="image-container">
        <img src="../img/arpanet.jpeg" alt="Réseau ARPANET" />
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Le saviez-vous ?</strong> L'objectif initial était de relier seulement trois universités : Stanford, Los Angeles et l'Utah.
    </div>
    
    
    
    <div class="image-container">
        <img src="../img/geo-mercator.svg" width = "70%" alt="Carte mondiale d'Internet" />
    </div>
</div>

<div class="definition-box">
    <div class="definition-title">🎯 Définition : Internet</div>
    <div class="definition-content">
        <strong>Internet</strong> est un réseau informatique à échelle mondiale sur lequel de nombreuses applications sont basées (email, transfert de fichiers, navigation web, etc.).
    </div>
</div>

<style>
.network-section {
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

.components-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.component-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.component-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.component-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.component-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.component-role {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.component-examples {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 8px;
    padding: 0.8rem;
    font-size: 0.85rem;
    color: #667eea;
    font-weight: 500;
}

.network-types {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.network-type-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.network-type-title {
    font-size: 1.1rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 0.5rem;
}

.network-type-description {
    color: #7f8c8d;
    font-size: 0.9rem;
}

.question-box {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.05));
    border-left: 5px solid #ffc107;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.question-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    font-weight: 500;
    text-align: center;
}

@media (max-width: 768px) {
    .components-grid {
        grid-template-columns: 1fr;
    }
    
    .network-types {
        grid-template-columns: 1fr;
    }
}
</style>

<div class="network-section">
    <h2 class="section-title">🔧 Anatomie d'un Réseau Informatique</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Définition : Réseau Informatique</div>
        <div class="definition-content">
            Un <strong>réseau informatique</strong> est un ensemble de machines reliées, par différents moyens, qui communiquent entre elles pour échanger des données ou des informations.
        </div>
    </div>
    
    <h3 style="text-align: center; color: #667eea; margin: 2rem 0;">🧩 Les Composants Essentiels</h3>
    
    <div class="components-grid">
        <div class="component-card">
            <div class="component-icon">💻</div>
            <div class="component-name">Machines</div>
            <div class="component-role">
                Éléments qui cherchent à communiquer, envoyer ou recevoir des données
            </div>
            <div class="component-examples">
                📱 Ordinateurs, tablettes, consoles, smartphones
            </div>
        </div>
        
        <div class="component-card">
            <div class="component-icon">🔀</div>
            <div class="component-name">Switch</div>
            <div class="component-role">
                Élément qui relie de manière locale des machines dans un même réseau
            </div>
            <div class="component-examples">
                🏠 Box internet, switch RJ45
            </div>
        </div>
        
        <div class="component-card">
            <div class="component-icon">🌐</div>
            <div class="component-name">Routeur</div>
            <div class="component-role">
                Élément qui permet de relier un réseau local à Internet ou d'autres réseaux
            </div>
            <div class="component-examples">
                🔗 Box internet, routeur spécialisé
            </div>
        </div>
        
        <div class="component-card">
            <div class="component-icon">📡</div>
            <div class="component-name">Supports de Transmission</div>
            <div class="component-role">
                Éléments qui permettent de relier les diverses machines au switch ou au routeur
            </div>
            <div class="component-examples">
                🔌 Câble Ethernet, Fibre optique, WiFi
            </div>
        </div>
    </div>
    
    <h3 style="text-align: center; color: #667eea; margin: 2rem 0;">🗺️ Typologie des Réseaux</h3>
    
    <div class="network-types">
        <div class="network-type-card">
            <div class="network-type-title">🏠 Réseau Local (LAN)</div>
            <div class="network-type-description">
                Réseau localisé dans une même zone géographique (maison, bureau, école)
            </div>
        </div>
        
        <div class="network-type-card">
            <div class="network-type-title">🌍 Réseau Internet (WAN)</div>
            <div class="network-type-description">
                Réseau accessible à Internet, connectant des réseaux locaux du monde entier
            </div>
        </div>
    </div>
    
    <div class="image-container">
        <img src="../img/rlinternet.png" alt="Schéma réseau local et Internet" />
    </div>
    
    <div class="question-box">
        <div class="question-content">
            🤔 <strong>Question clé :</strong> On dispose de machines et d'un réseau, mais comment se retrouvent-elles pour communiquer ? Quelles techniques sont utilisées ?
        </div>
    </div>
</div>

<style>
.addressing-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.address-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.address-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.address-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.address-type {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
}

.address-description {
    color: #7f8c8d;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.address-characteristics {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
}

.characteristic-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.characteristic-item:last-child {
    border-bottom: none;
}

.characteristic-label {
    font-weight: 500;
    color: #2c3e50;
}

.characteristic-value {
    font-weight: bold;
    color: #667eea;
}

.example-box {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #2c3e50;
}

.ip-structure {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.ip-parts {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 1rem 0;
}

.ip-part {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
}

.ip-part-title {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 0.5rem;
}

.ip-part-description {
    color: #7f8c8d;
    font-size: 0.9rem;
}

.calculation-example {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.calculation-step {
    margin: 1rem 0;
    padding: 0.8rem;
    background: rgba(102, 126, 234, 0.05);
    border-radius: 8px;
    font-family: 'Courier New', monospace;
}

.warning-box {
    background: linear-gradient(135deg, rgba(255, 87, 34, 0.1), rgba(255, 152, 0, 0.05));
    border-left: 5px solid #ff5722;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.warning-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    font-weight: 500;
}

@media (max-width: 768px) {
    .address-cards {
        grid-template-columns: 1fr;
    }
    
    .ip-parts {
        grid-template-columns: 1fr;
    }
}
</style>

<div class="addressing-section">
    <h2 class="section-title">🏷️ L'Adressage dans les Réseaux</h2>
    
    <div class="address-cards">
        <div class="address-card">
            <div class="address-type">🔗 Adressage Local : MAC</div>
            <div class="address-description">
                Une machine dispose d'une ou plusieurs <strong>cartes réseaux</strong> qui permettent de communiquer localement ou globalement vers Internet. Chaque carte possède une adresse unique.
            </div>
            
            <div class="definition-box">
                <div class="definition-title">📍 Adresse MAC</div>
                <div class="definition-content">
                    L'adresse <strong>MAC (Media Access Control)</strong> est aussi appelée <strong>adresse physique</strong> car elle correspond à l'adresse utilisée par le port Ethernet et le protocole Ethernet.
                </div>
            </div>
            
            <div class="address-characteristics">
                <div class="characteristic-item">
                    <span class="characteristic-label">Format</span>
                    <span class="characteristic-value">6 blocs de 2 caractères</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Base</span>
                    <span class="characteristic-value">Hexadécimale (16 caractères)</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Portée</span>
                    <span class="characteristic-value">Réseau local uniquement</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Unicité</span>
                    <span class="characteristic-value">Unique au monde</span>
                </div>
            </div>
            
            <div class="example-box">
                💡 Exemple : a1:b2:c3:d4:e5:f6
            </div>
            
            <div class="highlight-fact">
                🔢 <strong>Base hexadécimale :</strong> Représentation en 16 caractères (0-9, A-F)
            </div>
        </div>
        
        <div class="address-card">
            <div class="address-type">🌐 Adressage Internet : IP</div>
            <div class="address-description">
                Pour qu'un réseau soit accessible sur Internet, chaque machine doit posséder une adresse unique permettant de l'identifier parmi des milliards d'autres.
            </div>
            
            <div class="definition-box">
                <div class="definition-title">🎯 Adresse IP</div>
                <div class="definition-content">
                    L'<strong>Adresse IP (Internet Protocol)</strong> est constituée de 4 nombres allant de 0 à 255, représentés en binaire par l'ordinateur mais affichés en décimal pour l'humain.
                </div>
            </div>
            
            <div class="address-characteristics">
                <div class="characteristic-item">
                    <span class="characteristic-label">Format</span>
                    <span class="characteristic-value">4 nombres (0-255)</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Base humaine</span>
                    <span class="characteristic-value">Décimale (base 10)</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Base machine</span>
                    <span class="characteristic-value">Binaire (0 et 1)</span>
                </div>
                <div class="characteristic-item">
                    <span class="characteristic-label">Portée</span>
                    <span class="characteristic-value">Internet mondial</span>
                </div>
            </div>
            
            <div class="example-box">
                💡 Exemple : 127.0.0.1 (localhost)
            </div>
        </div>
    </div>
    
    <div class="ip-structure">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1.5rem;">🧩 Structure d'une Adresse IP</h3>
        
        <div class="ip-parts">
            <div class="ip-part">
                <div class="ip-part-title">🏠 Partie Réseau</div>
                <div class="ip-part-description">
                    Identifie un réseau spécifique sur Internet
                </div>
            </div>
            <div class="ip-part">
                <div class="ip-part-title">💻 Partie Machine</div>
                <div class="ip-part-description">
                    Identifie une machine sur le réseau défini
                </div>
            </div>
        </div>
        
        <div class="highlight-fact">
            🎭 <strong>Le Masque :</strong> Permet de définir la répartition des bits entre la partie réseau et la partie machine
        </div>
    </div>
    
    <div class="calculation-example">
        <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Exemple de Calcul</h4>
        
        <div class="highlight-fact">
            Adresse : <strong>128.40.94.3</strong> avec un masque de <strong>16 bits</strong>
        </div>
        
        <div class="calculation-step">
            <strong>En binaire :</strong> 10000000.00101000.01011110.00000100
        </div>
        
        <div class="calculation-step">
            <strong>Masque :</strong> 11111111.11111111.00000000.00000000
        </div>
        
        <div class="calculation-step">
            <strong>Adresse réseau :</strong> 128.40.0.0
        </div>
        
        <div class="calculation-step">
            <strong>Adresse machine :</strong> 94.3
        </div>
    </div>
    
    <div class="warning-box">
        <div class="warning-content">
            ⚠️ <strong>Important :</strong> L'adresse réseau est cruciale car deux machines sont dans le même réseau si et seulement si elles ont la même adresse réseau.
        </div>
    </div>
</div>

<style>
.protocol-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.protocol-intro {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.protocol-intro h2 {
    color: #667eea;
    font-size: 2rem;
    margin-bottom: 1rem;
}

.protocol-intro p {
    color: #7f8c8d;
    font-size: 1.1rem;
    line-height: 1.6;
}

.layers-container {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.layers-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    margin: 2rem 0;
}

.layer-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.layer-card:hover {
    transform: translateX(10px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.layer-card::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: linear-gradient(to bottom, #667eea, #764ba2);
}

.layer-number {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #667eea;
    color: white;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.9rem;
}

.layer-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 0.5rem;
    margin-right: 3rem;
}

.layer-description {
    color: #7f8c8d;
    font-size: 1rem;
    line-height: 1.5;
}

.process-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin: 2rem 0;
}

.process-card {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.process-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
}

.process-description {
    color: #7f8c8d;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.process-flow {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    align-items: center;
}

.flow-step {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 8px;
    padding: 0.8rem 1.5rem;
    color: #2c3e50;
    font-weight: 500;
    border: 1px solid rgba(102, 126, 234, 0.2);
    width: 100%;
    text-align: center;
}

.flow-arrow {
    color: #667eea;
    font-size: 1.5rem;
    font-weight: bold;
}

.note-box {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(139, 195, 74, 0.05));
    border-left: 5px solid #4caf50;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.note-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.note-title {
    color: #4caf50;
    font-weight: bold;
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

@media (max-width: 768px) {
    .process-container {
        grid-template-columns: 1fr;
    }
    
    .layer-card:hover {
        transform: translateY(-5px);
    }
}
</style>

<div class="protocol-section">
    <div class="protocol-intro">
        <h2>🌐 Le Protocole TCP-IP</h2>
        <p>
            Maintenant que nous savons comment les machines se reconnaissent sur Internet grâce aux adresses, 
            découvrons comment les données transitent réellement d'une machine à une autre à travers le monde.
        </p>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔗 Protocole TCP-IP</div>
        <div class="definition-content">
            Le protocole <strong>TCP-IP</strong> est un protocole de communication qui permet l'échange de données entre machines sur Internet. 
            Il constitue le langage universel d'Internet, permettant à des milliards d'appareils de communiquer ensemble.
        </div>
    </div>
    
    <div class="layers-container">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 2rem;">🏗️ Les 4 Couches du Protocole TCP-IP</h3>
        
        <div class="layers-grid">
            <div class="layer-card">
                <div class="layer-number">4</div>
                <div class="layer-title">📱 Couche Application</div>
                <div class="layer-description">
                    Correspond aux logiciels qui utilisent le réseau : navigateur web, logiciel de messagerie, 
                    applications mobiles, jeux en ligne, etc.
                </div>
            </div>
            
            <div class="layer-card">
                <div class="layer-number">3</div>
                <div class="layer-title">🚛 Couche Transport</div>
                <div class="layer-description">
                    S'occupe du transport des données et de leur intégrité. Garantit que les données arrivent 
                    complètes et dans le bon ordre.
                </div>
            </div>
            
            <div class="layer-card">
                <div class="layer-number">2</div>
                <div class="layer-title">🗺️ Couche Internet</div>
                <div class="layer-description">
                    S'occupe de l'adressage et du routage des données. Détermine le chemin optimal 
                    pour faire transiter les données.
                </div>
            </div>
            
            <div class="layer-card">
                <div class="layer-number">1</div>
                <div class="layer-title">🔌 Couche Accès Réseau</div>
                <div class="layer-description">
                    S'occupe de la transmission physique des données : câbles, WiFi, fibre optique, 
                    signaux électriques ou lumineux.
                </div>
            </div>
        </div>
    </div>
    
    <div class="process-container">
        <div class="process-card">
            <div class="process-title">📦 Encapsulation</div>
            <div class="process-description">
                Lorsqu'on <strong>envoie</strong> des données, elles "descendent" les couches 
                en se faisant encapsuler (ajouter des informations) à chaque étape.
            </div>
            
            <div class="process-flow">
                <div class="flow-step">📱 Application : Données utilisateur</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">🚛 Transport : + En-tête TCP</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">🗺️ Internet : + En-tête IP</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">🔌 Accès réseau : + En-tête Ethernet</div>
            </div>
        </div>
        
        <div class="process-card">
            <div class="process-title">📂 Désencapsulation</div>
            <div class="process-description">
                Lorsqu'on <strong>reçoit</strong> des données, elles "remontent" les couches 
                en se faisant désencapsuler (retirer des informations) à chaque étape.
            </div>
            
            <div class="process-flow">
                <div class="flow-step">🔌 Accès réseau : - En-tête Ethernet</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">🗺️ Internet : - En-tête IP</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">🚛 Transport : - En-tête TCP</div>
                <div class="flow-arrow">⬇️</div>
                <div class="flow-step">📱 Application : Données utilisateur</div>
            </div>
        </div>
    </div>
    
    <div class="note-box">
        <div class="note-title">💡 Pourquoi TCP-IP est-il si important ?</div>
        <div class="note-content">
            Le protocole TCP-IP est le fondement d'Internet car il permet de faire communiquer des machines 
            de différents types (ordinateurs, smartphones, serveurs, objets connectés, etc.) sur un réseau mondial. 
            C'est grâce à ce protocole universel que vous pouvez consulter un site web hébergé au Japon 
            depuis votre smartphone en France !
        </div>
    </div>
</div>
