using System.ComponentModel.DataAnnotations;
using FoxShelter.Models.Enums;

namespace FoxShelter.Models.Entities
{
    /// <summary>
    /// Classe représentant un don fait au refuge
    /// </summary>
    public class Don
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Le type de don est obligatoire")]
        [Display(Name = "Type de don")]
        public TypeDon TypeDon { get; set; }
        
        [Required(ErrorMessage = "La date du don est obligatoire")]
        [Display(Name = "Date du don")]
        [DataType(DataType.Date)]
        public DateTime DateDon { get; set; } = DateTime.Now;
        
        [Range(0, double.MaxValue, ErrorMessage = "Le montant doit être positif")]
        [Display(Name = "Montant")]
        [DataType(DataType.Currency)]
        public decimal? Montant { get; set; }
        
        [StringLength(200)]
        [Display(Name = "Description")]
        [DataType(DataType.MultilineText)]
        public string? Description { get; set; }
        
        [Range(0, int.MaxValue, ErrorMessage = "La quantité doit être positive")]
        [Display(Name = "Quantité")]
        public int? Quantite { get; set; }
        
        [StringLength(50)]
        [Display(Name = "Unité")]
        public string? Unite { get; set; }
        
        [Required(ErrorMessage = "Le nom du donateur est obligatoire")]
        [StringLength(100)]
        [Display(Name = "Nom du donateur")]
        public string NomDonateur { get; set; } = string.Empty;
        
        [StringLength(100)]
        [Display(Name = "Prénom du donateur")]
        public string? PrenomDonateur { get; set; }
        
        [EmailAddress(ErrorMessage = "Format d'email invalide")]
        [StringLength(150)]
        [Display(Name = "Email")]
        public string? Email { get; set; }
        
        [Phone(ErrorMessage = "Format de téléphone invalide")]
        [StringLength(20)]
        [Display(Name = "Téléphone")]
        public string? Telephone { get; set; }
        
        [StringLength(300)]
        [Display(Name = "Adresse")]
        [DataType(DataType.MultilineText)]
        public string? Adresse { get; set; }
        
        [Display(Name = "Don anonyme")]
        public bool EstAnonyme { get; set; } = false;
        
        [Display(Name = "Reçu fiscal souhaité")]
        public bool RecuFiscalSouhaite { get; set; } = false;
        
        [Display(Name = "Reçu fiscal envoyé")]
        public bool RecuFiscalEnvoye { get; set; } = false;
        
        [Display(Name = "Date d'envoi du reçu")]
        [DataType(DataType.Date)]
        public DateTime? DateEnvoiRecu { get; set; }
        
        [StringLength(500)]
        [Display(Name = "Commentaires")]
        [DataType(DataType.MultilineText)]
        public string? Commentaires { get; set; }
        
        [Display(Name = "Don récurrent")]
        public bool EstRecurrent { get; set; } = false;
        
        [Display(Name = "Fréquence (en mois)")]
        [Range(1, 12, ErrorMessage = "La fréquence doit être entre 1 et 12 mois")]
        public int? FrequenceRecurrence { get; set; }
        
        [Display(Name = "Prochaine échéance")]
        [DataType(DataType.Date)]
        public DateTime? ProchaineEcheance { get; set; }
        
        [Display(Name = "Date de création")]
        public DateTime DateCreation { get; set; } = DateTime.Now;
        
        [Display(Name = "Date de modification")]
        public DateTime DateModification { get; set; } = DateTime.Now;
        
        // Propriétés calculées
        [Display(Name = "Donateur complet")]
        public string DonateurComplet
        {
            get
            {
                if (EstAnonyme) return "Donateur anonyme";
                
                var nom = NomDonateur;
                if (!string.IsNullOrEmpty(PrenomDonateur))
                    nom = $"{PrenomDonateur} {nom}";
                    
                return nom;
            }
        }
        
        [Display(Name = "Valeur estimée")]
        public string ValeurEstimee
        {
            get
            {
                return TypeDon switch
                {
                    TypeDon.Argent => Montant?.ToString("C") ?? "Non spécifié",
                    TypeDon.Nourriture or TypeDon.Matériel or TypeDon.Médicaments or TypeDon.Équipement 
                        => $"{Quantite} {Unite ?? "unité(s)"}",
                    TypeDon.Service => Description ?? "Service non spécifié",
                    _ => "Non évalué"
                };
            }
        }
        
        [Display(Name = "Statut reçu fiscal")]
        public string StatutRecuFiscal
        {
            get
            {
                if (!RecuFiscalSouhaite) return "Non demandé";
                if (RecuFiscalEnvoye) return $"Envoyé le {DateEnvoiRecu:dd/MM/yyyy}";
                return "En attente";
            }
        }
        
        [Display(Name = "Ancienneté")]
        public string Anciennete
        {
            get
            {
                var duree = DateTime.Now - DateDon;
                if (duree.TotalDays < 1) return "Aujourd'hui";
                if (duree.TotalDays < 7) return $"Il y a {duree.Days} jour(s)";
                if (duree.TotalDays < 30) return $"Il y a {duree.Days / 7} semaine(s)";
                if (duree.TotalDays < 365) return $"Il y a {duree.Days / 30} mois";
                return $"Il y a {duree.Days / 365} an(s)";
            }
        }
        
        // Méthodes métier
        /// <summary>
        /// Calcule la valeur monétaire estimée du don
        /// </summary>
        public decimal CalculerValeurMonetaire()
        {
            return TypeDon switch
            {
                TypeDon.Argent => Montant ?? 0,
                TypeDon.Nourriture => (Quantite ?? 0) * 2.5m, // Estimation 2.5€/kg
                TypeDon.Matériel => (Quantite ?? 0) * 15m, // Estimation 15€/unité
                TypeDon.Médicaments => (Quantite ?? 0) * 25m, // Estimation 25€/unité
                TypeDon.Équipement => (Quantite ?? 0) * 50m, // Estimation 50€/unité
                TypeDon.Service => Montant ?? 0, // Valeur estimée du service
                _ => 0
            };
        }
        
        /// <summary>
        /// Détermine si le don nécessite un reçu fiscal
        /// </summary>
        public bool NecessiteRecuFiscal()
        {
            return RecuFiscalSouhaite && !RecuFiscalEnvoye && 
                   TypeDon == TypeDon.Argent && (Montant ?? 0) > 0;
        }
        
        /// <summary>
        /// Marque le reçu fiscal comme envoyé
        /// </summary>
        public void MarquerRecuEnvoye()
        {
            RecuFiscalEnvoye = true;
            DateEnvoiRecu = DateTime.Now;
            DateModification = DateTime.Now;
        }
        
        /// <summary>
        /// Calcule la prochaine échéance pour un don récurrent
        /// </summary>
        public void CalculerProchaineEcheance()
        {
            if (EstRecurrent && FrequenceRecurrence.HasValue)
            {
                ProchaineEcheance = DateDon.AddMonths(FrequenceRecurrence.Value);
            }
        }
        
        /// <summary>
        /// Vérifie si le don est échu (pour les dons récurrents)
        /// </summary>
        public bool EstEchu()
        {
            return EstRecurrent && ProchaineEcheance.HasValue && 
                   ProchaineEcheance.Value <= DateTime.Now;
        }
        
        /// <summary>
        /// Obtient la catégorie du don pour les statistiques
        /// </summary>
        public string ObtenirCategorie()
        {
            var valeur = CalculerValeurMonetaire();
            
            return valeur switch
            {
                < 25 => "Petit don",
                >= 25 and < 100 => "Don moyen",
                >= 100 and < 500 => "Don important",
                >= 500 and < 1000 => "Don majeur",
                >= 1000 => "Don exceptionnel",
                _ => "Non évalué"
            };
        }
        
        /// <summary>
        /// Génère un message de remerciement personnalisé
        /// </summary>
        public string GenererMessageRemerciement()
        {
            var donateur = EstAnonyme ? "Cher donateur anonyme" : $"Cher(e) {DonateurComplet}";
            var typeMessage = TypeDon switch
            {
                TypeDon.Argent => $"votre généreux don de {Montant:C}",
                TypeDon.Nourriture => $"votre don de nourriture ({ValeurEstimee})",
                TypeDon.Matériel => $"votre don de matériel ({ValeurEstimee})",
                TypeDon.Service => $"votre aide bénévole ({Description})",
                TypeDon.Médicaments => $"votre don de médicaments ({ValeurEstimee})",
                TypeDon.Équipement => $"votre don d'équipement ({ValeurEstimee})",
                _ => "votre généreux don"
            };
            
            return $"{donateur},\n\nNous vous remercions chaleureusement pour {typeMessage}. " +
                   $"Grâce à votre soutien, nous pouvons continuer à prendre soin des renards en détresse.\n\n" +
                   $"Cordialement,\nL'équipe du refuge FoxShelter";
        }
        
        /// <summary>
        /// Valide les données du don
        /// </summary>
        public List<string> ValiderDon()
        {
            var erreurs = new List<string>();
            
            if (TypeDon == TypeDon.Argent && (!Montant.HasValue || Montant <= 0))
                erreurs.Add("Le montant est obligatoire pour un don en argent");
                
            if (TypeDon != TypeDon.Argent && TypeDon != TypeDon.Service && 
                (!Quantite.HasValue || Quantite <= 0))
                erreurs.Add("La quantité est obligatoire pour ce type de don");
                
            if (EstRecurrent && !FrequenceRecurrence.HasValue)
                erreurs.Add("La fréquence est obligatoire pour un don récurrent");
                
            if (RecuFiscalSouhaite && string.IsNullOrEmpty(Adresse))
                erreurs.Add("L'adresse est obligatoire pour l'envoi du reçu fiscal");
                
            if (DateDon > DateTime.Now)
                erreurs.Add("La date du don ne peut pas être dans le futur");
            
            return erreurs;
        }
        
        /// <summary>
        /// Crée un don récurrent basé sur ce don
        /// </summary>
        public Don CreerDonRecurrentSuivant()
        {
            if (!EstRecurrent || !FrequenceRecurrence.HasValue)
                throw new InvalidOperationException("Ce don n'est pas récurrent");
                
            return new Don
            {
                TypeDon = this.TypeDon,
                DateDon = this.ProchaineEcheance ?? DateTime.Now,
                Montant = this.Montant,
                Description = this.Description,
                Quantite = this.Quantite,
                Unite = this.Unite,
                NomDonateur = this.NomDonateur,
                PrenomDonateur = this.PrenomDonateur,
                Email = this.Email,
                Telephone = this.Telephone,
                Adresse = this.Adresse,
                EstAnonyme = this.EstAnonyme,
                RecuFiscalSouhaite = this.RecuFiscalSouhaite,
                EstRecurrent = this.EstRecurrent,
                FrequenceRecurrence = this.FrequenceRecurrence,
                Commentaires = "Don récurrent automatique"
            };
        }
    }
}