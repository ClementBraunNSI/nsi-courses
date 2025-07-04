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

# 📚 Constructions élémentaires en Python

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Qu'est ce qu'un programme ?</h3>
        <div class="course-content">
            <strong>Défintion:</strong> On définit un <strong>programme</strong> comme étant une suite d'instruction élémentaires destinées à être exécutées par un ordinateur.<br><br>Le langage python est un langage dit de haut niveau. Cela veut dire qu'il est plus proche de nous (utilisateurs) que de l'ordinateur (du processeur).<br><br>Ce langage est basé sur nos ordinateurs qui réalisent des instructions de manière séquentielle (c'est à dire réalisées les unes après les autres).<br><br>On peut dénombrer un certain nombre d'instructions élémentaires qui permettent de créer un programme.<br>Ces instructions élémentaires peuvent utiliser des opérateurs.<br><br><strong>Définition:</strong> Un opérateur est un caractère ou un ensemble de caractère qui correspond à une opération pouvant être réalisée par le processeur.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Instanciation</h3>
        <div class="course-content">
            L'instanciation est une instruction qui permet d'associer une <strong>valeur</strong> à une <strong>variable</strong>.<br>Une variable en python est une chaîne de caractère que l'on associe à une <strong>type</strong> (domaine de valeurs).<br><br>L'instanciation utilise l'opérateur <code>=</code>.<br>Pour la machine, cela revient à associer un espace mémoire à la valeur désignée.<br><br>Par exemple :<br><br>``<code>python<br># Instancier a à la valeur 42<br>a = 42<br><br>#Instancier ma_chaine_de_caractere à la valeur 'Hello World!'<br>ma_chaine_de_caractere = 'Hello World!'<br></code>``<br><br>On a donc ici, l'explicitation des types entiers ou chaînes de caractères mais il en existe un certain nombre : tableaux, listes, nombres réels (réels à virgule flottante) ou d'autres objets que l'on peut créer nous même.<br><br>Cette opération est la base de la programmation. On utilisera le terme <strong>instancier</strong> pour définir le fait d'associer à une variable une valeur donnée.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Opérations mathématiques</h3>
        <div class="course-content">
            Le langage python est un langage informatique. En informatique, il est nécessaire de réaliser des opérations qui peuvent être du domaine mathématique.<br><br>Il existe un certain nombre d'opérations mathématiques qui sont associées à des opérateurs.<br>On peut citer :<br><br>- $+$: addition<br>- $-$: soustraction<br>- $\ast$: multiplication<br>- $/$ : division<br><br>Ces opérateurs utilisent 2 valeurs, à l'instar de nos opérations que l'on peut écrire sur papier.<br>Il en parait nécessaire d'instancier une variable à une opération, comme par exemple nos fonctions mathématiques $y = 3x+2$.<br><br>Par exemple:<br><br>``<code>python<br>a = 3 + 2 <br>b = 5 - 3<br>c = a * b<br>d = b / a<br></code>``<br><br>Les exemples précédents montrent que l'on peut réaliser des opérations sur les différentes variables que l'on a déjà créée.<br><br>Il faut cependant prendre compte d'une chose importante : <strong>le type des variables utilisées</strong>.<br>En effet, les opérations <strong>mathématiques</strong> sont réservées à des variables de type entiers ou nombres réels. Il faut cependant faire attention aux nombres réels (flottants) à cause des imprécisions (cf cours précédent).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Opérations de comparaisons</h3>
        <div class="course-content">
            Comme les opérations mathématiques, il est possible de réaliser des comparaisons sur des variables.<br><br>!!! danger<br>    <strong>On ne peut comparer des éléments uniquement s'ils sont du même type</strong> !  <br>    Si jamais lors d'un programme on compare deux éléments de types différents, on pourrait faire face à ce que l'on appelle une erreur (<strong>TypeError</strong>).<br><br>Il existe un certain nombre d'opérateurs en python qui permettent de réaliser des comparaisons.  <br><br>On peut citer :<br><br>- $a > b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand que b).<br>- $a < b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit que b).<br>- $a >= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand ou égal à b).<br>- $a <= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit ou égal à b).<br>- $a == b$ : Cet opérateur correspond à une comparaison : a est égal à b.<br><br>!!! Danger<br>    Il ne faut pas confondre les opérateurs $=$ et $==$.  <br>    En effet, $=$ ne sera utilisé uniquement lors d'<strong>instanciation</strong> de variables. Utiliser l'opérateur $=$ lors d'une <strong>comparaison</strong> peut mener à des erreurs! (<strong>SyntaxError</strong>).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Affichage et Demande à l'utilisateur</h3>
        <div class="course-content">
            La fonction <code>print()</code> est utilisée pour afficher des informations à l’écran.  <br>Elle peut afficher des chaînes de caractères, des nombres, ou même les résultats de calculs.  <br>On peut également concaténer plusieurs éléments à afficher en les séparant par des virgules dans l’appel à print().  <br>Par exemple, print("Bonjour", "le monde", 42) affichera “Bonjour le monde 42” dans la console.<br><br>D’un autre côté, la fonction input() permet de capturer des données saisies par l’utilisateur.  <br>Elle prend en argument une chaîne de caractères qui est affichée comme un message à l’utilisateur pour l’inviter à entrer une valeur.  <br>La valeur saisie par l’utilisateur est ensuite renvoyée sous forme de chaîne de caractères.  <br>Par exemple, nom = input("Quel est votre nom ? ") demandera à l’utilisateur de saisir son nom, qui sera ensuite stocké dans la variable nom.  <br><br>!!! Warning<br>    Attention ! La fonction input permet de stocker l'entrée de l'utilisateur dans une variable mais celle-ci sera forcément du type <code>string</code>.<br>    Si l'on souhaite traiter des nombres, il faudra alors modifier le type de la valeur à l'aide des fonctions le permettant.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Conditions</h3>
        <div class="course-content">
            Une condition est réalisable en python grâce à l'instruction <code>if</code>.<br><br>Cette condition permet d'évaluer des comparaisons, des états de variables ou des valeurs associées à des variables.<br>Si cette condition est validée, alors le bout de code associé est exécuté, sinon il peut exister un bloc de code associé au mot-clef <code>else</code>.<br><br>Par exemple, on souhaite réaliser un affichage suivant une valeur d'une variable âge qui correspond à l'âge de l'utilisateur qu'il renseigne.<br><br>``<code>python<br><br># Demander à l'utilisateur son age<br>age = input('Quel est votre âge?')<br><br># Lors d'une demande à l'aide d'input, on reçoit une chaîne de caractères, on doit la convertir en entier<br>age_entier = int(age)<br><br># Condition d'affichage<br>if age_entier > 18 :<br>    print('Vous êtes majeur')<br>else:<br>    print('Vous êtes mineur')<br></code>`<code><br><br>Ce bout de code permet d'afficher si l'utilisateur est majeur ou mineur.<br><br>On remarque la présence du bloc else.<br>Cependant, il existe un autre bloc permettant de réaliser des conditions si une condition n'est pas déjà validée. Ce bloc est le </code>elif<code>.<br><br>Par exemple, on va réaliser un programme qui permet de mettre une appréciation à une note.<br><br></code>`<code>python<br># On demande à l'utilisateur une note (A,B,C)<br>note = input('Quelle est la note à évaluer?')<br><br>if note == 'A' :<br>    print('Très bien')<br>elif note == 'B':<br>    print('Un peu plus pour exceller')<br>else:<br>    print("Poursuis tes efforts")<br></code>`<code><br><br>!!! Danger<br>    On remaraque que l'on a un bloc elif. Celui-ci est exécuté si la première condition n'est pas validée et ainsi de suite. On peut enchaîner autant de bloc </code>elif<code> que nécessaire.<br><br>    Cependant il faut faire attention au nombre de conditions réalisées car trop détailler peut ralentir la vitesse à laquelle on attend une réponse.<br>    Chaque condition est évaluée jusqu'à trouver une qui est valide, ou rentrer dans le </code>else<code>.<br><br>!!! Tip<br>    Le bloc </code>else<code> n'est pas obligatoire s'il ne doit rien faire. On peut l'omettre<br>    </code>`<code>python<br>    age = 36<br>    if age < 40:<br>        print("Vous êtes né après 1980")<br>    else:<br>        print('')<br>    </code>`<code><br>    Ici, print('') ne sert pas à grand chose, on peut l'omettre.<br>    </code>`<code>python<br>    age = 36<br>    if age < 40 :<br>        print('Vous êtes né après 1980')<br>    </code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Boucles</h3>
        <div class="course-content">
            Une boucle en python est la répétition d'une certaine partie d'un algorithme un certain nombre de fois ou suivant la validation d'une condition.<br><br>Il existe plusieurs types de boucles en python.<br><br>### La boucle while<br><br>La boucle <code>while</code> correspond à une boucle qui s'exécute <code>tant que</code> la condition choisie est valide.<br><br>Par exemple, on peut réaliser un bout de code tant qu'un nombre est positif, tant qu'un tableau n'est pas vide, tant qu'une chaîne de caractère n'est pas vide ou bien par exemple tant qu'une condition booléenne est valide.<br><br>On peut associer la syntaxe python suivante:<br><br>``<code>python<br>n = 30<br>i = 1<br># On veut afficher les nombres de 1 à n choisi en faisant croître un entier i.<br>while i <= n:<br>    print(i)<br>    i = i + 1<br></code>`<code><br><br>Ici, ce bout de code incrémente 1 jusqu'à ce qu'il soit supérieur à n. Cela veut dire que la boucle va se dérouler tant que i est inférieur ou égal à n.<br><br>!!! Danger<br>    Une boucle </code>while<code> peut ne pas s'arrêter !<br>    Il faut vérifier que la condition est valide jusqu'au point désiré. On parle de <strong>terminaison de boucle</strong>.<br>    Par exemple, on peut réaliser une boucle infinie en écrivant </code>while True<code> ou bien en ayant une condition qui traite un entier positif et ne jamais le décrémenter.<br><br>### La boucle for<br><br>Il existe un autre type de boucle en python : la boucle </code>for<code>.<br><br>Une boucle for est une boucle que l'on nomme </code>boucle pour<code>. Cette boucle s'exécute à l'aide d'une variable qui va évoluer par rapport à un objet itérable ou une valeur.<br>Par exemple cette boucle est utilisée peut être utilisée pour chaque valeur d'un tableau, pour une valeur jusqu'une borne etc...<br><br>Par exemple :<br><br></code>`<code>python<br>n = 30<br>for i in range(1,n+1):<br>    print(i)<br></code>`<code><br><br>Cette boucle permet d'afficher les entiers de 1 à n.<br>Elle va itérer jusqu'à ce que n soit égal à n et s'arrêter à n+1 avec l'utilisation de la fonction </code>range<code>.<br><br>!!! Tip<br>    La boucle </code>for<code> a un net avantage : Elle s'arrête forcément.<br>    En effet, la boucle </code>for` itère sur un objet itérable ou sur une variable donc sur un certain nombre d'itération donné.
        </div>
    </div>
    
</div>