# Épreuve Pratique 3 

## Exercice 1 (10 points)  

Dans cet exercice les tableaux sont représentés par des listes Python (type list).  

Écrire en python deux fonctions :

- **`lancer` de paramètre n, un entier positif, qui renvoie un tableau de n entiers obtenus aléatoirement entre 1 et 6 (1 et 6 inclus)**

- **`paire_6` de paramètre tab, un tableau de n entiers compris entre 1 et 6 et qui renvoie un booléen égal à True si le nombre de 6 est supérieur ou égal à 2, False sinon.**

On pourra utiliser la fonction randint(a,b) du module random pour laquelle la documentation officielle est la suivante :

!!!abstract "Documentation"
    $random.randint(a,b) \newline \texttt{Renvoie un entier n tel que } a \le n \le b.$

*Exemple :*  

```python
    >>> lancer(10)
    [6, 3, 2, 6, 2, 6, 4, 2, 2, 3]
    >>> paire_6([1, 2, 3, 4, 5, 6])
    True
    >>> paire_6([1, 2, 3, 4, 5, 1])
    False
```

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Exercice 2 (10 points)
Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet.  

!!!abstract "Codage de César"
    Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, …, le X en A, le Y en B et le Z en C.  
    Les autres caractères (‘!’,’ ?’ …) ne sont pas codés.  

La fonction `position_alphabet` ci-dessous prend en paramètre un caractère lettre et renvoie la position de lettre dans la chaîne de caractères alphabet s’il s’y trouve.  

La fonction `cesar` prend en paramètre une chaîne de caractères message et un nombre entier decalage et renvoie le nouveau message codé avec le codage de César utilisant le décalage decalage.

```python
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César pour le decalage donné'''
    resultat = ''
    for ... in message:
        if 'A' <= c and c <= 'Z':
            indice = (...) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = ...
    return resultat
```

**Compléter la fonction cesar.**

```python
    Exemples :
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
```