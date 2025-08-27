<style>
/* Styles modernes pour le cours Booléens */
.course-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.definition-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.function-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin: 2rem 0;
    padding: 0 1rem;
    align-items: start;
}

.function-grid .function-card:first-child {
    grid-column: 2 / 3;
    margin-bottom: 1rem;
}

.function-grid .function-card:nth-child(2) {
    grid-column: 1 / 2;
    grid-row: 2;
}

.function-grid .function-card:nth-child(3) {
    grid-column: 2 / 3;
    grid-row: 2;
}

.function-grid .function-card:nth-child(4) {
    grid-column: 3 / 4;
    grid-row: 2;
}

.function-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), 
                                      rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    min-height: 400px;
}

.function-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(199, 135, 58, 0.2);
}

.function-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, 
                               rgba(255, 255, 255, 0.1), 
                               transparent);
    transform: rotate(45deg);
    transition: all 0.6s;
    opacity: 0;
}

.function-card:hover::before {
    animation: shine 0.6s ease-in-out;
    opacity: 1;
}

.function-icon {
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 1rem;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
    flex-shrink: 0;
}

.function-name {
    font-size: 1.3rem;
    font-weight: 700;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    flex-shrink: 0;
}

.function-description {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    text-align: justify;
    flex-grow: 1;
}

.truth-table {
    background: #ffffff;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    overflow: hidden;
    margin-top: auto;
    flex-shrink: 0;
}

.truth-table table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Roboto Mono', monospace;
    font-size: 0.9rem;
    color: #484242;
    table-layout: fixed;
}

.truth-table th {
    background: #f5f5f5;
    color: #333;
    font-weight: 600;
    padding: 10px 8px;
    text-align: center;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    border-bottom: 1px solid #e0e0e0;
    width: 33.33%;
}

.truth-table td {
    padding: 8px;
    text-align: center;
    background: #ffffff;
    font-weight: 500;
    width: 33.33%;
    border-bottom: 1px solid #f0f0f0;
}

.truth-table tr:nth-child(even) td {
    background: #fafafa;
}

.truth-table th:first-child {
    border-top-left-radius: 8px;
}

.truth-table th:last-child {
    border-top-right-radius: 8px;
}

.truth-table tr:last-child td {
    border-bottom: none;
}

.truth-table tr:last-child td:first-child {
    border-bottom-left-radius: 8px;
}

.truth-table tr:last-child td:last-child {
    border-bottom-right-radius: 8px;
}

/* Styles spécifiques pour la table NOT (2 colonnes) */
.function-card:first-child .truth-table th,
.function-card:first-child .truth-table td {
    width: 50%;
}



.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #4299e1;
}

.code-title {
    color: #4299e1;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.operator-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.operator-card {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 193, 7, 0.2);
    text-align: center;
}

.operator-symbol {
    font-size: 1.5rem;
    font-weight: bold;
    color: #f39c12;
    margin-bottom: 0.5rem;
    font-family: 'Courier New', monospace;
}

.operator-name {
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.operator-python {
    color: #7f8c8d;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
}

@keyframes shine {
    0% {
        transform: translateX(-100%) rotate(45deg);
    }
    100% {
        transform: translateX(100%) rotate(45deg);
    }
}

@media (max-width: 1200px) {
    .function-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }
    
    .function-grid .function-card:first-child {
        grid-column: 1 / 3;
        margin-bottom: 1rem;
    }
    
    .function-grid .function-card:nth-child(2) {
        grid-column: 1 / 2;
        grid-row: 2;
    }
    
    .function-grid .function-card:nth-child(3) {
        grid-column: 2 / 3;
        grid-row: 2;
    }
    
    .function-grid .function-card:nth-child(4) {
        grid-column: 1 / 3;
        grid-row: 3;
    }
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .function-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .function-card {
        min-height: auto;
        padding: 1rem;
    }
    
    .operator-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
    
    .truth-table th,
    .truth-table td {
        padding: 8px 4px;
        font-size: 0.8rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🔢 Booléens et Fonctions booléennes</h1>
    <p class="course-subtitle">L'algèbre de George Boole et la logique binaire</p>
</div>

<div class="definition-box">
    <div class="definition-title">🎯 Définitions Fondamentales</div>
    <div class="definition-content">
        <p><strong>Variable booléenne :</strong> Une variable qui peut prendre <strong>deux états</strong> : <strong>Vrai ou Faux</strong>. Ces états peuvent être équivalents à des valeurs numériques : Vrai = 1 et Faux = 0.</p>
        <p><strong>Fonction booléenne :</strong> Une fonction qui prend en paramètre <strong>des variables booléennes</strong> et en ressort un résultat.</p>
        <p><strong>Équation booléenne :</strong> Un ensemble de fonctions booléenne prenant en paramètre un certain nombre de variables et renvoie un résultat en sortie.</p>
    </div>
</div>

<div class="highlight-fact">
    ⚡ <strong>En machine :</strong> Ces états correspondent <strong>à la présence du courant ou non</strong>.
</div>

<h2 class="section-title">🔧 Fonctions booléennes</h2>

<div class="definition-box">
    <div class="definition-title">📚 Concept des Tables de Vérité</div>
    <div class="definition-content">
        Il existe un certain nombre d'opérations booléennes. Ces fonctions donnent un résultat fini dépendant de l'état des variables en paramètre. On appelle cet ensemble de couples états/résultat <strong>une table de vérité</strong>.
    </div>
</div>

<div class="function-grid">
    <div class="function-card">
        <div class="function-icon">🚫</div>
        <div class="function-name">Fonction NOT (NON)</div>
        <div class="function-description">
            La fonction NOT prend en paramètre une variable booléenne et renvoie son opposé.
        </div>
        <div class="truth-table">
            <table>
                <thead>
                    <tr>
                        <th>a</th>
                        <th>s</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>0</td>
                        <td>1</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>0</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="function-card">
        <div class="function-icon">🤝</div>
        <div class="function-name">Fonction AND (ET)</div>
        <div class="function-description">
            La fonction AND prend en paramètre deux variables booléennes et renvoie en sortie si les deux variables sont à l'état 1. L'opérateur est $\times$ ou $\cdot$.
        </div>
        <div class="truth-table">
            <table>
                <thead>
                    <tr>
                        <th>a</th>
                        <th>b</th>
                        <th>s</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>0</td>
                        <td>1</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="function-card">
        <div class="function-icon">🔀</div>
        <div class="function-name">Fonction OR (OU)</div>
        <div class="function-description">
            La fonction OR prend en paramètre deux variables et renvoie 1 si l'une ou les deux variables booléennes sont à l'état 1. L'opérateur est $+$.
        </div>
        <div class="truth-table">
            <table>
                <thead>
                    <tr>
                        <th>a</th>
                        <th>b</th>
                        <th>s</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>0</td>
                        <td>1</td>
                        <td>1</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>0</td>
                        <td>1</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="function-card">
        <div class="function-icon">⚡</div>
        <div class="function-name">Fonction XOR (OU Exclusif)</div>
        <div class="function-description">
            La fonction XOR correspond à une fonction booléenne OR mais qui renvoie 1 uniquement si un des deux paramètre est à l'état 1.
        </div>
        <div class="truth-table">
            <table>
                <thead>
                    <tr>
                        <th>a</th>
                        <th>b</th>
                        <th>s</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>0</td>
                        <td>1</td>
                        <td>1</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>0</td>
                        <td>1</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>1</td>
                        <td>0</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<h2 class="section-title">🧮 Équations booléennes</h2>

<div class="definition-box">
    <div class="definition-title">📖 L'Algèbre de George Boole</div>
    <div class="definition-content">
        Une équation booléenne est un ensemble de fonctions booléennes. Ces fonctions répondent à l'algèbre booléenne créée par <strong>George Boole</strong> à la fin du XIXème siècle.
    </div>
</div>

<div class="highlight-fact">
    📐 <strong>Priorités opératoires :</strong> Les équations booléennes se lisent de gauche à droite et dépendent des priorités opératoires PEMDAS comme en mathématiques.
</div>

<div class="definition-box">
    <div class="definition-title">🔍 Exemple d'Évaluation</div>
    <div class="definition-content">
        <p><strong>Équation :</strong> $S = (a + b) \times c$ se lit "a ou b et c".</p>
        <p><strong>Avec :</strong> a = 1, b = 0 et c = 0</p>
        <p><strong>Évaluation :</strong></p>
        <ol>
            <li>On évalue d'abord l'opération OU : $(1+0) = 1$</li>
            <li>Puis l'opération ET : $1 \times 0 = 0$</li>
            <li><strong>Résultat :</strong> $S = 0$</li>
        </ol>
    </div>
</div>

<h2 class="section-title">🐍 Implémentation en Python</h2>

<div class="definition-box">
    <div class="definition-title">💻 Opérateurs Python</div>
    <div class="definition-content">
        Sur Python, on peut évaluer des équations booléennes avec des opérateurs transparents et des valeurs <strong>True</strong> (Vrai) et <strong>False</strong> (Faux).
    </div>
</div>

<div class="operator-grid">
    <div class="operator-card">
        <div class="operator-symbol">or</div>
        <div class="operator-name">Fonction OU</div>
        <div class="operator-python">Équivalent de +</div>
    </div>
    
    <div class="operator-card">
        <div class="operator-symbol">and</div>
        <div class="operator-name">Fonction ET</div>
        <div class="operator-python">Équivalent de ×</div>
    </div>
    
    <div class="operator-card">
        <div class="operator-symbol">not</div>
        <div class="operator-name">Fonction NON</div>
        <div class="operator-python">Négation logique</div>
    </div>
</div>

<div class="code-example">
    <div class="code-title">💻 Exemple Pratique en Python</div>
    <pre><code>a = True
b = False
c = False

# Évaluation de l'équation S = (a or b) and c
S = (a or b) and c
print(f"Résultat : {S}")  # Affiche : False

# Détail de l'évaluation
print(f"a or b = {a or b}")     # True
print(f"(a or b) and c = {S}")  # False</code></pre>
</div>

<div class="highlight-fact">
    🎯 <strong>Correspondance :</strong> True = 1 (Vrai) et False = 0 (Faux) - Python gère automatiquement la conversion entre les valeurs booléennes et numériques.
</div>
