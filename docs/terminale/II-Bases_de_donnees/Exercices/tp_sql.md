# TP SQL - Gestion d'une médiathèque

## Objectifs
- Créer et manipuler une base de données relationnelle
- Maîtriser les requêtes SQL (SELECT, INSERT, UPDATE, DELETE)
- Utiliser les jointures et les fonctions d'agrégation
- Analyser et optimiser les performances

---

## Partie 1 : Création de la base de données

### Contexte
Vous devez concevoir une base de données pour gérer une médiathèque qui prête des livres, DVD et CD.

### Analyse des besoins

**Entités identifiées :**
- **Adhérents** : personnes qui peuvent emprunter
- **Documents** : livres, DVD, CD disponibles
- **Auteurs/Réalisateurs/Artistes** : créateurs des documents
- **Emprunts** : historique des prêts
- **Catégories** : classification des documents

**Règles de gestion :**
- Un adhérent peut emprunter plusieurs documents
- Un document ne peut être emprunté que par un adhérent à la fois
- Un document peut avoir plusieurs auteurs/créateurs
- Durée d'emprunt : 3 semaines pour les livres, 1 semaine pour les DVD/CD
- Maximum 5 documents empruntés simultanément par adhérent

### Question 1 : Modélisation

**1.1** Dessinez le modèle conceptuel (entités-relations) sur papier.

**1.2** Créez les tables suivantes avec les contraintes appropriées :

```sql
-- Table CATEGORIES
CREATE TABLE CATEGORIES (
    -- À compléter
);

-- Table CREATEURS (auteurs, réalisateurs, artistes)
CREATE TABLE CREATEURS (
    -- À compléter
);

-- Table DOCUMENTS
CREATE TABLE DOCUMENTS (
    -- À compléter
);

-- Table ADHERENTS
CREATE TABLE ADHERENTS (
    -- À compléter
);

-- Table CREER (relation N-N entre DOCUMENTS et CREATEURS)
CREATE TABLE CREER (
    -- À compléter
);

-- Table EMPRUNTS
CREATE TABLE EMPRUNTS (
    -- À compléter
);
```

**Contraintes à respecter :**
- Clés primaires et étrangères
- Contraintes NOT NULL appropriées
- Contraintes CHECK (âge > 0, durée_emprunt > 0, etc.)
- Contraintes UNIQUE si nécessaire

### Question 2 : Insertion des données

**2.1** Insérez les catégories suivantes :
```sql
INSERT INTO CATEGORIES VALUES
    (1, 'Roman', 'Fiction littéraire'),
    (2, 'Science-Fiction', 'Littérature de science-fiction'),
    (3, 'Documentaire', 'Films documentaires'),
    (4, 'Action', 'Films d\'action'),
    (5, 'Musique Classique', 'Musique classique'),
    (6, 'Rock', 'Musique rock');
```

**2.2** Insérez au moins 10 créateurs (auteurs, réalisateurs, musiciens).

**2.3** Insérez au moins 15 documents de différents types :
- 8 livres
- 4 DVD
- 3 CD

**2.4** Insérez au moins 8 adhérents.

**2.5** Créez les relations entre documents et créateurs.

**2.6** Insérez quelques emprunts (en cours et terminés).

---

## Partie 2 : Requêtes de consultation

### Question 3 : Requêtes simples

**3.1** Affichez tous les documents disponibles (non empruntés) :
```sql
-- Votre requête ici
```

**3.2** Listez tous les adhérents majeurs (≥ 18 ans) :
```sql
-- Votre requête ici
```

**3.3** Trouvez tous les documents de science-fiction :
```sql
-- Votre requête ici
```

**3.4** Affichez les emprunts en retard (date de retour prévue dépassée) :
```sql
-- Votre requête ici
```

### Question 4 : Requêtes avec jointures

**4.1** Affichez tous les documents avec leurs créateurs :
```sql
-- Résultat attendu : titre, type, nom_createur, prenom_createur, role
```

**4.2** Listez les emprunts en cours avec les informations complètes :
```sql
-- Résultat attendu : nom_adherent, prenom_adherent, titre_document, 
--                   date_emprunt, date_retour_prevue
```

**4.3** Trouvez tous les livres de Victor Hugo :
```sql
-- Votre requête ici
```

**4.4** Affichez les adhérents qui n'ont jamais emprunté :
```sql
-- Votre requête ici
```

### Question 5 : Fonctions d'agrégation

**5.1** Comptez le nombre de documents par catégorie :
```sql
-- Résultat attendu : nom_categorie, nombre_documents
```

**5.2** Calculez l'âge moyen des adhérents :
```sql
-- Votre requête ici
```

**5.3** Trouvez le créateur le plus prolifique (le plus de documents) :
```sql
-- Votre requête ici
```

**5.4** Affichez le nombre d'emprunts par adhérent :
```sql
-- Résultat attendu : nom_adherent, prenom_adherent, nombre_emprunts
```

### Question 6 : Requêtes avancées

**6.1** Classez les documents par popularité (nombre d'emprunts) :
```sql
-- Résultat attendu : titre, type, nombre_emprunts
-- Triés par nombre d'emprunts décroissant
```

**6.2** Trouvez les adhérents ayant emprunté dans toutes les catégories :
```sql
-- Votre requête ici (difficile !)
```

**6.3** Calculez le taux d'occupation de la médiathèque :
```sql
-- Pourcentage de documents actuellement empruntés
```

**6.4** Affichez l'historique complet d'un document :
```sql
-- Pour un document donné, tous ses emprunts avec dates et adhérents
```

---

## Partie 3 : Vues et optimisation

### Question 7 : Création de vues

**7.1** Créez une vue `vue_documents_disponibles` :
```sql
CREATE VIEW vue_documents_disponibles AS
-- Votre requête ici
-- Doit afficher : id_document, titre, type, categorie, createurs
```

**7.2** Créez une vue `vue_emprunts_en_cours` :
```sql
CREATE VIEW vue_emprunts_en_cours AS
-- Votre requête ici
-- Doit afficher : adherent, document, dates, jours_restants
```

**7.3** Créez une vue `vue_statistiques_adherents` :
```sql
CREATE VIEW vue_statistiques_adherents AS
-- Votre requête ici
-- Doit afficher : adherent, nb_emprunts_total, nb_emprunts_en_cours, 
--                 date_dernier_emprunt
```

### Question 8 : Index et performance

**8.1** Analysez le plan d'exécution de cette requête :
```sql
EXPLAIN SELECT d.titre, a.nom, a.prenom
FROM DOCUMENTS d
JOIN EMPRUNTS e ON d.id_document = e.id_document
JOIN ADHERENTS a ON e.id_adherent = a.id_adherent
WHERE e.date_retour_effective IS NULL;
```

**8.2** Créez les index appropriés pour optimiser :
- Les recherches par titre de document
- Les recherches par nom d'adhérent
- Les jointures fréquentes
- Les requêtes sur les emprunts en cours

```sql
-- Vos instructions CREATE INDEX ici
```

**8.3** Mesurez l'amélioration des performances après création des index.

---

## Partie 4 : Procédures et fonctions

### Question 9 : Gestion des emprunts

**9.1** Écrivez une requête pour emprunter un document :
```sql
-- Fonction : emprunter_document(id_adherent, id_document)
-- Doit vérifier :
-- - Le document est disponible
-- - L'adhérent n'a pas déjà 5 emprunts en cours
-- - L'adhérent n'a pas de retard
-- Si OK, créer l'emprunt avec les bonnes dates
```

**9.2** Écrivez une requête pour retourner un document :
```sql
-- Fonction : retourner_document(id_emprunt)
-- Doit mettre à jour la date de retour effective
```

**9.3** Créez une requête pour calculer les amendes :
```sql
-- Fonction : calculer_amendes()
-- 0.50€ par jour de retard
-- Résultat : adherent, montant_amende, jours_retard
```

### Question 10 : Statistiques avancées

**10.1** Évolution des emprunts par mois :
```sql
-- Nombre d'emprunts par mois sur les 12 derniers mois
```

**10.2** Top 10 des documents les plus populaires :
```sql
-- Par catégorie et global
```

**10.3** Analyse des habitudes de lecture :
```sql
-- Catégories préférées par tranche d'âge
```

---

## Partie 5 : Maintenance et sécurité

### Question 11 : Contraintes et triggers

**11.1** Ajoutez une contrainte pour limiter les emprunts simultanés :
```sql
-- Maximum 5 emprunts en cours par adhérent
```

**11.2** Créez un trigger pour mettre à jour automatiquement le statut des documents :
```sql
-- Quand un emprunt est créé/terminé, 
-- mettre à jour le statut du document
```

**11.3** Ajoutez une table d'audit pour tracer les modifications :
```sql
CREATE TABLE AUDIT_EMPRUNTS (
    -- À compléter
);
-- Trigger pour enregistrer toutes les modifications
```

### Question 12 : Sauvegarde et restauration

**12.1** Écrivez les commandes pour :
- Sauvegarder la base complète
- Sauvegarder seulement les données
- Restaurer à partir d'une sauvegarde

**12.2** Planifiez une stratégie de sauvegarde :
- Fréquence des sauvegardes
- Rétention des sauvegardes
- Tests de restauration

---

## Partie 6 : Extensions et défis

### Question 13 : Fonctionnalités avancées

**13.1** Système de réservation :
```sql
-- Table RESERVATIONS
-- Permettre de réserver un document emprunté
-- Gérer la file d'attente
```

**13.2** Gestion des collections :
```sql
-- Table COLLECTIONS (séries, trilogies, etc.)
-- Relation avec DOCUMENTS
-- Requêtes pour afficher les collections complètes
```

**13.3** Système de recommandation :
```sql
-- Basé sur l'historique d'emprunts
-- "Les personnes qui ont emprunté X ont aussi emprunté Y"
```

### Question 14 : Interface web (optionnel)

**14.1** Créez une interface simple en HTML/CSS/JavaScript pour :
- Rechercher des documents
- Afficher les emprunts d'un adhérent
- Gérer les retours

**14.2** Utilisez une API REST pour connecter l'interface à la base :
- GET /documents (recherche)
- POST /emprunts (nouvel emprunt)
- PUT /emprunts/:id (retour)

---

## Barème et évaluation

### Critères d'évaluation

**Partie 1-2 (Base) - 8 points :**
- Modélisation correcte (2 pts)
- Création des tables avec contraintes (3 pts)
- Insertion des données (1 pt)
- Requêtes simples et jointures (2 pts)

**Partie 3-4 (Intermédiaire) - 6 points :**
- Vues bien conçues (2 pts)
- Index appropriés (2 pts)
- Requêtes avancées (2 pts)

**Partie 5-6 (Avancé) - 6 points :**
- Contraintes et triggers (2 pts)
- Optimisation et performance (2 pts)
- Extensions créatives (2 pts)

### Livrables attendus

1. **Script SQL complet** avec :
   - Création des tables
   - Insertion des données
   - Toutes les requêtes demandées
   - Commentaires explicatifs

2. **Rapport d'analyse** (2-3 pages) :
   - Justification des choix de modélisation
   - Analyse des performances
   - Propositions d'amélioration

3. **Jeu de données de test** :
   - Suffisamment fourni pour tester toutes les requêtes
   - Cas limites inclus

### Conseils de réalisation

**Organisation :**
1. Commencez par bien comprendre le domaine
2. Dessinez le modèle sur papier avant de coder
3. Testez chaque requête avec des données simples
4. Optimisez seulement après avoir un système fonctionnel

**Bonnes pratiques :**
- Nommage cohérent des tables et colonnes
- Commentaires dans le code SQL
- Gestion des erreurs
- Tests avec des cas limites

**Ressources utiles :**
- Documentation SQL de votre SGBD
- Outils de modélisation (draw.io, MySQL Workbench)
- Générateurs de données de test

---

## Solutions partielles

### Exemple de table DOCUMENTS
```sql
CREATE TABLE DOCUMENTS (
    id_document INTEGER PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('Livre', 'DVD', 'CD')),
    isbn_ean VARCHAR(20),
    date_publication DATE,
    id_categorie INTEGER NOT NULL,
    duree_emprunt INTEGER DEFAULT 21,
    statut VARCHAR(20) DEFAULT 'Disponible' 
        CHECK (statut IN ('Disponible', 'Emprunté', 'Réparation', 'Perdu')),
    FOREIGN KEY (id_categorie) REFERENCES CATEGORIES(id_categorie)
);
```

### Exemple de requête avec jointure
```sql
-- Documents avec leurs créateurs
SELECT d.titre, d.type, c.nom, c.prenom, cr.role
FROM DOCUMENTS d
JOIN CREER cr ON d.id_document = cr.id_document
JOIN CREATEURS c ON cr.id_createur = c.id_createur
ORDER BY d.titre, cr.role;
```

### Exemple d'index
```sql
-- Index pour optimiser les recherches par titre
CREATE INDEX idx_documents_titre ON DOCUMENTS(titre);

-- Index composé pour les emprunts en cours
CREATE INDEX idx_emprunts_en_cours 
ON EMPRUNTS(date_retour_effective, id_adherent) 
WHERE date_retour_effective IS NULL;
```

Ce TP vous permettra de maîtriser les aspects essentiels des bases de données relationnelles et du langage SQL, de la conception à l'optimisation !