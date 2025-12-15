<style>
/* Styles modernes pour le cours Fonctions en C */
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

.function-structure {
    background: rgba(76, 175, 80, 0.1);
    border-left: 4px solid #4CAF50;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.structure-title {
    color: #4CAF50;
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🔧 Fonctions en C</h1>
    <p class="course-subtitle">Modularité et réutilisabilité du code</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Qu'est-ce qu'une Fonction ?</div>
        <div class="definition-content">
            Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique. Elle permet de <strong>découper</strong> le code en petits morceaux logiques et d'éviter les répétitions. En C, le programme commence toujours par la fonction <code>main</code>.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⚙️</div>
            <div class="concept-name">Fonction</div>
            <div class="concept-description">
                Bloc de code avec un nom, un type de retour et des paramètres.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📥</div>
            <div class="concept-name">Paramètres</div>
            <div class="concept-description">
                Variables que l'on donne à la fonction pour qu'elle travaille (les ingrédients).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📤</div>
            <div class="concept-name">Type de Retour</div>
            <div class="concept-description">
                Type de la donnée renvoyée par la fonction (int, double, char...). Si elle ne renvoie rien, c'est <code>void</code>.
            </div>
        </div>
    </div>
    
    <div class="function-structure">
        <div class="structure-title">📋 Structure d'une Fonction en C</div>
        <div class="code-example">
            <pre><code>type_retour nom_de_fonction(type_1 param_1, type_2 param_2) {
    // Corps de la fonction
    // Instructions...
    
    return resultat; // Si type_retour n'est pas void
}</code></pre>
        </div>
    </div>
</div>

<div class="code-example">
    <div class="code-title">💻 Exemples de Fonctions</div>
    <pre><code>#include &lt;stdio.h&gt;

// Fonction qui convertit Celsius en Fahrenheit
// Elle prend un entier et renvoie un nombre réel (float)
float celsius_vers_fahrenheit(int temp_celsius) {
    float temp_fahrenheit = (temp_celsius * 1.8) + 32;
    return temp_fahrenheit;
}

// Fonction qui affiche un message (ne renvoie rien -> void)
void afficher_bonjour() {
    printf("Bonjour tout le monde !\n");
}

int main() {
    float f = celsius_vers_fahrenheit(25);
    printf("25 degres Celsius = %.2f Fahrenheit\n", f);
    
    afficher_bonjour();
    
    return 0;
}</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Anatomie d'une Fonction</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏷️</div>
            <div class="concept-name">Type de retour</div>
            <div class="concept-description">
                Indique ce que la fonction va "rendre". <code>int</code> pour un entier, <code>void</code> si elle ne rend rien.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📛</div>
            <div class="concept-name">Nom</div>
            <div class="concept-description">
                Le nom pour appeler la fonction (ex: <code>calculer_aire</code>). Pas d'espaces !
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📥</div>
            <div class="concept-name">Arguments</div>
            <div class="concept-description">
                Entre parenthèses, les variables nécessaires (ex: <code>int largeur</code>).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚙️</div>
            <div class="concept-name">Corps</div>
            <div class="concept-description">
                Entre accolades <code>{ }</code>, c'est le code qui s'exécute.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📤</div>
            <div class="concept-name">Return</div>
            <div class="concept-description">
                L'instruction <code>return</code> arrête la fonction et renvoie le résultat.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Attention :</strong> Si vous déclarez une fonction avec un type de retour (ex: <code>int</code>), vous <strong>DEVEZ</strong> utiliser <code>return</code> avec une valeur de ce type à la fin.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌍 Variables Locales et Globales</h2>
    
    <div class="definition-box">
        <div class="definition-title">📍 Portée des Variables</div>
        <div class="definition-content">
            La <strong>portée</strong> est la zone du code où une variable existe.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏠</div>
            <div class="concept-name">Variable Locale</div>
            <div class="concept-description">
                Déclarée <strong>dans</strong> une fonction. Elle n'existe que pendant l'exécution de cette fonction. Elle est détruite après.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌐</div>
            <div class="concept-name">Variable Globale</div>
            <div class="concept-description">
                Déclarée <strong>en dehors</strong> des fonctions (souvent tout en haut). Elle est accessible partout.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🏠 Exemple : Variable Locale</div>
        <pre><code>void ma_fonction() {
    int locale = 10; // Existe uniquement ici
    printf("%d\n", locale);
}

int main() {
    // printf("%d", locale); // ❌ Erreur : 'locale' n'existe pas ici
    ma_fonction();
    return 0;
}</code></pre>
    </div>
    
    <div class="highlight-fact">
        🔧 <strong>Conseil :</strong> Évitez les variables globales autant que possible. Elles rendent le code difficile à comprendre et à déboguer. Privilégiez les variables locales et les paramètres.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💡 Bonnes Pratiques</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📝</div>
            <div class="concept-name">Nommage</div>
            <div class="concept-description">
                Utilisez des verbes pour les actions (ex: <code>calculer_somme</code>, <code>afficher_menu</code>).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Responsabilité</div>
            <div class="concept-description">
                Une fonction = Une tâche. Si elle fait trop de choses, découpez-la.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">✅ Exemple propre</div>
        <pre><code>// Fonction simple et claire
int calculer_aire(int longueur, int largeur) {
    return longueur * largeur;
}

int main() {
    int aire = calculer_aire(10, 5);
    printf("Aire : %d\n", aire);
    return 0;
}</code></pre>
    </div>
</div>
