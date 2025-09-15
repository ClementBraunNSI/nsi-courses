<style>
/* Styles modernes pour le cours Projet de Développement */
.course-header {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
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
    color: #3498db;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #3498db;
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
    border-left: 4px solid #3498db;
}

.code-title {
    color: #3498db;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.highlight-fact {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.warning-fact {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.danger-fact {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.methodology-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.methodology-card {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(52, 152, 219, 0.2);
    transition: all 0.3s ease;
}

.methodology-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.methodology-icon {
    font-size: 2rem;
    color: #3498db;
    text-align: center;
    margin-bottom: 1rem;
}

.methodology-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 1rem;
}

.methodology-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    text-align: center;
    line-height: 1.5;
}

.phase-timeline {
    position: relative;
    margin: 2rem 0;
}

.phase-item {
    display: flex;
    align-items: center;
    margin: 1.5rem 0;
    position: relative;
}

.phase-number {
    background: linear-gradient(135deg, #3498db, #9b59b6);
    color: white;
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 1.5rem;
    flex-shrink: 0;
}

.phase-content {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    padding: 1.5rem;
    flex: 1;
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(5px);
}

.phase-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.phase-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.tool-card {
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    color: white;
    font-weight: 600;
    transition: all 0.3s ease;
}

.tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
}

.tool-ide {
    background: linear-gradient(135deg, #007ACC, #42a5f5);
}

.tool-git {
    background: linear-gradient(135deg, #f05032, #ff7043);
}

.tool-database {
    background: linear-gradient(135deg, #336791, #5c6bc0);
}

.tool-testing {
    background: linear-gradient(135deg, #68217a, #9c27b0);
}

.tool-deployment {
    background: linear-gradient(135deg, #0078d4, #2196f3);
}

.tool-monitoring {
    background: linear-gradient(135deg, #ff6b35, #ff9800);
}

.best-practices-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.practice-card {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-left: 4px solid #2ecc71;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}

.practice-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.practice-icon {
    font-size: 2rem;
    color: #2ecc71;
    margin-bottom: 1rem;
}

.practice-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
}

.practice-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .methodology-grid {
        grid-template-columns: 1fr;
    }
    
    .tools-grid {
        grid-template-columns: 1fr;
    }
    
    .best-practices-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
    
    .phase-item {
        flex-direction: column;
        text-align: center;
    }
    
    .phase-number {
        margin-right: 0;
        margin-bottom: 1rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">💻 Projet de Développement</h1>
    <p class="course-subtitle">BTS SIO SLAM - Bloc 1 : Support et mise à disposition de services informatiques</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Qu'est-ce qu'un Projet de Développement ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚀 Définition du Projet de Développement</div>
        <div class="definition-content">
            Un <strong>projet de développement</strong> est une démarche structurée visant à créer une solution logicielle répondant à un besoin spécifique. Il implique la planification, la conception, le développement, les tests et le déploiement d'une application ou d'un système informatique.
        </div>
    </div>
     
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">Planification</div>
            <div class="concept-description">
                Définition des objectifs, des ressources nécessaires, du planning et des livrables attendus.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎨</div>
            <div class="concept-name">Conception</div>
            <div class="concept-description">
                Élaboration de l'architecture, des maquettes et des spécifications techniques détaillées.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚙️</div>
            <div class="concept-name">Développement</div>
            <div class="concept-description">
                Implémentation du code source selon les spécifications et les bonnes pratiques de développement.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🧪</div>
            <div class="concept-name">Tests</div>
            <div class="concept-description">
                Validation du fonctionnement, détection des bugs et vérification de la conformité aux exigences.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Bon à savoir :</strong> Un projet de développement réussi combine compétences techniques, gestion de projet et communication efficace avec les parties prenantes.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Méthodologies de Gestion de Projet</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔄 Approches Méthodologiques</div>
        <div class="definition-content">
            Les <strong>méthodologies de gestion de projet</strong> fournissent un cadre structuré pour organiser, planifier et contrôler le développement d'un projet informatique. Chaque approche a ses avantages selon le contexte et les contraintes.
        </div>
    </div>
    
    <div class="methodology-grid">
        <div class="methodology-card">
            <div class="methodology-icon">📈</div>
            <div class="methodology-name">Méthode en Cascade</div>
            <div class="methodology-description">
                Approche séquentielle où chaque phase doit être terminée avant de passer à la suivante. Idéale pour les projets aux exigences stables.
            </div>
        </div>
        
        <div class="methodology-card">
            <div class="methodology-icon">🔄</div>
            <div class="methodology-name">Méthode Agile</div>
            <div class="methodology-description">
                Approche itérative et collaborative privilégiant l'adaptation au changement et la livraison continue de valeur.
            </div>
        </div>
        
        <div class="methodology-card">
            <div class="methodology-icon">📋</div>
            <div class="methodology-name">Scrum</div>
            <div class="methodology-description">
                Framework agile organisant le travail en sprints courts avec des rôles définis (Product Owner, Scrum Master, équipe).
            </div>
        </div>
        
        <div class="methodology-card">
            <div class="methodology-icon">🎯</div>
            <div class="methodology-name">Kanban</div>
            <div class="methodology-description">
                Méthode visuelle de gestion des flux de travail basée sur des tableaux et la limitation du travail en cours.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Gestion de Projet Agile en C#</div>
        <pre><code>// Modèle pour la gestion d'un projet Agile
public class AgileProject
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime? EndDate { get; set; }
    public ProjectStatus Status { get; set; }
    public List<Sprint> Sprints { get; set; } = new List<Sprint>();
    public List<UserStory> Backlog { get; set; } = new List<UserStory>();
    public List<TeamMember> Team { get; set; } = new List<TeamMember>();
    
    public Sprint CreateNewSprint(string name, DateTime startDate, DateTime endDate)
    {
        var sprint = new Sprint
        {
            Id = Sprints.Count + 1,
            Name = name,
            StartDate = startDate,
            EndDate = endDate,
            Status = SprintStatus.Planning,
            ProjectId = this.Id
        };
        
        Sprints.Add(sprint);
        return sprint;
    }
    
    public void AddUserStory(string title, string description, int storyPoints, Priority priority)
    {
        var userStory = new UserStory
        {
            Id = Backlog.Count + 1,
            Title = title,
            Description = description,
            StoryPoints = storyPoints,
            Priority = priority,
            Status = UserStoryStatus.New,
            CreatedDate = DateTime.UtcNow
        };
        
        Backlog.Add(userStory);
    }
    
    public List<UserStory> GetPrioritizedBacklog()
    {
        return Backlog
            .Where(us => us.Status != UserStoryStatus.Done)
            .OrderBy(us => us.Priority)
            .ThenByDescending(us => us.StoryPoints)
            .ToList();
    }
    
    public ProjectMetrics CalculateMetrics()
    {
        var completedStories = Backlog.Count(us => us.Status == UserStoryStatus.Done);
        var totalStories = Backlog.Count;
        var completedSprints = Sprints.Count(s => s.Status == SprintStatus.Completed);
        
        return new ProjectMetrics
        {
            CompletionPercentage = totalStories > 0 ? (double)completedStories / totalStories * 100 : 0,
            Velocity = CalculateAverageVelocity(),
            BurndownRate = CalculateBurndownRate(),
            TeamProductivity = CalculateTeamProductivity()
        };
    }
    
    private double CalculateAverageVelocity()
    {
        var completedSprints = Sprints.Where(s => s.Status == SprintStatus.Completed).ToList();
        if (!completedSprints.Any()) return 0;
        
        var totalStoryPoints = completedSprints.Sum(s => s.CompletedStoryPoints);
        return (double)totalStoryPoints / completedSprints.Count;
    }
}

public class Sprint
{
    public int Id { get; set; }
    public string Name { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public SprintStatus Status { get; set; }
    public int ProjectId { get; set; }
    public List<UserStory> UserStories { get; set; } = new List<UserStory>();
    public int CompletedStoryPoints => UserStories.Where(us => us.Status == UserStoryStatus.Done).Sum(us => us.StoryPoints);
    
    public void StartSprint()
    {
        Status = SprintStatus.Active;
        foreach (var story in UserStories)
        {
            if (story.Status == UserStoryStatus.New)
            {
                story.Status = UserStoryStatus.InProgress;
            }
        }
    }
    
    public void CompleteSprint()
    {
        Status = SprintStatus.Completed;
        // Déplacer les stories non terminées vers le backlog
        var incompleteStories = UserStories.Where(us => us.Status != UserStoryStatus.Done).ToList();
        // Logique pour remettre dans le backlog
    }
}

public enum ProjectStatus { Planning, Active, OnHold, Completed, Cancelled }
public enum SprintStatus { Planning, Active, Review, Retrospective, Completed }
public enum UserStoryStatus { New, InProgress, Testing, Done }
public enum Priority { Low = 1, Medium = 2, High = 3, Critical = 4 }</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Phases du Cycle de Développement</h2>
    
    <div class="definition-box">
        <div class="definition-title">📈 Cycle de Vie du Développement Logiciel (SDLC)</div>
        <div class="definition-content">
            Le <strong>cycle de vie du développement logiciel</strong> décrit les étapes successives nécessaires pour créer un logiciel de qualité, depuis l'analyse des besoins jusqu'à la maintenance en production.
        </div>
    </div>
    
    <div class="phase-timeline">
        <div class="phase-item">
            <div class="phase-number">1</div>
            <div class="phase-content">
                <div class="phase-title">📋 Analyse des Besoins</div>
                <div class="phase-description">
                    Collecte et analyse des exigences fonctionnelles et non-fonctionnelles. Définition du périmètre du projet et des critères d'acceptation.
                </div>
            </div>
        </div>
        
        <div class="phase-item">
            <div class="phase-number">2</div>
            <div class="phase-content">
                <div class="phase-title">🎨 Conception</div>
                <div class="phase-description">
                    Élaboration de l'architecture technique, des maquettes UI/UX, du modèle de données et des spécifications détaillées.
                </div>
            </div>
        </div>
        
        <div class="phase-item">
            <div class="phase-number">3</div>
            <div class="phase-content">
                <div class="phase-title">⚙️ Développement</div>
                <div class="phase-description">
                    Implémentation du code source, intégration des composants et développement des fonctionnalités selon les spécifications.
                </div>
            </div>
        </div>
        
        <div class="phase-item">
            <div class="phase-number">4</div>
            <div class="phase-content">
                <div class="phase-title">🧪 Tests</div>
                <div class="phase-description">
                    Tests unitaires, d'intégration, fonctionnels et de performance. Validation de la conformité aux exigences.
                </div>
            </div>
        </div>
        
        <div class="phase-item">
            <div class="phase-number">5</div>
            <div class="phase-content">
                <div class="phase-title">🚀 Déploiement</div>
                <div class="phase-description">
                    Mise en production, configuration des environnements, migration des données et formation des utilisateurs.
                </div>
            </div>
        </div>
        
        <div class="phase-item">
            <div class="phase-number">6</div>
            <div class="phase-content">
                <div class="phase-title">🔧 Maintenance</div>
                <div class="phase-description">
                    Support technique, corrections de bugs, évolutions fonctionnelles et optimisations de performance.
                </div>
            </div>
        </div>
    </div>
    
    <div class="warning-fact">
        ⚠️ <strong>Important :</strong> Ces phases peuvent être itératives dans les méthodologies agiles, permettant des ajustements continus selon les retours utilisateurs.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛠️ Outils et Technologies</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚡ Écosystème de Développement</div>
        <div class="definition-content">
            Un projet de développement moderne s'appuie sur un <strong>écosystème d'outils</strong> couvrant l'ensemble du cycle de vie : IDE, contrôle de version, bases de données, tests, déploiement et monitoring.
        </div>
    </div>
    
    <div class="tools-grid">
        <div class="tool-card tool-ide">
            <div style="font-size: 2rem; margin-bottom: 1rem;">💻</div>
            <div>IDE & Éditeurs</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Visual Studio, VS Code, JetBrains</div>
        </div>
        
        <div class="tool-card tool-git">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🔄</div>
            <div>Contrôle de Version</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Git, GitHub, GitLab, Azure DevOps</div>
        </div>
        
        <div class="tool-card tool-database">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🗄️</div>
            <div>Bases de Données</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">SQL Server, PostgreSQL, MongoDB</div>
        </div>
        
        <div class="tool-card tool-testing">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🧪</div>
            <div>Tests</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">xUnit, NUnit, Selenium, Postman</div>
        </div>
        
        <div class="tool-card tool-deployment">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🚀</div>
            <div>Déploiement</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Docker, Kubernetes, Azure, AWS</div>
        </div>
        
        <div class="tool-card tool-monitoring">
            <div style="font-size: 2rem; margin-bottom: 1rem;">📊</div>
            <div>Monitoring</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem;">Application Insights, Grafana, ELK</div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Configuration DevOps avec C# et Docker</div>
        <pre><code># Dockerfile pour une application ASP.NET Core
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["MyProject.Api/MyProject.Api.csproj", "MyProject.Api/"]
COPY ["MyProject.Core/MyProject.Core.csproj", "MyProject.Core/"]
COPY ["MyProject.Infrastructure/MyProject.Infrastructure.csproj", "MyProject.Infrastructure/"]
RUN dotnet restore "MyProject.Api/MyProject.Api.csproj"
COPY . .
WORKDIR "/src/MyProject.Api"
RUN dotnet build "MyProject.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MyProject.Api.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyProject.Api.dll"]

# docker-compose.yml pour l'environnement de développement
version: '3.8'
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:80"
      - "5001:443"
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ConnectionStrings__DefaultConnection=Server=db;Database=MyProjectDb;User=sa;Password=YourPassword123;
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs
  
  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=YourPassword123
      - MSSQL_PID=Express
    ports:
      - "1433:1433"
    volumes:
      - sqlserver_data:/var/opt/mssql
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  sqlserver_data:
  redis_data:</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Pipeline CI/CD avec GitHub Actions</div>
        <pre><code># .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore --configuration Release
    
    - name: Run unit tests
      run: dotnet test --no-build --configuration Release --logger trx --collect:"XPlat Code Coverage"
    
    - name: Generate test report
      uses: dorny/test-reporter@v1
      if: success() || failure()
      with:
        name: .NET Tests
        path: '**/*.trx'
        reporter: dotnet-trx
    
    - name: Code coverage
      uses: codecov/codecov-action@v3
      with:
        files: '**/coverage.cobertura.xml'
  
  security-scan:
    runs-on: ubuntu-latest
    needs: test
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Run security scan
      uses: securecodewarrior/github-action-add-sarif@v1
      with:
        sarif-file: 'security-scan-results.sarif'
  
  deploy:
    runs-on: ubuntu-latest
    needs: [test, security-scan]
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}
    
    - name: Build and push Docker image
      run: |
        docker build -t myproject:${{ github.sha }} .
        docker tag myproject:${{ github.sha }} myregistry.azurecr.io/myproject:latest
        docker push myregistry.azurecr.io/myproject:latest
    
    - name: Deploy to Azure Container Instances
      uses: azure/aci-deploy@v1
      with:
        resource-group: 'my-resource-group'
        dns-name-label: 'myproject-${{ github.sha }}'
        image: 'myregistry.azurecr.io/myproject:latest'
        registry-login-server: 'myregistry.azurecr.io'
        registry-username: ${{ secrets.REGISTRY_USERNAME }}
        registry-password: ${{ secrets.REGISTRY_PASSWORD }}
        name: 'myproject-container'
        location: 'West Europe'</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">✅ Bonnes Pratiques de Développement</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏆 Standards de Qualité</div>
        <div class="definition-content">
            Les <strong>bonnes pratiques de développement</strong> garantissent la qualité, la maintenabilité et la sécurité du code. Elles couvrent l'architecture, le codage, les tests, la documentation et la collaboration en équipe.
        </div>
    </div>
    
    <div class="best-practices-grid">
        <div class="practice-card">
            <div class="practice-icon">🏗️</div>
            <div class="practice-title">Architecture Clean</div>
            <div class="practice-description">
                Séparer les responsabilités en couches distinctes : présentation, logique métier, accès aux données. Respecter les principes SOLID.
            </div>
        </div>
        
        <div class="practice-card">
            <div class="practice-icon">📝</div>
            <div class="practice-title">Code Lisible</div>
            <div class="practice-description">
                Utiliser des noms explicites, commenter le code complexe, respecter les conventions de nommage et maintenir une structure cohérente.
            </div>
        </div>
        
        <div class="practice-card">
            <div class="practice-icon">🔄</div>
            <div class="practice-title">Contrôle de Version</div>
            <div class="practice-description">
                Commits atomiques avec messages clairs, utilisation de branches pour les fonctionnalités, revues de code systématiques.
            </div>
        </div>
        
        <div class="practice-card">
            <div class="practice-icon">🧪</div>
            <div class="practice-title">Tests Automatisés</div>
            <div class="practice-description">
                Couverture de tests élevée, tests unitaires, d'intégration et end-to-end. TDD (Test-Driven Development) quand approprié.
            </div>
        </div>
        
        <div class="practice-card">
            <div class="practice-icon">🔒</div>
            <div class="practice-title">Sécurité</div>
            <div class="practice-description">
                Validation des entrées, authentification robuste, chiffrement des données sensibles, audit de sécurité régulier.
            </div>
        </div>
        
        <div class="practice-card">
            <div class="practice-icon">📊</div>
            <div class="practice-title">Monitoring</div>
            <div class="practice-description">
                Logs structurés, métriques de performance, alertes automatiques, tableaux de bord pour le suivi en temps réel.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Architecture Clean avec C#</div>
        <pre><code>// Domain Layer - Entité métier
public class User
{
    public int Id { get; private set; }
    public string Email { get; private set; }
    public string FirstName { get; private set; }
    public string LastName { get; private set; }
    public DateTime CreatedAt { get; private set; }
    public bool IsActive { get; private set; }
    
    private User() { } // Pour EF Core
    
    public User(string email, string firstName, string lastName)
    {
        if (string.IsNullOrWhiteSpace(email))
            throw new ArgumentException("Email is required", nameof(email));
        
        if (!IsValidEmail(email))
            throw new ArgumentException("Invalid email format", nameof(email));
        
        Email = email.ToLowerInvariant();
        FirstName = firstName?.Trim();
        LastName = lastName?.Trim();
        CreatedAt = DateTime.UtcNow;
        IsActive = true;
    }
    
    public void Deactivate()
    {
        IsActive = false;
    }
    
    public void UpdateProfile(string firstName, string lastName)
    {
        FirstName = firstName?.Trim();
        LastName = lastName?.Trim();
    }
    
    private static bool IsValidEmail(string email)
    {
        try
        {
            var addr = new System.Net.Mail.MailAddress(email);
            return addr.Address == email;
        }
        catch
        {
            return false;
        }
    }
}

// Application Layer - Service métier
public interface IUserService
{
    Task<User> CreateUserAsync(CreateUserCommand command);
    Task<User> GetUserByIdAsync(int id);
    Task<IEnumerable<User>> GetActiveUsersAsync();
    Task DeactivateUserAsync(int id);
}

public class UserService : IUserService
{
    private readonly IUserRepository _userRepository;
    private readonly IEmailService _emailService;
    private readonly ILogger<UserService> _logger;
    
    public UserService(IUserRepository userRepository, IEmailService emailService, ILogger<UserService> logger)
    {
        _userRepository = userRepository;
        _emailService = emailService;
        _logger = logger;
    }
    
    public async Task<User> CreateUserAsync(CreateUserCommand command)
    {
        _logger.LogInformation("Creating user with email: {Email}", command.Email);
        
        // Vérifier si l'utilisateur existe déjà
        var existingUser = await _userRepository.GetByEmailAsync(command.Email);
        if (existingUser != null)
        {
            throw new BusinessException("User with this email already exists");
        }
        
        // Créer le nouvel utilisateur
        var user = new User(command.Email, command.FirstName, command.LastName);
        
        // Sauvegarder
        await _userRepository.AddAsync(user);
        await _userRepository.SaveChangesAsync();
        
        // Envoyer email de bienvenue
        await _emailService.SendWelcomeEmailAsync(user.Email, user.FirstName);
        
        _logger.LogInformation("User created successfully with ID: {UserId}", user.Id);
        
        return user;
    }
    
    public async Task<User> GetUserByIdAsync(int id)
    {
        var user = await _userRepository.GetByIdAsync(id);
        if (user == null)
        {
            throw new NotFoundException($"User with ID {id} not found");
        }
        
        return user;
    }
    
    public async Task<IEnumerable<User>> GetActiveUsersAsync()
    {
        return await _userRepository.GetActiveUsersAsync();
    }
    
    public async Task DeactivateUserAsync(int id)
    {
        var user = await GetUserByIdAsync(id);
        user.Deactivate();
        
        await _userRepository.SaveChangesAsync();
        
        _logger.LogInformation("User {UserId} deactivated", id);
    }
}

// Infrastructure Layer - Repository
public interface IUserRepository
{
    Task<User> GetByIdAsync(int id);
    Task<User> GetByEmailAsync(string email);
    Task<IEnumerable<User>> GetActiveUsersAsync();
    Task AddAsync(User user);
    Task SaveChangesAsync();
}

public class UserRepository : IUserRepository
{
    private readonly ApplicationDbContext _context;
    
    public UserRepository(ApplicationDbContext context)
    {
        _context = context;
    }
    
    public async Task<User> GetByIdAsync(int id)
    {
        return await _context.Users.FindAsync(id);
    }
    
    public async Task<User> GetByEmailAsync(string email)
    {
        return await _context.Users
            .FirstOrDefaultAsync(u => u.Email == email.ToLowerInvariant());
    }
    
    public async Task<IEnumerable<User>> GetActiveUsersAsync()
    {
        return await _context.Users
            .Where(u => u.IsActive)
            .OrderBy(u => u.LastName)
            .ToListAsync();
    }
    
    public async Task AddAsync(User user)
    {
        await _context.Users.AddAsync(user);
    }
    
    public async Task SaveChangesAsync()
    {
        await _context.SaveChangesAsync();
    }
}</code></pre>
    </div>
    
    <div class="danger-fact">
        🚨 <strong>Attention :</strong> Ne jamais committer de secrets (mots de passe, clés API) dans le code source. Utilisez des variables d'environnement ou des services de gestion de secrets.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📈 Gestion de la Qualité et des Risques</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Assurance Qualité</div>
        <div class="definition-content">
            La <strong>gestion de la qualité</strong> dans un projet de développement implique la mise en place de processus, d'outils et de métriques pour garantir que le produit final répond aux exigences et aux standards de qualité définis.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Métriques de Qualité</div>
            <div class="concept-description">
                <strong>Couverture de tests :</strong> > 80%<br>
                <strong>Complexité cyclomatique :</strong> < 10<br>
                <strong>Duplication de code :</strong> < 3%<br>
                <strong>Bugs critiques :</strong> 0
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚠️</div>
            <div class="concept-name">Gestion des Risques</div>
            <div class="concept-description">
                Identification proactive des risques techniques, fonctionnels et organisationnels avec plans de mitigation appropriés.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔍</div>
            <div class="concept-name">Revues de Code</div>
            <div class="concept-description">
                Processus systématique de relecture du code par les pairs pour détecter les bugs et améliorer la qualité.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">Standards de Codage</div>
            <div class="concept-description">
                Conventions de nommage, formatage, documentation et architecture respectées par toute l'équipe.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Tests Unitaires avec xUnit</div>
        <pre><code>// Tests unitaires pour le UserService
public class UserServiceTests
{
    private readonly Mock<IUserRepository> _userRepositoryMock;
    private readonly Mock<IEmailService> _emailServiceMock;
    private readonly Mock<ILogger<UserService>> _loggerMock;
    private readonly UserService _userService;
    
    public UserServiceTests()
    {
        _userRepositoryMock = new Mock<IUserRepository>();
        _emailServiceMock = new Mock<IEmailService>();
        _loggerMock = new Mock<ILogger<UserService>>();
        _userService = new UserService(_userRepositoryMock.Object, _emailServiceMock.Object, _loggerMock.Object);
    }
    
    [Fact]
    public async Task CreateUserAsync_WithValidData_ShouldCreateUser()
    {
        // Arrange
        var command = new CreateUserCommand
        {
            Email = "test@example.com",
            FirstName = "John",
            LastName = "Doe"
        };
        
        _userRepositoryMock.Setup(x => x.GetByEmailAsync(command.Email))
            .ReturnsAsync((User)null);
        
        _userRepositoryMock.Setup(x => x.AddAsync(It.IsAny<User>()))
            .Returns(Task.CompletedTask);
        
        _userRepositoryMock.Setup(x => x.SaveChangesAsync())
            .Returns(Task.CompletedTask);
        
        _emailServiceMock.Setup(x => x.SendWelcomeEmailAsync(It.IsAny<string>(), It.IsAny<string>()))
            .Returns(Task.CompletedTask);
        
        // Act
        var result = await _userService.CreateUserAsync(command);
        
        // Assert
        Assert.NotNull(result);
        Assert.Equal(command.Email.ToLowerInvariant(), result.Email);
        Assert.Equal(command.FirstName, result.FirstName);
        Assert.Equal(command.LastName, result.LastName);
        Assert.True(result.IsActive);
        
        _userRepositoryMock.Verify(x => x.AddAsync(It.IsAny<User>()), Times.Once);
        _userRepositoryMock.Verify(x => x.SaveChangesAsync(), Times.Once);
        _emailServiceMock.Verify(x => x.SendWelcomeEmailAsync(command.Email, command.FirstName), Times.Once);
    }
    
    [Fact]
    public async Task CreateUserAsync_WithExistingEmail_ShouldThrowBusinessException()
    {
        // Arrange
        var command = new CreateUserCommand
        {
            Email = "existing@example.com",
            FirstName = "Jane",
            LastName = "Smith"
        };
        
        var existingUser = new User(command.Email, "Existing", "User");
        _userRepositoryMock.Setup(x => x.GetByEmailAsync(command.Email))
            .ReturnsAsync(existingUser);
        
        // Act & Assert
        var exception = await Assert.ThrowsAsync<BusinessException>(
            () => _userService.CreateUserAsync(command));
        
        Assert.Equal("User with this email already exists", exception.Message);
        
        _userRepositoryMock.Verify(x => x.AddAsync(It.IsAny<User>()), Times.Never);
        _emailServiceMock.Verify(x => x.SendWelcomeEmailAsync(It.IsAny<string>(), It.IsAny<string>()), Times.Never);
    }
    
    [Theory]
    [InlineData("")]
    [InlineData(" ")]
    [InlineData("invalid-email")]
    [InlineData("@example.com")]
    [InlineData("test@")]
    public async Task CreateUserAsync_WithInvalidEmail_ShouldThrowArgumentException(string invalidEmail)
    {
        // Arrange
        var command = new CreateUserCommand
        {
            Email = invalidEmail,
            FirstName = "Test",
            LastName = "User"
        };
        
        // Act & Assert
        await Assert.ThrowsAsync<ArgumentException>(
            () => _userService.CreateUserAsync(command));
    }
    
    [Fact]
    public async Task GetUserByIdAsync_WithExistingId_ShouldReturnUser()
    {
        // Arrange
        var userId = 1;
        var expectedUser = new User("test@example.com", "John", "Doe");
        
        _userRepositoryMock.Setup(x => x.GetByIdAsync(userId))
            .ReturnsAsync(expectedUser);
        
        // Act
        var result = await _userService.GetUserByIdAsync(userId);
        
        // Assert
        Assert.NotNull(result);
        Assert.Equal(expectedUser.Email, result.Email);
    }
    
    [Fact]
    public async Task GetUserByIdAsync_WithNonExistingId_ShouldThrowNotFoundException()
    {
        // Arrange
        var userId = 999;
        _userRepositoryMock.Setup(x => x.GetByIdAsync(userId))
            .ReturnsAsync((User)null);
        
        // Act & Assert
        var exception = await Assert.ThrowsAsync<NotFoundException>(
            () => _userService.GetUserByIdAsync(userId));
        
        Assert.Equal($"User with ID {userId} not found", exception.Message);
    }
}</code></pre>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Conseil :</strong> Utilisez des outils d'analyse statique comme SonarQube pour détecter automatiquement les problèmes de qualité et les vulnérabilités de sécurité.
    </div>
</div>