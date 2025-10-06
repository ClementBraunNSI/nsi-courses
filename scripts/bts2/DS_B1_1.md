# Devoir Surveillé - Gestion de Projet

**BTS SIO - Seconde année**  
**Durée :** 2 heures  
**Barème :** 20 points  

---

## Consignes générales

- **Répondre directement sur une copie séparée**
- **Justifier les réponses**
- **Soigner la présentation** et l'orthographe
- 2 points sont répartis sur la rédaction, la justification et le soin de la copie.

---

## Exercice 1 – Gestion de projet

### Questions courtes

**1.** Définis un projet informatique et cite 3 caractéristiques essentielles.

**2.** Explique le triangle Qualité / Coût / Délai.

**3.** Associe chaque rôle à sa définition :
   - Chef de projet
   - Product Owner  
   - Scrum Master
   - Développeur

**4.** Donner deux différences majeures entre le cycle en V et les méthodes Agiles.

---
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Exercice 2 – Chemin critique

### Contexte : Planification du projet d'application mobile

Dans le cadre du projet d'application mobile e-commerce de l'exercice 3, l'équipe projet doit planifier les phases de développement. Voici les principales tâches identifiées pour la réalisation de l'application :

| Tâche | Description | Durée (jours) | Prédécesseurs |
|-------|-------------|---------------|---------------|
| A     | Analyse des besoins et spécifications | 4 | - |
| B     | Conception de l'architecture technique | 5 | A |
| C     | Design UX/UI et maquettes | 6 | A |
| D     | Développement du backend (API) | 3 | B |
| E     | Développement frontend mobile | 4 | B, C |
| F     | Intégration du module de paiement | 2 | C |
| G     | Tests d'intégration et déploiement | 5 | D, E, F |

### Questions

**1.** Construire le graphe PERT correspondant.

**2.** Calculer les dates au plus tôt de chaque tâche.

**3.** Calculer les dates au plus tard et les marges (totales et libres).

**4.** Identifier le chemin critique et la durée minimale du projet.

**5.** Si la tâche C (Design UX/UI) prend 2 jours de plus : le projet est-il retardé ? Justifier la réponse.

**6.** Si la tâche D (Développement backend) prend 3 jours de plus : analyser l'impact sur le projet.

---


<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Exercice 3 – Gestion des risques

### Cas pratique : Application mobile e-commerce

Une PME spécialisée dans la vente d'articles de sport en ligne souhaite développer une application mobile e-commerce.

#### Objectifs du projet

- Proposer une application iOS/Android permettant aux clients de consulter le catalogue et passer commande
- Intégrer un module de paiement sécurisé
- Mettre en place un système de fidélité (points + réductions)
- Livrer une première version dans 6 mois, afin d'être prête pour le Black Friday (période commerciale clé)

#### Ressources disponibles

**Équipe projet :**
- 1 chef de projet
- 1 product owner
- 1 UX/UI designer
- 4 développeurs (2 front, 2 back)
- 1 testeur QA

**Budget :** 120 000 €

**Infrastructure :** serveurs déjà en place, mais limités

### Travail demandé

**1.** Identifier au moins **6 risques possibles** dans ce projet (techniques, humains, organisationnels, financiers, externes…).

**2.** Pour chaque risque, préciser :
   - Sa **probabilité** (faible, moyenne, forte)
   - Son **impact** (faible, moyen, fort)

**3.** Construire la **matrice des risques** (probabilité × impact).

**4.** Calculer la **criticité**.

**5.** Classer les risques du **plus critique au moins critique**.

**6.** Proposer un **plan de mitigation** (solutions pour limiter les risques) pour **3 risques majeurs** (mesures préventives et correctives).
