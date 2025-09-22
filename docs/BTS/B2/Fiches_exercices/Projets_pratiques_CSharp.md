# Projets Pratiques C# - Applications Complètes

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
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.exercise-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
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

.exercise-card.beginner {
    border-left-color: var(--success-color);
}

.exercise-card.beginner:hover {
    box-shadow: 0 12px 25px rgba(16, 185, 129, 0.15);
}

.exercise-card.intermediate {
    border-left-color: var(--warning-color);
}

.exercise-card.intermediate:hover {
    box-shadow: 0 12px 25px rgba(245, 158, 11, 0.15);
}

.exercise-card.advanced {
    border-left-color: var(--danger-color);
}

.exercise-card.advanced:hover {
    box-shadow: 0 12px 25px rgba(239, 68, 68, 0.15);
}

.exercise-card.expert {
    border-left-color: var(--secondary-color);
}

.exercise-card.expert:hover {
    box-shadow: 0 12px 25px rgba(139, 92, 246, 0.15);
}

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--text-color);
    font-size: 1.3rem;
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

.difficulty-badge.beginner {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
    color: var(--success-color);
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.difficulty-badge.intermediate {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
    color: var(--warning-color);
    border: 1px solid rgba(245, 158, 11, 0.2);
}

.difficulty-badge.advanced {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
    color: var(--danger-color);
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.difficulty-badge.expert {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%);
    color: var(--secondary-color);
    border: 1px solid rgba(139, 92, 246, 0.2);
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
    transition: max-height 0.5s ease;
    margin-top: 1rem;
}

.solution-wrapper.show {
    max-height: 800px;
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
    font-size: 0.85rem;
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
    max-width: 900px;
    margin: 0 auto;
}

.features-list {
    background: #f8fafc;
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid var(--accent-color);
}

.features-list h5 {
    margin: 0 0 0.5rem 0;
    color: var(--accent-color);
    font-weight: 600;
}

.features-list ul {
    margin: 0;
    padding-left: 1.2rem;
}

.features-list li {
    margin-bottom: 0.3rem;
    color: #4b5563;
}

.project-stats {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
    flex-wrap: wrap;
}

.stat-item {
    background: rgba(99, 102, 241, 0.1);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    color: var(--primary-color);
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
        button.innerHTML = '<span class="arrow">💡</span> Voir la solution complète';
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
    <h1 class="context-header">🚀 Projets Pratiques C# - Applications Complètes</h1>
    <p class="context-description">
        Mettez en pratique tous vos acquis en C# avec des projets complets et réalistes ! 
        Ces applications combinent variables, types, opérateurs, entrées/sorties et logique métier 
        pour créer des programmes utiles et fonctionnels. Chaque projet est conçu pour renforcer 
        votre compréhension et votre maîtrise du langage C#.
    </p>
</div>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('beginner-section')">🌱 Débutant</button>
    <button class="section-tab" onclick="showSection('intermediate-section')">🔥 Intermédiaire</button>
    <button class="section-tab" onclick="showSection('advanced-section')">🚀 Avancé</button>
    <button class="section-tab" onclick="showSection('expert-section')">👑 Expert</button>
</div>

<div id="beginner-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card beginner">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge beginner">🌱 Débutant</div>
            <h4 class="exercise-title">🏪 Système de Caisse</h4>
            <div class="exercise-content">
                <p><strong>Créez un système de caisse simple pour un magasin.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Saisie du prix de plusieurs articles</li>
                        <li>Calcul du sous-total</li>
                        <li>Application d'une remise (en %)</li>
                        <li>Calcul de la TVA (20%)</li>
                        <li>Affichage du ticket de caisse formaté</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 30-45 min</span>
                    <span class="stat-item">📝 ~50 lignes</span>
                    <span class="stat-item">🎯 Variables, calculs, formatage</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class SystemeCaisse
{
    static void Main()
    {
        Console.WriteLine("🏪 SYSTÈME DE CAISSE 🏪");
        Console.WriteLine("========================\n");
        
        // Variables pour le calcul
        double sousTotal = 0;
        int nombreArticles = 0;
        
        // Saisie des articles
        Console.WriteLine("Saisissez le prix des articles (0 pour terminer) :");
        
        while (true)
        {
            Console.Write($"Article {nombreArticles + 1} (€) : ");
            double prix = double.Parse(Console.ReadLine());
            
            if (prix == 0) break;
            
            if (prix > 0)
            {
                sousTotal += prix;
                nombreArticles++;
                Console.WriteLine($"  ✓ Article ajouté : {prix:F2}€");
            }
            else
            {
                Console.WriteLine("  ❌ Prix invalide !");
            }
        }
        
        if (nombreArticles == 0)
        {
            Console.WriteLine("Aucun article saisi. Au revoir !");
            return;
        }
        
        // Remise
        Console.Write("\nRemise en % (0 si aucune) : ");
        double pourcentageRemise = double.Parse(Console.ReadLine());
        double montantRemise = sousTotal * pourcentageRemise / 100;
        double totalApresRemise = sousTotal - montantRemise;
        
        // TVA
        double tauxTVA = 20.0;
        double montantTVA = totalApresRemise * tauxTVA / 100;
        double totalTTC = totalApresRemise + montantTVA;
        
        // Affichage du ticket
        Console.Clear();
        Console.WriteLine("╔══════════════════════════════════╗");
        Console.WriteLine("║           TICKET DE CAISSE       ║");
        Console.WriteLine("╠══════════════════════════════════╣");
        Console.WriteLine($"║ Nombre d'articles : {nombreArticles,12} ║");
        Console.WriteLine($"║ Sous-total       : {sousTotal,12:F2}€ ║");
        
        if (pourcentageRemise > 0)
        {
            Console.WriteLine($"║ Remise ({pourcentageRemise}%)      : -{montantRemise,11:F2}€ ║");
            Console.WriteLine($"║ Total après remise: {totalApresRemise,11:F2}€ ║");
        }
        
        Console.WriteLine($"║ TVA ({tauxTVA}%)         : {montantTVA,12:F2}€ ║");
        Console.WriteLine("╠══════════════════════════════════╣");
        Console.WriteLine($"║ TOTAL TTC        : {totalTTC,12:F2}€ ║");
        Console.WriteLine("╚══════════════════════════════════╝");
        
        // Statistiques
        double prixMoyen = sousTotal / nombreArticles;
        Console.WriteLine($"\n📊 Prix moyen par article : {prixMoyen:F2}€");
        Console.WriteLine($"💰 Économies réalisées : {montantRemise:F2}€");
        
        Console.WriteLine("\nMerci de votre achat ! 😊");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card beginner">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge beginner">🌱 Débutant</div>
            <h4 class="exercise-title">📊 Calculateur de Notes</h4>
            <div class="exercise-content">
                <p><strong>Développez un système de gestion des notes d'un étudiant.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Saisie de plusieurs notes (sur 20)</li>
                        <li>Calcul de la moyenne générale</li>
                        <li>Détermination de la mention</li>
                        <li>Affichage du bulletin formaté</li>
                        <li>Statistiques (note min/max, écart-type)</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 25-35 min</span>
                    <span class="stat-item">📝 ~60 lignes</span>
                    <span class="stat-item">🎯 Tableaux, moyennes, conditions</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Collections.Generic;
using System.Linq;

class CalculateurNotes
{
    static void Main()
    {
        Console.WriteLine("📊 CALCULATEUR DE NOTES 📊");
        Console.WriteLine("===========================\n");
        
        // Informations étudiant
        Console.Write("Nom de l'étudiant : ");
        string nom = Console.ReadLine();
        
        Console.Write("Matière : ");
        string matiere = Console.ReadLine();
        
        // Saisie des notes
        List<double> notes = new List<double>();
        Console.WriteLine("\nSaisissez les notes (sur 20, -1 pour terminer) :");
        
        int numeroNote = 1;
        while (true)
        {
            Console.Write($"Note {numeroNote} : ");
            double note = double.Parse(Console.ReadLine());
            
            if (note == -1) break;
            
            if (note >= 0 && note <= 20)
            {
                notes.Add(note);
                numeroNote++;
                Console.WriteLine($"  ✓ Note enregistrée : {note:F1}/20");
            }
            else
            {
                Console.WriteLine("  ❌ Note invalide (0-20) !");
            }
        }
        
        if (notes.Count == 0)
        {
            Console.WriteLine("Aucune note saisie !");
            return;
        }
        
        // Calculs
        double moyenne = notes.Average();
        double noteMin = notes.Min();
        double noteMax = notes.Max();
        
        // Calcul de l'écart-type
        double variance = notes.Select(x => Math.Pow(x - moyenne, 2)).Average();
        double ecartType = Math.Sqrt(variance);
        
        // Détermination de la mention
        string mention;
        string emoji;
        
        if (moyenne >= 16)
        {
            mention = "Très Bien";
            emoji = "🏆";
        }
        else if (moyenne >= 14)
        {
            mention = "Bien";
            emoji = "🥈";
        }
        else if (moyenne >= 12)
        {
            mention = "Assez Bien";
            emoji = "🥉";
        }
        else if (moyenne >= 10)
        {
            mention = "Passable";
            emoji = "✅";
        }
        else
        {
            mention = "Insuffisant";
            emoji = "❌";
        }
        
        // Affichage du bulletin
        Console.Clear();
        Console.WriteLine("╔════════════════════════════════════════╗");
        Console.WriteLine("║              BULLETIN DE NOTES         ║");
        Console.WriteLine("╠════════════════════════════════════════╣");
        Console.WriteLine($"║ Étudiant : {nom,-27} ║");
        Console.WriteLine($"║ Matière  : {matiere,-27} ║");
        Console.WriteLine("╠════════════════════════════════════════╣");
        Console.WriteLine($"║ Nombre de notes    : {notes.Count,15} ║");
        Console.WriteLine($"║ Note minimale      : {noteMin,15:F1} ║");
        Console.WriteLine($"║ Note maximale      : {noteMax,15:F1} ║");
        Console.WriteLine($"║ Moyenne générale   : {moyenne,15:F2} ║");
        Console.WriteLine($"║ Écart-type         : {ecartType,15:F2} ║");
        Console.WriteLine("╠════════════════════════════════════════╣");
        Console.WriteLine($"║ Mention : {mention,-20} {emoji,7} ║");
        Console.WriteLine("╚════════════════════════════════════════╝");
        
        // Détail des notes
        Console.WriteLine("\n📝 Détail des notes :");
        for (int i = 0; i < notes.Count; i++)
        {
            string status = notes[i] >= 10 ? "✅" : "❌";
            Console.WriteLine($"  Note {i + 1,2} : {notes[i],5:F1}/20 {status}");
        }
        
        // Conseils
        Console.WriteLine("\n💡 Conseils :");
        if (moyenne >= 15)
            Console.WriteLine("Excellent travail ! Continuez ainsi ! 🌟");
        else if (moyenne >= 12)
            Console.WriteLine("Bon niveau, quelques efforts pour viser l'excellence ! 💪");
        else if (moyenne >= 10)
            Console.WriteLine("Résultats corrects, mais des progrès sont possibles ! 📈");
        else
            Console.WriteLine("Il faut redoubler d'efforts pour la prochaine fois ! 🎯");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="intermediate-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intermediate">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intermediate">🔥 Intermédiaire</div>
            <h4 class="exercise-title">🏦 Simulateur de Crédit</h4>
            <div class="exercise-content">
                <p><strong>Créez un simulateur de crédit bancaire complet.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Calcul des mensualités (formule mathématique)</li>
                        <li>Tableau d'amortissement détaillé</li>
                        <li>Calcul du coût total du crédit</li>
                        <li>Simulation de différents scénarios</li>
                        <li>Graphique ASCII de l'évolution</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 45-60 min</span>
                    <span class="stat-item">📝 ~100 lignes</span>
                    <span class="stat-item">🎯 Formules, boucles, formatage</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;

class SimulateurCredit
{
    static void Main()
    {
        Console.WriteLine("🏦 SIMULATEUR DE CRÉDIT BANCAIRE 🏦");
        Console.WriteLine("===================================\n");
        
        // Saisie des paramètres
        Console.Write("Montant du crédit (€) : ");
        double capital = double.Parse(Console.ReadLine());
        
        Console.Write("Taux d'intérêt annuel (%) : ");
        double tauxAnnuel = double.Parse(Console.ReadLine());
        
        Console.Write("Durée en années : ");
        int dureeAnnees = int.Parse(Console.ReadLine());
        
        // Calculs préliminaires
        double tauxMensuel = tauxAnnuel / 100 / 12;
        int nombreMois = dureeAnnees * 12;
        
        // Calcul de la mensualité (formule mathématique)
        double mensualite;
        if (tauxMensuel == 0)
        {
            mensualite = capital / nombreMois;
        }
        else
        {
            mensualite = capital * tauxMensuel * Math.Pow(1 + tauxMensuel, nombreMois) 
                        / (Math.Pow(1 + tauxMensuel, nombreMois) - 1);
        }
        
        double coutTotal = mensualite * nombreMois;
        double coutCredit = coutTotal - capital;
        
        // Affichage du résumé
        Console.Clear();
        Console.WriteLine("╔══════════════════════════════════════════╗");
        Console.WriteLine("║           SIMULATION DE CRÉDIT           ║");
        Console.WriteLine("╠══════════════════════════════════════════╣");
        Console.WriteLine($"║ Capital emprunté    : {capital,15:F2}€ ║");
        Console.WriteLine($"║ Taux annuel         : {tauxAnnuel,15:F2}% ║");
        Console.WriteLine($"║ Durée               : {dureeAnnees,12} ans ║");
        Console.WriteLine($"║ Nombre de mensualités: {nombreMois,12} ║");
        Console.WriteLine("╠══════════════════════════════════════════╣");
        Console.WriteLine($"║ Mensualité          : {mensualite,15:F2}€ ║");
        Console.WriteLine($"║ Coût total          : {coutTotal,15:F2}€ ║");
        Console.WriteLine($"║ Coût du crédit      : {coutCredit,15:F2}€ ║");
        Console.WriteLine("╚══════════════════════════════════════════╝");
        
        Console.WriteLine("\nAppuyez sur une touche pour voir le tableau d'amortissement...");
        Console.ReadKey();
        
        // Tableau d'amortissement
        Console.Clear();
        Console.WriteLine("📊 TABLEAU D'AMORTISSEMENT");
        Console.WriteLine("═══════════════════════════════════════════════════════════════");
        Console.WriteLine("Mois │   Mensualité │   Intérêts │    Capital │ Capital Restant");
        Console.WriteLine("─────┼──────────────┼────────────┼────────────┼────────────────");
        
        double capitalRestant = capital;
        double totalInterets = 0;
        
        for (int mois = 1; mois <= nombreMois; mois++)
        {
            double interetsMois = capitalRestant * tauxMensuel;
            double capitalRembourse = mensualite - interetsMois;
            capitalRestant -= capitalRembourse;
            totalInterets += interetsMois;
            
            // Affichage seulement des 12 premiers mois et des 12 derniers
            if (mois <= 12 || mois > nombreMois - 12)
            {
                Console.WriteLine($"{mois,4} │ {mensualite,12:F2}€ │ {interetsMois,10:F2}€ │ {capitalRembourse,10:F2}€ │ {Math.Max(0, capitalRestant),14:F2}€");
            }
            else if (mois == 13)
            {
                Console.WriteLine("  ...│      ...     │     ...    │     ...    │       ...      ");
            }
        }
        
        Console.WriteLine("═══════════════════════════════════════════════════════════════");
        Console.WriteLine($"TOTAL│ {coutTotal,12:F2}€ │ {totalInterets,10:F2}€ │ {capital,10:F2}€ │ {0,14:F2}€");
        
        // Graphique ASCII de l'évolution
        Console.WriteLine("\n📈 ÉVOLUTION DU CAPITAL RESTANT");
        Console.WriteLine("═══════════════════════════════════════");
        
        capitalRestant = capital;
        int largeurGraphique = 30;
        
        for (int annee = 0; annee <= dureeAnnees; annee++)
        {
            int barreLength = (int)((capitalRestant / capital) * largeurGraphique);
            string barre = new string('█', barreLength) + new string('░', largeurGraphique - barreLength);
            
            Console.WriteLine($"An {annee,2} │{barre}│ {capitalRestant,10:F0}€");
            
            // Simulation d'une année
            for (int mois = 1; mois <= 12 && annee < dureeAnnees; mois++)
            {
                double interetsMois = capitalRestant * tauxMensuel;
                double capitalRembourse = mensualite - interetsMois;
                capitalRestant = Math.Max(0, capitalRestant - capitalRembourse);
            }
        }
        
        // Comparaison avec d'autres durées
        Console.WriteLine("\n🔍 COMPARAISON AVEC D'AUTRES DURÉES");
        Console.WriteLine("═══════════════════════════════════════════════════════");
        Console.WriteLine("Durée │ Mensualité │ Coût total │ Coût crédit │ Différence");
        Console.WriteLine("──────┼────────────┼────────────┼─────────────┼───────────");
        
        for (int duree = Math.Max(1, dureeAnnees - 2); duree <= dureeAnnees + 2; duree++)
        {
            int mois = duree * 12;
            double mens = capital * tauxMensuel * Math.Pow(1 + tauxMensuel, mois) 
                         / (Math.Pow(1 + tauxMensuel, mois) - 1);
            double cout = mens * mois;
            double coutCred = cout - capital;
            double diff = coutCred - coutCredit;
            
            string marqueur = duree == dureeAnnees ? "►" : " ";
            Console.WriteLine($"{marqueur}{duree,4} │ {mens,10:F2}€ │ {cout,10:F2}€ │ {coutCred,11:F2}€ │ {diff,+9:F2}€");
        }
        
        Console.WriteLine("\n💡 Conseil : Plus la durée est courte, moins le crédit coûte cher !");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intermediate">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intermediate">🔥 Intermédiaire</div>
            <h4 class="exercise-title">🎰 Machine à Sous</h4>
            <div class="exercise-content">
                <p><strong>Développez une machine à sous avec système de crédits.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Système de crédits et de mises</li>
                        <li>Génération aléatoire des symboles</li>
                        <li>Calcul des gains selon les combinaisons</li>
                        <li>Statistiques de jeu</li>
                        <li>Interface utilisateur animée</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 40-55 min</span>
                    <span class="stat-item">📝 ~120 lignes</span>
                    <span class="stat-item">🎯 Random, logique, interface</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Threading;

class MachineASous
{
    static Random random = new Random();
    static string[] symboles = { "🍒", "🍋", "🍊", "🍇", "⭐", "💎", "7️⃣" };
    static int[] multiplicateurs = { 2, 3, 4, 5, 10, 20, 50 };
    
    static void Main()
    {
        int credits = 100;
        int totalMises = 0;
        int totalGains = 0;
        int nombreParties = 0;
        
        Console.WriteLine("🎰 MACHINE À SOUS DELUXE 🎰");
        Console.WriteLine("============================\n");
        Console.WriteLine("Bienvenue ! Vous commencez avec 100 crédits.");
        Console.WriteLine("Mise minimum : 1 crédit, maximum : 10 crédits\n");
        
        AfficherTableGains();
        
        while (credits > 0)
        {
            Console.WriteLine($"\n💰 Crédits disponibles : {credits}");
            Console.Write("Votre mise (0 pour quitter) : ");
            
            if (!int.TryParse(Console.ReadLine(), out int mise))
            {
                Console.WriteLine("❌ Mise invalide !");
                continue;
            }
            
            if (mise == 0)
            {
                Console.WriteLine("Merci d'avoir joué ! 👋");
                break;
            }
            
            if (mise < 1 || mise > 10)
            {
                Console.WriteLine("❌ Mise doit être entre 1 et 10 crédits !");
                continue;
            }
            
            if (mise > credits)
            {
                Console.WriteLine("❌ Crédits insuffisants !");
                continue;
            }
            
            // Déduction de la mise
            credits -= mise;
            totalMises += mise;
            nombreParties++;
            
            // Animation du tirage
            Console.WriteLine("\n🎰 Tirage en cours...");
            AnimationTirage();
            
            // Génération des résultats
            int[] resultats = new int[3];
            for (int i = 0; i < 3; i++)
            {
                resultats[i] = random.Next(symboles.Length);
            }
            
            // Affichage des résultats
            Console.WriteLine("╔═══════════════════════╗");
            Console.WriteLine($"║  {symboles[resultats[0]]}  │  {symboles[resultats[1]]}  │  {symboles[resultats[2]]}  ║");
            Console.WriteLine("╚═══════════════════════╝");
            
            // Calcul des gains
            int gain = CalculerGain(resultats, mise);
            
            if (gain > 0)
            {
                credits += gain;
                totalGains += gain;
                Console.WriteLine($"🎉 GAGNÉ ! +{gain} crédits !");
                
                if (gain >= mise * 10)
                    Console.WriteLine("💎 JACKPOT ! Incroyable ! 💎");
                else if (gain >= mise * 5)
                    Console.WriteLine("⭐ SUPER GAIN ! ⭐");
            }
            else
            {
                Console.WriteLine("😞 Perdu... Tentez votre chance !");
            }
            
            // Affichage des statistiques
            if (nombreParties % 5 == 0)
            {
                AfficherStatistiques(nombreParties, totalMises, totalGains, credits + totalMises - 100);
            }
        }
        
        // Statistiques finales
        Console.WriteLine("\n🎮 PARTIE TERMINÉE 🎮");
        AfficherStatistiques(nombreParties, totalMises, totalGains, credits + totalMises - 100);
        
        if (credits > 100)
            Console.WriteLine("🏆 Félicitations ! Vous repartez avec des gains ! 🏆");
        else if (credits > 50)
            Console.WriteLine("😊 Pas mal ! Vous avez bien résisté ! 😊");
        else
            Console.WriteLine("😅 La chance n'était pas de votre côté aujourd'hui ! 😅");
    }
    
    static void AnimationTirage()
    {
        for (int i = 0; i < 10; i++)
        {
            Console.Write($"\r🎰 {symboles[random.Next(symboles.Length)]} {symboles[random.Next(symboles.Length)]} {symboles[random.Next(symboles.Length)]} 🎰");
            Thread.Sleep(100);
        }
        Console.WriteLine();
    }
    
    static int CalculerGain(int[] resultats, int mise)
    {
        // Trois symboles identiques
        if (resultats[0] == resultats[1] && resultats[1] == resultats[2])
        {
            return mise * multiplicateurs[resultats[0]];
        }
        
        // Deux symboles identiques
        if (resultats[0] == resultats[1] || resultats[1] == resultats[2] || resultats[0] == resultats[2])
        {
            int symboleCommun = resultats[0] == resultats[1] ? resultats[0] : 
                               resultats[1] == resultats[2] ? resultats[1] : resultats[0];
            
            // Gain réduit pour deux symboles
            if (symboleCommun >= 4) // Symboles rares
                return mise * 2;
            else if (symboleCommun >= 2) // Symboles moyens
                return mise;
        }
        
        return 0; // Aucun gain
    }
    
    static void AfficherTableGains()
    {
        Console.WriteLine("📋 TABLE DES GAINS (pour 1 crédit misé)");
        Console.WriteLine("═══════════════════════════════════════");
        for (int i = 0; i < symboles.Length; i++)
        {
            Console.WriteLine($"{symboles[i]} {symboles[i]} {symboles[i]} = x{multiplicateurs[i]}");
        }
        Console.WriteLine("Deux symboles identiques = x1 ou x2");
        Console.WriteLine("═══════════════════════════════════════");
    }
    
    static void AfficherStatistiques(int parties, int mises, int gains, int benefice)
    {
        Console.WriteLine("\n📊 STATISTIQUES");
        Console.WriteLine("═══════════════════════════════");
        Console.WriteLine($"Parties jouées    : {parties}");
        Console.WriteLine($"Total misé        : {mises} crédits");
        Console.WriteLine($"Total gagné       : {gains} crédits");
        Console.WriteLine($"Bénéfice/Perte    : {benefice:+0;-0;0} crédits");
        
        if (mises > 0)
        {
            double tauxRetour = (double)gains / mises * 100;
            Console.WriteLine($"Taux de retour    : {tauxRetour:F1}%");
        }
        
        Console.WriteLine("═══════════════════════════════");
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="advanced-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card advanced">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge advanced">🚀 Avancé</div>
            <h4 class="exercise-title">🏨 Système de Réservation Hôtel</h4>
            <div class="exercise-content">
                <p><strong>Créez un système complet de gestion d'hôtel.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Gestion des chambres (types, prix, disponibilité)</li>
                        <li>Système de réservation avec dates</li>
                        <li>Calcul automatique des tarifs</li>
                        <li>Gestion des clients et historique</li>
                        <li>Rapports et statistiques</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 60-90 min</span>
                    <span class="stat-item">📝 ~200 lignes</span>
                    <span class="stat-item">🎯 Structures, dates, gestion</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Collections.Generic;
using System.Linq;

// Structures de données
struct Chambre
{
    public int Numero;
    public string Type;
    public double PrixParNuit;
    public bool EstDisponible;
    public DateTime DateLiberation;
}

struct Reservation
{
    public int Id;
    public string NomClient;
    public int NumeroChambre;
    public DateTime DateArrivee;
    public DateTime DateDepart;
    public double MontantTotal;
    public bool EstActive;
}

class SystemeHotel
{
    static List<Chambre> chambres = new List<Chambre>();
    static List<Reservation> reservations = new List<Reservation>();
    static int prochainIdReservation = 1;
    
    static void Main()
    {
        InitialiserChambres();
        
        Console.WriteLine("🏨 SYSTÈME DE RÉSERVATION HÔTEL 🏨");
        Console.WriteLine("===================================\n");
        
        bool continuer = true;
        while (continuer)
        {
            AfficherMenu();
            string choix = Console.ReadLine();
            
            switch (choix)
            {
                case "1":
                    AfficherChambres();
                    break;
                case "2":
                    FaireReservation();
                    break;
                case "3":
                    AfficherReservations();
                    break;
                case "4":
                    LibererChambre();
                    break;
                case "5":
                    AfficherStatistiques();
                    break;
                case "6":
                    continuer = false;
                    Console.WriteLine("Au revoir ! 👋");
                    break;
                default:
                    Console.WriteLine("❌ Choix invalide !");
                    break;
            }
            
            if (continuer)
            {
                Console.WriteLine("\nAppuyez sur une touche pour continuer...");
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
    
    static void InitialiserChambres()
    {
        // Chambres simples
        for (int i = 101; i <= 110; i++)
        {
            chambres.Add(new Chambre 
            { 
                Numero = i, 
                Type = "Simple", 
                PrixParNuit = 80, 
                EstDisponible = true,
                DateLiberation = DateTime.Today
            });
        }
        
        // Chambres doubles
        for (int i = 201; i <= 208; i++)
        {
            chambres.Add(new Chambre 
            { 
                Numero = i, 
                Type = "Double", 
                PrixParNuit = 120, 
                EstDisponible = true,
                DateLiberation = DateTime.Today
            });
        }
        
        // Suites
        for (int i = 301; i <= 304; i++)
        {
            chambres.Add(new Chambre 
            { 
                Numero = i, 
                Type = "Suite", 
                PrixParNuit = 200, 
                EstDisponible = true,
                DateLiberation = DateTime.Today
            });
        }
    }
    
    static void AfficherMenu()
    {
        Console.WriteLine("╔══════════════════════════════════╗");
        Console.WriteLine("║           MENU PRINCIPAL         ║");
        Console.WriteLine("╠══════════════════════════════════╣");
        Console.WriteLine("║ 1. Voir les chambres             ║");
        Console.WriteLine("║ 2. Faire une réservation         ║");
        Console.WriteLine("║ 3. Voir les réservations         ║");
        Console.WriteLine("║ 4. Libérer une chambre           ║");
        Console.WriteLine("║ 5. Statistiques                  ║");
        Console.WriteLine("║ 6. Quitter                       ║");
        Console.WriteLine("╚══════════════════════════════════╝");
        Console.Write("\nVotre choix : ");
    }
    
    static void AfficherChambres()
    {
        Console.Clear();
        Console.WriteLine("🏨 ÉTAT DES CHAMBRES");
        Console.WriteLine("═══════════════════════════════════════════════════════");
        Console.WriteLine("Numéro │   Type   │ Prix/nuit │  Statut  │ Libre le");
        Console.WriteLine("───────┼──────────┼───────────┼──────────┼──────────");
        
        var chambresParType = chambres.GroupBy(c => c.Type).OrderBy(g => g.Key);
        
        foreach (var groupe in chambresParType)
        {
            foreach (var chambre in groupe.OrderBy(c => c.Numero))
            {
                string statut = chambre.EstDisponible ? "✅ Libre" : "❌ Occupée";
                string dateLiberation = chambre.EstDisponible ? "Maintenant" : chambre.DateLiberation.ToString("dd/MM/yyyy");
                
                Console.WriteLine($"{chambre.Numero,6} │ {chambre.Type,-8} │ {chambre.PrixParNuit,9:F0}€ │ {statut,-8} │ {dateLiberation}");
            }
        }
        
        // Résumé
        int libres = chambres.Count(c => c.EstDisponible);
        int occupees = chambres.Count - libres;
        double tauxOccupation = (double)occupees / chambres.Count * 100;
        
        Console.WriteLine("═══════════════════════════════════════════════════════");
        Console.WriteLine($"Total : {chambres.Count} chambres | Libres : {libres} | Occupées : {occupees} | Taux : {tauxOccupation:F1}%");
    }
    
    static void FaireReservation()
    {
        Console.Clear();
        Console.WriteLine("📝 NOUVELLE RÉSERVATION");
        Console.WriteLine("========================\n");
        
        Console.Write("Nom du client : ");
        string nomClient = Console.ReadLine();
        
        Console.Write("Date d'arrivée (jj/mm/aaaa) : ");
        if (!DateTime.TryParse(Console.ReadLine(), out DateTime dateArrivee))
        {
            Console.WriteLine("❌ Date invalide !");
            return;
        }
        
        if (dateArrivee < DateTime.Today)
        {
            Console.WriteLine("❌ La date d'arrivée ne peut pas être dans le passé !");
            return;
        }
        
        Console.Write("Date de départ (jj/mm/aaaa) : ");
        if (!DateTime.TryParse(Console.ReadLine(), out DateTime dateDepart))
        {
            Console.WriteLine("❌ Date invalide !");
            return;
        }
        
        if (dateDepart <= dateArrivee)
        {
            Console.WriteLine("❌ La date de départ doit être après la date d'arrivée !");
            return;
        }
        
        // Afficher les chambres disponibles
        var chambresDisponibles = chambres.Where(c => c.EstDisponible || c.DateLiberation <= dateArrivee).ToList();
        
        if (!chambresDisponibles.Any())
        {
            Console.WriteLine("❌ Aucune chambre disponible pour ces dates !");
            return;
        }
        
        Console.WriteLine("\n🏨 Chambres disponibles :");
        Console.WriteLine("Numéro │   Type   │ Prix/nuit │ Total");
        Console.WriteLine("───────┼──────────┼───────────┼──────────");
        
        int nombreNuits = (dateDepart - dateArrivee).Days;
        
        foreach (var chambre in chambresDisponibles.OrderBy(c => c.Type).ThenBy(c => c.Numero))
        {
            double total = chambre.PrixParNuit * nombreNuits;
            Console.WriteLine($"{chambre.Numero,6} │ {chambre.Type,-8} │ {chambre.PrixParNuit,9:F0}€ │ {total,8:F0}€");
        }
        
        Console.Write($"\nChoisissez le numéro de chambre : ");
        if (!int.TryParse(Console.ReadLine(), out int numeroChambre))
        {
            Console.WriteLine("❌ Numéro invalide !");
            return;
        }
        
        var chambreChoisie = chambresDisponibles.FirstOrDefault(c => c.Numero == numeroChambre);
        if (chambreChoisie.Numero == 0)
        {
            Console.WriteLine("❌ Chambre non disponible !");
            return;
        }
        
        // Créer la réservation
        double montantTotal = chambreChoisie.PrixParNuit * nombreNuits;
        
        var reservation = new Reservation
        {
            Id = prochainIdReservation++,
            NomClient = nomClient,
            NumeroChambre = numeroChambre,
            DateArrivee = dateArrivee,
            DateDepart = dateDepart,
            MontantTotal = montantTotal,
            EstActive = true
        };
        
        reservations.Add(reservation);
        
        // Mettre à jour la chambre
        for (int i = 0; i < chambres.Count; i++)
        {
            if (chambres[i].Numero == numeroChambre)
            {
                var chambre = chambres[i];
                chambre.EstDisponible = false;
                chambre.DateLiberation = dateDepart;
                chambres[i] = chambre;
                break;
            }
        }
        
        // Confirmation
        Console.WriteLine("\n✅ RÉSERVATION CONFIRMÉE !");
        Console.WriteLine("═══════════════════════════════════");
        Console.WriteLine($"ID Réservation : {reservation.Id}");
        Console.WriteLine($"Client         : {nomClient}");
        Console.WriteLine($"Chambre        : {numeroChambre} ({chambreChoisie.Type})");
        Console.WriteLine($"Arrivée        : {dateArrivee:dd/MM/yyyy}");
        Console.WriteLine($"Départ         : {dateDepart:dd/MM/yyyy}");
        Console.WriteLine($"Durée          : {nombreNuits} nuit(s)");
        Console.WriteLine($"Prix/nuit      : {chambreChoisie.PrixParNuit:F0}€");
        Console.WriteLine($"TOTAL          : {montantTotal:F0}€");
    }
    
    static void AfficherReservations()
    {
        Console.Clear();
        Console.WriteLine("📋 RÉSERVATIONS ACTIVES");
        Console.WriteLine("═══════════════════════════════════════════════════════════════");
        
        var reservationsActives = reservations.Where(r => r.EstActive).OrderBy(r => r.DateArrivee).ToList();
        
        if (!reservationsActives.Any())
        {
            Console.WriteLine("Aucune réservation active.");
            return;
        }
        
        Console.WriteLine("ID │ Client           │ Chambre │ Arrivée    │ Départ     │ Total");
        Console.WriteLine("───┼──────────────────┼─────────┼────────────┼────────────┼──────────");
        
        foreach (var reservation in reservationsActives)
        {
            Console.WriteLine($"{reservation.Id,2} │ {reservation.NomClient,-16} │ {reservation.NumeroChambre,7} │ {reservation.DateArrivee:dd/MM/yyyy} │ {reservation.DateDepart:dd/MM/yyyy} │ {reservation.MontantTotal,8:F0}€");
        }
        
        double chiffreAffaires = reservationsActives.Sum(r => r.MontantTotal);
        Console.WriteLine("═══════════════════════════════════════════════════════════════");
        Console.WriteLine($"Total : {reservationsActives.Count} réservations | CA : {chiffreAffaires:F0}€");
    }
    
    static void LibererChambre()
    {
        Console.Clear();
        Console.WriteLine("🔓 LIBÉRATION DE CHAMBRE");
        Console.WriteLine("=========================\n");
        
        var reservationsActives = reservations.Where(r => r.EstActive).ToList();
        
        if (!reservationsActives.Any())
        {
            Console.WriteLine("Aucune réservation active à libérer.");
            return;
        }
        
        Console.WriteLine("Réservations actives :");
        foreach (var reservation in reservationsActives)
        {
            Console.WriteLine($"ID {reservation.Id} - {reservation.NomClient} - Chambre {reservation.NumeroChambre} - Départ {reservation.DateDepart:dd/MM/yyyy}");
        }
        
        Console.Write("\nID de la réservation à libérer : ");
        if (!int.TryParse(Console.ReadLine(), out int idReservation))
        {
            Console.WriteLine("❌ ID invalide !");
            return;
        }
        
        var reservationIndex = reservations.FindIndex(r => r.Id == idReservation && r.EstActive);
        if (reservationIndex == -1)
        {
            Console.WriteLine("❌ Réservation non trouvée !");
            return;
        }
        
        var reservation = reservations[reservationIndex];
        
        // Marquer la réservation comme inactive
        reservation.EstActive = false;
        reservations[reservationIndex] = reservation;
        
        // Libérer la chambre
        for (int i = 0; i < chambres.Count; i++)
        {
            if (chambres[i].Numero == reservation.NumeroChambre)
            {
                var chambre = chambres[i];
                chambre.EstDisponible = true;
                chambre.DateLiberation = DateTime.Today;
                chambres[i] = chambre;
                break;
            }
        }
        
        Console.WriteLine($"✅ Chambre {reservation.NumeroChambre} libérée avec succès !");
        Console.WriteLine($"Client {reservation.NomClient} - Montant : {reservation.MontantTotal:F0}€");
    }
    
    static void AfficherStatistiques()
    {
        Console.Clear();
        Console.WriteLine("📊 STATISTIQUES DE L'HÔTEL");
        Console.WriteLine("═══════════════════════════════════════");
        
        // Statistiques des chambres
        var statsChambres = chambres.GroupBy(c => c.Type)
                                   .Select(g => new { 
                                       Type = g.Key, 
                                       Total = g.Count(), 
                                       Libres = g.Count(c => c.EstDisponible),
                                       Occupees = g.Count(c => !c.EstDisponible)
                                   }).ToList();
        
        Console.WriteLine("CHAMBRES PAR TYPE :");
        foreach (var stat in statsChambres)
        {
            double taux = (double)stat.Occupees / stat.Total * 100;
            Console.WriteLine($"{stat.Type,-8} : {stat.Total} total | {stat.Libres} libres | {stat.Occupees} occupées ({taux:F1}%)");
        }
        
        // Statistiques des réservations
        var reservationsActives = reservations.Where(r => r.EstActive).ToList();
        var reservationsPassees = reservations.Where(r => !r.EstActive).ToList();
        
        Console.WriteLine("\nRÉSERVATIONS :");
        Console.WriteLine($"Actives        : {reservationsActives.Count}");
        Console.WriteLine($"Terminées      : {reservationsPassees.Count}");
        Console.WriteLine($"Total          : {reservations.Count}");
        
        // Chiffre d'affaires
        double caActuel = reservationsActives.Sum(r => r.MontantTotal);
        double caTotal = reservations.Sum(r => r.MontantTotal);
        
        Console.WriteLine("\nCHIFFRE D'AFFAIRES :");
        Console.WriteLine($"En cours       : {caActuel:F0}€");
        Console.WriteLine($"Total          : {caTotal:F0}€");
        
        if (reservations.Any())
        {
            double panieMoyen = caTotal / reservations.Count;
            Console.WriteLine($"Panier moyen   : {panieMoyen:F0}€");
        }
        
        // Prochaines arrivées
        var prochainesArrivees = reservationsActives
            .Where(r => r.DateArrivee >= DateTime.Today)
            .OrderBy(r => r.DateArrivee)
            .Take(5)
            .ToList();
        
        if (prochainesArrivees.Any())
        {
            Console.WriteLine("\nPROCHAINES ARRIVÉES :");
            foreach (var reservation in prochainesArrivees)
            {
                Console.WriteLine($"{reservation.DateArrivee:dd/MM} - {reservation.NomClient} - Ch.{reservation.NumeroChambre}");
            }
        }
    }
}</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="expert-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">👑 Expert</div>
            <h4 class="exercise-title">🎮 Jeu du Pendu Avancé</h4>
            <div class="exercise-content">
                <p><strong>Développez un jeu du pendu avec interface graphique ASCII.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Interface graphique ASCII animée</li>
                        <li>Système de catégories et niveaux</li>
                        <li>Gestion des scores et records</li>
                        <li>Indices et aide contextuelle</li>
                        <li>Sauvegarde des parties</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 90-120 min</span>
                    <span class="stat-item">📝 ~300 lignes</span>
                    <span class="stat-item">🎯 Interface, logique, sauvegarde</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

class JeuPendu
{
    static Dictionary<string, string[]> categories = new Dictionary<string, string[]>
    {
        ["Animaux"] = new[] { "ELEPHANT", "GIRAFE", "CROCODILE", "PAPILLON", "HIPPOPOTAME" },
        ["Pays"] = new[] { "FRANCE", "JAPON", "BRESIL", "AUSTRALIE", "NORVEGE" },
        ["Métiers"] = new[] { "PROGRAMMEUR", "MEDECIN", "ARCHITECTE", "CUISINIER", "POMPIER" },
        ["Sports"] = new[] { "FOOTBALL", "BASKETBALL", "NATATION", "ESCALADE", "CYCLISME" }
    };
    
    static string[] pendu = {
        "   ╔═══╗\n   ║   ║\n       ║\n       ║\n       ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n       ║\n       ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n   │   ║\n       ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n  ┌│   ║\n       ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n  ┌│┐  ║\n       ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n  ┌│┐  ║\n  ┌    ║\n   ════╩════",
        "   ╔═══╗\n   ║   ║\n   😵   ║\n  ┌│┐  ║\n  ┌ ┐  ║\n   ════╩════"
    };
    
    static void Main()
    {
        int score = 0;
        int parties = 0;
        
        Console.WriteLine("🎮 JEU DU PENDU AVANCÉ 🎮");
        Console.WriteLine("==========================\n");
        
        bool continuer = true;
        while (continuer)
        {
            AfficherMenuPrincipal();
            string choix = Console.ReadLine();
            
            switch (choix)
            {
                case "1":
                    var resultat = JouerPartie();
                    parties++;
                    if (resultat.gagne) score += resultat.points;
                    AfficherResultat(resultat, score, parties);
                    break;
                case "2":
                    AfficherRegles();
                    break;
                case "3":
                    AfficherStatistiques(score, parties);
                    break;
                case "4":
                    continuer = false;
                    Console.WriteLine("Merci d'avoir joué ! 🎮");
                    break;
                default:
                    Console.WriteLine("❌ Choix invalide !");
                    break;
            }
            
            if (continuer)
            {
                Console.WriteLine("\nAppuyez sur une touche pour continuer...");
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
    
    static void AfficherMenuPrincipal()
    {
        Console.WriteLine("╔══════════════════════════════════╗");
        Console.WriteLine("║           MENU PRINCIPAL         ║");
        Console.WriteLine("╠══════════════════════════════════╣");
        Console.WriteLine("║ 1. 🎯 Jouer une partie           ║");
        Console.WriteLine("║ 2. 📖 Règles du jeu              ║");
        Console.WriteLine("║ 3. 📊 Statistiques               ║");
        Console.WriteLine("║ 4. 🚪 Quitter                    ║");
        Console.WriteLine("╚══════════════════════════════════╝");
        Console.Write("\nVotre choix : ");
    }
    
    static (bool gagne, int points, string mot) JouerPartie()
    {
        Console.Clear();
        
        // Choix de la catégorie
        Console.WriteLine("🎯 NOUVELLE PARTIE");
        Console.WriteLine("==================\n");
        Console.WriteLine("Choisissez une catégorie :");
        
        var categoriesListe = categories.Keys.ToList();
        for (int i = 0; i < categoriesListe.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {categoriesListe[i]}");
        }
        
        Console.Write("\nCatégorie (1-" + categoriesListe.Count + ") : ");
        if (!int.TryParse(Console.ReadLine(), out int choixCategorie) || 
            choixCategorie < 1 || choixCategorie > categoriesListe.Count)
        {
            Console.WriteLine("❌ Choix invalide ! Catégorie aléatoire.");
            choixCategorie = new Random().Next(1, categoriesListe.Count + 1);
        }
        
        string categorieChoisie = categoriesListe[choixCategorie - 1];
        string[] mots = categories[categorieChoisie];
        string motSecret = mots[new Random().Next(mots.Length)];
        
        // Initialisation du jeu
        char[] motAffiche = new string('_', motSecret.Length).ToCharArray();
        List<char> lettresEssayees = new List<char>();
        int erreurs = 0;
        int maxErreurs = pendu.Length - 1;
        bool gagne = false;
        int indices = 2; // Nombre d'indices disponibles
        
        while (erreurs < maxErreurs && !gagne)
        {
            Console.Clear();
            AfficherEtatJeu(categorieChoisie, motAffiche, lettresEssayees, erreurs, indices);
            
            Console.Write("\nVotre choix (lettre/INDICE/SOLUTION) : ");
            string saisie = Console.ReadLine().ToUpper();
            
            if (saisie == "INDICE" && indices > 0)
            {
                DonnerIndice(motSecret, motAffiche, ref indices);
                continue;
            }
            
            if (saisie == "SOLUTION")
            {
                Console.Write("Tapez le mot complet : ");
                string tentative = Console.ReadLine().ToUpper();
                if (tentative == motSecret)
                {
                    gagne = true;
                    for (int i = 0; i < motSecret.Length; i++)
                        motAffiche[i] = motSecret[i];
                }
                else
                {
                    erreurs += 2; // Pénalité pour mauvaise solution
                    Console.WriteLine("❌ Mauvaise réponse ! -2 erreurs");
                    Console.ReadKey();
                }
                continue;
            }
            
            if (saisie.Length != 1 || !char.IsLetter(saisie[0]))
            {
                Console.WriteLine("❌ Veuillez saisir une seule lettre !");
                Console.ReadKey();
                continue;
            }
            
            char lettre = saisie[0];
            
            if (lettresEssayees.Contains(lettre))
            {
                Console.WriteLine("❌ Lettre déjà essayée !");
                Console.ReadKey();
                continue;
            }
            
            lettresEssayees.Add(lettre);
            
            if (motSecret.Contains(lettre))
            {
                for (int i = 0; i < motSecret.Length; i++)
                {
                    if (motSecret[i] == lettre)
                        motAffiche[i] = lettre;
                }
                
                Console.WriteLine("✅ Bonne lettre !");
                
                if (!motAffiche.Contains('_'))
                    gagne = true;
            }
            else
            {
                erreurs++;
                Console.WriteLine("❌ Lettre incorrecte !");
            }
            
            if (!gagne && erreurs < maxErreurs)
            {
                Console.ReadKey();
            }
        }
        
        // Calcul des points
        int points = 0;
        if (gagne)
        {
            points = (maxErreurs - erreurs) * 10 + motSecret.Length * 5;
            if (erreurs == 0) points *= 2; // Bonus sans erreur
        }
        
        return (gagne, points, motSecret);
    }
    
    static void AfficherEtatJeu(string categorie, char[] motAffiche, List<char> lettresEssayees, int erreurs, int indices)
    {
        Console.WriteLine("🎮 JEU DU PENDU 🎮");
        Console.WriteLine("==================\n");
        
        // Affichage du pendu
        Console.WriteLine(pendu[erreurs]);
        Console.WriteLine();
        
        // Informations de la partie
        Console.WriteLine($"📂 Catégorie : {categorie}");
        Console.WriteLine($"💡 Indices restants : {indices}");
        Console.WriteLine($"❌ Erreurs : {erreurs}/{pendu.Length - 1}");
        Console.WriteLine();
        
        // Mot à deviner
        Console.WriteLine("🔤 Mot à deviner :");
        Console.WriteLine("   " + string.Join(" ", motAffiche));
        Console.WriteLine();
        
        // Lettres essayées
        if (lettresEssayees.Any())
        {
            var bonnesLettres = lettresEssayees.Where(l => motAffiche.Contains(l)).ToList();
            var mauvaisesLettres = lettresEssayees.Where(l => !motAffiche.Contains(l)).ToList();
            
            if (bonnesLettres.Any())
                Console.WriteLine($"✅ Bonnes lettres : {string.Join(", ", bonnesLettres)}");
            
            if (mauvaisesLettres.Any())
                Console.WriteLine($"❌ Mauvaises lettres : {string.Join(", ", mauvaisesLettres)}");
        }
    }
    
    static void DonnerIndice(string motSecret, char[] motAffiche, ref int indices)
    {
        var lettresNonTrouvees = motSecret.Where((c, i) => motAffiche[i] == '_').Distinct().ToList();
        
        if (lettresNonTrouvees.Any())
        {
            char lettreIndice = lettresNonTrouvees[new Random().Next(lettresNonTrouvees.Count)];
            
            for (int i = 0; i < motSecret.Length; i++)
            {
                if (motSecret[i] == lettreIndice)
                    motAffiche[i] = lettreIndice;
            }
            
            indices--;
            Console.WriteLine($"💡 Indice : La lettre '{lettreIndice}' est dans le mot !");
        }
        else
        {
            Console.WriteLine("💡 Vous avez déjà trouvé toutes les lettres !");
        }
        
        Console.ReadKey();
    }
    
    static void AfficherResultat((bool gagne, int points, string mot) resultat, int scoreTotal, int parties)
    {
        Console.Clear();
        
        if (resultat.gagne)
        {
            Console.WriteLine("🎉 FÉLICITATIONS ! 🎉");
            Console.WriteLine("======================");
            Console.WriteLine("Vous avez gagné !");
        }
        else
        {
            Console.WriteLine("💀 GAME OVER 💀");
            Console.WriteLine("================");
            Console.WriteLine("Vous avez perdu...");
        }
        
        Console.WriteLine($"\n🔤 Le mot était : {resultat.mot}");
        Console.WriteLine($"🏆 Points gagnés : {resultat.points}");
        Console.WriteLine($"📊 Score total : {scoreTotal}");
        Console.WriteLine($"🎮 Parties jouées : {parties}");
        
        if (parties > 0)
        {
            double moyenne = (double)scoreTotal / parties;
            Console.WriteLine($"📈 Moyenne : {moyenne:F1} points/partie");
        }
    }
    
    static void AfficherRegles()
    {
        Console.Clear();
        Console.WriteLine("📖 RÈGLES DU JEU");
        Console.WriteLine("=================\n");
        Console.WriteLine("🎯 OBJECTIF :");
        Console.WriteLine("   Devinez le mot secret lettre par lettre avant que le pendu soit complet !\n");
        Console.WriteLine("🎮 COMMENT JOUER :");
        Console.WriteLine("   • Choisissez une catégorie");
        Console.WriteLine("   • Proposez des lettres une par une");
        Console.WriteLine("   • Utilisez 'INDICE' pour révéler une lettre (2 disponibles)");
        Console.WriteLine("   • Tapez 'SOLUTION' pour tenter le mot complet\n");
        Console.WriteLine("🏆 SYSTÈME DE POINTS :");
        Console.WriteLine("   • Points de base : (erreurs évitées × 10) + (longueur mot × 5)");
        Console.WriteLine("   • Bonus sans erreur : points × 2");
        Console.WriteLine("   • Pénalité mauvaise solution : +2 erreurs\n");
        Console.WriteLine("⚠️  ATTENTION :");
        Console.WriteLine("   • 6 erreurs maximum avant la défaite");
        Console.WriteLine("   • Les indices réduisent le score potentiel");
    }
    
    static void AfficherStatistiques(int score, int parties)
    {
        Console.Clear();
        Console.WriteLine("📊 VOS STATISTIQUES");
        Console.WriteLine("===================\n");
        Console.WriteLine($"🎮 Parties jouées     : {parties}");
        Console.WriteLine($"🏆 Score total        : {score} points");
        
        if (parties > 0)
        {
            double moyenne = (double)score / parties;
            Console.WriteLine($"📈 Score moyen        : {moyenne:F1} points");
            
            string niveau;
            if (moyenne >= 100) niveau = "🏆 MAÎTRE DU PENDU";
            else if (moyenne >= 75) niveau = "🥇 EXPERT";
            else if (moyenne >= 50) niveau = "🥈 CONFIRMÉ";
            else if (moyenne >= 25) niveau = "🥉 DÉBUTANT";
            else niveau = "📚 APPRENTI";
            
            Console.WriteLine($"🎖️  Niveau           : {niveau}");
        }
        
        Console.WriteLine($"\n📂 Catégories disponibles : {categories.Count}");
        Console.WriteLine($"🔤 Mots total         : {categories.Values.Sum(mots => mots.Length)}");
    }
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">👑 Expert</div>
            <h4 class="exercise-title">🧮 Calculatrice Scientifique</h4>
            <div class="exercise-content">
                <p><strong>Créez une calculatrice scientifique complète avec historique.</strong></p>
                
                <div class="features-list">
                    <h5>📋 Fonctionnalités à implémenter :</h5>
                    <ul>
                        <li>Opérations de base et scientifiques</li>
                        <li>Gestion des parenthèses et priorités</li>
                        <li>Fonctions trigonométriques</li>
                        <li>Historique des calculs</li>
                        <li>Variables et constantes</li>
                    </ul>
                </div>
                
                <div class="project-stats">
                    <span class="stat-item">⏱️ 120-150 min</span>
                    <span class="stat-item">📝 ~400 lignes</span>
                    <span class="stat-item">🎯 Parsing, math, interface</span>
                </div>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">💡</span> Voir la solution complète
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>// Solution complète disponible sur demande
// Ce projet nécessite une implémentation avancée
// avec parsing d'expressions mathématiques
Console.WriteLine("🧮 Projet Expert - Calculatrice Scientifique");
Console.WriteLine("Implémentation complète disponible dans le cours avancé !");</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

</div>

<script>
// Gestion de l'affichage des sections
function showSection(sectionId) {
    // Masquer toutes les sections
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    
    // Afficher la section sélectionnée
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.style.display = 'block';
    }
    
    // Mettre à jour les boutons de navigation
    const buttons = document.querySelectorAll('.nav-button');
    buttons.forEach(button => {
        button.classList.remove('active');
    });
    
    // Activer le bouton correspondant
    const activeButton = document.querySelector(`[onclick="showSection('${sectionId}')"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

// Gestion de l'affichage des solutions
function toggleSolution(button) {
    const card = button.closest('.exercise-card');
    const solutionWrapper = card.querySelector('.solution-wrapper');
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.style.display === 'block') {
        solutionWrapper.style.display = 'none';
        button.innerHTML = '<span class="arrow">💡</span> Voir la solution complète';
        arrow.style.transform = 'rotate(0deg)';
    } else {
        solutionWrapper.style.display = 'block';
        button.innerHTML = '<span class="arrow">💡</span> Masquer la solution';
        arrow.style.transform = 'rotate(180deg)';
    }
}

// Initialisation : afficher la section débutant par défaut
document.addEventListener('DOMContentLoaded', function() {
    showSection('beginner-section');
});

// Animation des cartes au survol
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.exercise-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Effet de parallaxe sur le header
window.addEventListener('scroll', function() {
    const header = document.querySelector('.header');
    const scrolled = window.pageYOffset;
    const parallax = scrolled * 0.5;
    
    if (header) {
        header.style.transform = `translateY(${parallax}px)`;
    }
});

// Compteur de projets complétés (simulation)
let projetsCompletes = 0;

function marquerProjetComplete(button) {
    projetsCompletes++;
    button.innerHTML = '✅ Projet terminé !';
    button.style.backgroundColor = '#4CAF50';
    button.disabled = true;
    
    // Afficher un message de félicitations
    const message = document.createElement('div');
    message.innerHTML = `🎉 Félicitations ! Vous avez terminé ${projetsCompletes} projet(s) !`;
    message.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: slideIn 0.5s ease-out;
    `;
    
    document.body.appendChild(message);
    
    // Supprimer le message après 3 secondes
    setTimeout(() => {
        message.remove();
    }, 3000);
}

// Animation CSS pour les notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);
</script>