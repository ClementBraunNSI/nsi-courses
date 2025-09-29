using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Enums
{
    /// <summary>
    /// Énumération représentant les différents types de dons
    /// </summary>
    public enum TypeDon
    {
        [Display(Name = "Don en argent")]
        Argent = 1,
        
        [Display(Name = "Don de nourriture")]
        Nourriture = 2,
        
        [Display(Name = "Don de matériel")]
        Materiel = 3,
        
        [Display(Name = "Don de service")]
        Service = 4,
        
        [Display(Name = "Don de médicaments")]
        Medicaments = 5,
        
        [Display(Name = "Don d'équipement")]
        Equipement = 6
    }
}