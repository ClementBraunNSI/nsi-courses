# Sujet de TP : Jeu du Pendu

## Présentation du problème

Le jeu du pendu est un jeu de devinettes où le joueur essaie de découvrir un mot en proposant des lettres, avec un nombre limité d'erreurs possibles.

## Fonctions à implémenter

### 1. `lettre_presente`
**Écrire une fonction `lettre_presente` qui prend en paramètre un mot et une lettre et renvoie un booléen indiquant si la lettre est présente dans le mot.**

*Exemple d'utilisation :*
```python
>>> lettre_presente('python', 'p')
True
>>> lettre_presente('python', 'z')
False
```

### 2. `ajouter_lettre`
**Écrire une fonction `ajouter_lettre` qui prend en paramètre une chaine de caractère correspondant à celle en cours, une lettre et la solution et renvoie la chaine à compléter avec la lettre si présente.**

*Exemple d'utilisation :*
```python
>>> ajouter_lettre('_y____', 'p', 'python')
'py____'
>>> ajouter_lettre('_____', 'o', 'python')
'___o__'
```

### 3. `lettre_deja_presente`
**Écrire une fonction `lettre_deja_presente` qui prend en paramètre une chaine de caractères en cours et une lettre et renvoie un booléen indiquant si la lettre est déjà présente dans la chaine.**

*Exemple d'utilisation :*
```python
>>> lettre_deja_presente('py____', 'p')
True
>>> lettre_deja_presente('py____', 'o')
False
```

### 4. `lettre_deja_proposee`
**Écrire une fonction `lettre_deja_proposee` qui prend en paramètre une liste de lettres proposées et une lettre et renvoie un booléen indiquant si la lettre a déjà été proposée.**

*Exemple d'utilisation :*
```python
>>> lettre_deja_proposee(['a', 'e'], 'a')
True
>>> lettre_deja_proposee(['a', 'e'], 'p')
False
```

### 5. `pendu`
**Écrire une fonction `pendu` qui gère le déroulement complet du jeu du pendu.**

#### Pseudo-code de la fonction :
```
Fonction pendu():
    solution = mot choisi aléatoirement
    en_cours = chaîne de '_' de même longueur que solution
    nb_essais = 8
    lettres_proposees = liste vide

    Tant que (nb_essais > 0 ET solution != en_cours):
        Demander à l'utilisateur de saisir une lettre
        
        Tant que (lettre déjà présente dans en_cours 
                   OU lettre déjà proposée):
            Afficher un message d'erreur
            Redemander une lettre
        
        Si (lettre est dans solution):
            Mettre à jour en_cours avec la lettre
        Sinon:
            Afficher "La lettre n'est pas dans le mot"
            Ajouter la lettre aux lettres_proposees
            Décrémenter nb_essais
        
        Afficher l'état en_cours

    Si (solution == en_cours):
        Afficher "Bravo, vous avez gagné !"
    Sinon:
        Afficher "Perdu ! Le mot était", solution
```