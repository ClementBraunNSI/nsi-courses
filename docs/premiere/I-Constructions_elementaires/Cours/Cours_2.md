<style>
/* Styles modernes pour le cours Types de données */
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

.concept-section {
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

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.concept-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.concept-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
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

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.type-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.type-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.type-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.type-icon {
    font-size: 2rem;
    font-weight: bold;
    color: #667eea;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Courier New', monospace;
}

.type-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 0.5rem;
}

.type-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    text-align: center;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .type-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Types de données en Python</h1>
    <p class="course-subtitle">Les types fondamentaux pour structurer vos données</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🔘 Les Booléens</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Type Booléen</div>
        <div class="definition-content">
            Le type booléen représente des valeurs de vérité avec seulement deux états possibles : <strong>True</strong> (vrai) et <strong>False</strong> (faux). Essentiel pour les conditions et le contrôle de flux.
        </div>
    </div>
    
    <div class="type-grid">
        <div class="type-card">
            <div class="type-icon">✅</div>
            <div class="type-name">True</div>
            <div class="type-description">
                Valeur vraie. Utilisée quand une condition est satisfaite ou un état est actif.
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">❌</div>
            <div class="type-name">False</div>
            <div class="type-description">
                Valeur fausse. Utilisée quand une condition n'est pas satisfaite ou un état est inactif.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Déclaration de Booléens</div>
        <pre><code>est_jeune = True
a_termine_cours = False
est_connecte = True</code></pre>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">and</div>
            <div class="concept-description">
                Opérateur ET logique. Retourne True seulement si les deux conditions sont vraies.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔀</div>
            <div class="concept-name">or</div>
            <div class="concept-description">
                Opérateur OU logique. Retourne True si au moins une des conditions est vraie.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">not</div>
            <div class="concept-description">
                Opérateur NON logique. Inverse la valeur booléenne (True devient False et vice versa).
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Opérateurs Logiques</div>
        <pre><code># Combinaisons logiques
est_jeune_et_a_termine = est_jeune and a_termine_cours  # False
est_jeune_ou_termine = est_jeune or a_termine_cours     # True
n_est_pas_termine = not a_termine_cours                 # True</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔢 Les Nombres</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Types Numériques</div>
        <div class="definition-content">
            Python propose plusieurs types pour représenter les nombres : les <strong>entiers (int)</strong> pour les nombres entiers et les <strong>flottants (float)</strong> pour les nombres décimaux.
        </div>
    </div>
    
    <div class="type-grid">
        <div class="type-card">
            <div class="type-icon">🔢</div>
            <div class="type-name">int (Entiers)</div>
            <div class="type-description">
                Nombres entiers positifs ou négatifs, sans limite de taille en Python.
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">📊</div>
            <div class="type-name">float (Flottants)</div>
            <div class="type-description">
                Nombres décimaux utilisant la norme IEEE754. Attention aux arrondis !
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Déclaration d'Entiers</div>
        <pre><code># Entiers positifs et négatifs
a = 42
b = -54
annee = 2024
temperature = -15</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Déclaration de Flottants</div>
        <pre><code># Nombres décimaux (attention au point !)
pi = 3.14159
racine_de_deux = 1.4142
prix = 19.99
temperature = -2.5</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Attention aux Flottants :</strong> Les opérations sur les flottants peuvent produire des erreurs d'arrondi. Évitez les comparaisons directes d'égalité entre flottants.
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Notation Décimale :</strong> En Python, utilisez le <strong>point</strong> (.) et non la virgule pour les décimales, suivant la convention anglo-saxonne.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📝 Caractères et Chaînes</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Type Chaîne (str)</div>
        <div class="definition-content">
            En Python, les caractères et chaînes de caractères utilisent le même type <strong>str</strong>. Un caractère est simplement une chaîne de longueur 1.
        </div>
    </div>
    
    <div class="type-grid">
        <div class="type-card">
            <div class="type-icon">🔤</div>
            <div class="type-name">Caractère</div>
            <div class="type-description">
                Une seule lettre, chiffre ou symbole. Convention : guillemets simples ('a').
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">📄</div>
            <div class="type-name">Chaîne</div>
            <div class="type-description">
                Séquence de caractères. Convention : guillemets doubles ("Hello").
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">🔍</div>
            <div class="type-name">Indexation</div>
            <div class="type-description">
                Accès aux caractères individuels par leur position (commence à 0).
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Déclaration de Chaînes</div>
        <pre><code># Chaînes et caractères
nom = "Alice"
prenom = "Bob"
lettre = 'a'
symbole = '@'</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Accès aux Caractères</div>
        <pre><code># Indexation (commence à 0)
nom = "Alice"
premiere_lettre = nom[0]   # 'A'
deuxieme_lettre = nom[1]   # 'l'
derniere_lettre = nom[-1]  # 'e' (index négatif)</code></pre>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">➕</div>
            <div class="concept-name">Concaténation</div>
            <div class="concept-description">
                Assembler des chaînes avec l'opérateur + pour créer de nouvelles chaînes.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Répétition</div>
            <div class="concept-description">
                Répéter une chaîne plusieurs fois avec l'opérateur * (multiplication).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🛠️</div>
            <div class="concept-name">Méthodes</div>
            <div class="concept-description">
                Nombreuses méthodes disponibles : .upper(), .lower(), .replace(), etc.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Convention :</strong> Utilisez les guillemets simples (') pour les caractères seuls et les guillemets doubles (") pour les chaînes de caractères.
    </div>
</div>
