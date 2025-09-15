# Projets & Stage - BTS SIO SLAM

## 🎯 Objectifs du module

Ce module accompagne les étudiants dans la réalisation de leurs projets professionnels et la préparation au stage :
- **Gestion de projet** informatique
- **Méthodologies** de développement
- **Travail en équipe** et collaboration
- **Préparation au stage** en entreprise
- **Soutenance** et présentation

---

## 📋 Chapitre 1 : Gestion de projet informatique

### 1.1 Méthodologies de projet

#### 🏗️ **Cycle de vie en V**

```
┌─────────────────────────────────────────┐
│            CYCLE EN V                   │
├─────────────────────────────────────────┤
│                                         │
│  📋 ANALYSE BESOINS ←→ 🧪 TESTS ACCEPTATION │
│       ↓                    ↑            │
│  📐 CONCEPTION GÉNÉRALE ←→ 🔧 TESTS INTÉGRATION │
│       ↓                    ↑            │
│  🔍 CONCEPTION DÉTAILLÉE ←→ ⚡ TESTS UNITAIRES │
│       ↓                    ↑            │
│       💻 DÉVELOPPEMENT                   │
│                                         │
└─────────────────────────────────────────┘
```

**Phases du projet** :

```csharp
// Modèle de gestion de projet
public class ProjetInformatique
{
    public enum PhaseProjet
    {
        Initialisation,
        Analyse,
        ConceptionGenerale,
        ConceptionDetaillee,
        Developpement,
        TestsUnitaires,
        TestsIntegration,
        TestsAcceptation,
        Deploiement,
        Maintenance
    }
    
    public class Livrable
    {
        public string Nom { get; set; }
        public string Description { get; set; }
        public PhaseProjet Phase { get; set; }
        public DateTime DatePrevue { get; set; }
        public DateTime? DateReelle { get; set; }
        public StatutLivrable Statut { get; set; }
        public List<string> Responsables { get; set; } = new();
        public List<string> Dependances { get; set; } = new();
    }
    
    public enum StatutLivrable
    {
        NonDemarre,
        EnCours,
        EnAttente,
        Termine,
        Valide
    }
    
    // Exemple de livrables pour un projet e-commerce
    public static List<Livrable> GetLivrablesECommerce()
    {
        return new List<Livrable>
        {
            // Phase Analyse
            new Livrable
            {
                Nom = "Cahier des charges",
                Description = "Spécifications fonctionnelles et techniques",
                Phase = PhaseProjet.Analyse,
                DatePrevue = DateTime.Now.AddDays(7),
                Responsables = new() { "Chef de projet", "Analyste" }
            },
            new Livrable
            {
                Nom = "Maquettes UI/UX",
                Description = "Wireframes et prototypes d'interface",
                Phase = PhaseProjet.Analyse,
                DatePrevue = DateTime.Now.AddDays(10),
                Responsables = new() { "Designer UX" }
            },
            
            // Phase Conception
            new Livrable
            {
                Nom = "Architecture technique",
                Description = "Diagrammes d'architecture et choix technologiques",
                Phase = PhaseProjet.ConceptionGenerale,
                DatePrevue = DateTime.Now.AddDays(14),
                Responsables = new() { "Architecte", "Lead Developer" },
                Dependances = new() { "Cahier des charges" }
            },
            new Livrable
            {
                Nom = "Modèle de données",
                Description = "Schéma de base de données et entités",
                Phase = PhaseProjet.ConceptionDetaillee,
                DatePrevue = DateTime.Now.AddDays(17),
                Responsables = new() { "Data Architect" },
                Dependances = new() { "Architecture technique" }
            },
            
            // Phase Développement
            new Livrable
            {
                Nom = "API Backend",
                Description = "Services REST et logique métier",
                Phase = PhaseProjet.Developpement,
                DatePrevue = DateTime.Now.AddDays(35),
                Responsables = new() { "Backend Developer" },
                Dependances = new() { "Modèle de données" }
            },
            new Livrable
            {
                Nom = "Interface utilisateur",
                Description = "Application web responsive",
                Phase = PhaseProjet.Developpement,
                DatePrevue = DateTime.Now.AddDays(40),
                Responsables = new() { "Frontend Developer" },
                Dependances = new() { "Maquettes UI/UX", "API Backend" }
            }
        };
    }
}
```

#### 🔄 **Méthodologie Agile - Scrum**

```csharp
// Modèle Scrum
public class ProjetScrum
{
    public class Sprint
    {
        public int Numero { get; set; }
        public string Objectif { get; set; }
        public DateTime DateDebut { get; set; }
        public DateTime DateFin { get; set; }
        public List<UserStory> UserStories { get; set; } = new();
        public List<Tache> Taches { get; set; } = new();
        public SprintReview Review { get; set; }
        public SprintRetrospective Retrospective { get; set; }
    }
    
    public class UserStory
    {
        public string Id { get; set; }
        public string Titre { get; set; }
        public string Description { get; set; }
        public string Persona { get; set; }
        public string Objectif { get; set; }
        public string Benefice { get; set; }
        public int StoryPoints { get; set; }
        public Priorite Priorite { get; set; }
        public List<CritereAcceptation> CriteresAcceptation { get; set; } = new();
        public StatutStory Statut { get; set; }
        
        // Format: En tant que [persona], je veux [objectif] afin de [bénéfice]
        public string FormatStandard => 
            $"En tant que {Persona}, je veux {Objectif} afin de {Benefice}";
    }
    
    public enum Priorite
    {
        Critique = 1,
        Haute = 2,
        Moyenne = 3,
        Basse = 4
    }
    
    public enum StatutStory
    {
        ProductBacklog,
        SprintBacklog,
        EnCours,
        EnTest,
        Terminee,
        Acceptee
    }
    
    public class CritereAcceptation
    {
        public string Description { get; set; }
        public bool EstValide { get; set; }
        public string Commentaire { get; set; }
    }
    
    public class Tache
    {
        public string Id { get; set; }
        public string Titre { get; set; }
        public string Description { get; set; }
        public string UserStoryId { get; set; }
        public string Assignee { get; set; }
        public int EstimationHeures { get; set; }
        public int HeuresPassees { get; set; }
        public StatutTache Statut { get; set; }
        public DateTime? DateDebut { get; set; }
        public DateTime? DateFin { get; set; }
    }
    
    public enum StatutTache
    {
        AFaire,
        EnCours,
        EnRevue,
        Terminee
    }
    
    // Exemple de Product Backlog pour un projet e-commerce
    public static List<UserStory> GetProductBacklogECommerce()
    {
        return new List<UserStory>
        {
            new UserStory
            {
                Id = "US001",
                Titre = "Inscription utilisateur",
                Persona = "visiteur",
                Objectif = "créer un compte",
                Benefice = "pouvoir passer des commandes",
                StoryPoints = 5,
                Priorite = Priorite.Critique,
                CriteresAcceptation = new List<CritereAcceptation>
                {
                    new() { Description = "L'utilisateur peut saisir email, mot de passe et informations personnelles" },
                    new() { Description = "Un email de confirmation est envoyé" },
                    new() { Description = "Le mot de passe respecte les critères de sécurité" },
                    new() { Description = "Les données sont validées côté client et serveur" }
                }
            },
            new UserStory
            {
                Id = "US002",
                Titre = "Connexion utilisateur",
                Persona = "utilisateur enregistré",
                Objectif = "me connecter à mon compte",
                Benefice = "accéder à mes informations personnelles",
                StoryPoints = 3,
                Priorite = Priorite.Critique,
                CriteresAcceptation = new List<CritereAcceptation>
                {
                    new() { Description = "L'utilisateur peut se connecter avec email/mot de passe" },
                    new() { Description = "Option 'Se souvenir de moi' disponible" },
                    new() { Description = "Lien 'Mot de passe oublié' fonctionnel" },
                    new() { Description = "Redirection vers la page demandée après connexion" }
                }
            },
            new UserStory
            {
                Id = "US003",
                Titre = "Catalogue produits",
                Persona = "visiteur",
                Objectif = "consulter les produits disponibles",
                Benefice = "découvrir l'offre et faire mon choix",
                StoryPoints = 8,
                Priorite = Priorite.Haute,
                CriteresAcceptation = new List<CritereAcceptation>
                {
                    new() { Description = "Affichage en grille avec images, prix et nom" },
                    new() { Description = "Filtres par catégorie, prix, marque" },
                    new() { Description = "Tri par prix, popularité, nouveauté" },
                    new() { Description = "Pagination des résultats" },
                    new() { Description = "Recherche textuelle" }
                }
            },
            new UserStory
            {
                Id = "US004",
                Titre = "Panier d'achat",
                Persona = "utilisateur",
                Objectif = "ajouter des produits à mon panier",
                Benefice = "préparer ma commande",
                StoryPoints = 5,
                Priorite = Priorite.Haute,
                CriteresAcceptation = new List<CritereAcceptation>
                {
                    new() { Description = "Bouton 'Ajouter au panier' sur chaque produit" },
                    new() { Description = "Modification des quantités dans le panier" },
                    new() { Description = "Suppression d'articles du panier" },
                    new() { Description = "Calcul automatique du total" },
                    new() { Description = "Persistance du panier entre les sessions" }
                }
            }
        };
    }
}
```

### 1.2 Outils de gestion de projet

#### 📊 **Tableau Kanban**

```html
<!-- Exemple de tableau Kanban en HTML/CSS -->
<!DOCTYPE html>
<html>
<head>
    <title>Tableau Kanban - Projet BTS</title>
    <style>
        .kanban-board {
            display: flex;
            gap: 20px;
            padding: 20px;
            background-color: #f5f5f5;
            min-height: 100vh;
        }
        
        .kanban-column {
            flex: 1;
            background-color: #e3e3e3;
            border-radius: 8px;
            padding: 15px;
            min-height: 500px;
        }
        
        .column-header {
            font-weight: bold;
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        
        .kanban-card {
            background-color: white;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .kanban-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .card-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .card-assignee {
            font-size: 0.8em;
            color: #666;
            margin-top: 5px;
        }
        
        .card-priority {
            display: inline-block;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.7em;
            font-weight: bold;
        }
        
        .priority-high { background-color: #ff6b6b; color: white; }
        .priority-medium { background-color: #ffd93d; color: black; }
        .priority-low { background-color: #6bcf7f; color: white; }
        
        .story-points {
            float: right;
            background-color: #007bff;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            text-align: center;
            font-size: 0.8em;
            line-height: 20px;
        }
    </style>
</head>
<body>
    <div class="kanban-board">
        <!-- Colonne À faire -->
        <div class="kanban-column">
            <div class="column-header">À FAIRE</div>
            
            <div class="kanban-card">
                <div class="card-title">US005 - Système de paiement</div>
                <div class="card-description">Intégration PayPal et Stripe</div>
                <span class="card-priority priority-high">HAUTE</span>
                <span class="story-points">8</span>
                <div class="card-assignee">Assigné à: Marie</div>
            </div>
            
            <div class="kanban-card">
                <div class="card-title">US006 - Gestion commandes</div>
                <div class="card-description">Interface admin pour les commandes</div>
                <span class="card-priority priority-medium">MOYENNE</span>
                <span class="story-points">5</span>
                <div class="card-assignee">Assigné à: Pierre</div>
            </div>
        </div>
        
        <!-- Colonne En cours -->
        <div class="kanban-column">
            <div class="column-header">EN COURS</div>
            
            <div class="kanban-card">
                <div class="card-title">US003 - Catalogue produits</div>
                <div class="card-description">Affichage et filtres</div>
                <span class="card-priority priority-high">HAUTE</span>
                <span class="story-points">8</span>
                <div class="card-assignee">Assigné à: Julie</div>
            </div>
            
            <div class="kanban-card">
                <div class="card-title">US004 - Panier d'achat</div>
                <div class="card-description">Gestion du panier utilisateur</div>
                <span class="card-priority priority-high">HAUTE</span>
                <span class="story-points">5</span>
                <div class="card-assignee">Assigné à: Thomas</div>
            </div>
        </div>
        
        <!-- Colonne En test -->
        <div class="kanban-column">
            <div class="column-header">EN TEST</div>
            
            <div class="kanban-card">
                <div class="card-title">US002 - Connexion utilisateur</div>
                <div class="card-description">Authentification et sécurité</div>
                <span class="card-priority priority-high">HAUTE</span>
                <span class="story-points">3</span>
                <div class="card-assignee">Assigné à: Alex</div>
            </div>
        </div>
        
        <!-- Colonne Terminé -->
        <div class="kanban-column">
            <div class="column-header">TERMINÉ</div>
            
            <div class="kanban-card">
                <div class="card-title">US001 - Inscription utilisateur</div>
                <div class="card-description">Création de compte</div>
                <span class="card-priority priority-high">HAUTE</span>
                <span class="story-points">5</span>
                <div class="card-assignee">Assigné à: Sarah</div>
            </div>
        </div>
    </div>
</body>
</html>
```

---

## 🤝 Chapitre 2 : Travail en équipe et collaboration

### 2.1 Gestion de version avec Git

#### 🌿 **Workflow Git Flow**

```bash
# Structure des branches Git Flow

# Branches principales
main/master     # Code en production
develop         # Code en développement

# Branches de fonctionnalités
feature/US001-inscription-utilisateur
feature/US003-catalogue-produits
feature/US004-panier-achat

# Branches de release
release/v1.0.0
release/v1.1.0

# Branches de hotfix
hotfix/fix-paiement-critique
```

**Commandes Git Flow** :

```bash
# Initialisation Git Flow
git flow init

# Démarrer une nouvelle fonctionnalité
git flow feature start US001-inscription-utilisateur

# Travailler sur la fonctionnalité
git add .
git commit -m "feat: ajout formulaire inscription"
git commit -m "feat: validation côté client"
git commit -m "feat: intégration API inscription"

# Terminer la fonctionnalité
git flow feature finish US001-inscription-utilisateur

# Démarrer une release
git flow release start v1.0.0

# Corrections de bugs en release
git commit -m "fix: validation email inscription"
git commit -m "fix: message d'erreur plus clair"

# Terminer la release
git flow release finish v1.0.0

# Hotfix critique
git flow hotfix start fix-paiement-critique
git commit -m "hotfix: correction calcul TVA"
git flow hotfix finish fix-paiement-critique
```

#### 📝 **Conventions de commit**

```bash
# Format: type(scope): description

# Types de commits
feat:     # Nouvelle fonctionnalité
fix:      # Correction de bug
docs:     # Documentation
style:    # Formatage, point-virgules manquants, etc.
refactor: # Refactoring du code
test:     # Ajout de tests
chore:    # Maintenance

# Exemples
git commit -m "feat(auth): ajout authentification JWT"
git commit -m "fix(cart): correction calcul total panier"
git commit -m "docs(api): documentation endpoints utilisateur"
git commit -m "test(payment): ajout tests unitaires paiement"
git commit -m "refactor(database): optimisation requêtes produits"
git commit -m "style(frontend): correction indentation composants"
git commit -m "chore(deps): mise à jour dépendances npm"
```

### 2.2 Code Review et qualité

#### 🔍 **Checklist de Code Review**

```markdown
# Checklist Code Review - BTS SIO SLAM

## ✅ Fonctionnalité
- [ ] Le code implémente correctement la user story
- [ ] Tous les critères d'acceptation sont respectés
- [ ] Les cas d'erreur sont gérés
- [ ] Les validations sont en place

## 🏗️ Architecture
- [ ] Le code respecte l'architecture définie
- [ ] Les responsabilités sont bien séparées
- [ ] Les patterns utilisés sont appropriés
- [ ] Pas de couplage fort

## 🔒 Sécurité
- [ ] Validation des entrées utilisateur
- [ ] Protection contre les injections SQL
- [ ] Gestion sécurisée des mots de passe
- [ ] Autorisation et authentification
- [ ] Pas de données sensibles en dur

## 🚀 Performance
- [ ] Pas de requêtes N+1
- [ ] Utilisation appropriée du cache
- [ ] Optimisation des requêtes base de données
- [ ] Gestion mémoire correcte

## 🧪 Tests
- [ ] Tests unitaires présents et pertinents
- [ ] Couverture de code suffisante
- [ ] Tests d'intégration si nécessaire
- [ ] Tous les tests passent

## 📖 Documentation
- [ ] Code auto-documenté (noms explicites)
- [ ] Commentaires pour la logique complexe
- [ ] Documentation API mise à jour
- [ ] README mis à jour si nécessaire

## 🎨 Style
- [ ] Respect des conventions de nommage
- [ ] Indentation et formatage corrects
- [ ] Pas de code mort ou commenté
- [ ] Longueur des méthodes raisonnable
```

#### 🤖 **Automatisation avec GitHub Actions**

```yaml
# .github/workflows/code-quality.yml
name: Code Quality Check

on:
  pull_request:
    branches: [ develop, main ]

jobs:
  code-quality:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: '6.0.x'
        
    - name: Restore dependencies
      run: dotnet restore
      
    - name: Build
      run: dotnet build --no-restore --configuration Release
      
    - name: Run tests
      run: |
        dotnet test --no-build --configuration Release \
          --collect:"XPlat Code Coverage" \
          --results-directory ./coverage
          
    - name: Code Coverage Report
      uses: codecov/codecov-action@v3
      with:
        directory: ./coverage
        fail_ci_if_error: true
        
    - name: SonarCloud Analysis
      uses: SonarSource/sonarcloud-github-action@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        
    - name: Quality Gate Check
      run: |
        # Vérification que la couverture de code est > 80%
        # Vérification qu'il n'y a pas de bugs critiques
        # Vérification de la dette technique
        
    - name: Comment PR
      uses: actions/github-script@v6
      with:
        script: |
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: '✅ Code quality checks passed! Ready for review.'
          })
```

---

## 🏢 Chapitre 3 : Préparation au stage

### 3.1 Recherche de stage

#### 📋 **Profil de poste - Développeur SLAM**

```markdown
# Profil de Poste - Stagiaire Développeur SLAM

## 🎯 Missions principales

### Développement d'applications
- Participation au développement d'applications web/mobile
- Implémentation de nouvelles fonctionnalités
- Correction de bugs et maintenance
- Tests et validation des développements

### Analyse et conception
- Participation à l'analyse des besoins utilisateurs
- Rédaction de spécifications techniques
- Conception de bases de données
- Modélisation UML

### Collaboration équipe
- Participation aux réunions d'équipe (daily, sprint planning)
- Code review et pair programming
- Documentation technique
- Veille technologique

## 🛠️ Compétences techniques recherchées

### Langages de programmation
- C# / .NET Core (indispensable)
- JavaScript / TypeScript
- SQL (SQL Server, MySQL, PostgreSQL)
- HTML5 / CSS3

### Frameworks et technologies
- ASP.NET Core MVC / Web API
- Entity Framework Core
- React / Angular / Vue.js (un au choix)
- Bootstrap / Tailwind CSS

### Outils de développement
- Visual Studio / VS Code
- Git / GitHub / GitLab
- Postman / Swagger
- Docker (notions)

### Méthodologies
- Agile / Scrum
- DevOps (notions)
- Tests unitaires
- CI/CD (notions)

## 🎓 Profil recherché

### Formation
- BTS SIO option SLAM (1ère ou 2ème année)
- Passion pour le développement
- Projets personnels appréciés

### Qualités personnelles
- Curiosité et envie d'apprendre
- Autonomie et prise d'initiative
- Esprit d'équipe
- Rigueur et organisation
- Communication

## 📈 Évolution possible
- Développeur Junior après le BTS
- Spécialisation (Frontend, Backend, Full-Stack)
- Lead Developer (avec expérience)
- Chef de projet technique
```

#### 📧 **Modèle de lettre de motivation**

```markdown
# Lettre de Motivation - Stage BTS SIO SLAM

[Vos coordonnées]
[Date]

[Coordonnées entreprise]

Objet : Candidature pour un stage de développeur SLAM

Madame, Monsieur,

Actuellement en [1ère/2ème] année de BTS SIO option SLAM au [nom établissement], je suis à la recherche d'un stage de [durée] semaines dans le domaine du développement d'applications.

## Pourquoi cette entreprise ?

Votre entreprise m'intéresse particulièrement car [raisons spécifiques] :
- Secteur d'activité en adéquation avec mes intérêts
- Technologies utilisées correspondant à ma formation
- Réputation d'innovation et de qualité
- Opportunités d'apprentissage

## Mes compétences

Au cours de ma formation, j'ai acquis des compétences en :
- **Développement** : C#/.NET Core, JavaScript, SQL
- **Frameworks** : ASP.NET Core, Entity Framework
- **Outils** : Visual Studio, Git, Postman
- **Méthodologies** : Agile/Scrum, tests unitaires

## Mes projets

J'ai réalisé plusieurs projets qui démontrent mes compétences :
- **[Nom projet 1]** : Application e-commerce avec panier et paiement
- **[Nom projet 2]** : API REST pour gestion de bibliothèque
- **[Nom projet 3]** : Site web responsive avec CMS

[Détailler 1-2 projets les plus pertinents]

## Ma motivation

Ce stage représente pour moi l'opportunité de :
- Mettre en pratique mes connaissances théoriques
- Découvrir le monde professionnel du développement
- Apprendre de développeurs expérimentés
- Contribuer concrètement aux projets de l'entreprise

## Mes qualités

- **Curiosité** : Veille technologique constante
- **Autonomie** : Capable de chercher des solutions
- **Collaboration** : Expérience du travail en équipe
- **Rigueur** : Respect des bonnes pratiques de développement

Je serais ravi de vous rencontrer pour discuter de cette opportunité et vous présenter plus en détail mes motivations et compétences.

Je vous remercie de l'attention que vous porterez à ma candidature et reste à votre disposition pour tout complément d'information.

Cordialement,
[Votre nom]

Pièces jointes :
- CV
- Portfolio de projets
- Relevés de notes
```

### 3.2 Préparation technique

#### 💼 **Portfolio de projets**

```html
<!-- Structure d'un portfolio web -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - [Votre Nom] - Développeur SLAM</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <!-- Header -->
    <header class="bg-primary text-white py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-8">
                    <h1 class="display-4">[Votre Nom]</h1>
                    <p class="lead">Étudiant BTS SIO SLAM - Développeur Full-Stack</p>
                    <p>Passionné par le développement d'applications web modernes et performantes</p>
                </div>
                <div class="col-md-4 text-center">
                    <img src="photo-profil.jpg" alt="Photo" class="rounded-circle img-fluid" style="max-width: 200px;">
                </div>
            </div>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                    <li class="nav-item"><a class="nav-link" href="#about">À propos</a></li>
                    <li class="nav-item"><a class="nav-link" href="#skills">Compétences</a></li>
                    <li class="nav-item"><a class="nav-link" href="#projects">Projets</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Section À propos -->
    <section id="about" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">À propos de moi</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <p class="lead text-center">
                        Étudiant en 2ème année de BTS SIO option SLAM, je suis passionné par le développement 
                        d'applications web et mobile. Mon objectif est de devenir un développeur full-stack 
                        capable de créer des solutions innovantes et performantes.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Compétences -->
    <section id="skills" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">Compétences Techniques</h2>
            <div class="row">
                <div class="col-md-6">
                    <h4><i class="fas fa-code"></i> Langages</h4>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>C# / .NET Core</span>
                            <span>90%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 90%"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>JavaScript / TypeScript</span>
                            <span>80%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 80%"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>SQL</span>
                            <span>85%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 85%"></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <h4><i class="fas fa-tools"></i> Technologies</h4>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>ASP.NET Core</span>
                            <span>85%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 85%"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>React</span>
                            <span>75%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 75%"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>Entity Framework</span>
                            <span>80%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" style="width: 80%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Projets -->
    <section id="projects" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Mes Projets</h2>
            <div class="row">
                <!-- Projet 1 -->
                <div class="col-lg-4 mb-4">
                    <div class="card h-100">
                        <img src="projet1-screenshot.jpg" class="card-img-top" alt="Projet E-commerce">
                        <div class="card-body">
                            <h5 class="card-title">E-commerce "TechStore"</h5>
                            <p class="card-text">
                                Application e-commerce complète avec gestion des produits, 
                                panier, paiement et interface d'administration.
                            </p>
                            <div class="mb-2">
                                <span class="badge bg-primary">C#</span>
                                <span class="badge bg-secondary">ASP.NET Core</span>
                                <span class="badge bg-success">React</span>
                                <span class="badge bg-info">SQL Server</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="https://github.com/username/techstore" class="btn btn-outline-primary btn-sm">
                                <i class="fab fa-github"></i> Code
                            </a>
                            <a href="https://techstore-demo.com" class="btn btn-primary btn-sm">
                                <i class="fas fa-external-link-alt"></i> Démo
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Projet 2 -->
                <div class="col-lg-4 mb-4">
                    <div class="card h-100">
                        <img src="projet2-screenshot.jpg" class="card-img-top" alt="API Bibliothèque">
                        <div class="card-body">
                            <h5 class="card-title">API Gestion Bibliothèque</h5>
                            <p class="card-text">
                                API REST pour la gestion d'une bibliothèque avec authentification JWT, 
                                gestion des emprunts et système de réservation.
                            </p>
                            <div class="mb-2">
                                <span class="badge bg-primary">C#</span>
                                <span class="badge bg-secondary">Web API</span>
                                <span class="badge bg-warning">JWT</span>
                                <span class="badge bg-info">PostgreSQL</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="https://github.com/username/library-api" class="btn btn-outline-primary btn-sm">
                                <i class="fab fa-github"></i> Code
                            </a>
                            <a href="https://library-api-docs.com" class="btn btn-primary btn-sm">
                                <i class="fas fa-book"></i> Documentation
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Projet 3 -->
                <div class="col-lg-4 mb-4">
                    <div class="card h-100">
                        <img src="projet3-screenshot.jpg" class="card-img-top" alt="Application Mobile">
                        <div class="card-body">
                            <h5 class="card-title">App Mobile "TaskManager"</h5>
                            <p class="card-text">
                                Application mobile de gestion de tâches avec synchronisation cloud, 
                                notifications push et mode hors-ligne.
                            </p>
                            <div class="mb-2">
                                <span class="badge bg-primary">C#</span>
                                <span class="badge bg-secondary">Xamarin</span>
                                <span class="badge bg-success">Azure</span>
                                <span class="badge bg-info">SQLite</span>
                            </div>
                        </div>
                        <div class="card-footer">
                            <a href="https://github.com/username/taskmanager-mobile" class="btn btn-outline-primary btn-sm">
                                <i class="fab fa-github"></i> Code
                            </a>
                            <a href="https://play.google.com/store/apps/details?id=com.taskmanager" class="btn btn-primary btn-sm">
                                <i class="fab fa-google-play"></i> Play Store
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Contact -->
    <section id="contact" class="py-5 bg-dark text-white">
        <div class="container">
            <h2 class="text-center mb-5">Contact</h2>
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="row">
                        <div class="col-md-6 text-center mb-4">
                            <i class="fas fa-envelope fa-2x mb-3"></i>
                            <h5>Email</h5>
                            <p>votre.email@example.com</p>
                        </div>
                        <div class="col-md-6 text-center mb-4">
                            <i class="fab fa-linkedin fa-2x mb-3"></i>
                            <h5>LinkedIn</h5>
                            <p>linkedin.com/in/votre-profil</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6 text-center mb-4">
                            <i class="fab fa-github fa-2x mb-3"></i>
                            <h5>GitHub</h5>
                            <p>github.com/votre-username</p>
                        </div>
                        <div class="col-md-6 text-center mb-4">
                            <i class="fas fa-phone fa-2x mb-3"></i>
                            <h5>Téléphone</h5>
                            <p>+33 X XX XX XX XX</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-secondary text-white text-center py-3">
        <div class="container">
            <p>&copy; 2024 [Votre Nom] - Portfolio BTS SIO SLAM</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## 🎤 Chapitre 4 : Soutenance et présentation

### 4.1 Structure de la soutenance

#### 📋 **Plan type de soutenance (20 minutes)**

```markdown
# Plan de Soutenance BTS SIO SLAM

## 1. Introduction (2 minutes)
- Présentation personnelle
- Contexte du stage/projet
- Plan de la présentation

## 2. Présentation de l'entreprise (3 minutes)
- Secteur d'activité
- Taille et organisation
- Équipe informatique
- Technologies utilisées

## 3. Missions et projets (10 minutes)

### Projet principal (7 minutes)
- **Contexte et enjeux**
  - Problématique métier
  - Objectifs du projet
  - Contraintes techniques

- **Solution développée**
  - Architecture technique
  - Technologies choisies
  - Fonctionnalités implémentées
  - Démonstration (3-4 minutes)

- **Difficultés rencontrées**
  - Problèmes techniques
  - Solutions apportées
  - Apprentissages

### Autres missions (3 minutes)
- Maintenance et corrections
- Participation aux projets équipe
- Veille technologique

## 4. Compétences développées (3 minutes)
- Compétences techniques acquises
- Compétences transversales
- Évolution personnelle

## 5. Conclusion (2 minutes)
- Bilan du stage
- Apports pour la formation
- Perspectives d'avenir

## Questions du jury (10 minutes)
- Préparation aux questions techniques
- Questions sur les choix d'architecture
- Questions sur les difficultés
- Questions sur l'évolution professionnelle
```

#### 🎯 **Conseils pour la présentation**

```markdown
# Conseils pour une Soutenance Réussie

## 🎨 Support visuel

### Slides efficaces
- **Maximum 15-20 slides** pour 20 minutes
- **1 idée par slide** - pas de surcharge
- **Visuels** : schémas, captures d'écran, diagrammes
- **Police lisible** : minimum 24pt
- **Couleurs contrastées** pour la lisibilité
- **Numérotation** des slides

### Éléments indispensables
- **Slide de titre** avec nom, formation, entreprise
- **Plan** de la présentation
- **Schéma d'architecture** du projet principal
- **Captures d'écran** de l'application
- **Code source** (extraits pertinents)
- **Slide de conclusion** avec bilan

## 🗣️ Expression orale

### Préparation
- **Répéter** la présentation plusieurs fois
- **Chronométrer** chaque partie
- **Préparer** les transitions entre slides
- **Anticiper** les questions du jury

### Pendant la soutenance
- **Regarder** le jury, pas l'écran
- **Parler** clairement et pas trop vite
- **Utiliser** un vocabulaire technique approprié
- **Expliquer** les acronymes et concepts
- **Montrer** son enthousiasme

## 💻 Démonstration technique

### Préparation
- **Tester** la démo plusieurs fois
- **Préparer** des captures d'écran de secours
- **Scénariser** le parcours utilisateur
- **Prévoir** les cas d'erreur

### Pendant la démo
- **Expliquer** ce qu'on fait avant de le faire
- **Montrer** les fonctionnalités clés
- **Mettre en valeur** les aspects techniques
- **Rester calme** en cas de problème

## ❓ Gestion des questions

### Types de questions fréquentes
- **Techniques** : "Pourquoi avoir choisi cette technologie ?"
- **Méthodologiques** : "Comment avez-vous géré les tests ?"
- **Personnelles** : "Qu'avez-vous appris ?"
- **Prospectives** : "Comment améliorer le projet ?"

### Stratégies de réponse
- **Écouter** attentivement la question
- **Reformuler** si nécessaire
- **Répondre** de manière structurée
- **Donner des exemples** concrets
- **Avouer** si on ne sait pas (et proposer de chercher)
```

### 4.2 Évaluation et critères

#### 📊 **Grille d'évaluation type**

```markdown
# Grille d'Évaluation Soutenance BTS SIO SLAM

## 📋 Présentation du projet (40 points)

### Contexte et enjeux (10 points)
- [ ] Présentation claire de l'entreprise (2 pts)
- [ ] Explication du contexte métier (3 pts)
- [ ] Identification des enjeux (3 pts)
- [ ] Définition des objectifs (2 pts)

### Solution technique (20 points)
- [ ] Architecture cohérente et justifiée (5 pts)
- [ ] Choix technologiques pertinents (5 pts)
- [ ] Fonctionnalités implémentées (5 pts)
- [ ] Qualité du code présenté (5 pts)

### Démonstration (10 points)
- [ ] Fonctionnement de l'application (4 pts)
- [ ] Scénarios d'usage pertinents (3 pts)
- [ ] Gestion des cas d'erreur (3 pts)

## 🎤 Qualité de la présentation (30 points)

### Support visuel (10 points)
- [ ] Slides claires et lisibles (3 pts)
- [ ] Schémas et visuels pertinents (3 pts)
- [ ] Structure logique (2 pts)
- [ ] Respect du temps (2 pts)

### Expression orale (20 points)
- [ ] Clarté de l'expression (5 pts)
- [ ] Vocabulaire technique approprié (5 pts)
- [ ] Aisance et confiance (5 pts)
- [ ] Interaction avec le jury (5 pts)

## 🧠 Maîtrise technique (30 points)

### Compétences développées (15 points)
- [ ] Compétences techniques acquises (8 pts)
- [ ] Compétences transversales (4 pts)
- [ ] Capacité d'adaptation (3 pts)

### Réponses aux questions (15 points)
- [ ] Pertinence des réponses (5 pts)
- [ ] Justification des choix (5 pts)
- [ ] Capacité d'analyse critique (5 pts)

## 🎯 Total : /100 points

### Barème de notation
- **90-100** : Excellent (18-20/20)
- **80-89** : Très bien (16-17/20)
- **70-79** : Bien (14-15/20)
- **60-69** : Assez bien (12-13/20)
- **50-59** : Passable (10-11/20)
- **< 50** : Insuffisant (< 10/20)
```

---

## 🛠️ Travaux pratiques

### TP 1 : Planification de projet Agile

**Objectif** : Créer un backlog produit et planifier 3 sprints

**Livrables** :
- Product backlog avec user stories
- Sprint planning pour 3 sprints
- Tableau Kanban
- Burndown chart

### TP 2 : Simulation de soutenance

**Objectif** : Préparer et présenter un projet en conditions réelles

**Étapes** :
1. Préparation du support de présentation
2. Répétition chronométrée
3. Soutenance devant la classe
4. Évaluation par les pairs

---

## 📖 Ressources complémentaires

### 📚 Documentation
- [Guide Scrum](https://scrumguides.org/)
- [Atlassian Agile](https://www.atlassian.com/agile)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)

### 🔧 Outils
- [Jira](https://www.atlassian.com/software/jira) - Gestion de projet
- [Trello](https://trello.com/) - Kanban simple
- [GitHub Projects](https://github.com/features/project-management/) - Intégré Git
- [Figma](https://www.figma.com/) - Maquettage

---

## ✅ Évaluation

### 📝 Contrôle continu (40%)
- Gestion de projet fil rouge
- Participation aux code reviews
- Présentation d'avancement

### 🎯 Soutenance finale (60%)
- Présentation du projet de stage
- Démonstration technique
- Questions du jury
- Rapport de stage

---

*Ce cours fait partie du **BTS SIO option SLAM** - Module Projets & Stage*