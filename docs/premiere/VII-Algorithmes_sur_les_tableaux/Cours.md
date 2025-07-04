<style>
/* Styles pour les cours avec système de cartes */

.course-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 100%;
}

.course-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 4px solid;
    width: 100%;
    max-width: 100%;
    margin: 1rem 0;
}

.course-card.definition {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.02) 100%);
}

.course-card.definition:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.course-card.example {
    border-left-color: #2196F3;
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.02) 100%);
}

.course-card.example:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
}

.course-card.warning {
    border-left-color: #F44336;
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.02) 100%);
}

.course-card.warning:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(244, 67, 54, 0.3);
}

.course-card.tip {
    border-left-color: #FF9800;
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.02) 100%);
}

.course-card.tip:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);
}

.course-card.highlight {
    border-left-color: #9C27B0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.05) 0%, rgba(156, 39, 176, 0.02) 100%);
}

.course-card.highlight:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(156, 39, 176, 0.3);
}

.course-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.course-content {
    margin-bottom: 1rem;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.badge.definition {
    background: rgba(76, 175, 80, 0.15);
    color: #4CAF50;
}

.badge.example {
    background: rgba(33, 150, 243, 0.15);
    color: #2196F3;
}

.badge.warning {
    background: rgba(244, 67, 54, 0.15);
    color: #F44336;
}

.badge.tip {
    background: rgba(255, 152, 0, 0.15);
    color: #FF9800;
}

.badge.highlight {
    background: rgba(156, 39, 176, 0.15);
    color: #9C27B0;
}

.btn {
    background: white;
    color: #4169E1;
    border: 2px solid #4169E1;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    text-decoration: none;
}

.btn:hover {
    background: rgba(65, 105, 225, 0.1);
    border-color: #1E90FF;
    color: #1E90FF;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(65, 105, 225, 0.4);
}

.exercise-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.math-container {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.table tr:hover {
    background: #f8f9fa;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #d63384;
}

pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre code {
    background: none;
    padding: 0;
    color: #495057;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-weight: 600;
}
</style>

# 📚 Optimisation du Tri : Algorithmes de Comparaison

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définitions et Problématiques</h3>
        <div class="course-content">
            ### Qu'est-ce que trier ?<br><br>Trier consiste à organiser un ensemble d'éléments dans un ordre précis (généralement croissant ou décroissant).  <br>C'est une opération fondamentale en informatique, utilisée dans de nombreux domaines :  <br><br>- Classement de données<br>- Préparation de données pour d'autres algorithmes<br>- Optimisation des performances de recherche<br><br>### Stratégies de Tri<br><br>On peut trier des données de plusieurs manières :<br><br>- Par comparaison : on compare les éléments entre eux<br>- Sans comparaison : on utilise des propriétés spécifiques des données
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Tri par Sélection</h3>
        <div class="course-content">
            ### Principe<br><br>Au début de l'algorithme, on cherche la plus petite valeur de la liste et on l'échange avec la valeur située à la première position.  <br>À partir de cette itération, on considère que la liste à trier est composée d'<strong>une partie triée composée d'un élément</strong> et <strong>une partie non triée</strong>.  <br>On va chercher à chaque itération du tri, on va chercher la valeur la plus petite de la zone non triée et on va la placer au début de celle-ci.  <br>Comme les valeurs de la zone non triée sont plus grandes que toutes les valeurs de la zone triée car sinon elles auraient été selectionnées, cette valeur se rajoute à la zone triée et ainsi de suite.  <br><br>### Exemple Illustratif<br><br>Liste initiale : [5, 2, 4, 6, 1, 3]<br><br>| Étapes  |   Liste en cours   | Min sélectionné |<br>|:-------:|:------------------:|:---------------:|<br>|  Début  | [5, 2, 4, 6, 1, 3] |        1        |<br>| Étape 1 | [1, 2, 4, 6, 5, 3] |        2        |<br>| Étape 2 | [1, 2, 3, 6, 5, 4] |        3        |<br>|   ...   |        ...         |       ...       |<br>|  Final  | [1, 2, 3, 4, 5, 6] |        -        |<br><br>### En Python<br><br>On va avoir besoin de <strong>trois fonctions</strong> :<br><br>- une fonction <code>indice_minimum_tranche</code> qui trouve l'indice du minimum dans une portion de la liste triée.<br>- une fonction <code>echange_valeur</code> qui échange la valeur à l'indice du début de la zone non triée avec celle qui est la plus petite.<br>- une fonction <code>tri_selection</code> qui va réaliser le tri et renvoyer la permutation triée de la liste.<br><br>!!! fox_exercice_important "Indice de la valeur minimum dans une tranche"<br>    <strong>Écrire une fonction <code>indice_minimum_tranche</code> qui prend en paramètres une liste, un indice de début et qui renvoie l'indice de la valeur la plus petite dans la tranche donnée.</strong>  <br>    *Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de* <strong>*Out Of Range</strong><strong>.*  <br>    *Exemple:*  <br>    ``<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>> indice_minimum_tranche(liste,1)<br>    4<br>    </code>`<code><br><br>!!! fox_exercice_important "Échange de valeur à l'aide des indices"<br>    </strong>Écrire une fonction </code>echange_valeur<code> qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste<strong>  <br>    *Attention, cette fonction fait une modification par effet de bord et ne renvoie rien.*  <br>    *Exemple:*  <br>    </code>`<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>>echange_valeur(liste, 0, 4)<br>    >>>print(liste)<br>    [0,5,2,4,1,8]<br>    </code>`<code><br><br>!!! fox_exercice_important "Tri par sélection du minimum"<br>    </strong>Écrire une fonction </code>tri_selection_minimum<code> qui prend en paramètre une liste et renvoie sa permutation triée.**  <br>    *Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  <br>    *Exemple:*  <br>    </code>`<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>>print(tri_selection_minimum(liste))<br>    [0,1,2,4,5,8]<br>    </code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Tri par Insertion</h3>
        <div class="course-content">
            On considère que la liste à trier est composée d'<strong>une partie triée composée d'un élément</strong> et <strong>une partie non triée</strong>.  <br>On va chercher à chaque itération <code>i</code> du tri, on va chercher à déplacer la valeur que l'on retrouve à la position <code>i</code> à sa bonne position dans la zone triée.  <br>Comme les valeurs de la zone non triée sont plus grandes que toutes les valeurs de la zone triée car sinon elles auraient été selectionnées, cette valeur se rajoute à la zone triée et ainsi de suite.  <br><br>### Exemple Illustratif<br><br>Liste initiale : [5, 2, 4, 6, 1, 3]<br><br>| Étapes  |   Liste en cours   | Élément inséré |<br>|:-------:|:------------------:|:--------------:|<br>|  Début  | [5, 2, 4, 6, 1, 3] |       -        |<br>| Étape 1 | [2, 5, 4, 6, 1, 3] |       2        |<br>| Étape 2 | [2, 4, 5, 6, 1, 3] |       4        |<br>| Étape 3 | [2, 4, 5, 6, 1, 3] |       6        |<br>| Étape 4 | [1, 2, 4, 5, 6, 3] |       1        |<br>| Étape 5 | [1, 2, 3, 4, 5, 6] |       3        |<br>|  Final  | [1, 2, 3, 4, 5, 6] |       -        |<br><br>### En Python<br><br>On va avoir besoin de <strong>trois fonctions</strong> :<br><br>- une fonction <code>echange_valeur</code> qui échange la valeur à l'indice du début de la zone non triée avec celle qui est la plus petite.<br>- une fonction <code>insertion</code> qui échange les valeurs dans la partie triée petit à petit jusqu'à trouver la bonne position.<br>- une fonction <code>tri_insertion</code> qui va réaliser le tri et renvoyer la permutation triée de la liste.<br><br>!!! fox_exercice_important "Échange de valeur à l'aide des indices"<br>    <strong>Écrire une fonction <code>echange_valeur</code> qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste</strong>  <br>    *Attention, cette fonction fait une modification par effet de bord et ne renvoie rien.*  <br>    *Exemple:*  <br>    ``<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>>echange_valeur(liste, 0, 4)<br>    >>>print(liste)<br>    [0,5,2,4,1,8]<br>    </code>`<code><br><br>!!! fox_exercice_important "Insertion d'une valeur dans une zone triée"<br>    <strong>Écrire une fonction </code>insertion_zone_triee<code> qui prend en paramètre une liste, et un indice correspondant à celui de la valeur qui est juste après la zone triée. Cette fonction échange la valeur à l'indice avec celles qui sont avant elles pour trouver sa bonne place.</strong><br>    *Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de* <strong>*Out Of Range</strong><strong>.*  <br>    *Exemple:*  <br>    </code>`<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>>insertion_zone_triee(liste,2)<br>    >>>print(liste)<br>    [1,2,5,4,0,8]<br>    </code>`<code><br><br>!!! fox_exercice_important "Tri par sélection du minimum"<br>    </strong>Écrire une fonction </code>tri_insertion<code> qui prend en paramètre une liste et renvoie sa permutation triée.**  <br>    *Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.*  <br>    *Exemple:*  <br>    </code>`<code>python<br>    >>>liste = [1,5,2,4,0,8]<br>    >>>print(tri_insertion(liste))<br>    [0,1,2,4,5,8]<br>    </code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Tris Sans Comparaison</h3>
        <div class="course-content">
            ### Tri par Dénombrement<br><br>Le tri par dénombrement est un algorithme de tri qui n'agit pas par comparaisons mais par comptage des éléments de la liste.<br><br>Exemple : Dans la liste L <strong>[3,2,1,2]</strong>, on peut dénombrer les valeurs de cette manière : une occurence de 1, deux occurences de 2 et une occurence de 3.<br><br>*Principe de fonctionnement :*<br>On considère la liste L précédente:<br><br>- On créée une liste d'occurences contenant un nombre de 0 équivalent à la valeur maximale + 1 de la liste à trier et une liste vide qui contiendra, à la fin, les éléments de la liste de départ triés.<br><br>- On parcourt la liste L à trier et à chaque élément, on incrémente la valeur à l'indice du nombre rencontré dans la liste d'occurences.<br><br>| itération | L                | occurences   |<br>| --------- | ---------------- | ------------ |<br>| 0         | [3,2,1,2]        | [0, 0, 0, 0] |<br>| 1         | [<strong>3</strong>, 2, 1, 2] | [0, 0, 0, 1] |<br>| 2         | [3, <strong>2</strong>, 1, 2] | [0, 0, 1, 1] |<br>| 3         | [3, 2, <strong>1</strong>, 2] | [0, 1, 1, 1] |<br>| 4         | [3, 2, 1, <strong>2</strong>] | [0, 1, 2, 1] |<br>  <br>- On peuple la liste vide de $x$ fois le nombre rencontré en balayant la liste d'occurences.<br><br>| itération | occurences       | liste_triee |<br>| --------- | ---------------- | ----------- |<br>| 1         | [<strong>0</strong>, 1, 2, 1] | []          |<br>| 2         | [0, <strong>1</strong>, 2, 1] | [1]         |<br>| 3         | [0, 1, <strong>2</strong>, 1] | [1, 2, 2]   |<br>| 4         | [0, 1, 2, <strong>1</strong>] | [1,2,2,3]   |
        </div>
    </div>
    
</div>