# Introduction aux réseaux

## Qu'est ce qu'un réseau internet

Un **réseau internet** est un ensemble de machines reliées entre elles qui échangent des informations sur Internet.

Dans un réseau, on retrouve un certain nombre de machines ...

- Des ordinateurs, smartphones, tablettes, consoles ...
- IOT : ensemble des objets connectés (par exemple : domotique)
- un (ou plusieurs) switchs est un élément d'un réseau qui permet de relier les machines entre elles pour s'échanger des données dans un réseau local. Un réseau local : ___________________________
- un routeur (ou plusieurs) routeur est un élément qui permet de relier plusieurs réseaux entre eux.

... qui sont reliées entre elles par :

- des câbles (RJ45)
- WiFi (Wireless Fidelity)
- par fibre optique

La communication est définie et régie par des protocoles. Un protocole <...>

#### Distinction Web et Internet

Internet correspond à **l'ensemble des réseaux organisés** de manière réticulaire.

Le Web correspond à une application d'Internet qui rend accessible des ressources grâce aux **liens hypertextes** (que l'on nomme usellement hyperliens).

#### Topologies de réseaux

Une topologie dans les réseaux correspond à la disposition des machines dans un réseau. 

On en distingue plusieurs : 

- Anneau
- Étoile (en général celui utilisé de manière domestique)
- Bus
- Hierarchique
- P2P

## Adresse MAC et IP

### Adresse MAC

Une adresse MAC (Media Access Control) correspond à l'adresse physique d'une interface d'une carte Réseau qui est **unique** et propre à la carte.
Elle est constituée d'un ensemble de 6 groupes de 16 bits représentés en hexadécimal.
Exemple : a8:9f:d9:4c:5c:d9
**Remarque : Un ordinateur possède une carte réseau qui a plusieurs interfaces.**

Le switch dans un réseau utilise l'adresse MAC de la carte réseau pour retransmettre les données à la bonne machine.

### Adresse IP

L'adresse IP est l'adresse d'une machine sur un réseau. Elle est attribuée à la première connexion de la machine sur le réseau.

Elle est constituée d'un ensemble de 4 octects représentés en décimal.
Exemple : 123.32.41.74

Grâce à ce modèle on peut définir $2^24$ adresse différentes, soient $4 294 967 296$ adresses différentes.

Combien de machines dans le monde en 2024 ? 200 milliards de machines connectées à Internet.
Comment les identifier ? Plusieurs méthodes : 

**Utilisation de sous-réseaux et de réseaux locaux**

 #TODO : Classes ip


**IPv6**

L'adresse IPv6 est composée d'un ensemble de 8 groupes de 4 symboles en hexadécimal.
Cela revient à $2^{128} \approx 3.40 \times 10^{38}$ adresses différentes.

#### Adresse d'un réseau

 #TODO : IP d'un réseau

### Modèle TCP/IP

<img src="Modele_IP.png" align='center' width = 50% />

Le modèle IP est un modèle en couche qui permet d'illustrer l'encapsulation des données pour permettre leur envoi ou leur reception et traitement.

Chaque couche a sa tâche prédéfinie, notamment grâce aux protocoles qui sont en jeux.

#### Accès Réseau

La couche accès réseau explicite la liaison entre les machines de manière physique (câbles, WiFi ...) et  la reception des données brutes (bits, ondes lumineuses, signal analogique) aux machines via les switchs ou les routeurs grâce aux adresses physiques (MAC).

Protocoles de la couche **Accès réseau** :
