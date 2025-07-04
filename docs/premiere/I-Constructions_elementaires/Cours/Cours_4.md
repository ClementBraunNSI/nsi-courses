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

# 📚 Pratiques de développement

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Objectif de cette leçon</h3>
        <div class="course-content">
            Cette leçon vous servira dans toute votre expérience de développement.<br>Le but d'appliquer les bonnes pratiques permet d'avoir un code lisible, compréhensible par d'autres personnes et surtout de comprendre ses propres programmes.<br><br>Il existe diverses techniques pour rendre son code lisible et compréhensible et elles sont listées dans ce cours.<br>Ces bonnes pratiques <strong>seront à appliquer toute l'année</strong> lors des exercices, des évaluations et surtout lors des épreuves pratiques.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Noms de variables</h3>
        <div class="course-content">
            Le nommage des variable est très important lors de la création d'un programme.<br>Nommer une variable correctement permet de se rappeler lors de la conception d'un algorithme, à quoi elle correspond.<br>Il semble logique lors de la conception d'un algorithme portant sur des conversions de température de nommer ses variables de manière logique.<br><br>``<code>python<br># Mauvaise pratique<br>x = 34<br>y = 'La température est de ' + str(x)<br><br># Bonne pratique<br>temperature = 34<br>affichage = 'La température est de ' + str(temperature)<br></code>`<code><br><br>Il existe plusieurs conventions de nommage mais il est plus simple d'utiliser la convention <strong>snake case</strong>.<br>Cette convention consiste à écrire des noms de variables explicites avec des _ (underscore ou tiret-du-bas) pour séparer les divers mots du nom.<br><br>Par exemple :<br><br></code>`<code>python<br>affichage_temperature = 'La température est de '<br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Spécification des fonctions</h3>
        <div class="course-content">
            La spécification d'une fonction correspond à écrire un bloc de texte avant le bloc de code d'une fonction. Ce bloc de texte explique ce que sont les paramètres d'entrée, le résultat en sortie s'il y a et explique brièvement ce que la fonction fait.<br><br>Cela permet de mettre au propre ce que fait et d'avoir une idée de comment concevoir le programme.<br>La spécification permet aussi de rendre compréhensible le programme pour un tiers.<br>La spécification est vivement recommandée (pour ne pas dire évaluée) lors des épreuves pratiques.<br><br>Par exemple :<br><br>``<code>python<br>def nombre_impair(nombre):<br>    '''<br>    params : <br>        entrée : nombre, entier<br>        sortie : un booléen<br>    Renvoie True si le nombre est impair, False sinon.<br>    '''<br>    if nombre %2 == 0:<br>        return False<br>    else:<br>        return True<br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Comprendre les erreurs</h3>
        <div class="course-content">
            Les erreurs sont des événements courants qui surviennent lors de l'exécution d'un programme. Elles peuvent être causées par différents types de problèmes, tels que des erreurs de syntaxe, des erreurs d'exécution ou des erreurs logiques. Chaque type d'erreur correspond à une situation particulière qui peut être identifiée et résolue avec des techniques appropriées.<br><br>### 1. Erreurs de Syntaxe<br><br>Les erreurs de syntaxe surviennent lorsque le code ne respecte pas les règles de la syntaxe du langage Python. Ces erreurs sont détectées lors de la phase d'analyse (ou de parsing) du code avant son exécution. Elles empêchent généralement l'interpréteur Python de comprendre et d'exécuter le programme correctement.<br><br><strong>Exemples :</strong><br><br>- Oubli de deux-points ( : ), par exemple dans une déclaration de fonction ou dans une boucle.<br>- Utilisation incorrecte des guillemets (", ') autour des chaînes de caractères.<br>- Indentation incorrecte, notamment dans les blocs de code tels que les boucles et les fonctions.<br><br>### 2. Erreurs d'Exécution (Exceptions)<br><br>Les erreurs d'exécution, également appelées exceptions, surviennent lorsqu'une instruction ou une expression est correctement écrite mais ne peut pas être exécutée correctement à cause d'une situation imprévue pendant l'exécution du programme. Python génère alors une exception et interrompt l'exécution du programme si celle-ci n'est pas gérée.<br><br><strong>Exemples courants d'exceptions :</strong><br><br>- <code>ZeroDivisionError</code> : Tentative de division par zéro.<br>- <code>TypeError</code> : Opération appliquée à un type d'objet inapproprié.<br>- <code>IndexError</code> : Tentative d'accès à un index inexistant dans une liste ou un tuple.<br><br>### 3. Erreurs Logiques (Bugs)<br><br>Les erreurs logiques, souvent appelées bugs, sont des erreurs plus subtiles où le programme s'exécute sans générer d'exception mais produit un résultat incorrect. Ces erreurs sont souvent dues à une mauvaise compréhension du problème ou à une mauvaise implémentation de l'algorithme.<br><br><strong>Exemples :</strong><br><br>- Mauvaise gestion des conditions dans une boucle.<br>- Utilisation incorrecte des variables dans une fonction.<br>- Algorithmes incorrects qui produisent des résultats imprévus.<br><br>### 4. L'effet de bord<br><br>Un effet de bord est la modification d'une variable qui n'est pas uniquement réservée dans une fonction.<br>Ce type d'erreur peut causer des comportements inattendus (suppresion ou mise à None d'un élément qui sera réutilisé par la suite).
        </div>
    </div>
    
</div>