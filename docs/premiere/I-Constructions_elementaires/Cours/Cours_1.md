<style>
/* Styles modernes pour le cours Constructions élémentaires */
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

.operator-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.operator-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.operator-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.operator-symbol {
    font-size: 2rem;
    font-weight: bold;
    color: #667eea;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Courier New', monospace;
}

.operator-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 0.5rem;
}

.operator-description {
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
    
    .operator-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Constructions élémentaires en Python</h1>
    <p class="course-subtitle">Les fondements de la programmation Python</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🤖 Qu'est-ce qu'un programme ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Définition Fondamentale</div>
        <div class="definition-content">
            Un <strong>programme</strong> est une suite d'instructions élémentaires destinées à être exécutées par un ordinateur.
        </div>
 </div>
     
     <div class="concept-grid">       <div class="concept-card">
            <div class="concept-icon">🐍</div>
            <div class="concept-name">Langage Python</div>
            <div class="concept-description">
                Python est un langage de <strong>haut niveau</strong>, plus proche de nous (utilisateurs) que de l'ordinateur (processeur).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Exécution Séquentielle</div>
            <div class="concept-description">
                Les instructions sont réalisées de manière <strong>séquentielle</strong> - les unes après les autres, dans l'ordre.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Les Opérateurs</div>
        <div class="definition-content">
            Un <strong>opérateur</strong> est un caractère ou un ensemble de caractères qui correspond à une opération pouvant être réalisée par le processeur.
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💾 Instanciation</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Concept d'Instanciation</div>
        <div class="definition-content">
            L'<strong>instanciation</strong> est une instruction qui permet d'associer une <strong>valeur</strong> à une <strong>variable</strong>. Une variable en Python est une chaîne de caractères que l'on associe à un <strong>type</strong> (domaine de valeurs).
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Opérateur d'Assignation</div>
            <div class="concept-description">
                L'instanciation utilise l'opérateur <strong>=</strong>. Pour la machine, cela revient à associer un espace mémoire à la valeur désignée.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏷️</div>
            <div class="concept-name">Variables et Types</div>
            <div class="concept-description">
                Les variables peuvent contenir différents types : entiers, chaînes de caractères, tableaux, listes, nombres réels, ou objets personnalisés.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples d'Instanciation</div>
        <pre><code># Instancier a à la valeur 42
a = 42

# Instancier ma_chaine_de_caractere à la valeur 'Hello World!'
ma_chaine_de_caractere = 'Hello World!'</code></pre>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Base de la programmation :</strong> L'instanciation est l'opération fondamentale qui consiste à associer une valeur à une variable.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🧮 Opérations Mathématiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Calculs en Python</div>
        <div class="definition-content">
            Python permet de réaliser des opérations mathématiques grâce à des <strong>opérateurs</strong> qui utilisent 2 valeurs, comme nos opérations sur papier.
        </div>
    </div>
    
    <div class="operator-grid">
        <div class="operator-card">
            <div class="operator-symbol">+</div>
            <div class="operator-name">Addition</div>
            <div class="operator-description">Additionne deux nombres</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">-</div>
            <div class="operator-name">Soustraction</div>
            <div class="operator-description">Soustrait le second nombre du premier</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">*</div>
            <div class="operator-name">Multiplication</div>
            <div class="operator-description">Multiplie deux nombres</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">/</div>
            <div class="operator-name">Division</div>
            <div class="operator-description">Divise le premier nombre par le second</div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples d'Opérations</div>
        <pre><code>a = 3 + 2  # Addition : a = 5
b = 5 - 3  # Soustraction : b = 2
c = a * b  # Multiplication : c = 10
d = b / a  # Division : d = 0.4</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Important :</strong> Les opérations mathématiques sont réservées aux variables de type entiers ou nombres réels. Attention aux imprécisions avec les flottants !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚖️ Opérations de Comparaisons</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Comparaisons en Python</div>
        <div class="definition-content">
            Python permet de comparer des variables pour évaluer des relations d'ordre ou d'égalité. <strong>Attention :</strong> on ne peut comparer que des éléments du même type !
        </div>
    </div>
    
    <div class="operator-grid">
        <div class="operator-card">
            <div class="operator-symbol">></div>
            <div class="operator-name">Supérieur</div>
            <div class="operator-description">a plus grand que b</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol"><</div>
            <div class="operator-name">Inférieur</div>
            <div class="operator-description">a plus petit que b</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">>=</div>
            <div class="operator-name">Supérieur ou égal</div>
            <div class="operator-description">a plus grand ou égal à b</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol"><=</div>
            <div class="operator-name">Inférieur ou égal</div>
            <div class="operator-description">a plus petit ou égal à b</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">==</div>
            <div class="operator-name">Égalité</div>
            <div class="operator-description">a est égal à b</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">!=</div>
            <div class="operator-name">Différence</div>
            <div class="operator-description">a est différent de b</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Erreur fréquente :</strong> Ne pas confondre <code>=</code> (assignation) et <code>==</code> (comparaison) ! Utiliser <code>=</code> dans une comparaison provoque une SyntaxError.
    </div>
    
    <div class="highlight-fact">
        🚫 <strong>TypeError :</strong> Comparer des éléments de types différents génère une erreur. Exemple : <code>5 > "hello"</code> est invalide.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💬 Affichage et Demande à l'Utilisateur</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📺</div>
            <div class="concept-name">Fonction print()</div>
            <div class="concept-description">
                Affiche des informations à l'écran : chaînes de caractères, nombres, résultats de calculs. Peut concaténer plusieurs éléments séparés par des virgules.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⌨️</div>
            <div class="concept-name">Fonction input()</div>
            <div class="concept-description">
                Capture les données saisies par l'utilisateur. Affiche un message d'invitation et renvoie la saisie sous forme de chaîne de caractères.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples d'Utilisation</div>
        <pre><code># Affichage simple
print("Bonjour le monde !")

# Affichage de plusieurs éléments
print("Bonjour", "le monde", 42)  # Affiche : Bonjour le monde 42

# Demande à l'utilisateur
nom = input("Quel est votre nom ? ")
print("Bonjour", nom)

# Conversion de type pour les nombres
age_str = input("Quel est votre âge ? ")
age = int(age_str)  # Conversion en entier</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Important :</strong> La fonction <code>input()</code> renvoie toujours une chaîne de caractères (string). Pour traiter des nombres, il faut convertir le type avec <code>int()</code> ou <code>float()</code>.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔀 Conditions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Structure Conditionnelle</div>
        <div class="definition-content">
            Les conditions permettent d'exécuter du code selon des critères spécifiques grâce à l'instruction <strong>if</strong>. Elles évaluent des comparaisons, des états de variables ou des valeurs.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🚪</div>
            <div class="concept-name">if</div>
            <div class="concept-description">
                Exécute le code si la condition est vraie. C'est la structure de base pour les décisions.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">elif</div>
            <div class="concept-description">
                "Else if" - teste une nouvelle condition si la précédente était fausse. Peut être répété plusieurs fois.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏁</div>
            <div class="concept-name">else</div>
            <div class="concept-description">
                Exécute le code si aucune des conditions précédentes n'était vraie. Optionnel.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Test de Majorité</div>
        <pre><code># Demander à l'utilisateur son âge
age = input('Quel est votre âge ? ')
age_entier = int(age)  # Conversion en entier

# Condition d'affichage
if age_entier >= 18:
    print('Vous êtes majeur')
else:
    print('Vous êtes mineur')</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Évaluation de Notes</div>
        <pre><code># Demande d'une note (A, B, C)
note = input('Quelle est la note à évaluer ? ')

if note == 'A':
    print('Très bien')
elif note == 'B':
    print('Un peu plus pour exceller')
elif note == 'C':
    print('Peut mieux faire')
else:
    print('Poursuis tes efforts')</code></pre>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Astuce :</strong> Le bloc <code>else</code> est optionnel. Si aucune action n'est nécessaire quand toutes les conditions sont fausses, vous pouvez l'omettre.
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Performance :</strong> Les conditions sont évaluées dans l'ordre. Placez les conditions les plus probables en premier pour optimiser les performances.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Boucles</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Répétition de Code</div>
        <div class="definition-content">
            Les boucles permettent de répéter un bloc de code plusieurs fois. Python propose deux types principaux : <strong>for</strong> (nombre d'itérations défini) et <strong>while</strong> (condition de continuation).
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔢</div>
            <div class="concept-name">Boucle for</div>
            <div class="concept-description">
                Répète un code un nombre défini de fois. Idéale quand on connaît le nombre d'itérations à l'avance.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⏳</div>
            <div class="concept-name">Boucle while</div>
            <div class="concept-description">
                Répète un code tant qu'une condition reste vraie. Utilisée quand le nombre d'itérations est inconnu.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">range()</div>
            <div class="concept-description">
                Fonction qui génère une séquence de nombres. Essentielle pour les boucles for avec compteur.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Boucle for : Affichage de 1 à n</div>
        <pre><code>n = 30
for i in range(1, n+1):
    print(i)

# Variantes de range() :
# range(10)      → 0, 1, 2, ..., 9
# range(1, 10)   → 1, 2, 3, ..., 9
# range(1, 10, 2) → 1, 3, 5, 7, 9</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Boucle while : Même résultat</div>
        <pre><code>n = 30
i = 1
# On veut afficher les nombres de 1 à n
while i <= n:
    print(i)
    i = i + 1  # Incrémentation obligatoire !</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Danger :</strong> Attention aux boucles infinies ! Dans une boucle <code>while</code>, oublier d'incrémenter la variable de contrôle peut créer une boucle qui ne s'arrête jamais.
    </div>
    
    <div class="highlight-fact">
         💡 <strong>Avantage :</strong> La boucle <code>for</code> s'arrête forcément car elle itère sur un nombre défini d'éléments. Utilisez <code>for</code> quand vous connaissez le nombre d'itérations, <code>while</code> pour les conditions dynamiques.
     </div>
 </div>

</body>
</html>
