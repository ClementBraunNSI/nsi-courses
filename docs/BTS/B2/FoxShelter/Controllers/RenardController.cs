using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using FoxShelter.Services;
using FoxShelter.Models.Entities;
using FoxShelter.Models.Enums;
using FoxShelter.Data;
using Microsoft.EntityFrameworkCore;

namespace FoxShelter.Controllers
{
    /// <summary>
    /// Contrôleur MVC pour la gestion des renards
    /// </summary>
    public class RenardController : Controller
    {
        private readonly RenardService _renardService;
        private readonly FoxShelterContext _context;
        
        public RenardController(RenardService renardService, FoxShelterContext context)
        {
            _renardService = renardService;
            _context = context;
        }
        
        /// <summary>
        /// Page d'accueil - Liste de tous les renards
        /// </summary>
        public async Task<IActionResult> Index(string? recherche, EtatSante? etatSante, bool? adopte)
        {
            ViewBag.Recherche = recherche;
            ViewBag.EtatSante = etatSante;
            ViewBag.Adopte = adopte;
            
            // Préparer les listes déroulantes pour les filtres
            ViewBag.EtatsSante = new SelectList(Enum.GetValues<EtatSante>(), etatSante);
            ViewBag.StatutsAdoption = new SelectList(new[]
            {
                new { Value = (bool?)null, Text = "Tous" },
                new { Value = (bool?)false, Text = "Non adoptés" },
                new { Value = (bool?)true, Text = "Adoptés" }
            }, "Value", "Text", adopte);
            
            List<Renard> renards;
            
            // Appliquer les filtres
            if (!string.IsNullOrWhiteSpace(recherche))
            {
                renards = await _renardService.RechercherRenardsAsync(recherche);
            }
            else if (etatSante.HasValue)
            {
                renards = await _renardService.ObtenirRenardsParEtatSanteAsync(etatSante.Value);
            }
            else
            {
                renards = await _renardService.ObtenirTousLesRenardsAsync();
            }
            
            // Filtrer par statut d'adoption si spécifié
            if (adopte.HasValue)
            {
                renards = renards.Where(r => r.EstAdopte == adopte.Value).ToList();
            }
            
            return View(renards);
        }
        
        /// <summary>
        /// Page des détails d'un renard
        /// </summary>
        public async Task<IActionResult> Details(int id)
        {
            var renard = await _renardService.ObtenirRenardParIdAsync(id);
            if (renard == null)
            {
                TempData["Erreur"] = "Renard non trouvé";
                return RedirectToAction(nameof(Index));
            }
            
            return View(renard);
        }
        
        /// <summary>
        /// Page de création d'un nouveau renard - GET
        /// </summary>
        public async Task<IActionResult> Create()
        {
            await PreparerListesDeroulantes();
            return View();
        }
        
        /// <summary>
        /// Page de création d'un nouveau renard - POST
        /// </summary>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(Renard renard)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    await _renardService.AjouterRenardAsync(renard);
                    TempData["Succes"] = $"Le renard {renard.Nom} a été ajouté avec succès";
                    return RedirectToAction(nameof(Details), new { id = renard.Id });
                }
                catch (ArgumentException ex)
                {
                    ModelState.AddModelError("", ex.Message);
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", "Une erreur est survenue lors de l'ajout du renard");
                    // Log l'erreur ici
                }
            }
            
            await PreparerListesDeroulantes(renard.RegimeAlimentaireId);
            return View(renard);
        }
        
        /// <summary>
        /// Page de modification d'un renard - GET
        /// </summary>
        public async Task<IActionResult> Edit(int id)
        {
            var renard = await _renardService.ObtenirRenardParIdAsync(id);
            if (renard == null)
            {
                TempData["Erreur"] = "Renard non trouvé";
                return RedirectToAction(nameof(Index));
            }
            
            await PreparerListesDeroulantes(renard.RegimeAlimentaireId);
            return View(renard);
        }
        
        /// <summary>
        /// Page de modification d'un renard - POST
        /// </summary>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, Renard renard)
        {
            if (id != renard.Id)
            {
                TempData["Erreur"] = "Identifiant invalide";
                return RedirectToAction(nameof(Index));
            }
            
            if (ModelState.IsValid)
            {
                try
                {
                    await _renardService.ModifierRenardAsync(renard);
                    TempData["Succes"] = $"Le renard {renard.Nom} a été modifié avec succès";
                    return RedirectToAction(nameof(Details), new { id = renard.Id });
                }
                catch (ArgumentException ex)
                {
                    ModelState.AddModelError("", ex.Message);
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", "Une erreur est survenue lors de la modification du renard");
                    // Log l'erreur ici
                }
            }
            
            await PreparerListesDeroulantes(renard.RegimeAlimentaireId);
            return View(renard);
        }
        
        /// <summary>
        /// Page de confirmation de suppression - GET
        /// </summary>
        public async Task<IActionResult> Delete(int id)
        {
            var renard = await _renardService.ObtenirRenardParIdAsync(id);
            if (renard == null)
            {
                TempData["Erreur"] = "Renard non trouvé";
                return RedirectToAction(nameof(Index));
            }
            
            return View(renard);
        }
        
        /// <summary>
        /// Suppression confirmée - POST
        /// </summary>
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            try
            {
                var supprime = await _renardService.SupprimerRenardAsync(id);
                if (supprime)
                {
                    TempData["Succes"] = "Le renard a été supprimé avec succès";
                }
                else
                {
                    TempData["Erreur"] = "Renard non trouvé";
                }
            }
            catch (InvalidOperationException ex)
            {
                TempData["Erreur"] = ex.Message;
            }
            catch (Exception ex)
            {
                TempData["Erreur"] = "Une erreur est survenue lors de la suppression";
                // Log l'erreur ici
            }
            
            return RedirectToAction(nameof(Index));
        }
        
        /// <summary>
        /// Marquer un renard comme adopté
        /// </summary>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> MarquerAdopte(int id, DateTime? dateAdoption)
        {
            try
            {
                var succes = await _renardService.MarquerCommeAdopteAsync(id, dateAdoption);
                if (succes)
                {
                    TempData["Succes"] = "Le renard a été marqué comme adopté";
                }
                else
                {
                    TempData["Erreur"] = "Renard non trouvé";
                }
            }
            catch (InvalidOperationException ex)
            {
                TempData["Erreur"] = ex.Message;
            }
            catch (Exception ex)
            {
                TempData["Erreur"] = "Une erreur est survenue";
                // Log l'erreur ici
            }
            
            return RedirectToAction(nameof(Details), new { id });
        }
        
        /// <summary>
        /// Modifier l'état de santé d'un renard
        /// </summary>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> ModifierEtatSante(int id, EtatSante nouvelEtat, string? commentaire)
        {
            try
            {
                var succes = await _renardService.ModifierEtatSanteAsync(id, nouvelEtat, commentaire);
                if (succes)
                {
                    TempData["Succes"] = "L'état de santé a été mis à jour";
                }
                else
                {
                    TempData["Erreur"] = "Renard non trouvé";
                }
            }
            catch (Exception ex)
            {
                TempData["Erreur"] = "Une erreur est survenue lors de la mise à jour";
                // Log l'erreur ici
            }
            
            return RedirectToAction(nameof(Details), new { id });
        }
        
        /// <summary>
        /// Page des statistiques
        /// </summary>
        public async Task<IActionResult> Statistiques()
        {
            var statistiques = await _renardService.ObtenirStatistiquesAsync();
            return View(statistiques);
        }
        
        /// <summary>
        /// Page des renards urgents
        /// </summary>
        public async Task<IActionResult> Urgents()
        {
            var renardsUrgents = await _renardService.ObtenirRenardsUrgentsAsync();
            return View(renardsUrgents);
        }
        
        /// <summary>
        /// Page des nouveaux arrivants
        /// </summary>
        public async Task<IActionResult> NouveauxArrivants(int jours = 7)
        {
            ViewBag.NombreJours = jours;
            var nouveauxArrivants = await _renardService.ObtenirNouveauxArrivantsAsync(jours);
            return View(nouveauxArrivants);
        }
        
        /// <summary>
        /// Page des renards nécessitant un suivi
        /// </summary>
        public async Task<IActionResult> SuiviVeterinaire()
        {
            var renardsASuivre = await _renardService.ObtenirRenardsNecessitantSuiviAsync();
            return View(renardsASuivre);
        }
        
        /// <summary>
        /// API JSON pour obtenir les renards (pour AJAX)
        /// </summary>
        [HttpGet]
        public async Task<IActionResult> ApiRenards(string? recherche)
        {
            List<Renard> renards;
            
            if (!string.IsNullOrWhiteSpace(recherche))
            {
                renards = await _renardService.RechercherRenardsAsync(recherche);
            }
            else
            {
                renards = await _renardService.ObtenirTousLesRenardsAsync();
            }
            
            var result = renards.Select(r => new
            {
                r.Id,
                r.Nom,
                r.Espece,
                r.Age,
                r.Sexe,
                EtatSante = r.EtatSante.ToString(),
                r.EstAdopte,
                DateArrivee = r.DateArrivee.ToString("dd/MM/yyyy"),
                DureeSejourJours = r.CalculerDureeSejourJours()
            });
            
            return Json(result);
        }
        
        /// <summary>
        /// Prépare les listes déroulantes pour les formulaires
        /// </summary>
        private async Task PreparerListesDeroulantes(int? regimeSelectionne = null)
        {
            // Liste des régimes alimentaires
            var regimes = await _context.RegimesAlimentaires
                .OrderBy(r => r.Nom)
                .ToListAsync();
            ViewBag.RegimesAlimentaires = new SelectList(regimes, "Id", "Nom", regimeSelectionne);
            
            // Liste des états de santé
            ViewBag.EtatsSante = new SelectList(Enum.GetValues<EtatSante>());
            
            // Liste des sexes
            ViewBag.Sexes = new SelectList(new[]
            {
                new { Value = "M", Text = "Mâle" },
                new { Value = "F", Text = "Femelle" }
            }, "Value", "Text");
        }
        
        /// <summary>
        /// Gestion des erreurs
        /// </summary>
        public IActionResult Error()
        {
            return View();
        }
    }
}
