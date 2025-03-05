# Épreuve Pratique 4 : Tris et algorithmique

## 

## Tri par selection du minimum

**Écrire une fonction `echange_valeur` qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste**  
*Exemple:*  

```python
>>>liste = [1,5,2,4,0,8]
>>>echange_valeur(liste, 0, 4)
>>>print(liste)
[0,5,2,4,1,8]
```

--- 

**Écrire une fonction `indice_minimum_tranche` qui prend en paramètres une liste, un indice de début et qui renvoie l'indice de la valeur la plus petite dans la tranche donnée.**  
*Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de* ***Out Of Range****.*  
*Exemple:*  

```python
>>>liste = [1,5,2,4,0,8]
>>> indice_minimum_tranche(liste,1)
4
```

**Exprimer la complexité de la fonction indice_minimum_tranche dans le pire des cas.**
*Aucune rigueur mathématique n'est attendue.*

--- 

**Écrire une fonction `tri_selection_minimum` qui prend en paramètre une liste et renvoie sa permutation triée.**  
*Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  
*Exemple:*  
```python
>>>liste = [1,5,2,4,0,8]
>>>print(tri_selection_minimum(liste))
[0,1,2,4,5,8]
```

**Exprimer la complexité de l'algorithme de tri par selection du minimum dans le pire des cas.**