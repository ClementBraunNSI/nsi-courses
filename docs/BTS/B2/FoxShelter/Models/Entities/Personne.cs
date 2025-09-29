using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Entities
{
    /// <summary>
    /// Classe abstraite représentant une personne (employé ou bénévole)
    /// </summary>
    public abstract class Personne
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le nom est obligatoire")]
        [StringLength(100, ErrorMessage = "Le nom ne peut pas dépasser 100 caractères")]
        [Display(Name = "Nom")]
        public string Nom { get; set; } = string.Empty;
        
        [Required(ErrorMessage = "Le prénom est obligatoire")]
        [StringLength(100, ErrorMessage = "Le prénom ne peut pas dépasser 100 caractères")]
        [Display(Name = "Prénom")]
        public string Prenom { get; set; } = string.Empty;
        
        [EmailAddress(ErrorMessage = "Format d'email invalide")]
        [Display(Name = "Email")]
        public string? Email { get; set; }
        
        [Phone(ErrorMessage = "Format de téléphone invalide")]
        [Display(Name = "Téléphone")]
        public string? Telephone { get; set; }
        
        [Display(Name = "Date de naissance")]
        [DataType(DataType.Date)]
        public DateTime? DateNaissance { get; set; }
        
        [StringLength(500, ErrorMessage = "L'adresse ne peut pas dépasser 500 caractères")]
        [Display(Name = "Adresse")]
        [DataType(DataType.MultilineText)]
        public string? Adresse { get; set; }
        
        // Propriétés calculées
        [Display(Name = "Nom complet")]
        public string NomComplet => $"{Prenom} {Nom}";
        
        [Display(Name = "Initiales")]
        public string Initiales => $"{Prenom.FirstOrDefault()}.{Nom.FirstOrDefault()}.";
        
        // Méthodes
        /// <summary>
        /// Calcule l'âge de la personne
        /// </summary>
        public int CalculerAge()
        {
            if (!DateNaissance.HasValue) return 0;
            
            var age = DateTime.Now.Year - DateNaissance.Value.Year;
            if (DateTime.Now.DayOfYear < DateNaissance.Value.DayOfYear)
                age--;
            return age;
        }
        
        /// <summary>
        /// Obtient le nom complet formaté
        /// </summary>
        public string ObtenirNomComplet()
        {
            return $"{Prenom} {Nom}";
        }
        
        /// <summary>
        /// Vérifie si la personne est majeure
        /// </summary>
        public bool EstMajeure()
        {
            return CalculerAge() >= 18;
        }
        
        /// <summary>
        /// Obtient l'affichage de l'âge
        /// </summary>
        public string ObtenirAgeAffichage()
        {
            var age = CalculerAge();
            return age > 0 ? $"{age} ans" : "Non renseigné";
        }
    }
    
    /// <summary>
    /// Classe représentant un employé du refuge
    /// </summary>
    public class Employe : Personne
    {
        [Range(0, 100000, ErrorMessage = "Le salaire doit être positif")]
        [Display(Name = "Salaire mensuel")]
        [DataType(DataType.Currency)]
        public decimal? Salaire { get; set; }
        
        [StringLength(100, ErrorMessage = "Le poste ne peut pas dépasser 100 caractères")]
        [Display(Name = "Poste")]
        public string? Poste { get; set; }
        
        [Display(Name = "Date d'embauche")]
        [DataType(DataType.Date)]
        public DateTime? DateEmbauche { get; set; }
        
        [Display(Name = "Est vétérinaire")]
        public bool EstVeterinaire { get; set; } = false;
        
        [StringLength(500)]
        [Display(Name = "Qualifications")]
        [DataType(DataType.MultilineText)]
        public string? Qualifications { get; set; }
        
        // Relations
        public virtual ICollection<SoinVeterinaire> SoinsEffectues { get; set; } = new List<SoinVeterinaire>();
        
        // Propriétés calculées
        [Display(Name = "Salaire annuel")]
        public decimal SalaireAnnuel => Salaire.HasValue ? Salaire.Value * 12 : 0;
        
        // Méthodes
        /// <summary>
        /// Calcule l'ancienneté en années
        /// </summary>
        public int CalculerAncienneteAnnees()
        {
            if (!DateEmbauche.HasValue) return 0;
            
            var anciennete = DateTime.Now.Year - DateEmbauche.Value.Year;
            if (DateTime.Now.DayOfYear < DateEmbauche.Value.DayOfYear)
                anciennete--;
            return anciennete;
        }
        
        /// <summary>
        /// Calcule l'ancienneté en mois
        /// </summary>
        public int CalculerAncienneteMois()
        {
            if (!DateEmbauche.HasValue) return 0;
            
            var mois = (DateTime.Now.Year - DateEmbauche.Value.Year) * 12;
            mois += DateTime.Now.Month - DateEmbauche.Value.Month;
            
            if (DateTime.Now.Day < DateEmbauche.Value.Day)
                mois--;
                
            return mois;
        }
        
        /// <summary>
        /// Calcule le salaire annuel
        /// </summary>
        public decimal CalculerSalaireAnnuel()
        {
            return Salaire.HasValue ? Salaire.Value * 12 : 0;
        }
        
        /// <summary>
        /// Détermine si l'employé peut effectuer des soins vétérinaires
        /// </summary>
        public bool PeutEffectuerSoins()
        {
            return EstVeterinaire;
        }
        
        /// <summary>
        /// Obtient le nombre de soins effectués
        /// </summary>
        public int NombreSoinsEffectues()
        {
            return SoinsEffectues?.Count ?? 0;
        }
        
        /// <summary>
        /// Obtient l'affichage de l'ancienneté
        /// </summary>
        public string ObtenirAncienneteAffichage()
        {
            var annees = CalculerAncienneteAnnees();
            var mois = CalculerAncienneteMois() % 12;
            
            if (annees == 0 && mois == 0) return "Nouveau";
            if (annees == 0) return $"{mois} mois";
            if (mois == 0) return $"{annees} an{(annees > 1 ? "s" : "")}";
            
            return $"{annees} an{(annees > 1 ? "s" : "")} et {mois} mois";
        }
    }
    
    /// <summary>
    /// Classe représentant un bénévole du refuge
    /// </summary>
    public class Benevole : Personne
    {
        [StringLength(500)]
        [Display(Name = "Disponibilités")]
        [DataType(DataType.MultilineText)]
        public string? Disponibilites { get; set; }
        
        [StringLength(500)]
        [Display(Name = "Compétences")]
        [DataType(DataType.MultilineText)]
        public string? Competences { get; set; }
        
        [Range(0, int.MaxValue, ErrorMessage = "Les heures doivent être positives")]
        [Display(Name = "Heures de bénévolat")]
        public int HeuresBenevolat { get; set; } = 0;
        
        [Display(Name = "Date de première intervention")]
        [DataType(DataType.Date)]
        public DateTime? DatePremiereIntervention { get; set; }
        
        [Display(Name = "Est actif")]
        public bool EstActif { get; set; } = true;
        
        [StringLength(200)]
        [Display(Name = "Motivation")]
        public string? Motivation { get; set; }
        
        // Propriétés calculées
        [Display(Name = "Heures par mois")]
        public decimal HeuresParMois
        {
            get
            {
                if (!DatePremiereIntervention.HasValue) return 0;
                
                var moisActivite = Math.Max(1, (DateTime.Now - DatePremiereIntervention.Value).Days / 30);
                return Math.Round((decimal)HeuresBenevolat / moisActivite, 1);
            }
        }
        
        // Méthodes
        /// <summary>
        /// Ajoute des heures de bénévolat
        /// </summary>
        public void AjouterHeures(int heures)
        {
            if (heures > 0)
            {
                HeuresBenevolat += heures;
                
                // Si c'est la première fois, enregistrer la date
                if (!DatePremiereIntervention.HasValue)
                    DatePremiereIntervention = DateTime.Now;
            }
        }
        
        /// <summary>
        /// Vérifie si le bénévole est disponible à une date donnée
        /// </summary>
        public bool EstDisponible(DateTime date)
        {
            if (!EstActif) return false;
            
            // Logique simplifiée - dans un vrai projet, on analyserait les disponibilités
            return !string.IsNullOrEmpty(Disponibilites);
        }
        
        /// <summary>
        /// Calcule la durée d'engagement en mois
        /// </summary>
        public int CalculerDureeEngagementMois()
        {
            if (!DatePremiereIntervention.HasValue) return 0;
            
            return (DateTime.Now.Year - DatePremiereIntervention.Value.Year) * 12 +
                   DateTime.Now.Month - DatePremiereIntervention.Value.Month;
        }
        
        /// <summary>
        /// Détermine si le bénévole est expérimenté (plus de 50h)
        /// </summary>
        public bool EstExperimente()
        {
            return HeuresBenevolat >= 50;
        }
        
        /// <summary>
        /// Obtient le niveau d'engagement
        /// </summary>
        public string ObtenirNiveauEngagement()
        {
            return HeuresBenevolat switch
            {
                < 10 => "Débutant",
                < 50 => "Régulier",
                < 100 => "Expérimenté",
                _ => "Expert"
            };
        }
        
        /// <summary>
        /// Désactive le bénévole
        /// </summary>
        public void Desactiver()
        {
            EstActif = false;
        }
        
        /// <summary>
        /// Réactive le bénévole
        /// </summary>
        public void Reactiver()
        {
            EstActif = true;
        }
    }
}