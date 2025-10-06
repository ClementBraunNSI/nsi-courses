# ✅ Corrections – Exercices ITIL

Ce document regroupe les corrections essentielles des exercices sur **les incidents, les problèmes et la gestion des changements ITIL**.  
Format condensé, prêt à l’emploi pour la préparation ou la correction orale.

---

## 🧩 Exercice 1.1 – Incident ou problème ?

| **Situation** | **Type** | **Justification** |
|----------------|-----------|-------------------|
| L’imprimante du service comptabilité ne fonctionne plus | Incident | Panne ponctuelle, impact limité. |
| Tous les lundis matin, le serveur web est lent | Problème | Dysfonctionnement récurrent nécessitant une analyse. |
| Un utilisateur ne peut plus accéder à son dossier personnel | Incident | Cas isolé, à corriger rapidement. |
| Analyse de la cause des pannes réseau | Problème | Recherche de cause racine d’incidents répétés. |

> 💡 *Incident = urgence / réaction rapide*  
> *Problème = enquête / prévention des récurrences*

---

## ⚙️ Exercice 1.2 – Priorisation des incidents

| **Incident** | **Impact** | **Urgence** | **Priorité** | **Justification** |
|---------------|-------------|-------------|---------------|--------------------|
| Serveur de messagerie en panne (toute l’entreprise) | Élevé | Élevée | **1** | Service critique, tout le monde impacté. |
| Site web client inaccessible | Élevé | Élevée | **2** | Impact externe fort, perte potentielle de clients. |
| Logiciel de comptabilité lent (fin de mois) | Moyen | Élevée | **3** | Urgent mais impact partiel. |
| Imprimante d’un bureau en panne | Faible | Faible | **4** | Impact faible et localisé. |

> 🧠 *Priorité = Impact × Urgence*  
> On traite d’abord ce qui bloque le plus d’utilisateurs.

---

## 🧭 Exercice 1.3 – Escalade des incidents

| **Incident** | **Niveau d’escalade** | **Justification** |
|---------------|------------------------|-------------------|
| Mot de passe oublié | Niveau 1 – Helpdesk | Résolution standard, pas technique. |
| Serveur de base de données corrompu | Niveau 3 – Experts | Requiert compétences avancées. |
| Bug dans un logiciel métier | Niveau 4 – Fournisseur | Nécessite correctif éditeur. |
| Installation d’un nouveau logiciel | Niveau 2 – Techniciens | Installation planifiée interne. |

> 🔁 *Chaque niveau correspond à un degré de technicité supérieur.*

---

## 🔧 Exercice 2.1 – Étapes du processus de gestion des changements

### Ordre correct :
1️⃣ Demande de changement  
2️⃣ Évaluation des risques  
3️⃣ Approbation du changement  
4️⃣ Planification du changement  
5️⃣ Test et validation  
6️⃣ Implémentation  
7️⃣ Révision post-implémentation

> 💬 *On ne déploie jamais un changement sans l’avoir évalué, approuvé et testé.*

---

## 🧩 Exercice 2.2 – Types de changements

| **Changement** | **Type** | **Approbation** | **Justification** |
|-----------------|-----------|-----------------|-------------------|
| Mise à jour de sécurité Windows | Standard | Pré-approuvée | Procédure routinière, faible risque. |
| Migration vers un nouveau serveur | Normal | CAB / Direction IT | Risque élevé, planification requise. |
| Redémarrage d’urgence du serveur web | Urgent | Responsable IT | Incident critique à corriger immédiatement. |
| Ajout d’un nouvel utilisateur | Standard | Automatique / Support | Opération fréquente et maîtrisée. |
| Changement d’architecture réseau | Normal | CAB / Direction | Impact important sur l’infrastructure. |

> 🧠 *Standard = routine / Normal = planifié / Urgent = immédiat*

---

## 📊 Exercice 3 – Cas d’entreprise

### **Problèmes constatés**
- Pannes répétées chaque semaine.  
- Appels directs aux techniciens.  
- Aucune documentation.  
- Changements non validés.

### **Processus ITIL à mettre en place**
| Processus | Objectif principal |
|------------|--------------------|
| Gestion des incidents | Centraliser les demandes et pannes. |
| Gestion des problèmes | Identifier et corriger les causes récurrentes. |
| Gestion des changements | Encadrer les modifications techniques. |
| Gestion des connaissances | Documenter et partager les solutions. |

### **Ordre de mise en œuvre**
1. Gestion des incidents → point d’entrée unique (outil de ticketing).  
2. Gestion des problèmes → analyse des causes profondes.  
3. Gestion des changements → validation et test avant déploiement.  
4. Gestion des connaissances → documentation et retours d’expérience.

### **Bénéfices attendus**
- Support plus efficace.  
- Moins de pannes récurrentes.  
- Changements mieux maîtrisés.  
- Capitalisation du savoir interne.

> 💡 *L’entreprise passe d’une logique “réactive” à une gestion “préventive et organisée”.*

---

## 🧾 Résumé général

| **Notion ITIL** | **Objectif clé** | **Exemple concret** |
|------------------|------------------|----------------------|
| Gestion des incidents | Rétablir le service rapidement | Redémarrer un serveur tombé en panne |
| Gestion des problèmes | Trouver la cause racine | Corriger un bug provoquant les pannes répétées |
| Gestion des changements | Modifier sans perturber | Déployer une mise à jour testée et validée |
| Gestion des connaissances | Capitaliser l’expérience | Créer une base de solutions dans GLPI |

---

> 🧠 **Phrase de conclusion à dire en classe :**  
> “ITIL, ce n’est pas de la technique, c’est de l’organisation.  
> On ne fait pas que réparer, on apprend à **éviter** que ça casse.”  
