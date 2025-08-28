# 🎮 Simulateur BBC Micro:bit V2

## 📋 Description

Cette application Python simule le fonctionnement d'une carte BBC Micro:bit V2 avec un mini IDE intégré. Elle permet aux élèves d'apprendre la programmation d'objets connectés de manière interactive et visuelle.

## 🚀 Installation et lancement

### Prérequis
- Python 3.6 ou plus récent
- Tkinter (généralement inclus avec Python)

### Lancement
```bash
python microbit_simulator.py
```

## 🎯 Fonctionnalités

### Simulation de la Micro:bit
- **Matrice LED 5x5** : Affichage visuel des LEDs
- **Boutons A et B** : Cliquables avec la souris
- **Capteurs simulés** :
  - Accéléromètre (valeurs aléatoires)
  - Capteur de température
  - Capteur de luminosité
- **Affichage en temps réel** des valeurs des capteurs

### Mini IDE
- **Onglet Blocs de code** : Interface par blocs pour faciliter l'apprentissage
- **Onglet Code Python** : Éditeur de texte pour le code Python
- **Exemples intégrés** : Code d'exemple pour commencer
- **Exécution en temps réel** : Voir les résultats immédiatement

## 📚 Utilisation pédagogique

### Pour les élèves

1. **Commencer avec les blocs** :
   - Utilisez l'onglet "Blocs de code"
   - Cliquez sur les boutons pour ajouter du code
   - Catégories disponibles : Affichage, Boutons, Capteurs, Contrôle, Images

2. **Passer au code Python** :
   - Basculez vers l'onglet "Code Python"
   - Modifiez le code généré
   - Ajoutez vos propres fonctionnalités

3. **Tester votre code** :
   - Cliquez sur "▶ Exécuter" pour lancer votre programme
   - Interagissez avec les boutons A et B
   - Observez les LEDs s'allumer
   - Utilisez "⏹ Arrêter" pour stopper l'exécution
   - "🔄 Reset" pour remettre à zéro

### Exemples d'activités

#### 1. Premier programme - Cœur clignotant
```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.clear()
    sleep(500)
```

#### 2. Compteur avec boutons
```python
from microbit import *

compteur = 0

while True:
    if button_a.was_pressed():
        compteur += 1
        display.scroll(str(compteur))
    if button_b.was_pressed():
        compteur -= 1
        display.scroll(str(compteur))
    sleep(100)
```

#### 3. Thermomètre
```python
from microbit import *

while True:
    temp = temperature()
    display.scroll(str(temp) + 'C')
    sleep(2000)
```

## 🎨 Interface utilisateur

### Zone de simulation (gauche)
- Représentation visuelle de la Micro:bit
- Matrice LED interactive
- Boutons A et B cliquables
- Panneau d'informations des capteurs
- Boutons de contrôle (Exécuter, Arrêter, Reset)

### Mini IDE (droite)
- **Onglet Blocs** : Catégories de blocs de code prêts à utiliser
- **Onglet Code** : Éditeur de texte avec exemples

## 🔧 API Simulée

### Affichage
- `display.show(Image.HEART)` : Afficher une image
- `display.scroll('Hello')` : Faire défiler du texte
- `display.set_pixel(x, y, brightness)` : Allumer/éteindre une LED
- `display.clear()` : Éteindre toutes les LEDs
- `display.read_light_level()` : Lire le niveau de luminosité

### Boutons
- `button_a.is_pressed()` : Vérifier si le bouton A est pressé
- `button_b.is_pressed()` : Vérifier si le bouton B est pressé
- `button_a.was_pressed()` : Vérifier si le bouton A a été pressé
- `button_a.wait_for_press()` : Attendre que le bouton A soit pressé

### Capteurs
- `temperature()` : Lire la température
- `accelerometer.get_x()` : Lire l'accélération X
- `accelerometer.get_y()` : Lire l'accélération Y
- `accelerometer.get_z()` : Lire l'accélération Z

### Images prédéfinies
- `Image.HEART` : Cœur
- `Image.HAPPY` : Visage heureux
- `Image.SAD` : Visage triste
- `Image.ARROW_N` : Flèche vers le haut

### Contrôle
- `sleep(ms)` : Pause en millisecondes

## 🎓 Objectifs pédagogiques

- **Découverte de la programmation** : Interface intuitive avec blocs de code
- **Transition vers Python** : Passage progressif des blocs au code textuel
- **Compréhension des objets connectés** : Capteurs, actionneurs, programmation
- **Logique algorithmique** : Boucles, conditions, variables
- **Interaction homme-machine** : Boutons, affichage, capteurs

## 🔍 Conseils d'utilisation

### Pour les enseignants
- Commencez par des exemples simples (cœur clignotant)
- Encouragez l'expérimentation avec les blocs
- Progressez vers la modification du code Python
- Utilisez les capteurs pour des projets plus avancés

### Pour les élèves
- N'hésitez pas à expérimenter
- Utilisez les exemples comme base
- Combinez différents blocs pour créer vos programmes
- Testez régulièrement votre code

## 🐛 Dépannage

### Problèmes courants
- **Le programme ne s'arrête pas** : Utilisez le bouton "⏹ Arrêter"
- **Erreur de syntaxe** : Vérifiez l'indentation et la syntaxe Python
- **LEDs qui ne s'allument pas** : Vérifiez les coordonnées (0-4 pour x et y)

### Messages d'erreur
- Les erreurs Python sont affichées dans une boîte de dialogue
- Lisez attentivement le message pour identifier le problème

## 📝 Licence

Cette application est destinée à un usage éducatif. Elle simule le comportement d'une BBC Micro:bit à des fins pédagogiques.

---

**Bon apprentissage ! 🎉**