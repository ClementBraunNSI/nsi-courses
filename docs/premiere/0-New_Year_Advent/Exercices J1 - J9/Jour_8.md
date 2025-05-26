# Jour 8 🦊❄️🎉 : La playlist de la soirée

Les invités veulent créer une playlist collaborative pour la soirée. Chaque personne propose quelques chansons avec leur durée. Il faut analyser la playlist pour s'assurer qu'elle ne soit pas trop longue.

## Informations nécessaires

On considère :
- Une **chanson** est représentée par un **tuple** : (titre, artiste, durée_en_secondes, proposé_par)
- La **playlist** est une **liste** de chansons

```python
playlist = [
    ("I Want It That Way", "Backstreet Boys", 213, "Alice"),
    ("Shape of You", "Ed Sheeran", 233, "Paul"),
    ("Blinding Lights", "The Weeknd", 200, "Sophie"),
    ("Rolling in the Deep", "Adele", 228, "Lucas"),
    ("Uptown Funk", "Mark Ronson feat. Bruno Mars", 269, "Alice"),
    ("Levitating", "Dua Lipa", 203, "Sophie"),
    ("Someone Like You", "Adele", 285, "Lucas")]
```

## Exercice Principal

!!! fox_correction "Temps par personne"
    **Écrire une fonction `temps_par_personne` qui prend en paramètre une playlist et renvoie un dictionnaire avec le temps total de musique proposé par chaque personne.**

    *Un temps doit être affiché sous la forme "X minutes et Y secondes"*

    ```python
    >>> temps = temps_par_personne(playlist)
    >>> print(temps["Marie"])
    "4 minutes et 1 secondes"
    ```

!!! fox_correction "Durée totale"
    **Écrire une fonction `duree_totale` qui calcule la durée totale de la playlist.**

    *La durée doit être affichée sous la forme "X heures et Y minutes"*

    ```python
    >>> duree = duree_totale(playlist)
    >>> print(duree)
    "2 heures et 15 minutes"
    ```

!!! fox_correction "Vérification durée"
    **Écrire une fonction `verifier_duree` qui prend en paramètre une playlist et une durée maximale en minutes, et qui renvoie True si la playlist ne dépasse pas la durée maximale.**

    ```python
    >>> verifier_duree(playlist, 180)  # 3 heures
    True
    ```

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec la playlist fournie.**
