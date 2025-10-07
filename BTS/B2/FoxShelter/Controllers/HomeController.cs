using Microsoft.AspNetCore.Mvc;
using FoxShelter.Services;
using FoxShelter.Models.Entities;
using System.Diagnostics;

namespace FoxShelter.Controllers
{
    /// <summary>
    /// Contrôleur principal pour la page d'accueil et les vues générales
    /// </summary>
    public class HomeController : Controller
    {
        private readonly RenardService _renardService;
        private readonly ILogger<HomeController> _logger;
        
        public HomeController(RenardService renardService, ILogger<HomeController> logger)
        {
            _renardService = renardService;
            _logger = logger;
        }
        
        /// <summary>
        /// Page d'accueil du refuge
        /// </summary>
        public async Task<IActionResult> Index()
        {
            try
            {
                // Récupérer les statistiques pour le tableau de bord
                var statistiques = await _renardService.ObtenirStatistiquesAsync();
                var renardsUrgents = await _renardService.ObtenirRenardsUrgentsAsync();
                var nouveauxArrivants = await _renardService.ObtenirNouveauxArrivantsAsync(7);
                var renardsASuivre = await _renardService.ObtenirRenardsNecessitantSuiviAsync();
                
                var viewModel = new AccueilViewModel
                {
                    Statistiques = statistiques,
                    RenardsUrgents = renardsUrgents.Take(5).ToList(),
                    NouveauxArrivants = nouveauxArrivants.Take(5).ToList(),
                    RenardsASuivre = renardsASuivre.Take(5).ToList()
                };
                
                return View(viewModel);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Erreur lors du chargement de la page d'accueil");
                TempData["Erreur"] = "Une erreur est survenue lors du chargement des données";
                return View(new AccueilViewModel());
            }
        }
        
        /// <summary>
        /// Page À propos du refuge
        /// </summary>
        public IActionResult About()
        {
            ViewData["Message"] = "FoxShelter - Refuge spécialisé dans la protection et le soin des renards";
            return View();
        }
        
        /// <summary>
        /// Page de contact
        /// </summary>
        public IActionResult Contact()
        {
            return View();
        }
        
        /// <summary>
        /// Page de confidentialité
        /// </summary>
        public IActionResult Privacy()
        {
            return View();
        }
        
        /// <summary>
        /// Page d'erreur
        /// </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel 
            { 
                RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier 
            });
        }
        
        /// <summary>
        /// API pour obtenir les données du tableau de bord en temps réel
        /// </summary>
        [HttpGet]
        public async Task<IActionResult> ApiTableauBord()
        {
            try
            {
                var statistiques = await _renardService.ObtenirStatistiquesAsync();
                var renardsUrgents = await _renardService.ObtenirRenardsUrgentsAsync();
                
                var result = new
                {
                    NombreTotal = statistiques.NombreTotal,
                    NombreUrgents = renardsUrgents.Count,
                    NombreAdoptes = statistiques.NombreAdoptes,
                    PourcentageAdoptes = statistiques.PourcentageAdoptes,
                    DerniereMiseAJour = DateTime.Now.ToString("HH:mm:ss")
                };
                
                return Json(result);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Erreur lors de la récupération des données du tableau de bord");
                return Json(new { erreur = "Erreur lors du chargement des données" });
            }
        }
    }
    
    /// <summary>
    /// ViewModel pour la page d'accueil
    /// </summary>
    public class AccueilViewModel
    {
        public StatistiquesRenards Statistiques { get; set; } = new();
        public List<Renard> RenardsUrgents { get; set; } = new();
        public List<Renard> NouveauxArrivants { get; set; } = new();
        public List<Renard> RenardsASuivre { get; set; } = new();
    }
    
    /// <summary>
    /// ViewModel pour les erreurs
    /// </summary>
    public class ErrorViewModel
    {
        public string? RequestId { get; set; }
        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
    }
}