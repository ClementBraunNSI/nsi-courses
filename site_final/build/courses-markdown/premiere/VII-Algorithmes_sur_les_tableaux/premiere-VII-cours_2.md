# La Recherche Dichotomique

## Qu'est-ce que la recherche dichotomique ?

La dichotomie est une méthode de recherche qui permet de trouver rapidement un élément dans une liste triée en divisant récursivement l'espace de recherche par deux.  
C'est comme chercher quelqu'un dans un annuaire téléphonique : au lieu de lire page par page, vous ouvrez au milieu et décidez de continuer à gauche ou à droite.

## Principe Fondamental

Le principe de la recherche dichotomique repose sur trois étapes simples :

- Commencer au milieu de la liste
- Comparer l'élément recherché avec la valeur médiane
- Éliminer la moitié de la liste qui ne peut pas contenir l'élément

### Conditions Préalables

Pour utiliser la dichotomie, la liste dans laquelle on réalise la recherche **doit** être triée (par ordre croissant ou décroissant).

```
fonction recherche_dichotomique(liste, valeur):
    debut <- 0
    fin <- longueur(liste) - 1

    tant que debut <= fin:
        milieu <- (debut + fin) // 2
        si liste[milieu] == valeur:
            retourner milieu  # L'indice où se trouve la valeur
        sinon si liste[milieu] < valeur:
            debut <- milieu + 1
        sinon:
            fin <- milieu - 1

    retourner -1  # La valeur n'est pas dans la liste
```