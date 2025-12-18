# Cybersécurité

## Introduction

La **cybersécurité** désigne l'ensemble des techniques et pratiques visant à protéger les systèmes informatiques, les réseaux et les données contre les attaques, les dommages ou les accès non autorisés. À l'ère du numérique, où nous partageons constamment des informations en ligne, comprendre les enjeux de la cybersécurité est devenu essentiel.

## Les enjeux de la sécurisation des échanges sur Internet

### Pourquoi sécuriser les échanges ?

Chaque jour, des milliards de données circulent sur Internet :
- Messages personnels
- Informations bancaires
- Données médicales
- Photos et vidéos privées
- Identifiants et mots de passe

**Sans sécurisation, ces données peuvent être :**
- **Interceptées** (lues par des personnes non autorisées)
- **Modifiées** (changées en cours de route)
- **Volées** (copiées sans autorisation)
- **Détruites** (supprimées ou rendues inaccessibles)

### Les risques quotidiens

**Pour les individus :**
- Vol d'identité
- Usurpation de compte
- Harcèlement en ligne
- Perte de données personnelles
- Fraude bancaire

**Pour les organisations :**
- Espionnage industriel
- Sabotage de systèmes
- Rançongiciels (ransomware)
- Perte de confiance des clients
- Amendes légales (RGPD)

### Exemple concret

**Situation sans sécurisation :**
```
Vous → [Mot de passe : 1234] → Site web
         ↑
    Pirate qui intercepte : "J'ai ton mot de passe !"
```

**Situation avec sécurisation (HTTPS) :**
```
Vous → [Mot de passe chiffré : %Kj#9@mL] → Site web
         ↑
    Pirate qui intercepte : "Je ne comprends rien !"
```

## Le chiffrement : principe de base

### Qu'est-ce que le chiffrement ?

Le **chiffrement** est une technique qui transforme un message clair en message codé illisible, sauf pour la personne qui possède la **clé** de déchiffrement.

**Vocabulaire :**
- **Message clair** : le message original, lisible
- **Chiffrement** : transformation du message clair en message codé
- **Message chiffré** : le message codé, illisible
- **Clé** : information secrète permettant de chiffrer/déchiffrer
- **Déchiffrement** : transformation du message chiffré en message clair

**Schéma :**
```
Message clair → [CHIFFREMENT avec CLÉ] → Message chiffré
Message chiffré → [DÉCHIFFREMENT avec CLÉ] → Message clair
```

## Méthodes de chiffrement simples

### 1. Le code de César

Le **code de César** est l'une des plus anciennes méthodes de chiffrement. Elle consiste à décaler chaque lettre de l'alphabet d'un nombre fixe de positions.

**Principe avec un décalage de 3 :**
```
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

**Exemple :**
```
Message clair :  BONJOUR
Clé (décalage) : 3
Message chiffré : ERQMRXU
```

**Activité pratique :**

Chiffrez les messages suivants avec un décalage de 3 :
1. PYTHON → ___________
2. COLLEGE → ___________

Déchiffrez les messages suivants (décalage de 3) :
1. LQIRUPDWLTXH → ___________
2. VHFXULWH → ___________


**Limites du code de César :**
- Seulement 26 clés possibles (26 lettres dans l'alphabet)
- Facile à casser par force brute (essayer toutes les possibilités)
- Ne résiste pas à l'analyse de fréquence

### 2. Le chiffrement XOR (OU EXCLUSIF)

Le **chiffrement XOR** utilise l'opérateur logique XOR (OU EXCLUSIF) pour combiner le message avec une clé.

**Rappel du XOR :**
| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

**Propriété intéressante :** A XOR B XOR B = A
→ On peut chiffrer ET déchiffrer avec la même opération !

**Exemple simplifié avec des caractères :**
```
Message : "HI"
Clé :     "AB"

Chiffrement :
H (72 en ASCII) XOR A (65 en ASCII) = 13
I (73 en ASCII) XOR B (66 en ASCII) = 11

Message chiffré : [13, 11]

Déchiffrement :
13 XOR A (65) = 72 → H
11 XOR B (66) = 73 → I
```


**Avantages du XOR :**
- Simple et rapide
- Chiffrement = déchiffrement (même algorithme)
- Impossible à casser si la clé est vraiment aléatoire et de même longueur que le message

**Limites :**
- La clé doit rester secrète
- Si la clé est courte et répétée, elle peut être devinée

## Le chiffrement moderne : HTTPS

### Qu'est-ce que HTTPS ?

**HTTPS** (HyperText Transfer Protocol Secure) est la version sécurisée du protocole HTTP. Il utilise le chiffrement pour protéger les échanges entre votre navigateur et un site web.

**Comment reconnaître un site HTTPS ?**
- Un cadenas 🔒 dans la barre d'adresse
- L'URL commence par `https://` (et non `http://`)

**Exemple :**
- ❌ `http://monsite.com` → Non sécurisé
- ✅ `https://monsite.com` → Sécurisé

### Que protège HTTPS ?

1. **Confidentialité** : Les données échangées sont chiffrées
2. **Intégrité** : Les données ne peuvent pas être modifiées en cours de route
3. **Authentification** : Vous êtes sûr de communiquer avec le bon site

**Activité :** Vérifier quelques sites et noter s'ils utilisent HTTPS
- Site de votre collège : ___________
- Google : ___________
- YouTube : ___________

## Les cyberattaques : comprendre pour se protéger

### 1. L'attaque de l'humain du milieu (Human-in-the-Middle)

**Principe :** Le pirate s'interpose entre deux parties qui communiquent et peut intercepter ou modifier les messages.

**Schéma de l'attaque :**
```
Sans attaque :
Alice → [Message] → Bob

Avec attaque (humain du milieu) :
Alice → [Message] → PIRATE → [Message modifié] → Bob
```

**Exemple concret :**

**Situation :** Vous vous connectez au WiFi public d'un café

```
Votre ordinateur → WiFi du café → Serveur de votre banque
                        ↑
                    PIRATE qui contrôle
                    le WiFi et lit tout !
```

**Ce que le pirate peut faire :**
- Lire vos mots de passe
- Voler vos numéros de carte bancaire
- Modifier les pages web que vous voyez
- Vous rediriger vers de faux sites

**Démonstration simplifiée en classe :**

Activité avec 3 élèves :
- **Alice** : Veut envoyer un message à Bob
- **Bob** : Attend le message d'Alice
- **Pirate** : Se place entre les deux

1. Alice écrit "Rendez-vous à 15h" et donne à Pirate (croyant le donner à Bob)
2. Pirate lit le message et le modifie : "Rendez-vous à 16h"
3. Pirate donne le message modifié à Bob
4. Bob arrive à 16h, Alice à 15h → confusion !

**Comment se protéger ?**
- ✅ Utiliser HTTPS (le chiffrement empêche le pirate de lire)
- ✅ Éviter les WiFi publics pour des opérations sensibles (banque, achats)
- ✅ Utiliser un VPN sur les réseaux non sûrs
- ✅ Vérifier le certificat de sécurité des sites (cadenas)

### 2. L'attaque par déni de service distribué (DDoS)

**Principe :** Submerger un serveur de requêtes pour le rendre inaccessible.

**DDoS = Distributed Denial of Service**

**Schéma de l'attaque :**
```
Normal :
Client 1 → Serveur (répond normalement)
Client 2 → Serveur (répond normalement)

Attaque DDoS :
10 000 ordinateurs infectés → SERVEUR (surchargé, ne répond plus)
```

**Analogie :** Un restaurant peut servir 50 clients en même temps. Si 5000 personnes arrivent d'un coup, le service s'arrête et plus personne n'est servi (même les clients légitimes).

**Comment ça marche ?**

1. Le pirate infecte des milliers d'ordinateurs avec un virus (créant un "botnet")
2. Au signal, tous ces ordinateurs envoient des demandes au serveur cible
3. Le serveur reçoit trop de demandes et plante
4. Les utilisateurs légitimes ne peuvent plus accéder au service

**Exemples réels d'attaques DDoS :**
- Octobre 2016 : Attaque massive contre Dyn (DNS), rendant inaccessibles Twitter, Netflix, Reddit
- Services de jeux en ligne régulièrement visés
- Sites gouvernementaux

**Comment se protéger (pour les sites) ?**
- Systèmes de détection d'attaques
- Distribution de charge sur plusieurs serveurs
- Services de protection DDoS (comme Cloudflare)
- Filtrage des requêtes suspectes

**Conséquences :**
- Perte financière pour les entreprises
- Impossibilité d'accéder aux services
- Atteinte à la réputation
- Peut masquer d'autres attaques

### Activité : Simuler une attaque DDoS (version éducative)

**Matériel :** Un élève = "serveur", les autres = "clients"

**Scénario 1 (normal) :**
- 3 élèves lèvent la main
- Le "serveur" répond à chacun tranquillement

**Scénario 2 (attaque DDoS) :**
- Toute la classe lève la main en même temps
- Le "serveur" est débordé et ne peut répondre à personne

**Réflexion :** Comment le serveur pourrait-il se défendre ?

## Les bonnes pratiques de cybersécurité

### 1. Protéger ses mots de passe

**Créer un mot de passe fort :**
- ✅ Au moins 12 caractères
- ✅ Mélanger majuscules, minuscules, chiffres, symboles
- ✅ Ne pas utiliser de mots du dictionnaire
- ✅ Différent pour chaque compte

**Exemples :**
- ❌ Faible : `password`, `123456`, `azerty`
- ❌ Faible : `Marie2010`, `Jesuisforte`
- ✅ Fort : `Tr0piCal!$oLeiL#89`, `MyP@ssw0rd!2024`

**Astuce pour créer un mot de passe mémorable :**
Prendre une phrase : "J'adore manger 3 pizzas le vendredi soir !"
→ Mot de passe : `Jam3pLvs!`

**Utiliser un gestionnaire de mots de passe :**
- Keepass, Bitwarden, 1Password
- Génère des mots de passe forts
- Les stocke de façon sécurisée
- Vous n'avez à retenir qu'un seul mot de passe maître

### 2. Activer l'authentification à deux facteurs (2FA)

**Principe :** Même si quelqu'un a votre mot de passe, il faut une deuxième preuve d'identité.

**Méthodes :**
- Code SMS envoyé sur votre téléphone
- Code généré par une application (Google Authenticator)
- Clé de sécurité physique (YubiKey)
- Empreinte digitale ou reconnaissance faciale

**Exemple :**
```
1. Vous entrez votre mot de passe → ✓
2. Vous recevez un code par SMS : 847293
3. Vous entrez ce code → ✓
4. Vous êtes connecté !
```

### 3. Reconnaître le phishing (hameçonnage)

**Phishing :** Technique pour voler vos informations en se faisant passer pour un organisme de confiance.

**Exemples de messages de phishing :**
```
❌ "Votre compte Netflix est suspendu. 
   Cliquez ici pour réactiver : http://netfliix.com"
   
❌ "Vous avez gagné un iPhone ! 
   Entrez vos coordonnées bancaires pour le recevoir."
   
❌ "Problème avec votre compte. 
   Envoyez-nous votre mot de passe pour vérification."
```

**Comment reconnaître le phishing ?**
- Email inattendu demandant des informations personnelles
- Fautes d'orthographe ou de grammaire
- Adresse de l'expéditeur suspecte (netflix.support-34@gmail.com)
- URL bizarre (netfliix.com au lieu de netflix.com)
- Sentiment d'urgence ("Agissez maintenant !")
- Promesses trop belles pour être vraies

**Que faire ?**
- ✅ Ne jamais cliquer sur les liens suspects
- ✅ Vérifier l'adresse email de l'expéditeur
- ✅ Aller directement sur le site officiel (ne pas utiliser le lien)
- ✅ Contacter l'organisme par un canal officiel
- ✅ Signaler le message comme phishing

### 4. Mettre à jour ses logiciels

Les mises à jour corrigent des failles de sécurité.

**À mettre à jour régulièrement :**
- Système d'exploitation (Windows, macOS, Linux)
- Navigateur web
- Applications
- Antivirus

### 5. Sécuriser sa navigation

- Utiliser HTTPS
- Ne pas accepter tous les cookies
- Utiliser un bloqueur de publicités (attention aux malwares)
- Navigation privée pour les recherches sensibles
- VPN sur les WiFi publics

### 6. Protéger ses données personnelles

**Réfléchir avant de partager :**
- Photos personnelles
- Adresse, numéro de téléphone
- Informations sur votre famille
- Votre emploi du temps

**Sur les réseaux sociaux :**
- Paramètres de confidentialité
- Limiter l'audience de vos publications
- Ne pas accepter d'inconnus
- Attention aux informations dans les photos (lieu, plaque d'immatriculation...)
