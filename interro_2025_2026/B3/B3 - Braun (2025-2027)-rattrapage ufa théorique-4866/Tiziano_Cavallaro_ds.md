Devoir Surveillé -- BTS SIO 1ère année (B3)

Partie 1 -- Révision de cours (6 points)

Système d\'Information et actifs (1,5 point)

1\. Citer 3 catégories d\'actifs différentes et donner un exemple
concret pour chacune.

2\. Expliquer ce qu\'est la criticité d\'un actif et donner 2 critères
qui l\'influencent

\- matériel : un clavier, souris\...

\- logiciel : avast, un antivirus

\- informationnel : pouvoir rechercher sur le web des informations qu'il
nous faut...

La criticité d'un actif c'est comme par exemple si un risque est faible,
moyen, grand \...

Triade CIA (2 points)

1\. Définir Confidentialité, Intégrité, Disponibilité.

2\. Associer chaque scénario au(x) pilier(s) compromis et justifier:

1\.

\- confidentialité c'est le fait de garder des informations secrètes

\- Intégrité c'est le fait de rajouter des informations

\- Disponibilité c'est le fait de pouvoir rajouter des informations

2\.

+----------------------+----------------------+----------------------+
| Scénario             | Pilier(s)            | Justification        |
|                      |                      |                      |
|                      | compromis            |                      |
+----------------------+----------------------+----------------------+
| Un administrateur    | Il y a un virus      | Il faut faire        |
| modifie              |                      | attention à          |
| accidentellement la  |                      | l'endroit où l'on    |
| configuration d\'un  |                      | clique               |
| routeur,             |                      |                      |
|                      |                      |                      |
| causant des pertes   |                      |                      |
| de paquets           |                      |                      |
+----------------------+----------------------+----------------------+
| Un mail confidentiel | Une personne à       | Si on ne choisis pas |
| est envoyé par       | pirater le compte    | de bon mot de passe  |
| erreur à tous les    |                      | sécurisé on risque   |
| employés             |                      | de se le faire       |
|                      |                      | cracker en brut      |
|                      |                      | force                |
+----------------------+----------------------+----------------------+
| Une attaque DDoS     | Fuite de l'adresse   | Si une personne      |
| rend le site web     | ipv4                 | possède l'ip de      |
| inaccessible pendant |                      | notre site, si on a  |
| 6 heures             |                      | pas de antiddos la   |
|                      |                      | personne             |
|                      |                      | malveillante peu     |
|                      |                      | faire de gros dégats |
+----------------------+----------------------+----------------------+

Menace, vulnérabilité, incident, risque (1,5 point)

1\. Donner une définition courte de chacun des 4 termes.

2\. Classer les situations ci-dessous et justifier en une phrase:

a\) Les mots de passe administrateurs sont stockés dans un fichier Excel
non protégé

b\) Un groupe de hackers spécialisé dans les ransomwares cible le
secteur de la santé

c\) Un employé clique sur un lien de phishing et installe un malware sur
son poste

1\.

Menace : Une menace est un considéré comme un virus

vulnérabilité : c'est lorsque on coupe notre antivirus et la protection
réel de l'ordinateur, il peut y avoir des virus

incident : un incident c'est quand on va faire une action du genre,
cliquer sur un lien de phishing

risque : un risque est tout simplement le fait que sur les sites il peu
y avoir pas mal de virus donc il ne faut pas trop prendre de risques en
allant sur des sites non sécurisé

2\.

Les mots de passe administrateurs sont stockés dans un fichier Excel non
protégé

Un employé clique sur un lien de phishing et installe un malware sur son
poste

Un groupe de hackers spécialisé dans les ransomwares cible le secteur de
la santé

justification : lorsque les mots de passes sont stocké dans un fichier
excel non sécurisé et qu'un employé clique sur un lien de phishing, les
hackers peuvent attaquer et réussir leur coup.

QCM --- notions rapides (1 point)

Donner la bonne réponse et justifier en une phrase:

1\. L\'intégrité protège contre: (A) **divulgation de données,** (B)
interruption de service, (C) altération de données : Car cela protège
l'intégralité des données stockés

2\. La propriété de non-répudiation permet de: (A) chiffrer les données,
(B) **prouver qu\'une action a été faite par quelqu\'un**, (C) bloquer
les virus : car la propriété est la pour savoir si cela a été fait par
une personne

3\. Un serveur web obsolète non patché depuis 1 an est une: (A) menace,
(B) **vulnérabilité**, (C) incident : au bout de 1 an sans mise à jours
il peut que être vulnérable donc ça ouvre des portes aux hackeurs

Partie 2 -- Étude de cas (12 points)

Étape 1 -- Actifs et criticité (3 points)

1\. Lister 4 actifs de BioLab et les classer par catégorie (matériel,
logiciel, informationnel, humain, immatériel).

2\. Donner une criticité (faible/moyenne/élevée/critique) pour chaque
actif et justifier les 2 plus critiques

Étape 2 -- Typologie des menaces (3 points)

Classer chaque situation dans la bonne catégorie (Humaine intentionnelle
/ Humaine non intentionnelle / Technique /

+----------------------+----------------------+----------------------+
| Scénario             | Pilier(s)            | Mesure               |
|                      |                      |                      |
|                      | compromis            | prioritaire          |
+----------------------+----------------------+----------------------+
| Un technicien de     | Humaine non          | C'est pas une action |
| maintenance insère   | intentionnelle       | qu'il veut faire     |
| une clé USB infectée |                      | donc ce n'est pas    |
| par erreur           |                      | intionné             |
+----------------------+----------------------+----------------------+
| Une inondation       | Technique            | Cela peu provenir    |
| endommage la salle   |                      | d'une panne          |
| serveurs située au   |                      | technique            |
| sous-sol             |                      |                      |
+----------------------+----------------------+----------------------+
| Un concurrent tente  | Humaine              | Le concurent est     |
| de voler la base de  | intentionnelle       | jaloux donc tente de |
| données clients      |                      | voler la base de     |
|                      |                      | données d'un de ses  |
| panne                |                      | clients donc c'est   |
|                      |                      | forcémement          |
|                      |                      | intentionnel         |
+----------------------+----------------------+----------------------+
| La CNIL sanctionne   | Légale               | Le CNIL fait une     |
| le laboratoire pour  |                      | bonne action pour    |
| non-conformité RGPD  |                      | son environnement    |
+----------------------+----------------------+----------------------+

Étape 3 -- Scénarios CIA et mesures (3 points)

Associer chaque scénario au(x) pilier(s) compromis et proposer UNE
mesure de protection prioritaire.

+-------------------------+---------------+-------------------------+
| Scénario                | Pilier(s)     | Mesure                  |
|                         |               |                         |
|                         | compromis     | prioritaire             |
+-------------------------+---------------+-------------------------+
| Employé mécontent       | environnement | La personne ne sait pas |
| exfiltre des résultats  |               | se que ça peu faire sur |
| d\'analyses sensibles   |               | l'environnement         |
+-------------------------+---------------+-------------------------+
| Attaque par force brute |               |                         |
| sur le portail web des  |               |                         |
| résultats patients      |               |                         |
+-------------------------+---------------+-------------------------+
| Les sauvegardes sont    |               |                         |
| hors service depuis 1   |               |                         |
| mois suite à une        |               |                         |
|                         |               |                         |
| panne                   |               |                         |
+-------------------------+---------------+-------------------------+
