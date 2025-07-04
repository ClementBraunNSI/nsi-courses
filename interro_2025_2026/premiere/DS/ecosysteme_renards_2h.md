# DS Première NSI - Écosystème des Renards (2h)
**Nom :** _________________ **Prénom :** _________________ **Classe :** _______

**L'évaluation porte sur 3 exercices indépendants.**
**Les exercices sont notés sur 18 et la rigueur, rédaction, justifications et en-têtes sont notés sur 2 points.**

## Exercice 1 : Observation des comportements de chasse (6 points)

Des biologistes étudient les comportements de chasse des renards en forêt. Chaque observation est enregistrée dans une liste `observations_chasse`. Chaque élément de la liste est une chaîne de caractères représentant le type de comportement observé (ex: "affût", "poursuite", "fouissage", "écoute").

**1. Écrire une fonction `compter_comportement` qui prend en paramètre la liste `observations_chasse` et un type de comportement (chaîne de caractères), et renvoie le nombre de fois où ce comportement a été observé.**

```python
# Exemple d'utilisation
>>> observations = ["affût", "poursuite", "affût", "fouissage", "affût", "écoute"]
>>> compter_comportement(observations, "affût")
3
>>> compter_comportement(observations, "saut")
0
```

**2. Écrire une fonction `repertoire_comportements` qui prend en paramètre la liste `observations_chasse` et renvoie le nombre de types de comportements *différents* observés.**

```python
# Exemple d'utilisation
>>> observations = ["affût", "poursuite", "affût", "fouissage", "écoute", "poursuite"]
>>> repertoire_comportements(observations)
4
```

**3. Écrire une fonction `comportements_exceptionnels` qui prend en paramètre la liste `observations_chasse` et un seuil (entier), et renvoie la liste des types de comportements qui apparaissent exactement `seuil` fois.**

```python
# Exemple d'utilisation
>>> observations = ["affût", "poursuite", "affût", "fouissage", "écoute", "poursuite", "fouissage"]
>>> comportements_exceptionnels(observations, 2)
['poursuite', 'fouissage']
```

**4. Écrire une fonction `analyse_sequences` qui prend en paramètre la liste `observations_chasse` et un entier `n`, et renvoie une liste des séquences de `n` comportements consécutifs sous forme de tuples.**

```python
# Exemple d'utilisation
>>> observations = ["affût", "poursuite", "fouissage", "écoute", "affût"]
>>> analyse_sequences(observations, 3)
[('affût', 'poursuite', 'fouissage'), ('poursuite', 'fouissage', 'écoute'), ('fouissage', 'écoute', 'affût')]
```

## Exercice 2 : Gestion d'une réserve naturelle (6 points)

Vous gérez une réserve naturelle qui abrite plusieurs familles de renards. Chaque famille est représentée par un dictionnaire avec les clés suivantes : `"id_famille"` (entier unique), `"territoire"` (chaîne), `"espece"` (chaîne, ex: "Renard roux", "Renard argenté"), `"nb_adultes"` (entier), `"nb_jeunes"` (entier), et `"statut_sante"` (chaîne: "excellent", "bon", "surveiller", "critique").

**1. Écrire une fonction `ajouter_famille` qui prend en paramètre une liste de familles et les informations d'une nouvelle famille (territoire, espèce, nombre d'adultes, nombre de jeunes), génère un nouvel ID unique, et ajoute cette famille (avec statut "bon" par défaut) à la liste.**

```python
# Exemple d'utilisation
>>> familles = [{'id_famille': 1, 'territoire': 'Secteur A', 'espece': 'Renard roux',
 'nb_adultes': 2, 'nb_jeunes': 4, 'statut_sante': 'excellent'}]
>>> ajouter_famille(familles, 'Secteur B', 'Renard argenté', 2, 3)
>>> familles # L'ID peut varier
[{'id_famille': 1, 'territoire': 'Secteur A', 'espece': 'Renard roux', 
'nb_adultes': 2, 'nb_jeunes': 4, 'statut_sante': 'excellent'}, 
{'id_famille': 2, 'territoire': 'Secteur B', 'espece': 'Renard argenté', 
'nb_adultes': 2, 'nb_jeunes': 3, 'statut_sante': 'bon'}]
```

**2. Écrire une fonction `familles_par_territoire` qui prend en paramètre une liste de familles et renvoie un dictionnaire où les clés sont les territoires et les valeurs sont les listes des familles présentes dans chaque territoire.**

```python
# Exemple d'utilisation
>>> familles = [
{'id_famille': 1, 'territoire': 'Secteur A', 'espece': 'Renard roux', 
'nb_adultes': 2, 'nb_jeunes': 4, 'statut_sante': 'excellent'},
{'id_famille': 2, 'territoire': 'Secteur B', 'espece': 'Renard argenté', 
'nb_adultes': 2, 'nb_jeunes': 3, 'statut_sante': 'bon'},
{'id_famille': 3, 'territoire': 'Secteur A', 'espece': 'Renard roux', 
'nb_adultes': 2, 'nb_jeunes': 2, 'statut_sante': 'surveiller'}]

>>> familles_par_territoire(familles)
{'Secteur A': [famille1, famille3], 'Secteur B': [famille2]}
```

**3. Écrire une fonction `mettre_a_jour_sante` qui prend en paramètre une liste de familles, l'ID d'une famille et un nouveau statut de santé, et met à jour le statut. La fonction renvoie `True` si la mise à jour a réussi, `False` si l'ID n'existe pas.**

**4. Écrire une fonction `population_totale_espece` qui prend en paramètre une liste de familles et une espèce, et renvoie un dictionnaire avec le nombre total d'adultes et de jeunes pour cette espèce.**

```python
# Exemple d'utilisation
>>> population_totale_espece(familles, 'Renard roux')
{'adultes': 4, 'jeunes': 6}
```

## Exercice 3 : Centre de soins vétérinaires (6 points)

Vous travaillez dans un centre de soins qui traite des renards blessés. Chaque patient est représenté par un dictionnaire avec les clés : `"id_patient"`, `"nom"`, `"age_mois"`, `"poids_kg"`, `"type_blessure"`, `"gravite"` (entier de 1 à 10) et `"date_admission"` (au format "JJ/MM/AAAA").

**1. Écrire une fonction `tri_patients_gravite` qui prend en paramètre une liste de patients et renvoie une nouvelle liste triée par gravité décroissante (les plus graves en premier).**  
**Utilisez l'algorithme de tri par insertion.**

```python
# Exemple d'utilisation
>>> patients = [
{'id_patient': 1, 'nom': 'Roux', 'age_mois': 24, 'poids_kg': 5.2, 'type_blessure': 'fracture', 'gravite': 6, 'date_admission': '10/01/2025'},
{'id_patient': 2, 'nom': 'Flame', 'age_mois': 18, 'poids_kg': 4.8, 'type_blessure': 'coupure', 'gravite': 3, 'date_admission': '12/01/2025'},
{'id_patient': 3, 'nom': 'Shadow', 'age_mois': 36, 'poids_kg': 6.1, 'type_blessure': 'empoisonnement', 'gravite': 9, 'date_admission': '11/01/2025'}]
>>> tri_patients_gravite(patients)
# Résultat trié par gravité décroissante (9, 6, 3)
```

**2. Écrire une fonction `recherche_patient_dichotomique` qui prend en paramètre une liste de patients triée par ID et un ID recherché, et renvoie le patient correspondant ou `None` si aucun patient n'a cet ID.**
**Utilisez l'algorithme de recherche dichotomique.**

**3. Écrire une fonction `statistiques_blessures` qui prend en paramètre une liste de patients et renvoie un dictionnaire contenant pour chaque type de blessure : le nombre de cas, la gravité moyenne et l'âge moyen des patients.**

```python
# Exemple d'utilisation
>>> statistiques_blessures(patients)
{'fracture': {'nombre': 1, 'gravite_moyenne': 6.0, 'age_moyen': 24.0},
'coupure': {'nombre': 1, 'gravite_moyenne': 3.0, 'age_moyen': 18.0},
'empoisonnement': {'nombre': 1, 'gravite_moyenne': 9.0, 'age_moyen': 36.0}}
```

**4. Écrire une fonction `patients_urgents` qui prend en paramètre une liste de patients et renvoie la liste des patients dont la gravité est supérieure ou égale à 7 ET le poids est inférieur à 4 kg.**

**Question bonus : Modifier la fonction `patients_urgents` pour qu'elle renvoie une liste triée par date d'admission (plus récents en premier).**