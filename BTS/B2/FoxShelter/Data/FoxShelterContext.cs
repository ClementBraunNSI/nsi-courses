using Microsoft.EntityFrameworkCore;
using FoxShelter.Models.Entities;
using FoxShelter.Models.Enums;

namespace FoxShelter.Data
{
    /// <summary>
    /// Contexte Entity Framework pour la base de données FoxShelter
    /// </summary>
    public class FoxShelterContext : DbContext
    {
        public FoxShelterContext(DbContextOptions<FoxShelterContext> options) : base(options)
        {
        }
        
        // DbSets pour les entités
        public DbSet<Renard> Renards { get; set; }
        public DbSet<Employe> Employes { get; set; }
        public DbSet<Benevole> Benevoles { get; set; }
        public DbSet<SoinVeterinaire> SoinsVeterinaires { get; set; }
        public DbSet<RegimeAlimentaire> RegimesAlimentaires { get; set; }
        public DbSet<Don> Dons { get; set; }
        
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            
            // Configuration de l'héritage TPH (Table Per Hierarchy) pour Personne
            modelBuilder.Entity<Personne>()
                .HasDiscriminator<string>("TypePersonne")
                .HasValue<Employe>("Employe")
                .HasValue<Benevole>("Benevole");
            
            // Configuration de la table Renards
            modelBuilder.Entity<Renard>(entity =>
            {
                entity.HasKey(r => r.Id);
                entity.Property(r => r.Nom).IsRequired().HasMaxLength(100);
                entity.Property(r => r.Espece).IsRequired().HasMaxLength(100);
                entity.Property(r => r.Sexe).IsRequired().HasMaxLength(1);
                entity.Property(r => r.EtatSante).HasConversion<string>();
                entity.Property(r => r.Poids).HasPrecision(5, 2);
                entity.Property(r => r.Description).HasMaxLength(1000);
                
                // Index pour améliorer les performances
                entity.HasIndex(r => r.Nom);
                entity.HasIndex(r => r.EtatSante);
                entity.HasIndex(r => r.EstAdopte);
                entity.HasIndex(r => r.DateArrivee);
                
                // Relation avec RegimeAlimentaire
                entity.HasOne(r => r.RegimeAlimentaire)
                      .WithMany(ra => ra.Renards)
                      .HasForeignKey(r => r.RegimeAlimentaireId)
                      .OnDelete(DeleteBehavior.SetNull);
                
                // Relation avec SoinsVeterinaires
                entity.HasMany(r => r.Soins)
                      .WithOne(s => s.Renard)
                      .HasForeignKey(s => s.RenardId)
                      .OnDelete(DeleteBehavior.Cascade);
            });
            
            // Configuration de la table Personnes (classe de base)
            modelBuilder.Entity<Personne>(entity =>
            {
                entity.HasKey(p => p.Id);
                entity.Property(p => p.Nom).IsRequired().HasMaxLength(100);
                entity.Property(p => p.Prenom).IsRequired().HasMaxLength(100);
                entity.Property(p => p.Email).HasMaxLength(150);
                entity.Property(p => p.Telephone).HasMaxLength(20);
                entity.Property(p => p.Adresse).HasMaxLength(300);
                
                // Index pour améliorer les performances
                entity.HasIndex(p => p.Email).IsUnique();
                entity.HasIndex(p => new { p.Nom, p.Prenom });
            });
            
            // Configuration spécifique pour Employe
            modelBuilder.Entity<Employe>(entity =>
            {
                entity.Property(e => e.Salaire).HasPrecision(10, 2);
                entity.Property(e => e.Poste).IsRequired().HasMaxLength(100);
                entity.Property(e => e.Qualifications).HasMaxLength(500);
                
                // Index pour améliorer les performances
                entity.HasIndex(e => e.Poste);
                entity.HasIndex(e => e.EstVeterinaire);
                
                // Relation avec SoinsVeterinaires
                entity.HasMany<SoinVeterinaire>()
                      .WithOne(s => s.Veterinaire)
                      .HasForeignKey(s => s.VeterinaireId)
                      .OnDelete(DeleteBehavior.Restrict);
            });
            
            // Configuration spécifique pour Benevole
            modelBuilder.Entity<Benevole>(entity =>
            {
                entity.Property(b => b.Disponibilites).HasMaxLength(200);
                entity.Property(b => b.Competences).HasMaxLength(500);
                entity.Property(b => b.Motivation).HasMaxLength(1000);
                
                // Index pour améliorer les performances
                entity.HasIndex(b => b.EstActif);
                entity.HasIndex(b => b.DatePremiereIntervention);
            });
            
            // Configuration de la table SoinsVeterinaires
            modelBuilder.Entity<SoinVeterinaire>(entity =>
            {
                entity.HasKey(s => s.Id);
                entity.Property(s => s.TypeSoin).HasConversion<string>();
                entity.Property(s => s.Description).IsRequired().HasMaxLength(1000);
                entity.Property(s => s.Medicaments).HasMaxLength(500);
                entity.Property(s => s.Cout).HasPrecision(8, 2);
                entity.Property(s => s.Observations).HasMaxLength(1000);
                
                // Index pour améliorer les performances
                entity.HasIndex(s => s.DateSoin);
                entity.HasIndex(s => s.TypeSoin);
                entity.HasIndex(s => s.EstTermine);
                entity.HasIndex(s => new { s.RenardId, s.DateSoin });
                
                // Contraintes de clés étrangères
                entity.HasOne(s => s.Renard)
                      .WithMany(r => r.Soins)
                      .HasForeignKey(s => s.RenardId)
                      .OnDelete(DeleteBehavior.Cascade);
                      
                entity.HasOne(s => s.Veterinaire)
                      .WithMany()
                      .HasForeignKey(s => s.VeterinaireId)
                      .OnDelete(DeleteBehavior.Restrict);
            });
            
            // Configuration de la table RegimesAlimentaires
            modelBuilder.Entity<RegimeAlimentaire>(entity =>
            {
                entity.HasKey(ra => ra.Id);
                entity.Property(ra => ra.Nom).IsRequired().HasMaxLength(100);
                entity.Property(ra => ra.Description).HasMaxLength(500);
                entity.Property(ra => ra.QuantiteParRepas).HasPrecision(5, 2);
                entity.Property(ra => ra.TypeNourriture).IsRequired().HasMaxLength(200);
                entity.Property(ra => ra.CoutJournalier).HasPrecision(8, 2);
                entity.Property(ra => ra.ComplementsAlimentaires).HasMaxLength(300);
                entity.Property(ra => ra.InstructionsSpeciales).HasMaxLength(300);
                
                // Index pour améliorer les performances
                entity.HasIndex(ra => ra.Nom);
                entity.HasIndex(ra => ra.EstRegimeMedical);
                entity.HasIndex(ra => new { ra.AdapteJeunes, ra.AdapteAdultes, ra.AdapteSeniors });
            });
            
            // Configuration de la table Dons
            modelBuilder.Entity<Don>(entity =>
            {
                entity.HasKey(d => d.Id);
                entity.Property(d => d.TypeDon).HasConversion<string>();
                entity.Property(d => d.Montant).HasPrecision(10, 2);
                entity.Property(d => d.Description).HasMaxLength(200);
                entity.Property(d => d.Unite).HasMaxLength(50);
                entity.Property(d => d.NomDonateur).IsRequired().HasMaxLength(100);
                entity.Property(d => d.PrenomDonateur).HasMaxLength(100);
                entity.Property(d => d.Email).HasMaxLength(150);
                entity.Property(d => d.Telephone).HasMaxLength(20);
                entity.Property(d => d.Adresse).HasMaxLength(300);
                entity.Property(d => d.Commentaires).HasMaxLength(500);
                
                // Index pour améliorer les performances
                entity.HasIndex(d => d.DateDon);
                entity.HasIndex(d => d.TypeDon);
                entity.HasIndex(d => d.EstRecurrent);
                entity.HasIndex(d => d.RecuFiscalSouhaite);
                entity.HasIndex(d => new { d.NomDonateur, d.PrenomDonateur });
            });
            
            // Données de test (Seed Data)
            SeedData(modelBuilder);
        }
        
        /// <summary>
        /// Méthode pour insérer des données de test
        /// </summary>
        private void SeedData(ModelBuilder modelBuilder)
        {
            // Régimes alimentaires de base
            modelBuilder.Entity<RegimeAlimentaire>().HasData(
                new RegimeAlimentaire
                {
                    Id = 1,
                    Nom = "Régime Standard Adulte",
                    Description = "Régime équilibré pour renards adultes en bonne santé",
                    FrequenceRepas = 2,
                    QuantiteParRepas = 0.8m,
                    TypeNourriture = "Croquettes premium + viande fraîche",
                    CoutJournalier = 4.50m,
                    AdapteAdultes = true,
                    EstRegimeMedical = false
                },
                new RegimeAlimentaire
                {
                    Id = 2,
                    Nom = "Régime Jeune",
                    Description = "Régime riche en nutriments pour jeunes renards",
                    FrequenceRepas = 4,
                    QuantiteParRepas = 0.3m,
                    TypeNourriture = "Lait maternisé + croquettes junior",
                    CoutJournalier = 6.00m,
                    AdapteJeunes = true,
                    EstRegimeMedical = false
                },
                new RegimeAlimentaire
                {
                    Id = 3,
                    Nom = "Régime Médical Digestif",
                    Description = "Régime spécial pour troubles digestifs",
                    FrequenceRepas = 3,
                    QuantiteParRepas = 0.5m,
                    TypeNourriture = "Aliments hypoallergéniques",
                    CoutJournalier = 8.00m,
                    ComplementsAlimentaires = "Probiotiques, enzymes digestives",
                    AdapteAdultes = true,
                    EstRegimeMedical = true,
                    InstructionsSpeciales = "Surveiller les selles, donner à température ambiante"
                }
            );
            
            // Employés de base
            modelBuilder.Entity<Employe>().HasData(
                new Employe
                {
                    Id = 1,
                    Nom = "Martin",
                    Prenom = "Sophie",
                    Email = "sophie.martin@foxshelter.fr",
                    Telephone = "01.23.45.67.89",
                    DateNaissance = new DateTime(1985, 3, 15),
                    Adresse = "123 Rue de la Forêt, 75001 Paris",
                    Salaire = 3500m,
                    Poste = "Vétérinaire",
                    DateEmbauche = new DateTime(2020, 1, 15),
                    EstVeterinaire = true,
                    Qualifications = "Docteur vétérinaire, spécialisation faune sauvage"
                },
                new Employe
                {
                    Id = 2,
                    Nom = "Dubois",
                    Prenom = "Pierre",
                    Email = "pierre.dubois@foxshelter.fr",
                    Telephone = "01.23.45.67.90",
                    DateNaissance = new DateTime(1990, 7, 22),
                    Adresse = "456 Avenue des Bois, 75002 Paris",
                    Salaire = 2800m,
                    Poste = "Soigneur animalier",
                    DateEmbauche = new DateTime(2021, 6, 1),
                    EstVeterinaire = false,
                    Qualifications = "BTS Productions animales, formation premiers secours"
                }
            );
            
            // Bénévoles de base
            modelBuilder.Entity<Benevole>().HasData(
                new Benevole
                {
                    Id = 3,
                    Nom = "Leroy",
                    Prenom = "Marie",
                    Email = "marie.leroy@email.fr",
                    Telephone = "06.12.34.56.78",
                    DateNaissance = new DateTime(1995, 11, 8),
                    Adresse = "789 Rue du Parc, 75003 Paris",
                    Disponibilites = "Week-ends et mercredi après-midi",
                    Competences = "Nettoyage, alimentation, socialisation",
                    HeuresBenevolat = 120,
                    DatePremiereIntervention = new DateTime(2023, 3, 1),
                    EstActif = true,
                    Motivation = "Passion pour la protection de la faune sauvage"
                }
            );
        }
        
        /// <summary>
        /// Méthode appelée lors de la sauvegarde pour mettre à jour les timestamps
        /// </summary>
        public override int SaveChanges()
        {
            UpdateTimestamps();
            return base.SaveChanges();
        }
        
        /// <summary>
        /// Méthode appelée lors de la sauvegarde asynchrone pour mettre à jour les timestamps
        /// </summary>
        public override Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
        {
            UpdateTimestamps();
            return base.SaveChangesAsync(cancellationToken);
        }
        
        /// <summary>
        /// Met à jour les timestamps de création et modification
        /// </summary>
        private void UpdateTimestamps()
        {
            var entries = ChangeTracker.Entries()
                .Where(e => e.State == EntityState.Added || e.State == EntityState.Modified);
                
            foreach (var entry in entries)
            {
                if (entry.Entity is Renard renard)
                {
                    if (entry.State == EntityState.Added)
                        renard.DateCreation = DateTime.Now;
                    renard.DateModification = DateTime.Now;
                }
                else if (entry.Entity is Don don)
                {
                    if (entry.State == EntityState.Added)
                        don.DateCreation = DateTime.Now;
                    don.DateModification = DateTime.Now;
                }
            }
        }
    }
}