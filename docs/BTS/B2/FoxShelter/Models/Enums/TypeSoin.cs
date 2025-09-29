using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Enums
{
    /// <summary>
    /// Énumération représentant les différents types de soins vétérinaires
    /// </summary>
    public enum TypeSoin
    {
        [Display(Name = "Consultation")]
        Consultation = 1,
        
        [Display(Name = "Vaccination")]
        Vaccination = 2,
        
        [Display(Name = "Chirurgie")]
        Chirurgie = 3,
        
        [Display(Name = "Urgence")]
        Urgence = 4,
        
        [Display(Name = "Contrôle")]
        Controle = 5,
        
        [Display(Name = "Traitement")]
        Traitement = 6,
        
        [Display(Name = "Radiographie")]
        Radiographie = 7,
        
        [Display(Name = "Analyse sanguine")]
        AnalyseSanguine = 8
    }
}