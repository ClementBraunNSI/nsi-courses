
# 📚 Fonctions en Python

## 📖 Définitions

Une fonction en Python correspond à un certain bout de code qui est à réaliser plusieurs fois. Utiliser une fonction permet de réduire le nombre de lignes de code et de le modulariser.

Par exemple, on peut écrire une fonction qui réalise un certain type d'opération en fonction des éléments qu'on lui fournit pour fonctionner.

Un paramètre est une variable qui permet le bon fonctionnement d'un algorithme. Ce paramètre répond à un type précisé pour le fonctionnement de la fonction.

Par exemple, on peut écrire une fonction qui calcule la température en Fahrenheit en donnant comme paramètre la température en Celsius.

On connait la fonction mathématique pour passer de l'une à l'autre :
$Temperature_{Fahrenheit} = (Temperature_{Celsius} \times \frac{9}{5}) + 32$.

On peut l'écrire en Python pour pouvoir l'utiliser à plusieurs endroit sans forcément la réécrire à chaque fois. On utilisera le mot-clef `def`, qui signifie **define** (définir).

En clair, la structure est :

```python
def nom_de_fonction(variable_1 : type, variable_2 : type) -> type_renvoi :
    '''
    Explications de la fonctions, paramètres et renvoi
    '''
    Corps de la fonction
    Renvoi ou non de la fonction
```

```python
def celsius_vers_fahrenheit(temp_celsius : int) -> float:
    '''
    params:
        entrée : temp_celsius : entier, température en celsius
        sortie : temp_fahrenheit : entier, température en Fahrenheit
    Convertit une température exprimée en Celsius en température exprimée en Fahrenheit.
    '''
    temp_fahrenheit = (temp_celsius * (9/5)) + 32
    return temp_fahrenheit

def afficher_bonjour(prenom : str) -> None :
    '''
    params:
        entrée : prenom : chaine de caractère, un prénom
        sortie : X
    Affiche dans le terminal : Bonjour, prenom.
    '''
    print('Bonjour, ' + prenom)

print(celsius_vers_fahrenheit(19))
print(celsius_vers_fahrenheit(25))
afficher_bonjour('Eudes')
afficher_bonjour('Germaine')
```

On va décortiquer la fonction précédente pour définir ce qu'est une fonction.

- Le mot clef `def`, qui indique que l'on définit une fonction
- Une fonction est définie par son nom, ici `celsius_vers_fahrenheit`.
- Des paramètres, ici un unique `temp_celsius`
- Une spécification, un bloc de texte qui indique le type des paramètres d'entrée et sortie et ce que fait la fonction. (Cela répond aux bonnes pratiques de développement).
- Un bloc de code, ici une opération

On peut aussi retrouver un retour, ici la fonction renvoie un résultat pour effectuer des traitements. Pour l'exemple précédent, on souhaite l'afficher dans le terminal.

> **⚠️ Danger**
> Attention ! Une fonction peut ne pas retourner quelque chose. Si rien n'est précisé, elle renvoie par défaut None.
> Cela peut expliquer certains comportements d'affichage ou d'affectation de variables.
> Par exemple, réaliser `print(afficher_bonjour('Eudes'))` affichera None dans le terminal car elle ne renvoie rien.

## 📖 Variables locales et globales

En Python, il existe deux types de variables selon leur portée :

### Variables locales

Une variable locale est définie à l'intérieur d'une fonction et n'est accessible que dans cette fonction.

```python
def ma_fonction():
    variable_locale = 10  # Variable locale
    print(variable_locale)

ma_fonction()  # Affiche 10
# print(variable_locale)  # Erreur ! La variable n'existe pas ici
```

### Variables globales

Une variable globale est définie en dehors de toute fonction et est accessible partout dans le programme.

```python
variable_globale = 20  # Variable globale

def ma_fonction():
    print(variable_globale)  # Accès à la variable globale

ma_fonction()  # Affiche 20
print(variable_globale)  # Affiche 20
```

### Modification d'une variable globale

Pour modifier une variable globale dans une fonction, il faut utiliser le mot-clé `global` :

```python
compteur = 0  # Variable globale

def incrementer():
    global compteur  # Indique qu'on veut modifier la variable globale
    compteur += 1

print(compteur)  # Affiche 0
incrémenter()
print(compteur)  # Affiche 1
```

## 💡 Bonnes pratiques

### Documentation des fonctions

Il est important de documenter ses fonctions avec des docstrings :

```python
def calculer_aire_rectangle(longueur: float, largeur: float) -> float:
    """
    Calcule l'aire d'un rectangle.
    
    Args:
        longueur (float): La longueur du rectangle
        largeur (float): La largeur du rectangle
    
    Returns:
        float: L'aire du rectangle
    """
    return longueur * largeur
```

### Noms de fonctions explicites

Utilisez des noms de fonctions qui décrivent clairement ce qu'elles font :

```python
# Bon
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

# Moins bon
def calc(n):
    return sum(n) / len(n)
```

### Fonctions courtes et spécialisées

Préférez des fonctions courtes qui font une seule chose bien :

```python
def est_pair(nombre):
    """Vérifie si un nombre est pair."""
    return nombre % 2 == 0

def filtrer_nombres_pairs(liste_nombres):
    """Filtre les nombres pairs d'une liste."""
    return [n for n in liste_nombres if est_pair(n)]
```