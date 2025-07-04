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

# 📚 Les circuits électroniques

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définitions</h3>
        <div class="course-content">
            Les circuits logiques sont des éléments fondamentaux de l'informatique, qui permettent de traiter l'information de manière numérique. Ils sont utilisés dans une multitude d'applications, allant des ordinateurs et des téléphones portables aux dispositifs de contrôle de la circulation et des systèmes de sécurité. Les circuits logiques sont construits à partir de composants électroniques, tels que des transistors, qui sont les briques de base des portes logiques.<br><br>Les transistors sont des dispositifs électroniques qui permettent de contrôler le flux de courant électrique. Ils peuvent être utilisés pour amplifier un signal ou pour activer ou désactiver un circuit. Les portes logiques sont des circuits électroniques qui effectuent des opérations logiques de base, telles que la conjonction, la disjonction, l'inversion, etc. Les portes logiques sont construites à partir de transistors, et peuvent être combinées pour former des circuits logiques plus complexes.<br><br>![transistor](transistor.png)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les portes logiques</h3>
        <div class="course-content">
            Une porte logique est un composant électronique qui effectue une opération logique sur un ou plusieurs signaux d'entrée pour produire un signal de sortie. Les portes logiques sont les briques de base des circuits logiques, et sont utilisées pour construire des circuits plus complexes.<br><br>On peut associer à une porte logique une <strong>table de vérité</strong>. Elle retranscrit les résultats de l'opération suivant chaque combinaison possible des variables d'entrée.<br><br>### Porte NOT<br><br>Cette porte logique produit un signal de sortie qui est l'inverse du signal d'entrée. Si le signal d'entrée est "1", le signal de sortie est "0", et vice versa. L’écriture de l’opération logique est :<br>$S = \overline{A}$.<br><br>#### Table de vérité<br><br>|entrée|sortie|<br>|------|------|<br>|0|1|<br>|1|0|<br><br>#### Représentation<br><br>![rprnot](repr_not.png)<br><br>### Porte AND<br><br>Cette porte logique produit un signal de sortie "1" uniquement si tous les signaux d'entrée sont "1". Sinon, le signal de sortie est "0". L’écriture de l’opération logique est :<br><br>$S = A \vee B$ ou $S = A \times B$<br><br>#### Table de vérité<br><br>|a|b|sortie|<br>|-|-|------|<br>|0|0|0|<br>|0|1|0|<br>|1|0|0|<br>|1|1|1|<br><br>#### Représentation électronique<br><br>![rprand](repr_and.png)<br><br>### Porte OR<br><br>Cette porte logique produit un signal de sortie "1" si l'un des signaux d'entrée est "1" ou si les deux signaux d’entrée sont “1”. Si tous les signaux d'entrée sont "0", le signal de sortie est "0".<br>L’écriture de l’opération logique est :<br><br>$S = A \wedge B$ ou $S = A + B$<br><br>#### Table de vérité<br><br>|a|b|sortie|<br>|-|-|------|<br>|0|0|0|<br>|0|1|1|<br>|1|0|1|<br>|1|1|1|<br><br>#### Représentation électronique<br><br>![rpror](repr_or.png)<br><br>### Porte XOR<br><br>Cette porte logique produit un signal de sortie "1" si un seul des signaux d'entrée est "1". Si tous les signaux d'entrée sont "0" ou "1", le signal de sortie est "0".<br><br>La porte XOR est une porte de combinaison.<br>Elle est équivalente à l'équation logique $S = \overline{A}B + A \overline{B}$.<br>On l'écrit $A \oplus B$.<br><br>#### Table de vérité<br><br>|a|b|sortie|<br>|-|-|------|<br>|0|0|0|<br>|0|1|1|<br>|1|0|1|<br>|1|1|0|<br><br>#### Représentation électronique<br><br>![rprxor](repr_xor.png)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les équations logiques</h3>
        <div class="course-content">
            Une équation logique est une expression algébrique qui représente une fonction logique en utilisant des variables logiques, des opérateurs logiques et des constantes logiques. L'équation logique permet de décrire le comportement d'un circuit logique ou d'une fonction logique de manière formelle.<br>Les équations logiques suivent des règles de priorité d'opérations similaires à PEMDAS.<br>Par exemple, une équation logique simple pourrait être $S = A \vee B \oplus C$.<br>Elle se lit "A et B ou C".
        </div>
    </div>
    
</div>