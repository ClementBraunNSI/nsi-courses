# Le modèle relationnel et les bases de données

## Introduction

Les bases de données relationnelles constituent l'un des piliers de l'informatique moderne. Elles permettent de stocker, organiser et manipuler efficacement de grandes quantités d'informations structurées.

### Pourquoi les bases de données ?

**Problèmes des fichiers traditionnels :**
- Redondance des données
- Incohérence possible
- Difficultés de partage
- Pas de contrôle d'accès concurrent
- Pas de garantie d'intégrité

**Avantages des bases de données :**
- Élimination de la redondance
- Cohérence des données
- Partage sécurisé
- Contrôle des accès
- Sauvegarde et récupération
- Requêtes complexes

---

## Le modèle relationnel

### Concepts fondamentaux

#### 1. Relation (Table)
Une **relation** est un ensemble de tuples ayant la même structure. En pratique, c'est une table.

#### 2. Attribut (Colonne)
Un **attribut** est une propriété des entités représentées. Chaque attribut a :
- Un nom unique dans la relation
- Un domaine (type de données)

#### 3. Tuple (Ligne)
Un **tuple** est un élément de la relation, représentant une entité.

#### 4. Domaine
Un **domaine** est l'ensemble des valeurs possibles pour un attribut.

### Exemple concret

**Relation ELEVES :**

| id_eleve | nom     | prenom | classe | age |
|----------|---------|--------|--------| --- |
| 1        | Dupont  | Marie  | TG1    | 17  |
| 2        | Martin  | Paul   | TG2    | 18  |
| 3        | Bernard | Julie  | TG1    | 17  |

- **Relation** : ELEVES
- **Attributs** : id_eleve, nom, prenom, classe, age
- **Tuples** : chaque ligne
- **Domaines** : 
  - id_eleve : entiers positifs
  - nom, prenom : chaînes de caractères
  - classe : {TG1, TG2, TG3, ...}
  - age : entiers entre 15 et 20

---

## Clés et contraintes

### Clé primaire

Une **clé primaire** est un attribut (ou ensemble d'attributs) qui :
- Identifie de manière unique chaque tuple
- Ne peut pas être NULL
- Ne peut pas être dupliquée

```sql
-- Exemple de définition
CREATE TABLE ELEVES (
    id_eleve INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    classe VARCHAR(10),
    age INTEGER
);
```

### Clé étrangère

Une **clé étrangère** est un attribut qui fait référence à la clé primaire d'une autre relation.

**Exemple avec deux tables :**

**Table CLASSES :**
| id_classe | nom_classe | professeur_principal |
|-----------|------------|---------------------|
| 1         | TG1        | M. Durand           |
| 2         | TG2        | Mme Petit           |

**Table ELEVES (modifiée) :**
| id_eleve | nom     | prenom | id_classe | age |
|----------|---------|--------|-----------|-----|
| 1        | Dupont  | Marie  | 1         | 17  |
| 2        | Martin  | Paul   | 2         | 18  |
| 3        | Bernard | Julie  | 1         | 17  |

```sql
CREATE TABLE CLASSES (
    id_classe INTEGER PRIMARY KEY,
    nom_classe VARCHAR(10) NOT NULL,
    professeur_principal VARCHAR(100)
);

CREATE TABLE ELEVES (
    id_eleve INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    id_classe INTEGER,
    age INTEGER,
    FOREIGN KEY (id_classe) REFERENCES CLASSES(id_classe)
);
```

### Contraintes d'intégrité

#### 1. Contrainte d'entité
- La clé primaire ne peut pas être NULL
- La clé primaire doit être unique

#### 2. Contrainte référentielle
- Une clé étrangère doit référencer une clé primaire existante
- Ou être NULL si autorisé

#### 3. Contraintes de domaine
- Les valeurs doivent respecter le type de données
- Contraintes CHECK personnalisées

```sql
CREATE TABLE ELEVES (
    id_eleve INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    id_classe INTEGER,
    age INTEGER CHECK (age >= 15 AND age <= 20),
    email VARCHAR(100) UNIQUE,
    FOREIGN KEY (id_classe) REFERENCES CLASSES(id_classe)
);
```

---

## Conception d'une base de données

### Étapes de conception

#### 1. Analyse des besoins
- Identifier les entités
- Identifier les relations entre entités
- Définir les attributs

#### 2. Modèle conceptuel (MCD)
- Diagramme entité-relation
- Cardinalités

#### 3. Modèle logique (MLD)
- Transformation en tables
- Définition des clés

#### 4. Modèle physique
- Implémentation dans un SGBD
- Optimisations

### Exemple : Système de gestion de bibliothèque

#### Analyse des besoins
**Entités identifiées :**
- Livre
- Auteur
- Emprunteur
- Emprunt

**Relations :**
- Un livre peut avoir plusieurs auteurs
- Un auteur peut écrire plusieurs livres
- Un emprunteur peut emprunter plusieurs livres
- Un livre peut être emprunté par plusieurs emprunteurs (à des moments différents)

#### Modèle logique

**Table AUTEURS :**
```sql
CREATE TABLE AUTEURS (
    id_auteur INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE,
    nationalite VARCHAR(50)
);
```

**Table LIVRES :**
```sql
CREATE TABLE LIVRES (
    id_livre INTEGER PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    date_publication DATE,
    genre VARCHAR(50),
    nb_pages INTEGER
);
```

**Table EMPRUNTEURS :**
```sql
CREATE TABLE EMPRUNTEURS (
    id_emprunteur INTEGER PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telephone VARCHAR(15),
    date_inscription DATE NOT NULL
);
```

**Table ECRIRE (relation plusieurs-à-plusieurs) :**
```sql
CREATE TABLE ECRIRE (
    id_auteur INTEGER,
    id_livre INTEGER,
    role VARCHAR(50) DEFAULT 'auteur',
    PRIMARY KEY (id_auteur, id_livre),
    FOREIGN KEY (id_auteur) REFERENCES AUTEURS(id_auteur),
    FOREIGN KEY (id_livre) REFERENCES LIVRES(id_livre)
);
```

**Table EMPRUNTS :**
```sql
CREATE TABLE EMPRUNTS (
    id_emprunt INTEGER PRIMARY KEY,
    id_livre INTEGER NOT NULL,
    id_emprunteur INTEGER NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    statut VARCHAR(20) DEFAULT 'en_cours',
    FOREIGN KEY (id_livre) REFERENCES LIVRES(id_livre),
    FOREIGN KEY (id_emprunteur) REFERENCES EMPRUNTEURS(id_emprunteur)
);
```

---

## Normalisation

La **normalisation** est un processus qui permet d'organiser les données pour :
- Éliminer la redondance
- Éviter les anomalies de mise à jour
- Assurer la cohérence

### Première forme normale (1FN)

Une relation est en 1FN si :
- Tous les attributs sont atomiques (indivisibles)
- Pas de groupes répétitifs

**❌ Pas en 1FN :**
| id_eleve | nom    | telephones        |
|----------|--------|------------------|
| 1        | Dupont | 01.23.45.67.89, 06.12.34.56.78 |

**✅ En 1FN :**
| id_eleve | nom    | telephone      | type      |
|----------|--------|----------------|----------|
| 1        | Dupont | 01.23.45.67.89 | fixe     |
| 1        | Dupont | 06.12.34.56.78 | portable |

### Deuxième forme normale (2FN)

Une relation est en 2FN si :
- Elle est en 1FN
- Tous les attributs non-clés dépendent entièrement de la clé primaire

**❌ Pas en 2FN :**
| id_commande | id_produit | nom_produit | quantite | prix_unitaire |
|-------------|------------|-------------|----------|---------------|
| 1           | 101        | Ordinateur  | 2        | 800           |
| 1           | 102        | Souris      | 1        | 25            |

Problème : `nom_produit` et `prix_unitaire` dépendent seulement de `id_produit`

**✅ En 2FN :**

**Table PRODUITS :**
| id_produit | nom_produit | prix_unitaire |
|------------|-------------|---------------|
| 101        | Ordinateur  | 800           |
| 102        | Souris      | 25            |

**Table LIGNES_COMMANDE :**
| id_commande | id_produit | quantite |
|-------------|------------|----------|
| 1           | 101        | 2        |
| 1           | 102        | 1        |

### Troisième forme normale (3FN)

Une relation est en 3FN si :
- Elle est en 2FN
- Aucun attribut non-clé ne dépend transitivement de la clé primaire

**❌ Pas en 3FN :**
| id_eleve | nom    | id_classe | nom_classe |
|----------|--------|-----------|------------|
| 1        | Dupont | 1         | TG1        |
| 2        | Martin | 1         | TG1        |

Problème : `nom_classe` dépend de `id_classe` qui dépend de `id_eleve`

**✅ En 3FN :**

**Table CLASSES :**
| id_classe | nom_classe |
|-----------|------------|
| 1         | TG1        |

**Table ELEVES :**
| id_eleve | nom    | id_classe |
|----------|--------|-----------|
| 1        | Dupont | 1         |
| 2        | Martin | 1         |

---

## Algèbre relationnelle

L'**algèbre relationnelle** définit les opérations de base sur les relations.

### Opérations de base

#### 1. Sélection (σ)
Sélectionne les tuples qui satisfont une condition.

**Notation :** σ_condition(Relation)

**Exemple :** σ_age>17(ELEVES)

```sql
-- Équivalent SQL
SELECT * FROM ELEVES WHERE age > 17;
```

#### 2. Projection (π)
Sélectionne certains attributs d'une relation.

**Notation :** π_attributs(Relation)

**Exemple :** π_nom,prenom(ELEVES)

```sql
-- Équivalent SQL
SELECT nom, prenom FROM ELEVES;
```

#### 3. Union (∪)
Combine deux relations compatibles.

**Notation :** R1 ∪ R2

```sql
-- Équivalent SQL
SELECT * FROM R1
UNION
SELECT * FROM R2;
```

#### 4. Intersection (∩)
Tuples présents dans les deux relations.

**Notation :** R1 ∩ R2

```sql
-- Équivalent SQL
SELECT * FROM R1
INTERSECT
SELECT * FROM R2;
```

#### 5. Différence (-)
Tuples de R1 qui ne sont pas dans R2.

**Notation :** R1 - R2

```sql
-- Équivalent SQL
SELECT * FROM R1
EXCEPT
SELECT * FROM R2;
```

#### 6. Produit cartésien (×)
Combine chaque tuple de R1 avec chaque tuple de R2.

**Notation :** R1 × R2

```sql
-- Équivalent SQL
SELECT * FROM R1, R2;
-- ou
SELECT * FROM R1 CROSS JOIN R2;
```

#### 7. Jointure (⋈)
Combine les tuples de deux relations selon une condition.

**Notation :** R1 ⋈_condition R2

```sql
-- Équivalent SQL
SELECT * FROM R1 JOIN R2 ON condition;
```

### Exemples pratiques

**Données :**

**ELEVES :**
| id_eleve | nom     | prenom | id_classe |
|----------|---------|--------|-----------|
| 1        | Dupont  | Marie  | 1         |
| 2        | Martin  | Paul   | 2         |
| 3        | Bernard | Julie  | 1         |

**CLASSES :**
| id_classe | nom_classe | professeur |
|-----------|------------|------------|
| 1         | TG1        | M. Durand  |
| 2         | TG2        | Mme Petit  |

**Requêtes :**

1. **Élèves de la classe TG1 :**
   ```
   π_nom,prenom(σ_nom_classe='TG1'(ELEVES ⋈ CLASSES))
   ```

2. **Noms des professeurs :**
   ```
   π_professeur(CLASSES)
   ```

3. **Élèves avec leur classe :**
   ```
   ELEVES ⋈_ELEVES.id_classe=CLASSES.id_classe CLASSES
   ```

---

## Implémentation en Python

### Simulation simple d'une base de données

```python
class Relation:
    def __init__(self, nom, attributs):
        self.nom = nom
        self.attributs = attributs  # Liste des noms d'attributs
        self.tuples = []  # Liste de dictionnaires
        self.cle_primaire = None
    
    def definir_cle_primaire(self, attribut):
        """Définit la clé primaire"""
        if attribut in self.attributs:
            self.cle_primaire = attribut
        else:
            raise ValueError(f"Attribut {attribut} non trouvé")
    
    def inserer(self, tuple_dict):
        """Insère un tuple"""
        # Vérifier que tous les attributs sont présents
        if set(tuple_dict.keys()) != set(self.attributs):
            raise ValueError("Attributs manquants ou en trop")
        
        # Vérifier l'unicité de la clé primaire
        if self.cle_primaire:
            valeur_cle = tuple_dict[self.cle_primaire]
            for t in self.tuples:
                if t[self.cle_primaire] == valeur_cle:
                    raise ValueError(f"Clé primaire {valeur_cle} déjà existante")
        
        self.tuples.append(tuple_dict.copy())
    
    def selection(self, condition):
        """Opération de sélection"""
        resultat = Relation(f"σ({self.nom})", self.attributs)
        resultat.cle_primaire = self.cle_primaire
        
        for tuple_dict in self.tuples:
            if condition(tuple_dict):
                resultat.tuples.append(tuple_dict.copy())
        
        return resultat
    
    def projection(self, attributs_voulus):
        """Opération de projection"""
        # Vérifier que les attributs existent
        for attr in attributs_voulus:
            if attr not in self.attributs:
                raise ValueError(f"Attribut {attr} non trouvé")
        
        resultat = Relation(f"π({self.nom})", attributs_voulus)
        
        tuples_vus = set()
        for tuple_dict in self.tuples:
            nouveau_tuple = {attr: tuple_dict[attr] for attr in attributs_voulus}
            # Éliminer les doublons
            tuple_key = tuple(nouveau_tuple[attr] for attr in attributs_voulus)
            if tuple_key not in tuples_vus:
                resultat.tuples.append(nouveau_tuple)
                tuples_vus.add(tuple_key)
        
        return resultat
    
    def jointure(self, autre_relation, condition):
        """Opération de jointure"""
        nouveaux_attributs = self.attributs + [
            attr for attr in autre_relation.attributs 
            if attr not in self.attributs
        ]
        
        resultat = Relation(f"{self.nom}⋈{autre_relation.nom}", nouveaux_attributs)
        
        for tuple1 in self.tuples:
            for tuple2 in autre_relation.tuples:
                # Combiner les tuples
                tuple_combine = tuple1.copy()
                for attr, valeur in tuple2.items():
                    if attr not in tuple_combine:
                        tuple_combine[attr] = valeur
                
                # Vérifier la condition
                if condition(tuple1, tuple2):
                    resultat.tuples.append(tuple_combine)
        
        return resultat
    
    def afficher(self):
        """Affiche la relation"""
        print(f"\nRelation {self.nom}:")
        if not self.tuples:
            print("Relation vide")
            return
        
        # En-têtes
        print("|", end="")
        for attr in self.attributs:
            print(f" {attr:^12} |", end="")
        print()
        
        # Séparateur
        print("|" + "-" * (14 * len(self.attributs) + 1) + "|")
        
        # Données
        for tuple_dict in self.tuples:
            print("|", end="")
            for attr in self.attributs:
                valeur = str(tuple_dict[attr])
                print(f" {valeur:^12} |", end="")
            print()

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer la relation ELEVES
    eleves = Relation("ELEVES", ["id_eleve", "nom", "prenom", "id_classe"])
    eleves.definir_cle_primaire("id_eleve")
    
    # Insérer des données
    eleves.inserer({"id_eleve": 1, "nom": "Dupont", "prenom": "Marie", "id_classe": 1})
    eleves.inserer({"id_eleve": 2, "nom": "Martin", "prenom": "Paul", "id_classe": 2})
    eleves.inserer({"id_eleve": 3, "nom": "Bernard", "prenom": "Julie", "id_classe": 1})
    
    # Créer la relation CLASSES
    classes = Relation("CLASSES", ["id_classe", "nom_classe", "professeur"])
    classes.definir_cle_primaire("id_classe")
    
    classes.inserer({"id_classe": 1, "nom_classe": "TG1", "professeur": "M. Durand"})
    classes.inserer({"id_classe": 2, "nom_classe": "TG2", "professeur": "Mme Petit"})
    
    # Afficher les relations
    eleves.afficher()
    classes.afficher()
    
    # Opérations
    print("\n=== OPÉRATIONS ===")
    
    # Sélection : élèves de la classe 1
    eleves_classe1 = eleves.selection(lambda t: t["id_classe"] == 1)
    eleves_classe1.afficher()
    
    # Projection : noms et prénoms
    noms_prenoms = eleves.projection(["nom", "prenom"])
    noms_prenoms.afficher()
    
    # Jointure : élèves avec leur classe
    eleves_avec_classe = eleves.jointure(
        classes, 
        lambda t1, t2: t1["id_classe"] == t2["id_classe"]
    )
    eleves_avec_classe.afficher()
```

---

## Exercices

### Exercice 1 : Modélisation
Modélisez une base de données pour un système de gestion d'une école :
- Élèves, professeurs, matières, classes, notes
- Définissez les relations et les contraintes
- Normalisez jusqu'à la 3FN

### Exercice 2 : Algèbre relationnelle
À partir des relations ELEVES et CLASSES :
1. Trouvez tous les élèves de M. Durand
2. Listez les professeurs qui ont des élèves
3. Comptez le nombre d'élèves par classe

### Exercice 3 : Implémentation
Étendez la classe `Relation` pour supporter :
- L'opération d'union
- Les contraintes de clé étrangère
- La suppression de tuples

---

## Conclusion

Le modèle relationnel offre :
- **Structure claire** : tables, lignes, colonnes
- **Intégrité** : contraintes et clés
- **Flexibilité** : requêtes complexes possibles
- **Normalisation** : élimination de la redondance
- **Base théorique** : algèbre relationnelle

Ces concepts sont essentiels pour comprendre les bases de données et le langage SQL que nous verrons dans le prochain cours.