using System.ComponentModel.DataAnnotations;
using FoxShelter.Models.Enums;

namespace FoxShelter.Models.Entities
{
    /// <summary>
    /// Classe représentant un renard dans le refuge
    /// </summary>
    public class Renard
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le nom est obligatoire")]
        [StringLength(100, ErrorMessage = "Le nom ne peut pas dépasser 100 caractères")]
        [Display(Name = "Nom du renard")]
        public string Nom { get; set; } = string.Empty;
        
        [Required(ErrorMessage = "L'espèce est obligatoire")]
        [StringLength(50)]
        [Display(Name = "Espèce")]
        public string Espece { get; set; } = "Renard roux";
        
        [Range(0, 20, ErrorMessage = "L'âge doit être entre 0 et 20 ans")]
        [Display(Name = "Âge (années)")]
        public int? Age { get; set; }
        
        [Required(ErrorMessage = "Le sexe est obligatoire")]
        [Display(Name = "Sexe")]
        public char Sexe { get; set; } // 'M' ou 'F'
        
        [Required]
        [Display(Name = "Date d'arrivée")]
        [DataType(DataType.Date)]
        public DateTime DateArrivee { get; set; } = DateTime.Now;
        
        [Required]
        [Display(Name = "État de santé")]
        public EtatSante EtatSante { get; set; }
        
        [Range(0.1, 50.0, ErrorMessage = "Le poids doit être entre 0.1 et 50 kg")]
        [Display(Name = "Poids (kg)")]
        public decimal? Poids { get; set; }
        
        [StringLength(1000, ErrorMessage = "La description ne peut pas dépasser 1000 caractères")]
        [Display(Name = "Description")]
        [DataType(DataType.MultilineText)]
        public string? Description { get; set; }
        
        [Display(Name = "Adopté")]
        public bool EstAdopte { get; set; } = false;
        
        [Display(Name = "Régime alimentaire")]
        public int? RegimeAlimentaireId { get; set; }
        public virtual RegimeAlimentaire? RegimeAlimentaire { get; set; }
        
        // Relations
        public virtual ICollection<SoinVeterinaire> Soins { get; set; } = new List<SoinVeterinaire>();
        
        [Display(Name = "Date de création")]
        public DateTime DateCreation { get; set; } = DateTime.Now;
        
        [Display(Name = "Date de modification")]
        public DateTime DateModification { get; set; } = DateTime.Now;
        
        // Propriétés calculées
        [Display(Name = "Nom complet")]
        public string NomComplet => $"{Nom} ({Espece})";
        
        [Display(Name = "Sexe (texte)")]
        public string SexeTexte => Sexe == 'M' ? "Mâle" : "Femelle";
        
        // Méthodes métier
        /// <summary>
        /// Calcule la durée de séjour en jours
        /// </summary>
        public int CalculerDureeSejourJours()
        {
            return (DateTime.Now - DateArrivee).Days;
        }
        
        /// <summary>
        /// Détermine si le renard peut être adopté
        /// </summary>
        public bool PeutEtreAdopte()
        {
            return (EtatSante == EtatSante.Bon || EtatSante == EtatSante.Excellent) && !EstAdopte;
        }
        
        /// <summary>
        /// Calcule le coût total des soins
        /// </summary>
        public decimal CalculerCoutTotal()
        {
            return Soins?.Sum(s => s.Cout) ?? 0;
        }
        
        /// <summary>
        /// Obtient le dernier soin effectué
        /// </summary>
        public SoinVeterinaire? DernierSoin()
        {
            return Soins?.OrderByDescending(s => s.DateSoin).FirstOrDefault();
        }
        
        /// <summary>
        /// Détermine si le renard nécessite une attention urgente
        /// </summary>
        public bool NecessiteAttentionUrgente()
        {
            return EtatSante == EtatSante.Critique || 
                   (DernierSoin()?.EstUrgent() == true && 
                    DernierSoin()?.DateSoin > DateTime.Now.AddDays(-3));
        }
        
        /// <summary>
        /// Calcule l'âge approximatif si non renseigné
        /// </summary>
        public string ObtenirAgeAffichage()
        {
            if (Age.HasValue)
                return $"{Age} an{(Age > 1 ? "s" : "")}";
            
            var dureeSejourMois = CalculerDureeSejourJours() / 30;
            return dureeSejourMois < 12 ? $"~{dureeSejourMois} mois" : $"~{dureeSejourMois / 12} an(s)";
        }
        
        /// <summary>
        /// Met à jour l'état de santé et la date de modification
        /// </summary>
        public void ModifierEtatSante(EtatSante nouvelEtat)
        {
            EtatSante = nouvelEtat;
            DateModification = DateTime.Now;
        }
        
        /// <summary>
        /// Marque le renard comme adopté
        /// </summary>
        public void MarquerCommeAdopte()
        {
            if (PeutEtreAdopte())
            {
                EstAdopte = true;
                DateModification = DateTime.Now;
            }
        }
    }
}