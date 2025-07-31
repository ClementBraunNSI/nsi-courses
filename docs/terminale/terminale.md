<style>
/* Bandeau de niveau */
.level-header {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  margin: 2rem 0;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-left: 5px solid #9C27B0;
}

.level-header-content {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.level-logo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.level-header h1 {
  margin: 0;
  font-size: 2.5rem;
  font-weight: 700;
  color: #9C27B0;
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
    width: 60px;
    height: 60px;
  }
}

/* Carrousel de catégories */
.category-carousel-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 2rem 0;
    padding: 0 4rem;
}

.carousel-wrapper {
    width: 100%;
    max-width: 800px;
    overflow: hidden;
    border-radius: 20px;
    position: relative;
}

.category-carousel-track {
    display: flex;
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    width: 400%; /* 4 slides */
}

.category-carousel-item {
    flex: 0 0 25%; /* 100% / 4 slides */
    padding: 0 1rem;
    box-sizing: border-box;
}

.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(156, 39, 176, 0.9);
    color: white;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    font-size: 1.5rem;
    cursor: pointer;
    z-index: 10;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(156, 39, 176, 0.3);
}

.carousel-btn:hover {
    background: rgba(156, 39, 176, 1);
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(156, 39, 176, 0.4);
}

#prevBtn {
    left: 0;
}

#nextBtn {
    right: 0;
}

.carousel-indicators {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1.5rem;
}

.carousel-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(156, 39, 176, 0.3);
    cursor: pointer;
    transition: all 0.3s ease;
}

.carousel-indicator.active {
    background: #9C27B0;
    transform: scale(1.2);
}

@media (max-width: 768px) {
    .category-carousel-container {
        padding: 0 3rem;
    }
    
    .carousel-btn {
        width: 40px;
        height: 40px;
        font-size: 1.2rem;
    }
}

/* Navigation ultra moderne 2024 - Terminale */
.modern-nav {
    padding: 2rem 0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.1), rgba(156, 39, 176, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    margin: 2rem 0;
    border: 1px solid rgba(156, 39, 176, 0.2);
}

.nav-header {
    text-align: center;
    margin-bottom: 3rem;
}

.nav-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.nav-subtitle {
    color: var(--md-default-fg-color--light);
    font-size: 1.1rem;
    font-weight: 300;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    padding: 0 2rem;
}

.category-card {
    background: var(--md-default-bg-color);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid rgba(156, 39, 176, 0.2);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(156, 39, 176, 0.1);
    height: 100%;
    display: flex;
    flex-direction: column;
}

.category-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.category-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    border-color: rgba(255, 255, 255, 0.4);
}

.category-card:hover::before {
    opacity: 1;
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
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.chapter-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.chapter-item:hover {
    background: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateX(8px);
}

.chapter-item:hover::before {
    left: 100%;
}

.chapter-title {
    font-weight: 600;
    color: white;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.chapter-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.chapter-link {
    background: rgba(255, 255, 255, 0.1);
    color: rgba(255, 255, 255, 0.9);
    padding: 0.4rem 0.8rem;
    border-radius: 8px;
    text-decoration: none;
    font-size: 0.85rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.chapter-link:hover {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    transform: scale(1.05);
    border-color: rgba(255, 255, 255, 0.3);
}

/* Couleurs thématiques par catégorie - Terminale */
.category-structures {
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.2), rgba(211, 47, 47, 0.2));
}

.category-programming {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(56, 142, 60, 0.2));
}

.category-data {
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.2), rgba(25, 118, 210, 0.2));
}

.category-systems {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.2), rgba(245, 124, 0, 0.2));
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
// Carrousel de catégories
let currentSlideIndex = 0;
const totalSlides = 4;

function updateCarousel() {
    const track = document.getElementById('categoryCarousel');
    const indicators = document.querySelectorAll('.carousel-indicator');
    
    if (track) {
        const translateX = -currentSlideIndex * 25; // 25% par slide (100% / 4 slides)
        track.style.transform = `translateX(${translateX}%)`;
    }
    
    // Mise à jour des indicateurs
    indicators.forEach((indicator, index) => {
        indicator.classList.toggle('active', index === currentSlideIndex);
    });
}

function changeSlide(direction) {
    currentSlideIndex += direction;
    
    if (currentSlideIndex >= totalSlides) {
        currentSlideIndex = 0;
    } else if (currentSlideIndex < 0) {
        currentSlideIndex = totalSlides - 1;
    }
    
    updateCarousel();
}

function currentSlide(slideIndex) {
    currentSlideIndex = slideIndex - 1;
    updateCarousel();
}

// Support tactile
let startX = 0;
let isDragging = false;

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel-wrapper');
    
    if (carousel) {
        carousel.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
        });
        
        carousel.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            e.preventDefault();
        });
        
        carousel.addEventListener('touchend', (e) => {
            if (!isDragging) return;
            
            const endX = e.changedTouches[0].clientX;
            const diffX = startX - endX;
            
            if (Math.abs(diffX) > 50) {
                if (diffX > 0) {
                    changeSlide(1);
                } else {
                    changeSlide(-1);
                }
            }
            
            isDragging = false;
        });
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
    updateCarousel();
});
</script>

<!-- Bandeau de niveau -->


<div class="modern-nav">
    <div class="level-header">
    <div class="level-header-content">
        <img src="../../images/fox_terminale.png" alt="Terminale" class="level-logo" />
        <div>
        <h1>Terminale NSI</h1>
        <p>Numérique et Sciences Informatiques</p>
        <p class="level-description">
            Approfondissement et spécialisation en informatique
        </p>
        </div>
    </div>
    
    <div class="category-carousel-container">
        <button class="carousel-btn" id="prevBtn" onclick="changeSlide(-1)">‹</button>
        
        <div class="carousel-wrapper">
            <div class="category-carousel-track" id="categoryCarousel">
            <!-- Catégorie Structures & Algorithmes -->
            <div class="category-carousel-item">
                <div class="category-card category-structures">
                    <div class="category-header">
                        <span class="category-icon">🧱</span>
                        <h3 class="category-title">Structures & Algorithmes</h3>
                    </div>
                    <p class="category-description">
                        Structures de données avancées, algorithmes complexes et optimisation
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Structures de données</div>
                            <div class="chapter-links">
                                <a href="../I-Structures_de_donnees/Cours/Cours_1/" class="chapter-link">📋 Listes</a>
                                <a href="../I-Structures_de_donnees/Cours/Cours_2/" class="chapter-link">📚 Piles</a>
                                <a href="../I-Structures_de_donnees/Cours/Cours_3/" class="chapter-link">🚶 Files</a>
                                <a href="../I-Structures_de_donnees/Cours/Cours_5/" class="chapter-link">🌳 Arbres</a>
                                <a href="../I-Structures_de_donnees/Cours/Cours_6/" class="chapter-link">🕸️ Graphes</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Algorithmes avancés</div>
                            <div class="chapter-links">
                                <a href="../III-Algorithmes/Cours/Cours_1/" class="chapter-link">⚡ Diviser pour régner</a>
                                <a href="../III-Algorithmes/Cours/Cours_2/" class="chapter-link">🎯 Prog. dynamique</a>
                                <a href="../III-Algorithmes/Cours/Cours_3/" class="chapter-link">🔍 Recherche textuelle</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Exercices structures</div>
                            <div class="chapter-links">
                                <a href="../I-Structures_de_donnees/Fiches_d_exercices/Fiche_exercices_listes/" class="chapter-link">📝 Listes</a>
                                <a href="../I-Structures_de_donnees/Fiches_d_exercices/Fiche_exercices_piles_files/" class="chapter-link">📝 Piles/Files</a>
                                <a href="../I-Structures_de_donnees/Fiches_d_exercices/Fiche_exercices_arbres/" class="chapter-link">📝 Arbres</a>
                                <a href="../I-Structures_de_donnees/Fiches_d_exercices/Fiche_exercices_graphes/" class="chapter-link">📝 Graphes</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Programmation Avancée -->
            <div class="category-carousel-item">
                <div class="category-card category-programming">
                    <div class="category-header">
                        <span class="category-icon">🔧</span>
                        <h3 class="category-title">Programmation Avancée</h3>
                    </div>
                    <p class="category-description">
                        Récursivité, programmation orientée objet, paradigmes et modularité
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Concepts avancés</div>
                            <div class="chapter-links">
                                <a href="../II-Programmation/Cours/Cours_1/" class="chapter-link">🔄 Récursivité</a>
                                <a href="../II-Programmation/Cours/Cours_2/" class="chapter-link">🏗️ POO</a>
                                <a href="../II-Programmation/Cours/Cours_3/" class="chapter-link">📦 Modularité</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Paradigmes de programmation</div>
                            <div class="chapter-links">
                                <a href="../VI-Langages_et_programmation/Cours/Cours_1/" class="chapter-link">🎨 Paradigmes</a>
                                <a href="../VI-Langages_et_programmation/Cours/Cours_2/" class="chapter-link">⚙️ Interprétation</a>
                                <a href="../VI-Langages_et_programmation/Cours/Cours_3/" class="chapter-link">🔄 Récursivité</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Exercices programmation</div>
                            <div class="chapter-links">
                                <a href="../II-Programmation/Fiches_d_exercices/Fiche_exercices_recursivite/" class="chapter-link">📝 Récursivité</a>
                                <a href="../II-Programmation/Fiches_d_exercices/Fiche_exercices_POO/" class="chapter-link">📝 POO</a>
                                <a href="../III-Algorithmes/Fiches_d_exercices/Fiche_exercices_diviser_regner/" class="chapter-link">📝 Diviser pour régner</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Données & Graphes -->
            <div class="category-carousel-item">
                <div class="category-card category-data">
                    <div class="category-header">
                        <span class="category-icon">🌐</span>
                        <h3 class="category-title">Données & Graphes</h3>
                    </div>
                    <p class="category-description">
                        Bases de données relationnelles, SQL et traitement de données complexes
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Bases de données</div>
                            <div class="chapter-links">
                                <a href="../IV-Bases_de_donnees/Cours/Cours_1/" class="chapter-link">🗃️ Modèle relationnel</a>
                                <a href="../IV-Bases_de_donnees/Cours/Cours_2/" class="chapter-link">💾 SQL</a>
                                <a href="../IV-Bases_de_donnees/Fiches_d_exercices/Fiche_exercices_SQL/" class="chapter-link">📝 Exercices SQL</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Structures avancées</div>
                            <div class="chapter-links">
                                <a href="../I-Structures_de_donnees/Cours/Cours_4/" class="chapter-link">📖 Dictionnaires</a>
                                <a href="../I-Structures_de_donnees/Fiches_d_exercices/Fiche_exercices_dictionnaires/" class="chapter-link">📝 Exercices dict.</a>
                                <a href="../III-Algorithmes/Fiches_d_exercices/Fiche_exercices_prog_dynamique/" class="chapter-link">📝 Prog. dynamique</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Systèmes & Réseaux -->
            <div class="category-carousel-item">
                <div class="category-card category-systems">
                    <div class="category-header">
                        <span class="category-icon">🖥️</span>
                        <h3 class="category-title">Systèmes & Réseaux</h3>
                    </div>
                    <p class="category-description">
                        Architecture matérielle, processeurs, systèmes sur puce et protocoles réseau
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Architecture matérielle</div>
                            <div class="chapter-links">
                                <a href="../V-Architectures_materielles/Cours/Cours_1/" class="chapter-link">⚙️ Processeurs</a>
                                <a href="../V-Architectures_materielles/Cours/Cours_2/" class="chapter-link">🔧 Systèmes sur puce</a>
                                <a href="../V-Architectures_materielles/Cours/Cours_3/" class="chapter-link">🔄 Gestion processus</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Réseaux & Protocoles</div>
                            <div class="chapter-links">
                                <a href="../V-Architectures_materielles/Cours/Cours_4/" class="chapter-link">🌐 Protocoles routage</a>
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

