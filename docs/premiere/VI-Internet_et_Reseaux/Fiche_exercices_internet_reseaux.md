# Fiche d'exercices : Internet et Réseaux

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

.exercise-card {
    background: var(--md-default-bg-color);
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 3px solid;
    width: 100%;
    max-width: 100%;
    min-height: fit-content;
}

.exercise-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background-color: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.medium {
    background-color: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background-color: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.exercise-title {
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: var(--md-default-fg-color);
}

.exercise-content {
    color: var(--md-default-fg-color--light);
    line-height: 1.5;
    margin-bottom: 1rem;
}

.toggle-solution {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.toggle-solution:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution-wrapper {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
}

.solution-wrapper.show {
    max-height: 2000px;
    margin-top: 1rem;
}

.solution {
    background: rgba(102, 126, 234, 0.05);
    border-radius: 8px;
    padding: 1rem;
    border-left: 3px solid #667eea;
}

.solution pre {
    background: rgba(0, 0, 0, 0.05);
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
    margin: 0;
}

.solution code {
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
}
</style>

## 📚 Partie 1 : Modèle en couches et protocoles

<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 1 - Le modèle OSI</h4>
        <div class="exercise-content">
            <strong>Le modèle OSI comprend 7 couches. Associez chaque couche à sa fonction :</strong><br><br>
            <strong>Couches :</strong> Physique, Liaison, Réseau, Transport, Session, Présentation, Application<br><br>
            <strong>Fonctions :</strong><br>
            1. Transmission des bits sur le support physique<br>
            2. Routage des paquets entre réseaux<br>
            3. Interface avec l'utilisateur<br>
            4. Contrôle de flux et correction d'erreurs<br>
            5. Établissement et gestion des connexions<br>
            6. Chiffrement et compression des données<br>
            7. Transport fiable des données
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Associations correctes :</strong><br>
                • Physique → 1. Transmission des bits sur le support physique<br>
                • Liaison → 4. Contrôle de flux et correction d'erreurs<br>
                • Réseau → 2. Routage des paquets entre réseaux<br>
                • Transport → 7. Transport fiable des données<br>
                • Session → 5. Établissement et gestion des connexions<br>
                • Présentation → 6. Chiffrement et compression des données<br>
                • Application → 3. Interface avec l'utilisateur
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 2 - Adresses IP</h4>
        <div class="exercise-content">
            <strong>Répondez aux questions suivantes sur les adresses IP :</strong><br><br>
            1. Combien d'octets compose une adresse IPv4 ?<br>
            2. Quelle est la plage de valeurs possibles pour chaque octet ?<br>
            3. Donnez un exemple d'adresse IP privée<br>
            4. Quelle est la différence entre une adresse IP publique et privée ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Réponses :</strong><br>
                1. Une adresse IPv4 est composée de 4 octets<br>
                2. Chaque octet peut avoir une valeur de 0 à 255<br>
                3. Exemples d'adresses privées : 192.168.1.1, 10.0.0.1, 172.16.0.1<br>
                4. Les adresses publiques sont uniques sur Internet, les privées sont utilisées dans les réseaux locaux
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 3 - Protocoles réseau</h4>
        <div class="exercise-content">
            <strong>Pour chaque situation, indiquez le protocole utilisé :</strong><br><br>
            1. Envoi d'un email<br>
            2. Navigation sur un site web sécurisé<br>
            3. Transfert de fichiers<br>
            4. Résolution de nom de domaine<br>
            5. Attribution automatique d'adresse IP<br>
            6. Test de connectivité réseau
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Protocoles :</strong><br>
                1. SMTP (Simple Mail Transfer Protocol)<br>
                2. HTTPS (HTTP Secure)<br>
                3. FTP (File Transfer Protocol)<br>
                4. DNS (Domain Name System)<br>
                5. DHCP (Dynamic Host Configuration Protocol)<br>
                6. PING (utilise ICMP)
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 4 - Calcul de sous-réseaux</h4>
        <div class="exercise-content">
            <strong>Soit le réseau 192.168.1.0/24 :</strong><br><br>
            1. Combien d'adresses IP sont disponibles ?<br>
            2. Quelle est l'adresse de diffusion (broadcast) ?<br>
            3. Quelles sont les adresses utilisables pour les hôtes ?<br>
            4. Si on divise ce réseau en 4 sous-réseaux égaux, donnez les plages d'adresses
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Réponses :</strong><br>
                1. 256 adresses (de 192.168.1.0 à 192.168.1.255)<br>
                2. Adresse de diffusion : 192.168.1.255<br>
                3. Adresses utilisables : 192.168.1.1 à 192.168.1.254 (254 adresses)<br>
                4. Sous-réseaux (/26) :<br>
                   • 192.168.1.0/26 : 192.168.1.1-62<br>
                   • 192.168.1.64/26 : 192.168.1.65-126<br>
                   • 192.168.1.128/26 : 192.168.1.129-190<br>
                   • 192.168.1.192/26 : 192.168.1.193-254
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 5 - Routage et tables de routage</h4>
        <div class="exercise-content">
            <strong>Analysez cette table de routage et répondez aux questions :</strong><br><br>
            <pre>
Destination     Masque          Passerelle      Interface
0.0.0.0         0.0.0.0         192.168.1.1     eth0
192.168.1.0     255.255.255.0   0.0.0.0         eth0
10.0.0.0        255.0.0.0       192.168.1.254   eth0
            </pre><br>
            1. Que signifie la première ligne ?<br>
            2. Vers où sera routé un paquet destiné à 192.168.1.50 ?<br>
            3. Vers où sera routé un paquet destiné à 10.5.3.2 ?<br>
            4. Vers où sera routé un paquet destiné à 8.8.8.8 ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse :</strong><br>
                1. La première ligne est la route par défaut (0.0.0.0/0) vers la passerelle 192.168.1.1<br>
                2. 192.168.1.50 correspond au réseau local (192.168.1.0/24), envoi direct via eth0<br>
                3. 10.5.3.2 correspond au réseau 10.0.0.0/8, routé vers 192.168.1.254<br>
                4. 8.8.8.8 ne correspond à aucune route spécifique, utilise la route par défaut vers 192.168.1.1
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 6 - Analyse de trame Ethernet</h4>
        <div class="exercise-content">
            <strong>Analysez cette trame Ethernet (en hexadécimal) :</strong><br><br>
            <pre>FF FF FF FF FF FF 00 1A 2B 3C 4D 5E 08 00 45 00 00 1C ...</pre><br>
            1. Quelle est l'adresse MAC de destination ?<br>
            2. Quelle est l'adresse MAC source ?<br>
            3. Quel est le type de protocole encapsulé ?<br>
            4. S'agit-il d'une diffusion (broadcast) ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse de la trame :</strong><br>
                1. Adresse MAC destination : FF:FF:FF:FF:FF:FF<br>
                2. Adresse MAC source : 00:1A:2B:3C:4D:5E<br>
                3. Type de protocole : 0x0800 = IPv4<br>
                4. Oui, c'est une diffusion car l'adresse de destination est FF:FF:FF:FF:FF:FF
            </div>
        </div>
    </div>
</div>

## 📚 Partie 2 : Sécurité et chiffrement

<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 7 - Types de chiffrement</h4>
        <div class="exercise-content">
            <strong>Classez ces méthodes de chiffrement :</strong><br><br>
            AES, RSA, César, DES, Diffie-Hellman, Vigenère<br><br>
            <strong>Catégories :</strong><br>
            • Chiffrement symétrique<br>
            • Chiffrement asymétrique<br>
            • Chiffrement historique
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Classification :</strong><br>
                • <strong>Symétrique :</strong> AES, DES<br>
                • <strong>Asymétrique :</strong> RSA, Diffie-Hellman<br>
                • <strong>Historique :</strong> César, Vigenère
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 8 - Certificats et PKI</h4>
        <div class="exercise-content">
            <strong>Expliquez le rôle de chaque élément dans une PKI :</strong><br><br>
            1. Autorité de certification (CA)<br>
            2. Certificat numérique<br>
            3. Clé publique<br>
            4. Clé privée<br>
            5. Révocation de certificat
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Rôles :</strong><br>
                1. <strong>CA :</strong> Entité de confiance qui émet et signe les certificats<br>
                2. <strong>Certificat :</strong> Document électronique qui lie une identité à une clé publique<br>
                3. <strong>Clé publique :</strong> Clé partagée publiquement pour chiffrer ou vérifier des signatures<br>
                4. <strong>Clé privée :</strong> Clé secrète pour déchiffrer ou signer<br>
                5. <strong>Révocation :</strong> Processus d'invalidation d'un certificat compromis
            </div>
        </div>
    </div>
</div>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices
function toggleSolution(button) {
    const wrapper = button.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (wrapper.classList.contains('show')) {
        wrapper.classList.remove('show');
        arrow.textContent = '→';
        arrow.style.transform = 'rotate(0deg)';
    } else {
        wrapper.classList.add('show');
        arrow.textContent = '↓';
        arrow.style.transform = 'rotate(90deg)';
    }
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Aucune initialisation spécifique nécessaire pour cette fiche
});
</script>