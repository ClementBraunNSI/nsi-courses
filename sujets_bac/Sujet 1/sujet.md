# Epreuve pratique BAC NSI

## Sujet 1 - Prédiction de la présence d'un renard dans un habitat donné

Le renard est un animal qui peut habiter dans plusieurs types d'habitats que ce soient des plaines, montagnes, environnements ruraux, périurbains voire dans de très faibles chances urbains.
La loi Biodiversité 2016 et l'arrêté du 3 aout 2023 indique que le renard n'est plus un animal "nuisible" mais "Susceptible d'être nuisible".

!!!tip article de loi
    L’arrêté du 3 août 2023 s'appuie sur une liste de 9 espèces indigènes qui peuvent être classés « susceptibles d’occasionner des dégâts » à l'échelle des départements, en fonction des populations et de la répartition locale de ces espèces :

Malgré ces changements de loi, le renard est un animal qui n'est pas apprécié de tous. Il est souvent chassé des zones où il pourrait normalement évoluer et réguler la faune. Pour éviter certaines dérives, il est recommandé de surveiller la population de renards dans les zones concernées et donc prédire si un renard pourrait habiter cette zone.

Pour la prédiction des zones possiblement habitables d'un renard, on considère les caractéristiques suivantes :

- la végétation
- la proximité de l'eau
- la densité urbaine
- la disponibilité de proies

Ces caractéristiques sont toutes mesurées sur une échelle de 1 à 10.

Pour évaluer la possibilité qu'un renard puisse habiter une zone prédéfinie, on utilisera **la méthode des k plus proches voisins**.

Un jeu de données est fourni qui est contenu dans le fichier `donnees_habitats.py` dont une partie du contenu est ci-après :

```python
donnees = [
    (7.211102550927978, {'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0, 
    'disponibilite_proies': 4, 'presence_renard': True})
    (8.660254037844387, {'vegetation': 10, 'proximite_eau': 5, 'densite_urbaine': 9, 
    'disponibilite_proies': 10, 'presence_renard': False})
    (5.196152422706632, {'vegetation': 8, 'proximite_eau': 5, 'densite_urbaine': 1, 
    'disponibilite_proies': 6, 'presence_renard': False})
]
```

Le fichier `prediction_habitat.py` contient des fonctions qui seront nécessaires à l'évaluation de ces zones qui devront être complétées, modifiées ou à implémenter.

1. **Compléter le code** de la fonction `distance` qui prend en paramètre deux habitats sous la forme de dictionnaires et renvoie la distance entre ces deux habitats. Pour se faire, **utiliser** la formule de distance euclidienne entre les différents critères de chaque habitat.

La distance euclidienne entre deux points $(x_1, y_1, ..., n_1)$ et $(x_2, y_2, ..., n_2)$ est donnée par la formule :

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}
$$

**Appel 1 : Appeler le professeur pour lui présenter vos réponses et votre fonction ou en cas de difficultés de compréhension de la représentation.**

1. **Écrire le code** de la fonction `distance_d_un_habitat` qui prend en paramètre un habitat sous la forme de dictionnaire et une liste d'habitats sous la forme de liste de dictionnaires. La fonction doit renvoyer une liste de tuples où chaque tuple contient :
    - la distance entre l'habitat fourni et un habitat de la liste donnée;
    - le dictionnaire représentant l'habitat.

**Tester** la fonction `distance_d_un_habitat` avec pour habitat `nouveau` fourni et la liste d'habitats `donnees` en affichant les 3 premiers tuples de la liste.
Les résultats doivent être :  

```python
(7.211102550927978, {'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0, 
'disponibilite_proies': 4, 'presence_renard': True})
(8.660254037844387, {'vegetation': 10, 'proximite_eau': 5, 'densite_urbaine': 9, 
'disponibilite_proies': 10, 'presence_renard': False})
(5.196152422706632, {'vegetation': 8, 'proximite_eau': 5, 'densite_urbaine': 1, 
'disponibilite_proies': 6, 'presence_renard': False})
```

**Appel 2 : Appeler le professeur pour lui présenter vos réponses et votre fonction ou en cas de difficultés de compréhension de la représentation.**

3. La fonction `k_plus_proches` n'est pas correcte et renvoie une erreur.
   **Expliquer** quelle est l'erreur dans cette fonction.
   **Corriger** la fonction pour pouvoir renvoyer les k plus proches voisins de l'habitat à analyser.

**Tester** la fonction `k_plus_proches` avec pour k = 10, l'habitat `nouveau` fourni et la liste d'habitats `donnees` en affichant les 3 premiers tuples de la liste.

**Appel 3 : Appeler le professeur pour lui présenter vos réponses et votre fonction ou en cas de difficultés de compréhension de la représentation.**

4. **Tester** la fonction `presence_renard` avec pour k = 10; k=50; k=100; k=500, l'habitat `nouveau` fourni et la liste d'habitats `donnees`. L'habitat `nouveau` proposé est-il susceptible de contenir une population de renards ? **Expliquer**.

**Appel 4 : Appeler le professeur pour lui présenter vos réponses et votre fonction ou en cas de difficultés de compréhension de la représentation.**  

**Description du dossier**

Le dossier fourni au candidat sur l'ordinateur comporte les éléments suivants :

- Une version PDF de l'énoncé ;
- un code source de départ `prediction_habitat.py` ;
- un jeu de données `donnees_habitats.py` qui contient toutes les zones à exploiter.

**Préparation de l'environnement**

Pour faire fonctionner le code fourni, les bibliothèques suivantes doivent être présentes : `math` et les données du fichier `donnees_habitats.py` doivent être importées.
