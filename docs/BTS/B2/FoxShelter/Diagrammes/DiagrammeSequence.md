# Diagrammes de Séquence UML - FoxShelter

## Vue d'ensemble

Ce document présente les diagrammes de séquence pour les principaux scénarios d'utilisation du système FoxShelter.

## 1. Diagramme de Séquence : Enregistrement d'un nouveau renard

```mermaid
sequenceDiagram
    participant E as Employé
    participant C as RenardController
    participant S as RenardService
    participant DB as FoxShelterContext
    participant R as RegimeService
    
    E->>C: GET /Renard/Create
    C->>R: ObtenirRegimesDisponibles()
    R-->>C: List<RegimeAlimentaire>
    C-->>E: Vue Create avec régimes
    
    E->>C: POST /Renard/Create (données renard)
    C->>C: ValidateModel()
    
    alt Validation réussie
        C->>S: AjouterAsync(renard)
        S->>S: ValiderDonnees(renard)
        S->>DB: Renards.Add(renard)
        S->>DB: SaveChangesAsync()
        DB-->>S: Renard créé avec ID
        S-->>C: Renard créé
        C->>C: TempData["Succes"] = "Renard enregistré"
        C-->>E: Redirect vers Details
    else Validation échouée
        C->>R: ObtenirRegimesDisponibles()
        R-->>C: List<RegimeAlimentaire>
        C-->>E: Vue Create avec erreurs
    end
```

## 2. Diagramme de Séquence : Effectuer un soin vétérinaire

```mermaid
sequenceDiagram
    participant V as Vétérinaire
    participant C as SoinController
    participant S as SoinService
    participant RS as RenardService
    participant DB as FoxShelterContext
    participant N as NotificationService
    
    V->>C: GET /Soin/Create?renardId=1
    C->>RS: ObtenirParIdAsync(1)
    RS-->>C: Renard
    C-->>V: Vue Create avec infos renard
    
    V->>C: POST /Soin/Create (données soin)
    C->>C: ValidateModel()
    
    alt Validation réussie
        C->>S: AjouterSoinAsync(soin)
        S->>S: ValiderSoin(soin)
        S->>DB: SoinsVeterinaires.Add(soin)
        
        alt Soin modifie état de santé
            S->>RS: ModifierEtatSanteAsync(renardId, nouvelEtat)
            RS->>DB: Renards.Update(renard)
        end
        
        S->>DB: SaveChangesAsync()
        DB-->>S: Soin enregistré
        
        alt Soin urgent ou critique
            S->>N: EnvoyerNotificationUrgence(soin)
            N-->>S: Notification envoyée
        end
        
        S-->>C: Soin créé
        C->>C: TempData["Succes"] = "Soin enregistré"
        C-->>V: Redirect vers Details renard
    else Validation échouée
        C-->>V: Vue Create avec erreurs
    end
```

## 3. Diagramme de Séquence : Processus d'adoption

```mermaid
sequenceDiagram
    participant A as Adoptant
    participant C as AdoptionController
    participant AS as AdoptionService
    participant RS as RenardService
    participant ES as EmailService
    participant DB as FoxShelterContext
    
    A->>C: GET /Adoption/Disponibles
    C->>RS: ObtenirRenardsAdoptablesAsync()
    RS->>DB: Query renards adoptables
    DB-->>RS: List<Renard>
    RS-->>C: Renards adoptables
    C-->>A: Vue avec renards disponibles
    
    A->>C: POST /Adoption/Demander (renardId, infos adoptant)
    C->>C: ValidateModel()
    
    alt Validation réussie
        C->>AS: CreerDemandeAdoptionAsync(demande)
        AS->>AS: ValiderEligibilite(adoptant)
        AS->>DB: DemandesAdoption.Add(demande)
        AS->>DB: SaveChangesAsync()
        DB-->>AS: Demande créée
        
        AS->>ES: EnvoyerConfirmationDemande(adoptant)
        ES-->>AS: Email envoyé
        
        AS-->>C: Demande enregistrée
        C->>C: TempData["Succes"] = "Demande enregistrée"
        C-->>A: Vue confirmation
    else Validation échouée
        C-->>A: Vue avec erreurs
    end
    
    Note over AS: Processus d'évaluation (asynchrone)
    
    AS->>AS: EvaluerDemandeAsync(demandeId)
    
    alt Demande approuvée
        AS->>RS: MarquerCommeAdopteAsync(renardId)
        RS->>DB: Update renard.EstAdopte = true
        RS->>DB: SaveChangesAsync()
        
        AS->>ES: EnvoyerNotificationApprobation(adoptant)
        ES-->>AS: Email envoyé
        
        AS->>AS: InitierSuiviPostAdoption(adoption)
    else Demande refusée
        AS->>ES: EnvoyerNotificationRefus(adoptant)
        ES-->>AS: Email envoyé
    end
```

## 4. Diagramme de Séquence : Génération de statistiques

```mermaid
sequenceDiagram
    participant A as Administrateur
    participant C as HomeController
    participant RS as RenardService
    participant SS as StatistiqueService
    participant DB as FoxShelterContext
    participant Cache as CacheService
    
    A->>C: GET /Home/Statistiques
    C->>Cache: ObtenirStatistiques("dashboard")
    
    alt Cache disponible
        Cache-->>C: Statistiques en cache
    else Cache expiré ou absent
        C->>RS: ObtenirStatistiquesAsync()
        
        par Statistiques renards
            RS->>DB: Query COUNT renards par état
            DB-->>RS: Données renards
        and Statistiques soins
            RS->>DB: Query soins par période
            DB-->>RS: Données soins
        and Statistiques adoptions
            RS->>DB: Query adoptions par mois
            DB-->>RS: Données adoptions
        end
        
        RS->>SS: CalculerStatistiquesCompletes(données)
        SS->>SS: CalculerTendances()
        SS->>SS: CalculerPourcentages()
        SS-->>RS: Statistiques calculées
        RS-->>C: StatistiquesCompletes
        
        C->>Cache: SauvegarderStatistiques("dashboard", stats, 1h)
        Cache-->>C: Sauvegardé
    end
    
    C-->>A: Vue avec statistiques et graphiques
```

## 5. Diagramme de Séquence : Gestion des alertes système

```mermaid
sequenceDiagram
    participant Sys as Système (Timer)
    participant AS as AlerteService
    participant RS as RenardService
    participant SS as SoinService
    participant NS as NotificationService
    participant DB as FoxShelterContext
    
    Sys->>AS: ExecuterVerificationsPeriodiques()
    
    par Vérification renards critiques
        AS->>RS: ObtenirRenardsEtatCritiqueAsync()
        RS->>DB: Query renards état = Critique
        DB-->>RS: List<Renard> critiques
        RS-->>AS: Renards critiques
        
        loop Pour chaque renard critique
            AS->>NS: EnvoyerAlerteUrgence(renard)
            NS-->>AS: Alerte envoyée
        end
        
    and Vérification suivis en retard
        AS->>SS: ObtenirSuivisEnRetardAsync()
        SS->>DB: Query soins avec suivi en retard
        DB-->>SS: List<SoinVeterinaire>
        SS-->>AS: Soins en retard
        
        loop Pour chaque suivi en retard
            AS->>NS: EnvoyerRappelSuivi(soin)
            NS-->>AS: Rappel envoyé
        end
        
    and Vérification capacité refuge
        AS->>RS: VerifierCapaciteRefugeAsync()
        RS->>DB: Query COUNT renards actifs
        DB-->>RS: Nombre renards
        RS-->>AS: Statut capacité
        
        alt Capacité dépassée
            AS->>NS: EnvoyerAlerteCapacite()
            NS-->>AS: Alerte envoyée
        end
    end
    
    AS->>AS: EnregistrerRapportVerification()
    AS-->>Sys: Vérifications terminées
```

## 6. Diagramme de Séquence : Sauvegarde et restauration

```mermaid
sequenceDiagram
    participant A as Administrateur
    participant C as AdminController
    participant BS as BackupService
    participant DB as FoxShelterContext
    participant FS as FileSystem
    participant Cloud as CloudStorage
    
    A->>C: POST /Admin/CreerSauvegarde
    C->>BS: CreerSauvegardeCompleteAsync()
    
    BS->>DB: BeginTransaction()
    DB-->>BS: Transaction démarrée
    
    par Sauvegarde données
        BS->>DB: ExporterDonnees("renards")
        DB-->>BS: Données renards
        BS->>FS: EcrireFichier("renards.json")
        
        BS->>DB: ExporterDonnees("soins")
        DB-->>BS: Données soins
        BS->>FS: EcrireFichier("soins.json")
        
        BS->>DB: ExporterDonnees("personnel")
        DB-->>BS: Données personnel
        BS->>FS: EcrireFichier("personnel.json")
    end
    
    BS->>FS: CreerArchive("backup_" + timestamp + ".zip")
    FS-->>BS: Archive créée
    
    alt Sauvegarde cloud activée
        BS->>Cloud: TelechargerArchive(archive)
        Cloud-->>BS: Upload réussi
    end
    
    BS->>DB: CommitTransaction()
    DB-->>BS: Transaction validée
    
    BS-->>C: Sauvegarde terminée
    C->>C: TempData["Succes"] = "Sauvegarde créée"
    C-->>A: Redirect vers liste sauvegardes
```

## Patterns et Principes Utilisés

### 1. Patterns Architecturaux
- **MVC (Model-View-Controller)** : Séparation des responsabilités
- **Service Layer** : Logique métier centralisée
- **Repository Pattern** : Abstraction de l'accès aux données via Entity Framework

### 2. Patterns de Conception
- **Command Pattern** : Pour les opérations complexes
- **Observer Pattern** : Pour les notifications
- **Strategy Pattern** : Pour les différents types de calculs

### 3. Principes SOLID
- **Single Responsibility** : Chaque service a une responsabilité unique
- **Open/Closed** : Extensions possibles sans modification
- **Dependency Inversion** : Dépendance vers les abstractions

## Gestion des Erreurs

### Types d'erreurs gérées
1. **Erreurs de validation** : Données invalides
2. **Erreurs métier** : Règles business non respectées
3. **Erreurs techniques** : Problèmes de base de données, réseau
4. **Erreurs de sécurité** : Accès non autorisé

### Stratégies de gestion
- **Try-catch** dans les services
- **Validation** côté client et serveur
- **Logging** des erreurs
- **Messages** utilisateur appropriés
- **Rollback** des transactions en cas d'erreur

## Performance et Optimisation

### Stratégies utilisées
1. **Mise en cache** des données fréquemment consultées
2. **Requêtes asynchrones** pour les opérations longues
3. **Pagination** pour les listes importantes
4. **Lazy loading** pour les relations Entity Framework
5. **Compression** des sauvegardes

### Points d'attention
- **N+1 queries** : Utilisation d'Include() approprié
- **Mémoire** : Disposal des ressources
- **Concurrence** : Gestion des accès simultanés
- **Scalabilité** : Architecture prête pour la montée en charge