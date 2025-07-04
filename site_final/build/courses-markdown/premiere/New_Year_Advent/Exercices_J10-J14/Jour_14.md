# Jour 14 🐻🦊❄️🎉 : Messages secrets du Réveillon

Jean et ses invités décident de jouer à un jeu de messages secrets pendant la soirée. Ils ont découvert le chiffrement de César, une méthode historique qui consiste à décaler les lettres de l'alphabet. Ils veulent créer un petit système pour s'envoyer des messages codés pendant la soirée.

## Informations nécessaires

On considère :
- Un **message** est une chaîne de caractères
- Un **décalage** est un nombre entier
- L'alphabet utilisé est l'alphabet standard (26 lettres sans accents)
- Les espaces ne sont pas modifiés par le chiffrement
- Les messages sont toujours en minuscules

Pour vous aider à réaliser les décalages, voici l'alphabet avec la position de chaque lettre :
```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
# Position :  0123456789...
```

*Note importante sur le retour au début de l'alphabet :*
Quand on fait un décalage qui dépasse la fin de l'alphabet (après 'z'), on doit revenir au début (à 'a'). En Python, on peut utiliser l'opérateur modulo `%` pour cela :
- `nombre % 26` nous donne le reste de la division par 26
- Cela permet de "revenir à zéro" quand on dépasse 25

Exemple :
```python
# Si on décale 'y' de 3 positions :
# Position de 'y' = 24
# 24 + 3 = 27
# 27 % 26 = 1 donc on revient à la position 1 ('b')

# Si on décale 'a' de 27 positions :
# Position de 'a' = 0
# 0 + 27 = 27
# 27 % 26 = 1 donc lettre à la position 1 ('b')
```

## Exercice Principal

!!! fox_correction "Chiffrement de message"
    **Écrire une fonction `chiffrer_message` qui prend en paramètre un message et un décalage et renvoie le message chiffré.**
    
    *Indication : On peut utiliser la chaîne ALPHABET et la méthode `index()` pour trouver la position d'une lettre*

    ```python
    >>> message = "bonne annee"
    >>> chiffre = chiffrer_message(message, 3)
    >>> print(chiffre)
    "erqqh dqqhh"
    ```

!!! fox_correction "Déchiffrement de message"
    **Écrire une fonction `dechiffrer_message` qui prend en paramètre un message chiffré et le décalage utilisé, et renvoie le message d'origine.**

    ```python
    >>> message_chiffre = "erqqh dqqhh"
    >>> original = dechiffrer_message(message_chiffre, 3)
    >>> print(original)
    "bonne annee"
    ```

!!! fox_correction "Vérification de message"
    **Écrire une fonction `est_message_valide` qui vérifie si un message peut être correctement chiffré (uniquement des lettres minuscules non accentuées et des espaces).**

    ```python
    >>> est_message_valide("bonne annee")
    True
    >>> est_message_valide("Bonne Année !")
    False
    ```

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec des messages de voeux pour la nouvelle année.**
