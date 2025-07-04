# Le modèle relationnel

## Introduction

Le **modèle relationnel** est un modèle de données qui organise les données sous forme de **relations** (tables). Proposé par Edgar F. Codd en 1970, il constitue la base théorique des systèmes de gestion de bases de données relationnelles (SGBDR).

## Concepts fondamentaux

### Relation (Table)

Une **relation** est une structure de données bidimensionnelle composée de :
- **Lignes** (tuples ou enregistrements) : représentent les instances d'entités
- **Colonnes** (attributs ou champs) : représentent les propriétés des entités

### Attribut

Un **attribut** est une propriété ou caractéristique d'une entité. Chaque attribut possède :
- Un **nom** unique dans la relation
- Un **domaine** : ensemble des valeurs possibles
- Un **type de données** (entier, chaîne, date, etc.)

### Domaine

Le **domaine** d'un attribut définit l'ensemble des valeurs autorisées pour cet attribut.

**Exemple :**
- Domaine de l'attribut "âge" : entiers positifs de 0 à 150
- Domaine de l'attribut "sexe" : {'M', 'F'}

### Tuple (Enregistrement)

Un **tuple** est une ligne de la table qui contient une valeur pour chaque attribut de la relation.

### Schéma relationnel

Le **schéma relationnel** décrit la structure d'une relation en spécifiant :
- Le nom de la relation
- La liste des attributs avec leurs domaines
- Les contraintes d'intégrité

**Notation :** `RELATION(attribut1: domaine1, attribut2: domaine2, ...)`

**Exemple :**
```
ETUDIANT(id_etudiant: entier, nom: chaîne, prenom: chaîne, age: entier, email: chaîne)
```

## Les clés

### Clé primaire

Une **clé primaire** est un attribut (ou un ensemble d'attributs) qui :
- Identifie de manière **unique** chaque tuple de la relation
- Ne peut pas être **NULL**
- Ne peut pas être **dupliquée**

**Exemple :**
```
ETUDIANT(id_etudiant: entier [PK], nom: chaîne, prenom: chaîne, age: entier)
```

### Clé étrangère

Une **clé étrangère** est un attribut (ou un ensemble d'attributs) qui :
- Fait référence à la clé primaire d'une autre relation
- Assure l'**intégrité référentielle**
- Peut être NULL (sauf contrainte spécifique)

**Exemple :**
```
INSCRIPTION(id_inscription: entier [PK], id_etudiant: entier [FK], id_cours: entier [FK], date_inscription: date)
```

### Clé candidate

Une **clé candidate** est un attribut (ou ensemble d'attributs) qui pourrait servir de clé primaire.

### Super-clé

Une **super-clé** est un ensemble d'attributs qui contient une clé candidate.

## Contraintes d'intégrité

### Intégrité d'entité

- La clé primaire ne peut jamais être NULL
- Chaque tuple doit être unique

### Intégrité référentielle

- Une clé étrangère doit soit être NULL, soit référencer une clé primaire existante
- Pas de "références pendantes"

### Intégrité de domaine

- Chaque valeur d'attribut doit appartenir au domaine défini
- Respect des types de données

## Exemple complet

Considérons une base de données pour une bibliothèque :

### Schémas relationnels

```
LIVRE(isbn: chaîne [PK], titre: chaîne, auteur: chaîne, annee_publication: entier, nb_pages: entier)

LECTEUR(id_lecteur: entier [PK], nom: chaîne, prenom: chaîne, date_naissance: date, email: chaîne)

EMPRUNT(id_emprunt: entier [PK], isbn: chaîne [FK], id_lecteur: entier [FK], date_emprunt: date, date_retour_prevue: date, date_retour_effective: date)
```

### Tables avec données

**Table LIVRE :**
| isbn | titre | auteur | annee_publication | nb_pages |
|------|-------|--------|-------------------|----------|
| 978-2-123456-78-9 | 1984 | George Orwell | 1949 | 328 |
| 978-2-987654-32-1 | Le Petit Prince | Antoine de Saint-Exupéry | 1943 | 96 |

**Table LECTEUR :**
| id_lecteur | nom | prenom | date_naissance | email |
|------------|-----|--------|----------------|-------|
| 1 | Dupont | Jean | 1990-05-15 | jean.dupont@email.com |
| 2 | Martin | Marie | 1985-12-03 | marie.martin@email.com |

**Table EMPRUNT :**
| id_emprunt | isbn | id_lecteur | date_emprunt | date_retour_prevue | date_retour_effective |
|------------|------|------------|--------------|--------------------|-----------------------|
| 1 | 978-2-123456-78-9 | 1 | 2024-01-15 | 2024-02-15 | 2024-02-10 |
| 2 | 978-2-987654-32-1 | 2 | 2024-01-20 | 2024-02-20 | NULL |

## Avantages du modèle relationnel

1. **Simplicité** : Structure tabulaire intuitive
2. **Flexibilité** : Facilité de modification et d'extension
3. **Intégrité** : Contraintes garantissant la cohérence des données
4. **Indépendance** : Séparation entre structure logique et physique
5. **Standardisation** : Langage SQL universel

## Normalisation

La **normalisation** est un processus qui vise à :
- Éliminer la redondance des données
- Éviter les anomalies de mise à jour
- Optimiser l'organisation des données

### Première forme normale (1FN)

Une relation est en 1FN si :
- Chaque attribut contient des valeurs atomiques (indivisibles)
- Pas de groupes répétitifs

### Deuxième forme normale (2FN)

Une relation est en 2FN si :
- Elle est en 1FN
- Tous les attributs non-clés dépendent entièrement de la clé primaire

### Troisième forme normale (3FN)

Une relation est en 3FN si :
- Elle est en 2FN
- Aucun attribut non-clé ne dépend transitivement de la clé primaire

## Exercices pratiques

### Exercice 1 : Identification des clés

Soit la relation suivante :
```
VOITURE(immatriculation, marque, modele, couleur, annee, proprietaire_nom, proprietaire_adresse)
```

1. Identifiez la clé primaire
2. Y a-t-il des clés candidates ?
3. Cette relation respecte-t-elle la 3FN ?

### Exercice 2 : Conception d'un schéma

Concevez un schéma relationnel pour gérer :
- Des étudiants (nom, prénom, numéro étudiant, email)
- Des cours (code cours, nom, crédits, enseignant)
- Des inscriptions (étudiant, cours, semestre, note)

1. Définissez les relations avec leurs attributs
2. Identifiez les clés primaires et étrangères
3. Vérifiez les contraintes d'intégrité

## Conclusion

Le modèle relationnel fournit une base solide pour l'organisation et la gestion des données. Sa simplicité conceptuelle, combinée à sa puissance expressive, en fait le standard de facto pour les bases de données. La compréhension de ses principes est essentielle pour concevoir des bases de données efficaces et maintenir l'intégrité des données.