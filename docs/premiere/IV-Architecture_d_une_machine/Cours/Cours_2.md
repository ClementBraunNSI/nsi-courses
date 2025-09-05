<style>
/* Styles modernes pour le cours Entiers Binaires et Hexadécimaux */
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

.timeline-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
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

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.info-box {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    border: 2px solid #4ecdc4;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    box-shadow: 0 5px 15px rgba(78, 205, 196, 0.2);
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

.model-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.model-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.model-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.model-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.model-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.model-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.method-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-type {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
}

.conversion-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.conversion-table table {
    width: 100%;
    border-collapse: collapse;
}

.conversion-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.conversion-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
    text-align: center;
}

.conversion-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .model-grid {
        grid-template-columns: 1fr;
    }
    
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Les circuits électroniques</h1>
    <p class="course-subtitle">Chapitre IV - Architecture d'une machine</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚡ Circuits logiques</div>
        <div class="definition-content">
            Les circuits logiques sont des <strong>éléments fondamentaux de l'informatique</strong>, qui permettent de traiter l'information de manière numérique. Ils sont utilisés dans une multitude d'applications, allant des ordinateurs et des téléphones portables aux dispositifs de contrôle de la circulation et des systèmes de sécurité.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🔌</div>
            <div class="model-name">Transistors</div>
            <div class="model-description">
                Dispositifs électroniques qui permettent de <strong>contrôler le flux de courant électrique</strong>. Ils peuvent être utilisés pour amplifier un signal ou pour activer ou désactiver un circuit.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🚪</div>
            <div class="model-name">Portes logiques</div>
            <div class="model-description">
                Circuits électroniques qui effectuent des <strong>opérations logiques de base</strong>, telles que la conjonction, la disjonction, l'inversion, etc. Elles sont construites à partir de transistors.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🏗️</div>
            <div class="model-name">Circuits complexes</div>
            <div class="model-description">
                Les portes logiques peuvent être <strong>combinées pour former des circuits logiques plus complexes</strong> qui réalisent des fonctions avancées.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🖼️ <strong>Image :</strong> ![transistor](transistor.png)
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Les portes logiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚪 Définition</div>
        <div class="definition-content">
            Une porte logique est un <strong>composant électronique</strong> qui effectue une opération logique sur un ou plusieurs signaux d'entrée pour produire un signal de sortie. Les portes logiques sont les briques de base des circuits logiques, et sont utilisées pour construire des circuits plus complexes.
        </div>
    </div>
    
    <div class="info-box">
        📊 <strong>Table de vérité :</strong> On peut associer à une porte logique une <strong>table de vérité</strong>. Elle retranscrit les résultats de l'opération suivant chaque combinaison possible des variables d'entrée.
    </div>
</div>

<div class="model-grid">
    <div class="model-card">
        <div class="model-icon">🚫</div>
        <div class="model-name">Porte NOT</div>
        <div class="model-description">
            Cette porte logique produit un signal de sortie qui est l'<strong>inverse du signal d'entrée</strong>. Si le signal d'entrée est "1", le signal de sortie est "0", et vice versa.<br><br>
            <strong>Équation :</strong> $S = \overline{A}$
        </div>
        <div class="conversion-table">
            <table>
                <tr><th>Entrée</th><th>Sortie</th></tr>
                <tr><td>0</td><td>1</td></tr>
                <tr><td>1</td><td>0</td></tr>
            </table>
        </div>
        <div class="highlight-fact">
            🖼️ ![rprnot](repr_not.png)
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">🔗</div>
        <div class="model-name">Porte AND</div>
        <div class="model-description">
            Cette porte logique produit un signal de sortie "1" <strong>uniquement si tous les signaux d'entrée sont "1"</strong>. Sinon, le signal de sortie est "0".<br><br>
            <strong>Équation :</strong> $S = A \vee B$ ou $S = A \times B$
        </div>
        <div class="conversion-table">
            <table>
                <tr><th>A</th><th>B</th><th>Sortie</th></tr>
                <tr><td>0</td><td>0</td><td>0</td></tr>
                <tr><td>0</td><td>1</td><td>0</td></tr>
                <tr><td>1</td><td>0</td><td>0</td></tr>
                <tr><td>1</td><td>1</td><td>1</td></tr>
            </table>
        </div>
        <div class="highlight-fact">
            🖼️ ![rprand](repr_and.png)
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">➕</div>
        <div class="model-name">Porte OR</div>
        <div class="model-description">
            Cette porte logique produit un signal de sortie "1" si <strong>l'un des signaux d'entrée est "1"</strong> ou si les deux signaux d'entrée sont "1". Si tous les signaux d'entrée sont "0", le signal de sortie est "0".<br><br>
            <strong>Équation :</strong> $S = A \wedge B$ ou $S = A + B$
        </div>
        <div class="conversion-table">
            <table>
                <tr><th>A</th><th>B</th><th>Sortie</th></tr>
                <tr><td>0</td><td>0</td><td>0</td></tr>
                <tr><td>0</td><td>1</td><td>1</td></tr>
                <tr><td>1</td><td>0</td><td>1</td></tr>
                <tr><td>1</td><td>1</td><td>1</td></tr>
            </table>
        </div>
        <div class="highlight-fact">
            🖼️ ![rpror](repr_or.png)
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">⚡</div>
        <div class="model-name">Porte XOR</div>
        <div class="model-description">
            Cette porte logique produit un signal de sortie "1" si <strong>un seul des signaux d'entrée est "1"</strong>. Si tous les signaux d'entrée sont "0" ou "1", le signal de sortie est "0".<br><br>
            <strong>Équation :</strong> $S = \overline{A}B + A \overline{B}$ ou $A \oplus B$
        </div>
        <div class="conversion-table">
            <table>
                <tr><th>A</th><th>B</th><th>Sortie</th></tr>
                <tr><td>0</td><td>0</td><td>0</td></tr>
                <tr><td>0</td><td>1</td><td>1</td></tr>
                <tr><td>1</td><td>0</td><td>1</td></tr>
                <tr><td>1</td><td>1</td><td>0</td></tr>
            </table>
        </div>
        <div class="highlight-fact">
            🖼️ ![rprxor](repr_xor.png)
        </div>
    </div>
</div>

## 📖 Les équations logiques

Une équation logique est une expression algébrique qui représente une fonction logique en utilisant des variables logiques, des opérateurs logiques et des constantes logiques. L'équation logique permet de décrire le comportement d'un circuit logique ou d'une fonction logique de manière formelle.
Les équations logiques suivent des règles de priorité d'opérations similaires à PEMDAS.
Par exemple, une équation logique simple pourrait être $S = A \vee B \oplus C$.
Elle se lit "A et B ou C".