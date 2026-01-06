Partie 1 -- Révision de cours (6 points)

Système d\'Information et actifs (1,5 point)

1\. Citer 3 catégories d\'actifs différentes et donner un exemple
concret pour chacune.

matériel, logiciel, informationnel, humain, immatériel

exemple : site web ; administrateur réseau ; hébergeur

2\. Expliquer ce qu\'est la criticité d\'un actif et donner 2 critères
qui l\'influencent.

La criticité 'un actif c'est le niveau d'importance en cas de problème
comme par exemple

administrateur : si il est pas en mesure de il peut avoir des problèmes
au niveau du réseau et la criticité peut être élevé a cause du fait que
personne ne puisse travailler car personne peut repérer le problème,
même chose pour l'hébergeur : si l'hébergeur a un problème la criticité
est élevé car le site web ne sera plus capable de fonctionner

Triade CIA (2 points)

1\. Définir Confidentialité, Intégrité, Disponibilité.

La confidentialité c'est le droit d'avoir accès a quelque chose ou non

L'intégrité c'est le d'avoir accès a quelque chose en ayant
l'autorisation de modifier le contenu donc de pouvoir faire des erreurs
de modifications

La disponibilité c'est le fait d'avoir un problème et donc de ne plus
pouvoir utiliser le résultat commis par l'attaque

2\. Associer chaque scénario au(x) pilier(s) compromis et justifier:

+-----------------------+-------------------+-----------------------+
| Scenario              | Pilier compromis  | Justification         |
+-----------------------+-------------------+-----------------------+
| Un administrateur     | Intégrité         | C'est un problème     |
| modifie               |                   | d'intégrité car       |
| accidentellement la   |                   | l'administrateur a    |
| configuration d\'un   |                   | modifier la           |
| routeur,              |                   | configuration donc il |
|                       |                   | a potentiellement     |
| causant des pertes de |                   | perdu des données qui |
| paquets               |                   | se trouvé dans les    |
|                       |                   | paquets               |
+-----------------------+-------------------+-----------------------+
| Un mail confidentiel  | Confidentialité   | Car tous les employé  |
| est envoyé par erreur |                   | ou accès au mail en   |
| à tous les employés   |                   | sachant qu'il était   |
|                       |                   | confidentiel donc     |
|                       |                   | certaine personne ne  |
|                       |                   | sont donc pas         |
|                       |                   | autorisé a le         |
|                       |                   | recevoir              |
+-----------------------+-------------------+-----------------------+
| Une attaque DDoS rend | Disponibilité     | L'attaque DdoS a      |
| le site web           |                   | poser des problèmes   |
| inaccessible pendant  |                   | sur le site web qui   |
| 6 heures              |                   | la rendu inaccessible |
|                       |                   | donc le site n'est    |
|                       |                   | plus disponible       |
|                       |                   | pendant en certain    |
|                       |                   | temps ce qui pose des |
|                       |                   | éventuel problème     |
+-----------------------+-------------------+-----------------------+

Menace, vulnérabilité, incident, risque (1,5 point)

1\. Donner une définition courte de chacun des 4 termes.

Menaces : c'est un problème qui est lié a l'attaque de quelque chose

vulnérabilité : c'est le fait du niveau d'empileur que ça peut prendre

incident : c'est le fait de ne plus pouvoir utilisé quelque chose a
cause d'un accident

risque : par exemple quel sont les risques de changer une bornes wifi a
ce moment la : plus d'accès a internet le temps du remplacement c'est un
risque

2\. Classer les situations ci-dessous et justifier en une phrase:

a\) Les mots de passe administrateurs sont stockés dans un fichier Excel
non protégé c'est un risque car si une personne malveillante a accès a
ce dossier elle peut faire de lourd problèmes

b\) Un groupe de hackers spécialisé dans les ransomwares cible le
secteur de la santé c'est une menace car c'est le début d'une attaque si
il cible

c\) Un employé clique sur un lien de phishing et installe un malware sur
son poste c'est un incident car la personne a cliquer sur un lieu et
cela peut avoir de lourdes conséquences

QCM --- notions rapides (1 point)

Donner la bonne réponse et justifier en une phrase:

1\. L\'intégrité protège contre: (A) divulgation de données, (B)
interruption de service, (C) altération de données car c'est le fait
d'agir sur quelque chose

2\. La propriété de non-répudiation permet de: (A) chiffrer les données,
(B) prouver qu\'une action a été faite par quelqu\'un, (C) bloquer les
virus car il prouve ce qu'il a fait avec la non-repuciation

3\. Un serveur web obsolète non patché depuis 1 an est une: (A) menace,
(B) vulnérabilité, (C) incident car on sais qu'il est obsolète donc il
est vulnérable car il est facile d'accès

Partie 2 -- Étude de cas (12 points)

Étape 1 -- Actifs et criticité (3 points)

1\. Lister 4 actifs de BioLab et les classer par catégorie (matériel,
logiciel, informationnel, humain, immatériel).

1 Le nom accès au dossier des patients( informationnel car dossier
dématérialisé )

2 blocage des ordinateur de contrôle (matériel car pas possible
d'utiliser le numérique)

3 Blocage du logiciel de gestion (logiciel car pas possible de gérer les
doses comme il le faut )

4 problème d'identifiant personnel (humain car pas de personnel
disponible)

2\. Donner une criticité (faible/moyenne/élevée/critique) pour chaque
actif et justifier les 2 plus critiques.

1:forte car on ne peut pas savoir les problèmes du patient

2 :critique car on ne peut pas utiliser les outils pour sauver des vie
grâce au analyse

3 :moyenne

4 :faible

Étape 2 -- Typologie des menaces (3 points)

  --------------------------------------------------------------------- ----------------------------- -------------------------------------------------------------------
  Situation                                                             Categorie                     justifiaction
  Un technicien de maintenance insère une clé USB infectée par erreur   Humaine non- intentionnelle   Le technicien a comis l'erreur d'inserer une clé usb infectée
  Une inondation endommage la salle serveurs située au sous-sol         Environementale               Probleme meteorologique a cause d'une inondation
  Un concurrent tente de voler la base de données clients               Techniquer                    Un concurent essaye de voler la base de donée avec une technique
  La CNIL sanctionne le laboratoire pour non-conformité RGPD            Legale                        La cnil effectue sont travailler car c'est non conforme au RGPD
  --------------------------------------------------------------------- ----------------------------- -------------------------------------------------------------------

Étape 3 -- Scénarios CIA et mesures (3 points)

Étape 4 -- Calcul du risque (3 points)
