# Internet

## Point historique

La création d'Internet date du début des années 1960. L'idée était de relier divers machines pour envoyer des données, à l'origine des travaux issus de laboratoires ou des universités.

A l'époque, le projet initial s'appelait ARPANET et était un projet détenu par la Défense des États-Unis chapeauté Robert Kahn à la Defense Advanced Research Projects Agency.
Le premier objectif était de relier les universités de Stanford, de Los Angeles et celle de l'Utah.

Ce n'est que le 20 septembre 1969 que la première communication voit le jour entre l'université de Californie et celle de Stanford.
Le premier message transmis de l'Histoire était *login*.

![arpa](img/arpanet.jpeg)

À la suite de cela, dans les années 70-80, des normalismes de communication ont vu le jour. On appelle cet ensemble de règles à respecter des **protocoles**.
La manière de communiquer pour les machines est découpées en diverses étapes.
Ces diverses étapes sont catégorisées dans un modèle : le modèle TCP-IP qui explique chaque étape de la communication.
Chaque étape (ou couche) du modèle TCP-IP correspond à divers protocoles.

Dans les années 1980, le fameux **protocole TCP/IPv4** a vu le jour. Il est installé en 1983 sur ARPANET, la même année où ont vu le jour les règles des systèmes de nom de domaine (DNS).

Les années 1990 ont permis de faire voir le jour à une des plus grandes technologies jamais créée par l'être humain : le WEB, créé au CERN (en Suisse) par Tim Berners-Lee et Robert Cailliau.

![tblrc](img/tblrc.jpeg)

Depuis, Internet permet de relier plus de 3 à 4 milliards d'internautes pour s'envoyer des mails, des fichiers ou accéder à une quantité de données incommensurable à l'aide de plusieurs applications dépendant de protocoles.
Par exemple, il existe des applications de mail (protocole POP), d'échange de fichier (FTP) ou de navigation sur des pages (WEB).

![map](img/geo-mercator.svg)

En clair, **Internet est un réseau informatique à échelle mondiale sur lequel de nombreuses applications sont basées.**

Pour information, 

## Notion de réseaux

### Définitions

Un **réseau informatique** est un ensemble de machines reliées, par différents moyens, qui communiquent entre elles pour échanger des données ou des informations.

On retrouve un certain nombre d'éléments sur un réseau informatique qui ont chacun leur propre rôle.

### Les éléments d'un réseau

Pour qu'un réseau fonctionne, il faut des éléments le constituant.
On retrouve :

| élément  | rôle                                                               | exemple                                      |
|----------|--------------------------------------------------------------------|----------------------------------------------|
| Machines | Élément qui cherche à communiquer, envoyer ou recevoir des données | ordinateur, tablettes, consoles, smartphones |
| Switch   | Élément qui relie de manière locale des machines                   | box internet, switch RJ45                    |
| Routeur  | Élément qui permet de relier un réseau local à Internet ou d'autres réseaux | Box internet, routeur spécifique    |
| Cables, Ondes | Élément qui permet de relier les diverses machines au Switch ou au routeur| Câble Ethernet, Fibre optique, WiFi|

On a défini dans les rôles divers types de réseaux.

On parle de réseau **local** lorsque dans un réseau, divers machines peuvent communiquer directement entre elles sans passer par d'autres réseaux. Exemple : un réseau domestique.

On peut représenter cela de cette manière :
![rlinternet](img/rlinternet.png)

On dispose de machines, d'un réseau mais, comment se retrouvent-elles pour communiquer? Quelles techniques sont utilisées?

## Adressages

### Adressage de machines sur un réseau local

Une machine dispose d'une ou plusieurs **cartes réseaux**. Ces cartes permettent de communiquer de manière locale ou de manière globale vers Internet.
Ces cartes disposent de plusieurs adresses qui permettent de l'identifier sur un réseau.

De manière locale, une carte réseau dispose d'une adresse **MAC (Media Access Control)**.
Cette adresse MAC peut aussi être appelée **adresse physique** car elle correspond à l'adresse utilisée par le port Ethernet et le protocole Ethernet.

Cette adresse est composée de 6 blocs de 2 caractères hexadécimaux. `Exemple : a1:b2:c3:d4:e5:f6`.

La base hexadécimale correspond à une représentation en 16 caractères de chiffres ou de nombres.

**Rédiger le tableau de conversion hexadécimal - décimal**.

### Adressage de machines sur Internet

Chaque réseau doit pouvoir être accessible et reconnaissable.
Sur Internet, on utilise ce que l'on appelle **l'Adresse IP** (pour Internet Protocole).

Une adresse IP est constituée de 4 nombres allant de 0 à 255 représenté en binaire.

Le binaire correspond à une représentation en 2 caractères de chiffres ou de nombres (0 et 1).

Par exemple : 127.0.0.1 est une adresse IP écrite en base 10, compréhensible par l'humain mais pas par l'ordinateur.

Il faut pouvoir convertir ces nombres en représentation **décimale** en **binaire**.

**Voir partie binaire.**

L'adresse IP est constituée de 2 parties :

* La partie Réseau : elle permet d'identifier un réseau sur Internet.
* La partie Machine : elle permet d'identifier une machine sur le réseau défini.

Pour connaître ces deux parties, on utilise ce que l'on appelle un **masque**.
Il permet de définir la répartition du nombre de bits pour la partie Réseau. On pourra en déduire le nombre de bits réservés pour la partie Machine. On peut le représenter de diverses manières :

_______________________________________________________________________________________
_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
______________________________________________________________________________________________________________________________________________________________________________

**Exemple :** 

On dispose de l'adresse **128.40.94.3** qui dispose d'un masque de 16 bits.  
Cela correspond en binaire à $10000000.00101000.01011110.00000100_2$.  
Cela veut dire que le masque est $11111111.11111111.00000000.00000000_2$.  

On peut donc définir que l'adresse du serveur est **128.40.0.0** et que cette adresse correspond à la machine **94.3** de ce réseau.

!!! Warning
    L'adresse réseau est très importante car deux machines sont dans le même réseau si elles ont la même adresse réseau.

## La communication entre deux machines

On sait comment les machines se reconnaissent sur Internet (quelle sont les adresses) mais on veut savoir surtout comment des données transitent sur Internet pour aller d'une machine à une autre.

Pour échanger des données, on ne peut pas les envoyer de but en blanc. En effet, les données sont trop volumineuses pour être envoyées d'un coup, il faut les découper. On appelle **paquet** une découpe d'une donnée qui doit être échangée entre deux machines.

Le protocole TCP-IP permet la communication et l'échange de données sur Internet entre une machine **émettrice** et une **réceptrice**.

Ce protocole est composé de deux protocoles :

* Le protocole TCP permet le contrôle et la sécurité de l'envoi des paquets. Il permet d'être sur qu'un paquet est arrivé à destination à l'aide **d'accusés de réceptions**.
* Le protocole IP qui permet d'identifier quelles machines sur quels réseaux communiquent à l'aide de l'adresse IP.

Le protocole TCP-IP fonctionne en plusieurs étapes :

1. Le protocole découpe la donnée à échanger en plusieurs paquets composés de 0 et de 1 d'une certaine taille donnée et numérotés.
2. La donnée transite pour partir de la machine de départ à la machine de destination.
3. Tous les paquets sont reconstruits à l'aide de leur numérotation.
4. Enfin, un contrôle est réalisé par la machine de réception pour s'assurer que la donnée est bien **intègre**, c'est à dire que la donnée est bien correcte. Si la donnée n'est pas correcte, la machine de reception demande de renvoyer les paquets "défectueux".

## Recherches : Topologie de réseaux

**Réaliser une recherche sur une des topologies de réseaux suivantes :**

* Topologie étoile
* Topologie anneau
* Topologie bus
* Topologie maillé (pair à pair)

**Quelle topologie est la plus utilisée dans un usage domestique?**
