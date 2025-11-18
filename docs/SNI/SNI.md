<style>
.md-content, .md-content__inner { box-shadow: none !important; border: 0 !important; background: transparent !important; }
.md-content, .md-content__inner { max-width: 100% !important; width: 100% !important; margin-left: auto !important; margin-right: auto !important; padding-left: clamp(0.5rem, 2vw, 2rem) !important; padding-right: clamp(0.5rem, 2vw, 2rem) !important; }
.md-main .md-container { max-width: min(1400px, 98vw) !important; width: 100% !important; }
.level-header { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 2rem; margin: 2rem 0; border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); border-left: 5px solid #2E86C1; }
.level-header-content { display: flex; align-items: center; gap: 2rem; justify-content: center; }
.level-logo { width: 100px; height: 100px; object-fit: contain; }
.level-header h1 { margin: 0; font-size: 2.5rem; font-weight: 700; color: #2E86C1; }
.level-header p { margin: 0.5rem 0; color: #333; font-size: 1.1rem; }
.level-description { font-style: italic; color: #555 !important; }
.modern-nav { padding: 2rem 0; background: linear-gradient(135deg, rgba(46, 134, 193, 0.1), rgba(26, 82, 118, 0.05)); backdrop-filter: blur(20px); border-radius: 24px; margin: 2rem 0; border: 1px solid rgba(46, 134, 193, 0.2); }
.nav-header { text-align: center; margin-bottom: 3rem; }
.nav-title { font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #2E86C1 0%, #1A5276 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
.nav-subtitle { color: #7f8c8d; font-size: 1.1rem; font-weight: 300; }
.category-carousel-container { position: relative; width: 100%; overflow: visible; margin: 2rem 0; display: flex; align-items: center; gap: 1rem; }
.carousel-wrapper { flex: 1; overflow: hidden; position: relative; }
.category-carousel-track { display: flex; transition: transform 0.5s ease; width: 700%; }
.category-carousel-item { flex: 0 0 14.2857%; min-height: 520px; width: 14.2857%; box-sizing: border-box; }
.carousel-btn { background: linear-gradient(135deg, #2E86C1, #1A5276); border: none; border-radius: 50%; width: 60px; height: 60px; color: white; font-size: 2rem; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(46, 134, 193, 0.3); flex-shrink: 0; z-index: 10; display: flex; align-items: center; justify-content: center; position: relative; outline: none; }
.carousel-btn:hover { transform: scale(1.1); box-shadow: 0 6px 20px rgba(46, 134, 193, 0.5); }
.carousel-btn:disabled { opacity: 0.3; cursor: not-allowed; transform: none; background: linear-gradient(135deg, #ccc, #999); }
.carousel-indicators { display: flex; gap: 0.5rem; justify-content: center; margin-top: 1.5rem; }
.carousel-indicator { width: 12px; height: 12px; border-radius: 50%; background: rgba(46, 134, 193, 0.3); cursor: pointer; transition: all 0.3s ease; }
.carousel-indicator.active { background: linear-gradient(135deg, #2E86C1, #1A5276); transform: scale(1.2); }
.categories-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; padding: 2rem; max-width: 1400px; margin: 0 auto; align-items: start; }
.category-card { background: var(--md-default-bg-color); border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); transition: all 0.3s ease; position: relative; overflow: hidden; min-height: 320px; display: flex; flex-direction: column; justify-content: space-between; }
.category-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%); z-index: 1; }
.category-card:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15); }
.category-card > * { position: relative; z-index: 2; }
.category-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; justify-content: center; }
.category-title { font-size: 1.4rem; font-weight: 600; color: var(--md-default-fg-color); margin: 0; }
.category-description { color: var(--md-default-fg-color--light); font-size: 0.9rem; margin-bottom: 1.5rem; line-height: 1.5; }
.chapter-list { display: flex; flex-direction: column; gap: 0.8rem; }
.chapter-item { background: rgba(255, 255, 255, 0.6); border-radius: 12px; padding: 1rem; border: 1px solid rgba(255, 255, 255, 0.4); transition: all 0.3s ease; position: relative; overflow: hidden; backdrop-filter: blur(5px); }
.chapter-title { font-weight: 600; color: #2c3e50; margin-bottom: 0.5rem; font-size: 1.1rem; }
.chapter-links { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.chapter-link { background: rgba(255, 255, 255, 0.8); color: #34495e; padding: 0.4rem 0.8rem; border-radius: 8px; text-decoration: none; font-size: 0.85rem; transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.3); backdrop-filter: blur(5px); }
@media (max-width: 768px) { .level-header-content { flex-direction: column; text-align: center; gap: 1rem; } .level-header h1 { font-size: 2rem; } .level-logo { width: 80px; height: 80px; } .category-carousel-item { flex: 0 0 100%; width: 100%; min-height: auto; padding: 0; } .carousel-wrapper { max-width: 100%; border-radius: 12px; } .carousel-btn { width: 50px; height: 50px; font-size: 1.5rem; } }
</style>

<script>
let currentSlideIndex = 0; const totalSlides = 7;
function generateIndicators() { const indicators = document.querySelector('.carousel-indicators'); if (!indicators) return; indicators.innerHTML = ''; for (let i = 0; i < totalSlides; i++) { const indicator = document.createElement('span'); indicator.className = 'carousel-indicator'; if (i === 0) indicator.classList.add('active'); indicator.onclick = () => currentSlide(i); indicators.appendChild(indicator); } }
function showSlide(index) { const track = document.getElementById('categoryCarousel'); const indicators = document.querySelectorAll('.carousel-indicator'); const prevBtn = document.getElementById('prevBtn'); const nextBtn = document.getElementById('nextBtn'); if (index >= totalSlides) { currentSlideIndex = 0; } else if (index < 0) { currentSlideIndex = totalSlides - 1; } else { currentSlideIndex = index; } const step = 100 / totalSlides; const translateX = -currentSlideIndex * step; if (track) track.style.transform = `translateX(${translateX}%)`; indicators.forEach((indicator, i) => { indicator.classList.toggle('active', i === currentSlideIndex); }); if (prevBtn) prevBtn.disabled = currentSlideIndex === 0; if (nextBtn) nextBtn.disabled = currentSlideIndex === totalSlides - 1; }
function changeSlide(direction) { showSlide(currentSlideIndex + direction); }
function currentSlide(index) { showSlide(index); }
document.addEventListener('DOMContentLoaded', function() { generateIndicators(); showSlide(0); });
</script>

<div class="modern-nav">
  <div class="level-header">
    <div class="level-header-content">
      <img src="../../images/fox_sni.png" alt="SNI" class="level-logo" />
      <div>
        <h1>3e SNI</h1>
        <p>Sciences Numériques et Informatique</p>
        <p class="level-description">Introduction aux fondamentaux du numérique</p>
      </div>
    </div>
  </div>

  <div class="nav-header">
    <h2 class="nav-title">Chapitres principaux</h2>
    <p class="nav-subtitle">Parcours de formation 3e SNI</p>
  </div>

  <div class="category-carousel-container category-carousel">
    <button class="carousel-btn" id="prevBtn" onclick="changeSlide(-1)">‹</button>
    <div class="carousel-wrapper">
      <div class="category-carousel-track" id="categoryCarousel">
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Architecture machine</h3>
            </div>
            <p class="category-description">Matériel, composants et organisation d’un système informatique</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Architecture_machine/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Cybersécurité</h3>
            </div>
            <p class="category-description">Risques numériques, bonnes pratiques et protection des systèmes</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Cybersecurite/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Intelligence artificielle</h3>
            </div>
            <p class="category-description">Principes, usages et enjeux des systèmes intelligents</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Intelligence_artificielle/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Programmation Python</h3>
            </div>
            <p class="category-description">Bases de la programmation et logique algorithmique</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Programmation_Python/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Représentation de base</h3>
            </div>
            <p class="category-description">Binaire, données et formats de représentation</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Representation_de_base/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Réseau & Communication</h3>
            </div>
            <p class="category-description">Internet, protocoles et échanges de données</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Reseau_Communication/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="category-carousel-item">
          <div class="category-card">
            <div class="category-header">
              <h3 class="category-title">Sécurisation des données</h3>
            </div>
            <p class="category-description">Vie privée, chiffrement et sauvegarde</p>
            <div class="chapter-list">
              <div class="chapter-item">
                <div class="chapter-title">Accéder au chapitre</div>
                <div class="chapter-links">
                  <a href="Securisation_donnees/" class="chapter-link">Ouvrir</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-btn" id="nextBtn" onclick="changeSlide(1)">›</button>
  </div>
  <div class="carousel-indicators"></div>
</div>