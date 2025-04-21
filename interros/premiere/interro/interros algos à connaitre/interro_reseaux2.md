# Interrogation : Internet et Réseaux

**L'évaluation porte sur 4 exercices indépendants.**
**Les exercices sont notés sur 24 et la rigueur, rédaction et justifications sont notés sur 2 points.**

## Exercice 1 : Fondamentaux des réseaux (6 points)

1. **Dans quel réseau utilise-t-on l'adresse IP d'une machine ?**
<br/>

2. **Décrire le rôle principal d'un routeur dans un réseau.**
<br/>

1. **Citer et expliquer brièvement le rôle des protocoles TCP et IP.**
<br/>

1. **Expliquer la différence entre un réseau local (LAN) et un réseau global.**

## Exercice 2 : Adressage IP et Sous-réseaux (6 points)

1. *On considère l'adresse IP suivante : 192.168.1.45/16*
<br/>

   a) **Quelle est l'adresse du réseau ?**
   <br/>

   b) **Quel est le masque de sous-réseau en notation décimale ?**
   <br/>

   c) **Combien de machines peuvent avoir une adresse dans ce réseau ? (Attention aux adresses interdites).**
<br/>
1. Dans un réseau d'entreprise, on a les configurations suivantes :
<br/>

- *Serveur Web : 192.168.5.10/24*
   <br/>

- *Base de données : 192.168.4.20/23*
   <br/>

- *Poste Client : 192.168.6.30/23*
  
**Ces machines peuvent-elles communiquer directement entre elles?**  
**Justifier votre réponse en déterminant les plages d'adresses de chaque sous-réseau.**

## Exercice 3 : Modèle TCP/IP et Encapsulation (6 points)

1. **Qu'est-ce que l'encapsulation? (Modèle IP)? Donner le nom des 4 couches du Modèle TCP/IP.**  
</br>
2. *Pour le protocole TCP :*
   a) **Expliquer le mécanisme de la "triple poignée de main" (three-way handshake) lors de l'établissement d'une connexion.**  
   b) **Comment le protocole TCP garantit la livraison des données?**
   c) **Expliquer comment TCP gère les erreurs de transmission et la retransmission des paquets perdus.**

## Exercice 4 : Vrai ou Faux - Configuration réseau (6 points)

On considère le réseau local suivant composé de trois sous-réseaux, on considère aussi que les routeurs sont reliés entre eux et que les passerelles leurs sont renseignées:

**Sous-réseau A :**

- PC1 : 192.168.1.10/24
- PC2 : 192.168.1.10/24
- Passerelle : 192.168.1.254

**Sous-réseau B :**

- Serveur1 : 192.168.2.50/24
- Serveur2 : 192.168.2.51/24
- Passerelle : 192.168.1.254

**Sous-réseau C :**

- Imprimante : 192.168.3.100/24
- Scanner : 192.168.3.101/24
- Passerelle : 192.168.3.1

**Pour chaque affirmation, indiquez si elle est vraie ou fausse et justifiez votre réponse :**

1. Les PC1 et PC2 peuvent communiquer entre eux car ils sont dans le même sous-réseau.
2. La configuration des passerelles permet une communication entre tous les sous-réseaux.
3. Il n'y a aucun conflit d'adresse IP dans ce réseau.
4. Les serveurs du sous-réseau B peuvent accéder à l'imprimante du sous-réseau C.
5. La configuration actuelle respecte les normes de l'adressage IP que l'on s'est fixés en cours.