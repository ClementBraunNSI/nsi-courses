# Exercices C# - Les Bases

<style>
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --danger-color: #ef4444;
    --text-color: #1f2937;
    --bg-light: #f8fafc;
    --border-color: #e2e8f0;
}

.exercise-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.section-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
    justify-content: center;
}

.section-tab {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 12px;
    cursor: pointer;
    font-size: 0.95rem;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2);
}

.section-tab:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(99, 102, 241, 0.3);
}

.section-tab.active {
    background: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color) 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(6, 182, 212, 0.3);
}

.section-content {
    display: none;
    animation: fadeIn 0.5s ease-in-out;
}

.section-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.exercise-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.exercise-card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border-left: 4px solid var(--primary-color);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.exercise-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), var(--secondary-color), var(--accent-color));
    opacity: 0;
    transition: opacity 0.3s ease;
}

.exercise-card:hover::before {
    opacity: 1;
}

.exercise-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(99, 102, 241, 0.15);
}

.exercise-card.intro {
    border-left-color: var(--success-color);
}

.exercise-card.intro:hover {
    box-shadow: 0 12px 25px rgba(16, 185, 129, 0.15);
}

.exercise-card.easy {
    border-left-color: var(--accent-color);
}

.exercise-card.easy:hover {
    box-shadow: 0 12px 25px rgba(6, 182, 212, 0.15);
}

.exercise-card.medium {
    border-left-color: var(--warning-color);
}

.exercise-card.medium:hover {
    box-shadow: 0 12px 25px rgba(245, 158, 11, 0.15);
}

.exercise-card.hard {
    border-left-color: var(--danger-color);
}

.exercise-card.hard:hover {
    box-shadow: 0 12px 25px rgba(239, 68, 68, 0.15);
}

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--text-color);
    font-size: 1.2rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.exercise-content {
    margin-bottom: 1.5rem;
    line-height: 1.7;
    color: #4b5563;
}

.exercise-content code {
    background: #f1f5f9;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    color: var(--primary-color);
    font-weight: 600;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.difficulty-badge.intro {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
    color: var(--success-color);
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.difficulty-badge.easy {
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(6, 182, 212, 0.05) 100%);
    color: var(--accent-color);
    border: 1px solid rgba(6, 182, 212, 0.2);
}

.difficulty-badge.medium {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
    color: var(--warning-color);
    border: 1px solid rgba(245, 158, 11, 0.2);
}

.difficulty-badge.hard {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
    color: var(--danger-color);
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.toggle-solution {
    background: linear-gradient(135deg, #9ca3af 0%, #6b7280 100%);
    color: white;
    border: none;
    padding: 0.7rem 1.3rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
}

.toggle-solution:hover {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(99, 102, 241, 0.3);
}

.toggle-solution.active {
    background: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color) 100%);
}

.arrow {
    transition: transform 0.3s ease;
    font-size: 1rem;
}

.toggle-solution.active .arrow {
    transform: rotate(180deg);
}

.solution-wrapper {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    margin-top: 1rem;
}

.solution-wrapper.show {
    max-height: 500px;
}

.solution {
    background: #1e293b;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
    border: 1px solid #334155;
}

.solution pre {
    margin: 0;
    color: #e2e8f0;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.9rem;
    line-height: 1.6;
    overflow-x: auto;
}

.solution code {
    color: #e2e8f0 !important;
    background: transparent !important;
}

.context-container {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(139, 92, 246, 0.05) 100%);
    border: 1px solid rgba(99, 102, 241, 0.1);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    text-align: center;
}

.context-header {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.context-description {
    font-size: 1.1rem;
    color: #6b7280;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
}
</style>

<script>
function showSection(sectionId) {
    // Masquer toutes les sections
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Désactiver tous les onglets
    const tabs = document.querySelectorAll('.section-tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Afficher la section sélectionnée
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Activer l'onglet correspondant
    event.target.classList.add('active');
}

function toggleSolution(button) {
    const wrapper = button.parentElement.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (wrapper.classList.contains('show')) {
        wrapper.classList.remove('show');
        button.classList.remove('active');
        button.innerHTML = '<span class="arrow">💡</span> Voir la solution';
    } else {
        wrapper.classList.add('show');
        button.classList.add('active');
        button.innerHTML = '<span class="arrow">💡</span> Masquer la solution';
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    const firstTab = document.querySelector('.section-tab');
    if (firstTab) {
        firstTab.click();
    }
});
</script>

<div class="exercise-container">

<div class="context-container">
    <h1 class="context-header">🎯 Exercices C# - Les Bases</h1>
    <p class="context-description">
        Découvrez les fondamentaux du C# à travers des exercices pratiques sur les variables, les types de données et les opérateurs. 
        Ces exercices vous permettront de maîtriser les concepts essentiels pour bien débuter en programmation C#.
    </p>
</div>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🌱 Introduction</button>
    <button class="section-tab" onclick="showSection('variables-section')">📦 Variables & Types</button>
    <button class="section-tab" onclick="showSection('operators-section')">⚡ Opérateurs</button>
    <button class="section-tab" onclick="showSection('practice-section')">🚀 Pratique</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">🎯 Premier programme C#</h4>
            <div class="exercise-content">
                <p><strong>Créez votre premier programme C# qui affiche "Hello, C#!" dans la console.</strong></p>
                <p>Utilisez la méthode <code>Console.WriteLine()</code> pour afficher le message.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, C#!");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">🔢 Types de données</h4>
            <div class="exercise-content">
                <p><strong>Identifiez les types C# correspondant aux valeurs suivantes :</strong></p>
                <ul>
                    <li><code>42</code></li>
                    <li><code>3.14</code></li>
                    <li><code>"Bonjour"</code></li>
                    <li><code>true</code></li>
                    <li><code>'A'</code></li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>// 42 → int (entier)
// 3.14 → double (nombre décimal)
// "Bonjour" → string (chaîne de caractères)
// true → bool (booléen)
// 'A' → char (caractère)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">📝 Déclaration de variables</h4>
            <div class="exercise-content">
                <p><strong>Déclarez et initialisez les variables suivantes :</strong></p>
                <ul>
                    <li>Une variable <code>age</code> de type entier avec la valeur 25</li>
                    <li>Une variable <code>nom</code> de type string avec votre prénom</li>
                    <li>Une variable <code>estEtudiant</code> de type booléen avec la valeur true</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>int age = 25;
string nom = "Alice";
bool estEtudiant = true;</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="variables-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">🔄 Échange de variables</h4>
            <div class="exercise-content">
                <p><strong>Écrivez un programme qui échange les valeurs de deux variables entières.</strong></p>
                <p>Déclarez deux variables <code>a = 10</code> et <code>b = 20</code>, puis échangez leurs valeurs et affichez le résultat.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        int a = 10;
        int b = 20;
        
        Console.WriteLine($"Avant échange: a = {a}, b = {b}");
        
        // Échange avec variable temporaire
        int temp = a;
        a = b;
        b = temp;
        
        Console.WriteLine($"Après échange: a = {a}, b = {b}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">🎂 Calcul d'âge</h4>
            <div class="exercise-content">
                <p><strong>Créez un programme qui calcule l'âge d'une personne.</strong></p>
                <p>Déclarez une variable pour l'année de naissance (ex: 1995) et calculez l'âge en 2024.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        int anneeNaissance = 1995;
        int anneeActuelle = 2024;
        int age = anneeActuelle - anneeNaissance;
        
        Console.WriteLine($"Année de naissance: {anneeNaissance}");
        Console.WriteLine($"Âge en {anneeActuelle}: {age} ans");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">💰 Conversion de devises</h4>
            <div class="exercise-content">
                <p><strong>Créez un convertisseur Euro vers Dollar.</strong></p>
                <p>Utilisez un taux de change de 1.10 (1€ = 1.10$). Convertissez 50€ en dollars et affichez le résultat formaté.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        double euros = 50.0;
        double tauxChange = 1.10;
        double dollars = euros * tauxChange;
        
        Console.WriteLine($"{euros:F2}€ = {dollars:F2}$");
        Console.WriteLine($"Taux de change utilisé: {tauxChange}");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="operators-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">🧮 Calculatrice simple</h4>
            <div class="exercise-content">
                <p><strong>Créez une calculatrice qui effectue les 4 opérations de base.</strong></p>
                <p>Utilisez deux nombres (ex: 15 et 4) et affichez le résultat de l'addition, soustraction, multiplication et division.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        int a = 15;
        int b = 4;
        
        Console.WriteLine($"Nombres: {a} et {b}");
        Console.WriteLine($"Addition: {a} + {b} = {a + b}");
        Console.WriteLine($"Soustraction: {a} - {b} = {a - b}");
        Console.WriteLine($"Multiplication: {a} * {b} = {a * b}");
        Console.WriteLine($"Division: {a} / {b} = {(double)a / b:F2}");
        Console.WriteLine($"Modulo: {a} % {b} = {a % b}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">🔢 Opérateurs logiques</h4>
            <div class="exercise-content">
                <p><strong>Testez les opérateurs logiques avec des variables booléennes.</strong></p>
                <p>Créez deux variables booléennes et testez les opérateurs <code>&&</code>, <code>||</code> et <code>!</code>.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        bool a = true;
        bool b = false;
        
        Console.WriteLine($"a = {a}, b = {b}");
        Console.WriteLine($"a && b = {a && b}");  // ET logique
        Console.WriteLine($"a || b = {a || b}");  // OU logique
        Console.WriteLine($"!a = {!a}");         // NON logique
        Console.WriteLine($"!b = {!b}");
        Console.WriteLine($"a && !b = {a && !b}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">📊 Comparaisons</h4>
            <div class="exercise-content">
                <p><strong>Comparez deux nombres avec tous les opérateurs de comparaison.</strong></p>
                <p>Utilisez les nombres 10 et 15, testez <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        int x = 10;
        int y = 15;
        
        Console.WriteLine($"x = {x}, y = {y}");
        Console.WriteLine($"x == y : {x == y}");  // Égal
        Console.WriteLine($"x != y : {x != y}");  // Différent
        Console.WriteLine($"x < y  : {x < y}");   // Inférieur
        Console.WriteLine($"x > y  : {x > y}");   // Supérieur
        Console.WriteLine($"x <= y : {x <= y}");  // Inférieur ou égal
        Console.WriteLine($"x >= y : {x >= y}");  // Supérieur ou égal
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="practice-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">🎯 Calculateur d'IMC</h4>
            <div class="exercise-content">
                <p><strong>Créez un calculateur d'Indice de Masse Corporelle (IMC).</strong></p>
                <p>Formule: IMC = poids (kg) / (taille (m))²</p>
                <p>Utilisez poids = 70kg et taille = 1.75m. Affichez l'IMC avec 2 décimales et une interprétation simple.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        double poids = 70.0;  // kg
        double taille = 1.75; // m
        
        double imc = poids / (taille * taille);
        
        Console.WriteLine($"Poids: {poids} kg");
        Console.WriteLine($"Taille: {taille} m");
        Console.WriteLine($"IMC: {imc:F2}");
        
        // Interprétation simple
        string interpretation;
        if (imc < 18.5)
            interpretation = "Insuffisance pondérale";
        else if (imc < 25)
            interpretation = "Poids normal";
        else if (imc < 30)
            interpretation = "Surpoids";
        else
            interpretation = "Obésité";
            
        Console.WriteLine($"Interprétation: {interpretation}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">⏰ Convertisseur de temps</h4>
            <div class="exercise-content">
                <p><strong>Convertissez un nombre de secondes en heures, minutes et secondes.</strong></p>
                <p>Exemple: 3665 secondes = 1 heure, 1 minute et 5 secondes.</p>
                <p>Utilisez les opérateurs de division entière et modulo.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        int totalSecondes = 3665;
        
        int heures = totalSecondes / 3600;
        int minutes = (totalSecondes % 3600) / 60;
        int secondes = totalSecondes % 60;
        
        Console.WriteLine($"Temps total: {totalSecondes} secondes");
        Console.WriteLine($"Conversion: {heures}h {minutes}m {secondes}s");
        
        // Version avec formatage conditionnel
        string resultat = "";
        if (heures > 0) resultat += $"{heures}h ";
        if (minutes > 0) resultat += $"{minutes}m ";
        resultat += $"{secondes}s";
        
        Console.WriteLine($"Format compact: {resultat}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">🎲 Générateur de nombres</h4>
            <div class="exercise-content">
                <p><strong>Créez un programme qui génère et analyse des nombres aléatoires.</strong></p>
                <p>Générez 3 nombres aléatoires entre 1 et 100, calculez leur somme, moyenne, et trouvez le plus grand.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class Program
{
    static void Main()
    {
        Random random = new Random();
        
        int nombre1 = random.Next(1, 101);  // 1 à 100
        int nombre2 = random.Next(1, 101);
        int nombre3 = random.Next(1, 101);
        
        Console.WriteLine($"Nombres générés: {nombre1}, {nombre2}, {nombre3}");
        
        int somme = nombre1 + nombre2 + nombre3;
        double moyenne = somme / 3.0;
        int maximum = Math.Max(Math.Max(nombre1, nombre2), nombre3);
        
        Console.WriteLine($"Somme: {somme}");
        Console.WriteLine($"Moyenne: {moyenne:F2}");
        Console.WriteLine($"Maximum: {maximum}");
        
        // Bonus: vérifier si tous sont pairs
        bool tousPairs = (nombre1 % 2 == 0) && (nombre2 % 2 == 0) && (nombre3 % 2 == 0);
        Console.WriteLine($"Tous pairs: {tousPairs}");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

</div>