# 📦 Fiche d'exercices : Les Tuples et les Listes en Python

!!! danger "⚠️ Attention - Méthodes de Boucles"
      Pour tous les exercices impliquant des boucles `for`, veuillez proposer deux solutions lorsque c'est pertinent :
      1. Une boucle sur les **valeurs** des éléments.
      2. Une boucle sur les **indices** des éléments.

      **Exemple :**
      ```python
      ma_liste = [10, 20, 30, 40]

      # Boucle sur les valeurs:
      print("Parcours par valeur:")
      for element in ma_liste:
          print(element)

      # Boucle sur les indices (utilisant len() pour la taille):
      print("\nParcours par indice:")
      for i in range(len(ma_liste)):
          print(f"Indice {i}: {ma_liste[i]}")
      ```

--- 

## 🌟 Niveau Facile (⭐️)

!!! fox_exercice "💻 Somme des éléments pairs ⭐"
    **Écrire une fonction `somme_elements_pairs` qui prend une liste de nombres en paramètre et renvoie la somme de tous les éléments pairs.**
    *Exemple :*
    ```python
    >>> somme_elements_pairs([1, 2, 3, 4, 5, 6])
    12 # (2 + 4 + 6)
    ```

??? fox_correction "✅ Correction"
    ```python
    def somme_elements_pairs(nombres: list) -> int:
        somme = 0
        # Parcours par valeur
        for nombre in nombres:
            if nombre % 2 == 0:
                somme += nombre
        return somme

    # Alternative avec parcours par indice
    # def somme_elements_pairs_indice(nombres: list) -> int:
    #     somme = 0
    #     for i in range(len(nombres)):
    #         if nombres[i] % 2 == 0:
    #             somme += nombres[i]
    #     return somme
    ```

---

!!! fox_exercice "💻 Trouver le dernier élément ⭐"
    **Écrire une fonction `dernier_element` qui prend un tuple en paramètre et renvoie son dernier élément. La fonction doit gérer le cas où le tuple est vide (renvoyer `None`).**
    *Exemple :*
    ```python
    >>> dernier_element((10, 20, 'a'))
    'a'
    >>> dernier_element(()) 
    None
    ```

??? fox_correction "✅ Correction"
    ```python
    def dernier_element(mon_tuple: tuple):
        if len(mon_tuple) > 0:
            return mon_tuple[-1] # L'indice -1 donne le dernier élément
        else:
            return None
    ```

---

!!! fox_exercice "💻 Concaténer deux tuples ⭐"
    **Écrire une fonction `concatener_tuples` qui prend deux tuples en paramètres et renvoie un nouveau tuple contenant tous les éléments des deux tuples.**
    *Exemple :*
    ```python
    >>> concatener_tuples((1, 2), (3, 4))
    (1, 2, 3, 4)
    ```

??? fox_correction "✅ Correction"
    ```python
    def concatener_tuples(tuple1: tuple, tuple2: tuple) -> tuple:
        return tuple1 + tuple2
    ```

---

!!! fox_exercice "💻 Vérifier si une liste est vide ⭐"
    **Écrire une fonction `est_vide` qui prend une liste en paramètre et renvoie `True` si la liste est vide, `False` sinon.**
    *Exemple :*
    ```python
    >>> est_vide([])
    True
    >>> est_vide([1, 2])
    False
    ```

??? fox_correction "✅ Correction"
    ```python
    def est_vide(ma_liste: list) -> bool:
        return len(ma_liste) == 0
    # Alternative : return not ma_liste
    ```

---

!!! fox_exercice "💻 Dupliquer les éléments d'une liste ⭐"
    **Écrire une fonction `dupliquer_elements` qui prend une liste et renvoie une nouvelle liste où chaque élément de la liste originale est dupliqué.**
    *Exemple :*
    ```python
    >>> dupliquer_elements([1, 'a', 3])
    [1, 1, 'a', 'a', 3, 3]
    ```

??? fox_correction "✅ Correction"
    ```python
    def dupliquer_elements(ma_liste: list) -> list:
        nouvelle_liste = []
        for element in ma_liste:
            nouvelle_liste.append(element)
            nouvelle_liste.append(element)
        return nouvelle_liste
    ```

---

!!! fox_exercice "💻 Compter éléments supérieurs à une valeur ⭐"
    **Écrire une fonction `compter_superieurs` qui prend une liste de nombres et un nombre `seuil`. Elle renvoie le nombre d'éléments dans la liste qui sont strictement supérieurs à `seuil`.**
    *Exemple :*
    ```python
    >>> compter_superieurs([10, 25, 5, 30, 15], 20)
    2 # (25, 30)
    ```

??? fox_correction "✅ Correction"
    ```python
    def compter_superieurs(nombres: list, seuil: int) -> int:
        compteur = 0
        for nombre in nombres:
            if nombre > seuil:
                compteur += 1
        return compteur
    ```

---

!!! fox_exercice "💻 Extraire les éléments d'indice pair ⭐"
    **Écrire une fonction `elements_indice_pair` qui prend une liste et renvoie une nouvelle liste contenant uniquement les éléments situés aux indices pairs (0, 2, 4, ...).**
    *Exemple :*
    ```python
    >>> elements_indice_pair(['a', 'b', 'c', 'd', 'e'])
    ['a', 'c', 'e']
    ```

??? fox_correction "✅ Correction"
    ```python
    def elements_indice_pair(ma_liste: list) -> list:
        resultat = []
        for i in range(len(ma_liste)):
            if i % 2 == 0:
                resultat.append(ma_liste[i])
        return resultat
    # Alternative plus concise avec le slicing:
    # def elements_indice_pair_slice(ma_liste: list) -> list:
    #     return ma_liste[::2]
    ```

--- 

## 🚀 Niveau Intermédiaire (⭐️⭐️)

!!! fox_exercice "💻 Inverser les mots d'une phrase ⭐️⭐️"
    **Écrire une fonction `inverser_mots_phrase` qui prend une liste de mots (chaînes de caractères) représentant une phrase et renvoie une nouvelle liste avec les mots dans l'ordre inverse.**
    *Exemple :*
    ```python
    >>> inverser_mots_phrase(['Bonjour', 'le', 'monde'])
    ['monde', 'le', 'Bonjour']
    ```

??? fox_correction "✅ Correction"
    ```python
    def inverser_mots_phrase(liste_mots: list) -> list:
        return liste_mots[::-1] # Slicing pour inverser la liste

    # Alternative avec boucle
    # def inverser_mots_phrase_boucle(liste_mots: list) -> list:
    #     nouvelle_liste = []
    #     for i in range(len(liste_mots) - 1, -1, -1):
    #         nouvelle_liste.append(liste_mots[i])
    #     return nouvelle_liste
    ```

---

!!! fox_exercice "💻 Éléments communs à deux listes (sans doublons) ⭐️⭐️"
    **Écrire une fonction `elements_communs` qui prend deux listes en paramètres et renvoie une nouvelle liste contenant les éléments communs aux deux listes, sans doublons, et dans l'ordre d'apparition de la première liste.**
    *Exemple :*
    ```python
    >>> elements_communs([1, 2, 3, 4, 2], [2, 4, 5, 6, 4])
    [2, 4]
    ```

??? fox_correction "✅ Correction"
    ```python
    def elements_communs(liste1: list, liste2: list) -> list:
        communs = []
        for element in liste1:
            if element in liste2 and element not in communs:
                communs.append(element)
        return communs
    ```

---

!!! fox_exercice "💻 Supprimer toutes les occurrences d'un élément ⭐️⭐️"
    **Écrire une fonction `supprimer_toutes_occurrences` qui prend une liste et un élément à supprimer. Elle modifie la liste en place en supprimant toutes les occurrences de cet élément.**
    *Exemple :*
    ```python
    >>> ma_liste = [1, 2, 3, 2, 4, 2]
    >>> supprimer_toutes_occurrences(ma_liste, 2)
    >>> print(ma_liste)
    [1, 3, 4]
    ```

??? fox_correction "✅ Correction"
    ```python
    def supprimer_toutes_occurrences(ma_liste: list, element_a_supprimer) -> None:
        # Il est plus sûr de construire une nouvelle liste si on ne doit pas modifier en place
        # ou d'itérer à l'envers ou avec une boucle while si on modifie en place.
        # Solution simple (crée une nouvelle liste implicitement avec filter ou compréhension):
        # ma_liste[:] = [x for x in ma_liste if x != element_a_supprimer]

        # Solution modifiant en place avec une boucle while (plus pédagogique ici)
        i = 0
        while i < len(ma_liste):
            if ma_liste[i] == element_a_supprimer:
                ma_liste.pop(i)
                # Ne pas incrémenter i, car l'élément suivant a pris la place de l'actuel
            else:
                i += 1
    ```

---

!!! fox_exercice "💻 Vérifier si une liste est un palindrome ⭐️⭐️"
    **Écrire une fonction `est_palindrome` qui prend une liste et renvoie `True` si la liste est un palindrome (se lit de la même manière de gauche à droite et de droite à gauche), `False` sinon.**
    *Exemple :*
    ```python
    >>> est_palindrome(['r', 'a', 'd', 'a', 'r'])
    True
    >>> est_palindrome([1, 2, 3, 2, 1])
    True
    >>> est_palindrome([1, 2, 3, 4, 5])
    False
    ```

??? fox_correction "✅ Correction"
    ```python
    def est_palindrome(ma_liste: list) -> bool:
        return ma_liste == ma_liste[::-1]

    # Alternative avec boucle
    # def est_palindrome_boucle(ma_liste: list) -> bool:
    #     longueur = len(ma_liste)
    #     for i in range(longueur // 2):
    #         if ma_liste[i] != ma_liste[longueur - 1 - i]:
    #             return False
    #     return True
    ```

---

!!! fox_exercice "💻 Rotation d'une liste vers la gauche ⭐️⭐️"
    **Écrire une fonction `rotation_gauche` qui prend une liste et un entier `k`. Elle renvoie une nouvelle liste résultant de `k` rotations des éléments vers la gauche.**
    *Exemple :*
    ```python
    >>> rotation_gauche([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    ```

??? fox_correction "✅ Correction"
    ```python
    def rotation_gauche(ma_liste: list, k: int) -> list:
        if not ma_liste:
            return []
        k = k % len(ma_liste) # Gérer les k > len(ma_liste)
        return ma_liste[k:] + ma_liste[:k]
    ```

---

!!! fox_exercice "💻 Aplatir une liste de listes ⭐️⭐️"
    **Écrire une fonction `aplatir_liste` qui prend une liste de listes (chaque sous-liste ne contient que des éléments simples) et renvoie une seule liste contenant tous les éléments des sous-listes.**
    *Exemple :*
    ```python
    >>> aplatir_liste([[1, 2], [3, 4, 5], [6]])
    [1, 2, 3, 4, 5, 6]
    ```

??? fox_correction "✅ Correction"
    ```python
    def aplatir_liste(liste_de_listes: list) -> list:
        aplatie = []
        for sous_liste in liste_de_listes:
            for element in sous_liste:
                aplatie.append(element)
        return aplatie
    # Alternative avec compréhension de liste imbriquée:
    # def aplatir_liste_comprehension(liste_de_listes: list) -> list:
    #     return [element for sous_liste in liste_de_listes for element in sous_liste]
    ```

---

!!! fox_exercice "💻 Fréquence de chaque élément ⭐️⭐️"
    **Écrire une fonction `frequence_elements` qui prend une liste et renvoie un dictionnaire où les clés sont les éléments de la liste et les valeurs sont leur fréquence (nombre d'occurrences).**
    *Exemple :*
    ```python
    >>> frequence_elements(['a', 'b', 'a', 'c', 'b', 'a'])
    {'a': 3, 'b': 2, 'c': 1}
    ```

??? fox_correction "✅ Correction"
    ```python
    def frequence_elements(ma_liste: list) -> dict:
        frequences = {}
        for element in ma_liste:
            if element in frequences:
                frequences[element] += 1
            else:
                frequences[element] = 1
        return frequences
    ```

--- 

## 🏆 Niveau Difficile (⭐️⭐️⭐️)

!!! fox_exercice "💻 Produit scalaire de deux listes (vecteurs) ⭐️⭐️⭐️"
    **Écrire une fonction `produit_scalaire` qui prend deux listes de nombres de même longueur et renvoie leur produit scalaire. Le produit scalaire de `A=[a1, a2, ..., an]` et `B=[b1, b2, ..., bn]` est `a1*b1 + a2*b2 + ... + an*bn`. Si les listes n'ont pas la même taille, renvoyer `None`.**
    *Exemple :*
    ```python
    >>> produit_scalaire([1, 2, 3], [4, 5, 6])
    32 # (1*4 + 2*5 + 3*6 = 4 + 10 + 18)
    >>> produit_scalaire([1,2], [3,4,5])
    None
    ```

??? fox_correction "✅ Correction"
    ```python
    def produit_scalaire(liste1: list, liste2: list):
        if len(liste1) != len(liste2):
            return None
        
        produit = 0
        for i in range(len(liste1)):
            produit += liste1[i] * liste2[i]
        return produit
    ```

---

!!! fox_exercice "💻 Générer toutes les sous-listes contiguës ⭐️⭐️⭐️"
    **Écrire une fonction `generer_sous_listes` qui prend une liste et renvoie une liste de toutes ses sous-listes contiguës (y compris la liste vide et la liste elle-même).**
    *Exemple :*
    ```python
    >>> generer_sous_listes([1, 2])
    [[], [1], [1, 2], [2]] # L'ordre peut varier
    ```

??? fox_correction "✅ Correction"
    ```python
    def generer_sous_listes(ma_liste: list) -> list:
        sous_listes = [[]]
        n = len(ma_liste)
        for i in range(n):
            for j in range(i, n):
                sous_listes.append(ma_liste[i:j+1])
        return sous_listes
    ```

---

!!! fox_exercice "💻 Plus longue sous-séquence croissante (simple) ⭐️⭐️⭐️"
    **Écrire une fonction `plus_longue_sous_sequence_croissante_simple` qui prend une liste de nombres et renvoie la longueur de la plus longue sous-séquence strictement croissante d'éléments contigus.**
    *Exemple :*
    ```python
    >>> plus_longue_sous_sequence_croissante_simple([1, 2, 1, 3, 4, 5, 2, 6])
    3 # pour [3, 4, 5]
    >>> plus_longue_sous_sequence_croissante_simple([5, 4, 3, 2, 1])
    1
    >>> plus_longue_sous_sequence_croissante_simple([])
    0
    ```

??? fox_correction "✅ Correction"
    ```python
    def plus_longue_sous_sequence_croissante_simple(nombres: list) -> int:
        if not nombres:
            return 0
        
        max_longueur = 1
        longueur_actuelle = 1
        
        for i in range(1, len(nombres)):
            if nombres[i] > nombres[i-1]:
                longueur_actuelle += 1
            else:
                longueur_actuelle = 1
            if longueur_actuelle > max_longueur:
                max_longueur = longueur_actuelle
        return max_longueur
    ```

---

!!! fox_exercice "💻 Déplacer zéros à la fin (ordre conservé) ⭐️⭐️⭐️"
    **Écrire une fonction `deplacer_zeros_fin` qui prend une liste de nombres et modifie la liste en place de sorte que tous les zéros soient déplacés à la fin, tout en conservant l'ordre relatif des éléments non nuls.**
    *Exemple :*
    ```python
    >>> ma_liste = [0, 1, 0, 3, 12, 0]
    >>> deplacer_zeros_fin(ma_liste)
    >>> print(ma_liste)
    [1, 3, 12, 0, 0, 0]
    ```

??? fox_correction "✅ Correction"
    ```python
    def deplacer_zeros_fin(nombres: list) -> None:
        # Compteur pour la position du prochain élément non nul
        index_non_nul = 0
        
        # Parcourir la liste. Si l'élément n'est pas zéro,
        # le placer à la position index_non_nul
        for i in range(len(nombres)):
            if nombres[i] != 0:
                nombres[index_non_nul] = nombres[i]
                index_non_nul += 1
        
        # Remplir le reste de la liste avec des zéros
        for i in range(index_non_nul, len(nombres)):
            nombres[i] = 0
    ```

---

!!! fox_exercice "💻 Intersection de plusieurs listes ⭐️⭐️⭐️"
    **Écrire une fonction `intersection_multiple` qui prend une liste de listes en paramètre. Elle doit renvoyer une nouvelle liste contenant uniquement les éléments présents dans *toutes* les sous-listes. L'ordre des éléments dans le résultat n'est pas important.**
    *Exemple :*
    ```python
    >>> intersection_multiple([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 8]])
    [3, 4] # ou [4, 3]
    >>> intersection_multiple([[10, 20], [20, 30], [40, 50]])
    []
    ```

??? fox_correction "✅ Correction"
    ```python
    def intersection_multiple(liste_de_listes: list) -> list:
        if not liste_de_listes:
            return []

        # Convertir la première liste en un ensemble pour commencer
        # Un ensemble (set) permet des opérations d'intersection efficaces
        resultat_set = set(liste_de_listes[0])

        # Itérer sur le reste des listes et mettre à jour l'intersection
        for i in range(1, len(liste_de_listes)):
            resultat_set.intersection_update(set(liste_de_listes[i]))
            # ou resultat_set = resultat_set.intersection(set(liste_de_listes[i]))

        return list(resultat_set)
    ```

---

!!! fox_exercice "💻 Partitionner en deux sous-listes de somme égale ⭐️⭐️⭐️"
    **Écrire une fonction `peut_partitionner` qui prend une liste de nombres entiers positifs et renvoie `True` si la liste peut être partitionnée en deux sous-listes (non nécessairement contiguës) dont la somme des éléments est égale, `False` sinon. (Ceci est une version simplifiée du problème de partition, on ne demande pas les sous-listes elles-mêmes).**
    *Indice : La somme totale des éléments doit être paire. Si c'est le cas, le problème revient à trouver une sous-liste dont la somme est égale à la moitié de la somme totale.*
    *Exemple :*
    ```python
    >>> peut_partitionner([10, 4, 6, 2]) # Somme totale 22. Cible = 11. (10,1) non, (4,6,2) non. (10,?) (4,?) (6,?) (2,?)
    # Sous-listes possibles: [10,2] (12) et [4,6] (10) -> False
    # [10,4] (14) et [6,2] (8) -> False
    # [10,6] (16) et [4,2] (6) -> False
    # [10] (10) et [4,6,2] (12) -> False
    # [4] (4) et [10,6,2] (18) -> False
    # [6] (6) et [10,4,2] (16) -> False
    # [2] (2) et [10,4,6] (20) -> False
    # Correction exemple: [1, 5, 11, 5] -> Somme 22, Cible 11. ([1,5,5] (11) et [11]) -> True
    >>> peut_partitionner([1, 5, 11, 5])
    True
    >>> peut_partitionner([1, 5, 3]) # Somme 9 -> False (car impaire)
    False
    ```

??? fox_correction "✅ Correction"
    ```python
    def peut_partitionner(nombres: list) -> bool:
        somme_totale = sum(nombres)

        # Si la somme totale est impaire, impossible de partitionner en deux sommes égales
        if somme_totale % 2 != 0:
            return False

        cible = somme_totale // 2

        # Utilisation d'un ensemble pour stocker les sommes de sous-ensembles possibles
        # On commence avec 0 (pour le sous-ensemble vide)
        sommes_possibles = {0}

        for nombre in nombres:
            nouvelles_sommes = set()
            for s in sommes_possibles:
                nouvelles_sommes.add(s + nombre)
            sommes_possibles.update(nouvelles_sommes)
            
            # Si on trouve la somme cible, on peut retourner True
            if cible in sommes_possibles:
                return True
        
        return False # Si on a parcouru tous les nombres sans trouver la cible
    ```