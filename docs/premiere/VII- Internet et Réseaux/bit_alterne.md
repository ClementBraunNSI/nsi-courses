# Bit alterné

## Quelle est l'utilité du protocole du bit alterné ?

Dans une communication, on souhaite toujours savoir si la personne qui doit recevoir un message, le reçoit réellement.
On peut l'illustrer par exemple avec l'usage d'un talkie walkie : 
A chaque message parlé sur le talkie-walkie, l'utilisateur utilise un code spécial pour dire que son message est terminé, en général "Terminé"
L'autre correspondant, s'il a reçu le message précédent doit bien commencer le sien par "Je reçois" ou "Reçu".
Cela permettait aux différents communiquants d'accuser réceptions de leurs messages respectifs.

![talkie_walkie](./talkie%20walkie.png)

Cela peut se transposer dans les communications numériques, notamment l'envoi de paquets.
**Rappel** : Avoir besoin d'un accusé de reception est une des principes fondamentaux du protocole TCP.
**Voir le cours sur les protocoles de communication**

<br>
<br>
<br>

## Comment cela s'illustre-t-il ?

En informatique, on se rapproche du même principe. 
Dans chaque requête, on dispose d'un bit, souvent représenté à la fin de l'entête, qui correspond à un envoi de message.

Dans le modèle client-serveur, le client envoie sa première requête avec ce bit à 0.
Le serveur, reçoit la requête, analyse la valeur du bit, s'il vaut 0, il envoie sa ressource avec le bit correspondant à 1.

On distingue deux cas :

- Si le client reçoit la ressource, il s'aperçoit que le bit est à 1, donc que sa requête à bien été traitée par le serveur. Il envoie donc une autre requête avec cette fois-ci ce bit de contrôle à 1 pour indiquer au serveur qu'il a reçu sa réponse.
- L'envoie de paquet est chronométré. Si le serveur n'a accusé de la reception de la ressource par le client, il se passe une TIMEOUT. Le serveur comprend que la ressource n'est pas arrivée et donc la renvoie avec le même bit de contrôle.

Si le client reçoit enfin sa ressource, il réalise une nouvelle requête avec le bit de contrôle reçu. 
Le serveur lui envoie la ressource suivante avec cette fois-ci le bit de contrôle inverse, indiquant qu'il a bien connaissance que le client a reçu la ressource précédente.




