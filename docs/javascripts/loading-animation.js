// Animation de loading screen pour la page d'accueil

// Fonction pour créer l'écran de chargement
function createLoadingScreen() {
    const loadingScreen = document.createElement('div');
    loadingScreen.id = 'loading-screen';
    loadingScreen.innerHTML = `
        <div class="loading-container">
            <div class="logo-container">
                <img src="images/test.png" alt="Logo NSI" class="loading-logo">
            </div>
            <h1 class="welcome-text">Bienvenue</h1>
            <p class="subtitle-text">Clément Braun - NSI</p>
            <div class="loading-bar">
                <div class="loading-progress"></div>
            </div>
            <p class="loading-text">Chargement en cours...</p>
        </div>
    `;
    
    document.body.appendChild(loadingScreen);
}

// Fonction pour animer la barre de progression
function animateProgressBar() {
    const progressBar = document.querySelector('.loading-progress');
    let progress = 0;
    
    const interval = setInterval(() => {
        progress += Math.random() * 15 + 5; // Progression aléatoire entre 5% et 20%
        
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            setTimeout(hideLoadingScreen, 500); // Attendre 500ms avant de cacher l'écran
        }
        
        progressBar.style.width = progress + '%';
    }, 200); // Mise à jour toutes les 200ms
}

// Fonction pour masquer l'écran de chargement
function hideLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    const mainContent = document.querySelector('.md-content');
    const logo = document.querySelector('.loading-logo');
    const loadingContainer = document.querySelector('.loading-container');
    
    if (loadingScreen && logo) {
        // Phase 1: Zoom et fade du logo
        logo.style.transition = 'all 1.5s cubic-bezier(0.4, 0, 0.2, 1)';
        logo.style.transform = 'scale(3)';
        logo.style.opacity = '0';
        
        // Phase 2: Fade des autres éléments
        setTimeout(() => {
            if (loadingContainer) {
                loadingContainer.style.transition = 'opacity 0.8s ease';
                loadingContainer.style.opacity = '0';
            }
        }, 800);
        
        // Phase 2.5: Créer un overlay de transition
        setTimeout(() => {
            const overlay = document.createElement('div');
            overlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, rgba(255, 152, 0, 1) 0%, rgba(255, 193, 7, 1) 100%);
                z-index: 9998;
                opacity: 1;
                transition: opacity 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            `;
            document.body.appendChild(overlay);
            
            // Commencer la transition de l'overlay
            setTimeout(() => {
                overlay.style.opacity = '0';
            }, 50);
            
            // Supprimer l'overlay après la transition
            setTimeout(() => {
                if (overlay.parentNode) {
                    overlay.remove();
                }
            }, 1600);
        }, 1200);
        
        // Phase 3: Suppression de l'écran et affichage du contenu
        setTimeout(() => {
            loadingScreen.remove();
            // Animation d'entrée du contenu principal avec fade-in
            if (mainContent) {
                // État initial: complètement invisible
                mainContent.style.opacity = '0';
                mainContent.style.transform = 'scale(0.9) translateY(30px)';
                mainContent.style.filter = 'blur(5px)';
                
                // Délai pour s'assurer que l'écran de chargement est supprimé
                setTimeout(() => {
                    mainContent.style.transition = 'all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                    mainContent.style.opacity = '1';
                    mainContent.style.transform = 'scale(1) translateY(0)';
                    mainContent.style.filter = 'blur(0px)';
                }, 200);
            }
        }, 1800);
    }
}

// Fonction d'initialisation
function initLoadingAnimation() {
    // Créer l'écran de chargement
    createLoadingScreen();
    
    // Masquer le contenu principal initialement
    const mainContent = document.querySelector('.md-content');
    if (mainContent) {
        mainContent.style.opacity = '0';
    }
    
    // Démarrer l'animation après un court délai
    setTimeout(() => {
        animateProgressBar();
    }, 500);
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Masquer immédiatement le contenu principal
    const mainContent = document.querySelector('.md-content');
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.visibility = 'hidden';
    }
    
    initLoadingAnimation();
    
    // Simulation du temps de chargement (3 secondes)
    setTimeout(() => {
        // Rendre le contenu visible avant l'animation
        if (mainContent) {
            mainContent.style.visibility = 'visible';
        }
        hideLoadingScreen();
    }, 3000);
});

// Styles CSS pour l'animation
const loadingStyles = `
<style>
#loading-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 50%, #ff6b35 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    transition: all 0.6s ease;
}

.loading-container {
    text-align: center;
    color: white;
    max-width: 400px;
    padding: 2rem;
}

.logo-container {
    position: relative;
    display: inline-block;
    margin-bottom: 2rem;
}

.loading-logo {
    width: 250px;
    height: 250px;
    object-fit: contain;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.1);
    padding: 35px;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.2);
    animation: logoFloat 4s ease-in-out infinite;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.welcome-text {
    font-size: 2.5rem;
    font-weight: bold;
    margin: 1rem 0;
    animation: fadeInUp 1s ease 0.5s both;
}

.subtitle-text {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 2rem;
    animation: fadeInUp 1s ease 0.7s both;
}

.loading-bar {
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 2px;
    overflow: hidden;
    margin: 2rem 0 1rem 0;
    animation: fadeInUp 1s ease 0.9s both;
}

.loading-progress {
    height: 100%;
    background: white;
    border-radius: 2px;
    width: 0%;
    transition: width 0.3s ease;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

.loading-text {
    font-size: 1rem;
    opacity: 0.8;
    animation: fadeInUp 1s ease 1.1s both;
}

@keyframes logoFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive design */
@media (max-width: 768px) {
    .loading-container {
        padding: 1rem;
    }
    
    .loading-logo {
        width: 180px;
        height: 180px;
        padding: 25px;
    }
    
    .welcome-text {
        font-size: 2rem;
    }
    
    .subtitle-text {
        font-size: 1rem;
    }
}
</style>
`;

// Injecter les styles dans le document
document.head.insertAdjacentHTML('beforeend', loadingStyles);