# Jour 2 🎊🦊🎉 : Planification des activités

Maintenant que les invitations sont gérées, il faut planifier les activités de la soirée. Chaque activité a une durée et certaines ont des contraintes d'horaires.

Marc veut optimiser le planning pour que la soirée soit parfaitement organisée.

## Informations nécessaires

On considère :
- Une **activité** est représentée par un **dictionnaire** contenant :
  - nom (str)
  - duree_minutes (int)
  - heure_debut (str) au format "HH:MM"
  - obligatoire (bool)

```python
activites = [
    {"nom": "Accueil des invités", "duree_minutes": 30, "heure_debut": "19:00", "obligatoire": True},
    {"nom": "Apéritif", "duree_minutes": 60, "heure_debut": "19:30", "obligatoire": True},
    {"nom": "Dîner", "duree_minutes": 90, "heure_debut": "20:30", "obligatoire": True},
    {"nom": "Jeux de société", "duree_minutes": 45, "heure_debut": "22:00", "obligatoire": False},
    {"nom": "Karaoké", "duree_minutes": 60, "heure_debut": "22:45", "obligatoire": False},
    {"nom": "Compte à rebours", "duree_minutes": 15, "heure_debut": "23:45", "obligatoire": True},
    {"nom": "Feux d'artifice", "duree_minutes": 20, "heure_debut": "00:00", "obligatoire": True},
    {"nom": "Rangement", "duree_minutes": 30, "heure_debut": "00:20", "obligatoire": False}
]
```

## Exercice Principal

!!! fox_correction "Durée totale des activités obligatoires"
    **Écrire une fonction `duree_activites_obligatoires` qui prend en paramètre une liste d'activités et renvoie la durée totale en minutes des activités obligatoires.**

    *La fonction doit additionner les durées des activités dont le champ 'obligatoire' est True.*

!!! fox_correction "Convertir heure en minutes"
    **Écrire une fonction `heure_en_minutes` qui prend en paramètre une chaîne au format "HH:MM" et renvoie le nombre de minutes depuis minuit.**

    *Exemple : "19:30" doit renvoyer 19*60 + 30 = 1170 minutes.*

!!! fox_correction "Activité la plus longue"
    **Écrire une fonction `activite_plus_longue` qui prend en paramètre une liste d'activités et renvoie le nom de l'activité qui dure le plus longtemps.**

    *En cas d'égalité, renvoyer la première activité trouvée.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec la liste d'activités fournie.**