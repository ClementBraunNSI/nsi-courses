# Projet - PokéNSI (Partie 1) 🎮

Le but de ce projet est de créer un jeu inspiré de Pokémon en utilisant Python.
Dans cette première partie, nous allons nous concentrer sur la création du Pokédex et la mise en place du système de combat.

## Le Pokédex 📱

Le Pokédex est une base de données qui contient tous les Pokémon du jeu. Chaque Pokémon possède les caractéristiques suivantes :

- nom (chaîne de caractères) 📝  
- hp (points de vie) ❤️  
- atq (points d'attaque) ⚔️  
- def (points de défense) 🛡️  
- attaques (liste des attaques disponibles) 💥  
- evolution (nom du Pokémon évolué) ✨  
- niveau_evolution (niveau requis pour évoluer) 📈  
- niveau (niveau actuel du Pokémon) 📊  
- xp (points d'expérience) ⭐  

### Création du Pokédex 🛠️

!!! fox_exercice "Création du Pokédex"
    **Créer une liste vide `pokedex` qui contiendra tous les Pokémon du jeu.**

!!! fox_exercice "Remplissage du Pokédex"
    On dispose de la fonction `remplir_pokedex` suivante. Elle permet de récupérer toutes les informations des pokemons pour en faire une liste de dictionnaires.

    ```python
        
        def remplir_pokedex(filename:str)->list:
            pokedex = []
            with open(filename,'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["nom"] != '' or pokemon_dans_pokedex(row["nom"]) == None:
                        pokedex.append({"nom":row["nom"],"hp":int(row["hp"]),
                                        "atq":int(row["atq"]),"def":int(row["def"]),"attaques":row["attaques"].split(";"),
                                        "evolution":row["evolution"],"niveau_evolution":int(row["niveau_evolution"]),"niveau":int(row["niveau"]), "xp":int(row["xp"])})
            return pokedex
    ```

    Vous utiliserez le fichier csv suivant : [pokedex.csv](pokedex.csv).
    Vous retrouverez comment importer un fichier `csv` dans le cours suivant : [cours sur le CSV](../../V%20-%20Dictionnaires%20et%20Traitement%20de%20tables/Cours/Cours_2.md)

!!! fox_exercice "Recherche dans le Pokédex 🔍"
    **Créer la fonction `pokemon_dans_pokedex` qui prend en paramètre un nom de Pokémon (str) et renvoie le dictionnaire correspondant au Pokémon s'il existe dans le pokédex, None sinon.**

!!! fox_exercice_test "Test du Pokédex ✅"
    **Tester vos fonctions de création du Pokédex :**
    1. Créer le Pokédex vide  
    2. Remplir le Pokédex avec le fichier CSV fourni  
    3. Afficher tous les Pokémon du Pokédex pour vérifier leur importation  
    4. Tester la fonction `pokemon_dans_pokedex` avec "Pikachu" puis avec "Mewtwo"  

## Le système de combat ⚔️

### Les attaques 💥

!!! fox_exercice "Dictionnaire d'attaques"
    **Créer un dictionnaire `attaques` qui contient les noms des attaques comme clés et leur puissance comme valeurs.**

    Exemple d'attaques à implémenter :  
    - tonerre ⚡: 40 points de dégâts  
    - queue de fer 🔨: 20 points de dégâts  
    - fouet lianes 🌿: 10 points de dégâts  
    - tranch'herbe 🌱: 20 points de dégâts  

### Gestion des dégâts 💢

Lors d'un combat, un pokemon doit en attaquer un autre avec une attaque. Cette attaque retire des points de vie au pokemon et les dégats sont calculés suivant la formule ci-après : 

$$\texttt{dégats}=\frac{(((N*0.4)+2)*\texttt{Atq}*\texttt{Deg})}{\texttt{Def}*50}+2$$

Avec :

- N : Niveau du Pokémon attaquant 📊  
- Atq : L'attaque du pokemon attaquant ⚔️  
- Deg : Les dégats de base de l'attaque reçue 💥  
- Def : La défense du pokémon défenseur 🛡️  

!!! fox_exercice "Gestion des points de vie  ❤️"
    **Créer la fonction `retirer_hp` qui prend en paramètre un Pokémon et un malus, et retire ces points de vie au Pokémon si les dégats est positif, c'est-à-dire si le pokemon defenseur réussit à `tanker` les dégats.**

!!! fox_exercice "Système d'attaque ⚔️"
    **Créer la fonction `attaquer` qui prend en paramètre un Pokémon attaquant, un Pokémon défenseur et une attaque.**  
    Cette fonction doit :  
    1. Récupérer les dégâts de base de l'attaque  
    2. Calculer les dégâts finaux selon la formule précédente  
    3. Retirer les points de vie au défenseur  

!!! fox_exercice_test "Test d'une attaque ⚡"
    1. Créer un Pikachu niveau 1.  
    2. Créer un Bulbizarre niveau 1.  
    3. Faire attaquer le Bulbizarre par le Pikachu grâce à son attaque `Tonnerre`.  
    4. Afficher les point de vie du Bulbizarre pour vérifier le bon fonctionnement.  

### Interface de combat 🎮

!!! fox_exercice "Affichage des attaques 📝"
    **Créer la fonction `afficher_attaques` qui prend en paramètre un Pokémon et affiche la liste numérotée de ses attaques disponibles.**

!!! fox_exercice "Choix d'attaque 🎯"
    **Créer la fonction `choisir_attaque` qui prend en paramètre un Pokémon et un type de joueur ("Joueur" ou "Ordi") et renvoie l'attaque choisie.**

    - Pour le joueur humain : afficher les attaques et demander un choix (1,2,3 ou 4) suivant le nombre d'attaques disponibles  
    - Pour l'ordinateur : choisir une attaque aléatoirement  

### Système d'expérience 📈

!!! fox_exercice "Augmentation des statistiques 💪"

    **Créer la fonction `augmenter_stats` qui prend en paramètre un Pokémon et augmente ses statistiques selon les formules :**  
    - `hp = hp + (1/50 * hp * niveau)`  
    - `atq = atq + (1/50 * atq * niveau)`  
    - `def = def + (1/50 * def * niveau)`  

!!! fox_exercice "Système d'évolution ✨"

    **Créer la fonction `evolution` qui prend en paramètre un Pokemon et le fait évoluer si son niveau actuel est supérieur au niveau requis pour évoluer.**
    Cette fonction demande à l'utilisateur s'il veut faire évoluer son pokemon via un choix (`input`).

    - Si le joueur indique `Oui`, alors cette fonction devra modifier le nom, l'attaque, la défense, le niveau pour sa prochaine évolution et le nom de son évolution  
    - Si le joueur indique `Non`, alors il ne se passe rien  

!!! question "Evoluer un pokemon 🤔"
    Il existe de nombreuses raisons de ne pas faire évoluer un pokemon. Certains apprennent des attaques plus rapidement que leur version évoluée.
    D'autres comme Ningale, s'il atteint le 20, il évoluera en Munja mais si le joueur a un slot de libre dans son équipe, il obtiendra en plus le pokemon Munjask.

Un pokemon peut monter de niveau si et seulement si :  
$\texttt{Experience} = 0.8*(\texttt{Niveau} +5)^3$

!!! fox_exercice "Gestion des niveaux 📊"
    **Créer la fonction `niveau_superieur` qui prend en paramètre un Pokemon et augmente son niveau.**
    Cette fonction a un rôle clef dans l'évolution du jeu car elle permet de faire monter les niveaux d'un pokemon, de modifier ses stats comme il monte de niveau et de le faire évoluer.
    Cette fonction devra utiliser les 2 précédentes :

    - Si le pokemon peut évoluer, alors on propose au joueur de le faire évoluer avec la fonction `evolution`
    - Augmente les stats du pokemon avec la fonction `augmenter_stats`
  
!!! fox_exercice_test "Test du système d'expérience 🌟"
    **Tester le gain d'expérience et la montée de niveau :**
    1. Créer un Pikachu niveau 1.
    2. Attribuer 300 xp au Pikachu.
    3. Utiliser la fonction `niveau_superieur` et vérifier qu'il passe bien niveau 2.
    4. Mettre Pikachu niveau 25.
    5. Utiliser la fonction `evolution` et vérifier, en indiquant le bon choix, qu'il devient bien un Raichu et que ses stats sont bien actualisées en fonction de son niveau.

### Combat complet 🏆

!!! fox_exercice "Système de combat contre un Pokémon sauvage 🆚"
    **Créer la fonction `combat_pokemon_sauvage` qui prend en paramètre une équipe de Pokémon et un Pokémon sauvage.**
    
    La fonction doit gérer un combat complet selon les étapes suivantes:

    1. **Initialisation** 🎬
        - Sélectionner le premier Pokémon de l'équipe
        - Sauvegarder les HP initiaux du Pokémon sauvage

    2. **Boucle de combat** ⚔️
        - Afficher l'état du combat (HP des deux Pokémon)
        - Tour du joueur:
            * Choisir une attaque
            * Appliquer les dégâts au Pokémon sauvage
            * Vérifier si le Pokémon sauvage est K.O.
        - Tour du Pokémon sauvage:
            * Choisir une attaque aléatoire
            * Appliquer les dégâts au Pokémon du joueur
            * Vérifier si le Pokémon du joueur est K.O.

    3. **Gestion des K.O.** 💫
        - Si le Pokémon sauvage est K.O.:
            * Attribuer l'expérience au Pokémon vainqueur
            * Vérifier la montée de niveau
            * Terminer le combat (Victoire)
        - Si le Pokémon du joueur est K.O.:
            * Passer au Pokémon suivant dans l'équipe
            * Si plus de Pokémon disponible, terminer le combat (Défaite)
            * Sinon, continuer le combat avec le nouveau Pokémon

    La fonction doit renvoyer:
    - `True` si le joueur gagne 🏆
    - `False` si tous les Pokémon de l'équipe sont K.O. 💔

!!! fox_exercice_test "Test d'un combat contre un Pokémon sauvage 🎯"
    **Réaliser un combat entre votre équipe et un Pokémon sauvage:**
    1. Créer une équipe avec au moins 2 Pokémon (par exemple: Pikachu niveau 5 et Bulbizarre niveau 5)
    2. Créer un Pokémon sauvage (par exemple: Salamèche niveau 5)
    3. Lancer le combat et observer:
        - L'affichage des états de combat
        - Le système de changement de Pokémon en cas de K.O.
        - Le gain d'expérience en cas de victoire