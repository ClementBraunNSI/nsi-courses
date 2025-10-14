# Devoir Surveillé – BTS SIO 2e année (B1)

## Gestion de projet, chemin critique, gestion des risques et ITIL

**Durée totale : 2 heures**  
**Partie 1 (20 min)** – Questions de cours  
**Partie 2 (1h40)** – Étude de cas : du projet à la gestion de service  

La justification, la rigueur, la rédaction et le soin de la copie entrent dans la notation sur 2 points.
Un manquement de ces 4 critères entraîne une perte de 2 points.

---

## Partie 1 – Révision de cours (20 min) (6 points)

### Gestion de projet

1. Donner la définition d’un **projet informatique**.  
2. Citer les **3 contraintes** du triangle de la gestion de projet.  
3. Décrire le rôle du **chef de projet** et indiquer deux de ses responsabilités.  
4. Expliquer la différence entre un **livrable** et un **jalon**.  
5. Citer deux **méthodes de planification** de projet et présenter un avantage pour chacune.  

---

### Chemin critique

1. Expliquer l’utilité du calcul du **chemin critique**.  
2. Indiquer la conséquence d’un **retard** sur une tâche du chemin critique.  

---

### Gestion des risques

1. Donner la **formule de la criticité** d’un risque.  
2. Citer les **4 étapes principales** de la gestion des risques.  
3. Donner un exemple de **risque technique** et un **risque humain** dans un projet informatique.  

---

### ITIL

1. Définir ce qu'est **ITIL**.
2. Expliquer la différence entre **gestion d’incident** et **gestion de problème**.  
3. Présenter le rôle de la **gestion des changements**.  
4. Indiquer l’utilité de la **gestion des connaissances** dans un service informatique.  


## 💼 Partie 2 – Étude de cas complète (1h40) (12 points)

### **Contexte général**

L’entreprise **CityPark** souhaite développer une application web et mobile pour gérer les parkings connectés dans plusieurs villes.  
Le projet, baptisé **ParkLink**, vise à :
- afficher en temps réel les places disponibles,  
- permettre le paiement via smartphone,  
- fournir des statistiques aux villes partenaires.  

L’équipe projet est composée de :

| Rôle | Nom | Responsabilités |
|------|------|----------------|
| Chef de projet | Thomas | Coordination, suivi du planning, gestion des risques |
| Développeuse back-end | Maëlle | API et base de données |
| Développeur front-end | Rayan | Interface utilisateur |
| Technicien support | Léo | Tests et maintenance future |

Durée prévue : **5 mois**  
Budget : **55 000 €**


<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


## 🔹 Étape 1 – Planification du projet

### 1. Contraintes et acteurs

a. Lister les **contraintes principales** du projet.

b. Analyser la **composition de l'équipe projet** :

   - Identifier un **rôle manquant** qui pourrait être nécessaire pour ce type de projet.
   - Expliquer pourquoi la **répartition des responsabilités** est importante dans la gestion de projet.


### 2. Tâches et dépendances

| Tâche | Description | Durée (jours) | Dépend de |
|-------|--------------|----------------|------------|
| A | Étude des besoins et cahier des charges | 5 | - |
| B | Conception de la base de données | 4 | A |
| C | Développement du back-end | 10 | B |
| D | Développement du front-end | 8 | A |
| E | Tests et intégration | 6 | C, D |
| F | Déploiement | 3 | E |

1. Construire un **diagramme de Gantt** du projet (tâches A à F) : dessiner les barres temporelles en jours, indiquer les dépendances, les chevauchements possibles et les jalons.
2. Représenter le **diagramme des dépendances (PERT)**.  
3. Calculer la **durée totale du projet**.  
4. Identifier le **chemin critique**.  
5. Déterminer la conséquence d’un **retard de 2 jours** sur la tâche D.


<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## 🔹 Étape 2 – Gestion des risques

L’équipe a identifié les risques suivants :  

| N° | Risque | Probabilité | Impact | Criticité | Mesure de mitigation |
|----|---------|--------------|---------|-------------|-----------------------|
| R1 | Départ d’un développeur | ______ | ______ | ______ | ______ |
| R2 | Panne du serveur de test | ______ | ______ | ______ | ______ |
| R3 | Retard sur le cahier des charges | ______ | ______ | ______ | ______ |
| R4 | Mauvaise communication dans l’équipe | ______ | ______ | ______ | ______ |
| R5 | Non-respect du budget | ______ | ______ | ______ | ______ |

1. L'équipe n'a pas été exhaustive vis à vis des risques en manquant d'analyse approfondie. Identifier **3 risques différents de ceux déjà identifiés**.
2. Compléter le tableau en **attribuant des valeurs** (Faible, Moyenne, Forte, Critique) aux colonnes Probabilité et Impact, puis calculer la **criticité**.  
3. Justifier **chaque choix** (expliquer pourquoi le risque ou la probabilité sont critiques, forts, moyens ou faibles).  
4. Classer les risques du **plus critique au moins critique**.  
5. Proposer **une action de prévention** et **une action corrective** pour le risque le plus critique.  
6. Expliquer l’utilité d’un **plan de mitigation**.  


## 🔹 Étape 3 – Gestion des services (ITIL)

Trois mois après la mise en production, **CityPark** met en place un service support. Voici les incidents observés :

| Situation | Description |
|------------|-------------|
| S1 | L’application est inaccessible pendant 20 minutes. |
| S2 | Tous les lundis matin, le service de paiement plante. |
| S3 | Le développeur déploie une mise à jour sans test préalable, provoquant un bug. |
| S4 | L’équipe n’a aucune trace des tickets d’incidents résolus. |

1. Associer chaque situation à la **bonne pratique ITIL** parmi :  
   - Gestion des problèmes  
   - Gestion des connaissances  
   - Gestion des incidents
   - Gestion des changements  

2. Pour chaque situation :  
   - Proposer une **action immédiate** (réactive)  
   - Proposer une **action durable** (préventive ou organisationnelle)  
3. Expliquer comment ITIL permet de **maintenir la qualité du service** sur le long terme.  
4. Citer un **outil concret** pouvant faciliter cette gestion.
