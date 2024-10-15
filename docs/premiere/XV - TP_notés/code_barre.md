# Vérification d'un Code-barres

Les codes-barres sont omniprésents dans notre quotidien, utilisés pour identifier des produits dans les magasins, les bibliothèques, et bien d'autres domaines.

## Exemple du calcul de la clé de contrôle

Nous allons étudier  le **Code EAN-13** : **9782091726649**

*Rappel : une valeur à la première position est d'indice 0, une valeur à la seconde position est d'indice 1 $\cdots$*

## Explication de l'algorithme  

- On ne travaille que sur les 12 premiers chiffres.
- On lit le numéro de gauche à droite
  - On réalise la somme de tous les chiffres situés à des positions impaires.  
  *Pour l'exemple : $9+8+0+1+2+6 = 26$.*
  - On réalise la somme de tous les chiffres situés à des positions paires.  
  *Pour l'exemple : $7+2+9+7+6+4 = 35$.*
- On multiplie la somme des chiffres de positions paires par 3.
*Pour l'exemple : $35 \times 3 = 105$.*
- On additionne la somme multipliée par 3 avec la somme des chiffres à indice impairs.
*Pour l'exemple : $105 + 26 = 131$.*
- On calcule le reste de la division euclidienne par 10 de ce nombre.
*Pour l'exemple : $131%10 = 1$.*
- On retire le reste à 10 pour obtenir la valeur qui servira de vérification.
*Pour l'exemple : $10-1 = 9$.*
- Si cette valeur de vérification est égale au dernier chiffre du numéro du code barre. : Le numéro d'EAN est valide, sinon il ne l'est pas.
*Pour l'exemple : la clef de contrôle calculée est 9, le dernier chiffre du code barre est bien 9, il est donc bien valide.*

## À réaliser

**Écrire une fonction `verifier_longueur` qui prend en paramètre une chaîne de caractères et renvoie `True` si le code-barres contient exactement 13 chiffres, `False` sinon.**.
*Exemple d'utilisation :*

```python
   >>> verifier_longueur('9782091726649')
   True
   >>> verifier_longueur('978209172664')
   False
```

**Écrire une fonction `mettre_bonne_longueur` qui prend une chaîne de caractères et renvoie une chaîne de caractères contenant les 12 premiers caractères.**

*Exemple d'utilisation:*

```python
   >>> mettre_bonne_longueur("9782091726649")
   '978209172664'
   >>> mettre_bonne_longueur("bonjourjesuisletexte")
   "bonjourjesui"
```

**Écrire une fonction `somme_positions_impairs` qui prend en paramètre une chaîne de caractères représentant un code barre et renvoie un entier correspondant à la somme des chiffres de positions impaires.**
*Exemple d'utilisation:*

```python
   >>> somme_positions_impairs('9782091726649')
   26
```

**Écrire une fonction `somme_positions_pairs` qui prend en paramètre une chaîne de caractère représentant un code barre et renvoie un entier correspondant à la somme des chiffres de positions paires.**
*Exemple d'utilisation:*

```python
   >>> somme_positions_pairs('9782091726649')
   35

```

**Écrire une fonction `multiplier_par_trois` qui prend en paramètre un entier et renvoie son produit avec trois.**
*Exemple d'utilisation:*

```python
   >>>  multiplier_par_trois(35)
   105
   >>> multiplier_par_trois(15)
   45
```

**Écrire une fonction `traitement` qui prend en paramètre deux entiers et renvoie un entier.**
Cette fonction va :

- Réaliser la somme de ces deux entiers.
- Calculer le reste de la division par 10 de cette somme.
- Soustraire le reste de la division à 10.

*Exemple d'utilisation*

```python
   >>> traitement(26,105)
      9
```

**Écrire une fonction `validation_code_barre` qui prend en paramètre un code barre représenté par une chaîne de caractère et renverra `True` s'il est valide, `False` sinon.**
Cette fonction utilisera toutes les fonctions précédentes pour réaliser la vérification notée au début de ce TP.

*Exemple d'utilisation*

```python
   >>> validation_code_barre("9782091726649")
   True
   >>> validation_code_barre("4006381333936")
   False
```
