# Le langage SQL

## Introduction

SQL (Structured Query Language) est le langage standard pour interagir avec les bases de données relationnelles. Il permet de :
- Créer et modifier la structure des données (DDL)
- Manipuler les données (DML)
- Contrôler les accès (DCL)
- Contrôler les transactions (TCL)

### Types d'instructions SQL

1. **DDL (Data Definition Language)** : CREATE, ALTER, DROP
2. **DML (Data Manipulation Language)** : SELECT, INSERT, UPDATE, DELETE
3. **DCL (Data Control Language)** : GRANT, REVOKE
4. **TCL (Transaction Control Language)** : COMMIT, ROLLBACK

---

## Création de la structure (DDL)

### CREATE TABLE

#### Syntaxe de base
```sql
CREATE TABLE nom_table (
    nom_colonne1 TYPE [CONTRAINTES],
    nom_colonne2 TYPE [CONTRAINTES],
    ...
    [CONTRAINTES_TABLE]
);
```

#### Types de données courants

**Types numériques :**
- `INTEGER` ou `INT` : nombres entiers
- `REAL` ou `FLOAT` : nombres décimaux
- `DECIMAL(p,s)` : nombres décimaux précis

**Types texte :**
- `VARCHAR(n)` : chaîne de caractères variable (max n)
- `CHAR(n)` : chaîne de caractères fixe
- `TEXT` : texte de longueur variable

**Types date/heure :**
- `DATE` : date (YYYY-MM-DD)
- `TIME` : heure (HH:MM:SS)
- `DATETIME` ou `TIMESTAMP` : date et heure

**Autres :**
- `BOOLEAN` : vrai/faux
- `BLOB` : données binaires

#### Contraintes de colonne

```sql
CREATE TABLE ELEVES (
    id_eleve INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INTEGER CHECK (age >= 15 AND age <= 25),
    date_naissance DATE,
    moyenne REAL DEFAULT 0.0
);
```

**Contraintes disponibles :**
- `PRIMARY KEY` : clé primaire
- `NOT NULL` : valeur obligatoire
- `UNIQUE` : valeur unique
- `CHECK (condition)` : contrainte personnalisée
- `DEFAULT valeur` : valeur par défaut
- `FOREIGN KEY` : clé étrangère

#### Clés étrangères

```sql
CREATE TABLE NOTES (
    id_note INTEGER PRIMARY KEY,
    id_eleve INTEGER NOT NULL,
    matiere VARCHAR(50) NOT NULL,
    note REAL CHECK (note >= 0 AND note <= 20),
    date_evaluation DATE NOT NULL,
    FOREIGN KEY (id_eleve) REFERENCES ELEVES(id_eleve)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

**Options pour les clés étrangères :**
- `ON DELETE CASCADE` : supprime les enregistrements liés
- `ON DELETE SET NULL` : met NULL dans la clé étrangère
- `ON DELETE RESTRICT` : empêche la suppression
- `ON UPDATE CASCADE` : met à jour les clés étrangères

### ALTER TABLE

```sql
-- Ajouter une colonne
ALTER TABLE ELEVES ADD COLUMN telephone VARCHAR(15);

-- Modifier une colonne
ALTER TABLE ELEVES ALTER COLUMN nom VARCHAR(100);

-- Supprimer une colonne
ALTER TABLE ELEVES DROP COLUMN telephone;

-- Ajouter une contrainte
ALTER TABLE ELEVES ADD CONSTRAINT chk_age 
    CHECK (age >= 15 AND age <= 25);
```

### DROP TABLE

```sql
-- Supprimer une table
DROP TABLE NOTES;

-- Supprimer si elle existe
DROP TABLE IF EXISTS NOTES;
```

---

## Manipulation des données (DML)

### INSERT - Insertion de données

#### Syntaxe de base
```sql
INSERT INTO nom_table (colonne1, colonne2, ...)
VALUES (valeur1, valeur2, ...);
```

#### Exemples

```sql
-- Insertion simple
INSERT INTO ELEVES (id_eleve, nom, prenom, age)
VALUES (1, 'Dupont', 'Marie', 17);

-- Insertion multiple
INSERT INTO ELEVES (id_eleve, nom, prenom, age) VALUES
    (2, 'Martin', 'Paul', 18),
    (3, 'Bernard', 'Julie', 17),
    (4, 'Petit', 'Lucas', 16);

-- Insertion avec toutes les colonnes (ordre de la table)
INSERT INTO ELEVES VALUES (5, 'Moreau', 'Emma', 'emma@email.com', 17, '2006-03-15', 14.5);

-- Insertion à partir d'une autre table
INSERT INTO ELEVES_ARCHIVE (id_eleve, nom, prenom)
SELECT id_eleve, nom, prenom FROM ELEVES WHERE age >= 18;
```

### SELECT - Consultation des données

#### Syntaxe complète
```sql
SELECT [DISTINCT] colonnes
FROM table1 [alias1]
[JOIN table2 [alias2] ON condition]
[WHERE condition]
[GROUP BY colonnes]
[HAVING condition]
[ORDER BY colonnes [ASC|DESC]]
[LIMIT nombre];
```

#### Sélection simple

```sql
-- Toutes les colonnes
SELECT * FROM ELEVES;

-- Colonnes spécifiques
SELECT nom, prenom, age FROM ELEVES;

-- Avec alias
SELECT nom AS "Nom de famille", prenom AS "Prénom" FROM ELEVES;

-- Valeurs distinctes
SELECT DISTINCT age FROM ELEVES;

-- Calculs
SELECT nom, prenom, age, (2024 - age) AS annee_naissance FROM ELEVES;
```

#### Clause WHERE - Filtrage

```sql
-- Conditions simples
SELECT * FROM ELEVES WHERE age > 17;
SELECT * FROM ELEVES WHERE nom = 'Dupont';
SELECT * FROM ELEVES WHERE email IS NOT NULL;

-- Opérateurs de comparaison
SELECT * FROM ELEVES WHERE age >= 16 AND age <= 18;
SELECT * FROM ELEVES WHERE age BETWEEN 16 AND 18;  -- Équivalent

-- Opérateurs logiques
SELECT * FROM ELEVES WHERE age > 17 OR moyenne > 15;
SELECT * FROM ELEVES WHERE NOT (age < 16);

-- Recherche de motifs
SELECT * FROM ELEVES WHERE nom LIKE 'Dup%';     -- Commence par "Dup"
SELECT * FROM ELEVES WHERE nom LIKE '%ont';     -- Finit par "ont"
SELECT * FROM ELEVES WHERE nom LIKE '%ar%';     -- Contient "ar"
SELECT * FROM ELEVES WHERE nom LIKE 'M_rtin';   -- M suivi d'un caractère puis "rtin"

-- Listes de valeurs
SELECT * FROM ELEVES WHERE age IN (16, 17, 18);
SELECT * FROM ELEVES WHERE nom NOT IN ('Dupont', 'Martin');
```

#### Fonctions d'agrégation

```sql
-- Fonctions de base
SELECT COUNT(*) FROM ELEVES;                    -- Nombre total
SELECT COUNT(email) FROM ELEVES;                -- Nombre de non-NULL
SELECT AVG(age) FROM ELEVES;                    -- Moyenne
SELECT MIN(age), MAX(age) FROM ELEVES;          -- Min et max
SELECT SUM(age) FROM ELEVES;                    -- Somme

-- Avec conditions
SELECT COUNT(*) FROM ELEVES WHERE age > 17;
SELECT AVG(moyenne) FROM ELEVES WHERE moyenne IS NOT NULL;
```

#### GROUP BY - Regroupement

```sql
-- Nombre d'élèves par âge
SELECT age, COUNT(*) AS nombre_eleves
FROM ELEVES
GROUP BY age;

-- Moyenne des notes par matière
SELECT matiere, AVG(note) AS moyenne_matiere
FROM NOTES
GROUP BY matiere;

-- Avec plusieurs colonnes
SELECT age, COUNT(*) AS nombre,
       AVG(moyenne) AS moyenne_age
FROM ELEVES
WHERE moyenne IS NOT NULL
GROUP BY age;
```

#### HAVING - Filtrage après regroupement

```sql
-- Âges avec plus de 2 élèves
SELECT age, COUNT(*) AS nombre
FROM ELEVES
GROUP BY age
HAVING COUNT(*) > 2;

-- Matières avec moyenne > 12
SELECT matiere, AVG(note) AS moyenne
FROM NOTES
GROUP BY matiere
HAVING AVG(note) > 12;
```

#### ORDER BY - Tri

```sql
-- Tri simple
SELECT * FROM ELEVES ORDER BY nom;              -- Croissant par défaut
SELECT * FROM ELEVES ORDER BY age DESC;         -- Décroissant

-- Tri multiple
SELECT * FROM ELEVES ORDER BY age DESC, nom ASC;

-- Tri avec calcul
SELECT nom, prenom, moyenne
FROM ELEVES
ORDER BY moyenne DESC NULLS LAST;               -- NULL à la fin
```

#### LIMIT - Limitation du nombre de résultats

```sql
-- Les 5 premiers
SELECT * FROM ELEVES ORDER BY moyenne DESC LIMIT 5;

-- Pagination (OFFSET)
SELECT * FROM ELEVES ORDER BY nom LIMIT 10 OFFSET 20;  -- Résultats 21-30
```

### Jointures

#### Types de jointures

**INNER JOIN - Jointure interne :**
```sql
-- Élèves avec leurs notes
SELECT e.nom, e.prenom, n.matiere, n.note
FROM ELEVES e
INNER JOIN NOTES n ON e.id_eleve = n.id_eleve;

-- Syntaxe alternative (implicite)
SELECT e.nom, e.prenom, n.matiere, n.note
FROM ELEVES e, NOTES n
WHERE e.id_eleve = n.id_eleve;
```

**LEFT JOIN - Jointure externe gauche :**
```sql
-- Tous les élèves, avec leurs notes si elles existent
SELECT e.nom, e.prenom, n.matiere, n.note
FROM ELEVES e
LEFT JOIN NOTES n ON e.id_eleve = n.id_eleve;
```

**RIGHT JOIN - Jointure externe droite :**
```sql
-- Toutes les notes, avec les élèves si ils existent
SELECT e.nom, e.prenom, n.matiere, n.note
FROM ELEVES e
RIGHT JOIN NOTES n ON e.id_eleve = n.id_eleve;
```

**FULL OUTER JOIN - Jointure externe complète :**
```sql
-- Tous les élèves et toutes les notes
SELECT e.nom, e.prenom, n.matiere, n.note
FROM ELEVES e
FULL OUTER JOIN NOTES n ON e.id_eleve = n.id_eleve;
```

#### Jointures multiples

```sql
-- Trois tables : ELEVES, CLASSES, PROFESSEURS
SELECT e.nom, e.prenom, c.nom_classe, p.nom_prof
FROM ELEVES e
INNER JOIN CLASSES c ON e.id_classe = c.id_classe
INNER JOIN PROFESSEURS p ON c.id_prof = p.id_prof;
```

#### Auto-jointure

```sql
-- Élèves du même âge
SELECT e1.nom AS eleve1, e2.nom AS eleve2, e1.age
FROM ELEVES e1
INNER JOIN ELEVES e2 ON e1.age = e2.age AND e1.id_eleve < e2.id_eleve;
```

### Sous-requêtes

#### Sous-requête scalaire

```sql
-- Élèves avec une moyenne supérieure à la moyenne générale
SELECT nom, prenom, moyenne
FROM ELEVES
WHERE moyenne > (SELECT AVG(moyenne) FROM ELEVES WHERE moyenne IS NOT NULL);
```

#### Sous-requête avec IN

```sql
-- Élèves qui ont des notes en mathématiques
SELECT nom, prenom
FROM ELEVES
WHERE id_eleve IN (
    SELECT DISTINCT id_eleve 
    FROM NOTES 
    WHERE matiere = 'Mathématiques'
);
```

#### Sous-requête avec EXISTS

```sql
-- Élèves qui ont au moins une note
SELECT nom, prenom
FROM ELEVES e
WHERE EXISTS (
    SELECT 1 FROM NOTES n WHERE n.id_eleve = e.id_eleve
);

-- Élèves qui n'ont aucune note
SELECT nom, prenom
FROM ELEVES e
WHERE NOT EXISTS (
    SELECT 1 FROM NOTES n WHERE n.id_eleve = e.id_eleve
);
```

#### Sous-requête corrélée

```sql
-- Élèves avec leur meilleure note
SELECT e.nom, e.prenom, 
       (SELECT MAX(note) FROM NOTES n WHERE n.id_eleve = e.id_eleve) AS meilleure_note
FROM ELEVES e;
```

### UPDATE - Modification des données

```sql
-- Modification simple
UPDATE ELEVES 
SET email = 'marie.dupont@email.com' 
WHERE id_eleve = 1;

-- Modification multiple
UPDATE ELEVES 
SET moyenne = 15.5, age = 18 
WHERE nom = 'Martin';

-- Modification avec calcul
UPDATE ELEVES 
SET moyenne = (
    SELECT AVG(note) 
    FROM NOTES 
    WHERE NOTES.id_eleve = ELEVES.id_eleve
)
WHERE id_eleve IN (SELECT DISTINCT id_eleve FROM NOTES);

-- Modification conditionnelle
UPDATE NOTES 
SET note = note + 1 
WHERE note < 20 AND matiere = 'Mathématiques';
```

### DELETE - Suppression des données

```sql
-- Suppression simple
DELETE FROM NOTES WHERE note < 5;

-- Suppression avec sous-requête
DELETE FROM ELEVES 
WHERE id_eleve NOT IN (
    SELECT DISTINCT id_eleve FROM NOTES
);

-- Suppression de tous les enregistrements
DELETE FROM NOTES;  -- Attention !

-- Suppression avec jointure (syntaxe dépendante du SGBD)
DELETE n FROM NOTES n
INNER JOIN ELEVES e ON n.id_eleve = e.id_eleve
WHERE e.age < 16;
```

---

## Fonctions SQL avancées

### Fonctions de chaînes

```sql
-- Manipulation de texte
SELECT 
    UPPER(nom) AS nom_majuscule,
    LOWER(prenom) AS prenom_minuscule,
    LENGTH(nom) AS longueur_nom,
    SUBSTR(nom, 1, 3) AS trois_premieres_lettres,
    CONCAT(prenom, ' ', nom) AS nom_complet
FROM ELEVES;

-- Recherche et remplacement
SELECT 
    REPLACE(email, '@email.com', '@ecole.fr') AS nouvel_email,
    TRIM(nom) AS nom_sans_espaces
FROM ELEVES;
```

### Fonctions de date

```sql
-- Manipulation de dates
SELECT 
    nom,
    date_naissance,
    YEAR(CURRENT_DATE) - YEAR(date_naissance) AS age_calcule,
    DATE_ADD(date_naissance, INTERVAL 18 YEAR) AS majorite,
    DATEDIFF(CURRENT_DATE, date_naissance) AS jours_depuis_naissance
FROM ELEVES;

-- Extraction de parties de date
SELECT 
    YEAR(date_evaluation) AS annee,
    MONTH(date_evaluation) AS mois,
    DAY(date_evaluation) AS jour,
    DAYNAME(date_evaluation) AS jour_semaine
FROM NOTES;
```

### Fonctions conditionnelles

```sql
-- CASE WHEN
SELECT 
    nom, prenom, moyenne,
    CASE 
        WHEN moyenne >= 16 THEN 'Très bien'
        WHEN moyenne >= 14 THEN 'Bien'
        WHEN moyenne >= 12 THEN 'Assez bien'
        WHEN moyenne >= 10 THEN 'Passable'
        ELSE 'Insuffisant'
    END AS mention
FROM ELEVES
WHERE moyenne IS NOT NULL;

-- IF (MySQL) ou IIF (SQL Server)
SELECT 
    nom, prenom,
    IF(moyenne >= 10, 'Admis', 'Refusé') AS resultat
FROM ELEVES;

-- COALESCE (valeur par défaut)
SELECT 
    nom, prenom,
    COALESCE(moyenne, 0) AS moyenne_ou_zero
FROM ELEVES;
```

### Fonctions de fenêtrage (Window Functions)

```sql
-- Rang et numérotation
SELECT 
    nom, prenom, moyenne,
    ROW_NUMBER() OVER (ORDER BY moyenne DESC) AS numero_ligne,
    RANK() OVER (ORDER BY moyenne DESC) AS rang,
    DENSE_RANK() OVER (ORDER BY moyenne DESC) AS rang_dense
FROM ELEVES
WHERE moyenne IS NOT NULL;

-- Fonctions d'agrégation avec fenêtrage
SELECT 
    nom, prenom, age, moyenne,
    AVG(moyenne) OVER (PARTITION BY age) AS moyenne_par_age,
    COUNT(*) OVER (PARTITION BY age) AS nombre_meme_age
FROM ELEVES
WHERE moyenne IS NOT NULL;

-- Valeurs précédentes/suivantes
SELECT 
    nom, prenom, moyenne,
    LAG(moyenne, 1) OVER (ORDER BY moyenne) AS moyenne_precedente,
    LEAD(moyenne, 1) OVER (ORDER BY moyenne) AS moyenne_suivante
FROM ELEVES
WHERE moyenne IS NOT NULL;
```

---

## Vues

### Création de vues

```sql
-- Vue simple
CREATE VIEW vue_eleves_majeurs AS
SELECT id_eleve, nom, prenom, age, moyenne
FROM ELEVES
WHERE age >= 18;

-- Vue avec jointure
CREATE VIEW vue_notes_detaillees AS
SELECT 
    e.nom, e.prenom, 
    n.matiere, n.note, n.date_evaluation
FROM ELEVES e
INNER JOIN NOTES n ON e.id_eleve = n.id_eleve;

-- Vue avec agrégation
CREATE VIEW vue_moyennes_par_matiere AS
SELECT 
    matiere,
    COUNT(*) AS nombre_notes,
    AVG(note) AS moyenne,
    MIN(note) AS note_min,
    MAX(note) AS note_max
FROM NOTES
GROUP BY matiere;
```

### Utilisation des vues

```sql
-- Utilisation comme une table normale
SELECT * FROM vue_eleves_majeurs;

SELECT nom, prenom FROM vue_eleves_majeurs WHERE moyenne > 15;

-- Jointure avec d'autres tables/vues
SELECT v.nom, v.prenom, vm.moyenne AS moyenne_matiere
FROM vue_eleves_majeurs v
INNER JOIN vue_notes_detaillees vn ON v.nom = vn.nom AND v.prenom = vn.prenom
INNER JOIN vue_moyennes_par_matiere vm ON vn.matiere = vm.matiere;
```

### Modification et suppression de vues

```sql
-- Modifier une vue
CREATE OR REPLACE VIEW vue_eleves_majeurs AS
SELECT id_eleve, nom, prenom, age, moyenne, email
FROM ELEVES
WHERE age >= 18;

-- Supprimer une vue
DROP VIEW vue_eleves_majeurs;
```

---

## Index et optimisation

### Création d'index

```sql
-- Index simple
CREATE INDEX idx_eleves_nom ON ELEVES(nom);

-- Index composé
CREATE INDEX idx_notes_eleve_matiere ON NOTES(id_eleve, matiere);

-- Index unique
CREATE UNIQUE INDEX idx_eleves_email ON ELEVES(email);

-- Index partiel (avec condition)
CREATE INDEX idx_notes_bonnes ON NOTES(note) WHERE note >= 15;
```

### Analyse des performances

```sql
-- Plan d'exécution (syntaxe varie selon le SGBD)
EXPLAIN SELECT * FROM ELEVES WHERE nom = 'Dupont';

EXPLAIN QUERY PLAN 
SELECT e.nom, AVG(n.note)
FROM ELEVES e
INNER JOIN NOTES n ON e.id_eleve = n.id_eleve
GROUP BY e.nom;
```

---

## Transactions

### Gestion des transactions

```sql
-- Transaction simple
BEGIN TRANSACTION;
    INSERT INTO ELEVES (id_eleve, nom, prenom, age) 
    VALUES (10, 'Nouveau', 'Élève', 17);
    
    INSERT INTO NOTES (id_note, id_eleve, matiere, note, date_evaluation)
    VALUES (100, 10, 'Mathématiques', 15, '2024-01-15');
COMMIT;

-- Transaction avec gestion d'erreur
BEGIN TRANSACTION;
    UPDATE ELEVES SET moyenne = 18 WHERE id_eleve = 1;
    
    -- Si une erreur survient
    -- ROLLBACK;  -- Annule toutes les modifications
    
    -- Si tout va bien
    COMMIT;  -- Valide toutes les modifications
```

### Points de sauvegarde

```sql
BEGIN TRANSACTION;
    INSERT INTO ELEVES (id_eleve, nom, prenom, age) VALUES (11, 'Test1', 'Élève', 17);
    
    SAVEPOINT point1;
    
    INSERT INTO ELEVES (id_eleve, nom, prenom, age) VALUES (12, 'Test2', 'Élève', 17);
    
    -- Retour au point de sauvegarde
    ROLLBACK TO point1;
    
    INSERT INTO ELEVES (id_eleve, nom, prenom, age) VALUES (13, 'Test3', 'Élève', 17);
    
COMMIT;
```

---

## Exemples pratiques complets

### Base de données d'une bibliothèque

```sql
-- Création des tables
CREATE TABLE AUTEURS (
    id_auteur INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE,
    nationalite VARCHAR(50)
);

CREATE TABLE LIVRES (
    id_livre INTEGER PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    date_publication DATE,
    genre VARCHAR(50),
    nb_pages INTEGER CHECK (nb_pages > 0)
);

CREATE TABLE ECRIRE (
    id_auteur INTEGER,
    id_livre INTEGER,
    role VARCHAR(50) DEFAULT 'auteur',
    PRIMARY KEY (id_auteur, id_livre),
    FOREIGN KEY (id_auteur) REFERENCES AUTEURS(id_auteur),
    FOREIGN KEY (id_livre) REFERENCES LIVRES(id_livre)
);

CREATE TABLE EMPRUNTEURS (
    id_emprunteur INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    date_inscription DATE NOT NULL
);

CREATE TABLE EMPRUNTS (
    id_emprunt INTEGER PRIMARY KEY,
    id_livre INTEGER NOT NULL,
    id_emprunteur INTEGER NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    FOREIGN KEY (id_livre) REFERENCES LIVRES(id_livre),
    FOREIGN KEY (id_emprunteur) REFERENCES EMPRUNTEURS(id_emprunteur)
);

-- Insertion de données de test
INSERT INTO AUTEURS VALUES
    (1, 'Hugo', 'Victor', '1802-02-26', 'Française'),
    (2, 'Camus', 'Albert', '1913-11-07', 'Française'),
    (3, 'Orwell', 'George', '1903-06-25', 'Britannique');

INSERT INTO LIVRES VALUES
    (1, 'Les Misérables', '9782070409228', '1862-01-01', 'Roman', 1232),
    (2, 'L\'Étranger', '9782070360024', '1942-01-01', 'Roman', 186),
    (3, '1984', '9782070368228', '1949-01-01', 'Science-fiction', 376);

INSERT INTO ECRIRE VALUES
    (1, 1, 'auteur'),
    (2, 2, 'auteur'),
    (3, 3, 'auteur');

INSERT INTO EMPRUNTEURS VALUES
    (1, 'Dupont', 'Marie', 'marie.dupont@email.com', '2023-09-01'),
    (2, 'Martin', 'Paul', 'paul.martin@email.com', '2023-10-15');

INSERT INTO EMPRUNTS VALUES
    (1, 1, 1, '2024-01-10', '2024-01-24', '2024-01-20'),
    (2, 2, 1, '2024-01-15', '2024-01-29', NULL),
    (3, 3, 2, '2024-01-12', '2024-01-26', NULL);
```

### Requêtes d'analyse

```sql
-- 1. Livres actuellement empruntés
SELECT l.titre, a.nom, a.prenom, e.nom AS emprunteur_nom, 
       emp.date_emprunt, emp.date_retour_prevue
FROM LIVRES l
INNER JOIN EMPRUNTS emp ON l.id_livre = emp.id_livre
INNER JOIN EMPRUNTEURS e ON emp.id_emprunteur = e.id_emprunteur
INNER JOIN ECRIRE ec ON l.id_livre = ec.id_livre
INNER JOIN AUTEURS a ON ec.id_auteur = a.id_auteur
WHERE emp.date_retour_effective IS NULL;

-- 2. Emprunteurs en retard
SELECT e.nom, e.prenom, l.titre, emp.date_retour_prevue,
       DATEDIFF(CURRENT_DATE, emp.date_retour_prevue) AS jours_retard
FROM EMPRUNTEURS e
INNER JOIN EMPRUNTS emp ON e.id_emprunteur = emp.id_emprunteur
INNER JOIN LIVRES l ON emp.id_livre = l.id_livre
WHERE emp.date_retour_effective IS NULL 
  AND emp.date_retour_prevue < CURRENT_DATE;

-- 3. Statistiques par genre
SELECT l.genre, 
       COUNT(*) AS nombre_livres,
       COUNT(emp.id_emprunt) AS nombre_emprunts,
       AVG(l.nb_pages) AS pages_moyennes
FROM LIVRES l
LEFT JOIN EMPRUNTS emp ON l.id_livre = emp.id_livre
GROUP BY l.genre
ORDER BY nombre_emprunts DESC;

-- 4. Top 5 des emprunteurs les plus actifs
SELECT e.nom, e.prenom, COUNT(emp.id_emprunt) AS nombre_emprunts
FROM EMPRUNTEURS e
INNER JOIN EMPRUNTS emp ON e.id_emprunteur = emp.id_emprunteur
GROUP BY e.id_emprunteur, e.nom, e.prenom
ORDER BY nombre_emprunts DESC
LIMIT 5;

-- 5. Livres jamais empruntés
SELECT l.titre, a.nom AS auteur_nom, a.prenom AS auteur_prenom
FROM LIVRES l
INNER JOIN ECRIRE ec ON l.id_livre = ec.id_livre
INNER JOIN AUTEURS a ON ec.id_auteur = a.id_auteur
WHERE l.id_livre NOT IN (
    SELECT DISTINCT id_livre FROM EMPRUNTS
);
```

---

## Exercices pratiques

### Exercice 1 : Système de gestion d'école

Créez une base de données pour gérer :
- Les élèves (nom, prénom, date de naissance, classe)
- Les professeurs (nom, prénom, matière principale)
- Les matières (nom, coefficient)
- Les notes (élève, matière, note, date)
- Les classes (nom, niveau, professeur principal)

**Questions :**
1. Écrivez les instructions CREATE TABLE
2. Insérez des données de test
3. Trouvez la moyenne générale de chaque élève
4. Listez les élèves ayant une moyenne > 15
5. Trouvez le professeur ayant le plus d'élèves

### Exercice 2 : E-commerce

Modélisez un système de vente en ligne :
- Clients, produits, commandes, lignes de commande
- Catégories de produits
- Historique des prix

**Requêtes à implémenter :**
1. Chiffre d'affaires par mois
2. Produits les plus vendus
3. Clients les plus fidèles
4. Panier moyen par client
5. Évolution des prix d'un produit

### Exercice 3 : Optimisation

À partir d'une base existante :
1. Identifiez les requêtes lentes avec EXPLAIN
2. Créez les index appropriés
3. Réécrivez les requêtes pour améliorer les performances
4. Créez des vues pour simplifier les requêtes complexes

---

## Bonnes pratiques

### Nommage
- **Tables** : noms au pluriel (ELEVES, COMMANDES)
- **Colonnes** : noms explicites (date_naissance, prix_unitaire)
- **Clés primaires** : id_table (id_eleve, id_commande)
- **Clés étrangères** : même nom que la clé primaire référencée
- **Index** : préfixe idx_ (idx_eleves_nom)

### Performance
- Utilisez des index sur les colonnes fréquemment utilisées dans WHERE
- Évitez SELECT * en production
- Utilisez LIMIT pour les grandes tables
- Préférez EXISTS à IN pour les sous-requêtes
- Analysez les plans d'exécution

### Sécurité
- Utilisez des requêtes préparées pour éviter l'injection SQL
- Accordez les privilèges minimums nécessaires
- Chiffrez les données sensibles
- Sauvegardez régulièrement

### Maintenance
- Documentez vos schémas
- Utilisez des transactions pour les opérations critiques
- Testez vos requêtes sur des données de test
- Surveillez les performances

---

## Conclusion

SQL est un langage puissant et standardisé qui permet :
- **Définition** : CREATE, ALTER, DROP
- **Manipulation** : SELECT, INSERT, UPDATE, DELETE
- **Contrôle** : transactions, contraintes, index
- **Analyse** : fonctions d'agrégation, jointures, sous-requêtes

La maîtrise de SQL est essentielle pour travailler efficacement avec les bases de données relationnelles, qui restent au cœur de la plupart des systèmes d'information.