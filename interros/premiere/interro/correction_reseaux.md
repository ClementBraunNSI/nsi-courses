# Correction : Internet et Réseaux

## Exercice 1 : Fondamentaux des réseaux (6 points)

1. **Différence entre adresse MAC et adresse IP (1.5 points)**
   - Adresse MAC :
     * Identifiant physique unique attribué à la carte réseau
     * Adresse sur 48 bits (6 octets) inscrite de façon permanente
     * Format : XX:XX:XX:XX:XX:XX (hexadécimal)
   - Adresse IP :
     * Identifiant logique attribué à une machine sur un réseau
     * Peut être changée et réattribuée
     * Format : XXX.XXX.XXX.XXX (4 octets en décimal)

2. **Rôle principal d'un routeur (1.5 points)**
   - Interconnecter différents réseaux
   - Acheminer les paquets de données entre ces réseaux
   - Déterminer le meilleur chemin pour transmettre les données
   - Maintenir des tables de routage pour diriger le trafic

3. **Deux protocoles du modèle TCP/IP (1.5 points)**
   - TCP (Transmission Control Protocol) :
     * Assure une transmission fiable et ordonnée des données
     * Établit une connexion (three-way handshake)
     * Contrôle de flux et gestion des erreurs
   - IP (Internet Protocol) :
     * Adressage et routage des paquets
     * Fragmentation et réassemblage des données
     * Pas de garantie de livraison

4. **Différence entre LAN et réseau global (1.5 points)**
   - Réseau Local (LAN) :
     * Limité géographiquement (bâtiment, campus)
     * Haute vitesse de transmission
     * Géré par une seule organisation
   - Réseau Global :
     * Couvre une zone géographique étendue
     * Interconnecte plusieurs réseaux locaux
     * Utilise des infrastructures publiques

## Exercice 2 : Adressage IP et Sous-réseaux (6 points)

1. **Pour l'adresse 192.168.1.45/24 (3 points)**

   a) Adresse du réseau (1 point)
   - 192.168.1.0
   - Car le masque /24 signifie que les 24 premiers bits sont fixes

   b) Masque en notation décimale (1 point)
   - 255.255.255.0
   - Car /24 = 24 bits à 1 suivis de 8 bits à 0

   c) Nombre d'hôtes possibles (1 point)
   - 2^8 - 2 = 254 hôtes
   - On soustrait 2 car l'adresse réseau et broadcast sont réservées

2. **Analyse des configurations réseau (3 points)**
   - Avec un masque /23 :
     * Serveur Web (192.168.5.10/23) : réseau 192.168.4.0 - 192.168.5.255
     * Base de données (192.168.4.20/23) : réseau 192.168.4.0 - 192.168.5.255
     * Poste Client (192.168.6.30/23) : réseau 192.168.6.0 - 192.168.7.255

   - Conclusion :
     * Le serveur web et la base de données sont dans le même sous-réseau
     * Le poste client est dans un sous-réseau différent
     * Communication directe possible uniquement entre le serveur web et la base de données

## Exercice 3 : Modèle TCP/IP et Encapsulation (6 points)

1. **Processus d'encapsulation (3 points)**
   - Couche Application :
     * Génération des données utilisateur
     * Protocoles : HTTP, FTP, SMTP
   - Couche Transport :
     * Segmentation des données
     * Ajout des en-têtes TCP/UDP
   - Couche Internet :
     * Ajout de l'en-tête IP
     * Adressage et routage
   - Couche Accès réseau :
     * Ajout des en-têtes MAC
     * Transmission physique

2. **Protocole TCP (3 points)**

   a) Triple poignée de main (1 point)
   1. Client envoie SYN
   2. Serveur répond SYN-ACK
   3. Client confirme avec ACK

   b) Garantie de livraison (1 point)
   - Numérotation des segments
   - Accusés de réception (ACK)
   - Retransmission si perte
   - Contrôle de flux

   c) Comparaison TCP/UDP (1 point)
   - TCP : Fiable, ordonné, mais plus lent
     * Cas d'usage : transfert de fichiers, email
   - UDP : Rapide, sans connexion, pas de garantie
     * Cas d'usage : streaming, jeux en ligne

## Exercice 4 : Réparation d'un réseau dysfonctionnel (6 points)

Problèmes identifiés et corrections :

1. **Conflit d'adressage IP (2 points)**
   - Vérifier que chaque machine a une adresse IP unique
   - Corriger les doublons d'adresses IP

2. **Configuration des masques de sous-réseau (2 points)**
   - S'assurer que les machines d'un même réseau ont le même masque
   - Vérifier que les plages d'adresses ne se chevauchent pas

3. **Configuration des passerelles (2 points)**
   - Configurer correctement les passerelles par défaut
   - Vérifier que les routeurs ont des interfaces dans les bons sous-réseaux

**Rigueur, rédaction et justifications : 2 points**
- Clarté des explications
- Justification des réponses
- Utilisation du vocabulaire technique approprié