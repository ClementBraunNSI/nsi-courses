# Interrogation : Bases de Python

## Exercice 1 : Questions de base de Python

1. **Quel est le résultat de l'opération suivante : 5//2**

!!! fox_correction_eval "Correction"
    L'opérateur a//b donne le quotient de la division de a par b.

2. **Quelle est la différence entre les opérateurs == et = ?**

!!! fox_correction_eval "Correction"
    `==` est utilisé pour la comparaison et `=` pour les assignation de variables.

3. **Quel opérateur permet de vérifier si deux variables sont différentes en Python?**
    `!=` permet de vérifier si 2 variables sont différentes.

## Exercice 2 : Étude de programme

On dispose du programme suivant : 

```python
    if x %2 == 0:
        resultat = True
    else: 
        resultat = False
    print(resultat)
```
1. **Quelle est la valeur de résultat si x vaut 12?**

!!! fox_correction_eval "Correction"
    resultat vaudra True car a % b donne le reste de la division de a par b et 12%2 = 0.

2. **Quelle est la valeur de résultat si x vaut 3?**

!!! fox_correction_eval "Correction"
    resultat vaudra False car 3%2 = 1.

3. **Que réalise ce programme ?**

!!! fox_correction_eval "Correction"
    Ce programme affiche False si x est impair, True sinon.

## Exercice 3 : Écriture de programmes simples

1. **Écrire un programme qui affiche dans le terminal la table de vérité d'une des fonctions booléennes suivantes : XOR ou AND ou OR**

!!! fox_correction_eval "Correction"

    ```python
        print("Table de vérité de la fonction booléenne OR" )
        print("A ", "B ", "S" )
        print("0 ", "0 ", "0" )
        print("0 ", "1 ", "1" )
        print("1 ", "0 ", "1" )
        print("1 ", "1 ", "1" )
    ```

2. **Écrire un programme qui demande l'âge d'un utilisateur et affiche dans le terminal : *Enfant* si l'âge est inférieur à 12 ans, *Adolescent* si l'âge est compris entre 12 et 17 ans ou *Adute* si l'âge est supérieur ou égal à 18.**

!!! fox_correction_eval "Correction"

    ```python
        age = int(input("Donnez votre âge"))
        if age >= 18:
            print("Adulte")
        elif age < 18 and age >= 12:
            print("Adolescent")
        elif age > 0:
            print("Enfant")
        else:
            print("L'âge ne peut pas être négatif")
    ```