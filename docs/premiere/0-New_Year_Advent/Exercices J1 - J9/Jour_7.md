# Jour 7 🦊❄️🎉 : Composer le menu du Réveillon

Jean et ses amis ont décidé de faire appel à un traiteur pour le réveillon. Le traiteur leur a fourni une liste de plats possibles avec leurs prix. Cependant, certains invités ont des restrictions alimentaires (végétarien, sans gluten...) et Jean doit s'assurer que tout le monde pourra manger.

## Informations nécessaires

Le traiteur fournit un catalogue sous forme de dictionnaire :
```python
catalogue_traiteur = {
    "entrees": [
        {"nom": "Foie gras maison", "prix": 15, "restrictions": ["végétarien"]},
        {"nom": "Salade de quinoa", "prix": 8, "restrictions": []},
        {"nom": "Saumon fumé", "prix": 12, "restrictions": []},
        {"nom": "Soupe à l'oignon", "prix": 6, "restrictions": []},
        {"nom": "Terrine de légumes", "prix": 7, "restrictions": []}
    ],
    "plats": [
        {"nom": "Dinde aux marrons", "prix": 20, "restrictions": ["végétarien"]},
        {"nom": "Saumon en croûte", "prix": 18, "restrictions": []},
        {"nom": "Rôti de bœuf", "prix": 22, "restrictions": ["végétarien"]},
        {"nom": "Lasagnes végétariennes", "prix": 15, "restrictions": []},
        {"nom": "Gratin dauphinois", "prix": 12, "restrictions": []}
    ],
    "desserts": [
        {"nom": "Bûche au chocolat", "prix": 16, "restrictions": []},
        {"nom": "Crumble aux pommes", "prix": 10, "restrictions": []},
        {"nom": "Plateau de fromages", "prix": 14, "restrictions": ["végétarien"]},
        {"nom": "Salade de fruits", "prix": 8, "restrictions": []},
        {"nom": "Tarte aux poires", "prix": 11, "restrictions": []}
    ]
}

invites = [
    {"nom": "Marie", "restrictions": ["végétarien"]},
    {"nom": "Paul", "restrictions": []},
    {"nom": "Sophie", "restrictions": ["végétarien"]},
    {"nom": "Lucas", "restrictions": []},
    {"nom": "Emma", "restrictions": []}
]
```

## Exercice Principal

!!! fox_correction "Plats accessibles"

    **Écrire une fonction `plats_possibles` qui prend en paramètre le catalogue du traiteur et une restriction alimentaire, et renvoie un dictionnaire contenant les plats accessibles pour chaque type de plat (entrées, plats, desserts).**

    ```python
    >>> plats = plats_possibles(catalogue_traiteur, "végétarien")
    >>> print(plats["entrees"])  # affiche les entrées possibles pour un végétarien
    ["Salade de quinoa", "Soupe à l'oignon", "Terrine de légumes"]
    ```

!!! fox_correction "Composition d'un menu"

    **Écrire une fonction `composer_menu` qui prend en paramètre le catalogue du traiteur et renvoie un dictionnaire avec un menu complet (une entrée, un plat, un dessert) choisis aléatoirement.**

    *Indication : La fonction random.choice(sequence) du module random permet de faire des choix aléatoires dans des séquences. **Attention à ne pas oublier d'importer le module random.***

    ```python
    #Exemple de random
    >>>import random
    >>>mylist = ["apple", "banana", "cherry"]
    >>>print(random.choice(mylist))
    banana
    ```
    
    ```python
    >>> menu = composer_menu(catalogue_traiteur)
    >>> print(menu)
    {
        'entree': 'Saumon fumé',
        'plat': 'Dinde aux marrons',
        'dessert': 'Bûche au chocolat'
    }
    ```

!!! fox_correction "Vérification du menu"

    **Écrire une fonction `verifier_menu` qui prend en paramètre un menu et une liste d'invités, et renvoie la liste des invités qui ne peuvent pas manger ce menu à cause de leurs restrictions.**

    ```python
    >>> menu = composer_menu(catalogue_traiteur)
    >>> invites_probleme = verifier_menu(menu, invites)
    >>> print(invites_probleme)  # affiche les invités ayant des restrictions incompatibles
    ['Marie', 'Sophie']  # si le menu contient des plats non végétariens
    ```

!!! fox_correction "Menu pour tous"

    **Écrire une fonction `menu_pour_tous` qui compose un menu que tous les invités peuvent manger et affiche le coût total du menu.**

    *Cette fonction devra utiliser les fonctions précédentes pour :*
    - *Composer un menu aléatoire*
    - *Vérifier qu'il convient à tous les invités*
    - *Recommencer si ce n'est pas le cas*
    - *Calculer et afficher le coût total*

```python
>>> menu_final = menu_pour_tous(catalogue_traiteur, invites)
Menu sélectionné :
- Entrée : Salade de quinoa (8€)
- Plat : Lasagnes végétariennes (15€)
- Dessert : Bûche au chocolat (16€)
Coût total : 39€
```

**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi qu'un exemple de menu généré qui convient à tous les invités.**