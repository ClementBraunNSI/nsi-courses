# Clément Braun - NSI

---

<style>
.level-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

.level-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(193, 131, 38, 0.93);
    text-align: center;
    transition: transform 0.3s ease;
}

.level-card:hover {
    transition: transform 0.6s ease;
    transform: translateY(-15px);
}

.level-card:hover img {
    box-shadow: 0 0 15px rgba(255, 127, 42, 0);
    filter: drop-shadow(0 0 10px rgba(255, 198, 55, 0.8));
    transition: box-shadow 0.3s ease;
}

.level-card img {
    width: 100%;
    height: 200px;
    object-fit: contain;
    margin-bottom: 1rem;
}

.btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: white !important;
    color: orange !important;
    border: 2px solid orange;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 1rem;

}
</style>

<div class="level-cards-container">
    <div class="level-card">
        <img src="images/fox_seconde.png" alt="Seconde">
        <h2>Seconde</h2>
        <p>Le programme de seconde</p>
        <a href="seconde/seconde" class="btn">Accéder au cours</a>
    </div>
    <div class="level-card">
        <img src="images/fox_premiere.png" alt="Première">
        <h2>Première</h2>
        <p>Le programme de première année</p>
        <a href="premiere/premiere" class="btn">Accéder au cours</a>
    </div>
    <div class="level-card">
        <img src="images/fox_terminale.png" alt="Première">
        <h2>Terminale</h2>
        <p>Le programme de deuxième année</p>
        <a href="terminale/terminale" class="btn">Accéder au cours</a>
    </div>
    <div class="level-card">
        <img src="images/chasserenarts.png" alt="Chasse aux Ren'Arts">
        <h2>Chasse aux Ren'arts</h2>
        <p>Un défi spécial pour les élèves</p>
        <a href="chasse_aux_renards" class="btn">Accéder au défi</a>
    </div>
</div>
---

<style>
.teaching-overview {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 50%, #ff6b35 100%);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
}

.teaching-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.teaching-card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(255, 127, 42, 0.2);
}

.teaching-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(255, 127, 42, 0.3);
}

.teaching-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    overflow: hidden;
}

.teaching-icon img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.teaching-title {
    color: #333;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.teaching-description {
    color: #666;
    font-size: 0.9rem;
    line-height: 1.4;
}

.teaching-level {
    display: inline-block;
    background: rgba(255, 127, 42, 0.1);
    color: #ff7f2a;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-bottom: 1rem;
}
</style>

## 📚 Présentation des enseignements

<div class="teaching-overview">
    <h3 style="color: white; text-align: center; margin-bottom: 0.5rem;">Parcours Numérique et Sciences Informatiques</h3>
    <p style="color: rgba(255,255,255,0.9); text-align: center; margin-bottom: 1.5rem;">De la découverte à la spécialisation, un apprentissage progressif des sciences du numérique</p>
    
    <div class="teaching-grid">
        <div class="teaching-card">
            <div class="teaching-level">Seconde</div>
            <div class="teaching-icon">
                <img src="images/fox_seconde.png" alt="SNT">
            </div>
            <h4 class="teaching-title">Sciences Numériques et Technologie</h4>
            <p class="teaching-description">Découverte des enjeux du numérique : internet, données, réseaux sociaux, objets connectés et cybersécurité.</p>
        </div>
        
        <div class="teaching-card">
            <div class="teaching-level">Première</div>
            <div class="teaching-icon">
                <img src="images/fox_premiere.png" alt="Première NSI">
            </div>
            <h4 class="teaching-title">NSI - Spécialité</h4>
            <p class="teaching-description">Initiation à la programmation Python, algorithmes, structures de données et bases de données.</p>
        </div>
        
        <div class="teaching-card">
             <div class="teaching-level">Terminale</div>
             <div class="teaching-icon">
                 <img src="images/fox_terminale.png" alt="Terminale NSI">
             </div>
             <h4 class="teaching-title">NSI - Approfondissement</h4>
             <p class="teaching-description">Programmation orientée objet, récursivité, graphes, réseaux et développement de projets.</p>
         </div>
         
         <div class="teaching-card" style="opacity: 0.8; border: 2px dashed rgba(255, 127, 42, 0.4);">
             <div class="teaching-level" style="background: rgba(255, 127, 42, 0.2);">Post-Bac</div>
             <div class="teaching-icon">
                 <div style="width: 60px; height: 60px; background: linear-gradient(45deg, #ff8c42, #ff6b35); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: bold;">🎓</div>
             </div>
             <h4 class="teaching-title">Études Supérieures</h4>
             <p class="teaching-description">Licence informatique, IUT, écoles d'ingénieurs, BTS SIO - Approfondissement en algorithmique, systèmes et réseaux.</p>
         </div>
     </div>
 </div>

### 📋 Programmes officiels
- [Bulletin officiel de la SNT](https://www.education.gouv.fr/bo/19/Special1/MENE1901641A.htm)
- [Bulletin officiel de la première NSI](https://www.education.gouv.fr/bo/19/Special1/MENE1901633A.htm)
- [Bulletin officiel de la terminale NSI](https://www.education.gouv.fr/bo/19/Special8/MENE1921247A.htm)

<style>
.software-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    padding: 2rem 0;
}

.software-card {
    background: var(--md-default-bg-color);
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.software-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    z-index: 1;
}

.software-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
}

.software-card > * {
    position: relative;
    z-index: 2;
}

.software-logo {
    width: 80px;
    height: 80px;
    margin: 0 auto 1.5rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.software-logo img {
    width: 60px;
    height: 60px;
    object-fit: contain;
}

.software-name {
    color: var(--md-default-fg-color);
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.software-description {
    color: var(--md-default-fg-color--light);
    font-size: 0.9rem;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.availability-badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-top: 0.5rem;
}

.available {
    background: rgba(76, 175, 80, 0.2);
    color: #4CAF50;
    border: 1px solid rgba(76, 175, 80, 0.3);
}

.not-available {
    background: rgba(255, 152, 0, 0.2);
    color: #FF9800;
    border: 1px solid rgba(255, 152, 0, 0.3);
}
</style>

## 💻 Logiciels utiles

<div class="software-grid">
    <div class="software-card">
        <div class="software-logo">
            <img src="https://code.visualstudio.com/assets/images/code-stable.png" alt="VS Code" style="width: 60px; height: 60px; object-fit: contain;">
        </div>
        <h3 class="software-name">Visual Studio Code</h3>
        <p class="software-description">Éditeur de code moderne avec extensions pour Python, JavaScript, C++. Interface intuitive et débogage intégré.</p>
        <span class="availability-badge available">✓ Disponible au lycée</span>
    </div>
    
    <div class="software-card">
        <div class="software-logo">
            <img src="https://user-images.githubusercontent.com/1057839/104211453-61c0f400-5434-11eb-8f52-c61c616578da.png" alt="Thonny" style="width: 60px; height: 60px; object-fit: contain;">
        </div>
        <h3 class="software-name">Thonny</h3>
        <p class="software-description">IDE Python simple et pédagogique, parfait pour débuter. Visualisation des variables et débogage pas à pas.</p>
        <span class="availability-badge available">✓ Disponible au lycée</span>
    </div>
    
    
    <div class="software-card">
        <div class="software-logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/VSCodium_Logo.png" alt="VSCodium" style="width: 60px; height: 60px; object-fit: contain;">
        </div>
        <h3 class="software-name">VSCodium</h3>
        <p class="software-description">Version open-source de VS Code sans télémétrie Microsoft. Mêmes fonctionnalités, plus de confidentialité.</p>
        <span class="availability-badge available">✓ Disponible au lycée</span>
    </div>
    
    <div class="software-card">
        <div class="software-logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/120px-PyCharm_Icon.svg.png" alt="PyCharm" style="width: 60px; height: 60px; object-fit: contain;">
        </div>
        <h3 class="software-name">PyCharm</h3>
        <p class="software-description">IDE professionnel pour Python avec refactoring avancé, débogage puissant et gestion de projets complexes.</p>
        <span class="availability-badge not-available">⚠ Installation personnelle</span>
    </div>
    
</div>

<style>
.bac-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 25px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 3rem;
    margin: 3rem 0;
    position: relative;
    overflow: hidden;
}

.bac-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    animation: rotate 20s linear infinite;
    z-index: 1;
}

.bac-section::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
    border-radius: 25px;
    z-index: 2;
}

@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.bac-content {
    position: relative;
    z-index: 3;
}

.bac-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #ffb347, #ff6b35);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.exam-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-top: 2rem;
}

.exam-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 2rem;
    position: relative;
    transition: all 0.3s ease;
}

.exam-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.exam-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
    border-radius: 20px;
    z-index: 1;
}

.exam-card > * {
    position: relative;
    z-index: 2;
}

.exam-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.exam-icon {
    width: 60px;
    height: 60px;
    border-radius: 15px;
    background: linear-gradient(135deg, #ffb347, #ff6b35);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 1rem;
    font-size: 1.5rem;
    color: white;
}

.exam-title {
    font-size: 1.3rem;
    font-weight: bold;
    margin: 0;
}

.exam-details {
    margin: 1rem 0;
}

.detail-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.detail-label {
    font-weight: 500;
    opacity: 0.8;
}

.detail-value {
    font-weight: bold;
    color: #ff7f2a;
}

.weight-indicator {
    text-align: center;
    margin-top: 1.5rem;
    padding: 1rem;
    background: rgba(255, 127, 42, 0.1);
    border-radius: 15px;
    border: 1px solid rgba(255, 127, 42, 0.2);
}

.weight-fraction {
     font-size: 2rem;
     font-weight: bold;
     color: #ff7f2a;
     display: block;
 }

/* Media queries pour mobile */
@media (max-width: 768px) {
    /* Section principale des cartes de niveau */
    .level-cards {
        grid-template-columns: 1fr;
        gap: 1rem;
        padding: 1rem 0;
    }
    
    .level-card {
        padding: 1rem;
    }
    
    .level-card img {
        height: 150px;
    }
    
    .level-card h2 {
        font-size: 1.3rem;
    }
    
    /* Section enseignements */
    .teaching-overview {
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .teaching-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .teaching-card {
        padding: 1rem;
    }
    
    .teaching-title {
        font-size: 1rem;
    }
    
    .teaching-description {
        font-size: 0.85rem;
    }
    
    /* Section logiciels */
    .software-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
        padding: 1rem 0;
    }
    
    .software-card {
        padding: 1.5rem;
    }
    
    .software-logo {
        width: 60px;
        height: 60px;
    }
    
    .software-logo img {
        width: 45px;
        height: 45px;
    }
    
    .software-name {
        font-size: 1rem;
    }
    
    .software-description {
        font-size: 0.85rem;
    }
    
    /* Section baccalauréat */
    .bac-section {
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .bac-title {
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    .exam-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .exam-card {
        padding: 1.5rem;
    }
    
    .exam-header {
        flex-direction: column;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .exam-icon {
        margin-right: 0;
        margin-bottom: 0.5rem;
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
    }
    
    .exam-title {
        font-size: 1.1rem;
    }
    
    .weight-fraction {
        font-size: 1.5rem;
    }
    
    /* Section contributeurs */
    .contributors-section {
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .section-title {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .contributors-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .contributor-card {
        padding: 1rem;
    }
    
    .contributor-avatar {
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
    }
    
    .contributor-name {
        font-size: 0.9rem;
    }
    
    .contributor-role {
        font-size: 0.8rem;
    }
    
    /* Section collègues */
    .colleagues-section {
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .colleagues-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
    
    .colleague-card {
        padding: 1rem;
        min-height: auto;
    }
    
    .colleague-header {
        margin-bottom: 0.5rem;
    }
    
    .colleague-icon {
        width: 40px;
        height: 40px;
        font-size: 1rem;
    }
    
    .colleague-name {
        font-size: 1rem;
    }
    
    .colleague-link {
        padding: 0.6rem 1rem;
        font-size: 0.9rem;
    }
}

/* Media queries pour très petits écrans */
@media (max-width: 480px) {
    .level-card {
        padding: 0.8rem;
    }
    
    .level-card h2 {
        font-size: 1.1rem;
    }
    
    .btn {
        padding: 0.4rem 0.8rem;
        font-size: 0.9rem;
    }
    
    .teaching-overview {
        padding: 1rem;
    }
    
    .bac-section {
        padding: 1rem;
    }
    
    .bac-title {
        font-size: 1.5rem;
    }
    
    .contributors-section {
        padding: 1rem;
    }
    
    .colleagues-section {
        padding: 1rem;
    }
    
    .section-title {
        font-size: 1.3rem;
    }
}
</style>

<div class="bac-section">
    <div class="bac-content">
        <h2 class="bac-title">🎓 Baccalauréat NSI</h2>
        
        <p style="text-align: center; font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">
            Le baccalauréat NSI est composé de deux épreuves complémentaires évaluant les compétences théoriques et pratiques.
        </p>
        
        <div class="exam-grid">
            <div class="exam-card">
                <div class="exam-header">
                    <div class="exam-icon">📝</div>
                    <h3 class="exam-title">Épreuve Écrite</h3>
                </div>
                
                <div class="exam-details">
                    <div class="detail-item">
                        <span class="detail-label">Durée</span>
                        <span class="detail-value">3h30</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Exercices</span>
                        <span class="detail-value">3 exercices</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Répartition</span>
                        <span class="detail-value">2×6pts + 1×8pts</span>
                    </div>
                </div>
                
                <div class="weight-indicator">
                    <span class="weight-fraction">3/4</span>
                    <small>de la note finale</small>
                </div>
                
                <p style="margin-top: 1rem; opacity: 0.8; font-size: 0.9rem;">
                    Épreuve théorique couvrant les concepts du cours, algorithmes et résolution de problèmes informatiques.
                </p>
            </div>
            
            <div class="exam-card">
                <div class="exam-header">
                    <div class="exam-icon">💻</div>
                    <h3 class="exam-title">Épreuve Pratique</h3>
                </div>
                
                <div class="exam-details">
                    <div class="detail-item">
                        <span class="detail-label">Durée</span>
                        <span class="detail-value">1h00</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Exercices</span>
                        <span class="detail-value">2 exercices</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Sujets</span>
                        <span class="detail-value">~40 sujets</span>
                    </div>
                </div>
                
                <div class="weight-indicator">
                    <span class="weight-fraction">1/4</span>
                    <small>de la note finale</small>
                </div>
                
                <p style="margin-top: 1rem; opacity: 0.8; font-size: 0.9rem;">
                    Programmation sur machine : rédaction d'algorithme et complétion de code à trous.
                </p>
            </div>
        </div>
    </div>
</div>

<style>
.contributors-section {
    background: linear-gradient(135deg, #ffb347 0%, #ff6b35 100%);
    border-radius: 20px;
    padding: 3rem;
    margin: 3rem 0;
    color: white;
    position: relative;
    overflow: hidden;
}

.contributors-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)"/></svg>');
    opacity: 0.3;
}

.contributors-content {
    position: relative;
    z-index: 2;
}

.section-title {
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 2rem;
    color: white;
}

.contributors-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
}

.contributor-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}

.contributor-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.25);
}

.contributor-avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem;
    font-size: 1.5rem;
}

.contributor-name {
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: white;
}

.contributor-role {
    font-size: 0.9rem;
    opacity: 0.9;
    color: rgba(255, 255, 255, 0.8);
}

.colleagues-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.colleagues-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.2rem;
}

.colleague-card {
    background: linear-gradient(135deg, rgba(255, 127, 42, 0.1), rgba(248, 246, 240, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 127, 42, 0.2);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 200px;
}

.colleague-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(135deg, #ffb347, #ff6b35);
}

.colleague-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(255, 127, 42, 0.2);
}

.colleague-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.colleague-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
    background: linear-gradient(135deg, #ffb347, #ff6b35);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 1rem;
    color: white;
    font-size: 1.2rem;
}

.colleague-name {
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0;
    color: var(--md-default-fg-color);
}

.colleague-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem 1.5rem;
    background: white;
    color: #ff6b35;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.3s ease;
    margin-top: auto;
    border: 2px solid #ff6b35;
    position: relative;
    box-shadow: none;
    width: 100%;
    text-align: center;
}

.colleague-link:hover {
    background:rgba(255, 188, 53, 0.26);
    color: white;
    text-decoration: none;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.colleague-link::after {
    content: '→';
    margin-left: 0.5rem;
    transition: all 0.3s ease;
}

.colleague-link:hover::after {
    transform: translateX(3px);
}
</style>

<div class="contributors-section">
    <div class="contributors-content">
        <h2 class="section-title">👥 Ont contribué à ce site</h2>
        
        <div class="contributors-grid">
            <div class="contributor-card">
                <div class="contributor-avatar">🦊</div>
                <div class="contributor-name">BRAUN Clément</div>
                <div class="contributor-role">Enseignant d'informatique</div>
            </div>
            
            <div class="contributor-card">
                <div class="contributor-avatar">💻</div>
                <div class="contributor-name">DELPLACE Nicolas</div>
                <div class="contributor-role">Enseignant d'informatique</div>
            </div>
            
            <div class="contributor-card">
                <div class="contributor-avatar">🎓</div>
                <div class="contributor-name">RAMSTEIN Stéphane</div>
                <div class="contributor-role">Enseignant d'informatique<br>Lycée Raymond Queneau</div>
            </div>
            
            <div class="contributor-card">
                <div class="contributor-avatar">🏫</div>
                <div class="contributor-name">PAPEGAY Benoit</div>
                <div class="contributor-role">Enseignant à l'Université de Lille</div>
            </div>
            
            <div class="contributor-card">
                <div class="contributor-avatar">🎯</div>
                <div class="contributor-name">MARCHAND Mathieu</div>
                <div class="contributor-role">Enseignant d'informatique<br>Lycée Benjamin Franklin</div>
            </div>
        </div>
    </div>
</div>

<div class="colleagues-section">
    <h2 class="section-title" style="color: var(--md-default-fg-color); margin-bottom: 2rem;">🌐 Sites de collègues de NSI</h2>
    
    <div class="colleagues-grid">
        <div class="colleague-card">
            <div class="colleague-header">
                <div class="colleague-icon">📚</div>
                <h3 class="colleague-name">RELMY Lucas</h3>
            </div>
            <p style="color: var(--md-default-fg-color--light); margin-bottom: 1rem;">Ressources complètes et exercices pratiques pour NSI</p>
            <a href="http://lucasrelmynsi.gitlab.io/site_cours/" class="colleague-link" target="_blank">Visiter le site</a>
        </div>
        
        <div class="colleague-card">
            <div class="colleague-header">
                <div class="colleague-icon">🔬</div>
                <h3 class="colleague-name">DEMERVILLE Erwan</h3>
            </div>
            <p style="color: var(--md-default-fg-color--light); margin-bottom: 1rem;">Cours détaillés et projets innovants en NSI</p>
            <a href="https://nsi.erwandemerville.fr" class="colleague-link" target="_blank">Visiter le site</a>
        </div>
        
        <div class="colleague-card">
            <div class="colleague-header">
                <div class="colleague-icon">⚡</div>
                <h3 class="colleague-name">RAMSTEIN Stéphane</h3>
            </div>
            <p style="color: var(--md-default-fg-color--light); margin-bottom: 1rem;">Approche pédagogique moderne et interactive</p>
            <a href="https://stephane_ramstein.gitlab.io/nsi/" class="colleague-link" target="_blank">Visiter le site</a>
        </div>
        
        <div class="colleague-card">
            <div class="colleague-header">
                <div class="colleague-icon">🚀</div>
                <h3 class="colleague-name">MARCHAND Mathieu</h3>
            </div>
            <p style="color: var(--md-default-fg-color--light); margin-bottom: 1rem;">Contenus avancés et méthodologie rigoureuse</p>
            <a href="https://mmarchand-nsi.github.io" class="colleague-link" target="_blank">Visiter le site</a>
        </div>
    </div>
</div>
