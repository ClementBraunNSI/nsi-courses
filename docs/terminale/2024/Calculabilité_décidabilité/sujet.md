# Calculabilité & Décidabilité

## Introduction : Un programme est une donnée

Une donnée est une valeur exploitable dans un programme.
Cette valeur peut être modifiée lors de l'appel de celui-ci.

Cependant, un programme _parent_ peut aussi prendre un autre programme comme donnée.

```python
def cercle(n):
    return 2 * math.pi * n

def carre(n):
    return 4 * n

def triangle_equilateral(n):
    return 3 * n

def pentagone_regulier(n):
    return 5 * n

def perimetre(forme,n):
    return forme(n)

liste_formes = [cercle,carre,triangle_equilateral,pentagone_regulier]

for forme in liste_formes:
    print(perimetre(forme,5))
```

Utiliser des fonctions comme données peut permettre de modulariser son programme et de l'adapter pour des modifications futures (ajout de fonctionnalités, modification de fonctions déjà existantes...).

## Définitions

Un algorithme est une suite **finie** d'instructions qui résout un problème.

Un problème en informatique est une traduction mathématique d'une question que l'on peut se poser.

On dit qu'un problème est calculable si ce problème peut être modélisé par un algorithme.
On appelle **théorie de la calculabilité** l'étude de la calculabilité d'un problème, c'est-à-dire, si un problème est calculable ou non.

On dit qu'un problème est décidable si ce problème peut être répondu par oui ou non, True ou False.
On appelle **théorie de la décidabilité** l'étude de la décidabilité d'un problème, c'est-à-dire, si un problème est décidable ou non.

La calculabilité et la décidabilité sont des fondements de l'informatique théorique.

L'origine de l'interêt de ces théories remonte au XVIIème siècle quand Gottfried Wilhelm Leibniz, un érudit, se demandait s'il était possible qu'une machine puisse résoudre tous les problèmes (mathématiques, de décision, de calcul...).

Cette reflexion a été remise au premier plan en 1928 par les mathématiciens allemands David Hilbert et Wilhelm Ackermann en posant le _Entscheidungproblem_ ou _problème de décision_ : _"Peut on toujours décider de façon mécanique si un énoncé est vrai?"_

[Vidéo introduction](https://www.youtube.com/watch?v=Zci9m08HQws&pp=ygUYYXJ0ZSBFbnRzY2hlaWR1bmdwcm9ibGVt)

## L'étude de l'Entscheidungproblem

David Hilbert cherchait à montrer que le _problème de la décision_ pouvait être décidé. Il n'a cependant jamais pu le prouver donc a supposé que c'était vrai.
Si cela était vrai, on aurait eu une révolution dans le monde de l'informatique car on aurait une preuve qu'un programme peut indiquer que d'autres sont vrais ou non.
Cependant, si cela était faux, on prouverait qu'un tel programme n'existe pas et que donc tous les programmes ne peuvent pas être décidés et que par ailleurs, tous les programmes ne peuvent pas être calculés.

On peut le résumer par ce schéma d'ensembles :

![schema](./Diagramme%20sans%20nom.drawio.png)

Une décénie plus tard, plusieurs mathématiciens ce sont penchés sur ce problème dont Alan Turing et Alonzo Church.

### Machine de Turing

La machine de Turing est une machine théorique. Elle n'as pas était pensée pour exister physiquement.
Elle est constituée :
    
un ruban infini
une tête de lecture qui peut lire et écrire sur ce ruban.
une table d'état

La machine se trouve dans un état, elle lis un symbole sur le ruban puis elle effectue les actions associées dans la table d'état.
La table d'état est composé de deux colonnes :
Première colonne : etat actuel & symbole lus
Deuxième colonne : etat suivant & déplacement de la tête de lecture & symbole à écrire

Cette machine de calcul permet de réfléchir sur la calculabilité d'un programme.
En effet Church énonce plusieurs choses dans dans sa thèse:
Toute fonction calculable est calculable sur une machine de Turing.
Chaque model(de calcul) possède la même puissance de calcul

Par définition, pour savoir si un programme est calculable(sur nos machines) on peut étudier s'il est calculable sur une machine de Turing.


### Lambda Calcul

```python
pentagone_regulier = lambda x : 5*x
```

## Une manière pour démontrer : Problème de l'arret

S'attaquer au problème de la décision était assez ambitieux pour Church et Turing. Ils ont alors choisi d'aborder le problème de l'arrêt.
S'ils réussissaient à valider ce problème, aborder le problème de la décision est possible.

On a expliqué précédemment que le modèle de la Machine de Turing est équivalent en terme de calcul au modèle de Von Neumann ou au lambda-calcul.

On peut se munir de deux fonctions python :

```python
def arret_garanti(fonction : Callable, args*):
    '''
    Paramètres :
    entrée : fonction : une fonction
             args* : les paramètres de la fonction passée en paramètre
    sortie : un booléen

    Renvoie True si le programme passé en paramètre s'arrête, False sinon.
    '''
    return #programme s'arrete




def une_fonction(n):
    '''
    Paramètres:
    entrée : un entier n
    sortie : une_fonction(n) si arret_garanti renvoie True, 1 sinon

    Fait tourner une_fonction en boucle si elle s'arrete, 
    renvoie un entier sinon.
    '''
    if arret_garanti(une_fonction(n)):
        return une_fonction(n)
    else : 
        return 1
```

La fonction _arret_garanti_, si elle fonctionne correctement, indique si un programme s'arrête ou non.

La fonction _une_fonction_, au vu de son implémentation, doit s'arrêter (renvoyer 1) si _arret_garanti_ indique qu'elle ne s'arrête pas.
De la même manière, si _arret_garanti_ indique que la fonction _une_fonction_ s'arrête, on appelle à nouveau _une_fonction_, donc elle ne s'arrête pas.

En analysant le code, on remarque que l'on se trouve dans le cas d'un paradoxe.

Ce contre-exemple indique donc que soit _une_fonction_ n'est pas réalisable, soit _arret_garanti_ n'est pas réalisable.

Le fait que _une_fonction_ dépende du résultat de son évaluation par _arret_garanti_ impose donc que la fonction _arret_garanti_ ne peut pas être écrite.

Comme ce problème de l'arrêt n'est pas décidable, Church et Turing ont indiqué que le _problème de la décision_ ne pouvait pas l'être. Cela a donc eu pour conséquence de montrer que tous les programmes ne peuvent être décidés.
