# Guide d'Installation FoxShelter

## 📋 Table des Matières

1. [Prérequis Système](#prérequis-système)
2. [Installation des Outils](#installation-des-outils)
3. [Configuration de l'Environnement](#configuration-de-lenvironnement)
4. [Installation du Projet](#installation-du-projet)
5. [Configuration de la Base de Données](#configuration-de-la-base-de-données)
6. [Premier Lancement](#premier-lancement)
7. [Vérification de l'Installation](#vérification-de-linstallation)
8. [Dépannage](#dépannage)
9. [Configuration Avancée](#configuration-avancée)

## 💻 Prérequis Système

### Configuration Minimale

- **OS** : Windows 10/11, macOS 10.15+, ou Linux (Ubuntu 18.04+)
- **RAM** : 4 GB minimum, 8 GB recommandé
- **Stockage** : 2 GB d'espace libre
- **Processeur** : x64 compatible

### Configuration Recommandée

- **OS** : Windows 11 ou macOS 12+
- **RAM** : 16 GB
- **Stockage** : SSD avec 10 GB d'espace libre
- **Processeur** : Intel i5/AMD Ryzen 5 ou supérieur

## 🛠️ Installation des Outils

### 1. Visual Studio 2022

#### Windows
1. Télécharger [Visual Studio 2022 Community](https://visualstudio.microsoft.com/fr/vs/community/)
2. Lancer l'installateur
3. Sélectionner les charges de travail :
   - **Développement web et ASP.NET**
   - **Développement .NET Desktop**
   - **Stockage et traitement des données**

#### Composants Requis
- .NET 8.0 SDK
- Entity Framework Core Tools
- SQL Server Express LocalDB
- Git pour Windows

### 2. .NET 8 SDK

#### Vérification de l'Installation
```bash
dotnet --version
```

#### Installation Manuelle
Si .NET 8 n'est pas installé :

**Windows :**
```powershell
# Via winget
winget install Microsoft.DotNet.SDK.8

# Ou télécharger depuis https://dotnet.microsoft.com/download
```

**macOS :**
```bash
# Via Homebrew
brew install --cask dotnet-sdk

# Ou télécharger depuis https://dotnet.microsoft.com/download
```

**Linux (Ubuntu) :**
```bash
# Ajouter le repository Microsoft
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

# Installer .NET 8
sudo apt-get update
sudo apt-get install -y dotnet-sdk-8.0
```

### 3. SQL Server

#### Option A : SQL Server Express LocalDB (Recommandé)

**Windows :**
- Inclus avec Visual Studio 2022
- Ou télécharger [SQL Server Express](https://www.microsoft.com/fr-fr/sql-server/sql-server-downloads)

**Vérification :**
```cmd
sqllocaldb info
```

#### Option B : SQL Server Express

**Windows :**
1. Télécharger [SQL Server Express](https://www.microsoft.com/fr-fr/sql-server/sql-server-downloads)
2. Installer avec les options par défaut
3. Noter l'instance : `.\SQLEXPRESS`

#### Option C : SQL Server Developer (Gratuit)

Pour un environnement de développement complet :
1. Télécharger [SQL Server Developer](https://www.microsoft.com/fr-fr/sql-server/sql-server-downloads)
2. Installer SQL Server Management Studio (SSMS)

### 4. Git

#### Installation
**Windows :**
```powershell
winget install Git.Git
```

**macOS :**
```bash
brew install git
```

**Linux :**
```bash
sudo apt-get install git
```

#### Configuration Initiale
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

## ⚙️ Configuration de l'Environnement

### 1. Variables d'Environnement

#### Windows
```cmd
# Ajouter .NET CLI aux variables PATH (généralement automatique)
setx PATH "%PATH%;C:\Program Files\dotnet"
```

#### macOS/Linux
```bash
# Ajouter à ~/.bashrc ou ~/.zshrc
export PATH="$PATH:/usr/local/share/dotnet"
export DOTNET_ROOT="/usr/local/share/dotnet"
```

### 2. Vérification des Outils

```bash
# Vérifier .NET
dotnet --version
dotnet --list-sdks

# Vérifier Entity Framework Tools
dotnet ef --version

# Vérifier Git
git --version

# Vérifier SQL Server LocalDB (Windows)
sqllocaldb info
```

## 📦 Installation du Projet

### 1. Cloner le Repository

```bash
# Créer un dossier de travail
mkdir C:\Dev\FoxShelter  # Windows
mkdir ~/Dev/FoxShelter   # macOS/Linux

# Naviguer vers le dossier
cd C:\Dev\FoxShelter     # Windows
cd ~/Dev/FoxShelter      # macOS/Linux

# Cloner le projet (remplacer par l'URL réelle)
git clone https://github.com/votre-repo/foxshelter.git .
```

### 2. Restaurer les Packages NuGet

```bash
# Naviguer vers le dossier du projet
cd FoxShelter

# Restaurer les dépendances
dotnet restore

# Vérifier la restauration
dotnet list package
```

### 3. Vérifier la Structure du Projet

```
FoxShelter/
├── Controllers/
├── Models/
├── Views/
├── Services/
├── Data/
├── wwwroot/
├── FoxShelter.csproj
├── Program.cs
└── appsettings.json
```

## 🗄️ Configuration de la Base de Données

### 1. Configuration de la Chaîne de Connexion

#### Option A : SQL Server LocalDB (Par défaut)

Le fichier `appsettings.json` contient déjà :
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
    "DefaultConnection": "Server=localhost;Database=FoxShelterDB;User Id=sa;Password=VotreMotDePasse;TrustServerCertificate=true;MultipleActiveResultSets=true"
  }
}
```

### 2. Installation des Outils Entity Framework

```bash
# Installer les outils EF globalement
dotnet tool install --global dotnet-ef

# Vérifier l'installation
dotnet ef --version
```

### 3. Création de la Base de Données

#### Méthode 1 : Migrations Entity Framework

```bash
# Créer la migration initiale (si pas déjà fait)
dotnet ef migrations add InitialCreate

# Appliquer les migrations
dotnet ef database update

# Vérifier les migrations
dotnet ef migrations list
```

#### Méthode 2 : Script SQL Manuel

Si vous préférez créer la base manuellement :

```sql
-- Se connecter à SQL Server et exécuter :
CREATE DATABASE FoxShelterDB;
GO

USE FoxShelterDB;
GO

-- Les tables seront créées automatiquement au premier lancement
```

### 4. Vérification de la Base de Données

#### Via SQL Server Management Studio (Windows)
1. Ouvrir SSMS
2. Se connecter à `(localdb)\mssqllocaldb` ou `.\SQLEXPRESS`
3. Vérifier que la base `FoxShelterDB` existe
4. Vérifier les tables créées

#### Via Ligne de Commande
```bash
# Lister les bases LocalDB
sqllocaldb info mssqllocaldb

# Tester la connexion
dotnet ef database update --verbose
```

## 🚀 Premier Lancement

### 1. Compilation du Projet

```bash
# Compiler le projet
dotnet build

# Vérifier qu'il n'y a pas d'erreurs
echo $?  # Doit retourner 0 (Linux/macOS)
echo %ERRORLEVEL%  # Doit retourner 0 (Windows)
```

### 2. Lancement en Mode Développement

```bash
# Lancer l'application
dotnet run

# Ou avec rechargement automatique
dotnet watch run
```

### 3. Accès à l'Application

L'application sera accessible aux adresses :
- **HTTPS** : https://localhost:5001
- **HTTP** : http://localhost:5000

### 4. Vérification du Lancement

Vous devriez voir dans la console :
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shutdown.
```

## ✅ Vérification de l'Installation

### 1. Tests de Base

#### Page d'Accueil
1. Ouvrir https://localhost:5001
2. Vérifier que la page d'accueil s'affiche
3. Vérifier les statistiques (peuvent être à 0)

#### Navigation
1. Cliquer sur "Renards" dans le menu
2. Vérifier que la liste s'affiche (vide au début)
3. Cliquer sur "Nouveau renard"
4. Vérifier que le formulaire s'affiche

#### Base de Données
1. Ajouter un renard de test
2. Vérifier qu'il apparaît dans la liste
3. Modifier ses informations
4. Vérifier la persistance des données

### 2. Tests Fonctionnels

```bash
# Exécuter les tests unitaires (si disponibles)
dotnet test

# Vérifier les logs
# Les logs sont dans le dossier Logs/ (si configuré)
```

### 3. Vérification des Ressources

#### CSS et JavaScript
1. Ouvrir les outils de développement (F12)
2. Vérifier qu'il n'y a pas d'erreurs 404
3. Vérifier que Bootstrap se charge correctement

#### API
1. Accéder à https://localhost:5001/api/renards
2. Vérifier la réponse JSON (peut être vide)

## 🔧 Dépannage

### Problèmes Courants

#### 1. Erreur "dotnet command not found"

**Solution :**
```bash
# Vérifier l'installation
which dotnet  # macOS/Linux
where dotnet  # Windows

# Réinstaller .NET SDK si nécessaire
```

#### 2. Erreur de Connexion à la Base de Données

**Symptômes :**
```
Microsoft.Data.SqlClient.SqlException: A network-related or instance-specific error occurred
```

**Solutions :**
```bash
# Vérifier LocalDB
sqllocaldb info
sqllocaldb start mssqllocaldb

# Ou modifier la chaîne de connexion
# Utiliser SQL Server Express au lieu de LocalDB
```

#### 3. Erreur de Migration Entity Framework

**Symptômes :**
```
Unable to create an object of type 'FoxShelterContext'
```

**Solutions :**
```bash
# Vérifier la chaîne de connexion
dotnet ef dbcontext info

# Recréer les migrations
dotnet ef migrations remove
dotnet ef migrations add InitialCreate
dotnet ef database update
```

#### 4. Port Déjà Utilisé

**Symptômes :**
```
Unable to bind to https://localhost:5001
```

**Solutions :**
```bash
# Changer les ports dans launchSettings.json
# Ou arrêter le processus utilisant le port
netstat -ano | findstr :5001  # Windows
lsof -i :5001                 # macOS/Linux
```

#### 5. Erreurs de Packages NuGet

**Solutions :**
```bash
# Nettoyer et restaurer
dotnet clean
dotnet restore

# Forcer la restauration
dotnet restore --force
```

### Logs et Diagnostics

#### Activer les Logs Détaillés

Modifier `appsettings.Development.json` :
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Debug",
      "Microsoft.AspNetCore": "Information",
      "Microsoft.EntityFrameworkCore": "Information"
    }
  }
}
```

#### Vérifier les Logs

```bash
# Lancer avec logs verbeux
dotnet run --verbosity detailed

# Ou consulter les logs de l'application
# (si configurés dans Program.cs)
```

## ⚙️ Configuration Avancée

### 1. Configuration Multi-Environnements

#### Développement
```json
// appsettings.Development.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=FoxShelterDB_Dev;Trusted_Connection=true"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Debug"
    }
  }
}
```

#### Production
```json
// appsettings.Production.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=prod-server;Database=FoxShelterDB;User Id=app_user;Password=secure_password"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  }
}
```

### 2. Configuration HTTPS

#### Certificat de Développement
```bash
# Installer le certificat de développement
dotnet dev-certs https --trust
```

#### Configuration Personnalisée
Modifier `Program.cs` pour personnaliser HTTPS :
```csharp
builder.WebHost.ConfigureKestrel(options =>
{
    options.ListenLocalhost(5000);
    options.ListenLocalhost(5001, listenOptions =>
    {
        listenOptions.UseHttps();
    });
});
```

### 3. Configuration de la Base de Données Avancée

#### Pool de Connexions
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=FoxShelterDB;Trusted_Connection=true;MultipleActiveResultSets=true;Max Pool Size=100;Min Pool Size=5"
  }
}
```

#### Timeout et Retry
```csharp
// Dans Program.cs
builder.Services.AddDbContext<FoxShelterContext>(options =>
    options.UseSqlServer(connectionString, sqlOptions =>
    {
        sqlOptions.CommandTimeout(30);
        sqlOptions.EnableRetryOnFailure(3);
    }));
```

### 4. Configuration des Emails (Optionnel)

```json
{
  "EmailSettings": {
    "SmtpServer": "smtp.gmail.com",
    "SmtpPort": 587,
    "SmtpUsername": "votre-email@gmail.com",
    "SmtpPassword": "votre-mot-de-passe-app",
    "EnableSsl": true,
    "FromEmail": "noreply@foxshelter.fr",
    "FromName": "FoxShelter"
  }
}
```

## 📚 Ressources Supplémentaires

### Documentation Officielle
- [ASP.NET Core](https://docs.microsoft.com/aspnet/core/)
- [Entity Framework Core](https://docs.microsoft.com/ef/core/)
- [.NET 8](https://docs.microsoft.com/dotnet/)

### Outils Utiles
- **SQL Server Management Studio** : Gestion de base de données
- **Postman** : Test des APIs
- **Visual Studio Code** : Éditeur léger
- **Git Extensions** : Interface graphique Git

### Communauté
- [Stack Overflow](https://stackoverflow.com/questions/tagged/asp.net-core)
- [GitHub Discussions](https://github.com/dotnet/aspnetcore/discussions)
- [Reddit r/dotnet](https://reddit.com/r/dotnet)

---

## 📞 Support

Si vous rencontrez des problèmes non couverts par ce guide :

1. **Vérifiez** les logs d'erreur
2. **Consultez** la section dépannage
3. **Recherchez** sur Stack Overflow
4. **Créez** une issue sur GitHub

---

*Guide d'installation FoxShelter - Version 1.0*
*Dernière mise à jour : Janvier 2024*