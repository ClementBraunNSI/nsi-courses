# B3 — Corrections TD 1 : Introduction à la cybersécurité

> Corrections des exercices issus du cours `Introduction_cybersecurite.md`.

## Correction — Exercice 1 : Identification et classification des actifs

### Classification des actifs

| N° | Actif | Catégorie |
|---:|---|---|
| 1 | Serveur hébergeant le site e-commerce | Matériel |
| 2 | Base de données clients (informations personnelles et historiques d’achat) | Informationnel |
| 3 | Site web e-commerce (application développée en interne) | Logiciel |
| 4 | Ordinateurs des employés (postes de travail) | Matériel |
| 5 | Responsable informatique (administrateur réseau/système) | Humain |
| 6 | Réputation et avis clients sur Internet | Immatériel |
| 7 | Fichier comptable annuel (bilan, factures, salaires) | Informationnel |
| 8 | Routeur et pare-feu de l’entreprise | Matériel |
| 9 | Logiciel de gestion des stocks | Logiciel |
| 10 | Employé du service client | Humain |
| 11 | Nom de domaine "techstore.fr" | Immatériel |
| 12 | Données de connexion (identifiants employés) | Informationnel |

### Classement par criticité (1 = le plus critique)

- 1. Base de données clients (données personnelles, cœur du business)
- 2. Serveur hébergeant le site e-commerce (indispensable pour la vente)
- 3. Site web e-commerce (application critique métier)
- 4. Nom de domaine "techstore.fr" (indisponibilité = site inaccessible)
- 5. Routeur et pare-feu (sécurité périmétrique, disponibilité du réseau)
- 6. Données de connexion (risque d’accès non autorisé)
- 7. Fichier comptable annuel (obligations légales et fiscales)
- 8. Logiciel de gestion des stocks (processus logistique)
- 9. Réputation et avis clients (impact fort mais indirect et différé)
- 10. Responsable informatique (ressource clé mais remplaçable en cas d’absence)
- 11. Ordinateurs des employés (impact local et maîtrisable)
- 12. Employé du service client (impact ponctuel, substituabilité)

Justifications des 3 premiers actifs:
- 1. Base de données clients: contient des données personnelles et l’historique d’achat; impact juridique (RGPD), réputationnel et financier majeur en cas de fuite.
- 2. Serveur du site: sa compromission ou indisponibilité arrête immédiatement les ventes; impact opérationnel et financier direct.
- 3. Application e-commerce: sans l’application, pas de parcours client ni de transaction; indisponibilité et intégrité critiques.

---

## Correction — Exercice 2 : Association piliers CIA et scénarios

| Scénario | Pilier(s) compromis | Justification |
|---:|---|---| 
| 1 | Disponibilité (principal), Intégrité (modification non autorisée par chiffrement) | Ransomware rend les fichiers inaccessibles; le chiffrement altère l’état attendu des données. |
| 2 | Disponibilité | Mauvaise configuration réseau entraîne indisponibilités/erreurs de transmission. |
| 3 | Confidentialité (principal), Intégrité (potentielle en MITM) | Interception des identifiants violant la confidentialité; MITM peut aussi altérer des échanges. |
| 4 | Disponibilité | Panne électrique prolongée rendant les systèmes indisponibles. |
| 5 | Intégrité | Modification frauduleuse de données (adresses) altère les informations. |
| 6 | Confidentialité | Diffusion non intentionnelle d’informations confidentielles à un public non autorisé. |

---

## Correction — Exercice 3 : Menace / vulnérabilité / risque / incident

| N° | Type | Justification |
|---:|---|---|
| 1 | Vulnérabilité | Logiciel obsolète (Apache 2018) expose des failles connues. |
| 2 | Menace | Groupe malveillant identifié ciblant un secteur. |
| 3 | Risque | Combinaison vraisemblance × impact chiffré (200 k€). |
| 4 | Vulnérabilité | Manque de sensibilisation = faiblesse organisationnelle/humaine. |
| 5 | Vulnérabilité | Mots de passe administrateurs accessibles à tous, non protégés. |

---

## Correction — Exercice 4 : Classification des menaces et mesure

| N° | Catégorie | Mesure de protection proposée |
|---:|---|---|
| 1 | Humaine intentionnelle | Revue de code systématique, séparation des rôles, CI/CD avec scans SAST, journalisation et traçabilité. |
| 2 | Humaine non intentionnelle | Sensibilisation/DLP, double vérification destinataires, bannières d’avertissement mails externes. |
| 3 | Technique | Gestion des correctifs (patch management), segmentation réseau, IDS/IPS. |
| 4 | Environnementale | Local technique adapté, PRA/PCA, sauvegardes hors site, capteurs anti-inondation. |
| 7 | Humaine non intentionnelle | Validation par pair, règles de configuration, formation. |
| 8 | Environnementale | Site de secours/Cloud, protections sismiques, redondance, assurance. |
| 9 | Légale | Programme RGPD, DPO, registre des traitements, DPIA, politiques et preuves de conformité. |
| 10 | Technique | Anti-DDoS (CDN/WAF), filtrage, surdimensionnement, architecture résiliente. |

---

## Correction — Exercice 5 : Étude de cas — MediCare

### 1) Type d’attaque initial
- Phishing (hameçonnage) ciblé conduisant au vol d’identifiants.

### 2) Vulnérabilités ayant permis l’attaque (exemples)
- Absence de MFA sur le VPN. 
- Pas de segmentation réseau (mouvements latéraux facilités). 
- Sauvegardes absentes ou non testées. 
- Droits administrateur sur tous les postes. 
- Aucune sensibilisation au phishing. 
- Surveillance insuffisante des connexions distantes (détection tardive). 

### 3) CIA compromis et comment
- Confidentialité: probable exfiltration/accès non autorisé aux dossiers médicaux. 
- Intégrité: chiffrement par ransomware modifie l’état des données; possible altération. 
- Disponibilité: indisponibilité totale des dossiers et des services (annulations). 

### 4) Conséquences
- Financières: interruption d’activité, pertes de revenus, coûts de remédiation/forensics, potentielle rançon. 
- Opérationnelles: opérations annulées, rendez-vous impossibles, désorganisation. 
- Juridiques: obligations RGPD (notification), risque de sanctions, audits. 
- Réputationnelles: perte de confiance patients/partenaires, médiatisation négative. 

### 5) Mesures prioritaires (prévention)
- Activer MFA sur accès distants et comptes sensibles. 
- Mettre en place sauvegardes 3-2-1, hors ligne et tests de restauration. 
- Segmenter le réseau (VLANs, règles de pare-feu). 
- Réduire les privilèges (principe du moindre privilège et comptes séparés). 
- Sensibiliser tout le personnel au phishing (campagnes et simulations). 

### 6) Notification CNIL
- Oui, si des données personnelles ont été exposées/à risque: notification à la CNIL dans les 72 heures (RGPD), et communication aux personnes concernées si risque élevé pour leurs droits et libertés.

---

## Correction — Exercice 6 : Calcul de risque pratique (DDoS)

### 1) Menace / vulnérabilités / actif
- Menace: attaque DDoS par botnet. 
- Vulnérabilités: serveur unique mutualisé, absence d’anti-DDoS, hébergeur sans mitigation, exposition publique du service critique. 
- Actif: site web e-commerce (revenus, image, continuité).

### 2) Vraisemblance (1–5)
- Élevée (4/5): secteur régulièrement visé, protections inexistantes, ciblage opportuniste.

### 3) Impact (1–5)
- Financier: 3–5 jours × 5 000€/jour = 15k–25k; perdus + coûts remédiation.
- Opérationnel: arrêt des commandes, support débordé, backlog.
- Réputationnel: insatisfaction clients, avis négatifs.
- Impact global: Majeur (3/5) à Critique (4/5). Retenue: 3/5.

### 4) Calcul du risque
- Risque = 4 × 3 = 12 → Élevé.

### 5) Mesures (coûts)
- Anti-DDoS/Protection amont (Cloudflare/Akamai/WAF) — 1 000€/an. 
- CDN et cache agressif pour pages publiques — 300€/an. 
- Architecture résiliente (hébergement dédié ou multi-régions, autoscaling) — 3 000€ mise à niveau.

### 6) Risque résiduel
- Nouvelle vraisemblance: 2/5 (mitigation amont efficace). 
- Impact: 2/5 (dégradation mais service maintenu ou reprise rapide). 
- Risque résiduel = 2 × 2 = 4 → Moyen (acceptable avec veille continue).

---

## Correction — Exercice 7 : Application EBIOS simplifiée (PetitCommerce)

### Étape 1 — Périmètre
- Biens essentiels: site de vente, données clients/commandes/paiements, service de paiement. 
- Biens supports: serveur web, BDD MySQL, code PHP, DNS/domaine, passerelle paiement, réseau, postes back-office. 
- Parties prenantes: clients, support, direction, PSP (fournisseur de paiement), hébergeur, CNIL.

### Étape 2 — Événements redoutés
- ER1: Fuite de données clients (C) — Gravité 4/4. 
- ER2: Frauduleuse modification de commandes/prix (I) — Gravité 3/4. 
- ER3: Indisponibilité du site en période de soldes (D) — Gravité 4/4.

### Étape 3 — Scénarios de menace (sur ER1)
- Scénario A: Phishing d’un administrateur → vol d’identifiants → export BDD. Source: cybercriminel; motivation: gain; capacité: moyenne. 
- Scénario B: Injection SQL sur formulaire vulnérable → dump BDD. Source: attaquant externe; motivation: gain/revente; capacité: moyenne/élevée.

### Étape 4 — Vraisemblance et impact
- Scénario A: Vraisemblance 3/5; Impact global 4/5 (financier, juridique RGPD, réputationnel) → Risque = 12 (Élevé). 
- Scénario B: Vraisemblance 4/5 (historique courant); Impact global 4/5 → Risque = 16 (Critique).

### Étape 5 — Mesures (priorisées)
- A1: MFA administrateurs et accès distants (Priorité 1) — 300€/an, 2 semaines. 
- A2: Sensibilisation phishing + bannières mails (P1) — 500€, 2 semaines. 
- A3: SIEM/alertes connexions suspectes (P2) — 2 000€/an, 1 mois. 
- B1: Requêtes préparées/ORM + revue code (P1) — 1 500€, 3 semaines. 
- B2: WAF + rules OWASP (P1) — 800€/an, 1 semaine. 
- B3: Tests sécu réguliers (SAST/DAST) (P2) — 1 200€/an, 1 mois.

### Étape 6 — Plan d’action et risque résiduel

| Mesure | Priorité | Coût | Délai | Scénarios traités | Effet |
|---|---:|---:|---:|---|---|
| MFA admins | 1 | 300€/an | 2 sem. | A | ↓ Vraisemblance A à 2 |
| Sensibilisation phishing | 1 | 500€ | 2 sem. | A | ↓ Vraisemblance A à 2 |
| WAF + OWASP | 1 | 800€/an | 1 sem. | B | ↓ Vraisemblance B à 2 |
| Requêtes préparées/ORM | 1 | 1 500€ | 3 sem. | B | ↓ Vraisemblance B à 2 |
| SAST/DAST | 2 | 1 200€/an | 1 mois | B | ↓ Impact (détection précoce) |
| SIEM/Alertes | 2 | 2 000€/an | 1 mois | A | ↓ Impact (réaction rapide) |

Risque résiduel estimé: 
- A: 2 × 3 = 6 → Moyen. 
- B: 2 × 3 = 6 → Moyen.

---

## Correction — Exercice 8 : Sélection de mesures de sécurité (cabinet médical)

Hypothèses de risques prioritaires (cohérents avec un cabinet médical de 5 médecins):
- R1: Ransomware sur serveurs/PC → indisponibilité dossiers patients (D), risque de fuite (C). 
- R2: Fuite de données patients (C) via vol identifiants/mauvaise pratique. 
- R3: Indisponibilité du système de rendez-vous (D) en heure ouvrée. 
- R4: Perte/vol d’équipements mobiles contenant des données (C). 
- R5: Non-conformité RGPD/documentation insuffisante (J).

Mesures proposées (équilibrées, par type):
- Organisationnelles: 
  - PSSI et politiques RGPD (registre, bases légales, DPIA si nécessaire). 
  - Sensibilisation régulière (phishing, mots de passe, confidentialité). 
  - Procédure de réponse aux incidents (rôles, notification CNIL ≤ 72h). 
- Techniques: 
  - Sauvegardes 3-2-1, hors ligne, tests mensuels; PRA/PCA. 
  - MFA sur accès sensibles (dossiers médicaux, VPN), chiffrement disque (BitLocker/FileVault). 
  - WAF/anti-DDoS pour portail patient, durcissement des postes, mises à jour automatiques. 
  - Gestionnaire de mots de passe + politique de complexité/rotation. 
- Physiques: 
  - Contrôle d’accès aux locaux (badges), baies verrouillées. 
  - Détection incendie/UPS pour continuité, verrouillage des postes.

Exemple d’adéquation mesure ↔ risque:
- R1: Sauvegardes 3-2-1, EDR, moindre privilège, segmentation réseau. 
- R2: MFA, chiffrement au repos/en transit, DLP et sensibilisation confidentialité. 
- R3: Hébergement résilient + supervision, PRA, anti-DDoS/CDN. 
- R4: Chiffrement complet des terminaux, gestion des inventaires, verrouillage physique. 
- R5: DPO (interne/externe), registre des traitements, chartes utilisateurs, preuve de conformité.

Estimation simple coût/délai (ordre de grandeur):
- Sensibilisation: 500€ / 2 semaines; Sauvegardes: 1 500€ + 200€/an / 3 semaines; 
- MFA: 300€/an / 2 semaines; EDR: 1 000€/an / 2 semaines; 
- DLP/WAF/CDN: 1 000–2 000€/an / 2–4 semaines.

---

> Remarque: certaines ordonnances peuvent varier selon le contexte exact; les justifications ci-dessus respectent les principes du cours et fournissent une base solide et argumentée.