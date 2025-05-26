# Projet - Réseau Social Simplifié 👥

Ce projet vise à simuler les fonctionnalités de base d'un réseau social en mode texte. Les utilisateurs pourront créer des comptes, se connecter, publier des messages, voir les messages de leurs amis, et gérer leurs amitiés.

## Concepts Abordés

- Structures de données : dictionnaires (pour les profils utilisateurs, les messages), listes (pour les listes d'amis, les fils d'actualité).
- Gestion de "bases de données" simples (par exemple, une liste de dictionnaires pour les utilisateurs, une autre pour les messages).
- Fonctions pour encapsuler les différentes actions.
- Logique de session utilisateur (utilisateur connecté).
- Manipulation de dates et heures (pour horodater les messages).

## Fonctionnalités à Implémenter

### 1. Gestion des Utilisateurs

Chaque utilisateur aura un profil.

!!! fox_exercice "Structure d'un profil utilisateur"
    Définissez une structure pour un profil utilisateur. Un dictionnaire est approprié :
    - `nom_utilisateur` (chaîne de caractères, unique)
    - `mot_de_passe` (chaîne de caractères - pour la simplicité, nous ne nous préoccuperons pas du hachage sécurisé dans ce projet de base)
    - `amis` (une liste de `nom_utilisateur`)
    - `messages_publies` (une liste d'identifiants de messages, ou les messages eux-mêmes)

!!! fox_exercice "Base de données des utilisateurs"
    Créez une liste globale (ou une structure de données équivalente) nommée `utilisateurs_db` pour stocker tous les profils utilisateurs.

!!! fox_exercice "Création de compte (Inscription)"
    Créez une fonction `creer_compte(utilisateurs_db, nom_utilisateur, mot_de_passe)` qui :
    1. Vérifie si `nom_utilisateur` existe déjà dans `utilisateurs_db`.
    2. Si non, crée un nouveau profil utilisateur (avec une liste d'amis et de messages vide) et l'ajoute à `utilisateurs_db`.
    3. Renvoie `True` si le compte est créé, `False` sinon (nom d'utilisateur déjà pris).

!!! fox_exercice "Connexion"
    Créez une fonction `se_connecter(utilisateurs_db, nom_utilisateur, mot_de_passe)` qui :
    1. Recherche l'utilisateur dans `utilisateurs_db`.
    2. Vérifie si le `mot_de_passe` fourni correspond.
    3. Renvoie le dictionnaire du profil utilisateur si la connexion réussit, `None` sinon.
    Gérez une variable globale `utilisateur_connecte` qui stockera le profil de l'utilisateur actuellement connecté (ou `None` si personne n'est connecté).

!!! fox_exercice_test "Tests de gestion des utilisateurs"
    1. Initialisez `utilisateurs_db`.
    2. Créez plusieurs comptes utilisateurs. Essayez de créer un compte avec un nom d'utilisateur existant.
    3. Tentez de vous connecter avec des identifiants corrects et incorrects.
    4. Vérifiez l'état de `utilisateur_connecte` après une connexion réussie et une déconnexion (implicite ou explicite si vous ajoutez une fonction de déconnexion).

### 2. Gestion des Amitiés

!!! fox_exercice "Envoyer une demande d'ami"
    Pour simplifier, nous allons considérer que les amitiés sont bidirectionnelles et instantanées (pas de système de demande/acceptation).
    Créez une fonction `ajouter_ami(utilisateurs_db, nom_utilisateur_connecte, nom_nouvel_ami)` qui :
    1. Vérifie que `nom_nouvel_ami` existe et n'est pas déjà ami avec `nom_utilisateur_connecte`.
    2. Ajoute `nom_nouvel_ami` à la liste `amis` de `nom_utilisateur_connecte`.
    3. Ajoute `nom_utilisateur_connecte` à la liste `amis` de `nom_nouvel_ami`.
    4. Renvoie `True` si l'amitié est ajoutée, `False` sinon (ami inexistant, déjà ami, ou tentative de s'ajouter soi-même).

!!! fox_exercice "Voir la liste d'amis"
    Créez une fonction `voir_amis(profil_utilisateur)` qui affiche la liste des amis de l'utilisateur dont le profil est fourni.

!!! fox_exercice_test "Tests de gestion des amitiés"
    1. Connectez-vous avec un utilisateur.
    2. Ajoutez plusieurs amis. Essayez d'ajouter un ami inexistant ou déjà ami.
    3. Connectez-vous avec un autre utilisateur et vérifiez que l'amitié est bien réciproque.
    4. Affichez les listes d'amis des utilisateurs concernés.

### 3. Publication et Affichage de Messages

Chaque message aura un contenu, un auteur, et une date de publication.

!!! fox_exercice "Structure d'un message"
    Définissez une structure pour un message (dictionnaire) :
    - `id_message` (entier, unique, peut être généré automatiquement)
    - `auteur` (chaîne de caractères, `nom_utilisateur`)
    - `contenu` (chaîne de caractères)
    - `timestamp` (date et heure de publication, utilisez le module `datetime`)

!!! fox_exercice "Base de données des messages"
    Créez une liste globale `messages_db` pour stocker tous les messages.
    Créez un compteur global `prochain_id_message` initialisé à 1.

!!! fox_exercice "Publier un message"
    Créez une fonction `publier_message(utilisateur_connecte, messages_db, contenu)` qui :
    1. Crée un nouveau dictionnaire de message avec un `id_message` unique (utilisez et incrémentez `prochain_id_message`), l'`auteur` (nom de l'utilisateur connecté), le `contenu`, et le `timestamp` actuel.
    2. Ajoute le message à `messages_db`.
    3. Ajoute l'`id_message` (ou une référence au message) à la liste `messages_publies` du profil de l'`utilisateur_connecte`.
    4. Renvoie le message créé.

!!! fox_exercice "Afficher le fil d'actualité"
    Créez une fonction `afficher_fil_actualite(utilisateur_connecte, utilisateurs_db, messages_db)` qui :
    1. Récupère la liste des amis de `utilisateur_connecte`.
    2. Collecte tous les messages publiés par `utilisateur_connecte` ET par ses amis.
    3. Trie ces messages par `timestamp` (du plus récent au plus ancien).
    4. Affiche les messages de manière lisible (par exemple: "[Timestamp] Auteur: Contenu").

!!! fox_exercice_test "Tests des messages et du fil d'actualité"
    1. Connectez-vous avec un utilisateur A.
    2. Publiez plusieurs messages.
    3. Connectez-vous avec un utilisateur B, ami avec A.
    4. Publiez plusieurs messages avec B.
    5. Affichez le fil d'actualité de A (devrait voir les messages de A et B).
    6. Affichez le fil d'actualité de B (devrait voir les messages de B et A).
    7. Connectez-vous avec un utilisateur C, non ami avec A ou B, et publiez un message.
    8. Vérifiez que les fils d'actualité de A et B n'affichent pas les messages de C (sauf si C est aussi leur propre message).

### 4. Interface Utilisateur (Menu Principal)

!!! fox_exercice "Menu principal"
    Créez une fonction `menu_principal()` qui gère l'état connecté/déconnecté.
    - Si déconnecté, propose : "1. Créer un compte", "2. Se connecter", "3. Quitter".
    - Si connecté, propose : "1. Publier un message", "2. Voir mon fil d'actualité", "3. Ajouter un ami", "4. Voir mes amis", "5. Se déconnecter", "6. Quitter".
    La fonction doit lire le choix de l'utilisateur et appeler les fonctions correspondantes.

!!! fox_exercice_test "Test de l'interface complète"
    Simulez une session complète :
    1. Créez deux ou trois utilisateurs.
    2. Connectez l'utilisateur A.
    3. Faites-lui ajouter l'utilisateur B comme ami.
    4. Publiez des messages avec A.
    5. Déconnectez A.
    6. Connectez B.
    7. Publiez des messages avec B.
    8. Affichez le fil d'actualité de B (doit contenir les messages de A et B).
    9. Quittez.

## Pour aller plus loin (Optionnel)

- **Suppression de messages/amis**.
- **Profils utilisateurs plus détaillés** (bio, photo de profil - textuelle!).
- **Messages privés** entre deux utilisateurs.
- **"J'aime"** sur les messages.
- **Persistance des données** : Sauvegardez `utilisateurs_db` et `messages_db` dans des fichiers (JSON ou CSV) pour que les données ne soient pas perdues à la fermeture du programme.
