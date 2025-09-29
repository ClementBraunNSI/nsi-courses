# Diagramme de Classes UML - FoxShelter

## Vue d'ensemble

Ce diagramme présente la structure des classes principales du système FoxShelter, leurs relations et leurs responsabilités.

## Diagramme de Classes

```mermaid
classDiagram
    %% Énumérations
    class EtatSante {
        <<enumeration>>
        Critique
        Mauvais
        Moyen
        Bon
        Excellent
    }
    
    class TypeSoin {
        <<enumeration>>
        Consultation
        Vaccination
        Chirurgie
        Urgence
        Controle
        Traitement
        Radiographie
        AnalyseSanguine
    }
    
    class TypeDon {
        <<enumeration>>
        Argent
        Nourriture
        Materiel
        Service
        Medicaments
        Equipement
    }
    
    %% Classes principales
    class Renard {
        +int Id
        +string Nom
        +string Espece
        +int Age
        +char Sexe
        +DateTime DateArrivee
        +EtatSante EtatSante
        +decimal Poids
        +string Description
        +bool EstAdopte
        +int RegimeAlimentaireId
        +DateTime DateCreation
        +DateTime DateModification
        
        +string NomComplet
        +string SexeTexte
        
        +int CalculerDureeSejourJours()
        +bool PeutEtreAdopte()
        +decimal CalculerCoutTotal()
        +SoinVeterinaire DernierSoin()
        +bool NecessiteAttentionUrgente()
        +string ObtenirAgeAffichage()
        +void ModifierEtatSante(EtatSante nouvelEtat)
        +void MarquerCommeAdopte()
    }
    
    class Personne {
        <<abstract>>
        +int Id
        +string Nom
        +string Prenom
        +string Email
        +string Telephone
        +DateTime DateNaissance
        +string Adresse
        
        +string NomComplet
        +string Initiales
        
        +int CalculerAge()
        +string ObtenirNomComplet()
        +bool EstMajeure()
        +string ObtenirAgeAffichage()
    }
    
    class Employe {
        +decimal Salaire
        +string Poste
        +DateTime DateEmbauche
        +bool EstVeterinaire
        +string Qualifications
        
        +int CalculerAncienneteAnnees()
        +decimal CalculerSalaireAnnuel()
        +bool PeutEffectuerSoins()
        +string ObtenirNiveauExperience()
    }
    
    class Benevole {
        +string Disponibilites
        +string Competences
        +int HeuresBenevolat
        +DateTime DatePremiereIntervention
        +bool EstActif
        +string Motivation
        
        +void AjouterHeures(int heures)
        +bool EstDisponible(DateTime date)
        +int CalculerDureeEngagementMois()
        +string ObtenirNiveauImplication()
    }
    
    class SoinVeterinaire {
        +int Id
        +DateTime DateSoin
        +TypeSoin TypeSoin
        +string Description
        +string Medicaments
        +decimal Cout
        +string Observations
        +DateTime? DateProchaineVisite
        +bool EstTermine
        +int VeterinaireId
        +int RenardId
        
        +string Resume
        +int DureeDepuisSoin
        
        +bool EstUrgent()
        +bool EstRecent()
        +bool ASuivi()
        +bool SuiviEnRetard()
        +int ObtenirPriorite()
        +string ObtenirCouleurAffichage()
        +string ObtenirIcone()
        +decimal CalculerCoutTotal()
        +void MarquerCommeTermine()
        +void ProgrammerSuivi(DateTime date)
        +string ObtenirResume()
    }
    
    class RegimeAlimentaire {
        +int Id
        +string Nom
        +string Description
        +int FrequenceRepas
        +decimal QuantiteParRepas
        +string TypeNourriture
        +decimal CoutJournalier
        +string ComplementsAlimentaires
        +bool AdapteJeunes
        +bool AdapteAdultes
        +bool AdapteSeniors
        +bool EstRegimeMedical
        +string InstructionsSpeciales
        
        +decimal QuantiteJournaliere
        +decimal CoutParKg
        +string TypeRegime
        
        +decimal CalculerCoutMensuel()
        +decimal CalculerCoutAnnuel()
        +bool EstAdapteAge(int age)
        +decimal CalculerQuantitePeriode(int jours)
        +decimal CalculerCoutPeriode(int jours)
        +List~string~ ObtenirHorairesRepas()
        +bool NecessiteSurveillance()
        +string ObtenirRecommandationsAge(int age)
        +Dictionary~string, object~ GenererPlanningJournalier()
        +bool ValiderRegime()
    }
    
    class Don {
        +int Id
        +TypeDon TypeDon
        +DateTime DateDon
        +decimal? Montant
        +string Description
        +decimal? Quantite
        +string Unite
        +string NomDonateur
        +string PrenomDonateur
        +string Email
        +string Telephone
        +string Adresse
        +bool EstAnonyme
        +bool RecuFiscalSouhaite
        +bool RecuFiscalEnvoye
        +DateTime? DateEnvoiRecu
        +string Commentaires
        +bool EstRecurrent
        +string FrequenceRecurrence
        +DateTime? ProchaineEcheance
        +DateTime DateCreation
        +DateTime DateModification
        
        +string DonateurComplet
        +decimal ValeurEstimee
        +string StatutRecuFiscal
        +int Anciennete
        
        +decimal CalculerValeurMonetaire()
        +bool NecessiteRecuFiscal()
        +void MarquerRecuEnvoye()
        +DateTime CalculerProchaineEcheance()
        +bool EstEchu()
        +string ObtenirCategorie()
        +string GenererMessageRemerciement()
        +bool ValiderDon()
        +Don CreerDonRecurrentSuivant()
    }
    
    %% Services
    class RenardService {
        -FoxShelterContext _context
        
        +Task~List~Renard~~ ObtenirTousAsync()
        +Task~Renard~ ObtenirParIdAsync(int id)
        +Task~Renard~ AjouterAsync(Renard renard)
        +Task~Renard~ ModifierAsync(Renard renard)
        +Task~bool~ SupprimerAsync(int id)
        +Task~List~Renard~~ RechercherAsync(string terme)
        +Task~Renard~ MarquerCommeAdopteAsync(int id)
        +Task~Renard~ ModifierEtatSanteAsync(int id, EtatSante nouvelEtat)
        +Task~StatistiquesRenards~ ObtenirStatistiquesAsync()
        +Task~List~Renard~~ ObtenirRenardsUrgentsAsync()
        +Task~List~Renard~~ ObtenirNouveauxArrivantsAsync(int jours)
        +Task~List~Renard~~ ObtenirRenardsNecessitantSuiviAsync()
    }
    
    class StatistiquesRenards {
        +int NombreTotal
        +int NombreAdoptes
        +int NombreUrgents
        +int NombreNouveauxArrivants
        +decimal PourcentageAdoptes
        +decimal CoutMoyenSoins
        +int DureeSejourMoyenne
        +Dictionary~EtatSante, int~ RepartitionEtatSante
        +Dictionary~string, int~ RepartitionEspeces
    }
    
    %% Contexte de base de données
    class FoxShelterContext {
        +DbSet~Renard~ Renards
        +DbSet~Employe~ Employes
        +DbSet~Benevole~ Benevoles
        +DbSet~SoinVeterinaire~ SoinsVeterinaires
        +DbSet~RegimeAlimentaire~ RegimesAlimentaires
        +DbSet~Don~ Dons
        
        +void OnModelCreating(ModelBuilder modelBuilder)
        +Task~int~ SaveChangesAsync()
    }
    
    %% Relations
    Personne <|-- Employe : hérite
    Personne <|-- Benevole : hérite
    
    Renard ||--o{ SoinVeterinaire : "reçoit"
    Employe ||--o{ SoinVeterinaire : "effectue"
    Renard }o--|| RegimeAlimentaire : "suit"
    
    Renard --> EtatSante : "a un"
    SoinVeterinaire --> TypeSoin : "est de type"
    Don --> TypeDon : "est de type"
    
    RenardService --> FoxShelterContext : "utilise"
    RenardService --> StatistiquesRenards : "génère"
    
    FoxShelterContext --> Renard : "gère"
    FoxShelterContext --> Employe : "gère"
    FoxShelterContext --> Benevole : "gère"
    FoxShelterContext --> SoinVeterinaire : "gère"
    FoxShelterContext --> RegimeAlimentaire : "gère"
    FoxShelterContext --> Don : "gère"
```

## Description des Classes

### Classes Entités

#### Renard
- **Responsabilité** : Représente un renard hébergé au refuge
- **Attributs principaux** : Informations d'identification, état de santé, données physiques
- **Méthodes clés** : Calculs de durée de séjour, vérifications d'adoptabilité, gestion de l'état

#### Personne (Abstraite)
- **Responsabilité** : Classe de base pour les personnes (employés et bénévoles)
- **Attributs principaux** : Informations personnelles de base
- **Méthodes clés** : Calculs d'âge, formatage des noms

#### Employe
- **Responsabilité** : Représente un employé du refuge
- **Spécialisation** : Informations professionnelles, qualifications vétérinaires
- **Méthodes clés** : Calculs de salaire et d'ancienneté

#### Benevole
- **Responsabilité** : Représente un bénévole du refuge
- **Spécialisation** : Disponibilités, compétences, suivi de l'engagement
- **Méthodes clés** : Gestion des heures, vérification de disponibilité

#### SoinVeterinaire
- **Responsabilité** : Représente un soin vétérinaire prodigué à un renard
- **Attributs principaux** : Type de soin, coût, observations, suivi
- **Méthodes clés** : Évaluation d'urgence, calculs de coût, gestion du suivi

#### RegimeAlimentaire
- **Responsabilité** : Définit un régime alimentaire pour les renards
- **Attributs principaux** : Composition, fréquence, coûts, adaptabilité
- **Méthodes clés** : Calculs nutritionnels et financiers, validation

#### Don
- **Responsabilité** : Représente un don fait au refuge
- **Attributs principaux** : Type, montant, donateur, récurrence
- **Méthodes clés** : Calculs de valeur, gestion des reçus fiscaux

### Classes Services

#### RenardService
- **Responsabilité** : Logique métier pour la gestion des renards
- **Fonctionnalités** : CRUD, recherche, statistiques, gestion des états
- **Pattern** : Service Layer

#### StatistiquesRenards
- **Responsabilité** : Agrégation de données statistiques
- **Utilisation** : Tableaux de bord, rapports

### Classes Infrastructure

#### FoxShelterContext
- **Responsabilité** : Contexte Entity Framework pour l'accès aux données
- **Pattern** : Repository/Unit of Work via EF Core

## Patterns Utilisés

1. **Héritage** : Personne → Employe/Benevole
2. **Composition** : Renard contient RegimeAlimentaire
3. **Association** : Relations entre entités
4. **Service Layer** : RenardService pour la logique métier
5. **Repository Pattern** : Via Entity Framework DbContext

## Contraintes et Règles Métier

1. Un renard ne peut avoir qu'un seul régime alimentaire actif
2. Seuls les employés vétérinaires peuvent effectuer certains soins
3. Les soins urgents doivent être traités en priorité
4. Les régimes médicaux nécessitent une surveillance particulière
5. Les dons récurrents génèrent automatiquement les échéances suivantes

## Évolutions Possibles

1. Ajout d'une classe `Adoption` pour tracer les adoptions
2. Classe `Planning` pour la gestion des horaires
3. Classe `Rapport` pour la génération de documents
4. Interface `INotificationService` pour les alertes
5. Classe `Medicament` pour une gestion plus fine des traitements