# KEKIFO

préambule :
    programme -> donnée
    pourquoi on cherche à prouver qu'un probleme de decision existe

définition :
    algorithme
    calculabilité -> équation diophantienne (pas simple mais contre exemple) / diamètre d'un cercle en fonction du rayon
    décidabilité -> comment s'habiller le lendemain /
    On veut savoir si toutes les fonctions sont calculables.

Comment résoudre ce problème ? Choix de l'absurde
    Turing :
        machine de turing (tete, ruban etc...) / Machines universelles  
            Fonction calculable -> Machine de turing qui le vérifie
    (Church :
        lambda calcul
            fonction calculable si calculable par lambda calcul)

expliciter équivalence de ces idées

prédire l'arrêt d'un programme est un problème de décision -> prouver qu'il existe permettrait de prouver que toutes les fonctions ne sont pas calculables

```python
def arret_garanti(f):
    ...

def une_fonction(n):
    if arret_garanti(fonction(n)):
        return une_fonction(n)
    else : 
        return 1

def arret(f):
    if ... : 
        return True
    else : 
        return False

def arret_fonction(f):
    if arret(arret_fonction(f)):
        while True:
            print("je m'arrete pas")
    else : 
        return False
```
