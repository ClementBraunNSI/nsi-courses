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

# 📚 Types de données en Python

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les booléens</h3>
        <div class="course-content">
            Le type booléen en Python est utilisé pour représenter des valeurs de vérité. Il n’a que deux valeurs possibles : True (vrai) et False (faux). Les booléens sont souvent utilisés dans les conditions et les boucles pour contrôler le flux d’exécution d’un programme.<br><br>``<code> python<br>    est_jeune = True<br>    a_termine_cours = False<br></code>`<code><br><br>Les opérateurs logiques tels que and, or, et not permettent de combiner ou d’inverser les valeurs booléennes :<br><br></code>`<code> python<br>    est_jeune_et_a_termine_cours = est_jeune and a_termine_cours <br>    est_vrai = not a_termine_cours  <br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les nombres</h3>
        <div class="course-content">
            ### Les entiers<br><br>Il existe plusieurs types en Python pour définir des nombres.<br>Il existe le type <strong>int</strong> qui permet d'instancier des nombres.<br><br>La syntaxe est assez claire : on veut instancier une variable *a* valant 42.<br><br>``<code>python<br>    a = 42<br>    b = -54<br></code>`<code><br><br>On peut réaliser des opérations sur ce type entier, elles sont répertoriées dans le cours sur les <strong>constructions élémentaires</strong>.<br><br>### Les flottants<br><br>Pour décrire des nombres réels (à virgule), python associe la valeur à un type appelé <strong>flottant</strong> qui correspond à une écriture à virgule flottante (IEEE754).<br><br>!!!danger<br>    Attention, pour rappel, en informatique pour représenter les nombres réels, il y a des arrondis qui sont réalisés.<br>    Ainsi, réaliser des opérations mathématiques sur des flottants <strong>est strictement interdit</strong> car les résultats, même s'ils nous paraissent corrects, ne le seront pas forcément pour la machine.<br><br>Comme pour les entiers, l'instanciation est triviale.<br><br></code>`<code>python<br>pi = 3.14159<br>racine_de_deux = 1.4132<br></code>``<br><br>!!! warning Le point<br>    Pour décrire un réel, on utilise le point et non la virgule comme habituellement à la main.<br>    Cela vient de l'écriture américaine qui utilise les <strong>.</strong> pour les parties entières et décimales et <strong>,</strong> pour les milliers, millions...
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les caractères et chaînes de caractères</h3>
        <div class="course-content">
            En Python, les caractères sont représentés comme des chaînes de longueur 1, et il n’y a pas de type char distinct comme dans certains autres langages. Les chaînes de caractères sont représentées par le type str.<br><br>!!! tip Astuce pour se repérer<br>    Il est conseillé pour mieux s'y retrouver, d'écrire les caractères seuls entre <strong>'</strong> et les chaînes de caractère entre <strong>"</strong><br><br>``<code> python<br>    nom = "Alice"<br>    lettre = 'a'<br></code>`<code><br><br>On peut aussi accéder aux caractères individuels d’une chaîne en utilisant des indices, commencer par 0 :<br><br></code>`<code>python <br>    premiere_lettre = nom[0]  # 'A'<br>    derniere_lettre = nom[-1]  # 'e'<br></code>``<br><br>Les chaînes peuvent être concaténées (<strong>opérateur +</strong>), répétées et comparées, et elles offrent une multitude de méthodes pour effectuer diverses opérations telles que la recherche, le remplacement ou la modification de la casse des caractères.
        </div>
    </div>
    
</div>