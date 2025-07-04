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

# 📚 Fonctions en python

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définitions</h3>
        <div class="course-content">
            Une fonction en python correspond à un certain bout de code qui est à réaliser plusieurs fois.<br>Utiliser une fonction permet de réduire le nombre de lignes de code et de le modulariser.<br><br>Par exemple, on peut écrire une fonction qui réalise un certain type d'opération en fonction des éléments qu'on lui fournit pour fonctionner.<br><br>Un paramètre est une variable qui permet le bon fonctionnement d'un algorithme. Ce paramètre répond à un type précisé pour le fonctionnement de la fonction.<br><br>Par exemple, on peut écrire une fonction qui calcule la température en Fahrenheit en donnant comme paramètre la température en Celsius.<br><br>On connait la fonction mathématique pour passer de l'une à l'autre <br>$Temperature_{Fahrenheit} = (Temperature_{Celsius} \times \frac{9}{5}) + 32$.<br><br>On peut l'écrire en python pour pouvoir l'utiliser à plusieurs endroit sans forcément la réécrire à chaque fois.<br>On utilisera le mot-clef <code>def</code>, qui signifie <strong>define</strong> (définir).<br><br>En clair, la structure est :<br><br>``<code>python<br><br>def nom_de_fonction(variable_1 : type, vartiable_2 : type) -> type_renvoi :<br>    '''<br>    Explications de la fonctions, paramètres et renvoi<br>    '''<br>    Corps de la fonction<br>    Renvoi ou non de la fonction<br></code>`<code><br><br></code>`<code>python<br>def celsius_vers_fahrenheit(temp_celsius : int) -> float:<br>    '''<br>    params:<br>        entrée : temp_celsius : entier, température en celsius<br>        sortie : temp_fahrenheit : entier, température en Fahrenheit<br>    Convertit une température exprimée en Celsius en température exprimée en Fahrenheit.<br>    '''<br>    temp_fahrenheit = (temp_celsius * (9/5)) + 32<br>    return temp_fahrenheit<br><br>def afficher_bonjour(prenom : str) -> None :<br>    '''<br>    params:<br>        entrée : prenom : chaine de caractère, un prénom<br>        sortie : X<br>    Affiche dans le terminal : Bonjour, prenom.<br>    '''<br>    print('Bonjour, ' + prenom)<br><br>print(celsius_vers_fahrenheit(19))<br>print(celsius_vers_fahrenheit(25))<br>afficher_bonjour('Eudes')<br>afficher_bonjour('Germaine')<br></code>`<code><br><br>On va décortiquer la fonction précédente pour définir ce qu'est une fonction.<br><br>- Le mot clef def, qui indique que l'on définit une fonction<br>- Une fonction est définie par son nom, ici </code>celsius_vers_fahrenheit<code>.<br>- Des paramètres, ici un unique temp_celsius<br>- Une spécification, un bloc de texte qui indique le type des paramètres d'entrée et sortie et ce que fait la fonction. (Cela répond aux bonnes pratiques de développement).<br>- Un bloc de code, ici une opération<br><br>On peut aussi retrouver un retour, ici la fonction renvoie un résultat pour effectuer des traitements. Pour l'exemple précédent, on souhaite l'afficher dans le terminal.<br><br>!!! Danger<br>    Attention ! Une fonction peut ne pas retourner quelque chose. Si rien n'est précisé, elle renvoie par défaut None.<br>    Cela peut expliquer certains comportements d'affichage ou d'affectation de variables.<br>    Par exemple, réaliser </code>print(afficher_bonjour('Eudes'))` affichera None dans le terminal car elle ne renvoie rien.
        </div>
    </div>
    
</div>