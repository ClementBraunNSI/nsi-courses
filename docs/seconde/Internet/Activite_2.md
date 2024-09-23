# TP ARCHITECTURE RÉSEAU : DNS

Nous avons vu au premier TP comment créer un réseau d’ordinateurs et
comment accéder d’une machine à une autre grâce au routage et aux
passerelles.

Dans ce micro-TP, on traitera de la notion de serveur DNS.

## 1 - Création du réseau

Reprendre le réseau du TP précédent.

## 2 - Un serveur WEB

1 - Rajouter un ordinateur dans le réseau 192.168.5.0 et le configurer pour y
avoir accès.

2 - En mode lecture, ajouter le logiciel de serveur web sur l’ordinateur.

3 - Double cliquer sur l’application serveur web et démarrer le serveur.

4 - Sur la machine 192.168.1.11, ajouter le logiciel de navigation internet et
rentrer dans la barre des tâches l’adresse IP du serveur web fraîchement
créé. La page devrait s’actualiser.

## 3 - Un serveur DNS

Ajouter une interface au routeur et dans un réseau 192.168.2.11, ajouter un
ordinateur.

Vous devrez vous retrouver avec ce réseau.

1 - Sur la machine 192.168.2.11, ajouter l’application serveur DNS et ouvrez-
la.

2 - Comme nom de domaine, ajoutez le _[http://www.nsi.fr](http://www.nsi.fr)_ et pour domaine
192.168.3.12, notre précédent serveur WEB.

3 - Est ce possible d’accéder à la page _[http://www.nsi.fr](http://www.nsi.fr)_?

4 - Ajouter l’adresse du serveur DNS pour tous les ordinateurs. Est-ce
possible d’accéder à la page?


## 4 - Ajouter sa page web

Sur le serveur WEB, ajouter l’application explorateur de fichiers.
Importer votre fichier index.html et le mettre dans le dossier webserver.

Actualiser et essayer d’accéder à sa page sur la machine 192.168.1.10.


