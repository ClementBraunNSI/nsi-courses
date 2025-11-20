using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Enums
{
    /// <summary>
    /// Énumération représentant l'état de santé d'un renard
    /// </summary>
    public enum EtatSante
    {
        [Display(Name = "Critique")]
        Critique = 1,
        
        [Display(Name = "Faible")]
        Faible = 2,
        
        [Display(Name = "Stable")]
        Stable = 3,
        
        [Display(Name = "Bon")]
        Bon = 4,
        
        [Display(Name = "Excellent")]
        Excellent = 5
    }
}