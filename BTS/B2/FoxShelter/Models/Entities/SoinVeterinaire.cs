using System.ComponentModel.DataAnnotations;
using FoxShelter.Models.Enums;

namespace FoxShelter.Models.Entities
{
    /// <summary>
    /// Classe représentant un soin vétérinaire effectué sur un renard
    /// </summary>
    public class SoinVeterinaire
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "La date du soin est obligatoire")]
        [Display(Name = "Date du soin")]
        [DataType(DataType.DateTime)]
        public DateTime DateSoin { get; set; } = DateTime.Now;
        
        [Required(ErrorMessage = "Le type de soin est obligatoire")]
        [Display(Name = "Type de soin")]
        public TypeSoin TypeSoin { get; set; }
        
        [Required(ErrorMessage = "La description est obligatoire")]
        [StringLength(1000, ErrorMessage = "La description ne peut pas dépasser 1000 caractères")]
        [Display(Name = "Description")]
        [DataType(DataType.MultilineText)]
        public string Description { get; set; } = string.Empty;
        
        [StringLength(500)]
        [Display(Name = "Médicaments prescrits")]
        [DataType(DataType.MultilineText)]
        public string? Medicaments { get; set; }
        
        [Range(0, 10000, ErrorMessage = "Le coût doit être positif")]
        [Display(Name = "Coût")]
        [DataType(DataType.Currency)]
        public decimal Cout { get; set; }
        
        [StringLength(500)]
        [Display(Name = "Observations")]
        [DataType(DataType.MultilineText)]
        public string? Observations { get; set; }
        
        [Display(Name = "Prochaine visite")]
        [DataType(DataType.Date)]
        public DateTime? DateProchaineVisite { get; set; }
        
        [Display(Name = "Soin terminé")]
        public bool EstTermine { get; set; } = true;
        
        // Clés étrangères
        [Required(ErrorMessage = "Le vétérinaire est obligatoire")]
        [Display(Name = "Vétérinaire")]
        public int VeterinaireId { get; set; }
        public virtual Employe Veterinaire { get; set; } = null!;
        
        [Required(ErrorMessage = "Le renard est obligatoire")]
        [Display(Name = "Renard")]
        public int RenardId { get; set; }
        public virtual Renard Renard { get; set; } = null!;
        
        // Propriétés calculées
        [Display(Name = "Résumé")]
        public string Resume => $"{TypeSoin} - {DateSoin:dd/MM/yyyy} - {Cout:C}";
        
        [Display(Name = "Durée depuis le soin")]
        public string DureeDepuisSoin
        {
            get
            {
                var duree = DateTime.Now - DateSoin;
                if (duree.Days == 0) return "Aujourd'hui";
                if (duree.Days == 1) return "Hier";
                if (duree.Days < 7) return $"Il y a {duree.Days} jours";
                if (duree.Days < 30) return $"Il y a {duree.Days / 7} semaine(s)";
                return $"Il y a {duree.Days / 30} mois";
            }
        }
        
        // Méthodes métier
        /// <summary>
        /// Détermine si le soin est urgent
        /// </summary>
        public bool EstUrgent()
        {
            return TypeSoin == TypeSoin.Urgence || 
                   TypeSoin == TypeSoin.Chirurgie;
        }
        
        /// <summary>
        /// Détermine si le soin est récent (moins de 7 jours)
        /// </summary>
        public bool EstRecent()
        {
            return (DateTime.Now - DateSoin).Days <= 7;
        }
        
        /// <summary>
        /// Détermine si une visite de suivi est prévue
        /// </summary>
        public bool ASuivi()
        {
            return DateProchaineVisite.HasValue && DateProchaineVisite.Value > DateTime.Now;
        }
        
        /// <summary>
        /// Détermine si le suivi est en retard
        /// </summary>
        public bool SuiviEnRetard()
        {
            return DateProchaineVisite.HasValue && 
                   DateProchaineVisite.Value < DateTime.Now && 
                   !EstTermine;
        }
        
        /// <summary>
        /// Obtient la priorité du soin (1 = très urgent, 5 = routine)
        /// </summary>
        public int ObtenirPriorite()
        {
            return TypeSoin switch
            {
                TypeSoin.Urgence => 1,
                TypeSoin.Chirurgie => 2,
                TypeSoin.Traitement => 3,
                TypeSoin.Consultation => 4,
                TypeSoin.Controle => 5,
                _ => 4
            };
        }
        
        /// <summary>
        /// Obtient la couleur d'affichage selon le type de soin
        /// </summary>
        public string ObtenirCouleurAffichage()
        {
            return TypeSoin switch
            {
                TypeSoin.Urgence => "danger",
                TypeSoin.Chirurgie => "warning",
                TypeSoin.Traitement => "info",
                TypeSoin.Consultation => "primary",
                TypeSoin.Controle => "success",
                TypeSoin.Vaccination => "secondary",
                _ => "light"
            };
        }
        
        /// <summary>
        /// Obtient l'icône d'affichage selon le type de soin
        /// </summary>
        public string ObtenirIcone()
        {
            return TypeSoin switch
            {
                TypeSoin.Urgence => "fas fa-exclamation-triangle",
                TypeSoin.Chirurgie => "fas fa-cut",
                TypeSoin.Traitement => "fas fa-pills",
                TypeSoin.Consultation => "fas fa-stethoscope",
                TypeSoin.Controle => "fas fa-check-circle",
                TypeSoin.Vaccination => "fas fa-syringe",
                TypeSoin.Radiographie => "fas fa-x-ray",
                TypeSoin.AnalyseSanguine => "fas fa-vial",
                _ => "fas fa-medical-kit"
            };
        }
        
        /// <summary>
        /// Calcule le coût avec les frais annexes (10% de frais de gestion)
        /// </summary>
        public decimal CalculerCoutTotal()
        {
            return Cout * 1.10m; // Ajout de 10% de frais de gestion
        }
        
        /// <summary>
        /// Marque le soin comme terminé
        /// </summary>
        public void MarquerCommeTermine()
        {
            EstTermine = true;
            DateProchaineVisite = null;
        }
        
        /// <summary>
        /// Programme une visite de suivi
        /// </summary>
        public void ProgrammerSuivi(DateTime dateSuivi)
        {
            if (dateSuivi > DateTime.Now)
            {
                DateProchaineVisite = dateSuivi;
                EstTermine = false;
            }
        }
        
        /// <summary>
        /// Obtient un résumé détaillé du soin
        /// </summary>
        public string ObtenirResume()
        {
            var resume = $"{TypeSoin} effectué le {DateSoin:dd/MM/yyyy} par {Veterinaire?.NomComplet ?? "Vétérinaire non renseigné"}";
            
            if (!string.IsNullOrEmpty(Medicaments))
                resume += $"\nMédicaments : {Medicaments}";
                
            if (DateProchaineVisite.HasValue)
                resume += $"\nProchain contrôle : {DateProchaineVisite:dd/MM/yyyy}";
                
            return resume;
        }
    }
}