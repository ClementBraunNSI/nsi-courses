# II - Fiche d'exercice : Les tuples et les listes

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

!!! fox_exercice "Somme d'éléments"
      **Écrire une fonction `somme_elements` qui prend une liste de nombres en paramètres et renvoie la somme de tous les éléments.**  
      *Exemple :*  
      *somme_elements([1, 2, 3, 4]) doit renvoyer 10.*

??? fox_correction "Correction"

    ```python
    def somme_elements(liste:list)->int:
      somme = 0
      for elt in liste:
         somme = somme + elt
      return somme
    ```

---

!!! fox_exercice "Compter les nombres pairs"
    **Écrire une fonction `compter_pairs` qui prend une liste d'entiers et renvoie le nombre d'éléments pairs dans cette liste.**  
    *Exemple :*
    ```python
      >>> compter_pairs([1,2,3,4,5])
      2
    ```

??? fox_correction "Correction"
    ```python
    def compter_pairs(liste:list)->int:
        nombre_pairs = 0
        for elt in liste:
            if elt % 2 == 0:
                nombre_pairs = nombre_pairs + 1
        return nombre_pairs
    ```
---

!!! fox_exercice "Longueur des chaînes"
    **Écrire une fonction `longueur_chaines` qui prend une liste de chaînes de caractères et renvoie une liste contenant la longueur de chaque chaîne.**  
    *Exemple :*
    ```python
    >>> longueur_chaines(["abc", "de", "fghi"])
    [3, 2, 4]
    ```

??? fox_correction "Correction"
    ```python
    def longueur_chaines(liste:list)->list:
        liste_longueurs = []
        for elt in liste:
            taille_elt = len(elt)
            liste_longueurs.append(taille_elt)
        return liste_longueurs
    ```

---

!!! fox_exercice "Produit d'éléments"
    **Écrire une fonction `produit_elements` qui prend une liste d'entiers et renvoie le produit de tous les éléments. Attention aux cas où la liste est vide.**  
    *Exemple :*
    ```python
    >>> produit_elements([2, 3, 4])
    24
    >>> produit_elements([])
    1
    ```

??? fox_correction "Correction"
    ```python
    def produit_elements(liste:list)->int:
        if not liste:  # si la liste est vide
            return 1
        produit = 1
        for elt in liste:
            produit = produit * elt
        return produit
    ```

---

!!! fox_exercice "Compter les occurrences"
    **Écrire une fonction `compter_occurrences` qui prend une liste et un élément, et renvoie le nombre de fois que cet élément apparaît dans la liste.**  
    *Exemple :*
    ```python
    >>> compter_occurrences([1, 2, 2, 3, 2], 2)
    3
    ```

??? fox_correction "Correction"
    ```python
    def compter_occurrences(liste:list, valeur: int)->int:
        occurrences = 0
        for elt in liste:
            if elt == valeur:
                occurrences = occurrences + 1
        return occurrences
    ```

---

!!! fox_exercice_important "Recherche d'un élément : ==Algorithme à connaître=="
    **Écrire une fonction `presence` qui prend en paramètre une valeur et une liste et renvoie `True` si la valeur demandée est dans la liste, `False` sinon.**  
    *Exemple :*
    ```python
    >>> presence(3, [1, 2, 3, 4])
    True
    >>> presence(5, [1, 2, 3, 4])
    False
    ```

??? fox_exercice_important_correction "Correction"
    ```python
    def presence(valeur: int, liste:list)->bool:
        present = False
        for elt in liste:
            if elt == valeur:
                present = True
        return present
    ```

---

!!! fox_exercice "Calcul de moyenne"
    **Écrire une fonction `moyenne` qui prend en paramètre une liste d'entiers et renvoie la moyenne de tous les nombres présents dans cette liste.**  
    *Exemple :*
    ```python
    >>> moyenne([1, 2, 3, 4, 5])
    3.0
    >>> moyenne([])
    0
    ```

??? fox_correction "Correction"
    ```python
    def moyenne(liste:list)->float:
        if not liste:  # si la liste est vide
            return 0
        taille_liste = len(liste)
        somme = 0
        for elt in liste:
            somme = somme + elt
        return somme / taille_liste
    ```
---

## Niveau Intermédiaire

!!! fox_exercice "Filtrer les nombres positifs"
    **Écrire une fonction `filtrer_positifs` qui prend une liste de nombres et renvoie une nouvelle liste contenant uniquement les nombres positifs.**  
    *Exemple :*
    ```python
    >>> filtrer_positifs([-1, 0, 3, -7, 8])
    [3, 8]
    ```

??? fox_correction "Correction"
    ```python
    def filtrer_positifs(liste:list)->list:
        positifs = []
        for elt in liste:
            if elt > 0:
                positifs.append(elt)
        return positifs
    ```

---

!!! fox_exercice_important "Maximum d'une liste : ==Algorithme à connaître=="
    **Écrire une fonction `maximum` qui prend une liste d'entiers prévue non vide et renvoie l'entier maximum.**  
    *Exemple :*
    ```python
    >>> maximum([3, 1, 9, 2])
    9
    ```

??? fox_exercice_important_correction "Correction"
    Comme on ne sait pas la composition de nos listes, pour éviter des soucis, on initialise notre maximum à la première valeur de la liste.
    Exemple, si l'on met 0 à maximum et que la liste est composée de négatifs, on ne trouvera jamais l'élément maximum.
    ```python
    def maximum(liste:list)->int:
        maxi = liste[0]
        for elt in liste:
            if elt > maxi:
                maxi = elt
        return maxi
    ```

--- 

!!! fox_exercice_important "Minimum d'une liste : ==Algorithme à connaître=="
    **Écrire une fonction `minimum` qui prend une liste d'entiers et renvoie l'entier minimum.**  
    *Exemple :*
    ```python
    >>> minimum([3, 1, 9, 2])
    1
    ```

??? fox_exercice_important_correction "Correction"
    Comme on ne sait pas la composition de nos listes, pour éviter des soucis, on initialise notre minimum à la première valeur de la liste.
    Exemple, si l'on met une valeur arbitraire et que la liste est composée de nombres supérieurs à celui-ci, on ne trouvera jamais l'élément minimum.
    ```python
    def minimum(liste:list)->int:
        mini = liste[0]
        for elt in liste:
            if elt < mini:
                mini = elt
        return mini
    ```

---

!!! fox_exercice "Concaténer des chaînes"
    **Écrire une fonction `concatener_chaines` qui prend une liste de chaînes de caractères et renvoie une seule chaîne qui est la concaténation de toutes les chaînes de la liste.**  
    *Exemple :*
    ```python
    >>> concatener_chaines(["Bonjour", " ", "le", " ", "monde"])
    "Bonjour le monde"
    ```

??? fox_correction "Correction"
    ```python
    def concatener_chaines(liste:list)->str:
        concatenation = ""
        for chaine in liste:
            concatenation = concatenation + chaine
        return concatenation
    ```

---

!!! fox_exercice "Inverser une liste"
    **Écrire une fonction `inverser_liste` qui prend une liste et renvoie une nouvelle liste avec les éléments dans l'ordre inverse.**  
    *Exemple :*
    ```python
    >>> inverser_liste([1, 2, 3])
    [3, 2, 1]
    ```

??? fox_correction "Correction"
    ```python
    def inverser_liste(liste:list)->list:
        liste_inversee = []
        for i in range(len(liste)-1, -1, -1):
            liste_inversee.append(liste[i])
        return liste_inversee
    ```

---

!!! fox_exercice "Valeurs uniques"
    **Écrire une fonction `valeurs_uniques` qui prend une liste et renvoie une nouvelle liste contenant les éléments sans doublons (dans l'ordre d'apparition).**  
    *Exemple :*
    ```python
    >>> valeurs_uniques([1, 2, 2, 3, 4, 4])
    [1, 2, 3, 4]
    ```

??? fox_correction "Correction"
    ```python
    def valeurs_uniques(liste:list)->list:
        liste_valeurs = []
        for elt in liste:
            if elt not in liste_valeurs:
                liste_valeurs.append(elt)
        return liste_valeurs
    ```

---

!!! fox_exercice "Séparer pairs et impairs"
    **Écrire une fonction `separer_pairs_impairs` qui prend une liste d'entiers et renvoie deux listes : une avec les éléments pairs et une autre avec les éléments impairs.**
    *Exemple :*  
    ```python
    >>> separer_pairs_impairs([1, 2, 3, 4, 5])
    ([2, 4], [1, 3, 5])
    ```

??? fox_correction "Correction"
    ```python
    def separer_pairs_impairs(liste:list)->tuple:
        pairs = []
        impairs = []
        for elt in liste:
            if elt % 2 == 0:
                pairs.append(elt)
            else:
                impairs.append(elt)
        return pairs, impairs
    ```

---

!!! fox_exercice "Recherche des diviseurs"
    **Écrire une fonction `diviseurs` qui prend un entier en paramètre et renvoie la liste de ses diviseurs.**
    *Exemple :*
    ```python
    >>> diviseurs(6)
    [1, 2, 3, 6]
    >>> diviseurs(10)
    [1, 2, 5, 10]
    ```
??? fox_correction "Correction"
    ```python
    def diviseurs(valeur:int)->list:
        diviseurs = []
        for i in range(1, valeur+1):  # On commence à 1 pour éviter la division par 0
            if valeur % i == 0:
                diviseurs.append(i)
        return diviseurs
    ```

!!! fox_exercice "Liste croissante"
    **Écrire une fonction `est_croissante` qui prend une liste d'entiers en paramètre et renvoie True si les éléments de la liste sont dans l'ordre croissant, False sinon.**
    *Exemple :*
    ```python
    >>> est_croissante([1, 2, 3, 4])
    True
    >>> est_croissante([1, 3, 2, 4])
    False
    ```
??? fox_correction "Correction"
    ```python
    def est_croissante(liste:list)->bool:
        i = 0
        while i < len(liste) - 1 and liste[i] <= liste[i+1]:
            i = i + 1
        return i == len(liste)-1
    ```

!!! fox_exercice "Échange de valeurs"
    **Écrire une fonction `echange` qui prend en paramètres une liste et deux indices, et échange les valeurs aux positions i et j dans la liste passée en paramètres.**
    *Exemple :*
    ```python
    >>> liste1 = [1, 2, 3, 4]
    >>> echange(liste1, 1, 2)
    >>> liste1
    [1, 3, 2, 4]
    >>> liste2 = [5, 10, 15]
    >>> echange(liste2, 0, 2)
    >>> liste2
    [15, 10, 5]
    ```
??? fox_correction "Correction"
    ```python
    #1ère solution : passer par une troisième valeur
    def echange(liste:list, i:int, j:int)->None:
        temp = liste[i]
        liste[i] = liste[j]
        liste[j] = temp
    ```
    ```python
    #2e solution : solution Python-esque
    def echange(liste:list, i:int, j:int)->None:
        liste[i], liste[j] = liste[j], liste[i]
    ```

!!! fox_exercice "Rangement de valeurs"
    **Écrire une fonction `rangement_valeurs` qui prend en paramètre une liste et un élément, et renvoie 3 listes : une liste contenant les valeurs inférieures à l'élément, une liste avec l'élément si présent, et une liste avec les valeurs supérieures.**
    *Exemple :*
    ```python
    >>> rangement_valeurs([1, 7, 4, 3, 6, 2, 8], 5)
    ([1, 4, 3, 2], [], [7, 6, 8])
    >>> rangement_valeurs([1, 2, 4, 3, 6, 2, 8], 2)
    ([1], [2, 2], [4, 3, 6, 8])
    ```
??? fox_correction "Correction"
    ```python
    def rangement_valeurs(liste:list, valeur:int)->tuple[list, list, list]:
        inferieures = []
        egales = []
        superieures = []
        for elt in liste:
            if elt > valeur:
                superieures.append(elt)
            elif elt == valeur:
                egales.append(elt)
            else:
                inferieures.append(elt)
        return inferieures, egales, superieures
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