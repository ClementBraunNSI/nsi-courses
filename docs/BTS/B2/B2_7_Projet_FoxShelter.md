# 🦊 B2.7 - Projet FoxShelter - Gestion de Refuge pour Renards

<style>
.project-header {
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(255, 107, 53, 0.3);
}

.project-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.project-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    font-weight: 300;
}

.concept-card {
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), rgba(247, 147, 30, 0.05));
    border: 1px solid rgba(255, 107, 53, 0.2);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.1);
    transition: all 0.3s ease;
}

.concept-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(255, 107, 53, 0.15);
}

.concept-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    display: block;
}

.concept-name {
    font-size: 1.3rem;
    font-weight: 700;
    color: #ff6b35;
    margin-bottom: 0.8rem;
}

.concept-description {
    color: #2c3e50;
    line-height: 1.6;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(247, 147, 30, 0.1), rgba(255, 107, 53, 0.1));
    border-left: 4px solid #ff6b35;
    padding: 1rem 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0 10px 10px 0;
    box-shadow: 0 2px 10px rgba(255, 107, 53, 0.1);
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
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), rgba(247, 147, 30, 0.05));
    border: 1px solid rgba(255, 107, 53, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.warning-box {
    background: linear-gradient(135deg, rgba(220, 53, 69, 0.1), rgba(255, 107, 107, 0.05));
    border: 1px solid rgba(220, 53, 69, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
    border-left: 4px solid #dc3545;
}

.success-box {
    background: linear-gradient(135deg, rgba(40, 167, 69, 0.1), rgba(72, 187, 120, 0.05));
    border: 1px solid rgba(40, 167, 69, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
    border-left: 4px solid #28a745;
}

.uml-diagram {
    background: #f8f9fa;
    border: 2px solid #ff6b35;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
}

.architecture-section {
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.05), rgba(247, 147, 30, 0.02));
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.feature-card {
    background: white;
    border: 1px solid rgba(255, 107, 53, 0.2);
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.1);
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(255, 107, 53, 0.15);
}

.tech-stack {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
}

.database-schema {
    background: #f1f3f4;
    border: 1px solid #dadce0;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    overflow-x: auto;
}
</style>

<div class="project-header">
    <h1 class="project-title">🦊 FoxShelter</h1>
    <p class="project-subtitle">Système de gestion de refuge pour renards - Projet BTS SIO 1 SLAM</p>
</div>

## 📋 Objectifs du projet

À la fin de ce projet, vous serez capable de :
- ✅ Concevoir une application complète avec UML
- ✅ Implémenter le pattern MVC en C#
- ✅ Gérer une base de données avec Entity Framework
- ✅ Appliquer tous les concepts de POO
- ✅ Créer une interface utilisateur fonctionnelle
- ✅ Documenter et tester votre application

---

## 🎯 Cahier des charges

<div class="concept-card">
<span class="concept-icon">📋</span>
<div class="concept-name">Contexte du projet</div>
<div class="concept-description">
Le refuge "FoxShelter" accueille des renards blessés, orphelins ou en détresse. L'association a besoin d'un système informatique pour gérer efficacement les animaux, le personnel, les soins vétérinaires et les finances.
</div>
</div>

### 🎪 Fonctionnalités principales

<div class="feature-grid">
<div class="feature-card">
<h4>🦊 Gestion des Renards</h4>
<ul>
<li>Enregistrement des nouveaux arrivants</li>
<li>Suivi de l'état de santé</li>
<li>Historique des soins</li>
<li>Gestion des adoptions</li>
</ul>
</div>

<div class="feature-card">
<h4>👥 Gestion du Personnel</h4>
<ul>
<li>Employés et bénévoles</li>
<li>Planning des équipes</li>
<li>Compétences et formations</li>
<li>Historique des interventions</li>
</ul>
</div>

<div class="feature-card">
<h4>🏥 Suivi Vétérinaire</h4>
<ul>
<li>Consultations et diagnostics</li>
<li>Traitements et médicaments</li>
<li>Vaccinations</li>
<li>Rapports médicaux</li>
</ul>
</div>

<div class="feature-card">
<h4>🍽️ Gestion Alimentaire</h4>
<ul>
<li>Régimes alimentaires spécialisés</li>
<li>Stock de nourriture</li>
<li>Planning des repas</li>
<li>Coûts alimentaires</li>
</ul>
</div>

<div class="feature-card">
<h4>💰 Gestion Financière</h4>
<ul>
<li>Dons et subventions</li>
<li>Frais vétérinaires</li>
<li>Coûts opérationnels</li>
<li>Rapports financiers</li>
</ul>
</div>

<div class="feature-card">
<h4>📊 Rapports & Statistiques</h4>
<ul>
<li>Nombre d'animaux accueillis</li>
<li>Taux de guérison</li>
<li>Coûts par animal</li>
<li>Efficacité des traitements</li>
</ul>
</div>
</div>

---

## 🏗️ Architecture du projet

<div class="architecture-section">
<h3>📐 Pattern MVC (Model-View-Controller)</h3>

<div class="highlight-fact">
<strong>🎯 Structure du projet :</strong>
<ul>
<li><strong>Models :</strong> Entités métier (Renard, Personne, SoinVeterinaire...)</li>
<li><strong>Views :</strong> Interfaces utilisateur (formulaires, listes, rapports)</li>
<li><strong>Controllers :</strong> Logique de traitement et coordination</li>
<li><strong>Data :</strong> Accès aux données avec Entity Framework</li>
</ul>
</div>

<div class="tech-stack">
<h4>🛠️ Stack Technologique</h4>
<ul>
<li><strong>Langage :</strong> C# .NET 6.0</li>
<li><strong>Framework :</strong> ASP.NET Core MVC</li>
<li><strong>Base de données :</strong> SQL Server / SQLite</li>
<li><strong>ORM :</strong> Entity Framework Core</li>
<li><strong>Interface :</strong> Bootstrap + CSS personnalisé</li>
<li><strong>Tests :</strong> xUnit</li>
</ul>
</div>
</div>

---

## 📊 Diagrammes UML

### 🏗️ Diagramme de classes

<div class="uml-diagram">
<strong>Diagramme de classes principal</strong><br><br>

```
┌─────────────────────────────────────┐
│              Renard                 │
├─────────────────────────────────────┤
│ - Id : int                          │
│ - Nom : string                      │
│ - Espece : string                   │
│ - Age : int                         │
│ - Sexe : char                       │
│ - DateArrivee : DateTime            │
│ - EtatSante : EtatSante             │
│ - Poids : decimal                   │
│ - Description : string              │
│ - EstAdopte : bool                  │
├─────────────────────────────────────┤
│ + AjouterSoin(soin: SoinVeterinaire)│
│ + ModifierEtatSante(etat: EtatSante)│
│ + CalculerDureeSejourJours() : int  │
│ + PeutEtreAdopte() : bool           │
└─────────────────────────────────────┘
                    │
                    │ 1..*
                    ▼
┌─────────────────────────────────────┐
│          SoinVeterinaire            │
├─────────────────────────────────────┤
│ - Id : int                          │
│ - DateSoin : DateTime               │
│ - TypeSoin : TypeSoin               │
│ - Description : string              │
│ - Medicaments : string              │
│ - Cout : decimal                    │
│ - VeterinaireId : int               │
│ - RenardId : int                    │
├─────────────────────────────────────┤
│ + CalculerCoutTotal() : decimal     │
│ + EstUrgent() : bool                │
└─────────────────────────────────────┘
                    │
                    │ *..*
                    ▼
┌─────────────────────────────────────┐
│             Personne                │
├─────────────────────────────────────┤
│ - Id : int                          │
│ - Nom : string                      │
│ - Prenom : string                   │
│ - Email : string                    │
│ - Telephone : string                │
│ - DateNaissance : DateTime          │
│ - Adresse : string                  │
├─────────────────────────────────────┤
│ + CalculerAge() : int               │
│ + ObtenirNomComplet() : string      │
└─────────────────────────────────────┘
                    ▲
        ┌───────────┴───────────┐
        │                       │
┌───────────────┐    ┌──────────────────┐
│   Employe     │    │    Benevole      │
├───────────────┤    ├──────────────────┤
│ - Salaire     │    │ - Disponibilites │
│ - Poste       │    │ - Competences    │
│ - DateEmbauche│    │ - HeuresBenevolat│
├───────────────┤    ├──────────────────┤
│ + CalculerAn- │    │ + AjouterHeures()│
│   ciennete()  │    │ + EstDisponible()│
└───────────────┘    └──────────────────┘

┌─────────────────────────────────────┐
│            RegimeAlimentaire        │
├─────────────────────────────────────┤
│ - Id : int                          │
│ - Nom : string                      │
│ - Description : string              │
│ - FrequenceRepas : int              │
│ - QuantiteParRepas : decimal        │
│ - TypeNourriture : string           │
│ - CoutJournalier : decimal          │
├─────────────────────────────────────┤
│ + CalculerCoutMensuel() : decimal   │
│ + EstAdapteAge(age: int) : bool     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│              Don                    │
├─────────────────────────────────────┤
│ - Id : int                          │
│ - Montant : decimal                 │
│ - DateDon : DateTime                │
│ - TypeDon : TypeDon                 │
│ - DonateurNom : string              │
│ - DonateurEmail : string            │
│ - EstRecurrent : bool               │
├─────────────────────────────────────┤
│ + CalculerTotalAnnuel() : decimal   │
│ + GenererRecu() : string            │
└─────────────────────────────────────┘
```
</div>

### 🎭 Diagramme de cas d'usage

<div class="uml-diagram">
<strong>Cas d'usage principaux</strong><br><br>

```
                    Système FoxShelter
    
    Employé                              Vétérinaire
       │                                     │
       │ ──── Enregistrer nouveau renard     │
       │ ──── Modifier informations renard   │
       │ ──── Gérer planning équipes         │
       │                                     │ ──── Effectuer consultation
       │                                     │ ──── Prescrire traitement
       │                                     │ ──── Suivre évolution santé
       │                                     │ ──── Générer rapport médical
    
    Bénévole                             Directeur
       │                                     │
       │ ──── Nourrir les renards            │
       │ ──── Nettoyer enclos                │
       │ ──── Enregistrer observations       │
       │                                     │ ──── Consulter rapports
       │                                     │ ──── Gérer budget
       │                                     │ ──── Valider adoptions
       │                                     │ ──── Superviser équipes
    
    Adoptant                             Donateur
       │                                     │
       │ ──── Consulter renards adoptables   │
       │ ──── Déposer demande adoption       │
       │ ──── Suivre processus adoption      │
       │                                     │ ──── Effectuer don
       │                                     │ ──── Consulter utilisation fonds
       │                                     │ ──── Recevoir reçu fiscal
```
</div>

---

## 💾 Modèle de base de données

<div class="database-schema">
<h3>🗄️ Schéma de base de données</h3>

<strong>Tables principales :</strong>

```sql
-- Table Renards
CREATE TABLE Renards (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nom NVARCHAR(100) NOT NULL,
    Espece NVARCHAR(50) NOT NULL,
    Age INT,
    Sexe CHAR(1) CHECK (Sexe IN ('M', 'F')),
    DateArrivee DATETIME2 NOT NULL DEFAULT GETDATE(),
    EtatSante INT NOT NULL, -- Enum: Critique=1, Faible=2, Stable=3, Bon=4
    Poids DECIMAL(5,2),
    Description NVARCHAR(MAX),
    EstAdopte BIT DEFAULT 0,
    RegimeAlimentaireId INT,
    DateCreation DATETIME2 DEFAULT GETDATE(),
    DateModification DATETIME2 DEFAULT GETDATE()
);

-- Table Personnes (classe mère)
CREATE TABLE Personnes (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nom NVARCHAR(100) NOT NULL,
    Prenom NVARCHAR(100) NOT NULL,
    Email NVARCHAR(255) UNIQUE,
    Telephone NVARCHAR(20),
    DateNaissance DATE,
    Adresse NVARCHAR(500),
    TypePersonne NVARCHAR(20) NOT NULL, -- Discriminator: Employe, Benevole
    -- Champs spécifiques Employe
    Salaire DECIMAL(10,2),
    Poste NVARCHAR(100),
    DateEmbauche DATE,
    -- Champs spécifiques Benevole
    Disponibilites NVARCHAR(MAX),
    Competences NVARCHAR(MAX),
    HeuresBenevolat INT DEFAULT 0
);

-- Table Soins Vétérinaires
CREATE TABLE SoinsVeterinaires (
    Id INT PRIMARY KEY IDENTITY(1,1),
    DateSoin DATETIME2 NOT NULL,
    TypeSoin INT NOT NULL, -- Enum: Consultation=1, Vaccination=2, Chirurgie=3, etc.
    Description NVARCHAR(MAX),
    Medicaments NVARCHAR(MAX),
    Cout DECIMAL(8,2),
    VeterinaireId INT NOT NULL,
    RenardId INT NOT NULL,
    FOREIGN KEY (VeterinaireId) REFERENCES Personnes(Id),
    FOREIGN KEY (RenardId) REFERENCES Renards(Id)
);

-- Table Régimes Alimentaires
CREATE TABLE RegimesAlimentaires (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nom NVARCHAR(100) NOT NULL,
    Description NVARCHAR(MAX),
    FrequenceRepas INT NOT NULL,
    QuantiteParRepas DECIMAL(5,2),
    TypeNourriture NVARCHAR(200),
    CoutJournalier DECIMAL(6,2)
);

-- Table Dons
CREATE TABLE Dons (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Montant DECIMAL(10,2) NOT NULL,
    DateDon DATETIME2 NOT NULL DEFAULT GETDATE(),
    TypeDon INT NOT NULL, -- Enum: Argent=1, Nourriture=2, Materiel=3
    DonateurNom NVARCHAR(200),
    DonateurEmail NVARCHAR(255),
    EstRecurrent BIT DEFAULT 0,
    Description NVARCHAR(MAX)
);

-- Table Planning (pour les équipes)
CREATE TABLE Plannings (
    Id INT PRIMARY KEY IDENTITY(1,1),
    PersonneId INT NOT NULL,
    DateDebut DATETIME2 NOT NULL,
    DateFin DATETIME2 NOT NULL,
    TypeActivite NVARCHAR(100),
    Description NVARCHAR(MAX),
    FOREIGN KEY (PersonneId) REFERENCES Personnes(Id)
);
```
</div>

---

## 🏗️ Structure du projet C#

<div class="code-example">
```
FoxShelter/
├── FoxShelter.Models/              # Couche Modèles
│   ├── Entities/
│   │   ├── Renard.cs
│   │   ├── Personne.cs
│   │   ├── Employe.cs
│   │   ├── Benevole.cs
│   │   ├── SoinVeterinaire.cs
│   │   ├── RegimeAlimentaire.cs
│   │   └── Don.cs
│   ├── Enums/
│   │   ├── EtatSante.cs
│   │   ├── TypeSoin.cs
│   │   └── TypeDon.cs
│   └── ViewModels/
│       ├── RenardViewModel.cs
│       ├── SoinViewModel.cs
│       └── RapportViewModel.cs
│
├── FoxShelter.Data/                # Couche Données
│   ├── FoxShelterContext.cs
│   ├── Repositories/
│   │   ├── IRepository.cs
│   │   ├── RenardRepository.cs
│   │   ├── PersonneRepository.cs
│   │   └── SoinRepository.cs
│   └── Migrations/
│
├── FoxShelter.Services/            # Couche Services
│   ├── IRenardService.cs
│   ├── RenardService.cs
│   ├── ISoinService.cs
│   ├── SoinService.cs
│   └── IStatistiqueService.cs
│
├── FoxShelter.Web/                 # Application Web MVC
│   ├── Controllers/
│   │   ├── HomeController.cs
│   │   ├── RenardController.cs
│   │   ├── PersonneController.cs
│   │   ├── SoinController.cs
│   │   └── RapportController.cs
│   ├── Views/
│   │   ├── Shared/
│   │   ├── Home/
│   │   ├── Renard/
│   │   ├── Personne/
│   │   └── Soin/
│   ├── wwwroot/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── Program.cs
│
└── FoxShelter.Tests/               # Tests unitaires
    ├── Models/
    ├── Services/
    └── Controllers/
```
</div>

---

## 🎯 Implémentation des modèles

### 🦊 Classe Renard

<div class="code-example">
```csharp
using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Entities
{
    public class Renard
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le nom est obligatoire")]
        [StringLength(100, ErrorMessage = "Le nom ne peut pas dépasser 100 caractères")]
        public string Nom { get; set; }
        
        [Required(ErrorMessage = "L'espèce est obligatoire")]
        [StringLength(50)]
        public string Espece { get; set; }
        
        [Range(0, 20, ErrorMessage = "L'âge doit être entre 0 et 20 ans")]
        public int? Age { get; set; }
        
        [Required]
        public char Sexe { get; set; } // 'M' ou 'F'
        
        [Required]
        public DateTime DateArrivee { get; set; } = DateTime.Now;
        
        [Required]
        public EtatSante EtatSante { get; set; }
        
        [Range(0.1, 50.0, ErrorMessage = "Le poids doit être entre 0.1 et 50 kg")]
        public decimal? Poids { get; set; }
        
        [StringLength(1000)]
        public string? Description { get; set; }
        
        public bool EstAdopte { get; set; } = false;
        
        public int? RegimeAlimentaireId { get; set; }
        public RegimeAlimentaire? RegimeAlimentaire { get; set; }
        
        // Relations
        public virtual ICollection<SoinVeterinaire> Soins { get; set; } = new List<SoinVeterinaire>();
        
        public DateTime DateCreation { get; set; } = DateTime.Now;
        public DateTime DateModification { get; set; } = DateTime.Now;
        
        // Méthodes métier
        public int CalculerDureeSejourJours()
        {
            return (DateTime.Now - DateArrivee).Days;
        }
        
        public bool PeutEtreAdopte()
        {
            return EtatSante == EtatSante.Bon && !EstAdopte;
        }
        
        public decimal CalculerCoutTotal()
        {
            return Soins.Sum(s => s.Cout);
        }
        
        public SoinVeterinaire? DernierSoin()
        {
            return Soins.OrderByDescending(s => s.DateSoin).FirstOrDefault();
        }
    }
}
```
</div>

### 👥 Classe Personne et héritages

<div class="code-example">
```csharp
using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Entities
{
    public abstract class Personne
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le nom est obligatoire")]
        [StringLength(100)]
        public string Nom { get; set; }
        
        [Required(ErrorMessage = "Le prénom est obligatoire")]
        [StringLength(100)]
        public string Prenom { get; set; }
        
        [EmailAddress(ErrorMessage = "Format d'email invalide")]
        public string? Email { get; set; }
        
        [Phone(ErrorMessage = "Format de téléphone invalide")]
        public string? Telephone { get; set; }
        
        public DateTime? DateNaissance { get; set; }
        
        [StringLength(500)]
        public string? Adresse { get; set; }
        
        // Méthodes
        public int CalculerAge()
        {
            if (!DateNaissance.HasValue) return 0;
            var age = DateTime.Now.Year - DateNaissance.Value.Year;
            if (DateTime.Now.DayOfYear < DateNaissance.Value.DayOfYear)
                age--;
            return age;
        }
        
        public string ObtenirNomComplet()
        {
            return $"{Prenom} {Nom}";
        }
    }
    
    public class Employe : Personne
    {
        [Range(0, 100000, ErrorMessage = "Le salaire doit être positif")]
        public decimal? Salaire { get; set; }
        
        [StringLength(100)]
        public string? Poste { get; set; }
        
        public DateTime? DateEmbauche { get; set; }
        
        public int CalculerAncienneteAnnees()
        {
            if (!DateEmbauche.HasValue) return 0;
            return DateTime.Now.Year - DateEmbauche.Value.Year;
        }
        
        public decimal CalculerSalaireAnnuel()
        {
            return Salaire.HasValue ? Salaire.Value * 12 : 0;
        }
    }
    
    public class Benevole : Personne
    {
        public string? Disponibilites { get; set; }
        public string? Competences { get; set; }
        
        [Range(0, int.MaxValue)]
        public int HeuresBenevolat { get; set; } = 0;
        
        public void AjouterHeures(int heures)
        {
            if (heures > 0)
                HeuresBenevolat += heures;
        }
        
        public bool EstDisponible(DateTime date)
        {
            // Logique de vérification des disponibilités
            return !string.IsNullOrEmpty(Disponibilites);
        }
    }
}
```
</div>

### 🏥 Classe SoinVeterinaire

<div class="code-example">
```csharp
using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Entities
{
    public class SoinVeterinaire
    {
        public int Id { get; set; }
        
        [Required]
        public DateTime DateSoin { get; set; } = DateTime.Now;
        
        [Required]
        public TypeSoin TypeSoin { get; set; }
        
        [Required(ErrorMessage = "La description est obligatoire")]
        [StringLength(1000)]
        public string Description { get; set; }
        
        public string? Medicaments { get; set; }
        
        [Range(0, 10000, ErrorMessage = "Le coût doit être positif")]
        public decimal Cout { get; set; }
        
        [Required]
        public int VeterinaireId { get; set; }
        public virtual Employe Veterinaire { get; set; }
        
        [Required]
        public int RenardId { get; set; }
        public virtual Renard Renard { get; set; }
        
        // Méthodes métier
        public bool EstUrgent()
        {
            return TypeSoin == TypeSoin.Urgence || 
                   TypeSoin == TypeSoin.Chirurgie;
        }
        
        public bool EstRecent()
        {
            return (DateTime.Now - DateSoin).Days <= 7;
        }
        
        public string ObtenirResume()
        {
            return $"{TypeSoin} - {DateSoin:dd/MM/yyyy} - {Cout:C}";
        }
    }
}
```
</div>

---

## 🎮 Contrôleurs MVC

### 🦊 RenardController

<div class="code-example">
```csharp
using Microsoft.AspNetCore.Mvc;
using FoxShelter.Models.Entities;
using FoxShelter.Services;
using FoxShelter.Models.ViewModels;

namespace FoxShelter.Web.Controllers
{
    public class RenardController : Controller
    {
        private readonly IRenardService _renardService;
        private readonly ISoinService _soinService;
        
        public RenardController(IRenardService renardService, ISoinService soinService)
        {
            _renardService = renardService;
            _soinService = soinService;
        }
        
        // GET: Renard
        public async Task<IActionResult> Index(string? recherche, EtatSante? etatSante)
        {
            var renards = await _renardService.ObtenirTousAsync();
            
            if (!string.IsNullOrEmpty(recherche))
            {
                renards = renards.Where(r => r.Nom.Contains(recherche, StringComparison.OrdinalIgnoreCase));
            }
            
            if (etatSante.HasValue)
            {
                renards = renards.Where(r => r.EtatSante == etatSante.Value);
            }
            
            var viewModel = new RenardIndexViewModel
            {
                Renards = renards.ToList(),
                Recherche = recherche,
                EtatSanteFiltre = etatSante,
                Statistiques = await _renardService.ObtenirStatistiquesAsync()
            };
            
            return View(viewModel);
        }
        
        // GET: Renard/Details/5
        public async Task<IActionResult> Details(int id)
        {
            var renard = await _renardService.ObtenirParIdAsync(id);
            if (renard == null)
            {
                return NotFound();
            }
            
            var soins = await _soinService.ObtenirParRenardAsync(id);
            
            var viewModel = new RenardDetailsViewModel
            {
                Renard = renard,
                Soins = soins.ToList(),
                CoutTotal = soins.Sum(s => s.Cout),
                DureeSejourJours = renard.CalculerDureeSejourJours()
            };
            
            return View(viewModel);
        }
        
        // GET: Renard/Create
        public IActionResult Create()
        {
            var viewModel = new RenardCreateViewModel();
            return View(viewModel);
        }
        
        // POST: Renard/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(RenardCreateViewModel viewModel)
        {
            if (ModelState.IsValid)
            {
                var renard = new Renard
                {
                    Nom = viewModel.Nom,
                    Espece = viewModel.Espece,
                    Age = viewModel.Age,
                    Sexe = viewModel.Sexe,
                    EtatSante = viewModel.EtatSante,
                    Poids = viewModel.Poids,
                    Description = viewModel.Description,
                    DateArrivee = viewModel.DateArrivee
                };
                
                await _renardService.AjouterAsync(renard);
                
                TempData["Success"] = $"Le renard {renard.Nom} a été ajouté avec succès !";
                return RedirectToAction(nameof(Index));
            }
            
            return View(viewModel);
        }
        
        // GET: Renard/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            var renard = await _renardService.ObtenirParIdAsync(id);
            if (renard == null)
            {
                return NotFound();
            }
            
            var viewModel = new RenardEditViewModel
            {
                Id = renard.Id,
                Nom = renard.Nom,
                Espece = renard.Espece,
                Age = renard.Age,
                Sexe = renard.Sexe,
                EtatSante = renard.EtatSante,
                Poids = renard.Poids,
                Description = renard.Description,
                EstAdopte = renard.EstAdopte
            };
            
            return View(viewModel);
        }
        
        // POST: Renard/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, RenardEditViewModel viewModel)
        {
            if (id != viewModel.Id)
            {
                return NotFound();
            }
            
            if (ModelState.IsValid)
            {
                try
                {
                    var renard = await _renardService.ObtenirParIdAsync(id);
                    if (renard == null)
                    {
                        return NotFound();
                    }
                    
                    renard.Nom = viewModel.Nom;
                    renard.Espece = viewModel.Espece;
                    renard.Age = viewModel.Age;
                    renard.Sexe = viewModel.Sexe;
                    renard.EtatSante = viewModel.EtatSante;
                    renard.Poids = viewModel.Poids;
                    renard.Description = viewModel.Description;
                    renard.EstAdopte = viewModel.EstAdopte;
                    renard.DateModification = DateTime.Now;
                    
                    await _renardService.ModifierAsync(renard);
                    
                    TempData["Success"] = $"Les informations de {renard.Nom} ont été mises à jour !";
                    return RedirectToAction(nameof(Details), new { id = renard.Id });
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", "Une erreur est survenue lors de la mise à jour.");
                }
            }
            
            return View(viewModel);
        }
        
        // POST: Renard/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Delete(int id)
        {
            var renard = await _renardService.ObtenirParIdAsync(id);
            if (renard == null)
            {
                return NotFound();
            }
            
            await _renardService.SupprimerAsync(id);
            
            TempData["Success"] = $"Le renard {renard.Nom} a été supprimé.";
            return RedirectToAction(nameof(Index));
        }
        
        // GET: Renard/Adoptables
        public async Task<IActionResult> Adoptables()
        {
            var renards = await _renardService.ObtenirAdoptablesAsync();
            return View(renards);
        }
    }
}
```
</div>

---

## 🎯 Exercices pratiques

<div class="exercise-box">
<h4>🏋️ Exercice 1 : Implémentation des Enums</h4>

Créez les énumérations suivantes avec leurs valeurs appropriées :

```csharp
// Votre code ici pour :
// - EtatSante (Critique, Faible, Stable, Bon, Excellent)
// - TypeSoin (Consultation, Vaccination, Chirurgie, Urgence, Controle)
// - TypeDon (Argent, Nourriture, Materiel, Service)
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 2 : Service RenardService</h4>

Implémentez la classe `RenardService` avec les méthodes :
- `ObtenirTousAsync()`
- `ObtenirParIdAsync(int id)`
- `AjouterAsync(Renard renard)`
- `ModifierAsync(Renard renard)`
- `SupprimerAsync(int id)`
- `ObtenirAdoptablesAsync()`
- `ObtenirStatistiquesAsync()`

```csharp
// Votre implémentation ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 3 : ViewModels</h4>

Créez les ViewModels pour :
- `RenardIndexViewModel` (liste + filtres + statistiques)
- `RenardDetailsViewModel` (détails + soins + coûts)
- `RenardCreateViewModel` (création)
- `RenardEditViewModel` (modification)

```csharp
// Vos ViewModels ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 4 : Context Entity Framework</h4>

Implémentez `FoxShelterContext` avec :
- Configuration des entités
- Relations entre tables
- Contraintes et index
- Données de test (Seed)

```csharp
// Votre DbContext ici
```
</div>

---

## 📚 Points clés à retenir

<div class="success-box">
<strong>🎯 Compétences développées :</strong>
<ul>
<li><strong>Architecture MVC :</strong> Séparation claire des responsabilités</li>
<li><strong>POO avancée :</strong> Héritage, polymorphisme, encapsulation</li>
<li><strong>Entity Framework :</strong> ORM et gestion de base de données</li>
<li><strong>Validation :</strong> Annotations et validation côté serveur</li>
<li><strong>Services :</strong> Logique métier découplée</li>
<li><strong>ViewModels :</strong> Adaptation des données pour les vues</li>
</ul>
</div>

<div class="warning-box">
<strong>⚠️ Points d'attention :</strong>
<ul>
<li><strong>Validation :</strong> Toujours valider côté serveur ET client</li>
<li><strong>Sécurité :</strong> Protection contre les injections SQL</li>
<li><strong>Performance :</strong> Utiliser async/await pour les opérations DB</li>
<li><strong>Tests :</strong> Tester la logique métier et les contrôleurs</li>
<li><strong>Documentation :</strong> Commenter le code complexe</li>
</ul>
</div>

---

## 🔗 Ressources complémentaires

- [ASP.NET Core MVC](https://docs.microsoft.com/fr-fr/aspnet/core/mvc/)
- [Entity Framework Core](https://docs.microsoft.com/fr-fr/ef/core/)
- [Validation en ASP.NET Core](https://docs.microsoft.com/fr-fr/aspnet/core/mvc/models/validation)
- [Patterns Repository et Service](https://docs.microsoft.com/fr-fr/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/)

---

**Étape précédente :** [B2.6 - Projets d'application](B2_6_Projets_applications.md)  
**Prochaine étape :** [B2.8 - Tests et déploiement](B2_8_Tests_deploiement.md)