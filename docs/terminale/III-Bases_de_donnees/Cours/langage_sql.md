# Langage SQL (Structured Query Language)

## Introduction

SQL (Structured Query Language) est le langage standard pour interagir avec les bases de données relationnelles. Développé dans les années 1970 par IBM, il permet de :
- **Interroger** les données (requêtes)
- **Modifier** la structure des bases de données
- **Insérer, modifier et supprimer** des données
- **Contrôler** les accès et la sécurité

## Types d'instructions SQL

### DDL (Data Definition Language)
**Définition de la structure des données**
- `CREATE` : Créer des objets (tables, index, vues)
- `ALTER` : Modifier la structure
- `DROP` : Supprimer des objets

### DML (Data Manipulation Language)
**Manipulation des données**
- `SELECT` : Interroger les données
- `INSERT` : Insérer des données
- `UPDATE` : Modifier des données
- `DELETE` : Supprimer des données

### DCL (Data Control Language)
**Contrôle des accès**
- `GRANT` : Accorder des droits
- `REVOKE` : Révoquer des droits

## Création de tables (DDL)

### Syntaxe CREATE TABLE

```sql
CREATE TABLE nom_table (
    colonne1 type_donnees [contraintes],
    colonne2 type_donnees [contraintes],
    ...
    [contraintes_table]
);
```

### Types de données courants

| Type | Description | Exemple |
|------|-------------|----------|
| `INTEGER` | Nombre entier | `age INTEGER` |
| `REAL` / `FLOAT` | Nombre décimal | `prix REAL` |
| `TEXT` / `VARCHAR(n)` | Chaîne de caractères | `nom VARCHAR(50)` |
| `DATE` | Date | `naissance DATE` |
| `BOOLEAN` | Booléen | `actif BOOLEAN` |

### Contraintes

```sql
CREATE TABLE etudiants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INTEGER CHECK (age >= 16 AND age <= 99),
    date_inscription DATE DEFAULT CURRENT_DATE
);
```

**Types de contraintes :**
- `PRIMARY KEY` : Clé primaire
- `FOREIGN KEY` : Clé étrangère
- `NOT NULL` : Valeur obligatoire
- `UNIQUE` : Valeur unique
- `CHECK` : Condition à respecter
- `DEFAULT` : Valeur par défaut

### Exemple complet : Base de données bibliothèque

```sql
-- Table des auteurs
CREATE TABLE auteurs (
    id_auteur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE,
    nationalite VARCHAR(30)
);

-- Table des livres
CREATE TABLE livres (
    isbn VARCHAR(17) PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    id_auteur INTEGER,
    annee_publication INTEGER CHECK (annee_publication > 0),
    nb_pages INTEGER CHECK (nb_pages > 0),
    genre VARCHAR(50),
    FOREIGN KEY (id_auteur) REFERENCES auteurs(id_auteur)
);

-- Table des lecteurs
CREATE TABLE lecteurs (
    id_lecteur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    date_inscription DATE DEFAULT CURRENT_DATE
);

-- Table des emprunts
CREATE TABLE emprunts (
    id_emprunt INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn VARCHAR(17),
    id_lecteur INTEGER,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    FOREIGN KEY (isbn) REFERENCES livres(isbn),
    FOREIGN KEY (id_lecteur) REFERENCES lecteurs(id_lecteur)
);
```

## Insertion de données (DML)

### INSERT INTO

```sql
-- Insertion d'un seul enregistrement
INSERT INTO auteurs (nom, prenom, date_naissance, nationalite)
VALUES ('Orwell', 'George', '1903-06-25', 'Britannique');

-- Insertion multiple
INSERT INTO auteurs (nom, prenom, nationalite) VALUES
    ('Hugo', 'Victor', 'Française'),
    ('Camus', 'Albert', 'Française'),
    ('Tolkien', 'J.R.R.', 'Britannique');

-- Insertion avec sous-requête
INSERT INTO livres_populaires (isbn, titre)
SELECT isbn, titre 
FROM livres 
WHERE nb_emprunts > 100;
```

## Requêtes de sélection (DML)

### SELECT de base

```sql
-- Sélection de toutes les colonnes
SELECT * FROM livres;

-- Sélection de colonnes spécifiques
SELECT titre, annee_publication FROM livres;

-- Sélection avec alias
SELECT titre AS "Titre du livre", 
       annee_publication AS "Année" 
FROM livres;
```

### Clause WHERE

```sql
-- Condition simple
SELECT * FROM livres WHERE annee_publication > 2000;

-- Conditions multiples
SELECT * FROM livres 
WHERE annee_publication BETWEEN 1950 AND 2000 
  AND genre = 'Science-fiction';

-- Opérateurs de comparaison
SELECT * FROM livres WHERE titre LIKE '%Python%';
SELECT * FROM auteurs WHERE nationalite IN ('Française', 'Britannique');
SELECT * FROM emprunts WHERE date_retour_effective IS NULL;
```

### Tri et limitation

```sql
-- Tri croissant
SELECT * FROM livres ORDER BY annee_publication;

-- Tri décroissant
SELECT * FROM livres ORDER BY annee_publication DESC;

-- Tri multiple
SELECT * FROM livres ORDER BY genre, annee_publication DESC;

-- Limitation du nombre de résultats
SELECT * FROM livres ORDER BY annee_publication DESC LIMIT 5;

-- Pagination
SELECT * FROM livres ORDER BY titre LIMIT 10 OFFSET 20;
```

## Jointures

### INNER JOIN

```sql
-- Livres avec leurs auteurs
SELECT l.titre, a.nom, a.prenom
FROM livres l
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur;
```

### LEFT JOIN

```sql
-- Tous les auteurs, même ceux sans livres
SELECT a.nom, a.prenom, l.titre
FROM auteurs a
LEFT JOIN livres l ON a.id_auteur = l.id_auteur;
```

### Jointures multiples

```sql
-- Emprunts avec détails du livre et du lecteur
SELECT 
    lec.nom AS lecteur_nom,
    lec.prenom AS lecteur_prenom,
    l.titre,
    a.nom AS auteur_nom,
    e.date_emprunt,
    e.date_retour_prevue
FROM emprunts e
INNER JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
INNER JOIN livres l ON e.isbn = l.isbn
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur
WHERE e.date_retour_effective IS NULL;
```

## Fonctions d'agrégation

### Fonctions de base

```sql
-- Nombre total de livres
SELECT COUNT(*) AS nombre_livres FROM livres;

-- Année de publication la plus récente
SELECT MAX(annee_publication) AS annee_max FROM livres;

-- Nombre moyen de pages
SELECT AVG(nb_pages) AS moyenne_pages FROM livres;

-- Somme des pages de tous les livres
SELECT SUM(nb_pages) AS total_pages FROM livres;
```

### GROUP BY et HAVING

```sql
-- Nombre de livres par genre
SELECT genre, COUNT(*) AS nombre_livres
FROM livres
GROUP BY genre
ORDER BY nombre_livres DESC;

-- Genres avec plus de 5 livres
SELECT genre, COUNT(*) AS nombre_livres
FROM livres
GROUP BY genre
HAVING COUNT(*) > 5;

-- Auteurs avec le nombre de leurs livres
SELECT 
    a.nom,
    a.prenom,
    COUNT(l.isbn) AS nombre_livres
FROM auteurs a
LEFT JOIN livres l ON a.id_auteur = l.id_auteur
GROUP BY a.id_auteur, a.nom, a.prenom
ORDER BY nombre_livres DESC;
```

## Sous-requêtes

### Sous-requête dans WHERE

```sql
-- Livres de l'auteur le plus prolifique
SELECT titre
FROM livres
WHERE id_auteur = (
    SELECT id_auteur
    FROM livres
    GROUP BY id_auteur
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- Livres plus récents que la moyenne
SELECT titre, annee_publication
FROM livres
WHERE annee_publication > (
    SELECT AVG(annee_publication)
    FROM livres
);
```

### Sous-requête avec EXISTS

```sql
-- Auteurs qui ont écrit au moins un livre
SELECT nom, prenom
FROM auteurs a
WHERE EXISTS (
    SELECT 1
    FROM livres l
    WHERE l.id_auteur = a.id_auteur
);
```

## Modification de données

### UPDATE

```sql
-- Mise à jour simple
UPDATE livres 
SET genre = 'Dystopie' 
WHERE titre = '1984';

-- Mise à jour avec jointure
UPDATE emprunts 
SET date_retour_effective = CURRENT_DATE
WHERE id_emprunt = 1;

-- Mise à jour conditionnelle
UPDATE livres 
SET genre = 'Classique'
WHERE annee_publication < 1950;
```

### DELETE

```sql
-- Suppression avec condition
DELETE FROM emprunts 
WHERE date_retour_effective IS NOT NULL 
  AND date_retour_effective < '2020-01-01';

-- Suppression avec sous-requête
DELETE FROM livres 
WHERE id_auteur IN (
    SELECT id_auteur 
    FROM auteurs 
    WHERE nationalite = 'Inconnue'
);
```

## Vues

```sql
-- Création d'une vue
CREATE VIEW livres_disponibles AS
SELECT 
    l.isbn,
    l.titre,
    a.nom AS auteur_nom,
    a.prenom AS auteur_prenom,
    l.genre
FROM livres l
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur
WHERE l.isbn NOT IN (
    SELECT isbn 
    FROM emprunts 
    WHERE date_retour_effective IS NULL
);

-- Utilisation de la vue
SELECT * FROM livres_disponibles WHERE genre = 'Science-fiction';
```

## Index pour l'optimisation

```sql
-- Index simple
CREATE INDEX idx_livres_genre ON livres(genre);

-- Index composé
CREATE INDEX idx_emprunts_dates ON emprunts(date_emprunt, date_retour_effective);

-- Index unique
CREATE UNIQUE INDEX idx_lecteurs_email ON lecteurs(email);
```

## Exemple pratique avec Python

```python
import sqlite3
from datetime import datetime, timedelta

def gestion_bibliotheque():
    # Connexion à la base
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    
    # Fonction pour emprunter un livre
    def emprunter_livre(isbn, id_lecteur):
        try:
            # Vérifier si le livre est disponible
            cursor.execute("""
                SELECT COUNT(*) FROM emprunts 
                WHERE isbn = ? AND date_retour_effective IS NULL
            """, (isbn,))
            
            if cursor.fetchone()[0] > 0:
                return "Livre déjà emprunté"
            
            # Créer l'emprunt
            date_emprunt = datetime.now().date()
            date_retour = date_emprunt + timedelta(days=21)  # 3 semaines
            
            cursor.execute("""
                INSERT INTO emprunts (isbn, id_lecteur, date_emprunt, date_retour_prevue)
                VALUES (?, ?, ?, ?)
            """, (isbn, id_lecteur, date_emprunt, date_retour))
            
            conn.commit()
            return "Emprunt créé avec succès"
            
        except sqlite3.Error as e:
            conn.rollback()
            return f"Erreur : {e}"
    
    # Fonction pour retourner un livre
    def retourner_livre(isbn, id_lecteur):
        try:
            cursor.execute("""
                UPDATE emprunts 
                SET date_retour_effective = CURRENT_DATE
                WHERE isbn = ? AND id_lecteur = ? AND date_retour_effective IS NULL
            """, (isbn, id_lecteur))
            
            if cursor.rowcount > 0:
                conn.commit()
                return "Livre retourné avec succès"
            else:
                return "Aucun emprunt trouvé"
                
        except sqlite3.Error as e:
            conn.rollback()
            return f"Erreur : {e}"
    
    # Fonction pour lister les emprunts en retard
    def emprunts_en_retard():
        cursor.execute("""
            SELECT 
                lec.nom,
                lec.prenom,
                l.titre,
                e.date_retour_prevue,
                (julianday('now') - julianday(e.date_retour_prevue)) AS jours_retard
            FROM emprunts e
            JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
            JOIN livres l ON e.isbn = l.isbn
            WHERE e.date_retour_effective IS NULL 
              AND e.date_retour_prevue < date('now')
            ORDER BY jours_retard DESC
        """)
        
        return cursor.fetchall()
    
    return emprunter_livre, retourner_livre, emprunts_en_retard
```

## Exercices pratiques

### Exercice 1 : Requêtes de base

À partir de la base de données bibliothèque, écrivez les requêtes SQL pour :

1. Afficher tous les livres publiés après 2000
2. Compter le nombre de livres par genre
3. Trouver les auteurs français
4. Lister les emprunts non rendus

### Exercice 2 : Jointures

Écrivez les requêtes pour :

1. Afficher les livres avec le nom complet de leur auteur
2. Lister tous les emprunts avec les détails du livre et du lecteur
3. Trouver les auteurs qui n'ont écrit aucun livre
4. Afficher les lecteurs qui n'ont jamais emprunté de livre

### Exercice 3 : Fonctions d'agrégation

1. Calculer le nombre moyen de pages par genre
2. Trouver l'auteur avec le plus de livres
3. Afficher le nombre d'emprunts par mois
4. Lister les genres avec plus de 3 livres

### Exercice 4 : Sous-requêtes

1. Trouver les livres plus longs que la moyenne
2. Afficher les lecteurs qui ont emprunté plus de 5 livres
3. Lister les livres jamais empruntés
4. Trouver les auteurs dont tous les livres ont été empruntés

## Bonnes pratiques

### Performance

1. **Utiliser des index** sur les colonnes fréquemment recherchées
2. **Éviter SELECT *** : sélectionner uniquement les colonnes nécessaires
3. **Utiliser LIMIT** pour limiter les résultats
4. **Optimiser les jointures** : utiliser les bonnes clés

### Sécurité

1. **Paramètres liés** : éviter les injections SQL
2. **Validation des entrées** : vérifier les données utilisateur
3. **Droits minimaux** : principe du moindre privilège
4. **Audit** : tracer les opérations sensibles

### Lisibilité

1. **Indentation** : structurer les requêtes complexes
2. **Alias explicites** : noms de colonnes clairs
3. **Commentaires** : documenter la logique métier
4. **Conventions** : noms cohérents pour tables et colonnes

## Conclusion

SQL est un langage puissant et standardisé qui permet de manipuler efficacement les données relationnelles. Sa maîtrise est essentielle pour :
- Développer des applications utilisant des bases de données
- Analyser et extraire des informations de grandes quantités de données
- Optimiser les performances des systèmes d'information
- Assurer l'intégrité et la sécurité des données

La pratique régulière et la compréhension des concepts sous-jacents sont clés pour devenir efficace en SQL.