# 📋 Plan du Programme BTS SIO 1ère Année - Cybersécurité & Programmation

## 🎯 Vue d'ensemble du programme

Ce document présente le plan détaillé du programme de BTS SIO 1ère année pour les domaines de la **cybersécurité** et de la **programmation**, conformément au référentiel officiel.

---

## 🔐 BLOC 1 : CYBERSÉCURITÉ

### 📚 **Module 1 : Fondamentaux de la Cybersécurité**

#### 1.1 Introduction à la cybersécurité
- **Définitions et enjeux**
  - Qu'est-ce que la cybersécurité ?
  - Enjeux économiques et sociétaux
  - Panorama des menaces actuelles
  - Cadre légal et réglementaire (RGPD, LPM, etc.)

- **Typologie des menaces**
  - Malwares (virus, trojans, ransomwares, spywares)
  - Attaques par déni de service (DoS/DDoS)
  - Ingénierie sociale et phishing
  - Attaques par force brute
  - Man-in-the-middle
  - Zero-day exploits

#### 1.2 Principes fondamentaux de sécurité
- **Triade CIA (Confidentialité, Intégrité, Disponibilité)**
  - Confidentialité : protection contre l'accès non autorisé
  - Intégrité : protection contre la modification non autorisée
  - Disponibilité : garantie d'accès aux ressources

- **Principes complémentaires**
  - Authentification et autorisation
  - Non-répudiation
  - Traçabilité et auditabilité
  - Principe de moindre privilège
  - Défense en profondeur

### 📚 **Module 2 : Cryptographie et Chiffrement**

#### 2.1 Bases de la cryptographie
- **Histoire et évolution**
  - Cryptographie classique (César, Vigenère)
  - Cryptographie moderne
  - Évolution des besoins

- **Types de chiffrement**
  - Chiffrement symétrique (AES, DES, 3DES)
  - Chiffrement asymétrique (RSA, ECC)
  - Fonctions de hachage (SHA, MD5)
  - Signatures numériques

#### 2.2 Applications pratiques
- **Protocoles cryptographiques**
  - TLS/SSL
  - IPSec
  - PGP/GPG
  - Certificats numériques et PKI

- **Implémentation**
  - Choix des algorithmes
  - Gestion des clés
  - Bonnes pratiques de mise en œuvre

### 📚 **Module 3 : Sécurité des Applications**

#### 3.1 Vulnérabilités applicatives
- **OWASP Top 10**
  - Injection SQL
  - Authentification défaillante
  - Exposition de données sensibles
  - XXE (XML External Entities)
  - Contrôle d'accès défaillant
  - Mauvaise configuration de sécurité
  - Cross-Site Scripting (XSS)
  - Désérialisation non sécurisée
  - Composants avec vulnérabilités connues
  - Journalisation et surveillance insuffisantes

#### 3.2 Sécurisation du développement
- **Secure Coding**
  - Validation des entrées
  - Gestion des erreurs
  - Authentification et autorisation
  - Gestion des sessions
  - Protection contre les injections

- **Tests de sécurité**
  - Tests statiques (SAST)
  - Tests dynamiques (DAST)
  - Tests interactifs (IAST)
  - Pentesting applicatif

### 📚 **Module 4 : Gestion des Incidents et Réponse**

#### 4.1 Détection et analyse
- **Monitoring et surveillance**
  - SIEM (Security Information and Event Management)
  - IDS/IPS (Intrusion Detection/Prevention Systems)
  - Analyse de logs
  - Indicateurs de compromission (IoC)

#### 4.2 Réponse aux incidents
- **Processus de réponse**
  - Préparation
  - Identification et classification
  - Confinement
  - Éradication
  - Récupération
  - Retour d'expérience

- **Plan de continuité d'activité (PCA)**
  - Analyse d'impact métier (BIA)
  - Stratégies de récupération
  - Tests et mise à jour

---

## 💻 BLOC 2 : PROGRAMMATION

### 📚 **Module 1 : Algorithmique et Structures de Données**

#### 1.1 Algorithmique fondamentale
- **Concepts de base**
  - Variables, types de données
  - Structures conditionnelles
  - Boucles et itérations
  - Fonctions et procédures
  - Récursivité

- **Complexité algorithmique**
  - Notation Big O
  - Analyse temporelle et spatiale
  - Optimisation d'algorithmes

#### 1.2 Structures de données
- **Structures linéaires**
  - Tableaux et listes
  - Piles (Stack)
  - Files (Queue)
  - Listes chaînées

- **Structures arborescentes**
  - Arbres binaires
  - Arbres de recherche
  - Tas (Heap)

- **Structures de données avancées**
  - Tables de hachage
  - Graphes
  - Ensembles (Sets)

### 📚 **Module 2 : Programmation Orientée Objet (POO)**

#### 2.1 Concepts fondamentaux
- **Paradigme objet**
  - Classes et objets
  - Attributs et méthodes
  - Constructeurs et destructeurs
  - Encapsulation

#### 2.2 Principes avancés
- **Héritage**
  - Classes mères et filles
  - Surcharge et redéfinition
  - Polymorphisme
  - Classes abstraites et interfaces

- **Composition et agrégation**
  - Relations entre objets
  - Patterns de conception (Design Patterns)
  - Singleton, Factory, Observer

### 📚 **Module 3 : Langages de Programmation**

#### 3.1 Python
- **Syntaxe et fondamentaux**
  - Types de données Python
  - Structures de contrôle
  - Fonctions et modules
  - Gestion des exceptions

- **Programmation avancée**
  - Compréhensions de listes
  - Décorateurs
  - Générateurs
  - Programmation fonctionnelle

- **Bibliothèques spécialisées**
  - Requests (HTTP)
  - Cryptography (chiffrement)
  - Pandas (analyse de données)
  - Flask/Django (web)

#### 3.2 Java
- **Fondamentaux Java**
  - Syntaxe et structure
  - Types primitifs et objets
  - Collections Framework
  - Gestion des exceptions

- **Programmation avancée**
  - Threads et concurrence
  - Streams et lambda expressions
  - Annotations
  - Réflexion

#### 3.3 C/C++
- **Programmation système**
  - Gestion mémoire
  - Pointeurs et références
  - Compilation et édition de liens
  - Bibliothèques système

### 📚 **Module 4 : Développement Web**

#### 4.1 Technologies front-end
- **HTML5/CSS3**
  - Structure sémantique
  - Responsive design
  - Flexbox et Grid
  - Animations CSS

- **JavaScript**
  - DOM et événements
  - AJAX et Fetch API
  - Frameworks (React, Vue.js)
  - Node.js

#### 4.2 Technologies back-end
- **Serveurs web**
  - Apache, Nginx
  - Configuration et sécurisation
  - Reverse proxy et load balancing

- **Frameworks web**
  - Flask/Django (Python)
  - Spring Boot (Java)
  - Express.js (Node.js)

### 📚 **Module 5 : Bases de Données**

#### 5.1 Modélisation et conception
- **Modèle relationnel**
  - Entités et relations
  - Normalisation (1NF, 2NF, 3NF)
  - Contraintes d'intégrité
  - Diagrammes ERD

#### 5.2 Langage SQL
- **Requêtes de base**
  - SELECT, INSERT, UPDATE, DELETE
  - Jointures (INNER, LEFT, RIGHT, FULL)
  - Sous-requêtes
  - Fonctions d'agrégation

- **Administration**
  - Création de tables et index
  - Gestion des utilisateurs et droits
  - Sauvegarde et restauration
  - Optimisation des performances

#### 5.3 Sécurité des bases de données
- **Vulnérabilités**
  - Injection SQL
  - Élévation de privilèges
  - Exposition de données

- **Mesures de protection**
  - Requêtes préparées
  - Chiffrement des données
  - Audit et monitoring
  - Contrôle d'accès

---

## 🔗 BLOC 3 : INTÉGRATION CYBERSÉCURITÉ-PROGRAMMATION

### 📚 **Module 1 : Sécurité dans le Développement**

#### 1.1 DevSecOps
- **Intégration de la sécurité**
  - Security by Design
  - Shift-left security
  - Automatisation des tests de sécurité
  - Pipeline CI/CD sécurisé

#### 1.2 Outils et pratiques
- **Analyse de code**
  - SonarQube
  - Checkmarx
  - Veracode
  - OWASP ZAP

### 📚 **Module 2 : Programmation Sécurisée**

#### 2.1 Techniques de protection
- **Validation et sanitisation**
  - Validation côté client et serveur
  - Échappement de caractères
  - Whitelist vs Blacklist
  - Regex sécurisées

#### 2.2 Authentification et autorisation
- **Mécanismes d'authentification**
  - Mots de passe sécurisés
  - Authentification multi-facteurs (MFA)
  - OAuth 2.0 et OpenID Connect
  - JWT (JSON Web Tokens)

### 📚 **Module 3 : Projets Pratiques**

#### 3.1 Développement d'applications sécurisées
- **Application web sécurisée**
  - Authentification robuste
  - Gestion des sessions
  - Protection CSRF/XSS
  - Chiffrement des données

#### 3.2 Outils de cybersécurité
- **Scanner de vulnérabilités**
  - Développement d'un outil de scan
  - Détection d'injections SQL
  - Analyse de ports
  - Reporting automatisé

---

## 📊 ÉVALUATION ET COMPÉTENCES

### 🎯 **Compétences visées**

#### Cybersécurité
- Identifier et analyser les menaces
- Mettre en œuvre des mesures de protection
- Gérer les incidents de sécurité
- Auditer la sécurité d'un système

#### Programmation
- Concevoir et développer des applications
- Maîtriser plusieurs langages de programmation
- Implémenter des bases de données
- Respecter les bonnes pratiques de développement

### 📋 **Modalités d'évaluation**

#### Contrôle continu
- **QCM et tests théoriques** (30%)
  - Connaissances fondamentales
  - Analyse de cas pratiques
  - Veille technologique

- **Travaux pratiques** (40%)
  - Développement d'applications
  - Configuration sécurisée
  - Résolution de problèmes

- **Projets** (30%)
  - Projet de développement sécurisé
  - Audit de sécurité
  - Présentation et documentation

#### Certification
- **Préparation aux certifications**
  - CompTIA Security+
  - CISSP Associate
  - CEH (Certified Ethical Hacker)
  - Certifications développement (Oracle, Microsoft)

---

## 📚 RESSOURCES ET OUTILS

### 🛠️ **Environnements de développement**
- **IDE et éditeurs**
  - Visual Studio Code
  - IntelliJ IDEA
  - Eclipse
  - PyCharm

- **Outils de versioning**
  - Git et GitHub/GitLab
  - Workflows collaboratifs
  - Gestion des branches

### 🔧 **Outils de cybersécurité**
- **Analyse et test**
  - Wireshark
  - Metasploit
  - Burp Suite
  - OWASP ZAP

- **Monitoring et SIEM**
  - Splunk
  - ELK Stack
  - Nagios
  - OSSIM

### 📖 **Documentation et veille**
- **Sources officielles**
  - ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)
  - OWASP
  - NIST Cybersecurity Framework
  - ISO 27001/27002

- **Veille technologique**
  - CVE (Common Vulnerabilities and Exposures)
  - Bulletins de sécurité
  - Conférences (SSTIC, Black Hat, DEF CON)
  - Blogs spécialisés

---

## 🎯 OBJECTIFS PÉDAGOGIQUES PAR SEMESTRE

### **Semestre 1 (Septembre - Janvier)**
- **Fondamentaux de la cybersécurité**
- **Algorithmique et programmation de base**
- **Introduction aux langages (Python/Java)**
- **Bases de données relationnelles**

### **Semestre 2 (Février - Juin)**
- **Sécurité applicative et OWASP**
- **Programmation orientée objet avancée**
- **Développement web sécurisé**
- **Projet intégrateur cybersécurité-programmation**

---

## 📈 PROGRESSION PÉDAGOGIQUE

### **Niveau débutant (Mois 1-3)**
- Concepts théoriques fondamentaux
- Exercices guidés et tutoriels
- Environnement de développement sécurisé

### **Niveau intermédiaire (Mois 4-6)**
- Projets pratiques encadrés
- Analyse de cas réels
- Développement d'applications simples

### **Niveau avancé (Mois 7-9)**
- Projets autonomes
- Audit et pentesting
- Intégration de solutions complètes

---

*Ce plan est conforme au référentiel BTS SIO et peut être adapté selon les spécificités de l'établissement et les évolutions technologiques.*