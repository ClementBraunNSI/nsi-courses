# Interrogation : Boucles en python

**L'évaluation porte sur 2 exercices indépendants.**
**Les exercices sont notés sur 18 et la rigueur, rédaction et justifications sont notés sur 2 points.**

## Exercice 1 : Étude de programme : Suite de Fibonacci (6 points)

La suite de Fibonacci est une séquence de nombres où chaque terme est la somme des deux termes précédents. 

Elle commence généralement par 0 et 1, puis chaque terme suivant est calculé comme :

$F(n) = F(n-1) + F(n-2)$
$F(0) = 0\newline F(1) = 1\newline F(2) = 1 + 0 = 1\newline F(3) = 1 + 1 = 2\newline
\cdots$

On dispose du programme suivant :  

```python
x = 0
y = 1
compteur = 0

while compteur < 10 :
    print(x)
    y = x + y
    x = y - x
    compteur = compteur + 1
```

1) **Donner les valeurs de `a` et de `b` lors des 5 premières itérations de la boucle.**
2) **Que se passerait-il si l'on changeait la valeur de 10 à 20 ? Combien de termes seraient affichés?**
3) **À quoi sert la variable `compteur` pour la boucle et l'instruction `compteur = compteur + 1`**
4) **Comment pourrait-on modifier le programme pour demander à l'utilisateur le nombre de tours de boucles?**
   
Bonus: **Est-il possible d'écrire ce programme à l'aide d'une boucle `for` ? Si oui, l'écrire.**

<br>
<br>
<br>
<br>
<br>
<br>


## Exercice 2 : Écriture de programmes simples (12 points)

1) **Écrire un programme qui affiche la table de multiplication (multiples de 1 à 10 compris) d'un nombre demandé par l'utilisateur.**

2) **Écrire un programme qui affiche la somme des carrés de 0 à 100.**
*Rappel : l'opérateur `a**b` permet d'obtenir le nombre $a^b$.*
3) **Écrire un programme qui compte le nombre de consonne d'un mot ou d'une phrase demandé à l'utilisateur (stocké dans une chaîne de caractères).**
*Exemple : Pour l'entrée "Python" le programme affichera `4 consonnes`.*
4) **Écrire un programme qui affiche les caractères d'une chaîne de caractères demandée par l'utilisateur dans l'autre sens.**
*Exemple : Pour l'entrée "kayak" le programme affichera `kayak`.*