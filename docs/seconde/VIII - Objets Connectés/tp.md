# Travail Pratique : Cartes Micro:bit

## Définitions

Les cartes Micro:bit sont des cartes électroniques qui sont une introduction à l'informatique embarquée et à la réalisation d'affichages, sons etc... à l'aide de boutons et de leds.

Une carte Micro:bit est consituée de plusieurs éléments :

|Présentation de la carte|Carte avec une tête renard minimaliste en pixel art|
|-|-|
|![carte](microbit.png)|![fox](fox_microbit.png)|

## Documentation des fonctionnalités

| Fonctionnalité | Explication | Exemple |
|----------------|-------------|----------|
| Affichage LED | Affiche des motifs sur la grille de LED 5x5 | `display.show(Image.HEART)` |
| Messages défilants | Fait défiler du texte sur l'écran LED | `display.scroll("Bonjour")` |
| Boutons | Deux boutons (A et B) pour l'interaction | `button_a.is_pressed()` |
| Pause | Met en pause le programme | `sleep(1000)` # pause 1 seconde |
| Images prédéfinies | Motifs LED préenregistrés | `Image.HAPPY`, `Image.SAD`, `Image.HEART` |
| Boucle infinie | Répète le code en continu | `while True:` |

## Pour commencer

Pour programmer la carte, on utilise le site [Site de Micro:Bit](https://python.microbit.org/v/3/reference).

![site](editor.png)

Le bloc orange correspond à la bibliothèque des blocs pouvant être utilisés.
Le bloc marron est l'éditeur de code.
Le bloc vert permet d'envoyer le programme à la carte.

Voici un exemple simple pour commencer :

```python
# Importer les paquets necessaires
from microbit import *

# Boucle infinie
while True:
    # Affiche un coeur
    display.show(Image.HEART)
    # Attend 1 seconde
    sleep(1000)
    # Affiche un message
    display.scroll('Hello')
```

## Exercices

### 🌟 Exercice 1 : Affichage simple
**Difficulté : ⭐**

Affichez le motif d'un visage souriant (`Image.HAPPY`) sur l'écran LED.

💡 **Indice :** Utilisez `display.show()` avec `Image.HAPPY`

### 🎨 Exercice 2 : Message défilant
**Difficulté : ⭐**

Faites défiler votre prénom sur l'écran LED.

💡 **Indice :** Utilisez `display.scroll("votre_prenom")`

### 🎮 Exercice 3 : Premier bouton
**Difficulté : ⭐⭐**

Affichez un cœur quand on appuie sur le bouton A.

```python
# Structure de base
from microbit import *

while True:
    if button_a.is_pressed():
        # Votre code ici
```

### 🎨 Exercice 4 : Alternance simple
**Difficulté : ⭐⭐**

Alternez entre deux images toutes les secondes (par exemple un cœur et un carré).

💡 **Indice :** 
- Utilisez `Image.HEART` et `Image.SQUARE`
- N'oubliez pas `sleep(1000)` entre les images

### 🦊 Exercice 5 : Tête de Renard
**Difficulté : ⭐⭐⭐**

Recréez la tête de renard montrée dans l'introduction en utilisant le système de pixel art de la Micro:bit.

💡 **Indice :**

- Regardez attentivement l'image du renard dans l'introduction
- Utilisez différents niveaux de luminosité (0-9) pour créer les détails
- Commencez par dessiner votre motif sur papier en grille 5x5

```python
# Structure de base pour la tête de renard
display.show(Image("00000:"  # Ligne 1
                "00000:"  # Ligne 2
                "00000:"  # Ligne 3
                "00000:"  # Ligne 4
                "00000"))  # Ligne 5
# Remplacez les 0 par les bonnes valeurs de luminosité
```

### 🌟 Exercice 6 : Message au bouton
**Difficulté : ⭐⭐**

Affichez "A" quand on appuie sur le bouton A, et "B" quand on appuie sur le bouton B.

💡 **Indice :** 
- Utilisez `button_a.is_pressed()` et `button_b.is_pressed()`
- Utilisez `display.scroll()`

### Exercice Bonus : Images personnalisées
**Difficulté : ⭐⭐⭐**

Créez et affichez votre propre motif sur l'écran LED.

```python
# Exemple de création d'image
mon_image = Image("09090:" # Ligne 1
                 "00000:" # Ligne 2
                 "90009:" # Ligne 3
                 "09990:" # Ligne 4
                 "00000") # Ligne 5
# Les chiffres représentent la luminosité (0-9)
```



💡 **Indice :** 
- Dessinez d'abord votre motif sur papier
- Utilisez des chiffres de 0 (éteint) à 9 (luminosité maximale)