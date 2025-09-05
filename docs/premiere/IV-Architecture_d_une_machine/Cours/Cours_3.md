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
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
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
    <h1 class="course-title">📚 Jeux d'instruction</h1>
    <p class="course-subtitle">Chapitre IV - Architecture d'une machine</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Jeu d'instruction</div>
        <div class="definition-content">
            Un jeu d'instruction correspond à l'<strong>ensemble des opérations réalisables et câblées</strong> pour un processeur donné.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🔢</div>
            <div class="model-name">Binaire</div>
            <div class="model-description">
                Les processeurs, par leur composition ne comprennent que le <strong>binaire</strong> mais le système d'exploitation permet de traduire les langages de programmation en opérations compréhensibles par le processeur.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🏷️</div>
            <div class="model-name">Mnémonique</div>
            <div class="model-description">
                On appelle <strong>mnémonique</strong> une instruction compréhensible par le processeur. Suivant le processeur, il existe divers mnémoniques.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⚙️</div>
            <div class="model-name">Assembleur</div>
            <div class="model-description">
                Il existe un langage de programmation proche du processeur et compréhensible par l'être humain : <strong>l'assembleur</strong>.
            </div>
        </div>
    </div>
    
    <div class="info-box">
        🔧 <strong>Types d'opérations :</strong> Il existe diverses opérations, comme en python, que l'on peut distinguer :
    </div>
</div>

<div class="model-grid">
    <div class="model-card">
        <div class="model-icon">💾</div>
        <div class="model-name">Opérations Registres</div>
        <div class="model-description">
            <strong>STR X, Val</strong> : Stocke la valeur Val dans le registre X.<br><br>
            <strong>MOV A B</strong> : Déplace les valeurs d'un registre A à un autre B.
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">🧮</div>
        <div class="model-name">Opérations Mathématiques</div>
        <div class="model-description">
            <strong>ADD X Y</strong> : Ajouter deux valeurs.<br>
            <strong>SUB X Y</strong> : Soustraire un opérande d'un autre.<br>
            <strong>MUL X Y</strong> : Multiplier deux valeurs.<br>
            <strong>DIV X Y</strong> : Diviser un opérande par un autre.
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">🔗</div>
        <div class="model-name">Opérations Booléennes</div>
        <div class="model-description">
            <strong>AND</strong> : Effectuer une opération logique AND entre deux valeurs.<br>
            <strong>OR</strong> : Effectuer une opération logique OR entre deux valeurs.<br>
            <strong>XOR</strong> : Effectuer une opération logique XOR entre deux valeurs.
        </div>
    </div>
    
    <div class="model-card">
        <div class="model-icon">🔄</div>
        <div class="model-name">Boucles et Conditions</div>
        <div class="model-description">
            Pour les boucles, on saute à une certaine étape indiquée dans le code du programme après une comparaison. Pour les conditions, l'endroit du saut correspond au résultat que l'on souhaite. On déclare ce que l'on appelle des <strong>ancres</strong>.
        </div>
    </div>
</div>

<div class="method-grid">
    <div class="method-card">
        <div class="method-type">🔍 CMP A B</div>
        <div class="definition-content">
            Comparer deux valeurs.
        </div>
    </div>
    
    <div class="method-card">
        <div class="method-type">⚖️ JE</div>
        <div class="definition-content">
            Sauter à une autre instruction si les valeurs sont égales (Jump if Equal).
        </div>
    </div>
    
    <div class="method-card">
        <div class="method-type">❌ JNE</div>
        <div class="definition-content">
            Sauter à une autre instruction si les valeurs ne sont pas égales (Jump if Not Equal).
        </div>
    </div>
    
    <div class="method-card">
        <div class="method-type">📈 JG</div>
        <div class="definition-content">
            Sauter à une autre instruction si un opérande est supérieur à l'autre (Jump if Greater).
        </div>
    </div>
    
    <div class="method-card">
        <div class="method-type">📉 JL</div>
        <div class="definition-content">
            Sauter à une autre instruction si un opérande est inférieur à l'autre (Jump if Less).
        </div>
    </div>
</div>

L'assembleur n'est pas au programme, mais il permet de mieux comprendre le fonctionnement d'un ordinateur et le fait qu'il soit un modèle de machine séquentiel.

*Exemple:*

```python
STR A, 15 # Stocke 15 dans A
ADD A, 10 # Ajoute 10 à la valeur dans A
STR B, 10 # Stocke 10 dans B
LOAD A # Met A dans la mémoire active
MUL 10 # Multiplie la valeur dans la mémoire active par 10
STR A # Stocke le résultat de la mémoire active dans A 
CMP A, B
boucle:
JE fin_boucle
STR C, 0
ADD B, 1
ADD C,1
JMP boucle
fin_boucle
```