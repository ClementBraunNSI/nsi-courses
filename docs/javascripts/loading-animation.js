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
            <div class="fox-progress">
                <div class="fox-icon" data-index="0">🦊</div>
                <div class="fox-icon" data-index="1">🦊</div>
                <div class="fox-icon" data-index="2">🦊</div>
                <div class="fox-icon" data-index="3">🦊</div>
                <div class="fox-icon" data-index="4">🦊</div>
            </div>
            <p class="loading-text">Chargement en cours...</p>
        </div>
    `;
    
    document.body.appendChild(loadingScreen);
}

// Fonction pour animer les icônes de renard et le remplissage du logo
function animateProgressBar() {
    const foxIcons = document.querySelectorAll('.fox-icon');
    const logoFill = document.querySelector('.logo-fill');
    let progress = 0;
    let currentFoxIndex = 0;
    
    const interval = setInterval(() => {
        // Accélérer la progression pour une ouverture plus rapide
        progress += Math.random() * 35 + 20; // Progression plus rapide entre 20% et 55%
        
        // Calculer quel renard doit être affiché
        const foxToShow = Math.floor((progress / 100) * foxIcons.length);
        
        // Afficher les renards progressivement
        for (let i = currentFoxIndex; i < foxToShow && i < foxIcons.length; i++) {
            setTimeout(() => {
                foxIcons[i].classList.add('visible');
            }, i * 100); // Délai entre chaque renard
            currentFoxIndex = i + 1;
        }
        
        if (progress >= 100) {
            progress = 100;
            // S'assurer que tous les renards sont visibles
            foxIcons.forEach((fox, index) => {
                setTimeout(() => {
                    fox.classList.add('visible');
                }, index * 50);
            });
            
            clearInterval(interval);
            // Optionnel: animation finale du logo (si définie)
            // setTimeout(() => {
            //     if (typeof animateLogoCompletion === 'function') {
            //         animateLogoCompletion();
            //     }
            // }, 400);
            // Enchaîner rapidement vers la fermeture du loading
            setTimeout(hideLoadingScreen, 600);
        }
        
        // Synchroniser le remplissage du logo avec la progression
        if (logoFill) {
            logoFill.style.height = progress + '%';
        }
    }, 180); // Mise à jour plus fréquente pour un effet plus rapide
}

// Fonction pour masquer l'écran de chargement
function hideLoadingScreen() {
    // Garde pour éviter les appels multiples
    if (window.isLoadingScreenHiding) return;
    window.isLoadingScreenHiding = true;

    const loadingScreen = document.getElementById('loading-screen');
    const mainContent = document.querySelector('.md-content');
    const logo = document.querySelector('.loading-logo');
    const loadingContainer = document.querySelector('.loading-container');
    
    if (loadingScreen && logo) {
        // Phase 1: Zoom et fade du logo (plus court)
        logo.style.transition = 'all 0.7s cubic-bezier(0.4, 0, 0.2, 1)';
        logo.style.transform = 'scale(3)';
        logo.style.opacity = '0';
        
        // Phase 2: Fade des autres éléments (plus court)
        setTimeout(() => {
            if (loadingContainer) {
                loadingContainer.style.transition = 'opacity 0.4s ease';
                loadingContainer.style.opacity = '0';
            }
        }, 350);
        
        // Phase 2.5: (Simplifiée) pas d'overlay pour éviter reflows et rollback
        
        // Phase 3: Suppression de l'écran et fade-in flat du contenu (moderne)
        setTimeout(() => {
            loadingScreen.remove();
            if (mainContent) {
                // Rendre visible et préparer le reveal
                mainContent.style.visibility = 'visible';
                // État initial: opacity à 0 pour un fade-in flat
                mainContent.style.opacity = '0';
                mainContent.style.willChange = 'opacity';
                // Déclencher le fade-in
                setTimeout(() => {
                    mainContent.style.transition = 'opacity 240ms ease-out';
                    mainContent.style.opacity = '1';
                }, 20);
                // Nettoyage après reveal
                setTimeout(() => {
                    mainContent.style.transition = '';
                    mainContent.style.willChange = '';
                }, 280);
            }
        }, 640);
    }
}

// Fonction d'initialisation
function initLoadingAnimation() {
    // Créer l'écran de chargement
    createLoadingScreen();
    
    // Masquer le contenu principal initialement
    const mainContent = document.querySelector('.md-content');
    if (mainContent) {
        // Utiliser visibility et opacity pour préparer le fade-in
        mainContent.style.visibility = 'hidden';
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
        mainContent.style.visibility = 'hidden';
    }
    // Démarrer le loading (la fermeture sera déclenchée par animateProgressBar)
    initLoadingAnimation();
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

.fox-progress {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    margin: 2rem 0 1rem 0;
    animation: fadeInUp 1s ease 0.9s both;
}

.fox-icon {
    font-size: 2rem;
    opacity: 0;
    transform: scale(0.5) rotate(-10deg);
    transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    filter: grayscale(100%) brightness(0.3);
    color: transparent;
    text-shadow: 0 0 0 rgba(255, 255, 255, 0.3);
}

.fox-icon.visible {
    opacity: 1;
    transform: scale(1) rotate(0deg);
    filter: grayscale(100%) brightness(1);
    color: transparent;
    text-shadow: 0 0 0 white;
    animation: foxBounce 0.6s ease;
}

@keyframes foxBounce {
    0% {
        transform: scale(0.5) rotate(-10deg);
    }
    50% {
        transform: scale(1.2) rotate(5deg);
    }
    100% {
        transform: scale(1) rotate(0deg);
    }
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