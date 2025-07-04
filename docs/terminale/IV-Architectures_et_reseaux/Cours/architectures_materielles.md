# Architectures matérielles et systèmes d'exploitation

    🏗️ Architectures matérielles et systèmes d'exploitation
    Comprendre le fonctionnement interne des ordinateurs

## I. Architecture de von Neumann

🏛️ Le modèle fondamental

L'architecture de von Neumann, proposée en 1945, reste la base de la plupart des ordinateurs modernes. Elle repose sur le principe de **programme enregistré** : les instructions et les données sont stockées dans la même mémoire.

### Composants principaux

Architecture de von Neumann

Unité de Contrôle (UC)
Unité Arithmétique et Logique (UAL)
Mémoire
Entrées/Sorties

Bus de données ↔ Bus d'adresses ↔ Bus de contrôle

#### 1. Le processeur (CPU)

**Unité de Contrôle (UC) :**
- Décode les instructions
- Coordonne l'exécution
- Gère les signaux de contrôle

**Unité Arithmétique et Logique (UAL) :**
- Effectue les calculs arithmétiques
- Réalise les opérations logiques
- Compare les valeurs

**Registres :**
- Mémoire ultra-rapide du processeur
- Stockent temporairement les données
- Types : registres généraux, compteur ordinal, registre d'instruction

Exemple de cycle d'instruction :

1. **Fetch** : Charger l'instruction depuis la mémoire
2. **Decode** : Décoder l'instruction
3. **Execute** : Exécuter l'opération
4. **Store** : Stocker le résultat

#### 2. La mémoire

Registres CPU~1 ns - Quelques Ko
Cache L1/L2/L3~10 ns - Quelques Mo
Mémoire RAM~100 ns - Quelques Go
Stockage SSD~0.1 ms - Centaines de Go
Stockage HDD~10 ms - Téraoctets

Principe de localité :
- **Temporelle** : Une donnée récemment utilisée sera probablement réutilisée
- **Spatiale** : Les données proches d'une donnée utilisée seront probablement utilisées

#### 3. Les bus

- **Bus de données** : Transport des informations
- **Bus d'adresses** : Spécification de l'emplacement mémoire
- **Bus de contrôle** : Signaux de coordination

### Limites de l'architecture de von Neumann

Goulot d'étranglement de von Neumann :

Le bus unique entre CPU et mémoire limite les performances car :
- Une seule opération à la fois (lecture OU écriture)
- La vitesse du bus limite la vitesse globale
- Conflit entre accès aux instructions et aux données

## II. Architectures modernes

### Architecture Harvard

🔄 Séparation instructions/données

L'architecture Harvard sépare physiquement la mémoire des instructions de celle des données, permettant un accès simultané.

**Avantages :**
- Accès simultané aux instructions et données
- Optimisation possible pour chaque type de mémoire
- Meilleure sécurité (séparation)

**Inconvénients :**
- Complexité accrue
- Coût plus élevé
- Utilisation moins flexible de la mémoire

### Architectures parallèles

#### 1. Processeurs multi-cœurs

Processeur Quad-Core

Cœur 1L1 Cache
Cœur 2L1 Cache
Cœur 3L1 Cache
Cœur 4L1 Cache

Cache L2 partagé
Cache L3 partagé

#### 2. Architectures SIMD/MIMD

- **SIMD** (Single Instruction, Multiple Data) : Une instruction sur plusieurs données
- **MIMD** (Multiple Instructions, Multiple Data) : Instructions différentes sur données différentes

### GPU et calcul parallèle

GPU vs CPU :

- **CPU** : Peu de cœurs très puissants, optimisé pour les tâches séquentielles
- **GPU** : Milliers de cœurs simples, optimisé pour le parallélisme massif

## III. Systèmes d'exploitation

🖥️ Interface entre matériel et logiciel

Le système d'exploitation (OS) gère les ressources matérielles et fournit une interface aux applications.

### Fonctions principales

#### 1. Gestion des processus

Nouveau
Prêt
En cours
En attente
Terminé

**Ordonnancement des processus :**
- **FIFO** (First In, First Out)
- **SJF** (Shortest Job First)
- **Round Robin** : Attribution cyclique du temps CPU
- **Priorités** : Processus prioritaires en premier

# Exemple de commandes Unix pour la gestion des processus

# Lister les processus en cours
ps aux

# Afficher les processus en temps réel
top

# Tuer un processus
kill -9 PID

# Lancer un processus en arrière-plan
nohup python script.py &

#### 2. Gestion de la mémoire

**Techniques de gestion :**

1. **Allocation contiguë** : Processus en blocs contigus
2. **Pagination** : Division en pages de taille fixe
3. **Segmentation** : Division en segments de taille variable
4. **Mémoire virtuelle** : Illusion d'une mémoire plus grande

Mémoire virtuelle :

- Chaque processus a son espace d'adressage virtuel
- Translation automatique adresse virtuelle → physique
- Permet le swap (échange avec le disque)
- Protection entre processus

#### 3. Gestion des fichiers

**Systèmes de fichiers courants :**
- **FAT32** : Compatible, limité à 4 Go par fichier
- **NTFS** : Windows, journalisé, permissions avancées
- **ext4** : Linux, performant, journalisé
- **APFS** : macOS, optimisé pour SSD

# Commandes de gestion de fichiers Unix

# Permissions (lecture, écriture, exécution)
chmod 755 fichier.txt

# Propriétaire et groupe
chown user:group fichier.txt

# Espace disque
df -h
du -sh dossier/

# Liens symboliques
ln -s /chemin/source /chemin/lien

#### 4. Gestion des entrées/sorties

**Méthodes d'E/S :**

1. **E/S programmées** : CPU attend la fin de l'opération
2. **E/S par interruption** : CPU libéré pendant l'opération
3. **DMA** (Direct Memory Access) : Transfert direct mémoire-périphérique

### Types de systèmes d'exploitation

#### 1. Systèmes temps réel

Contraintes temporelles strictes :

- **Temps réel dur** : Échéance absolue (systèmes critiques)
- **Temps réel mou** : Échéance préférable (multimédia)

#### 2. Systèmes distribués

- Coordination de machines multiples
- Transparence pour l'utilisateur
- Tolérance aux pannes
- Passage à l'échelle

#### 3. Systèmes embarqués

- Ressources limitées
- Consommation optimisée
- Fiabilité critique
- Temps de démarrage rapide

## IV. Virtualisation

☁️ Abstraction des ressources

La virtualisation permet de faire fonctionner plusieurs systèmes d'exploitation sur une même machine physique.

### Types de virtualisation

#### 1. Virtualisation complète

- Hyperviseur de type 1 (bare-metal) : VMware ESXi, Hyper-V
- Hyperviseur de type 2 (hosted) : VirtualBox, VMware Workstation

#### 2. Paravirtualisation

- OS invité modifié pour coopérer
- Meilleures performances
- Exemple : Xen

#### 3. Conteneurisation

Docker - Exemple de conteneurisation :

```dockerfile
# Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

```bash
# Commandes Docker
docker build -t mon-app .
docker run -p 8080:80 mon-app
docker ps
```

### Avantages de la virtualisation

- **Consolidation** : Meilleure utilisation des ressources
- **Isolation** : Sécurité entre environnements
- **Flexibilité** : Déploiement et migration faciles
- **Économies** : Réduction des coûts matériels

## V. Sécurité des systèmes

### Mécanismes de protection

#### 1. Contrôle d'accès

# Modèle de permissions Unix
# rwx rwx rwx
# ||| ||| |||
# ||| ||| ||+-- Autres : exécution
# ||| ||| |+--- Autres : écriture
# ||| ||| +---- Autres : lecture
# ||| ||+------ Groupe : exécution
# ||| |+------- Groupe : écriture
# ||| +-------- Groupe : lecture
# ||+---------- Propriétaire : exécution
# |+----------- Propriétaire : écriture
# +------------ Propriétaire : lecture

# Exemple : rwxr-xr-- = 754
chmod 754 fichier.txt

#### 2. Authentification

- **Facteur de connaissance** : Mot de passe
- **Facteur de possession** : Token, carte
- **Facteur d'inhérence** : Biométrie
- **Authentification multi-facteurs** (MFA)

#### 3. Chiffrement

- **Chiffrement symétrique** : AES, ChaCha20
- **Chiffrement asymétrique** : RSA, ECC
- **Fonctions de hachage** : SHA-256, bcrypt

### Vulnérabilités courantes

Principales menaces :

- **Buffer overflow** : Débordement de tampon
- **Injection de code** : SQL injection, XSS
- **Escalade de privilèges** : Exploitation de failles
- **Attaques par canal auxiliaire** : Timing, consommation

## VI. Performance et optimisation

### Métriques de performance

- **Débit** (Throughput) : Opérations par seconde
- **Latence** : Temps de réponse
- **Utilisation** : Pourcentage d'usage des ressources
- **Passage à l'échelle** (Scalability)

### Techniques d'optimisation

#### 1. Optimisations matérielles

- **Pipeline** : Exécution en parallèle des étapes
- **Prédiction de branchement** : Anticipation des sauts
- **Exécution dans le désordre** : Réorganisation des instructions
- **Exécution spéculative** : Exécution anticipée

#### 2. Optimisations logicielles

# Exemple d'optimisation en Python

# Non optimisé
def somme_carres_lente(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# Optimisé avec compréhension de liste
def somme_carres_rapide(n):
    return sum(i*i for i in range(n))

# Optimisé mathématiquement
def somme_carres_math(n):
    return n * (n-1) * (2*n-1) // 6

## VII. Tendances actuelles

### 1. Informatique quantique

Principes quantiques :

- **Superposition** : Qubit dans plusieurs états simultanément
- **Intrication** : Corrélation entre qubits distants
- **Interférence** : Amplification/annulation de probabilités

### 2. Edge Computing

- Traitement près des sources de données
- Réduction de la latence
- Économie de bande passante
- Applications IoT

### 3. Intelligence artificielle matérielle

- **TPU** (Tensor Processing Unit) : Google
- **NPU** (Neural Processing Unit) : Huawei
- **Puces neuromorphiques** : Intel Loihi

## Exercices pratiques

TP 1 : Analyse de performance

1. Utilisez `htop` pour analyser l'utilisation CPU et mémoire
2. Mesurez les performances d'E/S avec `iostat`
3. Analysez la hiérarchie mémoire avec `lscpu`
4. Comparez les performances SSD vs HDD

TP 2 : Virtualisation

1. Installez VirtualBox et créez une VM Linux
2. Configurez Docker et créez un conteneur
3. Comparez les performances native vs virtualisée
4. Testez la migration de conteneurs

TP 3 : Sécurité système

1. Configurez un pare-feu avec `iptables`
2. Analysez les logs système avec `journalctl`
3. Testez l'authentification par clé SSH
4. Chiffrez un disque avec LUKS

---

    📝 Exercices
    🔬 TP Performance
    ☁️ TP Virtualisation