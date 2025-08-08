# 📱 Objets Connectés

L'idée de connecter des objets du quotidien à Internet remonte aux années 1980. Le premier objet connecté de l'histoire était un distributeur de Coca-Cola à l'université Carnegie Mellon en 1982. Les étudiants pouvaient vérifier à distance si des boissons étaient disponibles et si elles étaient froides !

**L'objectif était simple : éviter de se déplacer pour rien jusqu'au distributeur.**

Ce n'est qu'en 1999 que Kevin Ashton, chercheur au MIT, invente le terme "Internet of Things" (Internet des Objets) pour décrire un monde où tous les objets seraient connectés.

**La première définition était : "un réseau d'objets physiques connectés à Internet".**

![iot_history](img/iot_history.svg)

À la suite de cela, dans les années 2000-2010, les technologies sans fil se sont démocratisées.
On appelle ces technologies de communication des **protocoles de communication**.

La manière de faire communiquer les objets connectés est découpée en diverses étapes.
Ces diverses étapes permettent de collecter des données, les transmettre, les traiter et agir en conséquence.
Chaque étape correspond à différents composants et technologies.
Dans les années 2010, les **capteurs miniaturisés** et les **réseaux basse consommation** ont vu le jour.
Ils sont installés massivement depuis 2015, la même année où ont vu le jour les premières plateformes IoT grand public.
Les années 2020 ont permis de faire voir le jour à une des plus grandes révolutions technologiques : la **5G** et l'**intelligence artificielle embarquée**.

![iot_evolution](img/iot_evolution.svg)

Depuis, les objets connectés permettent de relier plus de 50 milliards d'appareils pour collecter des données, automatiser des tâches ou améliorer notre quotidien à l'aide de plusieurs technologies dépendant de protocoles.
Par exemple, il existe des capteurs de température (protocole LoRaWAN), des montres connectées (Bluetooth) ou des assistants vocaux (WiFi).

![iot_map](img/iot_world_map.svg)

En clair, **un objet connecté est un dispositif physique équipé de capteurs, d'actionneurs et d'une connexion réseau qui lui permet de collecter, échanger et traiter des données via Internet.**

## Définitions

Un **objet connecté** est un dispositif physique doté de capacités de communication qui peut se connecter à Internet ou à d'autres objets pour échanger des données.
**On retrouve un certain nombre de composants dans un objet connecté qui ont chacun leur propre rôle.**

### Les composants d'un objet connecté

Pour qu'un objet connecté fonctionne, il faut des composants le constituant.

**On retrouve :**

| Composant | Rôle | Exemple |
|-----------|------|----------|
| Capteurs | Éléments qui mesurent des grandeurs physiques de l'environnement | capteur de température, accéléromètre, caméra |
| Actionneurs | Éléments qui agissent sur l'environnement physique | moteur, LED, haut-parleur |
| Microprocesseur | Élément qui traite les données et contrôle l'objet | Arduino, Raspberry Pi, ESP32 |
| Interface de communication | Élément qui permet de communiquer avec d'autres objets ou Internet | module WiFi, Bluetooth, LoRa |
| Alimentation | Élément qui fournit l'énergie nécessaire au fonctionnement | batterie, panneau solaire, secteur |

On a défini dans les rôles divers types de capteurs et d'actionneurs.
On peut les regrouper en 2 catégories :

- **Capteurs** : dispositifs qui mesurent et collectent des données de l'environnement.
- **Actionneurs** : dispositifs qui agissent sur l'environnement en réponse aux données.

![composants_iot](img/composants_iot.svg)

!!!danger
    On dispose de composants, d'un objet mais, comment communiquent-ils entre eux ? Quelles technologies sont utilisées ?

### Types de capteurs et actionneurs

Un objet connecté dispose de **capteurs** pour mesurer son environnement et d'**actionneurs** pour agir sur celui-ci.

Ces composants permettent de transformer des grandeurs physiques en données numériques ou inversement.
De manière générale, un capteur dispose d'une **grandeur mesurée** et d'une **unité de mesure**.

**Exemples de capteurs courants :**

| Type de capteur | Grandeur mesurée | Unité | Exemple d'usage |
|-----------------|------------------|-------|------------------|
| Température | Température ambiante | °C | Thermostat connecté |
| Humidité | Taux d'humidité | % | Station météo |
| Mouvement | Accélération, rotation | m/s², °/s | Montre connectée |
| Lumière | Intensité lumineuse | lux | Éclairage automatique |
| Son | Niveau sonore | dB | Assistant vocal |
| Pression | Pression atmosphérique | hPa | Altimètre |

**Exemples d'actionneurs courants :**

| Type d'actionneur | Action réalisée | Exemple d'usage |
|-------------------|-----------------|------------------|
| LED | Émission de lumière | Ampoule connectée |
| Moteur | Mouvement mécanique | Volet roulant |
| Haut-parleur | Émission sonore | Enceinte connectée |
| Écran | Affichage d'informations | Tablette |
| Électrovanne | Contrôle de fluide | Arrosage automatique |

### Protocoles de communication

Chaque objet connecté doit pouvoir communiquer avec d'autres objets ou avec Internet.
Sur les réseaux IoT, on utilise différents **protocoles de communication** selon les besoins.
**Un protocole de communication définit les règles d'échange de données entre objets.**

Les protocoles se différencient par leur **portée**, leur **consommation énergétique** et leur **débit**.

**Comparaison des principaux protocoles :**

| Protocole | Portée | Consommation | Débit | Usage typique |
|-----------|--------|--------------|-------|---------------|
| WiFi | 50-100m | Élevée | Très haut | Objets domestiques |
| Bluetooth | 10-100m | Moyenne | Moyen | Objets personnels |
| LoRaWAN | 2-15km | Très faible | Très faible | Capteurs ruraux |
| Sigfox | 3-50km | Très faible | Très faible | Objets autonomes |
| 4G/5G | National | Élevée | Très haut | Objets mobiles |
| Zigbee | 10-100m | Faible | Faible | Domotique |

!!!info "Focus sur LoRaWAN"
    **LoRaWAN** (Long Range Wide Area Network) est un protocole spécialement conçu pour les objets connectés.
    
    **Ses avantages :**
    - Très longue portée (jusqu'à 15km en zone rurale)
    - Très faible consommation (batterie de 10 ans)
    - Pénétration dans les bâtiments
    - Réseau public gratuit en France
    
    **Ses inconvénients :**
    - Très faible débit (quelques octets par message)
    - Limitation du nombre de messages par jour
    
    **Exemple d'usage :** capteur de niveau d'eau dans un puits agricole qui envoie une mesure par heure.

## Fonctionnement d'un système IoT

Un système d'objets connectés fonctionne selon un cycle en plusieurs étapes :

1. **Collecte** : Les capteurs mesurent des grandeurs physiques de l'environnement
2. **Transmission** : Les données sont envoyées via un protocole de communication
3. **Traitement** : Les données sont analysées par un serveur ou une plateforme cloud
4. **Analyse** : Des algorithmes déterminent les actions à entreprendre
5. **Action** : Des commandes sont envoyées aux actionneurs pour agir sur l'environnement

![cycle_iot](img/cycle_iot.svg)

### Exemple concret : Thermostat connecté

Prenons l'exemple d'un **thermostat connecté** pour comprendre le fonctionnement :

**Étape 1 - Collecte :**
- Le capteur de température mesure 18°C dans la pièce
- Le capteur de présence détecte une personne

**Étape 2 - Transmission :**
- Les données sont envoyées via WiFi vers une plateforme cloud
- Format des données : `{"temperature": 18, "presence": true, "timestamp": "2024-01-15T14:30:00"}`

**Étape 3 - Traitement :**
- La plateforme compare avec la consigne (20°C)
- Elle vérifie les horaires de programmation
- Elle consulte l'historique de consommation

**Étape 4 - Analyse :**
- Décision : "Il faut chauffer car température < consigne ET présence détectée"
- Calcul de la puissance optimale selon l'isolation

**Étape 5 - Action :**
- Commande envoyée à l'actionneur (électrovanne)
- Démarrage du chauffage
- Notification envoyée sur l'application mobile

!!!warning
    Ce cycle se répète en permanence, généralement toutes les quelques minutes, pour maintenir un contrôle précis.

## Applications des objets connectés

Les objets connectés transforment de nombreux secteurs de notre société :

### Domotique
- **Éclairage intelligent** : ampoules qui s'adaptent à la luminosité extérieure
- **Sécurité** : caméras, détecteurs de mouvement, serrures connectées
- **Confort** : thermostats, volets automatiques, enceintes connectées

### Santé
- **Montres connectées** : surveillance du rythme cardiaque, compteur de pas
- **Dispositifs médicaux** : tensiomètres, glucomètres connectés
- **Télémédecine** : consultation à distance, suivi de patients

### Agriculture
- **Capteurs de sol** : mesure de l'humidité, de la température, du pH
- **Irrigation automatique** : arrosage optimisé selon les besoins
- **Surveillance du bétail** : colliers connectés pour localiser les animaux

### Industrie
- **Maintenance prédictive** : capteurs sur les machines pour anticiper les pannes
- **Optimisation énergétique** : suivi de la consommation en temps réel
- **Traçabilité** : suivi des produits tout au long de la chaîne de production

### Villes intelligentes
- **Éclairage public** : adaptation automatique selon la fréquentation
- **Gestion des déchets** : capteurs de remplissage des poubelles
- **Transport** : optimisation du trafic, véhicules autonomes

![applications_iot](img/applications_iot.svg)

**L'avenir des objets connectés s'oriente vers une intégration toujours plus poussée dans notre quotidien, avec des objets plus intelligents, plus autonomes et plus respectueux de l'environnement.**