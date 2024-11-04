# Fiche d'exercice : Les tuples et les listes

!!! danger Attention
      Tous les exercices, s'ils sont réalisés par des boucles `for`, doivent être faits avec une boucle sur les indices et une boucle sur les valeurs.
      ```python
         l = [1,2,3,4]
         # for par valeur:
         for elt in l:
            print(l)

         # for par indice (utilisation de len() qui permet d'avoir la taille d'une séquence):
         for i in range(len(l)):
            print(l[i])
      ```

## Exercices d'introduction

1. **Créer un tuple nommé  `mon_tuple` qui contient les éléments 1,2,3,4,5 et une liste `ma_liste` qui contient les éléments suivants 'a','b','c','d','e'.** 
**Les afficher dans le terminal.**

??? fox_correction "Correction"

   ```python
      mon_tuple = (1,2,3,4,5)
      ma_liste = ['a','b','c','d','e']
   ```

2. **Afficher dans le terminal le troisième élément de `mon_tuple`et le premier élément de `ma_liste`.**

3. **Modifier le deuxième élément de `ma_liste` par 'z'.  
Vérifier la modification en affichant la liste dans le terminal.**

4. **Ajouter l'élément 'f' dans `ma_liste`.
Supprimer le premier élément de `ma_liste`.  
Vérifier les modifications en affichant la liste dans le terminal.**

5. **Afficher dans le terminal tous les éléments de `mon_tuple` et `ma_liste` un à un à l'aide d'une boucle `for`.**

6. **Créer une liste `nombres` qui contient les chiffres allant de 1 à 9. (Proposer une version par compréhension).
Afficher dans le terminal les 5 premiers éléments de la liste en utilisant une boucle while.
Afficher les éléments du quatrième au huitième en utilisant une boucle for.  
Afficher les éléments de la liste `nombres` dans le sens inverse en utilisant une boucle while.**

---

## Niveau Facile

**Écrire une fonction `somme_elements` qui prend une liste de nombres en paramètre et renvoie la somme de tous les éléments.**  
*Exemple :*  
*somme_elements([1, 2, 3, 4]) doit renvoyer 10.*

---

**Écrire une fonction `compter_pairs` qui prend une liste d'entiers et renvoie le nombre d'éléments pairs dans cette liste.**  
*Exemple :*  
*compter_pairs([1, 2, 3, 4, 5, 6]) doit renvoyer 3.*

---

**Écrire une fonction `longueur_chaines` qui prend une liste de chaînes de caractères et renvoie une liste contenant la longueur de chaque chaîne.**  
*Exemple :*  
*longueur_chaines(["abc", "de", "fghi"]) doit renvoyer [3, 2, 4].*

---

**Écrire une fonction `produit_elements` qui prend une liste d'entiers et renvoie le produit de tous les éléments. Attention aux cas où la liste est vide.**  
*Exemple :*  
*produit_elements([2, 3, 4]) doit renvoyer 24.*

---

**Écrire une fonction `compter_occurrences` qui prend une liste et un élément, et renvoie le nombre de fois que cet élément apparaît dans la liste.**  
*Exemple :*  
*compter_occurrences([1, 2, 2, 3, 2], 2) doit renvoyer 3.*

---

==***Algorithme à connaître***==
**Écrire une fonction `presence`qui prend en paramètre une valeur et une liste et renvoie `True` si la valeur demandée est dans la liste, `False` sinon.**
*Exemple :*
*presence(3, [1, 2, 3, 4]) doit renvoyer True.*
*presence(5, [1, 2, 3, 4]) doit renvoyer False.*

---

**Écrire une fonction `moyenne` qui prend en paramètre une liste d'entiers et renvoie la moyenne de tous les nombres présents dans cette liste.**
*Exemple :*
*moyenne([1, 2, 3, 4, 5]) doit renvoyer 3.0.*

---

## Niveau Intermédiaire

**Écrire une fonction `filtrer_positifs` qui prend une liste de nombres et renvoie une nouvelle liste contenant uniquement les nombres positifs.**  
*Exemple :*  
*filtrer_positifs([-1, 0, 3, -7, 8]) doit renvoyer [3, 8].*

---

==***Algorithme à connaître***==
**Écrire une fonction `maximum` qui prend une liste d'entiers et renvoie l'entier maximum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 9.*

---

==***Algorithme à connaître***==
**Écrire une fonction `minimum` qui prend une liste d'entiers et renvoie l'entier minimum.**  
*Exemple :*  
*max_et_min([3, 1, 9, 2]) doit renvoyer 1.*

---

**Écrire une fonction `concatener_chaines` qui prend une liste de chaînes de caractères et renvoie une seule chaîne qui est la concaténation de toutes les chaînes de la liste.**  
*Exemple :*  
*concatener_chaines(["Bonjour", " ", "le", " ", "monde"]) doit renvoyer "Bonjour le monde".*

---

**Écrire une fonction `inverser_liste` qui prend une liste et renvoie une nouvelle liste avec les éléments dans l'ordre inverse.**  
*Exemple :*  
*inverser_liste([1, 2, 3]) doit renvoyer [3, 2, 1].*

---

**Écrire une fonction `valeurs_uniques` qui prend une liste et renvoie une nouvelle liste contenant les éléments sans doublons (dans l'ordre d'apparition).**  
*Exemple :*  
*valeurs_uniques([1, 2, 2, 3, 4, 4]) doit renvoyer [1, 2, 3, 4].*

---

**Écrire une fonction `moyenne_elements` qui prend une liste de nombres et renvoie la moyenne des éléments. Gérez le cas où la liste est vide.**  
*Exemple :*  
*moyenne_elements([5, 10, 15]) doit renvoyer 10.0.*

---

**Écrire une fonction `separer_pairs_impairs` qui prend une liste d'entiers et renvoie deux listes : une avec les éléments pairs et une autre avec les éléments impairs.**  
*Exemple :*  
*separer_pairs_impairs([1, 2, 3, 4, 5]) doit renvoyer ([2, 4], [1, 3, 5]).*

---

**Écrire une fonction `diviseurs` qui prend un entier en paramètre et renvoie la liste de ses diviseurs.**
*Exemple :*
*diviseurs(6) doit renvoyer [1, 2, 3, 6] (car 1, 2, 3 et 6 sont les diviseurs de 6).*
*diviseurs(10) doit renvoyer [1, 2, 5, 10] (car 1, 2, 5 et 10 sont les diviseurs de 10).*
---

**Écrire une fonction `est_croissante` qui prend une liste d’entiers en paramètre et renvoie True si les éléments de la liste sont dans l’ordre croissant, False sinon.**
*Exemple :*
*est_croissante([1, 2, 3, 4]) doit renvoyer True.*
*est_croissante([1, 3, 2, 4]) doit renvoyer False.*
---

**Écrire une fonction `echange` qui prend en paramètres une liste et deux indices, et échange les valeurs aux positions i et j dans la liste passée en paramètres.**
*Exemple :*
*echange([1, 2, 3, 4], 1, 2), cela doit modifier la liste pour donner [1, 3, 2, 4].*
*echange([5, 10, 15], 0, 2), cela doit modifier la liste pour donner [15, 10, 5].*

---

**Écrire une fonction `rangement_valeurs` qui prend en paramètre une liste et un élément, et renvoie 3 listes : une liste contenant les valeurs inférieures à l’élément, une liste avec l’élément si présent, et une liste avec les valeurs supérieures.**  
*Exemple :*  
```python
rangement_valeurs([1, 7, 4, 3, 6, 2, 8], 5)  # Renvoie: [1, 4, 3, 2], [], [7, 6, 8]
rangement_valeurs([1, 2, 4, 3, 6, 2, 8], 2)  # Renvoie: [1], [2, 2], [4, 3, 6, 8]
```

## Niveau Difficile

**Écrire une fonction `compter_voyelles` qui prend une liste de chaînes de caractères et renvoie le nombre total de voyelles présentes dans toutes les chaînes.**
*Exemple :*
*compter_voyelles([“chat”, “chien”]) doit renvoyer 3.*

---

**Écrire une fonction `valeurs_en_double` qui prend une liste et renvoie une nouvelle liste contenant uniquement les éléments qui apparaissent plus d’une fois (sans répétitions supplémentaires).**
*Exemple :*
*valeurs_en_double([1, 2, 2, 3, 4, 4, 5]) doit renvoyer [2, 4].*

---

**Écrire une fonction `indice_element` qui prend une liste et un élément, et renvoie l’indice de la première occurrence de cet élément dans la liste, ou -1 s’il n’est pas présent.**
*Exemple :*
*indice_element([10, 20, 30], 20) doit renvoyer 1.*

---

**Écrire une fonction `fusionner_sans_doublons` qui prend en paramètres deux listes et renvoie une nouvelle liste contenant tous les éléments des deux listes sans doublons.**
*Exemple :*
*fusionner_sans_doublons([1, 2, 3], [2, 3, 4]), cela doit renvoyer [1, 2, 3, 4].*
*fusionner_sans_doublons(['a', 'b'], ['b', 'c', 'a']), cela doit renvoyer ['a', 'b', 'c'].*