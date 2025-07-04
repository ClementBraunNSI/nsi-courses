# Vérification d'un numéro de carte bancaire

Un certain nombre d'applications utilise la formule de Luhn pour vérifier si un identifiant ou un nombre est
utilisable dans certains contextes.  

Une des application notable de la vérification par la **formule de Luhn** est celle des numéros de cartes bancaires.  

## Explication de l'algorithme

L'algorithme se déroule en 3 étapes : 

- On lit de gauche à droite une chaîne de caractère.
- On multiplie un chiffre sur deux par 2.
  - Si celui-ci est supérieur à 10, on additionne les 2 chiffres composant le nombre.
- On additionne l'intégralité des chiffres après les calculs précédents.
- Si la somme de tous ses chiffres et divisible par 10, alors la carte bancaire est valide, sinon elle ne l'est pas.

## A réaliser

**Écrire une fonction `multiplier_additionner` qui prend en paramètre un nombre entier int et renvoie un entier.**
Cette fonction multiplie par deux le chiffre donné en paramètre et si celui-ci est supérieur à 10, additionne les
deux chiffres le composant (par exemple $\texttt{multiplierconcatener(8)} \rightarrow 8 \times 2 = 16 \rightarrow 1 + 6 = 7$).  
*Exemple d'utilisation :*

```python
    >>> multiplier_additionner(4)
    8
    >>> multiplier_additionner(8)
    7
```

**Compléter la fonction `multiplication_un_sur_deux` suivante qui prend en paramètre un numéro de carte bancaire sous forme de chaîne de caractère et renvoie une chaîne de caractère.**  
Cette fonction multiplie et concatène les chiffres du nombre de carte bancaire un sur deux.  Elle réutilisera la fonction précédente.
*Exemple d'utilisation*

```python
    >>> multiplication_un_sur_deux('3849')
    '3749'
    >>> multiplication_un_sur_deux('7642')
    '7344'
```

```python
    def multiplication_un_sur_deux(numero_cb:str)->str:
    '''
    entrée:
    numero_cb : numéro de carte bancaire
    sortie : numéro sous forme de chaîne de caractère après traitement
    Réalise le prétraitement avant la somme finale.
    '''
    res = ''
    for i in range(len(...)):
        if i ... 2 == ...:
            res += str(multiplier_additionner(numero_cb[...]))
        else:
            res += numero_cb[...]
    return res
```

**Écrire une fonction `somme_chiffre` qui prend en paramètre une chaîne de caractère représentant un numéro de carte bancaire et renvoie la somme de tous les nombres le composant.**  

*Exemple d'utilisation :*

```python
    >>> somme_chiffre("4539148803436467")
    75
    >>> somme_chiffre("3712348123980741")
    63
```

**Écrire une fonction `divisible_par_10` qui prend en paramètre un nombre entier et renvoie `True` s'il est divisible par 10, `False` sinon.**  

*Exemple d'utilisation:*

```python
    >>> divisible_par_10(75)
    False
    >>> divisible_par_10(60)
    True
``` 

**Écrire une fonction `verification_CB_Luhn` qui prend en paramètre un numéro de carte bancaire sous forme de chaîne de caractère et renvoie `True` s'il est valide, `False` sinon.**  
Cette fonction utilisera toutes les fonctions précédemment implémantées.

*Exemple d'utilisation:*

```python
    cb_1 = "4539148803236467"
    cb_2 = "3712348123980741"

    >>> numero_carte_bancaire_valide(cb_1)
    True
    >>> numero_carte_bancaire_valide(cb_2)
    False
```