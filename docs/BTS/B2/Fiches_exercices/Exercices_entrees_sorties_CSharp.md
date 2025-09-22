# Exercices C# - Entrées/Sorties Console

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

.tip-box {
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.05) 0%, rgba(6, 182, 212, 0.02) 100%);
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid var(--accent-color);
}

.tip-box h5 {
    margin: 0 0 0.5rem 0;
    color: var(--accent-color);
    font-weight: 600;
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
    <h1 class="context-header">💬 Exercices C# - Entrées/Sorties Console</h1>
    <p class="context-description">
        Maîtrisez les interactions avec l'utilisateur en C# ! Ces exercices vous apprendront à lire les données saisies par l'utilisateur 
        et à afficher des résultats formatés dans la console. Découvrez les méthodes <code>Console.ReadLine()</code>, <code>Console.Write()</code> 
        et les techniques de formatage avancées.
    </p>
</div>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🌱 Introduction</button>
    <button class="section-tab" onclick="showSection('input-section')">📥 Saisie utilisateur</button>
    <button class="section-tab" onclick="showSection('format-section')">🎨 Formatage</button>
    <button class="section-tab" onclick="showSection('interactive-section')">🎮 Programmes interactifs</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">👋 Salutation personnalisée</h4>
            <div class="exercise-content">
                <p><strong>Créez un programme qui demande le nom de l'utilisateur et l'accueille personnellement.</strong></p>
                <p>Utilisez <code>Console.ReadLine()</code> pour lire le nom et affichez "Bonjour [nom] !"</p>
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
        Console.Write("Quel est votre nom ? ");
        string nom = Console.ReadLine();
        Console.WriteLine($"Bonjour {nom} !");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">🔢 Saisie de nombres</h4>
            <div class="exercise-content">
                <p><strong>Demandez à l'utilisateur de saisir deux nombres et affichez leur somme.</strong></p>
                <p>N'oubliez pas de convertir les chaînes en nombres avec <code>int.Parse()</code> ou <code>Convert.ToInt32()</code>.</p>
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
        Console.Write("Premier nombre : ");
        int nombre1 = int.Parse(Console.ReadLine());
        
        Console.Write("Deuxième nombre : ");
        int nombre2 = int.Parse(Console.ReadLine());
        
        int somme = nombre1 + nombre2;
        Console.WriteLine($"La somme de {nombre1} et {nombre2} est {somme}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">🌱 Introduction</div>
            <h4 class="exercise-title">📏 Calcul d'aire</h4>
            <div class="exercise-content">
                <p><strong>Calculez l'aire d'un rectangle en demandant la longueur et la largeur.</strong></p>
                <p>Formule : Aire = longueur × largeur</p>
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
        Console.WriteLine("=== Calcul d'aire d'un rectangle ===");
        
        Console.Write("Longueur (en cm) : ");
        double longueur = double.Parse(Console.ReadLine());
        
        Console.Write("Largeur (en cm) : ");
        double largeur = double.Parse(Console.ReadLine());
        
        double aire = longueur * largeur;
        
        Console.WriteLine($"L'aire du rectangle est {aire} cm²");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="input-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">🎂 Calcul d'âge interactif</h4>
            <div class="exercise-content">
                <p><strong>Demandez l'année de naissance et calculez l'âge de l'utilisateur.</strong></p>
                <p>Affichez un message personnalisé selon l'âge (mineur/majeur).</p>
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
        Console.Write("En quelle année êtes-vous né(e) ? ");
        int anneeNaissance = int.Parse(Console.ReadLine());
        
        int anneeActuelle = DateTime.Now.Year;
        int age = anneeActuelle - anneeNaissance;
        
        Console.WriteLine($"Vous avez {age} ans.");
        
        if (age >= 18)
            Console.WriteLine("Vous êtes majeur(e) !");
        else
            Console.WriteLine($"Vous serez majeur(e) dans {18 - age} an(s).");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">🌡️ Convertisseur de température</h4>
            <div class="exercise-content">
                <p><strong>Convertissez des degrés Celsius en Fahrenheit.</strong></p>
                <p>Formule : F = (C × 9/5) + 32</p>
                <div class="tip-box">
                    <h5>💡 Astuce</h5>
                    <p>Utilisez <code>double.Parse()</code> pour les nombres décimaux.</p>
                </div>
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
        Console.WriteLine("=== Convertisseur Celsius → Fahrenheit ===");
        
        Console.Write("Température en Celsius : ");
        double celsius = double.Parse(Console.ReadLine());
        
        double fahrenheit = (celsius * 9.0 / 5.0) + 32;
        
        Console.WriteLine($"{celsius}°C = {fahrenheit:F1}°F");
        
        // Message selon la température
        if (celsius <= 0)
            Console.WriteLine("Il fait très froid ! ❄️");
        else if (celsius >= 30)
            Console.WriteLine("Il fait très chaud ! ☀️");
        else
            Console.WriteLine("Température agréable ! 😊");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">🛒 Calculateur de prix</h4>
            <div class="exercise-content">
                <p><strong>Calculez le prix total d'un achat avec TVA.</strong></p>
                <p>Demandez le prix HT, le taux de TVA (en %), et calculez le prix TTC.</p>
                <p>Affichez aussi le montant de la TVA.</p>
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
        Console.WriteLine("=== Calculateur de prix avec TVA ===");
        
        Console.Write("Prix HT (€) : ");
        double prixHT = double.Parse(Console.ReadLine());
        
        Console.Write("Taux de TVA (%) : ");
        double tauxTVA = double.Parse(Console.ReadLine());
        
        double montantTVA = prixHT * tauxTVA / 100;
        double prixTTC = prixHT + montantTVA;
        
        Console.WriteLine("\n=== FACTURE ===");
        Console.WriteLine($"Prix HT    : {prixHT:F2} €");
        Console.WriteLine($"TVA ({tauxTVA}%)   : {montantTVA:F2} €");
        Console.WriteLine($"Prix TTC   : {prixTTC:F2} €");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="format-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">⭐ Facile</div>
            <h4 class="exercise-title">📊 Tableau de données</h4>
            <div class="exercise-content">
                <p><strong>Créez un tableau formaté avec les informations d'une personne.</strong></p>
                <p>Demandez nom, prénom, âge et ville, puis affichez-les dans un tableau aligné.</p>
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
        Console.WriteLine("=== Saisie d'informations ===");
        
        Console.Write("Nom : ");
        string nom = Console.ReadLine();
        
        Console.Write("Prénom : ");
        string prenom = Console.ReadLine();
        
        Console.Write("Âge : ");
        int age = int.Parse(Console.ReadLine());
        
        Console.Write("Ville : ");
        string ville = Console.ReadLine();
        
        Console.WriteLine("\n" + new string('=', 40));
        Console.WriteLine("           FICHE PERSONNELLE");
        Console.WriteLine(new string('=', 40));
        Console.WriteLine($"{"Nom",-12} : {nom}");
        Console.WriteLine($"{"Prénom",-12} : {prenom}");
        Console.WriteLine($"{"Âge",-12} : {age} ans");
        Console.WriteLine($"{"Ville",-12} : {ville}");
        Console.WriteLine(new string('=', 40));
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">💰 Formatage monétaire</h4>
            <div class="exercise-content">
                <p><strong>Créez un programme qui affiche des montants avec différents formats.</strong></p>
                <p>Demandez un montant et affichez-le en euros, dollars et avec différentes précisions.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        Console.Write("Montant en euros : ");
        double montant = double.Parse(Console.ReadLine());
        
        double montantDollars = montant * 1.10; // Taux fictif
        
        Console.WriteLine("\n=== FORMATAGE MONÉTAIRE ===");
        Console.WriteLine($"Format standard    : {montant:F2} €");
        Console.WriteLine($"Format monétaire   : {montant:C}");
        Console.WriteLine($"Sans décimales     : {montant:F0} €");
        Console.WriteLine($"3 décimales        : {montant:F3} €");
        Console.WriteLine($"En dollars         : ${montantDollars:F2}");
        Console.WriteLine($"Notation comptable : {montant,15:F2} €");
        
        if (montant >= 1000)
            Console.WriteLine($"Avec séparateurs   : {montant:N2} €");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">🔥 Intermédiaire</div>
            <h4 class="exercise-title">📅 Formatage de dates</h4>
            <div class="exercise-content">
                <p><strong>Affichez la date actuelle dans différents formats.</strong></p>
                <p>Montrez les formats court, long, personnalisé et dans différentes langues.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        Console.Write("Entrez votre nom : ");
        string nom = Console.ReadLine();
        
        DateTime maintenant = DateTime.Now;
        
        Console.WriteLine($"\nBonjour {nom} !");
        Console.WriteLine("\n=== FORMATS DE DATE ===");
        Console.WriteLine($"Date courte        : {maintenant:d}");
        Console.WriteLine($"Date longue        : {maintenant:D}");
        Console.WriteLine($"Date et heure      : {maintenant:F}");
        Console.WriteLine($"Format ISO         : {maintenant:yyyy-MM-dd}");
        Console.WriteLine($"Format personnalisé: {maintenant:dddd dd MMMM yyyy}");
        Console.WriteLine($"Heure seulement    : {maintenant:HH:mm:ss}");
        Console.WriteLine($"Format US          : {maintenant.ToString("MM/dd/yyyy", CultureInfo.InvariantCulture)}");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="interactive-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">🎮 Menu interactif</h4>
            <div class="exercise-content">
                <p><strong>Créez un menu interactif avec plusieurs options.</strong></p>
                <p>Le programme doit afficher un menu, lire le choix de l'utilisateur et exécuter l'action correspondante.</p>
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
        bool continuer = true;
        
        while (continuer)
        {
            Console.Clear();
            Console.WriteLine("╔══════════════════════════════╗");
            Console.WriteLine("║        MENU PRINCIPAL        ║");
            Console.WriteLine("╠══════════════════════════════╣");
            Console.WriteLine("║ 1. Calculer une aire         ║");
            Console.WriteLine("║ 2. Convertir température     ║");
            Console.WriteLine("║ 3. Calculer l'âge            ║");
            Console.WriteLine("║ 4. Quitter                   ║");
            Console.WriteLine("╚══════════════════════════════╝");
            Console.Write("\nVotre choix (1-4) : ");
            
            string choix = Console.ReadLine();
            
            switch (choix)
            {
                case "1":
                    CalculerAire();
                    break;
                case "2":
                    ConvertirTemperature();
                    break;
                case "3":
                    CalculerAge();
                    break;
                case "4":
                    continuer = false;
                    Console.WriteLine("Au revoir !");
                    break;
                default:
                    Console.WriteLine("Choix invalide !");
                    break;
            }
            
            if (continuer)
            {
                Console.WriteLine("\nAppuyez sur une touche pour continuer...");
                Console.ReadKey();
            }
        }
    }
    
    static void CalculerAire()
    {
        Console.Write("Longueur : ");
        double longueur = double.Parse(Console.ReadLine());
        Console.Write("Largeur : ");
        double largeur = double.Parse(Console.ReadLine());
        Console.WriteLine($"Aire = {longueur * largeur} unités²");
    }
    
    static void ConvertirTemperature()
    {
        Console.Write("Température en °C : ");
        double celsius = double.Parse(Console.ReadLine());
        double fahrenheit = (celsius * 9.0 / 5.0) + 32;
        Console.WriteLine($"{celsius}°C = {fahrenheit:F1}°F");
    }
    
    static void CalculerAge()
    {
        Console.Write("Année de naissance : ");
        int annee = int.Parse(Console.ReadLine());
        int age = DateTime.Now.Year - annee;
        Console.WriteLine($"Vous avez {age} ans");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">🧮 Calculatrice avancée</h4>
            <div class="exercise-content">
                <p><strong>Créez une calculatrice interactive complète.</strong></p>
                <p>L'utilisateur saisit deux nombres et choisit l'opération. Gérez les erreurs (division par zéro, saisie invalide).</p>
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
        Console.WriteLine("🧮 CALCULATRICE AVANCÉE 🧮\n");
        
        try
        {
            Console.Write("Premier nombre : ");
            double nombre1 = double.Parse(Console.ReadLine());
            
            Console.Write("Deuxième nombre : ");
            double nombre2 = double.Parse(Console.ReadLine());
            
            Console.WriteLine("\nOpérations disponibles :");
            Console.WriteLine("+ : Addition");
            Console.WriteLine("- : Soustraction");
            Console.WriteLine("* : Multiplication");
            Console.WriteLine("/ : Division");
            Console.WriteLine("% : Modulo");
            Console.WriteLine("^ : Puissance");
            
            Console.Write("\nChoisissez une opération : ");
            string operation = Console.ReadLine();
            
            double resultat = 0;
            bool operationValide = true;
            
            switch (operation)
            {
                case "+":
                    resultat = nombre1 + nombre2;
                    break;
                case "-":
                    resultat = nombre1 - nombre2;
                    break;
                case "*":
                    resultat = nombre1 * nombre2;
                    break;
                case "/":
                    if (nombre2 == 0)
                    {
                        Console.WriteLine("❌ Erreur : Division par zéro impossible !");
                        operationValide = false;
                    }
                    else
                        resultat = nombre1 / nombre2;
                    break;
                case "%":
                    if (nombre2 == 0)
                    {
                        Console.WriteLine("❌ Erreur : Modulo par zéro impossible !");
                        operationValide = false;
                    }
                    else
                        resultat = nombre1 % nombre2;
                    break;
                case "^":
                    resultat = Math.Pow(nombre1, nombre2);
                    break;
                default:
                    Console.WriteLine("❌ Opération non reconnue !");
                    operationValide = false;
                    break;
            }
            
            if (operationValide)
            {
                Console.WriteLine($"\n✅ Résultat : {nombre1} {operation} {nombre2} = {resultat:F2}");
            }
        }
        catch (FormatException)
        {
            Console.WriteLine("❌ Erreur : Veuillez saisir des nombres valides !");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Erreur inattendue : {ex.Message}");
        }
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">🚀 Difficile</div>
            <h4 class="exercise-title">🎯 Jeu de devinette</h4>
            <div class="exercise-content">
                <p><strong>Créez un jeu où l'utilisateur doit deviner un nombre.</strong></p>
                <p>Le programme génère un nombre aléatoire entre 1 et 100. L'utilisateur a des indices "trop grand" ou "trop petit".</p>
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
        int nombreSecret = random.Next(1, 101);
        int tentatives = 0;
        int maxTentatives = 7;
        bool trouve = false;
        
        Console.WriteLine("🎯 JEU DE DEVINETTE 🎯");
        Console.WriteLine("J'ai choisi un nombre entre 1 et 100.");
        Console.WriteLine($"Vous avez {maxTentatives} tentatives pour le trouver !\n");
        
        while (!trouve && tentatives < maxTentatives)
        {
            tentatives++;
            Console.Write($"Tentative {tentatives}/{maxTentatives} - Votre nombre : ");
            
            try
            {
                int proposition = int.Parse(Console.ReadLine());
                
                if (proposition < 1 || proposition > 100)
                {
                    Console.WriteLine("⚠️ Le nombre doit être entre 1 et 100 !");
                    tentatives--; // Ne pas compter cette tentative
                    continue;
                }
                
                if (proposition == nombreSecret)
                {
                    trouve = true;
                    Console.WriteLine($"🎉 Bravo ! Vous avez trouvé en {tentatives} tentative(s) !");
                    
                    if (tentatives <= 3)
                        Console.WriteLine("🏆 Excellent ! Vous êtes un expert !");
                    else if (tentatives <= 5)
                        Console.WriteLine("👍 Bien joué !");
                    else
                        Console.WriteLine("😅 Vous y êtes arrivé de justesse !");
                }
                else if (proposition < nombreSecret)
                {
                    Console.WriteLine("📈 Trop petit ! Essayez plus grand.");
                }
                else
                {
                    Console.WriteLine("📉 Trop grand ! Essayez plus petit.");
                }
                
                if (!trouve && tentatives < maxTentatives)
                {
                    int ecart = Math.Abs(proposition - nombreSecret);
                    if (ecart <= 5)
                        Console.WriteLine("🔥 Vous êtes très proche !");
                    else if (ecart <= 10)
                        Console.WriteLine("🌡️ Vous vous rapprochez !");
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("❌ Veuillez saisir un nombre valide !");
                tentatives--; // Ne pas compter cette tentative
            }
            
            Console.WriteLine();
        }
        
        if (!trouve)
        {
            Console.WriteLine($"😞 Dommage ! Le nombre était {nombreSecret}.");
            Console.WriteLine("Essayez encore une prochaine fois !");
        }
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

</div>