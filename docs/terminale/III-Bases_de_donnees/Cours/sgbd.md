# Systèmes de Gestion de Bases de Données (SGBD)

## Introduction

Un **Système de Gestion de Bases de Données** (SGBD) est un logiciel qui permet de :
- **Créer** et **organiser** des bases de données
- **Stocker**, **modifier** et **extraire** des informations
- **Gérer** les accès concurrents et la sécurité
- **Assurer** l'intégrité et la cohérence des données

## Fonctionnalités principales d'un SGBD

### 1. Gestion des données

- **Stockage physique** : Organisation des données sur les supports de stockage
- **Indexation** : Création d'index pour accélérer les recherches
- **Compression** : Optimisation de l'espace de stockage

### 2. Gestion des transactions

Une **transaction** est une séquence d'opérations qui doit être exécutée de manière atomique.

**Propriétés ACID :**
- **Atomicité** : Tout ou rien (all or nothing)
- **Cohérence** : Respect des contraintes d'intégrité
- **Isolation** : Les transactions concurrentes n'interfèrent pas
- **Durabilité** : Les modifications sont permanentes

```python
# Exemple conceptuel de transaction
def transfert_argent(compte_source, compte_destination, montant):
    # Début de transaction
    try:
        # Opération 1 : Débiter le compte source
        debiter(compte_source, montant)
        
        # Opération 2 : Créditer le compte destination
        crediter(compte_destination, montant)
        
        # Valider la transaction (COMMIT)
        valider_transaction()
    except Exception:
        # Annuler la transaction (ROLLBACK)
        annuler_transaction()
```

### 3. Gestion de la concurrence

Plusieurs utilisateurs peuvent accéder simultanément à la base de données :

- **Verrous (Locks)** : Empêchent les accès concurrents conflictuels
- **Isolation des transactions** : Différents niveaux d'isolation
- **Détection des interblocages** : Résolution des situations de blocage mutuel

### 4. Sécurité et contrôle d'accès

- **Authentification** : Vérification de l'identité des utilisateurs
- **Autorisation** : Gestion des droits d'accès (lecture, écriture, modification)
- **Audit** : Traçabilité des opérations
- **Chiffrement** : Protection des données sensibles

### 5. Sauvegarde et récupération

- **Sauvegardes régulières** : Copies de sécurité des données
- **Journalisation** : Enregistrement des modifications
- **Récupération après panne** : Restauration de l'état cohérent

## Architecture d'un SGBD

### Architecture à trois niveaux (ANSI/SPARC)

```
┌─────────────────────────────────────┐
│           Niveau externe            │  ← Vues utilisateurs
│    (Schémas externes/Vues)          │
├─────────────────────────────────────┤
│          Niveau conceptuel          │  ← Schéma logique global
│      (Schéma conceptuel)            │
├─────────────────────────────────────┤
│          Niveau interne             │  ← Organisation physique
│       (Schéma interne)              │
└─────────────────────────────────────┘
```

#### Niveau externe
- **Vues utilisateurs** : Chaque utilisateur voit une partie de la base
- **Personnalisation** : Adaptation aux besoins spécifiques
- **Sécurité** : Masquage des données sensibles

#### Niveau conceptuel
- **Schéma global** : Description complète de la structure logique
- **Contraintes d'intégrité** : Règles de cohérence
- **Indépendance** : Séparation de la logique et du physique

#### Niveau interne
- **Organisation physique** : Stockage sur disque
- **Optimisation** : Index, partitionnement, clustering
- **Performance** : Stratégies d'accès aux données

## Types de SGBD

### SGBD Relationnels (SGBDR)

**Caractéristiques :**
- Basés sur le modèle relationnel
- Utilisation du langage SQL
- Respect des propriétés ACID

**Exemples :**
- **MySQL** : Open source, très populaire pour le web
- **PostgreSQL** : Open source, très complet et robuste
- **Oracle Database** : Commercial, haute performance
- **SQL Server** : Microsoft, intégration Windows
- **SQLite** : Embarqué, fichier unique

### SGBD NoSQL

**Types principaux :**

1. **Bases orientées documents** (MongoDB, CouchDB)
2. **Bases clé-valeur** (Redis, DynamoDB)
3. **Bases orientées colonnes** (Cassandra, HBase)
4. **Bases orientées graphes** (Neo4j, ArangoDB)

## Exemple pratique : SQLite

SQLite est un SGBD embarqué parfait pour l'apprentissage :

```python
import sqlite3

# Connexion à la base de données (création si inexistante)
connexion = sqlite3.connect('bibliotheque.db')
curseur = connexion.cursor()

# Création d'une table
curseur.execute('''
    CREATE TABLE IF NOT EXISTS livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        auteur TEXT NOT NULL,
        annee INTEGER,
        disponible BOOLEAN DEFAULT 1
    )
''')

# Insertion de données
livres_data = [
    ('1984', 'George Orwell', 1949),
    ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943),
    ('Dune', 'Frank Herbert', 1965)
]

curseur.executemany(
    'INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)',
    livres_data
)

# Validation des modifications
connexion.commit()

# Requête de sélection
curseur.execute('SELECT * FROM livres WHERE annee < 1950')
resultats = curseur.fetchall()

for livre in resultats:
    print(f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}")

# Fermeture de la connexion
connexion.close()
```

## Optimisation des performances

### Index

Les **index** accélérent les recherches :

```sql
-- Création d'un index sur la colonne 'auteur'
CREATE INDEX idx_auteur ON livres(auteur);

-- Index composé sur plusieurs colonnes
CREATE INDEX idx_auteur_annee ON livres(auteur, annee);
```

### Requêtes optimisées

```sql
-- Éviter SELECT *
SELECT titre, auteur FROM livres WHERE annee > 1950;

-- Utiliser LIMIT pour limiter les résultats
SELECT titre FROM livres ORDER BY annee DESC LIMIT 10;

-- Utiliser des jointures efficaces
SELECT l.titre, e.date_emprunt 
FROM livres l 
INNER JOIN emprunts e ON l.id = e.livre_id 
WHERE e.date_retour IS NULL;
```

## Sécurité des SGBD

### Injection SQL

**Problème :**
```python
# DANGEREUX - Vulnérable aux injections SQL
nom_utilisateur = input("Nom d'utilisateur: ")
requete = f"SELECT * FROM utilisateurs WHERE nom = '{nom_utilisateur}'"
curseur.execute(requete)
```

**Solution :**
```python
# SÉCURISÉ - Utilisation de paramètres
nom_utilisateur = input("Nom d'utilisateur: ")
requete = "SELECT * FROM utilisateurs WHERE nom = ?"
curseur.execute(requete, (nom_utilisateur,))
```

### Gestion des droits

```sql
-- Création d'un utilisateur
CREATE USER 'lecteur'@'localhost' IDENTIFIED BY 'mot_de_passe';

-- Attribution de droits spécifiques
GRANT SELECT ON bibliotheque.livres TO 'lecteur'@'localhost';

-- Révocation de droits
REVOKE INSERT ON bibliotheque.livres FROM 'lecteur'@'localhost';
```

## Exercices pratiques

### Exercice 1 : Analyse d'architecture

Pour chaque niveau de l'architecture ANSI/SPARC, donnez un exemple concret dans le contexte d'une base de données de gestion scolaire.

### Exercice 2 : Choix de SGBD

Pour chaque cas d'usage, justifiez le choix du SGBD :
1. Application mobile avec base de données locale
2. Site e-commerce avec forte charge
3. Système de gestion documentaire
4. Application d'analyse de réseaux sociaux

### Exercice 3 : Sécurité

Identifiez les failles de sécurité dans ce code Python :

```python
def authentifier_utilisateur(nom, mot_de_passe):
    connexion = sqlite3.connect('users.db')
    curseur = connexion.cursor()
    
    requete = f"SELECT id FROM users WHERE nom='{nom}' AND password='{mot_de_passe}'"
    curseur.execute(requete)
    
    if curseur.fetchone():
        return True
    return False
```

Proposez une version corrigée.

## Tendances actuelles

### Cloud et bases de données

- **Database as a Service (DBaaS)** : Amazon RDS, Google Cloud SQL
- **Bases de données serverless** : AWS Aurora Serverless
- **Multi-cloud** : Portabilité entre fournisseurs

### Big Data et analytique

- **Data Warehouses** : Stockage pour l'analyse
- **Data Lakes** : Stockage de données brutes
- **OLAP vs OLTP** : Optimisation pour l'analyse vs transactions

### Intelligence artificielle

- **Bases de données vectorielles** : Pour l'IA et le machine learning
- **Optimisation automatique** : Tuning automatique des performances
- **Requêtes en langage naturel** : Interface conversationnelle

## Conclusion

Les SGBD sont des outils essentiels dans le paysage informatique moderne. Leur évolution continue répond aux besoins croissants de :
- **Performance** : Gestion de volumes de données toujours plus importants
- **Disponibilité** : Systèmes fonctionnant 24h/24, 7j/7
- **Sécurité** : Protection contre les cyberattaques
- **Flexibilité** : Adaptation aux nouveaux types de données et d'usages

La maîtrise des concepts fondamentaux des SGBD est cruciale pour tout développeur ou administrateur de systèmes d'information.