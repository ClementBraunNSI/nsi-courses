# 📚 Introduction aux bases de données et au langage SQL

## 📖 Définition - Introduction aux Bases de Données

### Qu'est-ce qu'une Base de Données ?

Une **base de données** est un ensemble organisé d'informations structurées de manière à pouvoir être facilement accessible, gérée et mise à jour.

On peut associer cela à un grand tableau organisé en colonnes, nommées attributs (à l'instar des fichiers CSV).

### Pourquoi utiliser une Base de Données ?

Le but principal des bases de données est de faciliter :

- **Le stockage organisé** : Les informations sont rangées de façon structurée, souvent sous forme de tables, ce qui facilite la gestion.
- **La recherche efficace** : On peut rapidement trouver des données spécifiques grâce à des requêtes.
- **La maintenance** : On peut mettre à jour ou supprimer des informations de façon sécurisée.
- **L'intégrité et la sécurité des données** : Les bases de données relationnelles assurent que les données sont fiables et protégées.

## 📚 Historique - Historique des Bases de Données Relationnelles

### Origines

Dans les années 1960, les bases de données étaient très basiques et souvent peu optimisées.
En 1970, **Edgar F. Codd** propose le **modèle relationnel**. Son idée était de simplifier la gestion des données en les organisant sous forme de tables reliées par des relations logiques.

### Le modèle relationnel

Dans ce modèle, les données sont organisées en **tables**.
Une table est constituée de :

- **Lignes** (ou enregistrements) : Chaque ligne représente un élément unique (par exemple, un étudiant).
- **Colonnes** (ou attributs) : Chaque colonne décrit une caractéristique de cet élément (par exemple, le nom, l'âge, la classe).

Exemple d'une table `Etudiants` :

| id  | nom       | age | classe   |
|-----|-----------|-----|-----------|
| 1   | Alice     | 17  | Terminale|
| 2   | Bob       | 16  | Première |
| 3   | Charlie   | 18  | Terminale|

---

## 📖 Définition - Introduction au SQL

### Qu'est-ce que le SQL ?

Le **SQL** (Structured Query Language) est le langage utilisé pour interagir avec une base de données relationnelle. Il permet de **poser des questions** à la base de données et d'obtenir des réponses sous forme de tables. On parle de **requêtes SQL** pour désigner ces questions.

### Principes de base du SQL

Le SQL permet de réaliser des requêtes de demande de données suivant des critères plus facilement et de manière plus sécurisée en communiquant avec une base de données normalisée.

#### Projeter des données : `SELECT`

La commande `SELECT` permet de **récupérer des lignes spécifiques** (appelés **enregistrements**) d'une table.

> **⚠️ Attention**
> Il ne faut pas confondre la commande SELECT avec la sélection. Sélectionner des données revient à réaliser une projection **avec des contraintes**.

*Exemple* : Supposons que nous voulons obtenir les informations de tous les étudiants.

```sql
SELECT * FROM Etudiants;
```

`SELECT *` signifie "retourner toutes les colonnes". `FROM Etudiants` indique que l'on travaille avec la table Etudiants.

*Exemple* : Supposons que l'on veut afficher uniquement le nom et l'âge des étudiants

```sql
SELECT nom, age FROM Etudiants;
```

#### Sélectionner des attributs

Pour sélectionner les valeurs suivant des contraintes / conditions, on doit ajouter à notre requête le mot-clef WHERE avec une condition à la suite.

Par exemple, si l'on souhaite aficher le nom des étudiants qui ont plus de 17 ans, on va utiliser la requête suivante:

```sql
SELECT nom FROM Etudiants WHERE age > 17;
```

Ici, on veut afficher le nom des étudiants avec l'instruction `SELECT nom FROM Etudiants` mais en ajouter la contrainte `WHERE age > 17` permet d'obtenir tous les noms uniquement de ceux ayant plus de 17 ans.

## 📖 Définition - Activité : SQL Murder Mystery

Pour appliquer cela, vous pouvez vous diriger vers le site "SQL Murder Mystery" qui permet de résoudre une enquête d'un crime à l'aide de bases de données et de requête en langage SQL.
*(Attention, le site est uniquement en anglais)*.

Vous pouvez rejoindre le site [en cliquant ici](https://mystery.knightlab.com)