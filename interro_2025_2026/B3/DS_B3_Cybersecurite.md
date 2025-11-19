# Devoir Surveillé – BTS SIO 2e année (B3)

## Introduction à la cybersécurité

**Durée totale : 2 heures 15**  
**Partie 1 (40 min)** – Questions de cours  
**Partie 2 (1h35)** – Étude de cas et analyse de risque

La justification, la rigueur, la rédaction et le soin de la copie entrent dans la notation sur 2 points. Un manquement de ces 4 critères entraîne une perte de 2 points.

---

## Partie 1 – Révision de cours (8 points)

### Système d’Information et actifs

1. Définir un **Système d’Information (SI)** et donner 3 exemples d’actifs.  
2. Citer **5 catégories d’actifs** et donner un exemple pour chacune.  
3. Expliquer la notion de **criticité** d’un actif et donner 3 critères qui l’influencent.

---

### Triade CIA

1. Définir **Confidentialité**, **Intégrité**, **Disponibilité**.  
2. Associer chaque scénario au(x) pilier(s) compromis et justifier succinctement:

| Scénario | Pilier(s) compromis | Justification |
|---|---|---|
| Ransomware chiffre les serveurs de fichiers |  |  |
| Interception de mots de passe en transit |  |  |
| Modification non autorisée des prix en base |  |  |
| Panne électrique longue durée |  |  |

---

### Menace, vulnérabilité, incident, risque

1. Donner une **définition** courte de chacun des termes.  
2. Classer les situations ci-dessous et justifier:  
   a) Serveur web non patché depuis 6 mois  
   b) Groupe de cybercriminels ciblant le secteur  
   c) Compromission réussie d’un poste par phishing  
   d) Probabilité élevée d’attaque avec impact majeur

---

### Mesures de sécurité

1. Proposer 3 **mesures techniques** contre le phishing.  
2. Proposer 3 **mesures organisationnelles** pour réduire les risques internes.

---

## Partie 2 – Étude de cas (18 points)

### Contexte

« PetitCommerce » est une boutique en ligne (10 personnes). Le site web (PHP/MySQL) représente 95% du chiffre d’affaires. Vous réalisez une **analyse de risque** sur le périmètre du service e‑commerce.

### Étape 0 – Définitions appliquées (2 points)

1. Dans le **périmètre PetitCommerce**, donner une définition concise et contextualisée de :  
   a) Menace  
   b) Vulnérabilité  
   c) Incident  
   d) Risque  
2. Associer un **exemple concret** à chacune des définitions (lié à l’activité e‑commerce).

### Étape 1 – Actifs et criticité (3 points)

1. Lister 10 actifs et les **classer par catégorie**.  
2. Donner une **criticité** (faible/moyenne/élevée/critique) pour 5 actifs et **justifier** les 3 plus élevés.

| N° | Actif | Catégorie | Criticité | Justification |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |
| 10 |  |  |  |  |

### Étape 2 – Triade CIA et scénarios (3 points)

Associer chaque scénario au(x) pilier(s) compromis et proposer **une mesure de protection** prioritaire.

| N° | Scénario | Pilier(s) compromis | Mesure prioritaire |
|---|---|---|---|
| 1 | Phishing sur comptable, vol d’identifiants |  |  |
| 2 | DDoS sur le site e‑commerce |  |  |
| 3 | Injection SQL sur formulaire de login |  |  |
| 4 | Sauvegardes hors service pendant 3 semaines |  |  |
| 5 | Employé mécontent exfiltre des données |  |  |

### Étape 3 – Menaces, vulnérabilités, incidents, risques (3 points)

Compléter le tableau.

| Élément | Catégorie | Justification |
|---|---|---|
| Version obsolète d’Apache |  |  |
| Absence de MFA sur VPN |  |  |
| Groupe APT ciblant le secteur |  |  |
| Chiffrement réussi de la base clients |  |  |
| Probabilité élevée de fuite de données sensibles |  |  |

### Étape 4 – Calcul du risque et matrice (3 points)

Utiliser l’échelle 1–5 pour la **vraisemblance** et l’**impact**. Calculer **Risque = Vraisemblance × Impact**. Classer 5 risques et identifier le **Top 3**.

| Risque | Vraisemblance (1–5) | Impact (1–5) | Score | Priorité |
|---|---|---|---|---|
| R1 |  |  |  |  |
| R2 |  |  |  |  |
| R3 |  |  |  |  |
| R4 |  |  |  |  |
| R5 |  |  |  |  |

Proposer, pour les 3 risques prioritaires, **une mesure** de **réduction**, **transfert**, **éviter** ou **accepter** et justifier.

| Risque prioritaire | Traitement | Mesure proposée | Justification |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

### Étape 5 – Architecture de sécurité du e‑commerce (2 points)

Cartographier une **architecture de sécurité minimale** pour le site e‑commerce en distinguant les **zones de confiance** et les **contrôles**:

- Zones: Internet, **DMZ** (serveur web/WAF), **LAN** (admin/back‑office), **Base de données**  
- Contrôles: **WAF/Reverse proxy**, pare‑feu L3/L7, **IDS/IPS**, **VPN** admin, **journalisation centralisée** (SIEM)  
- Flux principaux: Clients → WAF → Serveur web → Base de données ; Admins → VPN → LAN ; Sauvegardes ; Exposition publique

Compléter le tableau:

| Composant | Zone | Contrôles en place | Risque en cas de mauvaise configuration |
|---|---|---|---|
| Serveur web | DMZ |  |  |
| Base de données | LAN |  |  |
| Accès administrateurs | LAN |  |  |
| Journalisation/SIEM | LAN |  |  |
| Pare‑feu (frontière) | DMZ/LAN |  |  |

Proposer **3 indicateurs de supervision** pertinents (ex: taux d’erreurs 5xx, volume de tentatives bloquées WAF, pics de latence).

### Étape 6 – Conformité RGPD et notification CNIL (2 points)

À partir d’un scénario d’incident (ex: fuite de données clients):

1. Déterminer s’il s’agit d’une **violation de données personnelles** et si la **notification** à la **CNIL (72h)** et aux personnes concernées est requise. **Justifier**.  
2. Rédiger la **trame de notification**: nature de la violation, catégories de données/personnes, nombre de personnes impactées, conséquences, mesures prises/proposées.  
3. Préciser les **rôles** et la **gouvernance**: DPO, RSSI, Direction ; registre des traitements à mettre à jour ; preuves et traçabilité.  
4. Proposer 3 **mesures préventives** pour réduire la probabilité/l’impact (ex: MFA, chiffrement au repos/en transit, formation phishing).