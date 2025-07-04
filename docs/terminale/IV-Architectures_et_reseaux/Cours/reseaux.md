# Réseaux informatiques

    🌐 Réseaux informatiques
    Communication et interconnexion des systèmes

## I. Concepts fondamentaux

🔗 Qu'est-ce qu'un réseau ?

Un réseau informatique est un ensemble d'équipements interconnectés qui peuvent communiquer entre eux pour partager des ressources et échanger des informations.

### Types de réseaux par étendue

- **PAN** (Personal Area Network) : Réseau personnel (Bluetooth, USB)
- **LAN** (Local Area Network) : Réseau local (entreprise, domicile)
- **MAN** (Metropolitan Area Network) : Réseau métropolitain (ville)
- **WAN** (Wide Area Network) : Réseau étendu (Internet)

### Topologies de réseaux

    🌟 Étoile
    Tous les nœuds connectés à un hub central
    Avantages : Facile à gérer
    Inconvénients : Point de défaillance unique

    🔄 Anneau
    Nœuds connectés en boucle fermée
    Avantages : Pas de collision
    Inconvénients : Panne d'un nœud = panne totale

    🕸️ Maillé
    Chaque nœud connecté à plusieurs autres
    Avantages : Très fiable
    Inconvénients : Coûteux

    🚌 Bus
    Tous les nœuds sur un même câble
    Avantages : Simple et économique
    Inconvénients : Collisions possibles

## II. Modèle OSI et pile TCP/IP

📚 Modèle en couches

Les modèles en couches permettent de structurer et standardiser les communications réseau en divisant les fonctionnalités en niveaux distincts.

### Modèle OSI (7 couches)

7. Application (HTTP, FTP, SMTP)
6. Présentation (Chiffrement, Compression)
5. Session (Gestion des sessions)
4. Transport (TCP, UDP)
3. Réseau (IP, ICMP)
2. Liaison (Ethernet, WiFi)
1. Physique (Câbles, Signaux)

### Pile TCP/IP (4 couches)

Application (HTTP, FTP, DNS)
Transport (TCP, UDP)
Internet (IP, ICMP)
Accès réseau (Ethernet, WiFi)

Encapsulation :

Chaque couche ajoute ses propres en-têtes aux données :
- **Application** : Données
- **Transport** : Segment (TCP) ou Datagramme (UDP)
- **Internet** : Paquet IP
- **Accès réseau** : Trame

## III. Protocoles de la couche réseau

### Protocole IP (Internet Protocol)

📍 Adressage IP

Le protocole IP fournit un système d'adressage unique pour identifier chaque machine sur Internet.

#### IPv4

**Format :** 4 octets (32 bits) - `192.168.1.1`

ClassePlageMasque par défautUsage
A1.0.0.0 - 126.255.255.255/8 (255.0.0.0)Très grands réseaux
B128.0.0.0 - 191.255.255.255/16 (255.255.0.0)Réseaux moyens
C192.0.0.0 - 223.255.255.255/24 (255.255.255.0)Petits réseaux

**Adresses privées (RFC 1918) :**
- `10.0.0.0/8` (10.0.0.0 - 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 - 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 - 192.168.255.255)

Calcul de sous-réseaux :

Réseau : `192.168.1.0/24`
- Adresse réseau : `192.168.1.0`
- Masque : `255.255.255.0` ou `/24`
- Première adresse utilisable : `192.168.1.1`
- Dernière adresse utilisable : `192.168.1.254`
- Adresse de diffusion : `192.168.1.255`
- Nombre d'hôtes : 254

#### IPv6

**Format :** 8 groupes de 4 chiffres hexadécimaux (128 bits)

# Exemples d'adresses IPv6
2001:0db8:85a3:0000:0000:8a2e:0370:7334  # Format complet
2001:db8:85a3::8a2e:370:7334             # Format compressé
::1                                       # Loopback (équivalent à 127.0.0.1)
::                                        # Adresse nulle
fe80::1                                   # Lien local

**Avantages d'IPv6 :**
- Espace d'adressage quasi-illimité
- Configuration automatique
- Sécurité intégrée (IPSec)
- Qualité de service améliorée

### Routage

🗺️ Acheminement des paquets

Le routage détermine le chemin optimal pour acheminer les paquets de la source vers la destination.

#### Algorithmes de routage

**1. Routage statique :**
- Routes configurées manuellement
- Adapté aux petits réseaux stables

**2. Routage dynamique :**
- **RIP** (Routing Information Protocol) : Vecteur de distance
- **OSPF** (Open Shortest Path First) : État de liens
- **BGP** (Border Gateway Protocol) : Routage inter-domaines

# Commandes de routage Linux

# Afficher la table de routage
route -n
ip route show

# Ajouter une route statique
sudo route add -net 192.168.2.0/24 gw 192.168.1.1
sudo ip route add 192.168.2.0/24 via 192.168.1.1

# Route par défaut
sudo route add default gw 192.168.1.1
sudo ip route add default via 192.168.1.1

### NAT (Network Address Translation)

Principe du NAT :

Le NAT permet à plusieurs machines d'un réseau privé de partager une seule adresse IP publique pour accéder à Internet.

**Types de NAT :**
- **NAT statique** : Correspondance 1:1 fixe
- **NAT dynamique** : Pool d'adresses publiques
- **PAT** (Port Address Translation) : Multiplexage par ports

## IV. Protocoles de la couche transport

### TCP (Transmission Control Protocol)

🔒 Transport fiable

TCP garantit la livraison ordonnée et sans erreur des données grâce à des mécanismes de contrôle sophistiqués.

**Caractéristiques :**
- **Orienté connexion** : Établissement de session
- **Fiable** : Détection et correction d'erreurs
- **Contrôle de flux** : Adaptation au récepteur
- **Contrôle de congestion** : Adaptation au réseau

**Établissement de connexion (3-way handshake) :**

Client → Serveur : SYN (seq=x)
Serveur → Client : SYN-ACK (seq=y, ack=x+1)
Client → Serveur : ACK (seq=x+1, ack=y+1)

# Connexion établie

**Fermeture de connexion (4-way handshake) :**

Client → Serveur : FIN
Serveur → Client : ACK
Serveur → Client : FIN
Client → Serveur : ACK

# Connexion fermée

### UDP (User Datagram Protocol)

⚡ Transport rapide

UDP privilégie la rapidité à la fiabilité, idéal pour les applications temps réel.

**Caractéristiques :**
- **Sans connexion** : Pas d'établissement de session
- **Non fiable** : Pas de garantie de livraison
- **Rapide** : Overhead minimal
- **Simple** : En-tête de 8 octets seulement

**Applications typiques :**
- DNS (résolution de noms)
- DHCP (configuration automatique)
- Streaming vidéo/audio
- Jeux en ligne

Comparaison TCP vs UDP :

| Critère | TCP | UDP |
|---------|-----|-----|
| Fiabilité | Élevée | Faible |
| Vitesse | Modérée | Élevée |
| Overhead | Important | Minimal |
| Ordre | Garanti | Non garanti |
| Usage | Web, Email | DNS, Streaming |

## V. Protocoles de la couche application

### HTTP/HTTPS (HyperText Transfer Protocol)

🌐 Web et navigation

HTTP est le protocole fondamental du World Wide Web, permettant le transfert de pages web et de ressources.

**Méthodes HTTP principales :**

# GET : Récupérer une ressource
GET /index.html HTTP/1.1
Host: www.example.com

# POST : Envoyer des données
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded

username=john&password=secret

# PUT : Créer/modifier une ressource
PUT /users/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{"name": "John Doe", "email": "john@example.com"}

# DELETE : Supprimer une ressource
DELETE /users/123 HTTP/1.1
Host: api.example.com

**Codes de statut HTTP :**
- **2xx** : Succès (200 OK, 201 Created)
- **3xx** : Redirection (301 Moved, 304 Not Modified)
- **4xx** : Erreur client (404 Not Found, 403 Forbidden)
- **5xx** : Erreur serveur (500 Internal Error, 503 Unavailable)

**HTTPS = HTTP + TLS/SSL :**
- Chiffrement des données
- Authentification du serveur
- Intégrité des messages

### DNS (Domain Name System)

📞 Annuaire d'Internet

Le DNS traduit les noms de domaine lisibles par l'homme en adresses IP utilisables par les machines.

**Hiérarchie DNS :**

# Structure hiérarchique
.                    # Racine
├── com.             # Domaine de premier niveau (TLD)
│   ├── google.com.  # Domaine de second niveau
│   └── amazon.com.
├── org.
│   └── wikipedia.org.
└── fr.
    └── gouv.fr.

**Types d'enregistrements DNS :**

TypeDescriptionExemple
AAdresse IPv4example.com → 192.168.1.1
AAAAAdresse IPv6example.com → 2001:db8::1
CNAMEAliaswww.example.com → example.com
MXServeur mailexample.com → mail.example.com
NSServeur de nomsexample.com → ns1.example.com
TXTTexte libreVérification SPF, DKIM

# Commandes DNS

# Résolution simple
nslookup google.com
dig google.com

# Requête spécifique
dig google.com MX
dig @8.8.8.8 google.com

# Résolution inverse
dig -x 8.8.8.8

# Trace complète
dig +trace google.com

### DHCP (Dynamic Host Configuration Protocol)

Configuration automatique :

DHCP permet l'attribution automatique d'adresses IP et de paramètres réseau aux clients.

**Processus DHCP (DORA) :**

1. DISCOVER : Client diffuse une demande
2. OFFER    : Serveur propose une configuration
3. REQUEST  : Client demande la configuration
4. ACK      : Serveur confirme l'attribution

**Paramètres fournis :**
- Adresse IP
- Masque de sous-réseau
- Passerelle par défaut
- Serveurs DNS
- Durée de bail (lease time)

### FTP (File Transfer Protocol)

**Modes de fonctionnement :**
- **Mode actif** : Serveur initie la connexion de données
- **Mode passif** : Client initie toutes les connexions

# Commandes FTP de base
ftp ftp.example.com

# Connexion
User: anonymous
Password: email@domain.com

# Navigation
ls          # Lister les fichiers
cd dossier  # Changer de répertoire
pwd         # Répertoire courant

# Transfert
get fichier.txt      # Télécharger
put fichier.txt      # Envoyer
mget *.txt          # Télécharger plusieurs
binary              # Mode binaire
ascii               # Mode texte

# Déconnexion
quit

## VI. Sécurité réseau

🛡️ Protection des communications

La sécurité réseau vise à protéger l'intégrité, la confidentialité et la disponibilité des données en transit.

### Principales menaces

🔴 Menaces critiques :
- **Man-in-the-Middle** : Interception des communications
- **DDoS** : Déni de service distribué
- **Injection SQL** : Exploitation de bases de données
- **Phishing** : Usurpation d'identité

🟡 Menaces modérées :
- **Sniffing** : Écoute du trafic réseau
- **Spoofing** : Usurpation d'adresse
- **Port scanning** : Reconnaissance des services
- **Brute force** : Attaque par force brute

### Mécanismes de protection

#### 1. Pare-feu (Firewall)

# Configuration iptables (Linux)

# Politique par défaut : tout bloquer
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Autoriser le loopback
iptables -A INPUT -i lo -j ACCEPT

# Autoriser les connexions établies
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Autoriser SSH (port 22)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Autoriser HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Bloquer une adresse IP
iptables -A INPUT -s 192.168.1.100 -j DROP

# Sauvegarder les règles
iptables-save > /etc/iptables/rules.v4

#### 2. VPN (Virtual Private Network)

**Types de VPN :**
- **Site-to-Site** : Connexion entre réseaux
- **Remote Access** : Connexion d'utilisateurs distants
- **Client-to-Site** : Accès sécurisé aux ressources

**Protocoles VPN :**
- **IPSec** : Sécurité au niveau IP
- **OpenVPN** : Solution open source
- **WireGuard** : Protocole moderne et rapide
- **PPTP/L2TP** : Protocoles plus anciens

#### 3. Chiffrement

TLS/SSL :

1. **Handshake** : Négociation des paramètres
2. **Échange de clés** : Établissement de la clé de session
3. **Authentification** : Vérification des certificats
4. **Chiffrement** : Communication sécurisée

#### 4. Détection d'intrusion

**IDS (Intrusion Detection System) :**
- **NIDS** : Surveillance du trafic réseau
- **HIDS** : Surveillance des hôtes

**IPS (Intrusion Prevention System) :**
- Détection + blocage automatique
- Analyse en temps réel
- Signatures et comportements

### Bonnes pratiques

Recommandations de sécurité :

1. **Principe du moindre privilège** : Accès minimal nécessaire
2. **Défense en profondeur** : Plusieurs couches de sécurité
3. **Mise à jour régulière** : Correctifs de sécurité
4. **Surveillance continue** : Monitoring et logs
5. **Formation des utilisateurs** : Sensibilisation aux risques
6. **Sauvegarde et récupération** : Plan de continuité

## VII. Réseaux sans fil

### WiFi (IEEE 802.11)

📡 Connectivité sans fil

Le WiFi permet la communication sans fil en utilisant les ondes radio dans les bandes 2,4 GHz et 5 GHz.

**Standards WiFi :**

StandardAnnéeFréquenceDébit maxPortée
802.11a19995 GHz54 Mbps35 m
802.11b19992,4 GHz11 Mbps140 m
802.11g20032,4 GHz54 Mbps140 m
802.11n20092,4/5 GHz600 Mbps250 m
802.11ac20135 GHz6,93 Gbps35 m
802.11ax (WiFi 6)20192,4/5 GHz9,6 Gbps120 m

**Sécurité WiFi :**
- **WEP** : Obsolète, facilement cassable
- **WPA** : Amélioration de WEP
- **WPA2** : Standard actuel (AES)
- **WPA3** : Dernière génération (2018)

### Bluetooth

**Classes de puissance :**
- **Classe 1** : 100 mW, portée ~100 m
- **Classe 2** : 2,5 mW, portée ~10 m
- **Classe 3** : 1 mW, portée ~1 m

**Versions Bluetooth :**
- **Bluetooth 4.0** : Bluetooth Low Energy (BLE)
- **Bluetooth 5.0** : Portée et vitesse améliorées
- **Bluetooth 6.0** : Localisation précise

## VIII. Internet des Objets (IoT)

🌐 Objets connectés

L'IoT connecte des objets du quotidien à Internet, permettant la collecte de données et le contrôle à distance.

### Protocoles IoT

**Protocoles de communication :**
- **MQTT** : Messaging léger pour IoT
- **CoAP** : HTTP pour objets contraints
- **LoRaWAN** : Longue portée, faible consommation
- **Zigbee** : Maillage pour domotique
- **6LoWPAN** : IPv6 sur réseaux contraints

# Exemple MQTT avec Python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connecté avec le code {rc}")
    client.subscribe("capteurs/temperature")

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    print(f"Température reçue: {temperature}°C")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqtt.org", 1883, 60)
client.loop_forever()

### Défis de l'IoT

Problématiques :

- **Sécurité** : Objets souvent peu sécurisés
- **Vie privée** : Collecte massive de données
- **Interopérabilité** : Standards multiples
- **Scalabilité** : Milliards d'objets connectés
- **Énergie** : Autonomie des batteries

## IX. Réseaux de nouvelle génération

### 5G

**Caractéristiques :**
- **Débit** : Jusqu'à 20 Gbps
- **Latence** :
Mécanismes de transition IPv4/IPv6 :

- **Dual Stack** : Support simultané IPv4 et IPv6
- **Tunneling** : Encapsulation IPv6 dans IPv4
- **Translation** : Conversion entre protocoles

### SDN (Software Defined Networking)

**Principe :**
- Séparation plan de contrôle / plan de données
- Contrôleur centralisé
- Programmabilité du réseau
- Virtualisation des fonctions réseau

## Exercices pratiques

TP 1 : Configuration réseau

1. Configurez une interface réseau statique
2. Testez la connectivité avec `ping` et `traceroute`
3. Analysez le trafic avec `tcpdump` ou Wireshark
4. Configurez un serveur DHCP

TP 2 : Sécurité réseau

1. Configurez un pare-feu avec `iptables`
2. Mettez en place un VPN avec OpenVPN
3. Analysez les logs de sécurité
4. Testez la détection d'intrusion

TP 3 : Services réseau

1. Installez et configurez un serveur DNS
2. Mettez en place un serveur web HTTPS
3. Configurez un serveur FTP sécurisé
4. Testez la résolution de noms

---

    📝 Exercices
    🔧 TP Configuration
    🛡️ TP Sécurité