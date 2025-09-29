# FoxShelter - Système de Gestion de Refuge pour Renards

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Fonctionnalités](#fonctionnalités)
3. [Architecture](#architecture)
4. [Prérequis](#prérequis)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Utilisation](#utilisation)
8. [API](#api)
9. [Tests](#tests)
10. [Déploiement](#déploiement)
11. [Maintenance](#maintenance)
12. [Contribution](#contribution)
13. [Support](#support)

## 🦊 Vue d'ensemble

FoxShelter est une application web complète développée en C# .NET 8 avec ASP.NET Core MVC pour la gestion d'un refuge spécialisé dans la protection et le soin des renards. Le système permet de gérer tous les aspects du refuge : renards, personnel, soins vétérinaires, alimentation, dons et adoptions.

### Objectifs du Projet

- **Pédagogique** : Projet complet pour BTS SIO 1 SLAM
- **Pratique** : Application réelle de gestion de refuge
- **Technique** : Démonstration des compétences C# et .NET

### Technologies Utilisées

- **Backend** : C# .NET 8, ASP.NET Core MVC
- **Base de données** : SQL Server avec Entity Framework Core
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Outils** : Visual Studio, SQL Server Management Studio

## 🚀 Fonctionnalités

### Gestion des Renards
- ✅ Enregistrement des nouveaux arrivants
- ✅ Suivi de l'état de santé
- ✅ Gestion des informations personnelles (nom, espèce, âge, sexe)
- ✅ Calcul automatique de la durée de séjour
- ✅ Statut d'adoption
- ✅ Recherche et filtrage avancés

### Gestion Vétérinaire
- ✅ Planification des soins
- ✅ Historique médical complet
- ✅ Gestion des médicaments
- ✅ Suivi des coûts
- ✅ Alertes pour les suivis urgents
- ✅ Rapports médicaux

### Gestion du Personnel
- ✅ Employés et bénévoles
- ✅ Qualifications vétérinaires
- ✅ Planning et disponibilités
- ✅ Suivi des heures de bénévolat
- ✅ Gestion des salaires

### Gestion Alimentaire
- ✅ Régimes alimentaires personnalisés
- ✅ Calcul des coûts nutritionnels
- ✅ Planification des repas
- ✅ Adaptation selon l'âge
- ✅ Régimes médicaux spéciaux

### Gestion des Dons
- ✅ Enregistrement des dons (argent, matériel, nourriture)
- ✅ Génération de reçus fiscaux
- ✅ Dons récurrents
- ✅ Suivi des donateurs
- ✅ Rapports financiers

### Gestion des Adoptions
- ✅ Catalogue des renards adoptables
- ✅ Processus de demande d'adoption
- ✅ Évaluation des candidats
- ✅ Suivi post-adoption
- ✅ Statistiques d'adoption

### Tableaux de Bord et Rapports
- ✅ Statistiques en temps réel
- ✅ Graphiques et indicateurs
- ✅ Alertes automatiques
- ✅ Rapports personnalisables
- ✅ Export des données

## 🏗️ Architecture

### Architecture Générale

```
FoxShelter/
├── Controllers/          # Contrôleurs MVC
├── Models/              # Modèles de données
│   ├── Entities/        # Entités métier
│   ├── Enums/          # Énumérations
│   └── ViewModels/     # Modèles de vue
├── Views/              # Vues Razor
├── Services/           # Services métier
├── Data/               # Contexte Entity Framework
├── wwwroot/            # Ressources statiques
├── Diagrammes/         # Documentation UML
└── Documentation/      # Documentation technique
```

### Couches Applicatives

1. **Présentation** : Contrôleurs MVC et vues Razor
2. **Logique Métier** : Services et règles business
3. **Accès aux Données** : Entity Framework Core
4. **Base de Données** : SQL Server

### Patterns Utilisés

- **MVC (Model-View-Controller)** : Architecture principale
- **Repository Pattern** : Via Entity Framework
- **Service Layer** : Logique métier centralisée
- **Dependency Injection** : Inversion de contrôle
- **Unit of Work** : Gestion des transactions

## 📋 Prérequis

### Logiciels Requis

- **Visual Studio 2022** (Community, Professional ou Enterprise)
- **.NET 8 SDK** ou supérieur
- **SQL Server** (LocalDB, Express ou complet)
- **Git** pour le contrôle de version

### Connaissances Recommandées

- **C#** : Syntaxe de base, POO, LINQ
- **ASP.NET Core MVC** : Contrôleurs, vues, modèles
- **Entity Framework Core** : ORM, migrations
- **SQL** : Requêtes de base
- **HTML/CSS/JavaScript** : Frontend web
- **Bootstrap** : Framework CSS

## 🛠️ Installation

### 1. Cloner le Projet

```bash
git clone https://github.com/votre-repo/foxshelter.git
cd foxshelter
```

### 2. Restaurer les Packages NuGet

```bash
dotnet restore
```

### 3. Configurer la Base de Données

#### Option A : SQL Server LocalDB (Recommandé pour le développement)

La chaîne de connexion par défaut utilise LocalDB :

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=FoxShelterDB;Trusted_Connection=true;MultipleActiveResultSets=true"
  }
}
```

#### Option B : SQL Server Express

Modifier `appsettings.json` :

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=.\\SQLEXPRESS;Database=FoxShelterDB;Trusted_Connection=true;MultipleActiveResultSets=true"
  }
}
```

#### Option C : SQL Server avec Authentification

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=votre-serveur;Database=FoxShelterDB;User Id=votre-utilisateur;Password=votre-mot-de-passe;MultipleActiveResultSets=true"
  }
}
```

### 4. Créer et Initialiser la Base de Données

```bash
# Créer la migration initiale (si pas déjà fait)
dotnet ef migrations add InitialCreate

# Appliquer les migrations
dotnet ef database update
```

### 5. Lancer l'Application

```bash
dotnet run
```

L'application sera accessible à l'adresse : `https://localhost:5001`

## ⚙️ Configuration

### Fichier appsettings.json

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=FoxShelterDB;Trusted_Connection=true;MultipleActiveResultSets=true"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.EntityFrameworkCore": "Information"
    }
  },
  "AllowedHosts": "*",
  "FoxShelter": {
    "NomRefuge": "FoxShelter - Refuge pour Renards",
    "Adresse": "123 Rue de la Forêt, 75001 Paris",
    "Telephone": "01.23.45.67.89",
    "Email": "contact@foxshelter.fr",
    "SiteWeb": "https://www.foxshelter.fr",
    "CapaciteMaximale": 50,
    "HeuresOuverture": {
      "Lundi": "09:00-18:00",
      "Mardi": "09:00-18:00",
      "Mercredi": "09:00-18:00",
      "Jeudi": "09:00-18:00",
      "Vendredi": "09:00-18:00",
      "Samedi": "10:00-16:00",
      "Dimanche": "Fermé"
    },
    "Notifications": {
      "EmailUrgence": "urgence@foxshelter.fr",
      "EmailAdministration": "admin@foxshelter.fr",
      "SeuillAlerteCritique": 5,
      "DelaiRappelSuiviJours": 3
    }
  }
}
```

### Variables d'Environnement

Pour la production, utilisez des variables d'environnement :

```bash
export ConnectionStrings__DefaultConnection="Server=prod-server;Database=FoxShelterDB;..."
export FoxShelter__EmailUrgence="urgence@foxshelter.fr"
```

## 📖 Utilisation

### Interface Utilisateur

#### Page d'Accueil
- **Tableau de bord** avec statistiques principales
- **Alertes** pour les cas urgents
- **Liens rapides** vers les fonctionnalités principales

#### Gestion des Renards
1. **Ajouter un renard** : Formulaire complet avec validation
2. **Consulter la liste** : Tableau avec recherche et filtres
3. **Voir les détails** : Fiche complète avec historique
4. **Modifier les informations** : Mise à jour des données
5. **Marquer comme adopté** : Finalisation de l'adoption

#### Gestion des Soins
1. **Programmer un soin** : Planification avec vétérinaire
2. **Effectuer un soin** : Saisie des détails et observations
3. **Consulter l'historique** : Suivi médical complet
4. **Générer des rapports** : Documents médicaux

### Workflows Principaux

#### Arrivée d'un Nouveau Renard
1. Cliquer sur "Nouveau renard"
2. Remplir le formulaire d'enregistrement
3. Assigner un régime alimentaire
4. Programmer un examen vétérinaire
5. Valider l'enregistrement

#### Processus d'Adoption
1. Consulter les renards adoptables
2. Évaluer la demande d'adoption
3. Organiser une rencontre
4. Finaliser l'adoption
5. Initier le suivi post-adoption

## 🔌 API

### Endpoints Principaux

#### Renards
```
GET    /api/renards              # Liste tous les renards
GET    /api/renards/{id}         # Détails d'un renard
POST   /api/renards              # Créer un nouveau renard
PUT    /api/renards/{id}         # Modifier un renard
DELETE /api/renards/{id}         # Supprimer un renard
GET    /api/renards/urgents      # Renards en état critique
GET    /api/renards/adoptables   # Renards disponibles à l'adoption
```

#### Soins Vétérinaires
```
GET    /api/soins                # Liste tous les soins
POST   /api/soins                # Enregistrer un nouveau soin
GET    /api/soins/renard/{id}    # Historique d'un renard
GET    /api/soins/urgents        # Soins urgents requis
```

#### Statistiques
```
GET    /api/stats/dashboard      # Statistiques du tableau de bord
GET    /api/stats/renards        # Statistiques détaillées des renards
GET    /api/stats/financier      # Rapport financier
```

### Format des Réponses

```json
{
  "success": true,
  "data": {
    "id": 1,
    "nom": "Rusty",
    "espece": "Renard roux",
    "age": 2,
    "sexe": "M",
    "etatSante": "Bon",
    "dateArrivee": "2024-01-15T00:00:00Z"
  },
  "message": "Renard récupéré avec succès"
}
```

## 🧪 Tests

### Tests Unitaires

```bash
# Exécuter tous les tests
dotnet test

# Tests avec couverture
dotnet test --collect:"XPlat Code Coverage"

# Tests spécifiques
dotnet test --filter "Category=Unit"
```

### Tests d'Intégration

```bash
# Tests d'intégration
dotnet test --filter "Category=Integration"
```

### Structure des Tests

```
FoxShelter.Tests/
├── Unit/
│   ├── Services/
│   ├── Controllers/
│   └── Models/
├── Integration/
│   ├── Api/
│   └── Database/
└── Fixtures/
    └── TestData/
```

## 🚀 Déploiement

### Déploiement Local (IIS)

1. **Publier l'application** :
```bash
dotnet publish -c Release -o ./publish
```

2. **Configurer IIS** :
   - Créer un nouveau site web
   - Pointer vers le dossier `publish`
   - Configurer le pool d'applications (.NET Core)

3. **Configurer la base de données** :
   - Créer la base de données de production
   - Exécuter les migrations
   - Configurer la chaîne de connexion

### Déploiement Azure

1. **Azure App Service** :
```bash
# Publier vers Azure
dotnet publish -c Release
az webapp deploy --resource-group myResourceGroup --name myapp --src-path ./bin/Release/net8.0/publish.zip
```

2. **Azure SQL Database** :
   - Créer une base Azure SQL
   - Configurer le firewall
   - Mettre à jour la chaîne de connexion

### Déploiement Docker

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["FoxShelter.csproj", "."]
RUN dotnet restore "./FoxShelter.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "FoxShelter.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FoxShelter.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FoxShelter.dll"]
```

```bash
# Construire l'image
docker build -t foxshelter .

# Lancer le conteneur
docker run -d -p 8080:80 --name foxshelter-app foxshelter
```

## 🔧 Maintenance

### Sauvegardes

#### Base de Données
```sql
-- Sauvegarde complète
BACKUP DATABASE FoxShelterDB 
TO DISK = 'C:\Backups\FoxShelter_Full.bak'

-- Sauvegarde différentielle
BACKUP DATABASE FoxShelterDB 
TO DISK = 'C:\Backups\FoxShelter_Diff.bak'
WITH DIFFERENTIAL
```

#### Fichiers Application
- Sauvegarder le dossier `wwwroot/uploads`
- Sauvegarder les fichiers de configuration
- Sauvegarder les logs

### Monitoring

#### Logs
```csharp
// Configuration dans Program.cs
builder.Logging.AddFile("Logs/foxshelter-{Date}.txt");
```

#### Métriques
- Temps de réponse des pages
- Utilisation de la base de données
- Erreurs applicatives
- Utilisation mémoire

### Mises à Jour

1. **Sauvegarder** l'application et la base de données
2. **Tester** en environnement de développement
3. **Déployer** en mode maintenance
4. **Vérifier** le bon fonctionnement
5. **Remettre** en service

## 🤝 Contribution

### Standards de Code

- **Conventions C#** : PascalCase pour les classes et méthodes
- **Commentaires** : Documentation XML pour les méthodes publiques
- **Tests** : Couverture minimale de 80%
- **Git** : Messages de commit descriptifs

### Processus de Contribution

1. **Fork** le projet
2. **Créer** une branche feature
3. **Développer** avec tests
4. **Tester** localement
5. **Soumettre** une pull request

### Structure des Commits

```
type(scope): description

feat(renards): ajouter recherche par espèce
fix(soins): corriger calcul des coûts
docs(readme): mettre à jour installation
test(services): ajouter tests unitaires
```

## 📞 Support

### Documentation
- **README** : Ce fichier
- **Wiki** : Documentation détaillée
- **API Docs** : Documentation Swagger
- **Diagrammes UML** : Architecture technique

### Contact
- **Email** : support@foxshelter.fr
- **Issues** : GitHub Issues
- **Discussions** : GitHub Discussions

### FAQ

**Q: Comment réinitialiser la base de données ?**
```bash
dotnet ef database drop
dotnet ef database update
```

**Q: Comment ajouter de nouvelles données de test ?**
Modifier la méthode `SeedData()` dans `FoxShelterContext.cs`

**Q: Comment changer le thème de l'interface ?**
Modifier les variables CSS dans `wwwroot/css/site.css`

**Q: Comment configurer les emails ?**
Ajouter la configuration SMTP dans `appsettings.json`

---

## 📄 Licence

Ce projet est développé dans un cadre pédagogique pour le BTS SIO 1 SLAM.

## 🙏 Remerciements

- **Équipe pédagogique** BTS SIO
- **Communauté .NET** pour les ressources
- **Refuges animaliers** pour l'inspiration

---

*Dernière mise à jour : Janvier 2024*