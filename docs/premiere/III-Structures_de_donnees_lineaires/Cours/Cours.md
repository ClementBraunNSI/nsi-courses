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

# 📚 Structures de données linéaires

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définition</h3>
        <div class="course-content">
            Une <strong>structure de données linéaire</strong> est une collection d'<strong>éléments</strong> stockés séquentiellement. En Python, les deux principales implémentations de tableaux (un concept général de structure de données linéaire) sont les <strong>listes</strong> (mutables, c'est-à-dire modifiables après création) et les <strong>tuples</strong> (immuables, c'est-à-dire non modifiables après création).<br><br>Ces structures permettent d’organiser et de stocker divers éléments. Elles sont ordonnées, ce qui signifie que chaque élément a une position spécifiques (indice), et les éléments sont généralement stockés dans des zones mémoires contiguës ou liées.<br><br>Utiliser des tableaux (listes ou tuples) permet de ne pas avoir à créer une variable distincte pour chaque élément à stocker.<br><br>On peut accéder à un élément d'un tableau en utilisant son <strong>indice</strong>. Un indice correspond à la position de l'élément dans le tableau.<br><br>!!! Danger Important<br>	Cas particulier, en <strong>python</strong>, comme dans la plupart des autres langages de programmation, les indices de tableaux commencent à 0.<br><br>Pour initialiser un <strong>tuple</strong> vide (un type de tableau immuable), on l’associe à une variable :<br><br>``<code>python<br># Instance d'un tuple vide<br>>>> mon_tuple_vide = ()<br>>>> print(type(mon_tuple_vide))<br><class 'tuple'><br>>>> print(mon_tuple_vide)<br>()<br></code>`<code><br><br>Pour initialiser une <strong>liste</strong> vide (un type de tableau mutable), on utilise des crochets </code>[]<code> :<br><br></code>`<code>python<br># Instance d'une liste vide<br>>>> ma_liste_vide = []<br>>>> print(type(ma_liste_vide))<br><class 'list'><br>>>> print(ma_liste_vide)<br>[]<br></code>`<code><br><br>Considérons un exemple de tableau d'entiers :<br><br>| indice | élément |<br>| --- | --- |<br>| 0 | 312 |<br>| 1 | 354 |<br>| 2 | 1234 |<br><br>En Python, pour un <strong>tuple</strong>, on l'écrirait avec des parenthèses </code>()<code> :<br><br></code>`<code>python<br>mon_tuple = (312, 354, 1234)<br># print(mon_tuple) # Pourrait afficher (312, 354, 1234)<br></code>`<code><br><br>Pour une <strong>liste</strong>, on l'écrirait avec des crochets </code>[]<code> :<br><br></code>`<code>python<br>ma_liste = [312, 354, 1234]<br># print(ma_liste) # Pourrait afficher [312, 354, 1234]<br></code>`<code><br><br>On peut créer des tableaux possédant diverses valeurs, leur taille étant limitée par l’espace mémoire de la machine :<br><br></code>`<code>python<br>tableau_de_notes = (14,15,20,19)<br>tableau_animaux = ("chien", "chat", "oiseau", "poisson")<br></code>`<code><br><br>!!! Tip<br>	Dans la majorité des cas, il est préférable de <strong>créer des tableaux pour des données de même type</strong>.<br>	Cela permet d’éviter des erreurs pour l’interpréteur et éviter des incompréhensions pour la suite du code.<br><br>!!! Danger Mutabilité : Tuples (immuables) vs Listes (mutables)<br>	Attention à la distinction entre tuples et listes concernant la mutabilité !<br><br>	<strong>Tuples (immuables) :</strong><br>	Un tuple est <strong>immuable</strong>. Cela signifie qu'une fois qu'un tuple est créé, ses éléments ne peuvent pas être modifiés, ajoutés ou supprimés directement. Toute tentative de modifier un élément d'un tuple existant résultera en une erreur </code>TypeError<code>.<br>	Par exemple :<br>	</code>`<code>python<br>	mon_tuple = (10, 20, 30)<br>	# mon_tuple[0] = 5 # Ceci lèverait une TypeError: 'tuple' object does not support item assignment<br>	</code>`<code><br>	Pour "modifier" un tuple, on doit en réalité créer un nouveau tuple.<br><br>	<strong>Listes (mutables) :</strong><br>	Une liste est <strong>mutable</strong>. Cela signifie que l'on peut modifier ses éléments, en ajouter ou en supprimer après sa création.<br>	Par exemple :<br>	</code>`<code>python<br>	ma_liste = [10, 20, 30]<br>	ma_liste[0] = 5  # Modifie l'élément à l'indice 0<br>	ma_liste.append(40) # Ajoute un élément à la fin<br>	# print(ma_liste) # Afficherait [5, 20, 30, 40]<br>	</code>`<code><br>	L'erreur </code>TypeError` mentionnée dans le contexte original ("les valeurs d'un tuple ne supportent pas l'assignation de valeurs") s'applique spécifiquement aux tuples.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Taille d’un tableau</h3>
        <div class="course-content">
            Les tableaux possèdent des fonctions qui leurs sont propres.<br><br>Ces fonctions s’appellent des méthodes.<br><br>La méthode <code>len</code> permet d’obtenir la longueur d’un tableau, ie sa taille. Cela fonctionne de la même manière que lorsque l’on souhaite obtenir la longueur d’une chaîne de caractère.<br><br>``<code>python<br>tableau_animaux = ("chien", "chat", "oiseau", "poisson")<br>>>>print(len(tableaux_animaux))<br>4<br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Accéder à un élément d’un tableau</h3>
        <div class="course-content">
            ### Notion d’indice<br><br>Pour accéder à un élément du tableau, on peut s’intéresser à sa position dans le tableau, c’est à dire son <strong>indice</strong>.<br><strong>Rappel important : L’indice commence à 0 !</strong><br><br>On peut accéder à un élément d'un tableau (liste ou tuple) en utilisant son indice avec la syntaxe <code>nom_du_tableau[indice]</code>:<br><br>``<code>python<br># Exemple avec un tuple<br>mon_tuple_animaux = ("chien", "chat", "poisson", "vache")<br># On veut l'élément à la position 3 du tuple (le quatrième élément)<br># >>> print(mon_tuple_animaux[3]) # Afficherait 'vache'<br><br># Exemple avec une liste<br>ma_liste_animaux = ["chien", "chat", "poisson", "vache"]<br># >>> print(ma_liste_animaux[1]) # Afficherait 'chat'<br></code>`<code><br><br>On peut vouloir accéder à tous les éléments d’un tableau (liste ou tuple), ou à une partie de celui-ci.<br>Pour ce faire, on peut utiliser les boucles <strong></code>while<code> (tant que) et </code>for<code> (pour)</strong> afin de parcourir les éléments.<br><br></code>`<code>python<br>tableau = ("chien", "chat", "poisson", "vache")<br><br>#pour i allant de 0 à la taille du tableau:<br>for i in range(len(tableau)):<br>	print(tableau[i])<br><br># tant que i est plus petit que la taille du tableau<br>i=0<br>while i < len(tableau):<br>	print(tableau[i])<br>	i = i + 1<br></code>`<code><br><br>De cette même manière, on fait varier i pour qu’il prenne tous les indices du tableau et on arrive à accéder à tous les éléments du tableau.<br><br>### Notion de *in*<br><br>Python permet d’utiliser bon nombres de mots-clefs. Le mot-clef <strong>*in</strong>* en fait partie.<br><br>Celui ci permet de savoir si un élément fait partie d’une autre variable. On peut l’utiliser notamment pour savoir si un caractère ou un mot fait partie d’une chaîne de caractère.<br><br>En reprenant l’exemple précédent, on veut une autre méthode de parcours de tableau:<br><br></code>`<code>python<br>tableau = ("chien", "chat", "poisson", "vache")<br>chaine = ""<br><br>#pour i allant de 0 à la taille du tableau:<br>for element in tableau:<br>	print(element)<br></code>`<code><br><br>De ce fait, on accède aussi à tous les éléments du tableau.<br><br>On peut aussi fusionner des tableaux. On peut utiliser l'opérateur </code>+<code> qui sert à <strong>concaténer</strong> des tableaux.<br><br>En clair :<br></code>`<code>python<br>	tableau_1 = (1,2,3)<br>	tableau_2 = (4,5,6)<br>	tableau_3 = tableau_1 + tableau_2<br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les listes</h3>
        <div class="course-content">
            Les listes sont des tableaux mutables. Cela veut dire que l'on peut rajouter des éléments, en retirer ou même modifier le contenu de ce tableau.<br><br>### Ajout d’élément dans une liste<br><br>On peut rajouter des éléments dans une liste créée de diverses manières.<br><br>Exemple : *On veut créer une liste qui correspond à la table de multiplication de 2*<br><br>``<code>python<br>#Initialisation d'une liste vide<br>multiples_de_2 = []<br><br>#Boucle for pour remplir notre liste<br>for i in range(0,11):<br><br>	#On ajoute la valeur i dans le tableau.<br>	multiples_de_2 = multiples_de_2 + [i*2]<br></code>`<code><br><br>En procédant de cette manière, on créée implicitement un tableau d’une valeur contenant ici notre nombre *i multiplié par 2*.<br><br>Le procédé utilisé ici est la <strong>construction par concaténation</strong>. Cette méthode par concaténation a un inconvénient implicite : elle créée une nouvelle liste à la place de modifier la liste en place.<br><br>L’avantage d’utiliser des listes en python pour créer des tableaux provient de l’essence de la liste : <strong>utiliser les méthodes</strong> de listes.<br><br>Au lieu de créer des “sous-listes” de taille 1, on peut utiliser la méthode *append* qui permet d’ajouter une variable à la fin du tableau.<br><br></code>`<code>python<br>#Initialisation d'une liste vide<br>multiples_de_2 = []<br><br>#Boucle for pour remplir notre liste<br>for i in range(0,11): # i prendra les valeurs de 0 à 10<br><br>	#On ajoute la valeur i*2 à la fin de la liste.<br>	#La méthode append() modifie la liste en place et retourne None.<br>	multiples_de_2.append(i*2)<br><br># print(multiples_de_2) # Pourrait afficher [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]<br></code>``<br><br>La méthode *append* a l’avantage sur la méthode par concaténation <strong>de modifier en place la liste au lieu d’en créer une autre.</strong>
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Retirer des éléments d’une liste</h3>
        <div class="course-content">
            Pour retirer des éléments d’une liste, on peut utiliser les méthodes des listes / tableaux.<br><br>### La méthode pop<br><br>La méthode pop est utilisable dans 2 cas:<br><br>$$<br>\begin{equation*}<br>  {element~retiré}=<br>     \begin{cases}<br>        tableau[i] & \text{si } tableau.pop(i) \\<br>        tableau[len(tableau)] & \text{si } tableau.pop(~)<br>     \end{cases}<br>\end{equation*}<br>$$<br><br>``<code>python<br>tableau = [1,2,3,4]<br>>>> print(tableau.pop(1))<br>2<br>>>> print(tableau.pop())<br>4<br></code>`<code><br><br>### La méthode remove<br><br>La méthode remove permet de retirer la première occurence d’un élément passé en paramètre.<br><br>On a donc :<br><br></code>`<code>python<br>>>> tableau = [1,2,2,3,4,4]<br>>>> tableau.remove(2)<br>>>> print(tableau)<br>[1,2,3,4,4]<br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Pour aller plus loin</h3>
        <div class="course-content">
            ### Construction de liste par compréhension<br><br>On peut simplifier le code utilisé précédemment en une seule ligne. Cela a pour but de rendre le code plus concis, de réduire le nombre de lignes et de se rapprocher de notions et écritures plus mathématiques.<br><br>``<code>python<br><br># Comment instancier à l'aide de la méthode par compréhension:<br># nom_variable = [expression for element in iterable]<br># ou avec une condition:<br># nom_variable = [expression for element in iterable if condition]<br><br># Exemple: On initialise la liste directement avec les multiples de 3 de 0*3 à 10*3<br>multiples_de_3 = [i * 3 for i in range(0, 11)] # i prend les valeurs de 0 à 10<br># print(multiples_de_3) # Afficherait [0, 3, 6, ..., 30]<br></code>``<br><br>L’écriture ici peut être scindée en plusieurs blocs :<br><br>- multiple_de_3 : nom de la variable<br>- = assignation de la valeur à la variable<br>- i : valeur qui sera renseignée dans le tableau ou la liste<br>- for i in range(0,11) : on fait varier i entre 0 et 11 non compris<br><br>Cette notation peut être difficile à lire aux premiers abords mais il est utile de la maîtriser pour rendre son code plus aéré.
        </div>
    </div>
    
</div>