# Les fonctions en Python

## 1. Définir une fonction

```python
def nom_de_la_fonction(param1, param2):
    # Code à exécuter
    return resultat  # facultatif
```

- def : Mot-clé pour déclarer une fonction.
- nom_de_la_fonction : Nom choisi pour la fonction.
- param1, param2 : Paramètres d’entrée (facultatifs).
- return : Renvoie le résultat (facultatif).

## 2. Appeler une fonction

```python
    nom_de_la_fonction(arg1, arg2)
```

Remplacer arg1 et arg2 par les valeurs des arguments.

## 3. Exemple simple

```python
    def addition(a, b):
        return a + b

    resultat = addition(3, 5)  # Donne 8
```

## 4. Fonctions sans paramètres

```python
    def dire_bonjour():
```

## 5. Fonctions sans return

```python
    def afficher_carre(n):
        print(n ** 2)

    afficher_carre(4)  # Affiche 16
```

## 6. Retourner plusieurs valeurs

```python
    def operations(a, b):
    addition = a + b
        multiplication = a * b
        return addition, multiplication

    somme, produit = operations(3, 4)
    # somme = 7, produit = 12
```

## 7. Signature de fonction

```python
    def addition(a: int, b: int) -> int:
        return a + b
```

Indique que a et b sont des int et que la fonction renvoie un int.
