# Révisions listes

## Niveau facile

1. **Écrire une fonction `double_elements` qui prend une liste d'entiers et renvoie une nouvelle liste où chaque élément est doublé.**  
   *Exemple :*  
   ```python
   double_elements([1, 2, 3]) # doit renvoyer [2, 4, 6]
   ```

2. **Écrire une fonction `carres` qui prend une liste d'entiers et renvoie une liste contenant le carré de chaque élément.**  
   *Exemple :*  
   ```python
   carres([1, 2, 3, 4]) # doit renvoyer [1, 4, 9, 16]
   ```

---

## Niveau intermédiaire 

1. **Écrire une fonction `elements_communs` qui prend deux listes et renvoie une nouvelle liste contenant les éléments communs aux deux listes (sans doublons).**  
   *Exemple :*  
   ```python
   elements_communs([1, 2, 3], [2, 3, 4]) # doit renvoyer [2, 3]
   ```

2. **Écrire une fonction `extraire_nombres` qui prend une liste mixte contenant des entiers, des chaînes de caractères et d'autres types, et renvoie une nouvelle liste contenant uniquement les nombres.**  
Indications :  

- La fonction `isinstance(variable, type)` renvoie `True` si la variable est bien du type demandé.
- Cette fonction devra rajouter dans une liste vide les éléments qui ne sont pas ceux égaux à cela non désiré.

   *Exemple :*  

   ```python
   extraire_nombres([1, "chat", 3, "chien", 4.5, 6]) # doit renvoyer [1, 3, 4.5, 6]
   ```

3. **Écrire une fonction `supprimer_occurrences` qui prend une liste et un élément, et renvoie une nouvelle liste en supprimant toutes les occurrences de cet élément.**  
Indication : Cette fonction devra rajouter dans une liste vide les éléments qui ne sont pas ceux égaux à cela non désiré.
   *Exemple :*  

   ```python
   supprimer_occurrences([1, 2, 3, 2, 4], 2) # doit renvoyer [1, 3, 4]
   ```

## Niveau Difficile

1. **Écrire une fonction `indices_element` qui prend une liste et un élément, et renvoie une liste des indices de toutes les occurrences de cet élément dans la liste.**  
   *Exemple :*  

   ```python
   indices_element([10, 20, 30, 20, 10], 20) # doit renvoyer [1, 3]
   ```

2. **Écrire une fonction `alternance_pairs_impairs` qui prend une liste d'entiers et vérifie si les éléments alternent entre pair et impair. Renvoie True si c'est le cas, sinon False.**  
   *Exemple :*

   ```python
   alternance_pairs_impairs([2, 3, 4, 5, 6]) # doit renvoyer True
   alternance_pairs_impairs([2, 2, 4, 5]) # doit renvoyer False
   ```
