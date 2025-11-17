# Étude de cas - FuchsTechnology

**BTS SIO SLAM - Bloc B1**  
**Durée estimée : 2 à 4 heures**  
**Rendu attendu : Document PDF complet**

---

## 0 Présentation de l'entreprise

**FuchsTechnology** est une entreprise de développement d'applications sur mesure comptant 25 collaborateurs. L'entreprise développe des solutions logicielles pour des clients variés (e-commerce, gestion, mobile).

### 0.1 Contexte actuel

FuchsTechnology fait face à plusieurs problématiques :
- **Parc informatique obsolète** : ordinateurs de plus de 8 ans, ralentissements fréquents
- **Absence de sécurité unifiée** : pas d'antivirus centralisé
- **Logiciels métiers périmés** : versions non supportées
- **Nouveau projet client** : une société annexe, **TechStore**, souhaite une application web de gestion de stock

### 0.2 Budget disponible

**50 000 €** pour le renouvellement complet du parc informatique et des licences.

---

## 1 Renouvellement du parc informatique

### 1.1 Devis de nouveau matériel

#### 1.1.1 Objectif
Établir un devis détaillé pour renouveler le parc informatique dans la limite du budget de 50 000 €.

#### 1.1.2 Composition de l'équipe FuchsTechnology

| Poste | Nombre | Besoins spécifiques |
|-------|--------|---------------------|
| Développeurs Full-Stack | 12 | Stations performantes, 2 écrans |
| Chef de projet | 2 | Station standard, mobilité |
| Designers UI/UX | 3 | Station haute performance graphique |
| Testeurs QA | 4 | Station standard |
| Support technique | 2 | Station standard + outils réseau |
| Direction | 2 | Laptops premium |

#### 1.1.3 Équipements à prévoir

Pour chaque collaborateur, prévoir :
- **Poste de travail** adapté au profil
- **Écran(s)** : 1 ou 2 selon le poste
- **Périphériques** : clavier, souris
- **Logiciels métiers** :
  - Suite Office 365 (tous)
  - IDE (JetBrains IntelliJ IDEA ou Visual Studio Code) pour développeurs
  - Adobe Creative Suite pour designers
  - Outils de test (Selenium, Postman) pour QA
- **Antivirus professionnel** : protection centralisée (ex : Bitdefender GravityZone, Kaspersky Endpoint)
- **Serveur** : 1 serveur pour hébergement interne et gestion centralisée

#### 1.1.4 Travail à réaliser

**Créer un tableau de devis détaillé** comprenant :

| Catégorie | Quantité | Description | Prix unitaire HT | Prix total HT |
|-----------|----------|-------------|------------------|---------------|
| Postes développeurs | 12 | PC fixe performant (i7, 32 GB RAM, SSD 1TB) | | |
| Postes designers | 3 | PC haute performance graphique (i9, 64 GB RAM, GPU dédié) | | |
| Postes standards | 8 | PC standard (i5, 16 GB RAM, SSD 512GB) | | |
| Laptops direction | 2 | Laptop premium (Dell XPS ou équivalent) | | |
| Écrans | 35 | Écrans 24" Full HD | | |
| Écrans designers | 3 | Écrans 27" 4K | | |
| Périphériques | 25 | Clavier + souris | | |
| Licences Office 365 | 25 | Abonnement annuel Business Premium | | |
| Licences JetBrains | 12 | IntelliJ IDEA Ultimate (annuel) | | |
| Licences Adobe CC | 3 | Creative Cloud All Apps (annuel) | | |
| Antivirus entreprise | 25 | Licence annuelle | | |
| Serveur | 1 | Serveur Dell PowerEdge ou équivalent | | |
| **TOTAL HT** | | | | |
| **TVA (20%)** | | | | |
| **TOTAL TTC** | | | | |

**Contrainte** : Le total TTC ne doit pas dépasser **50 000 €**.

### 1.2 Inventaire CMDB

#### 1.2.1 Objectif

Réaliser un inventaire complet du patrimoine informatique existant de FuchsTechnology sous forme de CMDB (Configuration Management Database) après le renouvellement.

### 1.2.2 Rappel théorique - CMDB

La **CMDB (Configuration Management Database)** est une base de données centralisée qui contient des informations sur tous les éléments de configuration (CI - Configuration Items) du système d'information d'une organisation.

**Éléments à inventorier** :
- **Matériel** : postes de travail, serveurs, périphériques, équipements réseau
- **Logiciels** : applications, licences, versions
- **Services** : services IT fournis aux utilisateurs
- **Relations** : interdépendances entre éléments

**Informations essentielles pour chaque CI** :
- Identifiant unique
- Type et modèle
- Localisation
- Utilisateur/propriétaire
- Date d'acquisition
- État (en service, en panne, obsolète)
- Informations de maintenance

#### 1.2.3 Travail à faire

Réaliser l'inventaire complet du patrimoine informatique de FuchsTechnology après le renouvellement du matériel.
Faire correspondre chaque ligne du CMDB à un équipement informatique ou à un logiciel à licence.

## 2 Planification projet — Application TechStore

### 2.0 Objectif
Planifier le développement de l'application de gestion de stock pour le client TechStore à l'aide d'un diagramme de Gantt.

### 2.1 Description du projet

**TechStore** souhaite une application web permettant de :
- Gérer un inventaire de produits (ajout, modification, suppression)
- Suivre les entrées/sorties de stock
- Générer des alertes de stock faible
- Produire des rapports d'activité
- Gérer les utilisateurs et leurs droits

### 2.2 Tâches du projet

Voici les tâches identifiées pour le projet :

| ID | Tâche | Description | Durée (jours) | Prédécesseurs |
|----|-------|-------------|---------------|---------------|
| **A** | Analyse des besoins | Entretiens client, spécifications fonctionnelles | 5 | - |
| **B** | Conception base de données | Modélisation MCD/MLD | 4 | A |
| **C** | Conception UI/UX | Maquettes et prototypes | 6 | A |
| **D** | Validation conception | Présentation au client | 2 | B, C |
| **E** | Développement Backend | API REST + base de données | 12 | D |
| **F** | Développement Frontend | Interface utilisateur | 10 | D |
| **G** | Module d'authentification | Gestion utilisateurs et droits | 5 | E |
| **H** | Module de reporting | Génération de rapports PDF | 4 | E, F |
| **I** | Intégration et tests unitaires | Tests techniques | 6 | E, F, G, H |
| **J** | Tests fonctionnels | Tests avec scénarios utilisateur | 5 | I |
| **K** | Corrections des anomalies | Résolution des bugs identifiés | 4 | J |
| **L** | Recette client | Validation par le client | 3 | K |
| **M** | Formation utilisateurs | Formation des équipes TechStore | 2 | L |
| **N** | Mise en production | Déploiement final | 2 | M |

### 2.3 Travail à réaliser

1. **Créer un diagramme de Gantt** pour ce projet :
   - Utiliser un tableur (Excel, Google Sheets) ou un outil dédié (GanttProject, ProjectLibre)
   - Représenter toutes les tâches avec leur durée
   - Indiquer les dépendances entre tâches
   - Identifier visuellement les jalons importants (validation conception, recette client, mise en production)
   - Calculer la **durée totale du projet**

2. **Identifier les jalons clés** :
   - Jalon 1 : Validation de la conception
   - Jalon 2 : Fin du développement
   - Jalon 3 : Recette client validée
   - Jalon 4 : Mise en production


---

## 3 Chemin critique

### 3.1 Objectif
Identifier le chemin critique du projet TechStore et calculer les marges de manœuvre pour chaque tâche.

### 3.2 Rappel théorique

- **Chemin critique** : séquence de tâches déterminant la durée minimale du projet
- **Marge totale** : retard maximum qu'une tâche peut prendre sans retarder le projet
- **Tâche critique** : tâche avec une marge totale = 0

### 3.3 Travail à réaliser

1. **Tracer le réseau PERT** du projet (graphe des tâches et dépendances)

2. **Calculer pour chaque tâche** :
   - **Date de début au plus tôt** (calcul avant)
   - **Date de début au plus tard** (calcul arrière)
   - **Marge totale** = Date au plus tard - Date au plus tôt - Durée
   
3. **Identifier le chemin critique** (tâches avec marge = 0)

4. **Créer un tableau récapitulatif** :

| Tâche | Durée | Début au plus tôt | Début au plus tard | Marge totale | Critique ? |
|-------|-------|-------------------|-------------------|--------------|------------|
| A | 5 | 0 | | | |
| B | 4 | | | | |
| C | 6 | | | | |
| ... | | | | | |

5. **Justification** :
   - Expliquer pourquoi ces tâches sont critiques
   - Indiquer les conséquences d'un retard sur une tâche critique
   - Proposer 2-3 mesures pour sécuriser le chemin critique

💡 **Exemple de justification** : "La tâche E (Développement Backend) est critique car elle détermine la durée minimale du projet. Un retard d'un jour sur cette tâche retardera automatiquement la livraison finale d'un jour. Il est recommandé d'affecter les développeurs les plus expérimentés et de prévoir des points d'avancement quotidiens."

---

## ⚠️ PARTIE 4 : GESTION DES RISQUES

### 🎯 Objectifs
1. Analyser les risques liés à l'infrastructure de FuchsTechnology
2. Analyser les risques liés au projet TechStore

### 4.2 Rappel — Matrice des risques

| Probabilité / Impact | Négligeable (1) | Mineur (2) | Modéré (3) | Majeur (4) | Critique (5) |
|---------------------|-----------------|------------|------------|------------|--------------|
| **Très probable (5)** | 5 | 10 | 15 | 20 | 25 |
| **Probable (4)** | 4 | 8 | 12 | 16 | 20 |
| **Possible (3)** | 3 | 6 | 9 | 12 | 15 |
| **Peu probable (2)** | 2 | 4 | 6 | 8 | 10 |
| **Rare (1)** | 1 | 2 | 3 | 4 | 5 |

**Niveaux de criticité** :
- 1-6 : Risque faible (surveillance)
- 8-9 : Risque moyen (plan de contingence)
- 10-16 : Risque élevé (actions préventives obligatoires)
- 20-25 : Risque critique (traitement immédiat)

### 4.3 Risques infrastructurels (FuchsTechnology)

#### 4.3.1 Travail à réaliser

Identifier **au minimum 6 risques** liés à l'infrastructure de l'entreprise et compléter le tableau :

| ID | Risque identifié | Probabilité (1-5) | Impact (1-5) | Criticité | Stratégie | Mesures de mitigation |
|----|------------------|-------------------|--------------|-----------|-----------|----------------------|
| R01 | Panne du serveur principal | | | | | |
| R02 | Cyberattaque (ransomware) | | | | | |
| R03 | Perte de données (absence de sauvegarde) | | | | | |
| R04 | Coupure électrique prolongée | | | | | |
| R05 | Défaillance du système antivirus | | | | | |
| R06 | ... | | | | | |

Types de risques à considérer :
- Pannes matérielles
- Risques de sécurité
- Risques humains (départ d'un administrateur clé)
- Risques environnementaux (incendie, inondation)
- Risques réseau

Stratégies disponibles : Éviter, Transférer, Réduire, Accepter

### 4.4 Risques projet (Application TechStore)

#### 4.4.1 Travail à réaliser

Identifier **au minimum 6 risques** liés au développement de l'application TechStore :

| ID | Risque identifié | Probabilité (1-5) | Impact (1-5) | Criticité | Stratégie | Mesures de mitigation |
|----|------------------|-------------------|--------------|-----------|-----------|----------------------|
| R11 | Dérive du périmètre fonctionnel | | | | | |
| R12 | Départ d'un développeur clé | | | | | |
| R13 | Sous-estimation de la complexité technique | | | | | |
| R14 | Retard de validation client | | | | | |
| R15 | Problèmes d'intégration API | | | | | |
| R16 | ... | | | | | |

Types de risques à considérer :
- Risques techniques (choix technologiques, intégration)
- Risques de planning (retards, sous-estimation)
- Risques humains (compétences, disponibilité)
- Risques clients (changements de besoins, validation)
- Risques de sécurité applicative

### 4.5 Justification attendue

Pour chaque risque, justifier brièvement :
- Pourquoi cette probabilité et cet impact ?
- Pourquoi cette stratégie de traitement ?
- Comment les mesures de mitigation réduiront le risque ?

---

## 5 Gestion ITIL

### 5.1 Objectif
Mettre en place une gestion de services ITIL pour l'application TechStore une fois mise en production.

### 5.2 Rappel théorique

ITIL définit les bonnes pratiques pour **faire vivre un service dans la durée** après sa mise en production.

**Les 3 pratiques essentielles** :
1. **Gestion des incidents** : rétablir le service rapidement
2. **Gestion des problèmes** : identifier et corriger les causes profondes
3. **Gestion des changements** : modifier le service sans créer de pannes

### 5.3 Gestion des incidents

#### 5.3.1 Travail à réaliser

1. **Définir les niveaux de priorité** des incidents pour l'application TechStore :

| Priorité | Impact | Urgence | Exemple | Délai de résolution cible |
|----------|--------|---------|---------|---------------------------|
| **Critique** | Élevé | Élevée | Application complètement inaccessible | |
| **Élevée** | Élevé | Moyenne | | |
| **Moyenne** | Moyen | Moyenne | | |
| **Faible** | Faible | Faible | | |

2. **Définir le processus d'escalade** :

| Niveau | Responsable | Type d'intervention | Délai de prise en charge |
|--------|-------------|---------------------|--------------------------|
| **Niveau 1** | Support utilisateur (Helpdesk) | | |
| **Niveau 2** | Technicien spécialisé | | |
| **Niveau 3** | Expert/Développeur senior | | |
| **Niveau 4** | Fournisseurs externes | | |

3. **Proposer 3 exemples d'incidents** avec leur traitement :

**Incident 1** :
- Description :
- Priorité :
- Solution temporaire (workaround) :
- Niveau d'escalade :

**Incident 2** :
- Description :
- Priorité :
- Solution temporaire :
- Niveau d'escalade :

**Incident 3** :
- Description :
- Priorité :
- Solution temporaire :
- Niveau d'escalade :

### 5.4 Gestion des problèmes

#### 5.4.1 Travail à réaliser

Identifier **3 problèmes potentiels** (causes profondes récurrentes) et leur traitement :

| Problème | Incidents associés | Cause racine identifiée | Solution définitive proposée | Délai de mise en œuvre |
|----------|-------------------|------------------------|----------------------------|------------------------|
| Exemple : Lenteurs fréquentes de l'application | Incidents de timeout récurrents | Requêtes SQL non optimisées | Optimisation des index et requêtes | 2 semaines |
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |

### 5.5 Gestion des changements

#### 5.5.1 Travail à réaliser

1. **Définir les types de changements** pour l'application TechStore :

| Type | Description | Niveau d'approbation | Exemple |
|------|-------------|---------------------|---------|
| **Standard** | Changement pré-approuvé, faible risque | Automatique | Mise à jour de sécurité mineure |
| **Normal** | Changement nécessitant évaluation | | |
| **Urgent** | Changement d'urgence suite à incident critique | | |

2. **Décrire le processus de gestion des changements** :

Remplir les étapes manquantes et leur contenu :

1. **Demande de changement** : Qui peut demander ? Quel formulaire ?
2. **Évaluation des risques** : Quels critères d'évaluation ?
3. **Approbation** : Qui approuve selon le type ?
4. **Planification** : Quand effectuer le changement ?
5. **Tests** : Dans quel environnement tester ?
6. **Implémentation** : Qui réalise ? Quand ?
7. **Révision post-implémentation** : Vérifications à effectuer ?

3. **Proposer 3 exemples de changements** avec leur processus :

**Changement 1** : (ex : Ajout d'une nouvelle fonctionnalité)
- Type :
- Risques identifiés :
- Plan de tests :
- Procédure de rollback :

**Changement 2** :
- Type :
- Risques identifiés :
- Plan de tests :
- Procédure de rollback :

**Changement 3** :
- Type :
- Risques identifiés :
- Plan de tests :
- Procédure de rollback :

---

## 6 Format du rendu

### 6.1 Contenu du PDF

Faire contenir au document PDF **dans l'ordre** :

1. **Page de garde** :
   - Titre : "Étude de cas FuchsTechnology"
   - Vos noms et prénoms
   - Classe : BTS SIO SLAM 2
   - Date

2. **Sommaire** avec pagination

3. **Partie 1 : Inventaire CMDB du patrimoine informatique**
   - Tableau CMDB matériel
   - Tableau CMDB licences
   - Tableau services IT
   - Analyse de l'état du parc
   - Plan de migration

4. **Partie 2 : Diagramme de Gantt**
   - Image du Gantt
   - Durée totale du projet
   - Jalons identifiés

5. **Partie 3 : Chemin critique**
   - Réseau PERT ou tableau récapitulatif
   - Identification du chemin critique
   - Justifications et mesures de sécurisation

6. **Partie 4 : Gestion des risques**
   - 4.1 Risques infrastructurels (tableau + justifications)
   - 4.2 Risques projet (tableau + justifications)

7. **Partie 5 : Gestion ITIL**
   - 5.1 Gestion des incidents
   - 5.2 Gestion des problèmes
   - 5.3 Gestion des changements
   - 5.4 Outils et organisation

### 6.2 Critères d'évaluation

| Critère | Points |
|---------|--------|
| Devis réaliste et respectant le budget | /3 |
| Inventaire CMDB complet et cohérent | /4 |
| Diagramme de Gantt complet et cohérent | /3 |
| Chemin critique correctement identifié et justifié | /3 |
| Analyse des risques pertinente et complète | /4 |
| Gestion ITIL cohérente et appliquée | /3 |
| **TOTAL** | **/20** |
