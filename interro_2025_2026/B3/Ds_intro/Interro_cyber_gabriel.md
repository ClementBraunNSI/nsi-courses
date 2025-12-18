Devoir Surveillé -- BTS SIO

Système d'information et actifs

1)Un systèmes information est l'ensemble d'un groupe de matériels.
Actifs matériels, actifs logiciels et actifs humains.

2)Actifs matériel exemple un ordinateur, actifs logiciel exemple un
systèmes d'exploitation, actifs humain les employés, actifs
informationnelles exemple les donnés des clients et actifs immatériel
exemple la réputation de l'entreprise.

3)Si cela a la de la valeur, son importance dans l'entreprise.

Triade CIA

1)La confidentialité est le faite que les données sois accessible
seulement au personne autorisées.

L'intégrité est le faite que les données n'ont pas étaient modifier
intentionnellement ou accidentel.

La disponibilité est le faite que les données sont accessible quand
c'est nécessaire.

2\)

  --------------------------------------------- ----------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  Scénario                                      Pilier(s) compromis                       Justification
  Ransomware chiffre les serveurs de fichiers   Confidentialité Intégrité disponibilité   Car les données on étaient accessible par une personne externes elles ont étaient modifier et elles ne sont plus accessible
  Interception de mots de passe en transit      confidentialité                           Car les mots de passe on étaient récupéré
  Modification non autorisée des prix en base   intégrité                                 Car les données on étaient changer intentionnellement
  --------------------------------------------- ----------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

  ------------------------------- --------------- ------------------------------------------------------
  Panne électrique longue durée   disponibilité   Sans électricité les données ne sont plus accessible
  ------------------------------- --------------- ------------------------------------------------------

Menace, vulnérabilité, incident, risque

1)Une menace est le faite d'utiliser une faille pour faire des dégâts.

Une vulnérabilité est une faiblesse qui peut être utiliser.

Un incident est la réalisation d'une menace en utilisant une
vulnérabilité

Un risque est la probabilité que un évènement se produise et fasse des
dégâts

2\)

a)Vulnérabilité

b)Menace

c)Incident

d)Risque

Propriétés complémentaires de sécurité

1)Traçabilité est le faite de savoir retrouver qui à fait quelle action

Authenticité est de prouver l'identité d'une personne

Typologie des menaces -- classification rapide

+-------------+-------------+-------------+-------------+-------------+
| Humaines    | Humaines    | Technique   | Envir       | Légale      |
| int         | non         |             | onnementale |             |
| entionnelle | int         |             |             |             |
|             | entionnelle |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Groupe de   | Employé qui | Co          | Inondation  | CNIL        |
| hacker      | envoie par  | nfiguration | dans la     | constate    |
| ciblant un  | erreur un   | par défaut  | salle des   | une         |
| secteur     | document    | exposée sur | serveurs :  | non         |
| i           | c           | une base de | c'est une   | -conformité |
| ndustriel : | onfidentiel | données     | c           | RGPD        |
| attaque     | à un        |             | atastrophes |             |
| int         | mauvais     |             | naturelle   | Utilisation |
| entionnelle | des         |             |             | d'un        |
|             | tinataire : |             | Tremblement | logiciel    |
| Ransomware  | c'était une |             | de terre    | sans        |
| via         | erreur donc |             | impactant   | licences    |
| phishing :  | pas         |             | le          |             |
| attaque     | int         |             | d           |             |
| int         | entionnelle |             | atacenter : |             |
| entionnelle |             |             | c'est une   |             |
|             |             |             | c           |             |
|             |             |             | atastrophes |             |
|             |             |             | naturelle   |             |
+-------------+-------------+-------------+-------------+-------------+

QCM -- notions rapides

La disponibilité protège contre : interruption de services

Un ransomware compromet d'abord : l'intégrité

Un log centralisé sert principalement : traçabilité

La non-répudiation est garantie par : signature numérique

Une configuration par défaut exposé est une : vulnérabilité

Partie 2 -- étude de cas

Contexte

*Actifs et criticité*

1)Les employés : Actifs humains

Les données client : Actifs informationnels

La réputation de l'entreprise : Actifs immatériels

Le site : Actifs immatériels

Les serveurs : Actifs matériels

2)Les employés : faible

Les données client : élevée

La réputation de l'entreprise : critique : si la réputation de
l'entreprise est mauvaise le client ne vont plus venir acheté

Le site : critique : si on perds le site on n'a plus rien

Le serveur : critique : si on perds le serveur on ne peux plus rien le
temps de retrouver un serveur et on perd de l'argent

Triade CIA et scénarios

  ---- --------------------------------------------- --------------------- ----------------------
  N°   Scénario                                      Pilier(s) compromis   Mesure prioritaire
  1    Phishing sur comptable, vol d'identifiants    confidentialité       Formation
  2    DDoS sur le site e-commerce                   disponibilité         Service anti-DDoS
  3    Injection SQL sur formulaire de login         confidentialité       Tester la sécurisé
  4    Sauvegardes hors service pendant 3 semaines   disponibilité         Avoir des backups
  5    Employé mécontent exfiltre des données        confidentialité       Chiffrer les données
  ---- --------------------------------------------- --------------------- ----------------------

Menaces, vulnérabilité, incident, risques

  -------------------------------------------------- --------------- -----------------------------------------------
  élément                                            Catégorie       Justification
  Version obsolète d'Apache                          vulnérabilité   Car cela vas créée des failles
  Absence de MFA sur VPN                             menace          
  Groupe APT ciblant le secteur                      Incident        Car
  Chiffrement réussi de la base client               menace          
  Probabilité élevée de fuite de données sensibles   Risque          Car il y a probabilité qu'il y est des dégâts
  -------------------------------------------------- --------------- -----------------------------------------------

Attaques courantes

Phishing : La personne envoie un mail en se faisant passer pour une
entreprise

Le mail contient un lien vers un faut site

La victime mets ses vrai identifiants sur le faux site

La personne récupère le identifiants de la victime

l'intégrité et la confidentialité
