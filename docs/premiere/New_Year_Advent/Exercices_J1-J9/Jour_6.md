# Jour 6 🦊🐼❄️🎉 : Le compte à rebours jusqu'à minuit

Pour le réveillon, Jean veut créer une ambiance festive en projetant un compte à rebours avant minuit. N'ayant pas de matériel d'affichage particulier, il décide de créer un affichage numérique en Python qui simule un afficheur 7 segments, comme ceux que l'on trouve sur les réveils digitaux.

## Informations nécessaires

Un afficheur 7 segments est composé de 7 segments (nommés de a à g) qui peuvent être allumés ou éteints pour former des chiffres :

```
         aaaa
        f    b
        f    b
         gggg
        e    c
        e    c
         dddd
```

Chaque segment peut être **activé** ou **désactivé** en fonction du chiffre à afficher. On indique qu'un segment activé est représenté par le booléen `True` et désactivé par le `False`. On utilise le dictionnaire suivant pour représenter l'état des segments pour chaque chiffre :

!!! fox_correction "Segments des chiffres"

    **Donner le dictionnaire qui associe chaque chiffre aux segments en précisant s'il est allumé ou éteint.**

    *Exemple:*
    ```python
        ... 
        0: {"a": True, "b": True, "c": True, "d": True, "e": True, "f": True, "g": False},
        1: {"a": False, "b": True, "c": True, "d": False, "e": False, "f": False, "g": False}
        ...
    ```

## Exercice principal

### 1. Représentation d'un chiffre

!!! fox_correction "Afficher un chiffre"

    **Écrire une fonction afficher_chiffre_bool qui prend en paramètre un chiffre et affiche sa représentation à l’écran.**

    Pour chaque segment :
    - Si le segment est activé (True), afficher *
    - Si le segment est désactivé (False), afficher un espace ( )
  
    *Exemple d’affichage pour le chiffre 5 :*
    ``` 
    ***
    *   
    *   
    ***
        *
        *
    ***
    ```

    *Indication : pseudo_code*

    ```
    fonction afficher_chiffre_bool(chiffre):
        initialiser une chaîne vide "representation"
        
        si le segment a est activé :
            ajouter " *** \n" à "representation"
        sinon :
            ajouter "     \n" à "representation"
        
        pour chaque ligne des segments f et b (haut gauche et haut droite) :
            si le segment f est activé :
                ajouter "*" à "representation"
            sinon :
                ajouter " " à "representation"
            
            ajouter "   " à "representation"
            
            si le segment b est activé :
                ajouter "*\n" à "representation"
            sinon :
                ajouter " \n" à "representation"
        
        si le segment g est activé :
            ajouter " *** \n" à "representation"
        sinon :
            ajouter "     \n" à "representation"
        
        pour chaque ligne des segments e et c (bas gauche et bas droite) :
            si le segment e est activé :
                ajouter "*" à "representation"
            sinon :
                ajouter " " à "representation"
            
            ajouter "   " à "representation"
            
            si le segment c est activé :
                ajouter "*\n" à "representation"
            sinon :
                ajouter " \n" à "representation"
        
        si le segment d est activé :
            ajouter " *** \n" à "representation"
        sinon :
            ajouter "     \n" à "representation"
        
        retourner "representation"
    ```

## 2. Compte à rebours

!!! fox_correction "Compte à rebours"

    **Écrire une fonction compte_a_rebours qui prend en paramètre un nombre de départ et affiche le décompte jusqu’à 0.**
    La fonction devra :
    - Utiliser afficher_chiffre_bool pour afficher chaque chiffre.
    - Attendre une seconde entre chaque chiffre.
    - Effacer l’écran avant d’afficher le chiffre suivant.

    *Indication : vous utiliserez le module time `import time` pour réaliser une pause de 1 seconde entre chaque affichage de chiffre. Vous utiliserez la fonction `time.sleep(nombre_de_secondes).`*

**Pour valider cet exercice, vous devrez rendre les fonctions construites ainsi qu’une capture d’écran du compte à rebours en action.**