<style>
/* Styles modernes pour le cours C# - Bases */
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
    
    .type-grid {
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
    <h1 class="course-title">🎯 Les Bases du C#</h1>
    <p class="course-subtitle">Découverte du langage de programmation C#</p>
</div>

<div class="concept-section">
    <h2 class="section-title">💻 Qu'est-ce que le C# ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Définition Fondamentale</div>
        <div class="definition-content">
            C# (prononcé "C Sharp") est un <strong>langage de programmation orienté objet</strong> développé par Microsoft. Il fait partie de la plateforme .NET et combine la puissance du C++ avec la simplicité du Visual Basic.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏗️</div>
            <div class="concept-name">Orienté Objet</div>
            <div class="concept-description">
                Tout est objet en C#. Le langage utilise les concepts de classes, objets, héritage et encapsulation.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔒</div>
            <div class="concept-name">Fortement Typé</div>
            <div class="concept-description">
                Chaque variable doit avoir un type défini. Cela permet de détecter les erreurs dès la compilation.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌐</div>
            <div class="concept-name">Multiplateforme</div>
            <div class="concept-description">
                Fonctionne sur Windows, Linux, macOS grâce à .NET Core et .NET 5+.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Géré par le CLR</div>
            <div class="concept-description">
                Le Common Language Runtime gère automatiquement la mémoire et l'exécution.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Le saviez-vous ?</strong> C# a été créé en 2000 par Anders Hejlsberg, le même développeur qui a créé Turbo Pascal et Delphi !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔢 Types de Données Fondamentaux</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Types Numériques</div>
        <div class="definition-content">
            C# propose plusieurs types pour représenter les nombres : les <strong>entiers</strong> pour les nombres entiers et les <strong>décimaux</strong> pour les nombres à virgule.
        </div>
    </div>
    
    <div class="type-grid">
        <div class="type-card">
            <div class="type-icon">byte</div>
            <div class="type-name">byte</div>
            <div class="type-description">
                8 bits - 0 à 255<br>
                <code>byte age = 25;</code>
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">int</div>
            <div class="type-name">int</div>
            <div class="type-description">
                32 bits - Type entier le plus courant<br>
                <code>int score = 1500;</code>
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">long</div>
            <div class="type-name">long</div>
            <div class="type-description">
                64 bits - Très grands nombres<br>
                <code>long population = 7800000000L;</code>
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">float</div>
            <div class="type-name">float</div>
            <div class="type-description">
                32 bits - ~7 chiffres de précision<br>
                <code>float prix = 19.99f;</code>
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">double</div>
            <div class="type-name">double</div>
            <div class="type-description">
                64 bits - ~15-17 chiffres de précision<br>
                <code>double pi = 3.14159265359;</code>
            </div>
        </div>
        
        <div class="type-card">
            <div class="type-icon">decimal</div>
            <div class="type-name">decimal</div>
            <div class="type-description">
                128 bits - Précision financière<br>
                <code>decimal salaire = 2500.50m;</code>
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📝 Types Texte et Caractères</div>
        <div class="definition-content">
            C# distingue les <strong>caractères individuels (char)</strong> des <strong>chaînes de caractères (string)</strong>.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔤</div>
            <div class="concept-name">char</div>
            <div class="concept-description">
                Caractère unique entre apostrophes simples.<br>
                <code>char lettre = 'A';</code>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📄</div>
            <div class="concept-name">string</div>
            <div class="concept-description">
                Chaîne de caractères entre guillemets doubles.<br>
                <code>string nom = "Jean Dupont";</code>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">✅</div>
            <div class="concept-name">bool</div>
            <div class="concept-description">
                Valeur booléenne : true ou false.<br>
                <code>bool estMajeur = true;</code>
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples de Déclarations</div>
        <pre><code>// Types numériques
int nombre = 42;
double prix = 19.99;
decimal salaire = 2500.50m;

// Types texte
char lettre = 'A';
string message = "Bonjour le monde !";

// Type booléen
bool estVrai = true;
bool estFaux = false;</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📦 Variables et Déclarations</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Déclaration de Variables</div>
        <div class="definition-content">
            En C#, chaque variable doit être <strong>déclarée avec un type</strong> avant d'être utilisée. Vous pouvez déclarer puis initialiser, ou faire les deux en même temps.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📝</div>
            <div class="concept-name">Déclaration Simple</div>
            <div class="concept-description">
                Déclarer une variable avec son type, puis l'initialiser séparément.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Déclaration + Initialisation</div>
            <div class="concept-description">
                Déclarer et initialiser une variable en une seule instruction.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Mot-clé var</div>
            <div class="concept-description">
                Laisser le compilateur déduire automatiquement le type.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Syntaxes de Déclaration</div>
        <pre><code>// Déclaration puis initialisation
int nombre;
nombre = 42;

// Déclaration avec initialisation
int autreNombre = 100;

// Déclaration multiple
int a, b, c;
int x = 1, y = 2, z = 3;

// Avec le mot-clé var (type déduit)
var nom = "Alice";        // string
var age = 25;            // int
var prix = 19.99;        // double
var estActif = true;     // bool</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Attention :</strong> Avec <code>var</code>, l'initialisation est obligatoire car le compilateur doit pouvoir déduire le type !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🧮 Opérateurs</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Opérations en C#</div>
        <div class="definition-content">
            C# propose de nombreux opérateurs pour effectuer des calculs, des comparaisons et des opérations logiques.
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
            <div class="operator-description">Soustrait le second du premier</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">*</div>
            <div class="operator-name">Multiplication</div>
            <div class="operator-description">Multiplie deux nombres</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">/</div>
            <div class="operator-name">Division</div>
            <div class="operator-description">Divise le premier par le second</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">%</div>
            <div class="operator-name">Modulo</div>
            <div class="operator-description">Reste de la division entière</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">++</div>
            <div class="operator-name">Incrémentation</div>
            <div class="operator-description">Ajoute 1 à la variable</div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples d'Opérations Arithmétiques</div>
        <pre><code>int a = 10, b = 3;

int somme = a + b;        // 13
int difference = a - b;   // 7
int produit = a * b;      // 30
int quotient = a / b;     // 3 (division entière)
int reste = a % b;        // 1

// Division décimale
double quotientDecimal = (double)a / b;  // 3.333...

// Incrémentation
int compteur = 5;
compteur++;              // compteur = 6
++compteur;              // compteur = 7</code></pre>
    </div>
    
    <div class="operator-grid">
        <div class="operator-card">
            <div class="operator-symbol">==</div>
            <div class="operator-name">Égal à</div>
            <div class="operator-description">Compare l'égalité</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">!=</div>
            <div class="operator-name">Différent de</div>
            <div class="operator-description">Compare la différence</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">></div>
            <div class="operator-name">Supérieur à</div>
            <div class="operator-description">Compare la supériorité</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol"><</div>
            <div class="operator-name">Inférieur à</div>
            <div class="operator-description">Compare l'infériorité</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">&&</div>
            <div class="operator-name">ET logique</div>
            <div class="operator-description">Vrai si les deux sont vrais</div>
        </div>
        
        <div class="operator-card">
            <div class="operator-symbol">||</div>
            <div class="operator-name">OU logique</div>
            <div class="operator-description">Vrai si au moins un est vrai</div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples de Comparaisons et Logique</div>
        <pre><code>int age = 20;
bool permis = true;

// Comparaisons
bool estMajeur = age >= 18;           // true
bool estMineur = age < 18;            // false

// Opérateurs logiques
bool peutConduire = age >= 18 && permis;  // true
bool besoinFormation = age < 18 || !permis;  // false</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💬 Entrées et Sorties Console</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Interaction avec l'Utilisateur</div>
        <div class="definition-content">
            C# utilise la classe <strong>Console</strong> pour afficher des informations et récupérer les saisies de l'utilisateur.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📤</div>
            <div class="concept-name">Console.WriteLine</div>
            <div class="concept-description">
                Affiche du texte suivi d'un retour à la ligne. Méthode principale pour l'affichage.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📥</div>
            <div class="concept-name">Console.ReadLine</div>
            <div class="concept-description">
                Lit une ligne de texte saisie par l'utilisateur. Retourne toujours une chaîne.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Conversion de Types</div>
            <div class="concept-description">
                Utilise Parse() ou TryParse() pour convertir les chaînes en nombres.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Affichage avec Console.WriteLine</div>
        <pre><code>// Affichage simple
Console.WriteLine("Bonjour le monde !");

// Affichage de variables
string nom = "Alice";
int age = 25;
Console.WriteLine("Nom : " + nom);
Console.WriteLine("Age : " + age);

// Interpolation de chaînes (moderne)
Console.WriteLine($"Je m'appelle {nom} et j'ai {age} ans.");

// Formatage avec placeholders
Console.WriteLine("Nom : {0}, Age : {1}", nom, age);</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Saisie avec Console.ReadLine</div>
        <pre><code>// Saisie de texte
Console.Write("Entrez votre nom : ");
string nom = Console.ReadLine();

// Saisie de nombres
Console.Write("Entrez votre age : ");
string ageTexte = Console.ReadLine();
int age = int.Parse(ageTexte);

// Méthode plus sûre avec TryParse
Console.Write("Entrez un nombre : ");
string input = Console.ReadLine();
if (int.TryParse(input, out int nombre))
{
    Console.WriteLine($"Vous avez saisi : {nombre}");
}
else
{
    Console.WriteLine("Ce n'est pas un nombre valide !");
}</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Important :</strong> <code>Console.ReadLine()</code> retourne toujours une chaîne de caractères. Pour traiter des nombres, il faut convertir avec <code>int.Parse()</code> ou <code>int.TryParse()</code>.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Programme Complet</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Structure d'un Programme C#</div>
        <div class="definition-content">
            Voici un exemple complet qui utilise tous les concepts vus dans ce cours.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Calculatrice Simple</div>
        <pre><code>using System;

class Program
{
    static void Main()
    {
        // Affichage du titre
        Console.WriteLine("=== Calculatrice Simple ===");
        
        // Saisie du premier nombre
        Console.Write("Entrez le premier nombre : ");
        string input1 = Console.ReadLine();
        double nombre1 = double.Parse(input1);
        
        // Saisie du second nombre
        Console.Write("Entrez le second nombre : ");
        string input2 = Console.ReadLine();
        double nombre2 = double.Parse(input2);
        
        // Calculs
        double somme = nombre1 + nombre2;
        double difference = nombre1 - nombre2;
        double produit = nombre1 * nombre2;
        
        // Affichage des résultats
        Console.WriteLine($"\nRésultats :");
        Console.WriteLine($"{nombre1} + {nombre2} = {somme}");
        Console.WriteLine($"{nombre1} - {nombre2} = {difference}");
        Console.WriteLine($"{nombre1} × {nombre2} = {produit}");
        
        // Gestion de la division par zéro
        if (nombre2 != 0)
        {
            double quotient = nombre1 / nombre2;
            Console.WriteLine($"{nombre1} ÷ {nombre2} = {quotient:F2}");
        }
        else
        {
            Console.WriteLine("Division par zéro impossible !");
        }
        
        Console.WriteLine("\nAppuyez sur une touche pour quitter...");
        Console.ReadKey();
    }
}</code></pre>
    </div>
    
    <div class="highlight-fact">
        🎯 <strong>Points clés à retenir :</strong><br>
        • <strong>Types de base :</strong> int, double, string, bool, char<br>
        • <strong>Variables :</strong> Déclaration avec type explicite ou var<br>
        • <strong>Opérateurs :</strong> Arithmétiques, comparaison, logiques<br>
        • <strong>Console :</strong> WriteLine pour afficher, ReadLine pour saisir<br>
        • <strong>Conversion :</strong> Parse() et TryParse() pour convertir les types
    </div>
</div>
