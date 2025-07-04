# Exercices SQL - Bases de données

## Schéma de la base de données

📊 Base de données : Bibliothèque

**Table AUTEURS**
- `id_auteur` (INTEGER, PK) : Identifiant unique
- `nom` (VARCHAR(50)) : Nom de famille
- `prenom` (VARCHAR(50)) : Prénom
- `date_naissance` (DATE) : Date de naissance
- `nationalite` (VARCHAR(30)) : Nationalité

**Table LIVRES**
- `isbn` (VARCHAR(17), PK) : Code ISBN
- `titre` (VARCHAR(200)) : Titre du livre
- `id_auteur` (INTEGER, FK) : Référence vers AUTEURS
- `annee_publication` (INTEGER) : Année de publication
- `nb_pages` (INTEGER) : Nombre de pages
- `genre` (VARCHAR(50)) : Genre littéraire

**Table LECTEURS**
- `id_lecteur` (INTEGER, PK) : Identifiant unique
- `nom` (VARCHAR(50)) : Nom de famille
- `prenom` (VARCHAR(50)) : Prénom
- `email` (VARCHAR(100)) : Adresse email
- `date_inscription` (DATE) : Date d'inscription

**Table EMPRUNTS**
- `id_emprunt` (INTEGER, PK) : Identifiant unique
- `isbn` (VARCHAR(17), FK) : Référence vers LIVRES
- `id_lecteur` (INTEGER, FK) : Référence vers LECTEURS
- `date_emprunt` (DATE) : Date d'emprunt
- `date_retour_prevue` (DATE) : Date de retour prévue
- `date_retour_effective` (DATE) : Date de retour effective (NULL si non rendu)

## Exercices

    Requêtes de base
    Jointures
    Agrégation
    Avancé

Exercice 1 : Sélections simples
Facile

**Questions :**

1. Affichez tous les livres de la base de données.
2. Affichez uniquement les titres et années de publication des livres.
3. Trouvez tous les livres publiés après 2000.
4. Listez tous les auteurs français.
5. Affichez les livres de science-fiction de plus de 300 pages.

Voir la solution

```sql
-- 1. Tous les livres
SELECT * FROM livres;

-- 2. Titres et années
SELECT titre, annee_publication FROM livres;

-- 3. Livres après 2000
SELECT * FROM livres WHERE annee_publication > 2000;

-- 4. Auteurs français
SELECT * FROM auteurs WHERE nationalite = 'Française';

-- 5. Science-fiction > 300 pages
SELECT * FROM livres
WHERE genre = 'Science-fiction' AND nb_pages > 300;
```

Exercice 2 : Tri et limitation
Facile

**Questions :**

1. Affichez les livres triés par année de publication (du plus récent au plus ancien).
2. Trouvez les 5 livres les plus longs.
3. Listez les auteurs par ordre alphabétique de nom.
4. Affichez les 10 premiers emprunts par date.

Voir la solution

```sql
-- 1. Livres par année (récent → ancien)
SELECT * FROM livres ORDER BY annee_publication DESC;

-- 2. 5 livres les plus longs
SELECT titre, nb_pages FROM livres
ORDER BY nb_pages DESC LIMIT 5;

-- 3. Auteurs par ordre alphabétique
SELECT * FROM auteurs ORDER BY nom, prenom;

-- 4. 10 premiers emprunts
SELECT * FROM emprunts
ORDER BY date_emprunt LIMIT 10;
```

Exercice 3 : Jointures simples
Moyen

**Questions :**

1. Affichez les livres avec le nom complet de leur auteur.
2. Listez tous les emprunts avec le titre du livre emprunté.
3. Trouvez les emprunts en cours avec les détails du lecteur.
4. Affichez tous les auteurs, même ceux qui n'ont pas écrit de livres.

Voir la solution

```sql
-- 1. Livres avec auteurs
SELECT l.titre, a.nom, a.prenom
FROM livres l
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur;

-- 2. Emprunts avec titres
SELECT e.date_emprunt, l.titre
FROM emprunts e
INNER JOIN livres l ON e.isbn = l.isbn;

-- 3. Emprunts en cours avec lecteurs
SELECT e.date_emprunt, l.titre, lec.nom, lec.prenom
FROM emprunts e
INNER JOIN livres l ON e.isbn = l.isbn
INNER JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
WHERE e.date_retour_effective IS NULL;

-- 4. Tous les auteurs (même sans livres)
SELECT a.nom, a.prenom, l.titre
FROM auteurs a
LEFT JOIN livres l ON a.id_auteur = l.id_auteur;
```

Exercice 4 : Jointures complexes
Moyen

**Questions :**

1. Affichez tous les emprunts avec les détails complets (lecteur, livre, auteur).
2. Trouvez les lecteurs qui n'ont jamais emprunté de livre.
3. Listez les livres jamais empruntés.
4. Affichez les emprunts en retard avec toutes les informations.

Voir la solution

```sql
-- 1. Emprunts avec détails complets
SELECT
    lec.nom AS lecteur_nom,
    lec.prenom AS lecteur_prenom,
    l.titre,
    a.nom AS auteur_nom,
    a.prenom AS auteur_prenom,
    e.date_emprunt,
    e.date_retour_prevue
FROM emprunts e
INNER JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
INNER JOIN livres l ON e.isbn = l.isbn
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur;

-- 2. Lecteurs sans emprunts
SELECT lec.nom, lec.prenom
FROM lecteurs lec
LEFT JOIN emprunts e ON lec.id_lecteur = e.id_lecteur
WHERE e.id_lecteur IS NULL;

-- 3. Livres jamais empruntés
SELECT l.titre, a.nom, a.prenom
FROM livres l
INNER JOIN auteurs a ON l.id_auteur = a.id_auteur
LEFT JOIN emprunts e ON l.isbn = e.isbn
WHERE e.isbn IS NULL;

-- 4. Emprunts en retard
SELECT
    lec.nom,
    lec.prenom,
    l.titre,
    e.date_retour_prevue,
    (julianday('now') - julianday(e.date_retour_prevue)) AS jours_retard
FROM emprunts e
INNER JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
INNER JOIN livres l ON e.isbn = l.isbn
WHERE e.date_retour_effective IS NULL
  AND e.date_retour_prevue

Exercice 5 : Fonctions d'agrégation
Moyen

**Questions :**

1. Comptez le nombre total de livres dans la base.
2. Trouvez le nombre moyen de pages par livre.
3. Affichez l'année de publication la plus ancienne et la plus récente.
4. Comptez le nombre de livres par genre.
5. Trouvez le genre avec le plus de livres.

Voir la solution

```sql
-- 1. Nombre total de livres
SELECT COUNT(*) AS nombre_livres FROM livres;

-- 2. Nombre moyen de pages
SELECT AVG(nb_pages) AS moyenne_pages FROM livres;

-- 3. Années min et max
SELECT
    MIN(annee_publication) AS plus_ancienne,
    MAX(annee_publication) AS plus_recente
FROM livres;

-- 4. Livres par genre
SELECT genre, COUNT(*) AS nombre_livres
FROM livres
GROUP BY genre
ORDER BY nombre_livres DESC;

-- 5. Genre avec le plus de livres
SELECT genre, COUNT(*) AS nombre_livres
FROM livres
GROUP BY genre
ORDER BY nombre_livres DESC
LIMIT 1;
```

Exercice 6 : GROUP BY et HAVING
Moyen

**Questions :**

1. Affichez le nombre de livres par auteur.
2. Trouvez les auteurs qui ont écrit plus de 3 livres.
3. Calculez le nombre moyen de pages par genre (genres avec plus de 2 livres).
4. Listez les lecteurs avec le nombre de leurs emprunts.
5. Trouvez les lecteurs qui ont emprunté plus de 5 livres.

Voir la solution

```sql
-- 1. Livres par auteur
SELECT
    a.nom,
    a.prenom,
    COUNT(l.isbn) AS nombre_livres
FROM auteurs a
LEFT JOIN livres l ON a.id_auteur = l.id_auteur
GROUP BY a.id_auteur, a.nom, a.prenom
ORDER BY nombre_livres DESC;

-- 2. Auteurs avec plus de 3 livres
SELECT
    a.nom,
    a.prenom,
    COUNT(l.isbn) AS nombre_livres
FROM auteurs a
INNER JOIN livres l ON a.id_auteur = l.id_auteur
GROUP BY a.id_auteur, a.nom, a.prenom
HAVING COUNT(l.isbn) > 3;

-- 3. Moyenne pages par genre (>2 livres)
SELECT
    genre,
    COUNT(*) AS nombre_livres,
    AVG(nb_pages) AS moyenne_pages
FROM livres
GROUP BY genre
HAVING COUNT(*) > 2;

-- 4. Emprunts par lecteur
SELECT
    lec.nom,
    lec.prenom,
    COUNT(e.id_emprunt) AS nombre_emprunts
FROM lecteurs lec
LEFT JOIN emprunts e ON lec.id_lecteur = e.id_lecteur
GROUP BY lec.id_lecteur, lec.nom, lec.prenom;

-- 5. Lecteurs avec plus de 5 emprunts
SELECT
    lec.nom,
    lec.prenom,
    COUNT(e.id_emprunt) AS nombre_emprunts
FROM lecteurs lec
INNER JOIN emprunts e ON lec.id_lecteur = e.id_lecteur
GROUP BY lec.id_lecteur, lec.nom, lec.prenom
HAVING COUNT(e.id_emprunt) > 5;
```

Exercice 7 : Sous-requêtes
Difficile

**Questions :**

1. Trouvez les livres plus longs que la moyenne.
2. Affichez les auteurs qui ont écrit le plus de livres.
3. Listez les livres de l'auteur le plus prolifique.
4. Trouvez les lecteurs qui ont emprunté des livres de science-fiction.

Voir la solution

```sql
-- 1. Livres plus longs que la moyenne
SELECT titre, nb_pages
FROM livres
WHERE nb_pages > (SELECT AVG(nb_pages) FROM livres);

-- 2. Auteurs avec le plus de livres
SELECT a.nom, a.prenom, COUNT(l.isbn) AS nombre_livres
FROM auteurs a
INNER JOIN livres l ON a.id_auteur = l.id_auteur
GROUP BY a.id_auteur, a.nom, a.prenom
HAVING COUNT(l.isbn) = (
    SELECT MAX(nb_livres)
    FROM (
        SELECT COUNT(isbn) AS nb_livres
        FROM livres
        GROUP BY id_auteur
    )
);

-- 3. Livres de l'auteur le plus prolifique
SELECT titre
FROM livres
WHERE id_auteur = (
    SELECT id_auteur
    FROM livres
    GROUP BY id_auteur
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 4. Lecteurs ayant emprunté de la science-fiction
SELECT DISTINCT lec.nom, lec.prenom
FROM lecteurs lec
INNER JOIN emprunts e ON lec.id_lecteur = e.id_lecteur
WHERE e.isbn IN (
    SELECT isbn
    FROM livres
    WHERE genre = 'Science-fiction'
);
```

Exercice 8 : Requêtes complexes
Difficile

**Questions :**

1. Trouvez les livres qui n'ont jamais été empruntés par des lecteurs inscrits avant 2020.
2. Affichez les genres où tous les livres ont été empruntés au moins une fois.
3. Listez les auteurs dont tous les livres font plus de 200 pages.
4. Trouvez les lecteurs qui ont emprunté des livres de tous les genres disponibles.

Voir la solution

```sql
-- 1. Livres jamais empruntés par lecteurs pré-2020
SELECT l.titre
FROM livres l
WHERE l.isbn NOT IN (
    SELECT DISTINCT e.isbn
    FROM emprunts e
    INNER JOIN lecteurs lec ON e.id_lecteur = lec.id_lecteur
    WHERE lec.date_inscription  200 pages
SELECT a.nom, a.prenom
FROM auteurs a
WHERE NOT EXISTS (
    SELECT 1
    FROM livres l
    WHERE l.id_auteur = a.id_auteur
      AND l.nb_pages

## Projet pratique

Projet : Système de recommandation
Projet

**Objectif :** Créer des requêtes pour un système de recommandation de livres.

**Fonctionnalités à implémenter :**

1. **Livres similaires** : Trouvez les livres du même genre et de la même époque (±10 ans)
2. **Auteurs populaires** : Classez les auteurs par nombre d'emprunts de leurs livres
3. **Tendances** : Identifiez les genres les plus empruntés par mois
4. **Recommandations personnalisées** : Pour un lecteur donné, suggérez des livres basés sur ses emprunts précédents

**Bonus :**
- Créez des vues pour simplifier les requêtes complexes
- Ajoutez des index pour optimiser les performances
- Implémentez des procédures stockées (si votre SGBD le permet)