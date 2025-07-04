# Epreuve pratique 4 : Tris et algorithmique

## Tri par insertion

**Écrire une fonction `echange_valeur` qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste** 
*Exemple:*  

```python
>>>liste = [1,5,2,4,0,8]
>>>echange_valeur(liste, 0, 4)
>>>print(liste)
[0,5,2,4,1,8]
```

---

**Écrire une fonction `insertion_zone_triee` qui prend en paramètre une liste, et un indice correspondant à celui de la valeur qui est juste après la zone triée. Cette fonction échange la valeur à l'indice avec celles qui sont avant elles pour trouver sa bonne place.**
*Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste.*
*Exemple:*  

```python
    >>>liste = [1,5,2,4,0,8]
    >>>insertion_zone_triee(liste,2)
    >>>print(liste)
    [1,2,5,4,0,8]
```

**Exprimer la complexité de l'algorithme d'insertion dans une zone donnée dans le pire des cas (le préciser).**
*Aucune rigueur mathématique n'est attendue.*

---

**Écrire une fonction `tri_insertion` qui prend en paramètre une liste et renvoie sa permutation triée.**  
*Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  
*Exemple:*  
```python
    >>>liste = [1,5,2,4,0,8]
    >>>print(tri_insertion(liste))
    [0,1,2,4,5,8]
```

**Exprimer la complexité de l'algorithme de tri par insertion dans le pire des cas.**