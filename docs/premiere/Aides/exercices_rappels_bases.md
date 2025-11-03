# Exercices de rappel - Les bases de Python 🐍

## 1. Les boucles `for` et `while` 🔄
[📚 Voir le cours sur les boucles](../I-Constructions_elementaires/Cours/Cours_1.md)

### Exercice 1.1 - Compter jusqu'à 10
**Objectif**: Écrire un programme qui affiche les nombres de 1 à 10.

**À faire**:

1. Utilisez une boucle `for`  
2. Puis refaites le même exercice avec une boucle `while`  

**Exemple de sortie attendue**:

```python
1
2
3
...
10
```

**Indice**: Pour la boucle `for`, pensez à utiliser `range()`.

### Exercice 1.2 - Table de multiplication

**Objectif**: Afficher la table de multiplication d'un nombre.

**À faire**:

Écrivez un programme qui:

1. Demande à l'utilisateur un nombre  
2. Affiche sa table de multiplication de 1 à 10  

**Exemple**:
Pour l'entrée 7:
```python
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

## 2. Les conditions `if` 🤔

[📚 Voir le cours sur les conditions](../I-Constructions_elementaires/Cours/Cours_1.md)

### Exercice 2.1 - Pair ou Impair

**Objectif**: Déterminer si un nombre est pair ou impair.

**À faire**:

1. Demandez un nombre à l'utilisateur  
2. Affichez "Pair" ou "Impair" selon le nombre  

**Indice**: Utilisez l'opérateur modulo `%`

### Exercice 2.2 - Note et Mention

**Objectif**: Afficher la mention correspondant à une note.

**À faire**:
Écrivez un programme qui:

1. Demande une note sur 20
2. Affiche la mention correspondante:
   - < 10: "Insuffisant"
   - 10-12: "Passable"
   - 12-14: "Assez Bien"
   - 14-16: "Bien"
   - ≥ 16: "Très Bien"

## 3. Les listes 📝

[📚 Voir le cours sur les listes](../III-Structures_de_donnees_lineaires/Cours/Cours.md)

### Exercice 3.1 - Manipulation de liste

**Objectif**: Pratiquer les opérations de base sur les listes.

**À faire**:

1. Créez une liste vide  
2. Ajoutez les nombres de 1 à 5  
3. Insérez le nombre 0 au début  
4. Supprimez le dernier élément  
5. Affichez la liste à chaque étape  

**Indice**: Utilisez `append()`, `insert()`, `pop()`

### Exercice 3.2 - Moyenne de classe
**Objectif**: Calculer la moyenne d'une liste de notes.

**À faire**:

1. Créez une liste de 5 notes  
2. Calculez et affichez la moyenne  
3. Affichez la note la plus haute et la plus basse  

**Indice**: Utilisez `len()`, `max()`, `min()`

## 4. Les dictionnaires 📚

[📚 Voir le cours sur les dictionnaires](../V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_1.md)

### Exercice 4.1 - Carnet d'adresses

**Objectif**: Créer et manipuler un carnet d'adresses simple.

**À faire**:

1. Créez un dictionnaire vide  
2. Ajoutez 3 contacts avec leur numéro de téléphone  
3. Affichez tous les contacts  
4. Modifiez un numéro  
5. Supprimez un contact  

**Exemple de structure**:
```python
carnet = {
    "Alice": "0123456789",
    "Bob": "9876543210"
}
```

### Exercice 4.2 - Mini-inventaire
**Objectif**: Gérer un inventaire de produits avec leurs prix.

**À faire**:
1. Créez un dictionnaire avec 4 produits et leurs prix
2. Affichez le prix d'un produit spécifique
3. Calculez le prix total de l'inventaire
4. Appliquez une réduction de 20% sur tous les prix

## Exercice Final - Tout Ensemble! 🎯

**Objectif**: Créer un mini-programme de gestion de notes d'élèves.

**À faire**:
1. Créez un dictionnaire où les clés sont les noms des élèves et les valeurs sont des listes de notes
2. Ajoutez au moins 3 élèves avec 4 notes chacun
3. Pour chaque élève:
   - Calculez sa moyenne
   - Déterminez sa mention
   - Affichez un résumé

**Exemple de structure**:
```python
notes = {
    "Alice": [15, 12, 18, 14],
    "Bob": [10, 8, 13, 15],
    "Charlie": [17, 16, 15, 18]
}
```

**Bonus**: Ajoutez des fonctionnalités comme:
- Trouver l'élève avec la meilleure moyenne
- Calculer la moyenne de la classe
- Afficher un graphique des moyennes

---