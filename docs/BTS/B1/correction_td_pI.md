# Correction détaillée – Études de cas B1.1.1

## Cas 1 – Start-up logiciel (niveau débutant)

**Ressources clés :**

* PC Dev 1 et Dev 2 (Dell Latitude 3510, SSD rapide, garantie 3 ans)
* NAS Synology DS220+ (sauvegarde nocturne, garantie 2 ans)
* IDE Visual Studio Code + comptes GitHub
* Sage Start (licence annuelle, mise à jour trimestrielle)
* Routeur TP-Link et Switch 8 ports
* Imprimante HP LaserJet 1100

### 1. Ressources critiques

* NAS : contient toutes les données clients et projets → indisponible = arrêt du projet
* PC dev + IDE : nécessaire pour écrire et tester le logiciel
* Licences Sage Start : indispensable pour la comptabilité

### 2. Dépendances

* IDE dépend du PC Dev
* PC Dev dépend du NAS pour accéder aux projets
* Sage Start dépend du PC du comptable et des fichiers stockés sur le NAS
* Imprimante dépend du PC pour lancer les impressions

### 3. Sauvegardes

* NAS : sauvegarde automatique tous les soirs
* IDE / GitHub : versioning automatique du code
* Sage Start : export mensuel des données comptables

### 4. Améliorations possibles

* Installer un UPS pour NAS et PC critiques
* Vérifier régulièrement la capacité du NAS
* Centraliser les mises à jour des PC et logiciels

---

## Cas 2 – PME informatique (niveau intermédiaire)

**Ressources clés :**

* 10 PC fixes HP EliteDesk pour les devs
* 5 PC portables Lenovo pour chefs de projet
* Serveur Synology DS920+
* Serveur MySQL
* Réseau : 2 switches Netgear, firewall Fortinet
* IDE professionnels, logiciels de design, licences annuelles
* Comptes utilisateurs avec droits adaptés au rôle

### 1. Ressources critiques

* Serveur MySQL : base de données projet → panne = arrêt du développement
* PC dev + IDE : essentiels pour le développement et les tests
* Firewall et switches : sécurité réseau → vulnérabilité sinon

### 2. Dépendances

* IDE → PC dev → serveur fichiers → NAS
* Logiciels de design → PC chef de projet → serveur fichiers
* Accès comptes utilisateurs dépend du serveur AD/LDAP

### 3. Sauvegardes

* Serveur fichiers : backup quotidien sur NAS
* Serveur MySQL : dump quotidien + export hebdomadaire
* Logiciels : vérifier licences et mises à jour automatiques

### 4. Améliorations possibles

* Monitoring serveur MySQL + alertes email
* Vérification du firmware des switches et firewall
* Documenter les procédures de restauration en cas de panne
* Plan de maintenance périodique pour PC et serveurs

---

## Cas 3 – Grande société informatique (niveau avancé)

**Ressources clés :**

* 35 PC dev, 15 PC chefs de projet / QA
* Serveurs : Synology DS1821+, Exchange 2019, MySQL/PostgreSQL, serveur de test
* Réseau : routeurs et switches Cisco, firewall Fortinet
* Logiciels : IDE, suites bureautiques, logiciels métiers, licences annuelles
* Comptes AD/LDAP, droits selon rôle
* Documentation technique centralisée

### 1. Ressources critiques

* Serveur Exchange et NAS : messagerie et stockage projet → indisponible = blocage
* Serveur MySQL/PostgreSQL : bases de données → indisponible = projets bloqués
* PC Dev + IDE : développement impossible sans ces postes
* Firewall et switches : sécurité réseau → faille potentielle si défaillance

### 2. Dépendances

* IDE → PC Dev → Serveur fichiers → NAS
* PC chef de projet → logiciel de design / gestion projet → Serveur fichiers
* Serveur de test → accès aux serveurs de prod pour QA
* Documentation technique → accessible à tous → dépend serveur central

### 3. Sauvegardes

* Serveurs NAS et bases de données : snapshot quotidien + sauvegarde externe hebdomadaire
* Messagerie Exchange : backup quotidien + archivage mensuel
* PC dev et logiciels critiques : versioning code + sauvegarde configuration IDE

### 4. Améliorations possibles

* Mise en place d’un monitoring global SI
* Automatisation des sauvegardes et tests de restauration
* Vérification régulière des licences et mises à jour
* Séparation des serveurs de test et production
* Plan de continuité d’activité avec redondance ou serveur de secours


