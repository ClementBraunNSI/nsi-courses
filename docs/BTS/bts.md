<style>
/* Carrousel pour les catégories */
.category-carousel-container {
  position: relative;
  width: 100%;
  overflow: visible;
  margin: 2rem 0;
  display: flex;
  align-items: center;
  gap: 1rem;
  min-height: 650px;
}

.category-carousel-track {
  display: flex;
  transition: transform 0.5s ease;
  width: 300%; /* 3 slides × 100% */
}

.category-carousel-item {
  flex: 0 0 33.333%; /* 100% / 3 slides = 33.333% each */
  min-height: 600px;
  width: 33.333%;
  box-sizing: border-box;
}

.carousel-navigation {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1.5rem;
}

.carousel-wrapper {
  flex: 1;
  overflow: hidden;
  position: relative;
}

.carousel-btn {
  background: linear-gradient(135deg, #4a90e2, #357abd);
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(74, 144, 226, 0.3);
  flex-shrink: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  outline: none;
}

.carousel-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(74, 144, 226, 0.5);
}

.carousel-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  transform: none;
  background: linear-gradient(135deg, #ccc, #999);
}

.carousel-btn:active {
  transform: scale(0.95);
}

.carousel-indicators {
  display: flex;
  gap: 0.5rem;
}

.carousel-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(74, 144, 226, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-indicator.active {
  background: linear-gradient(135deg, #4a90e2, #357abd);
  transform: scale(1.2);
}

/* Bandeau de niveau harmonisé avec index.md */
.level-header {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(74, 144, 226, 0.3);
  text-align: center;
  transition: transform 0.3s ease;
  margin: 2rem 0;
}

.level-header:hover {
  transition: transform 0.6s ease;
  transform: translateY(-15px);
}

.level-header:hover img {
  box-shadow: 0 0 15px rgba(74, 144, 226, 0);
  filter: drop-shadow(0 0 10px rgba(74, 144, 226, 0.8));
  transition: box-shadow 0.3s ease;
}

.level-header-content {
  display: flex;
  align-items: center;
  gap: 2rem;
  justify-content: center;
}

.level-logo {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin-bottom: 1rem;
}

.level-header h1 {
  margin: 0;
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #4a90e2, #357abd);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.level-header p {
  margin: 0.5rem 0;
  color: #333;
  font-size: 1.1rem;
}

.level-description {
  font-style: italic;
  color: #555 !important;
}

@media (max-width: 768px) {
  .level-header-content {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .level-header h1 {
    font-size: 2rem;
  }
  
  .level-logo {
    width: 80px;
    height: 80px;
  }
  
  .category-carousel-container {
    gap: 0.5rem;
    min-height: 600px;
  }
  
  .carousel-btn {
    width: 50px;
    height: 50px;
    font-size: 1.5rem;
  }
}

/* Navigation ultra moderne harmonisée avec index.md */
.modern-nav {
    padding: 2rem 0;
    background: linear-gradient(135deg, rgba(74, 144, 226, 0.1), rgba(53, 122, 189, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    margin: 2rem 0;
    border: 1px solid rgba(74, 144, 226, 0.2);
}

.nav-header {
    text-align: center;
    margin-bottom: 3rem;
}

.nav-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.nav-subtitle {
    color: #7f8c8d;
    font-size: 1.1rem;
    font-weight: 300;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    padding: 2rem;
    max-width: 1400px;
    margin: 0 auto;
    align-items: start;
}

.category-card {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    height: auto;
    min-height: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.category-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    z-index: 1;
}

.category-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
}

.category-card > * {
    position: relative;
    z-index: 2;
}

.category-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.category-icon {
    font-size: 2.5rem;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
}

.category-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--md-default-fg-color);
    margin: 0;
}

.category-description {
    color: var(--md-default-fg-color--light);
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

.chapter-list {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

.chapter-item {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    padding: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.chapter-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.5s ease;
}

.chapter-item:hover {
    background: rgba(255, 255, 255, 0.8);
    border-color: rgba(255, 255, 255, 0.6);
    transform: translateX(8px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.chapter-item:hover::before {
    left: 100%;
}

.chapter-title {
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.chapter-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.chapter-link {
    background: rgba(255, 255, 255, 0.8);
    color: #34495e;
    padding: 0.4rem 0.8rem;
    border-radius: 8px;
    text-decoration: none;
    font-size: 0.85rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(5px);
}

.chapter-link:hover {
    background: rgba(255, 255, 255, 0.95);
    color: #2c3e50;
    transform: scale(1.05);
    border-color: rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Couleurs thématiques par catégorie - BTS */
.category-support {
    background: linear-gradient(135deg, rgba(74, 144, 226, 0.2), rgba(53, 122, 189, 0.2));
}

.category-programming {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(56, 142, 60, 0.2));
}

.category-systems {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.2), rgba(245, 124, 0, 0.2));
}

/* Responsive design */
@media (max-width: 1200px) {
    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        padding: 1.5rem;
    }
}

@media (max-width: 768px) {
    .categories-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
        padding: 1rem;
    }
    
    .nav-title {
        font-size: 2rem;
    }
    
    .category-card {
        padding: 1.5rem;
    }
}

/* Animation d'entrée */
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

.category-card {
    animation: fadeInUp 0.6s ease forwards;
}

.category-card:nth-child(1) { animation-delay: 0.1s; }
.category-card:nth-child(2) { animation-delay: 0.2s; }
.category-card:nth-child(3) { animation-delay: 0.3s; }
</style>

<script>
let currentSlideIndex = 0;
const totalSlides = 3;

// Fonction pour générer automatiquement les indicateurs
function generateIndicators() {
    const carouselContainer = document.querySelector('.category-carousel');
    let indicatorsContainer = carouselContainer.querySelector('.carousel-indicators');
    
    // Créer le conteneur d'indicateurs s'il n'existe pas
    if (!indicatorsContainer) {
        indicatorsContainer = document.createElement('div');
        indicatorsContainer.className = 'carousel-indicators';
        carouselContainer.appendChild(indicatorsContainer);
    }
    
    // Vider les indicateurs existants
    indicatorsContainer.innerHTML = '';
    
    // Générer les indicateurs automatiquement
    for (let i = 0; i < totalSlides; i++) {
        const indicator = document.createElement('span');
        indicator.className = 'carousel-indicator';
        if (i === 0) indicator.classList.add('active');
        indicator.onclick = () => currentSlide(i);
        indicatorsContainer.appendChild(indicator);
    }
}

function showSlide(index) {
    const track = document.getElementById('categoryCarousel');
    const indicators = document.querySelectorAll('.carousel-indicator');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    
    // Assurer que l'index est dans les limites
    if (index >= totalSlides) {
        currentSlideIndex = 0;
    } else if (index < 0) {
        currentSlideIndex = totalSlides - 1;
    } else {
        currentSlideIndex = index;
    }
    
    // Déplacer le carrousel
    const translateX = -currentSlideIndex * 33.333;
    track.style.transform = `translateX(${translateX}%)`;
    
    // Mettre à jour les indicateurs
    indicators.forEach((indicator, i) => {
        indicator.classList.toggle('active', i === currentSlideIndex);
    });
    
    // Mettre à jour les boutons
    if (prevBtn) prevBtn.disabled = currentSlideIndex === 0;
    if (nextBtn) nextBtn.disabled = currentSlideIndex === totalSlides - 1;
}

function changeSlide(direction) {
    showSlide(currentSlideIndex + direction);
}

function currentSlide(index) {
    showSlide(index);
}

// Support tactile
let startX = 0;
let endX = 0;

document.getElementById('categoryCarousel').addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
});

document.getElementById('categoryCarousel').addEventListener('touchend', (e) => {
    endX = e.changedTouches[0].clientX;
    handleSwipe();
});

function handleSwipe() {
    const threshold = 50;
    const diff = startX - endX;
    
    if (Math.abs(diff) > threshold) {
        if (diff > 0) {
            changeSlide(1); // Swipe gauche - slide suivant
        } else {
            changeSlide(-1); // Swipe droite - slide précédent
        }
    }
}

// Initialiser les indicateurs au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    generateIndicators();
    showSlide(0); // Afficher le premier slide
});

// Support clavier
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        changeSlide(-1);
    } else if (e.key === 'ArrowRight') {
        changeSlide(1);
    }
});

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    showSlide(0);
});
</script>

<!-- Bandeau de niveau -->
<div class="modern-nav">
    <div class="level-header">
        <div class="level-header-content">
            <div>
                <h1>BTS SI0</h1>
                <p>Services Informatiques aux Organisations</p>
                <p class="level-description">
                    Fondamentaux de l'informatique et des services numériques
                </p>
            </div>
        </div>
    </div>
    
    <div class="nav-header">
        <h2 class="nav-title">Blocs de Compétences</h2>
        <p class="nav-subtitle">Parcours de formation professionnalisante</p>
    </div>
    
    <div class="categories-grid">
        <!-- Bloc 1 - Support et Services -->
        <div class="category-card category-support">
            <div class="category-header">
                <span class="category-icon">🛠️</span>
                <h3 class="category-title">Bloc 1 - Support & Services</h3>
            </div>
            <p class="category-description">
                Support et mise à disposition de services informatiques, gestion du patrimoine et assistance utilisateurs
            </p>
            <div class="chapter-list">
                <div class="chapter-item">
                    <div class="chapter-title">B1.1 - Gestion du patrimoine informatique</div>
                        <a href="../B1/Patrimoine_informatique" class="chapter-link">📚 Patrimoine Informatique</a>
                    <div class="chapter-links">

                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">B1.2 - Réponse aux incidents</div>
                    <div class="chapter-links">
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">B1.3 - Présence en ligne</div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">B1.5 - Gestion de projets</div>
                    <div class="chapter-links">
                        <a href="../B1/Chemin_critique" class="chapter-link">📚 Chemin critique</a>
                        <a href="../B1/Gestion_projet" class="chapter-link">📚 Gestion de projet</a>
                        <a href="../B1/Gestion_risques" class="chapter-link">📚 Gestion des risques</a>
                        <a href="../B1/Methodes_agiles" class="chapter-link">📚 Méthodes agiles</a>
                        <a href="../B1/ITIL" class="chapter-link">📚 ITIL</a>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Programmation & Développement -->
        <div class="category-card category-programming">
            <div class="category-header">
                <span class="category-icon">💻</span>
                <h3 class="category-title">Programmation & Développement</h3>
            </div>
            <p class="category-description">
                Bases de la programmation, langages de développement et outils de création d'applications
            </p>
        </div>
        
        <!-- Cyber Sécurité -->
        <div class="category-card category-security">
            <div class="category-header">
                <span class="category-icon">🔒</span>
                <h3 class="category-title">Cyber Sécurité</h3>
            </div>
            <p class="category-description">
                Sécurité des systèmes informatiques, réseaux et services d'infrastructure
            </p>
            <div class="chapter-item">
                <div class="chapter-title">B3.1</div>
                <div class="chapter-links">
                    
                   <a href="../B3/Introduction_cybersecurite" class="chapter-link">📚 Introduction </a>
                </div>
            </div>
                <div class="chapter-title">TP Python</div>
                <div class="chapter-links">
                    
                   <a href="../B3/TP/premiers_pas_python" class="chapter-link">TP Python 1 : variables /conditions  / fonctions </a>
                </div>
            </div>


        </div>
    </div>
</div>