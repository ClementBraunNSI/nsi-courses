# Interrogation : Dictionnaires

**L'évaluation porte sur 3 exercices indépendants.**
**Les exercices sont notés sur 18 et la rigueur, rédaction et justifications sont notés sur 2 points.**

## Exercice 1 : Questions de cours (2 points)

1. Un dictionnaire est un couple (... : ...). À quoi correspondent chacun des ... ?
2. Créer le dictionnaire Python associé à cet objet :  

|ville|code postal|departmement|region|nombre d'habitants|
|-----|-----------|------------|------|------------------|
|Vannes|56000, 56001,56002,56003|Morbihan|Bretagne|54420|

3. Donner l'instruction python qui permet de changer le nombre d'habitant de 54420 à 54532.

## Exercice 2 : Complétion de programme (4 points)

**Compléter la fonction `filtrer_dictionnaire` qui prend en paramètre un dictionnaire et une valeur seuil, et renvoie un nouveau dictionnaire ne contenant que les éléments supérieurs à cette valeur.**

*Exemple :*

```python
    filtrer_dictionnaire({'a': 10, 'b': 5, 'c': 15, 'd': 3}, 7)  # Renvoie: {'a': 10, 'c': 15}
    filtrer_dictionnaire({'x': 2, 'y': 8, 'z': 4}, 10)  # Renvoie: {}
```

```python
    def filtrer_dictionnaire(dico: dict, seuil: int) -> dict:
    resultat = {}
    for ... :
        if ... > seuil:
            resultat[...] = ...
    return resultat

```

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Exercice 3 : Écriture de programmes (12 points)

**Écrire une fonction compter_occurrences qui prend une liste et renvoie un dictionnaire où les clés sont les éléments de la liste et les valeurs sont leurs nombres d'occurrences.**
*Exemple :*
*compter_occurrences(['pomme', 'banane', 'pomme', 'cerise', 'banane', 'pomme']) doit renvoyer {'pomme': 3, 'banane': 2, 'cerise': 1}*.

**Écrire une fonction notes_par_appreciation qui prend un dictionnaire de notes et renvoie un nouveau dictionnaire classant les notes par appréciation.**

*Critères de notation :*

*Moins de 10 : "Insuffisant"*
*Entre 10 et 12 : "Passable"*
*Entre 12 et 14 : "Bien"*
*Entre 14 et 16 : "Très bien"*
*16 et plus : "Excellent"*

```python
    >>> notes = {'Pierre': 15, 'Marie': 8, 'Jean': 13, 'Sophie': 17}
    >>> notes_par_appreciation(notes)  
    {
         'Insuffisant': ['Marie'], 
         'Bien': ['Jean'], 
         'Très bien': ['Pierre'], 
         'Excellent': ['Sophie']
     }
```

**Écrire une fonction kilometre_max qui prend un dictionnaire et renvoie le nom de la voiture la plus kilométrée.**
*Exemple :*
*trouver_max({'X1': 132000, 'Bayon': 25000, 'Paceman': 145000}) doit renvoyer 'Paceman'*.

**Écrire une fonction filtrer_par_cle qui prend un dictionnaire et une longueur minimale, et renvoie un nouveau dictionnaire ne contenant que les clés de longueur supérieure ou égale à la longueur donnée.**
*Exemple :*
*filtrer_par_cle({'a': 1, 'abc': 2, 'de': 3, 'fghi': 4}, 3) doit renvoyer {'abc': 2, 'fghi': 4}*.