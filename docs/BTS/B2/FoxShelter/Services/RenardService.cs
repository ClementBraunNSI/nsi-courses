using Microsoft.EntityFrameworkCore;
using FoxShelter.Data;
using FoxShelter.Models.Entities;
using FoxShelter.Models.Enums;

namespace FoxShelter.Services
{
    /// <summary>
    /// Service métier pour la gestion des renards
    /// </summary>
    public class RenardService
    {
        private readonly FoxShelterContext _context;
        
        public RenardService(FoxShelterContext context)
        {
            _context = context;
        }
        
        /// <summary>
        /// Obtient tous les renards avec leurs relations
        /// </summary>
        public async Task<List<Renard>> ObtenirTousLesRenardsAsync()
        {
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Include(r => r.Soins)
                    .ThenInclude(s => s.Veterinaire)
                .OrderBy(r => r.Nom)
                .ToListAsync();
        }
        
        /// <summary>
        /// Obtient un renard par son ID
        /// </summary>
        public async Task<Renard?> ObtenirRenardParIdAsync(int id)
        {
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Include(r => r.Soins)
                    .ThenInclude(s => s.Veterinaire)
                .FirstOrDefaultAsync(r => r.Id == id);
        }
        
        /// <summary>
        /// Obtient les renards non adoptés
        /// </summary>
        public async Task<List<Renard>> ObtenirRenardsNonAdoptesAsync()
        {
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Where(r => !r.EstAdopte)
                .OrderBy(r => r.DateArrivee)
                .ToListAsync();
        }
        
        /// <summary>
        /// Obtient les renards par état de santé
        /// </summary>
        public async Task<List<Renard>> ObtenirRenardsParEtatSanteAsync(EtatSante etatSante)
        {
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Where(r => r.EtatSante == etatSante)
                .OrderBy(r => r.Nom)
                .ToListAsync();
        }
        
        /// <summary>
        /// Obtient les renards nécessitant une attention urgente
        /// </summary>
        public async Task<List<Renard>> ObtenirRenardsUrgentsAsync()
        {
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Include(r => r.Soins)
                .Where(r => r.EtatSante == EtatSante.Critique || 
                           r.EtatSante == EtatSante.Faible)
                .OrderBy(r => r.EtatSante)
                .ThenBy(r => r.DateArrivee)
                .ToListAsync();
        }
        
        /// <summary>
        /// Recherche des renards par nom ou espèce
        /// </summary>
        public async Task<List<Renard>> RechercherRenardsAsync(string terme)
        {
            if (string.IsNullOrWhiteSpace(terme))
                return await ObtenirTousLesRenardsAsync();
                
            terme = terme.ToLower();
            
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Where(r => r.Nom.ToLower().Contains(terme) || 
                           r.Espece.ToLower().Contains(terme) ||
                           (r.Description != null && r.Description.ToLower().Contains(terme)))
                .OrderBy(r => r.Nom)
                .ToListAsync();
        }
        
        /// <summary>
        /// Ajoute un nouveau renard
        /// </summary>
        public async Task<Renard> AjouterRenardAsync(Renard renard)
        {
            // Validation métier
            var erreurs = ValiderRenard(renard);
            if (erreurs.Any())
                throw new ArgumentException($"Erreurs de validation : {string.Join(", ", erreurs)}");
            
            // Vérifier l'unicité du nom
            var nomExiste = await _context.Renards
                .AnyAsync(r => r.Nom.ToLower() == renard.Nom.ToLower());
            if (nomExiste)
                throw new ArgumentException($"Un renard avec le nom '{renard.Nom}' existe déjà");
            
            renard.DateCreation = DateTime.Now;
            renard.DateModification = DateTime.Now;
            
            _context.Renards.Add(renard);
            await _context.SaveChangesAsync();
            
            return renard;
        }
        
        /// <summary>
        /// Met à jour un renard existant
        /// </summary>
        public async Task<Renard> ModifierRenardAsync(Renard renard)
        {
            var renardExistant = await _context.Renards.FindAsync(renard.Id);
            if (renardExistant == null)
                throw new ArgumentException($"Aucun renard trouvé avec l'ID {renard.Id}");
            
            // Validation métier
            var erreurs = ValiderRenard(renard);
            if (erreurs.Any())
                throw new ArgumentException($"Erreurs de validation : {string.Join(", ", erreurs)}");
            
            // Vérifier l'unicité du nom (sauf pour le renard actuel)
            var nomExiste = await _context.Renards
                .AnyAsync(r => r.Nom.ToLower() == renard.Nom.ToLower() && r.Id != renard.Id);
            if (nomExiste)
                throw new ArgumentException($"Un autre renard avec le nom '{renard.Nom}' existe déjà");
            
            // Mise à jour des propriétés
            renardExistant.Nom = renard.Nom;
            renardExistant.Espece = renard.Espece;
            renardExistant.Age = renard.Age;
            renardExistant.Sexe = renard.Sexe;
            renardExistant.EtatSante = renard.EtatSante;
            renardExistant.Poids = renard.Poids;
            renardExistant.Description = renard.Description;
            renardExistant.RegimeAlimentaireId = renard.RegimeAlimentaireId;
            renardExistant.DateModification = DateTime.Now;
            
            await _context.SaveChangesAsync();
            
            return renardExistant;
        }
        
        /// <summary>
        /// Marque un renard comme adopté
        /// </summary>
        public async Task<bool> MarquerCommeAdopteAsync(int renardId, DateTime? dateAdoption = null)
        {
            var renard = await _context.Renards.FindAsync(renardId);
            if (renard == null)
                return false;
            
            if (!renard.PeutEtreAdopte())
                throw new InvalidOperationException("Ce renard ne peut pas être adopté dans son état actuel");
            
            renard.MarquerCommeAdopte();
            await _context.SaveChangesAsync();
            
            return true;
        }
        
        /// <summary>
        /// Modifie l'état de santé d'un renard
        /// </summary>
        public async Task<bool> ModifierEtatSanteAsync(int renardId, EtatSante nouvelEtat, string? commentaire = null)
        {
            var renard = await _context.Renards.FindAsync(renardId);
            if (renard == null)
                return false;
            
            renard.ModifierEtatSante(nouvelEtat);
            await _context.SaveChangesAsync();
            
            return true;
        }
        
        /// <summary>
        /// Supprime un renard (soft delete en marquant comme adopté)
        /// </summary>
        public async Task<bool> SupprimerRenardAsync(int id)
        {
            var renard = await _context.Renards.FindAsync(id);
            if (renard == null)
                return false;
            
            // Vérifier s'il y a des soins en cours
            var soinsEnCours = await _context.SoinsVeterinaires
                .AnyAsync(s => s.RenardId == id && !s.EstTermine);
            
            if (soinsEnCours)
                throw new InvalidOperationException("Impossible de supprimer un renard ayant des soins en cours");
            
            _context.Renards.Remove(renard);
            await _context.SaveChangesAsync();
            
            return true;
        }
        
        /// <summary>
        /// Obtient les statistiques des renards
        /// </summary>
        public async Task<StatistiquesRenards> ObtenirStatistiquesAsync()
        {
            var renards = await _context.Renards.ToListAsync();
            
            return new StatistiquesRenards
            {
                NombreTotal = renards.Count,
                NombreAdoptes = renards.Count(r => r.EstAdopte),
                NombreNonAdoptes = renards.Count(r => !r.EstAdopte),
                NombreCritiques = renards.Count(r => r.EtatSante == EtatSante.Critique),
                NombreMalades = renards.Count(r => r.EtatSante == EtatSante.Faible),
                NombreEnConvalescence = renards.Count(r => r.EtatSante == EtatSante.Stable),
                NombreEnBonneSante = renards.Count(r => r.EtatSante == EtatSante.Bon),
                NombreExcellents = renards.Count(r => r.EtatSante == EtatSante.Excellent),
                PoidsMovenKg = renards.Where(r => r.Poids.HasValue).Select(r => r.Poids!.Value).DefaultIfEmpty(0).Average(),
                AgeMovenAnnees = Convert.ToDecimal(renards.Where(r => r.Age.HasValue).Select(r => (double)r.Age!.Value).DefaultIfEmpty(0).Average()),
                DureeMovenneSejourJours = renards.Average(r => r.CalculerDureeSejourJours()),
                CoutTotalSoins = await _context.SoinsVeterinaires.SumAsync(s => s.Cout)
            };
        }
        
        /// <summary>
        /// Obtient les renards arrivés récemment
        /// </summary>
        public async Task<List<Renard>> ObtenirNouveauxArrivantsAsync(int nombreJours = 7)
        {
            var dateLimit = DateTime.Now.AddDays(-nombreJours);
            
            return await _context.Renards
                .Include(r => r.RegimeAlimentaire)
                .Where(r => r.DateArrivee >= dateLimit)
                .OrderByDescending(r => r.DateArrivee)
                .ToListAsync();
        }
        
        /// <summary>
        /// Obtient les renards nécessitant un suivi vétérinaire
        /// </summary>
        public async Task<List<Renard>> ObtenirRenardsNecessitantSuiviAsync()
        {
            return await _context.Renards
                .Include(r => r.Soins)
                    .ThenInclude(s => s.Veterinaire)
                .Where(r => r.Soins.Any(s => s.DateProchaineVisite.HasValue && 
                                           s.DateProchaineVisite.Value <= DateTime.Now.AddDays(3)))
                .OrderBy(r => r.Soins.Where(s => s.DateProchaineVisite.HasValue)
                                   .Min(s => s.DateProchaineVisite))
                .ToListAsync();
        }
        
        /// <summary>
        /// Valide les données d'un renard
        /// </summary>
        private List<string> ValiderRenard(Renard renard)
        {
            var erreurs = new List<string>();
            
            if (string.IsNullOrWhiteSpace(renard.Nom))
                erreurs.Add("Le nom est obligatoire");
            
            if (string.IsNullOrWhiteSpace(renard.Espece))
                erreurs.Add("L'espèce est obligatoire");
            
            if (renard.Sexe != 'M' && renard.Sexe != 'F')
                erreurs.Add("Le sexe doit être 'M' ou 'F'");
            
            if (renard.Age.HasValue && (renard.Age < 0 || renard.Age > 20))
                erreurs.Add("L'âge doit être entre 0 et 20 ans");
            
            if (renard.Poids.HasValue && (renard.Poids <= 0 || renard.Poids > 15))
                erreurs.Add("Le poids doit être entre 0 et 15 kg");
            
            if (renard.DateArrivee > DateTime.Now)
                erreurs.Add("La date d'arrivée ne peut pas être dans le futur");
            
            return erreurs;
        }
    }
    
    /// <summary>
    /// Classe pour les statistiques des renards
    /// </summary>
    public class StatistiquesRenards
    {
        public int NombreTotal { get; set; }
        public int NombreAdoptes { get; set; }
        public int NombreNonAdoptes { get; set; }
        public int NombreCritiques { get; set; }
        public int NombreMalades { get; set; }
        public int NombreEnConvalescence { get; set; }
        public int NombreEnBonneSante { get; set; }
        public int NombreExcellents { get; set; }
        public decimal PoidsMovenKg { get; set; }
        public decimal AgeMovenAnnees { get; set; }
        public double DureeMovenneSejourJours { get; set; }
        public decimal CoutTotalSoins { get; set; }
        
        public decimal PourcentageAdoptes => NombreTotal > 0 ? (decimal)NombreAdoptes / NombreTotal * 100 : 0;
        public decimal PourcentageUrgents => NombreTotal > 0 ? (decimal)(NombreCritiques + NombreMalades) / NombreTotal * 100 : 0;
    }
}
