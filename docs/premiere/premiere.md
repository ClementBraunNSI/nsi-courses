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
  width: 500%; /* 5 slides × 100% */
}

.category-carousel-item {
  flex: 0 0 20%; /* 100% / 5 slides = 20% each */
  min-height: 600px;
  width: 20%;
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
  background: linear-gradient(135deg, #ffb347, #ff6b35);
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(255, 179, 71, 0.3);
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
  box-shadow: 0 6px 20px rgba(255, 179, 71, 0.5);
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
  background: rgba(255, 179, 71, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-indicator.active {
  background: linear-gradient(135deg, #ffb347, #ff6b35);
  transform: scale(1.2);
}

/* Bandeau de niveau harmonisé avec index.md */
.level-header {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(193, 131, 38, 0.93);
  text-align: center;
  transition: transform 0.3s ease;
  margin: 2rem 0;
}

.level-header:hover {
  transition: transform 0.6s ease;
  transform: translateY(-15px);
}

.level-header:hover img {
  box-shadow: 0 0 15px rgba(255, 127, 42, 0);
  filter: drop-shadow(0 0 10px rgba(255, 198, 55, 0.8));
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
  background: linear-gradient(135deg, #ffb347, #ff6b35);
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
    background: linear-gradient(135deg, rgba(255, 179, 71, 0.1), rgba(255, 107, 53, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    margin: 2rem 0;
    border: 1px solid rgba(255, 127, 42, 0.2);
}

.nav-header {
    text-align: center;
    margin-bottom: 3rem;
}

.nav-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffb347 0%, #ff6b35 100%);
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

/* Couleurs thématiques par catégorie - Première */
.category-data {
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.2), rgba(25, 118, 210, 0.2));
}

.category-programming {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(56, 142, 60, 0.2));
}

.category-algorithms {
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.2), rgba(123, 31, 162, 0.2));
}

.category-systems {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.2), rgba(245, 124, 0, 0.2));
}

.category-projects {
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.2), rgba(211, 47, 47, 0.2));
}

/* Responsive design */
@media (max-width: 1200px) {
    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(3, auto);
        gap: 1.5rem;
        padding: 1.5rem;
    }
}

@media (max-width: 768px) {
    .categories-grid {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(6, auto);
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
.category-card:nth-child(4) { animation-delay: 0.4s; }
.category-card:nth-child(5) { animation-delay: 0.5s; }
</style>

<script>
let currentSlideIndex = 0;
const totalSlides = 5;

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
    const translateX = -currentSlideIndex * 20;
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
        <img src="../../images/fox_premiere.png" alt="Première" class="level-logo" />
        <div>
        <h1>Première NSI</h1>
        <p>Numérique et Sciences Informatiques</p>
        <p class="level-description">
            Approfondissement des concepts informatiques et algorithmiques
        </p>
        </div>
    </div>
    
    <div class="category-carousel-container">
        <button class="carousel-btn" id="prevBtn" onclick="changeSlide(-1)">‹</button>
        
        <div class="carousel-wrapper">
            <div class="category-carousel-track" id="categoryCarousel">
            <!-- Catégorie Programmation -->
            <div class="category-carousel-item">
                <div class="category-card category-programming">
                    <div class="category-header">
                        <span class="category-icon">🛠️</span>
                        <h3 class="category-title">Programmation</h3>
                    </div>
                    <p class="category-description">
                        Constructions élémentaires, fonctions, spécifications et programmation orientée objet
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Constructions élémentaires</div>
                            <div class="chapter-links">
                                <a href="../I-Constructions_elementaires/Cours/Cours_1/" class="chapter-link">📚 Structures de base de Python</a>
                                <a href="../I-Constructions_elementaires/Cours/Cours_2/" class="chapter-link">📚 Les types</a>
                                <a href="../I-Constructions_elementaires/Cours/Cours_4/" class="chapter-link">📚 Les fonctions</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Exercices programmation</div>
                            <div class="chapter-links">
                                <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_boucles/" class="chapter-link">🔄 Boucles</a>
                                <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_fonctions/" class="chapter-link">⚙️ Fonctions</a>
                                <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_specification/" class="chapter-link">📋 Spécification</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">POO & Structures avancées</div>
                            <div class="chapter-links">
                                <a href="../XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_cours/" class="chapter-link">🏗️ POO</a>
                                <a href="../XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_piles_files/" class="chapter-link">📚 Piles & Files</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Données & Structures -->
            <div class="category-carousel-item">
                <div class="category-card category-data">
                    <div class="category-header">
                        <span class="category-icon">🗃️</span>
                        <h3 class="category-title">Données & Structures</h3>
                    </div>
                    <p class="category-description">
                        Représentation des données, structures linéaires et traitement de tables
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Représentation des données</div>
                            <div class="chapter-links">
                                <a href="../II-Representation_des_donnees/Cours/c_1_booleen_et_operations/" class="chapter-link">🔢 Booléens</a>
                                <a href="../II-Representation_des_donnees/Cours/c_2_entier_binaire_hexa/" class="chapter-link">💻 Binaire/Hexa</a>
                                <a href="../II-Representation_des_donnees/Cours/c_2_entier_relatif/" class="chapter-link">➕ Entiers relatifs</a>
                                <a href="../II-Representation_des_donnees/Cours/c_2_nombres_reels/" class="chapter-link">🔢 Nombres réels</a>
                                <a href="../II-Representation_des_donnees/Cours/c_3_caracteres/" class="chapter-link">📝 Caractères</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Structures linéaires</div>
                            <div class="chapter-links">
                                <a href="../III-Structures_de_donnees_lineaires/Cours/Cours/" class="chapter-link">📚 Listes/Tuples</a>
                                <a href="../III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercices_tuples_listes/" class="chapter-link">✏️ Exercices</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Traitement de données</div>
                            <div class="chapter-links">
                                <a href="../V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_1/" class="chapter-link">📚 Dictionnaires</a>
                                <a href="../V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_2/" class="chapter-link">📊 Traitement de données en tables</a>
                                <a href="../V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_3/" class="chapter-link">Avant-goût : SQL</a>
                                <a href="../V-Dictionnaires_et_Traitement_de_tables/Exercices/Fiche_exercices_dictionnaires/" class="chapter-link">✏️ Exercices</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Algorithmes -->
            <div class="category-carousel-item">
                <div class="category-card category-algorithms">
                    <div class="category-header">
                        <span class="category-icon">🔍</span>
                        <h3 class="category-title">Algorithmes</h3>
                    </div>
                    <p class="category-description">
                        Algorithmes de tri, recherche, stratégies gloutonnes et intelligence artificielle
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Algorithmes sur tableaux</div>
                            <div class="chapter-links">
                                <a href="../VII-Algorithmes_sur_les_tableaux/Cours/" class="chapter-link">📚 Cours</a>
                                <a href="../VII-Algorithmes_sur_les_tableaux/Mesures_de_complexite/mesure_tris/sujets_mesure_tris/" class="chapter-link">📊 Complexité</a>
                                <a href="../VII-Algorithmes_sur_les_tableaux/dicho/" class="chapter-link">🔍 Dichotomie</a>
                                
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Stratégies algorithmiques</div>
                            <div class="chapter-links">
                                <a href="../VIII-Algorithmes_Gloutons/Algorithmes%20Gloutons_22_23/" class="chapter-link">🎯 Gloutons</a>
                                <a href="../VIII-Algorithmes_Gloutons/Gloutons_exercices/" class="chapter-link">🎯 Exercices Gloutons</a>
                                <a href="../XI-K_plus_proches_voisins/Cours/" class="chapter-link">🤖 KNN</a>
                                <a href="../XI-K_plus_proches_voisins/TP_KNN/" class="chapter-link">💻 TP KNN</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Systèmes -->
            <div class="category-carousel-item">
                <div class="category-card category-systems">
                    <div class="category-header">
                        <span class="category-icon">💻</span>
                        <h3 class="category-title">Systèmes</h3>
                    </div>
                    <p class="category-description">
                        Architecture machine, systèmes d'exploitation, réseaux et protocoles web
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Architecture machine</div>
                            <div class="chapter-links">
                                <a href="../IV-Architecture_d_une_machine/Cours/Cours_1/" class="chapter-link">🖥️ Processeur</a>
                                <a href="../IV-Architecture_d_une_machine/Cours/Cours_2/" class="chapter-link">🔌 Portes logiques</a>
                                <a href="../IV-Architecture_d_une_machine/Exercices/Fiche_Exo/" class="chapter-link">💻 Exercices logiques</a>
                                <a href="../IV-Architecture_d_une_machine/Cours/Cours_3/" class="chapter-link">Jeux d'instructions</a>
                                <a href="../IV-Architecture_d_une_machine/Cours/Cours_4/" class="chapter-link">Ludopédagogie : Minecraft</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Systèmes d'exploitation</div>
                            <div class="chapter-links">
                                <a href="../VIIII-Systemes_d_exploitation_et_commandes_Linux/Cours/Cours_1/" class="chapter-link">📚 Principes</a>
                                <a href="../VIIII-Systemes_d_exploitation_et_commandes_Linux/Cours/Cours_2/" class="chapter-link">📚 Commandes Linux</a>
                                <a href="../VIIII-Systemes_d_exploitation_et_commandes_Linux/TP_Commandes_Linux/TP_commandes_linux/" class="chapter-link">🐧 TP Linux</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">Internet & Web</div>
                            <div class="chapter-links">
                                <a href="../VI-Internet_et_Reseaux/Cours/" class="chapter-link">🌐 Réseaux</a>
                                <a href="../X-Web_et_HTTP/Cours/Cours" class="chapter-link">📡 Le WEB</a>
                                <a href="../X-Web_et_HTTP/Cours/Cours_html/" class="chapter-link">📡 Notice HTML</a>
                                <a href="../X-Web_et_HTTP/TP/Projet/" class="chapter-link">🚀 Projet web</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Catégorie Projets & Évaluations -->
            <div class="category-carousel-item">
                <div class="category-card category-projects">
                    <div class="category-header">
                        <span class="category-icon">🎯</span>
                        <h3 class="category-title">Projets & Évaluations</h3>
                    </div>
                    <p class="category-description">
                        Projets créatifs, TP notés, corrections et ressources d'aide
                    </p>
                    <div class="chapter-list">
                        <div class="chapter-item">
                            <div class="chapter-title">Projets créatifs</div>
                            <div class="chapter-links">
                                <a href="../XIII-Projets/" class="chapter-link">🎨 Tous les projets</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">TP Notés</div>
                            <div class="chapter-links">
                                <a href="../XIIII-TP_notes/Carte_Bleue/verification_carte_bleue/" class="chapter-link">💳 Carte Bleue</a>
                                <a href="../XIIII-TP_notes/Code_Barre/code_barre/" class="chapter-link">📊 Code Barre</a>
                                <a href="../XIIII-TP_notes/Interro_Algo_a_savoir/sujet1_md/" class="chapter-link">📝 Interro Algo</a>
                            </div>
                        </div>
                        <div class="chapter-item">
                            <div class="chapter-title">New Year Advent</div>
                            <div class="chapter-links">
                                <a href="../New_Year_Advent/new_year_advent" class="chapter-link">🎄 New Year Advent</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        
    </div>
    <button class="carousel-btn" id="nextBtn" onclick="changeSlide(1)">›</button>
</div>
