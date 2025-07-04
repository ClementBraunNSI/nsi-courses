# Pratiques de développement

## Objectif de cette leçon

Cette leçon vous servira dans toute votre expérience de développement.
Le but d'appliquer les bonnes pratiques permet d'avoir un code lisible, compréhensible par d'autres personnes et surtout de comprendre ses propres programmes.

Il existe diverses techniques pour rendre son code lisible et compréhensible et elles sont listées dans ce cours.
Ces bonnes pratiques **seront à appliquer toute l'année** lors des exercices, des évaluations et surtout lors des épreuves pratiques.

## Noms de variables

Le nommage des variable est très important lors de la création d'un programme.
Nommer une variable correctement permet de se rappeler lors de la conception d'un algorithme, à quoi elle correspond.
Il semble logique lors de la conception d'un algorithme portant sur des conversions de température de nommer ses variables de manière logique.

```python
# Mauvaise pratique
x = 34
y = 'La température est de ' + str(x)

# Bonne pratique
temperature = 34
affichage = 'La température est de ' + str(temperature)
```

Il existe plusieurs conventions de nommage mais il est plus simple d'utiliser la convention **snake case**.
Cette convention consiste à écrire des noms de variables explicites avec des _ (underscore ou tiret-du-bas) pour séparer les divers mots du nom.

Par exemple :

```python
affichage_temperature = 'La température est de '
```

## Spécification des fonctions

La spécification d'une fonction correspond à écrire un bloc de texte avant le bloc de code d'une fonction. Ce bloc de texte explique ce que sont les paramètres d'entrée, le résultat en sortie s'il y a et explique brièvement ce que la fonction fait.

Cela permet de mettre au propre ce que fait et d'avoir une idée de comment concevoir le programme.
La spécification permet aussi de rendre compréhensible le programme pour un tiers.
La spécification est vivement recommandée (pour ne pas dire évaluée) lors des épreuves pratiques.

Par exemple :

```python
def nombre_impair(nombre):
    '''
    params : 
        entrée : nombre, entier
        sortie : un booléen
    Renvoie True si le nombre est impair, False sinon.
    '''
    if nombre %2 == 0:
        return False
    else:
        return True
```

## Comprendre les erreurs

Les erreurs sont des événements courants qui surviennent lors de l'exécution d'un programme. Elles peuvent être causées par différents types de problèmes, tels que des erreurs de syntaxe, des erreurs d'exécution ou des erreurs logiques. Chaque type d'erreur correspond à une situation particulière qui peut être identifiée et résolue avec des techniques appropriées.

### 1. Erreurs de Syntaxe

Les erreurs de syntaxe surviennent lorsque le code ne respecte pas les règles de la syntaxe du langage Python. Ces erreurs sont détectées lors de la phase d'analyse (ou de parsing) du code avant son exécution. Elles empêchent généralement l'interpréteur Python de comprendre et d'exécuter le programme correctement.

**Exemples :**

- Oubli de deux-points ( : ), par exemple dans une déclaration de fonction ou dans une boucle.
- Utilisation incorrecte des guillemets (", ') autour des chaînes de caractères.
- Indentation incorrecte, notamment dans les blocs de code tels que les boucles et les fonctions.

### 2. Erreurs d'Exécution (Exceptions)

Les erreurs d'exécution, également appelées exceptions, surviennent lorsqu'une instruction ou une expression est correctement écrite mais ne peut pas être exécutée correctement à cause d'une situation imprévue pendant l'exécution du programme. Python génère alors une exception et interrompt l'exécution du programme si celle-ci n'est pas gérée.

**Exemples courants d'exceptions :**

- `ZeroDivisionError` : Tentative de division par zéro.
- `TypeError` : Opération appliquée à un type d'objet inapproprié.
- `IndexError` : Tentative d'accès à un index inexistant dans une liste ou un tuple.

### 3. Erreurs Logiques (Bugs)

Les erreurs logiques, souvent appelées bugs, sont des erreurs plus subtiles où le programme s'exécute sans générer d'exception mais produit un résultat incorrect. Ces erreurs sont souvent dues à une mauvaise compréhension du problème ou à une mauvaise implémentation de l'algorithme.

**Exemples :**

- Mauvaise gestion des conditions dans une boucle.
- Utilisation incorrecte des variables dans une fonction.
- Algorithmes incorrects qui produisent des résultats imprévus.

### 4. L'effet de bord

Un effet de bord est la modification d'une variable qui n'est pas uniquement réservée dans une fonction.
Ce type d'erreur peut causer des comportements inattendus (suppresion ou mise à None d'un élément qui sera réutilisé par la suite).
