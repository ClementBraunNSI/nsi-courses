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
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
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
  box-shadow: 0 6px 20px rgba(231, 76, 60, 0.5);
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
  background: rgba(231, 76, 60, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-indicator.active {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  transform: scale(1.2);
}

/* Bandeau de niveau harmonisé avec index.md */
.level-header {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(231, 76, 60, 0.3);
  text-align: center;
  transition: transform 0.3s ease;
  margin: 2rem 0;
}

.level-header:hover {
  transition: transform 0.6s ease;
  transform: translateY(-15px);
}

.level-header:hover img {
  box-shadow: 0 0 15px rgba(231, 76, 60, 0);
  filter: drop-shadow(0 0 10px rgba(231, 76, 60, 0.8));
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
  background: linear-gradient(135deg, #e74c3c, #c0392b);
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
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    margin: 2rem 0;
    border: 1px solid rgba(231, 76, 60, 0.2);
}

.nav-header {
    text-align: center;
    margin-bottom: 3rem;
}

.nav-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
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

/* Couleurs thématiques par catégorie - BTS 2 */
.category-slam {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.2), rgba(192, 57, 43, 0.2));
}

.category-cybersecurity {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.2), rgba(142, 68, 173, 0.2));
}

.category-project {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.2), rgba(41, 128, 185, 0.2));
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

<!-- Bandeau de niveau -->
<div class="modern-nav">
    <div class="level-header">
        <div class="level-header-content">
            <div>
                <h1>BTS SIO 2ème Année</h1>
                <p>Services Informatiques aux Organisations</p>
                <p class="level-description">
                    Spécialisation et approfondissement des compétences professionnelles
                </p>
            </div>
        </div>
    </div>
    
    <div class="nav-header">
        <h2 class="nav-title">Blocs de Compétences Avancés</h2>
        <p class="nav-subtitle">Expertise et spécialisation professionnelle</p>
    </div>
    
    <div class="categories-grid">
        <!-- Bloc 2 - SLAM -->
        <div class="category-card category-slam">
            <div class="category-header">
                <span class="category-icon">🚀</span>
                <h3 class="category-title">Bloc 2 - SLAM</h3>
            </div>
            <p class="category-description">
                Solutions Logicielles et Applications Métiers - Conception et développement d'applications
            </p>
            <div class="chapter-list">
                <div class="chapter-item">
                    <div class="chapter-title">B2.1 - Conception d'applications</div>
                    <div class="chapter-links">
                        <a href="./B2_SLAM_Conception.md" class="chapter-link">📚 Conception & Développement SLAM</a>
                        <a href="../B2/B2_1_Conception/projets/" class="chapter-link">🎯 Projets</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">B2.2 - Développement Web</div>
                    <div class="chapter-links">
                        <a href="../B2/B2_2_Dev_Web/" class="chapter-link">📚 PHP/JavaScript</a>
                        <a href="../B2/B2_2_Dev_Web/frameworks/" class="chapter-link">⚡ Frameworks</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">B2.3 - Bases de données</div>
                    <div class="chapter-links">
                        <a href="../B2/B2_3_BDD/" class="chapter-link">📚 SQL Avancé</a>
                        <a href="../B2/B2_3_BDD/optimisation/" class="chapter-link">⚡ Optimisation</a>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Cybersécurité -->
        <div class="category-card category-cybersecurity">
            <div class="category-header">
                <span class="category-icon">🔒</span>
                <h3 class="category-title">Cybersécurité</h3>
            </div>
            <p class="category-description">
                Sécurité des systèmes d'information, protection des données et gestion des risques
            </p>
            <div class="chapter-list">
                <div class="chapter-item">
                    <div class="chapter-title">Sécurité des applications</div>
                    <div class="chapter-links">
                        <a href="./B2_Cybersecurite.md" class="chapter-link">📚 Cybersécurité pour SLAM</a>
                        <a href="../Cybersecurite/App_Security/tp/" class="chapter-link">💻 TP Sécurité</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">Cryptographie</div>
                    <div class="chapter-links">
                        <a href="../Cybersecurite/Cryptographie/" class="chapter-link">📚 Chiffrement</a>
                        <a href="../Cybersecurite/Cryptographie/exercices/" class="chapter-link">✏️ Exercices</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">Audit & Tests</div>
                    <div class="chapter-links">
                        <a href="../Cybersecurite/Audit/" class="chapter-link">📚 Méthodologie</a>
                        <a href="../Cybersecurite/Audit/outils/" class="chapter-link">🔧 Outils</a>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Projets & Stage -->
        <div class="category-card category-project">
            <div class="category-header">
                <span class="category-icon">📋</span>
                <h3 class="category-title">Projets & Stage</h3>
            </div>
            <p class="category-description">
                Projets personnalisés encadrés, stage en entreprise et préparation à l'insertion professionnelle
            </p>
            <div class="chapter-list">
                <div class="chapter-item">
                    <div class="chapter-title">PPE - Projets Encadrés</div>
                    <div class="chapter-links">
                        <a href="./B2_Projets_Stage.md" class="chapter-link">📚 Projets & Stage - Guide complet</a>
                        <a href="../Projets/PPE/exemples/" class="chapter-link">💡 Exemples</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">Stage en entreprise</div>
                    <div class="chapter-links">
                        <a href="../Stage/Preparation/" class="chapter-link">📚 Préparation</a>
                        <a href="../Stage/Rapport/" class="chapter-link">📝 Rapport</a>
                    </div>
                </div>
                <div class="chapter-item">
                    <div class="chapter-title">Veille technologique</div>
                    <div class="chapter-links">
                        <a href="../Veille/Methodologie/" class="chapter-link">📚 Méthodes</a>
                        <a href="../Veille/Outils/" class="chapter-link">🔧 Outils</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>