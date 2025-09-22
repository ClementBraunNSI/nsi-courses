# 🚀 B2.6 - Projets d'Applications C#

<style>
.concept-card {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(255, 193, 7, 0.05));
    border: 1px solid rgba(255, 152, 0, 0.2);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.1);
    transition: all 0.3s ease;
}

.concept-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(255, 152, 0, 0.15);
}

.concept-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    display: block;
}

.concept-name {
    font-size: 1.3rem;
    font-weight: 700;
    color: #ff6f00;
    margin-bottom: 0.8rem;
}

.concept-description {
    color: #2c3e50;
    line-height: 1.6;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.1));
    border-left: 4px solid #ff9800;
    padding: 1rem 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0 10px 10px 0;
    box-shadow: 0 2px 10px rgba(255, 152, 0, 0.1);
}

.code-example {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-family: 'Courier New', monospace;
}

.exercise-box {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(255, 193, 7, 0.05));
    border: 1px solid rgba(255, 152, 0, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.project-box {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.15), rgba(255, 193, 7, 0.1));
    border: 2px solid rgba(255, 152, 0, 0.4);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 6px 20px rgba(255, 152, 0, 0.15);
}

.custom-h3 {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.9), rgba(255, 193, 7, 0.8));
    color: white;
    padding: 1.2rem 2rem;
    border-radius: 15px;
    margin: 2.5rem 0 1.5rem 0;
    font-size: 1.4rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    box-shadow: 0 8px 20px rgba(255, 152, 0, 0.3);
    border: 1px solid rgba(255, 152, 0, 0.3);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.custom-h3:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(255, 152, 0, 0.4);
}

.custom-h4 {
    background: rgba(255, 152, 0, 0.1);
    color: #2c3e50;
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    border-left: 4px solid #ff9800;
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.1);
    transition: all 0.3s ease;
}

.custom-h4:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(255, 152, 0, 0.2);
    background: rgba(255, 152, 0, 0.15);
}
</style>

## 📋 Objectifs du cours

À la fin de ce cours, vous serez capable de :
- ✅ Concevoir une application avec UML
- ✅ Structurer un projet C# professionnel
- ✅ Implémenter des applications complètes
- ✅ Appliquer les bonnes pratiques de développement
- ✅ Gérer les erreurs et la validation
- ✅ Créer des interfaces utilisateur simples

---

<h3 class="custom-h3">📐 Introduction à UML</h3>

<div class="concept-card">
<span class="concept-icon">📊</span>
<div class="concept-name">Unified Modeling Language (UML)</div>
<div class="concept-description">
UML est un langage de modélisation graphique qui permet de concevoir et documenter des systèmes logiciels. Il aide à visualiser la structure et le comportement d'une application avant de la développer.
</div>
</div>

<div class="highlight-fact">
<strong>🎯 Diagrammes UML essentiels :</strong>
<ul>
<li><strong>Diagramme de classes :</strong> Structure des classes et leurs relations</li>
<li><strong>Diagramme de cas d'usage :</strong> Fonctionnalités du système</li>
<li><strong>Diagramme de séquence :</strong> Interactions entre objets</li>
<li><strong>Diagramme d'activité :</strong> Flux de travail et processus</li>
</ul>
</div>

<h4 class="custom-h4">📊 Diagramme de classes</h4>

<div class="uml-diagram">
<strong>Exemple : Système de gestion de bibliothèque</strong><br><br>

```
┌─────────────────────────┐
│       Document          │
├─────────────────────────┤
│ - titre: string         │
│ - auteur: string        │
│ - anneePublication: int │
│ - estEmprunte: bool     │
├─────────────────────────┤
│ + Emprunter(): bool     │
│ + Retourner(): void     │
│ + AfficherInfos(): void │
└─────────────────────────┘
            △
            │
    ┌───────┴───────┐
    │               │
┌───▽───────┐   ┌───▽──────┐
│   Livre    │   │ Magazine │
├────────────┤   ├──────────┤
│ - isbn     │   │ - numero │
│ - pages    │   │ - period │
├────────────┤   ├──────────┤
│ + Lire()   │   │ + Lire() │
└────────────┘   └──────────┘

┌─────────────────────────┐
│      Utilisateur        │
├─────────────────────────┤
│ - nom: string           │
│ - email: string         │
│ - documentsEmpruntes    │
├─────────────────────────┤
│ + EmprunterDocument()   │
│ + RetournerDocument()   │
└─────────────────────────┘
            │
            │ 1..*
            ▽
┌─────────────────────────┐
│        Emprunt          │
├─────────────────────────┤
│ - dateEmprunt: DateTime │
│ - dateRetour: DateTime  │
│ - document: Document    │
├─────────────────────────┤
│ + CalculerRetard(): int │
│ + CalculerAmende(): dec │
└─────────────────────────┘
```
</div>

---

<h3 class="custom-h3">🎯 Projet 1 : Gestionnaire de Tâches</h3>

<div class="project-box">
<h4>📝 Description du projet</h4>
Créer une application console pour gérer des tâches personnelles avec :
- Création, modification, suppression de tâches
- Catégorisation et priorités
- Suivi des échéances
- Sauvegarde en fichier JSON
</div>

<h4 class="custom-h4">📐 Conception UML</h4>

<div class="uml-diagram">
<strong>Diagramme de classes - Gestionnaire de Tâches</strong><br><br>

```
┌─────────────────────────┐
│        Tache            │
├─────────────────────────┤
│ - id: int               │
│ - titre: string         │
│ - description: string   │
│ - dateCreation: DateTime│
│ - dateEcheance: DateTime│
│ - estTerminee: bool     │
│ - priorite: Priorite    │
│ - categorie: Categorie  │
├─────────────────────────┤
│ + Terminer(): void      │
│ + ModifierTitre(): void │
│ + EstEnRetard(): bool   │
│ + AfficherDetails(): void│
└─────────────────────────┘
            │
            │ *
            ▽
┌─────────────────────────┐
│   GestionnaireTaches    │
├─────────────────────────┤
│ - taches: List<Tache>   │
│ - prochainId: int       │
├─────────────────────────┤
│ + AjouterTache(): void  │
│ + SupprimerTache(): bool│
│ + ListerTaches(): void  │
│ + FiltrerParCategorie() │
│ + SauvegarderFichier()  │
│ + ChargerFichier(): void│
└─────────────────────────┘

┌─────────────────┐    ┌─────────────────┐
│    Priorite     │    │   Categorie     │
├─────────────────┤    ├─────────────────┤
│ + Basse         │    │ + Travail       │
│ + Normale       │    │ + Personnel     │
│ + Haute         │    │ + Urgent        │
│ + Critique      │    │ + Loisir        │
└─────────────────┘    └─────────────────┘
```
</div>

<h4 class="custom-h4">💻 Implémentation</h4>

<div class="code-example">
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;

// Énumérations
public enum Priorite
{
    Basse = 1,
    Normale = 2,
    Haute = 3,
    Critique = 4
}

public enum Categorie
{
    Travail,
    Personnel,
    Urgent,
    Loisir,
    Etudes,
    Sante
}

// Classe Tache
public class Tache
{
    public int Id { get; set; }
    public string Titre { get; set; }
    public string Description { get; set; }
    public DateTime DateCreation { get; set; }
    public DateTime? DateEcheance { get; set; }
    public bool EstTerminee { get; set; }
    public Priorite Priorite { get; set; }
    public Categorie Categorie { get; set; }
    
    public Tache()
    {
        DateCreation = DateTime.Now;
        EstTerminee = false;
        Priorite = Priorite.Normale;
    }
    
    public Tache(string titre, string description, Categorie categorie, Priorite priorite = Priorite.Normale)
    {
        Titre = titre;
        Description = description;
        Categorie = categorie;
        Priorite = priorite;
        DateCreation = DateTime.Now;
        EstTerminee = false;
    }
    
    public void Terminer()
    {
        EstTerminee = true;
        Console.WriteLine($"✅ Tâche '{Titre}' marquée comme terminée !");
    }
    
    public void ModifierTitre(string nouveauTitre)
    {
        string ancienTitre = Titre;
        Titre = nouveauTitre;
        Console.WriteLine($"📝 Titre modifié : '{ancienTitre}' → '{nouveauTitre}'");
    }
    
    public bool EstEnRetard()
    {
        return DateEcheance.HasValue && 
               DateTime.Now > DateEcheance.Value && 
               !EstTerminee;
    }
    
    public void AfficherDetails()
    {
        Console.WriteLine($"\n📋 Tâche #{Id}");
        Console.WriteLine($"   Titre : {Titre}");
        Console.WriteLine($"   Description : {Description}");
        Console.WriteLine($"   Catégorie : {Categorie}");
        Console.WriteLine($"   Priorité : {Priorite}");
        Console.WriteLine($"   Créée le : {DateCreation:dd/MM/yyyy HH:mm}");
        
        if (DateEcheance.HasValue)
        {
            Console.WriteLine($"   Échéance : {DateEcheance:dd/MM/yyyy HH:mm}");
            if (EstEnRetard())
                Console.WriteLine("   ⚠️  EN RETARD !");
        }
        
        Console.WriteLine($"   Statut : {(EstTerminee ? "✅ Terminée" : "⏳ En cours")}");
    }
    
    public string ObtenirIconePriorite()
    {
        return Priorite switch
        {
            Priorite.Basse => "🟢",
            Priorite.Normale => "🟡",
            Priorite.Haute => "🟠",
            Priorite.Critique => "🔴",
            _ => "⚪"
        };
    }
}

// Classe GestionnaireTaches
public class GestionnaireTaches
{
    private List<Tache> taches;
    private int prochainId;
    private const string FICHIER_SAUVEGARDE = "taches.json";
    
    public GestionnaireTaches()
    {
        taches = new List<Tache>();
        prochainId = 1;
        ChargerFichier();
    }
    
    public void AjouterTache(string titre, string description, Categorie categorie, 
                           Priorite priorite = Priorite.Normale, DateTime? echeance = null)
    {
        if (string.IsNullOrWhiteSpace(titre))
        {
            Console.WriteLine("❌ Le titre ne peut pas être vide !");
            return;
        }
        
        var nouvelleTache = new Tache(titre, description, categorie, priorite)
        {
            Id = prochainId++,
            DateEcheance = echeance
        };
        
        taches.Add(nouvelleTache);
        Console.WriteLine($"✅ Tâche '{titre}' ajoutée avec succès !");
        SauvegarderFichier();
    }
    
    public bool SupprimerTache(int id)
    {
        var tache = taches.FirstOrDefault(t => t.Id == id);
        if (tache == null)
        {
            Console.WriteLine($"❌ Aucune tâche trouvée avec l'ID {id}");
            return false;
        }
        
        taches.Remove(tache);
        Console.WriteLine($"🗑️  Tâche '{tache.Titre}' supprimée");
        SauvegarderFichier();
        return true;
    }
    
    public void ListerTaches(bool afficherTerminees = true)
    {
        var tachesAfficher = afficherTerminees ? 
            taches : taches.Where(t => !t.EstTerminee).ToList();
        
        if (!tachesAfficher.Any())
        {
            Console.WriteLine("📭 Aucune tâche à afficher");
            return;
        }
        
        Console.WriteLine("\n📋 LISTE DES TÂCHES");
        Console.WriteLine("==================");
        
        foreach (var tache in tachesAfficher.OrderBy(t => t.EstTerminee)
                                           .ThenByDescending(t => t.Priorite)
                                           .ThenBy(t => t.DateEcheance))
        {
            string statut = tache.EstTerminee ? "✅" : "⏳";
            string retard = tache.EstEnRetard() ? " ⚠️" : "";
            string echeance = tache.DateEcheance?.ToString("dd/MM") ?? "Sans échéance";
            
            Console.WriteLine($"{statut} #{tache.Id:D2} {tache.ObtenirIconePriorite()} " +
                            $"{tache.Titre} ({tache.Categorie}) - {echeance}{retard}");
        }
    }
    
    public void FiltrerParCategorie(Categorie categorie)
    {
        var tachesFiltrees = taches.Where(t => t.Categorie == categorie).ToList();
        
        Console.WriteLine($"\n📂 Tâches de la catégorie : {categorie}");
        Console.WriteLine("=====================================");
        
        if (!tachesFiltrees.Any())
        {
            Console.WriteLine("📭 Aucune tâche dans cette catégorie");
            return;
        }
        
        foreach (var tache in tachesFiltrees)
        {
            tache.AfficherDetails();
        }
    }
    
    public void AfficherStatistiques()
    {
        int total = taches.Count;
        int terminees = taches.Count(t => t.EstTerminee);
        int enRetard = taches.Count(t => t.EstEnRetard());
        int critiques = taches.Count(t => t.Priorite == Priorite.Critique && !t.EstTerminee);
        
        Console.WriteLine("\n📊 STATISTIQUES");
        Console.WriteLine("================");
        Console.WriteLine($"Total des tâches : {total}");
        Console.WriteLine($"Terminées : {terminees} ({(total > 0 ? (terminees * 100.0 / total):0):F1}%)");
        Console.WriteLine($"En retard : {enRetard}");
        Console.WriteLine($"Critiques en cours : {critiques}");
        
        if (total > 0)
        {
            var categorieStats = taches.GroupBy(t => t.Categorie)
                                      .Select(g => new { Categorie = g.Key, Count = g.Count() })
                                      .OrderByDescending(x => x.Count);
            
            Console.WriteLine("\nRépartition par catégorie :");
            foreach (var stat in categorieStats)
            {
                Console.WriteLine($"  {stat.Categorie} : {stat.Count}");
            }
        }
    }
    
    public Tache ObtenirTache(int id)
    {
        return taches.FirstOrDefault(t => t.Id == id);
    }
    
    public void SauvegarderFichier()
    {
        try
        {
            var json = JsonConvert.SerializeObject(taches, Formatting.Indented);
            File.WriteAllText(FICHIER_SAUVEGARDE, json);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Erreur lors de la sauvegarde : {ex.Message}");
        }
    }
    
    public void ChargerFichier()
    {
        try
        {
            if (File.Exists(FICHIER_SAUVEGARDE))
            {
                var json = File.ReadAllText(FICHIER_SAUVEGARDE);
                taches = JsonConvert.DeserializeObject<List<Tache>>(json) ?? new List<Tache>();
                
                if (taches.Any())
                {
                    prochainId = taches.Max(t => t.Id) + 1;
                    Console.WriteLine($"📂 {taches.Count} tâche(s) chargée(s) depuis le fichier");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Erreur lors du chargement : {ex.Message}");
            taches = new List<Tache>();
        }
    }
}

// Interface utilisateur console
public class InterfaceConsole
{
    private GestionnaireTaches gestionnaire;
    
    public InterfaceConsole()
    {
        gestionnaire = new GestionnaireTaches();
    }
    
    public void Demarrer()
    {
        Console.WriteLine("🎯 GESTIONNAIRE DE TÂCHES");
        Console.WriteLine("=========================");
        
        bool continuer = true;
        while (continuer)
        {
            AfficherMenu();
            string choix = Console.ReadLine();
            
            switch (choix)
            {
                case "1":
                    AjouterNouvelleTache();
                    break;
                case "2":
                    gestionnaire.ListerTaches();
                    break;
                case "3":
                    TerminerTache();
                    break;
                case "4":
                    SupprimerTache();
                    break;
                case "5":
                    FiltrerParCategorie();
                    break;
                case "6":
                    gestionnaire.AfficherStatistiques();
                    break;
                case "7":
                    AfficherDetailsTache();
                    break;
                case "0":
                    continuer = false;
                    Console.WriteLine("👋 Au revoir !");
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
    
    private void AfficherMenu()
    {
        Console.WriteLine("\n📋 MENU PRINCIPAL");
        Console.WriteLine("==================");
        Console.WriteLine("1. ➕ Ajouter une tâche");
        Console.WriteLine("2. 📋 Lister les tâches");
        Console.WriteLine("3. ✅ Terminer une tâche");
        Console.WriteLine("4. 🗑️  Supprimer une tâche");
        Console.WriteLine("5. 📂 Filtrer par catégorie");
        Console.WriteLine("6. 📊 Afficher les statistiques");
        Console.WriteLine("7. 🔍 Détails d'une tâche");
        Console.WriteLine("0. 🚪 Quitter");
        Console.Write("\nVotre choix : ");
    }
    
    private void AjouterNouvelleTache()
    {
        Console.WriteLine("\n➕ AJOUTER UNE NOUVELLE TÂCHE");
        Console.WriteLine("==============================");
        
        Console.Write("Titre : ");
        string titre = Console.ReadLine();
        
        Console.Write("Description : ");
        string description = Console.ReadLine();
        
        // Sélection de la catégorie
        Console.WriteLine("\nCatégories disponibles :");
        var categories = Enum.GetValues<Categorie>();
        for (int i = 0; i < categories.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {categories[i]}");
        }
        
        Console.Write("Choisissez une catégorie (1-6) : ");
        if (int.TryParse(Console.ReadLine(), out int choixCategorie) && 
            choixCategorie >= 1 && choixCategorie <= categories.Length)
        {
            Categorie categorie = categories[choixCategorie - 1];
            
            // Sélection de la priorité
            Console.WriteLine("\nPriorités disponibles :");
            var priorites = Enum.GetValues<Priorite>();
            for (int i = 0; i < priorites.Length; i++)
            {
                Console.WriteLine($"{i + 1}. {priorites[i]}");
            }
            
            Console.Write("Choisissez une priorité (1-4, défaut=2) : ");
            Priorite priorite = Priorite.Normale;
            if (int.TryParse(Console.ReadLine(), out int choixPriorite) && 
                choixPriorite >= 1 && choixPriorite <= priorites.Length)
            {
                priorite = priorites[choixPriorite - 1];
            }
            
            // Échéance optionnelle
            Console.Write("Date d'échéance (dd/MM/yyyy, optionnel) : ");
            DateTime? echeance = null;
            string dateStr = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(dateStr) && 
                DateTime.TryParseExact(dateStr, "dd/MM/yyyy", null, 
                                     System.Globalization.DateTimeStyles.None, out DateTime date))
            {
                echeance = date;
            }
            
            gestionnaire.AjouterTache(titre, description, categorie, priorite, echeance);
        }
        else
        {
            Console.WriteLine("❌ Catégorie invalide !");
        }
    }
    
    private void TerminerTache()
    {
        Console.Write("\n✅ ID de la tâche à terminer : ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            var tache = gestionnaire.ObtenirTache(id);
            if (tache != null)
            {
                tache.Terminer();
                gestionnaire.SauvegarderFichier();
            }
            else
            {
                Console.WriteLine($"❌ Aucune tâche trouvée avec l'ID {id}");
            }
        }
        else
        {
            Console.WriteLine("❌ ID invalide !");
        }
    }
    
    private void SupprimerTache()
    {
        Console.Write("\n🗑️  ID de la tâche à supprimer : ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            gestionnaire.SupprimerTache(id);
        }
        else
        {
            Console.WriteLine("❌ ID invalide !");
        }
    }
    
    private void FiltrerParCategorie()
    {
        Console.WriteLine("\n📂 FILTRER PAR CATÉGORIE");
        Console.WriteLine("=========================");
        
        var categories = Enum.GetValues<Categorie>();
        for (int i = 0; i < categories.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {categories[i]}");
        }
        
        Console.Write("Choisissez une catégorie (1-6) : ");
        if (int.TryParse(Console.ReadLine(), out int choix) && 
            choix >= 1 && choix <= categories.Length)
        {
            gestionnaire.FiltrerParCategorie(categories[choix - 1]);
        }
        else
        {
            Console.WriteLine("❌ Choix invalide !");
        }
    }
    
    private void AfficherDetailsTache()
    {
        Console.Write("\n🔍 ID de la tâche à afficher : ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            var tache = gestionnaire.ObtenirTache(id);
            if (tache != null)
            {
                tache.AfficherDetails();
            }
            else
            {
                Console.WriteLine($"❌ Aucune tâche trouvée avec l'ID {id}");
            }
        }
        else
        {
            Console.WriteLine("❌ ID invalide !");
        }
    }
}

// Programme principal
class Program
{
    static void Main(string[] args)
    {
        try
        {
            var interface = new InterfaceConsole();
            interface.Demarrer();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Erreur fatale : {ex.Message}");
            Console.WriteLine("Appuyez sur une touche pour quitter...");
            Console.ReadKey();
        }
    }
}