using System.ComponentModel.DataAnnotations;

namespace FoxShelter.Models.Entities
{
    /// <summary>
    /// Classe représentant un régime alimentaire pour les renards
    /// </summary>
    public class RegimeAlimentaire
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le nom du régime est obligatoire")]
        [StringLength(100, ErrorMessage = "Le nom ne peut pas dépasser 100 caractères")]
        [Display(Name = "Nom du régime")]
        public string Nom { get; set; } = string.Empty;
        
        [StringLength(500)]
        [Display(Name = "Description")]
        [DataType(DataType.MultilineText)]
        public string? Description { get; set; }
        
        [Required(ErrorMessage = "La fréquence des repas est obligatoire")]
        [Range(1, 10, ErrorMessage = "La fréquence doit être entre 1 et 10 repas par jour")]
        [Display(Name = "Fréquence des repas (par jour)")]
        public int FrequenceRepas { get; set; }
        
        [Required(ErrorMessage = "La quantité par repas est obligatoire")]
        [Range(0.1, 5.0, ErrorMessage = "La quantité doit être entre 0.1 et 5 kg")]
        [Display(Name = "Quantité par repas (kg)")]
        public decimal QuantiteParRepas { get; set; }
        
        [Required(ErrorMessage = "Le type de nourriture est obligatoire")]
        [StringLength(200)]
        [Display(Name = "Type de nourriture")]
        public string TypeNourriture { get; set; } = string.Empty;
        
        [Range(0, 100, ErrorMessage = "Le coût doit être positif")]
        [Display(Name = "Coût journalier")]
        [DataType(DataType.Currency)]
        public decimal CoutJournalier { get; set; }
        
        [StringLength(300)]
        [Display(Name = "Compléments alimentaires")]
        public string? ComplementsAlimentaires { get; set; }
        
        [Display(Name = "Adapté aux jeunes")]
        public bool AdapteJeunes { get; set; } = false;
        
        [Display(Name = "Adapté aux adultes")]
        public bool AdapteAdultes { get; set; } = true;
        
        [Display(Name = "Adapté aux seniors")]
        public bool AdapteSeniors { get; set; } = false;
        
        [Display(Name = "Régime médical")]
        public bool EstRegimeMedical { get; set; } = false;
        
        [StringLength(300)]
        [Display(Name = "Instructions spéciales")]
        [DataType(DataType.MultilineText)]
        public string? InstructionsSpeciales { get; set; }
        
        // Relations
        public virtual ICollection<Renard> Renards { get; set; } = new List<Renard>();
        
        // Propriétés calculées
        [Display(Name = "Quantité journalière")]
        public decimal QuantiteJournaliere => QuantiteParRepas * FrequenceRepas;
        
        [Display(Name = "Coût par kg")]
        public decimal CoutParKg => QuantiteJournaliere > 0 ? CoutJournalier / QuantiteJournaliere : 0;
        
        [Display(Name = "Type de régime")]
        public string TypeRegime
        {
            get
            {
                if (EstRegimeMedical) return "Médical";
                if (AdapteJeunes && !AdapteAdultes && !AdapteSeniors) return "Jeunes";
                if (AdapteSeniors && !AdapteJeunes && !AdapteAdultes) return "Seniors";
                if (AdapteAdultes && !AdapteJeunes && !AdapteSeniors) return "Adultes";
                return "Universel";
            }
        }
        
        // Méthodes métier
        /// <summary>
        /// Calcule le coût mensuel du régime
        /// </summary>
        public decimal CalculerCoutMensuel()
        {
            return CoutJournalier * 30;
        }
        
        /// <summary>
        /// Calcule le coût annuel du régime
        /// </summary>
        public decimal CalculerCoutAnnuel()
        {
            return CoutJournalier * 365;
        }
        
        /// <summary>
        /// Détermine si le régime est adapté à un âge donné
        /// </summary>
        public bool EstAdapteAge(int? age)
        {
            if (!age.HasValue) return AdapteAdultes; // Par défaut, considérer comme adulte
            
            return age.Value switch
            {
                < 1 => AdapteJeunes,
                >= 1 and < 7 => AdapteAdultes,
                >= 7 => AdapteSeniors,
                _ => false
            };
        }
        
        /// <summary>
        /// Calcule la quantité de nourriture pour une période donnée
        /// </summary>
        public decimal CalculerQuantitePeriode(int jours)
        {
            return QuantiteJournaliere * jours;
        }
        
        /// <summary>
        /// Calcule le coût pour une période donnée
        /// </summary>
        public decimal CalculerCoutPeriode(int jours)
        {
            return CoutJournalier * jours;
        }
        
        /// <summary>
        /// Obtient les horaires de repas recommandés
        /// </summary>
        public List<TimeSpan> ObtenirHorairesRepas()
        {
            var horaires = new List<TimeSpan>();
            
            switch (FrequenceRepas)
            {
                case 1:
                    horaires.Add(new TimeSpan(8, 0, 0)); // 8h00
                    break;
                case 2:
                    horaires.Add(new TimeSpan(8, 0, 0)); // 8h00
                    horaires.Add(new TimeSpan(18, 0, 0)); // 18h00
                    break;
                case 3:
                    horaires.Add(new TimeSpan(7, 0, 0)); // 7h00
                    horaires.Add(new TimeSpan(12, 0, 0)); // 12h00
                    horaires.Add(new TimeSpan(18, 0, 0)); // 18h00
                    break;
                case 4:
                    horaires.Add(new TimeSpan(6, 0, 0)); // 6h00
                    horaires.Add(new TimeSpan(11, 0, 0)); // 11h00
                    horaires.Add(new TimeSpan(16, 0, 0)); // 16h00
                    horaires.Add(new TimeSpan(20, 0, 0)); // 20h00
                    break;
                default:
                    // Pour plus de 4 repas, répartir équitablement sur 14h (6h-20h)
                    var intervalleHeures = 14.0 / FrequenceRepas;
                    for (int i = 0; i < FrequenceRepas; i++)
                    {
                        var heures = 6 + (i * intervalleHeures);
                        horaires.Add(TimeSpan.FromHours(heures));
                    }
                    break;
            }
            
            return horaires;
        }
        
        /// <summary>
        /// Vérifie si le régime nécessite une surveillance particulière
        /// </summary>
        public bool NecessiteSurveillance()
        {
            return EstRegimeMedical || FrequenceRepas > 4 || !string.IsNullOrEmpty(InstructionsSpeciales);
        }
        
        /// <summary>
        /// Obtient les recommandations d'âge
        /// </summary>
        public string ObtenirRecommandationsAge()
        {
            var recommandations = new List<string>();
            
            if (AdapteJeunes) recommandations.Add("Jeunes (< 1 an)");
            if (AdapteAdultes) recommandations.Add("Adultes (1-7 ans)");
            if (AdapteSeniors) recommandations.Add("Seniors (> 7 ans)");
            
            return recommandations.Count > 0 ? string.Join(", ", recommandations) : "Non spécifié";
        }
        
        /// <summary>
        /// Génère un planning de repas pour une journée
        /// </summary>
        public string GenererPlanningJournalier()
        {
            var horaires = ObtenirHorairesRepas();
            var planning = new List<string>();
            
            foreach (var horaire in horaires)
            {
                planning.Add($"{horaire:hh\\:mm} - {QuantiteParRepas:F1} kg de {TypeNourriture}");
            }
            
            return string.Join("\n", planning);
        }
        
        /// <summary>
        /// Valide la cohérence du régime
        /// </summary>
        public List<string> ValiderRegime()
        {
            var erreurs = new List<string>();
            
            if (QuantiteJournaliere > 3)
                erreurs.Add("La quantité journalière semble excessive (> 3kg)");
                
            if (CoutJournalier > 50)
                erreurs.Add("Le coût journalier semble élevé (> 50€)");
                
            if (FrequenceRepas > 6)
                erreurs.Add("La fréquence des repas semble excessive (> 6 par jour)");
                
            if (!AdapteJeunes && !AdapteAdultes && !AdapteSeniors)
                erreurs.Add("Le régime doit être adapté à au moins une tranche d'âge");
            
            return erreurs;
        }
    }
}