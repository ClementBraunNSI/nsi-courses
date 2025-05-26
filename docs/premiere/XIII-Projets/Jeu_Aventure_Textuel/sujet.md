# Projet - Jeu d'Aventure Textuel avec Sauvegarde ⚔️🗺️

L'objectif de ce projet est de développer un jeu d'aventure textuel où le joueur explore différents lieux, interagit avec des objets et des personnages, et dont la progression peut être sauvegardée et reprise.

## Concepts Abordés

- Structures de données : dictionnaires (pour représenter les lieux, l'inventaire), listes.
- Fonctions et modularité.
- Manipulation de chaînes de caractères pour l'analyse des commandes du joueur.
- Logique conditionnelle (gestion des choix et des conséquences).
- Sauvegarde et chargement de l'état du jeu (utilisation de fichiers JSON ou pickle).

## Fonctionnalités à Implémenter

### 1. Définition du Monde du Jeu

Le monde du jeu est composé de plusieurs lieux interconnectés. Chaque lieu a une description, des sorties possibles vers d'autres lieux, et potentiellement des objets à ramasser ou des personnages à rencontrer.

!!! fox_exercice "Structure d'un lieu"
    Définir une structure pour représenter un lieu. Un dictionnaire est un bon choix. Chaque lieu devrait avoir au moins :
    - `nom` (chaîne de caractères, ex: "Forêt Sombre")
    - `description` (chaîne de caractères, ex: "Vous êtes dans une forêt sombre et menaçante. Un sentier part vers le nord.")
    - `sorties` (un dictionnaire où les clés sont des directions, ex: "nord", "sud", et les valeurs sont les noms des lieux correspondants, ex: "Clairière Ensoleillée")
    - `objets` (une liste de chaînes de caractères représentant les objets présents dans le lieu, ex: ["épée rouillée", "potion de soin"])

!!! fox_exercice "Création de la carte du jeu"
    Créer un dictionnaire principal nommé `carte_du_jeu` où les clés sont les noms des lieux et les valeurs sont les dictionnaires de lieu que vous avez définis.
    Créer au moins 3-4 lieux interconnectés pour commencer.
    Par exemple :
    ```python
    carte_du_jeu = {
        "Forêt Sombre": {
            "description": "Vous êtes dans une forêt sombre et menaçante. Un sentier part vers le nord.",
            "sorties": {"nord": "Clairière Ensoleillée"},
            "objets": ["branche solide"]
        },
        "Clairière Ensoleillée": {
            "description": "Une douce lumière baigne cette clairière. Un vieux puits se trouve au centre. Des chemins mènent au sud et à l'est.",
            "sorties": {"sud": "Forêt Sombre", "est": "Caverne Mystérieuse"},
            "objets": ["vieille corde"]
        }
        # Ajoutez d'autres lieux
    }
    ```

### 2. Le Joueur

Le joueur a un état qui doit être suivi : son lieu actuel et son inventaire.

!!! fox_exercice "État du joueur"
    Créer un dictionnaire `joueur` pour stocker les informations du joueur :
    - `lieu_actuel` (chaîne de caractères, le nom du lieu où se trouve le joueur, initialisé au lieu de départ)
    - `inventaire` (une liste de chaînes de caractères, initialement vide)

### 3. Mécaniques de Jeu de Base

!!! fox_exercice "Afficher le lieu actuel"
    Créer une fonction `afficher_lieu(carte, nom_lieu)` qui affiche la description du lieu actuel et les objets visibles.

!!! fox_exercice "Déplacement du joueur"
    Créer une fonction `se_deplacer(joueur, carte, direction)` qui :
    1. Vérifie si la `direction` est une sortie valide depuis le `lieu_actuel` du joueur.
    2. Si oui, met à jour `joueur['lieu_actuel']` avec le nouveau lieu et renvoie `True`.
    3. Si non, affiche un message d'erreur (ex: "Vous ne pouvez pas aller par là.") et renvoie `False`.

!!! fox_exercice "Ramasser un objet"
    Créer une fonction `ramasser_objet(joueur, carte, nom_objet)` qui :
    1. Vérifie si `nom_objet` est présent dans la liste `objets` du `lieu_actuel`.
    2. Si oui, ajoute l'objet à `joueur['inventaire']`, le retire du lieu, affiche un message (ex: "Vous avez ramassé : épée rouillée") et renvoie `True`.
    3. Si non, affiche un message d'erreur et renvoie `False`.

!!! fox_exercice "Afficher l'inventaire"
    Créer une fonction `afficher_inventaire(joueur)` qui affiche le contenu de l'inventaire du joueur.

### 4. Boucle de Jeu et Analyseur de Commandes

!!! fox_exercice "Analyseur de commandes simples"
    Créer une fonction `analyser_commande(commande_str)` qui prend la chaîne de caractères entrée par le joueur (ex: "aller nord", "prendre épée") et la décompose en un verbe d'action (ex: "aller", "prendre") et un argument optionnel (ex: "nord", "épée").
    La fonction devrait renvoyer un tuple, par exemple `("aller", "nord")` ou `("inventaire", None)`.
    Gérer au moins les commandes : `aller <direction>`, `prendre <objet>`, `inventaire`, `regarder` (pour ré-afficher la description du lieu), `quitter`.

!!! fox_exercice "Boucle de jeu principale"
    Créer la boucle principale du jeu qui :
    1. Affiche le lieu actuel du joueur.
    2. Demande au joueur d'entrer une commande.
    3. Analyse la commande.
    4. Exécute l'action correspondante en appelant les fonctions appropriées (`se_deplacer`, `ramasser_objet`, etc.).
    5. Continue jusqu'à ce que le joueur tape "quitter" ou qu'une condition de fin de jeu soit atteinte (non implémenté dans cette étape).

!!! fox_exercice_test "Test des mécaniques de base"
    1. Initialiser la `carte_du_jeu` et le `joueur`.
    2. Lancer la boucle de jeu.
    3. Tester les déplacements entre les lieux.
    4. Essayer de vous déplacer dans des directions invalides.
    5. Ramasser des objets présents dans les lieux.
    6. Essayer de ramasser des objets qui ne sont pas là ou déjà pris.
    7. Afficher votre inventaire.
    8. Utiliser la commande `regarder`.
    9. Quitter le jeu.

### 5. Sauvegarde et Chargement de la Partie

!!! fox_exercice "Sauvegarder la partie"
    Créer une fonction `sauvegarder_partie(joueur, carte, nom_fichier)` qui sauvegarde l'état actuel du `joueur` (lieu actuel, inventaire) et l'état de la `carte` (notamment les objets qui ont été déplacés des lieux vers l'inventaire) dans un fichier.
    Le format JSON est recommandé pour sa lisibilité.
    *Astuce : Vous aurez besoin de sauvegarder `joueur['lieu_actuel']`, `joueur['inventaire']`, et l'état actuel de `carte_du_jeu[lieu]['objets']` pour chaque lieu.*

!!! fox_exercice "Charger une partie"
    Créer une fonction `charger_partie(nom_fichier)` qui lit les données depuis le fichier de sauvegarde et restaure l'état du `joueur` et de la `carte`.
    La fonction doit renvoyer le `joueur` et la `carte` chargés. Si le fichier de sauvegarde n'existe pas, elle peut initialiser une nouvelle partie ou renvoyer des valeurs indiquant qu'aucune sauvegarde n'a été trouvée.

!!! fox_exercice "Intégration dans la boucle de jeu"
    Modifier la boucle de jeu pour :
    - Au démarrage, demander à l'utilisateur s'il veut charger une partie sauvegardée ou commencer une nouvelle partie.
    - Ajouter une commande "sauvegarder" que le joueur peut taper pour sauvegarder sa progression.

!!! fox_exercice_test "Test de la sauvegarde et du chargement"
    1. Commencer une nouvelle partie, déplacez-vous, ramassez quelques objets.
    2. Sauvegarder la partie.
    3. Quitter le jeu.
    4. Relancer le jeu et charger la partie sauvegardée.
    5. Vérifier que vous êtes au bon endroit, avec le bon inventaire, et que les objets ramassés ne sont plus dans leurs lieux d'origine.

## Pour aller plus loin (Optionnel)

- **Personnages Non Joueurs (PNJ)** : Ajoutez des PNJ avec qui interagir (commande `parler <personnage>`).
- **Énigmes simples** : Introduisez des énigmes qui nécessitent d'utiliser des objets de l'inventaire (commande `utiliser <objet> sur <cible>`).
- **Conditions de victoire/défaite** : Définissez un objectif pour le jeu.
- **Plus de commandes** : `examiner <objet>`, `lacher <objet>`.
