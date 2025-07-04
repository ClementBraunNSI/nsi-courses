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

# 📚 Jeux d'instruction

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définitions</h3>
        <div class="course-content">
            Un jeu d'instruction correspond à l'ensemble des opérations réalisables et câblées pour un processeur donné.<br><br>Les processeurs, par leur composition ne comprennent que le binaire mais le système d'exploitation permet de traduire les langages de programmation en opérations compréhensibles par le processeur.<br>On appelle <strong>mnémonique</strong> une instruction compréhensible par le processeur.<br><br>Suivant le processeur, il existe divers <strong>mnémoniques</strong>, cependant il existe un langage de programmation proche du processeur et compréhensible par l'être humain : <strong>l'assembleur</strong>.<br><br>Il existe diverses opérations, comme en python, que l'on peut distinguer :<br><br><strong>Opérations liées aux valeurs et aux registres</strong><br><br>- <strong>STR X, Val</strong> : Stocke la valeur Val dans le registre X.<br><br>- <strong>MOV A B</strong> : Déplace les valeurs d'un registre <strong>A</strong> à un autre <strong>B</strong>.<br><br><strong>Opérations mathématiques</strong><br><br>- <strong>ADD X Y</strong> : Ajouter deux valeurs.<br>- <strong>SUB X Y</strong> : Soustraire un opérande d'un autre.<br>- <strong>MUL X Y</strong> : Multiplier deux valeurs.<br>- <strong>DIV X Y</strong> : Diviser un opérande par un autre.<br><br><strong>Opérations booléennes</strong><br><br>- <strong>AND</strong> : Effectuer une opération logique AND entre deux valeurs.<br>- <strong>OR</strong> : Effectuer une opération logique OR entre deux valeurs.<br>- <strong>XOR</strong> : Effectuer une opération logique XOR entre deux valeurs.<br><br><strong>Boucles et conditions</strong><br><br>Pour les boucles, on saute à une certaine étape indiquée dans le code du programme après une comparaison.<br>Pour les conditions, l'endroit du saut correspond au résultat que l'on souhaite.<br>On déclare ce que l'on appelle des <strong>ancres</strong> et si la comparaison donne un résultat, on saute à un endroit, sinon à un autre.<br><br>- <strong>CMP A B</strong> : Comparer deux valeurs.<br>- <strong>JE</strong> : Sauter à une autre instruction si les valeurs sont égaux (Jump if Equal).<br>- <strong>JNE</strong> : Sauter à une autre instruction si les valeurs ne sont pas égaux (Jump if Not Equal).<br>- <strong>JG</strong> : Sauter à une autre instruction si un opérande est supérieur à l'autre (Jump if Greater).<br>- <strong>JL</strong> : Sauter à une autre instruction si un opérande est inférieur à l'autre (Jump if Less).<br><br>L'assembleur n'est pas au programme, mais il permet de mieux comprendre le fonctionnement d'un ordinateur et le fait qu'il soit un modèle de machine séquentiel.<br><br>*Exemple:*<br><br>``<code>python<br>    STR A, 15 # Stocke 15 dans A<br>    ADD A, 10 # Ajoute 10 à la valeur dans A<br>    STR B, 10 # Stocke 10 dans B<br>    LOAD A # Met A dans la mémoire active<br>    MUL 10 # Multiplie la valeur dans la mémoire active par 10<br>    STR A # Stocke le résultat de la mémoire active dans A <br>    CMP A, B<br>    boucle:<br>    JE fin_boucle<br>    STR C, 0<br>    ADD B, 1<br>    ADD C,1<br>    JMP boucle<br>    fin_boucle<br></code>``
        </div>
    </div>
    
</div>