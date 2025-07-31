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
  width: 400%; /* 4 slides × 100% */
}

.category-carousel-item {
  flex: 0 0 25%; /* 100% / 4 slides = 25% each */
  min-height: 600px;
  width: 25%;
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
  background: linear-gradient(135deg, #667eea, #764ba2);
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
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
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
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
  background: rgba(102, 126, 234, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-indicator.active {
  background: linear-gradient(135deg, #667eea, #764ba2);
  transform: scale(1.2);
}

/* Bandeau de niveau harmonisé avec index.md */
.level-header {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3);
  text-align: center;
  transition: transform 0.3s ease;
  margin: 2rem 0;
}

.level-header:hover {
  transition: transform 0.6s ease;
  transform: translateY(-15px);
}

.level-header:hover img {
  box-shadow: 0 0 15px rgba(102, 126, 234, 0);
  filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.8));
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
  background: linear-gradient(135deg, #667eea, #764ba2);
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

/* Bandeau de niveau */
.level-header {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  margin: 2rem 0;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-left: 5px solid #667eea;
}

<style>
/* Navigation ultra moderne harmonisée avec index.md */
.modern-nav {
    padding: 2rem 0;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
}

.nav-header {
    text-align: center;
    margin-bottom: 3rem;
}

.nav-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, auto);
    gap: 2rem;
    padding: 2rem;
    max-width: 1400px;
    margin: 0 auto;
    align-items: start;
    grid-auto-flow: row dense;
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

/* Couleurs thématiques par catégorie - Seconde */
.category-web {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.3), rgba(155, 89, 182, 0.3));
    border: 1px solid rgba(52, 152, 219, 0.2);
}

.category-programming {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.3), rgba(39, 174, 96, 0.3));
    border: 1px solid rgba(46, 204, 113, 0.2);
}

.category-multimedia {
    background: linear-gradient(135deg, rgba(230, 126, 34, 0.3), rgba(231, 76, 60, 0.3));
    border: 1px solid rgba(230, 126, 34, 0.2);
}

.category-data {
    background: linear-gradient(135deg, rgba(142, 68, 173, 0.3), rgba(74, 144, 226, 0.3));
    border: 1px solid rgba(142, 68, 173, 0.2);
}

/* Responsive design */
@media (max-width: 768px) {
    .category-grid {
        grid-template-columns: 1fr;
        padding: 0 1rem;
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
.category-card:nth-child(4) { animation-delay: 0.4s; }
</style>

<script>
let currentSlideIndex = 0;
const totalSlides = 4;

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
    const translateX = -currentSlideIndex * 25;
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
    showSlide(index - 1);
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
        <img src="../../images/fox_seconde.png" alt="Seconde" class="level-logo" />
        <div>
        <h1>Seconde SNT</h1>
        <p>Sciences Numériques et Technologie</p>
        <p class="level-description">
            Découverte des enjeux du numérique dans la société contemporaine
        </p>
        </div>
    </div>
    
    <div class="category-carousel-container">
        <button class="carousel-btn" id="prevBtn" onclick="changeSlide(-1)">‹</button>
        
        <div class="carousel-wrapper">
            <div class="category-carousel-track" id="categoryCarousel">
            <!-- Catégorie Internet & Web -->
            <div class="category-carousel-item">
                <div class="category-card category-web">
                    <div class="category-header">
                        <span class="category-icon">🌐</span>
                        <h3 class="category-title">Internet & Web</h3>
                    </div>
                    <p class="category-description">
                        Découvrez le fonctionnement d'Internet, les protocoles de communication et la création de sites web
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Internet</div>
                            <div class="chapter-links">
                                <a href="../I_-_Internet/Cours/" class="chapter-link">📚 Cours principal</a>
                                <a href="../I_-_Internet/Activite/" class="chapter-link">🎯 Activité</a>
                                <a href="../I_-_Internet/Binaire_Décimal/" class="chapter-link">🔢 Binaire/Décimal</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Web</div>
                            <div class="chapter-links">
                                <a href="../II_-_Web/Cours/" class="chapter-link">📚 Cours HTML</a>
                                <a href="../II_-_Web/Projet_creation_site/" class="chapter-link">🚀 Projet création site</a>
                                <a href="../II_-_Web/monstres" class="chapter-link">🎨 Galerie des créations</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Réseaux sociaux</div>
                            <div class="chapter-links">
                                <a href="../III_-_Reseaux_sociaux/Cours/" class="chapter-link">📚 Cours théorique</a>
                                <a href="../III_-_Reseaux_sociaux/TP_reseau_social/" class="chapter-link">💻 TP Modélisation</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Programmation -->
            <div class="category-carousel-item">
                <div class="category-card category-programming">
                    <div class="category-header">
                        <span class="category-icon">🐍</span>
                        <h3 class="category-title">Programmation</h3>
                    </div>
                    <p class="category-description">
                        Initiez-vous à la programmation avec Python : variables, boucles, conditions et algorithmes
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Python - Bases</div>
                            <div class="chapter-links">
                                <a href="../IIII_-_Programmation_Python/Fiche_exercices_python/" class="chapter-link">🐍 Exercices Python</a>
                                <a href="../IIII_-_Programmation_Python/Fiche_exercices_boucles/" class="chapter-link">🔄 Exercices boucles</a>
                                <a href="../IIII_-_Programmation_Python/Fiche_exercices_conditions/" class="chapter-link">❓ Exercices conditions</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Multimédia & Données -->
            <div class="category-carousel-item">
                <div class="category-card category-multimedia">
                    <div class="category-header">
                        <span class="category-icon">📸</span>
                        <h3 class="category-title">Multimédia & Données</h3>
                    </div>
                    <p class="category-description">
                        Explorez le traitement d'images, la géolocalisation et la structuration des données numériques
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Photographie Numérique</div>
                            <div class="chapter-links">
                                <a href="../V_-_Photographie_Numerique/c_1_Photographie_Noir_et_Blanc/" class="chapter-link">⚫ Noir et Blanc</a>
                                <a href="../V_-_Photographie_Numerique/c_2_Photographie_Couleur/" class="chapter-link">🌈 Couleur</a>
                                <a href="../V_-_Photographie_Numerique/c_3_Metadonnees/" class="chapter-link">📋 Métadonnées</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Géolocalisation</div>
                            <div class="chapter-links">
                                <a href="../VI_-_Geolocalisation/La%20Géolocalisation_22_23/" class="chapter-link">🗺️ Cours géolocalisation</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Données Structurées</div>
                            <div class="chapter-links">
                                <a href="../VII_-_Donnees_Structurees/Activité%20blockly/" class="chapter-link">🧩 Activité Blockly</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Objets Connectés -->
            <div class="category-carousel-item">
                <div class="category-card category-data">
                    <div class="category-header">
                        <span class="category-icon">💡</span>
                        <h3 class="category-title">Objets Connectés</h3>
                    </div>
                    <p class="category-description">
                        Découvrez l'Internet des Objets et programmez des micro-contrôleurs avec des capteurs
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Micro:bit & IoT</div>
                            <div class="chapter-links">
                                <a href="../VIII_-_Objets_Connectes/activite/" class="chapter-link">🧩 Activité Blockly</a>
                                <a href="../VIII_-_Objets_Connectes/tp/" class="chapter-link">💻 TP Micro:bit</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="carousel-indicators">
            <span class="carousel-indicator active" onclick="currentSlide(1)"></span>
            <span class="carousel-indicator" onclick="currentSlide(2)"></span>
            <span class="carousel-indicator" onclick="currentSlide(3)"></span>
            <span class="carousel-indicator" onclick="currentSlide(4)"></span>
        </div>
    </div>
    <button class="carousel-btn" id="nextBtn" onclick="changeSlide(1)">›</button>
</div>
</div>

