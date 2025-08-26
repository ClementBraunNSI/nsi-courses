# Clément Braun - NSI

---

<!-- Script d'animation de loading -->
<script src="../javascripts/loading-animation.js"></script>

<!-- Script de protection par mot de passe -->
<script src="../javascripts/password-protection.js"></script>

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
        <img src="images/fox_seconde.png" alt="SNT Seconde">
        <h2>SNT - Seconde</h2>
        <p>Sciences Numériques et Technologie : découverte des enjeux du numérique dans notre société</p>
        <a href="seconde/seconde" class="btn">Accéder aux ressources</a>
    </div>
    <div class="level-card">
        <img src="images/fox_premiere.png" alt="NSI Première">
        <h2>NSI - Première</h2>
        <p>Numérique et Sciences Informatiques : initiation à la programmation et aux concepts fondamentaux</p>
        <a href="premiere/premiere" class="btn">Accéder aux ressources</a>
    </div>
    <div class="level-card">
        <img src="images/fox_terminale.png" alt="NSI Terminale">
        <h2>NSI - Terminale</h2>
        <p>Approfondissement en informatique : structures de données, bases de données et projets avancés</p>
        <a href="terminale/terminale" class="btn">Accéder aux ressources</a>
    </div>
    <div class="level-card">
        <img src="images/chasserenarts.png" alt="Chasse aux Ren'Arts">
        <h2>Chasse aux Ren'arts</h2>
        <p>Défi ludique et pédagogique pour mettre en pratique les compétences NSI de manière créative</p>
        <a href="chasse_aux_renards" class="btn">Participer au défi</a>
    </div>
</div>
---

<style>
.teaching-overview {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 50%, #ff6b35 100%);
    border-radius: 15px;
    padding: 3rem;
    margin: 2rem 0;
    position: relative;
    overflow: hidden;
}

.pathway-title {
    text-align: center;
    color: white;
    margin-bottom: 3rem;
}

.pathway-title h3 {
    margin: 0;
    font-size: 2rem;
    font-weight: bold;
}

.pathway-title p {
    margin: 0.5rem 0 0 0;
    font-size: 1.1rem;
    opacity: 0.9;
}

.horizontal-pathway {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    max-width: 1000px;
    margin: 0 auto;
}

.pathway-circle {
    position: relative;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.95);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 3px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    flex-shrink: 0;
}

.pathway-circle:hover {
    transform: scale(1.2);
    background: rgba(255, 255, 255, 1);
    box-shadow: 0 15px 50px rgba(255, 107, 53, 0.3);
    border-color: rgba(255, 127, 42, 0.6);
    z-index: 20;
}

.pathway-circle img {
    width: 50px;
    height: 50px;
    object-fit: contain;
    margin-bottom: 0.5rem;
}

.pathway-circle .level-name {
    font-size: 0.9rem;
    font-weight: bold;
    color: #333;
    text-align: center;
    line-height: 1.2;
}

.pathway-circle .level-short {
    font-size: 0.7rem;
    color: #666;
    margin-top: 0.2rem;
}

.superieur-circle {
    opacity: 0.8;
    border-style: dashed;
}

/* Flèches de connexion */
.pathway-arrow {
    position: relative;
    flex: 1;
    height: 2px;
    background: rgba(255, 255, 255, 0.4);
    margin: 0 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 80px;
}

.pathway-arrow::after {
    content: '';
    position: absolute;
    right: -5px;
    top: 50%;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-left: 8px solid rgba(255, 255, 255, 0.4);
    border-top: 5px solid transparent;
    border-bottom: 5px solid transparent;
}

.pathway-arrow.dashed {
    background: repeating-linear-gradient(
        to right,
        rgba(255, 255, 255, 0.4) 0px,
        rgba(255, 255, 255, 0.4) 8px,
        transparent 8px,
        transparent 16px
    );
}

.pathway-arrow.dashed::after {
    border-left-color: rgba(255, 255, 255, 0.4);
}

@media (max-width: 1024px) {
    .horizontal-pathway {
        flex-direction: column;
        align-items: center;
        gap: 2rem;
    }
    
    .pathway-arrow {
        width: 2px;
        height: 30px;
        transform: rotate(90deg);
        margin: 0;
    }
    
    .pathway-arrow::after {
        right: 50%;
        top: -5px;
        transform: translateX(50%) rotate(-90deg);
    }
    
    .pathway-circle {
        width: 120px;
        height: 120px;
    }
}

.terminale-circle {
    bottom: 50px;
    left: 50%;
    transform: translateX(-50%);
}

.superieur-circle {
    top: 50%;
    left: 50px;
    transform: translateY(-50%);
    opacity: 0.8;
    border-style: dashed;
}

/* Lignes de connexion */
.pathway-line {
    position: absolute;
    background: rgba(255, 255, 255, 0.3);
    z-index: 1;
}

.line-1 {
    top: 120px;
    left: 50%;
    width: 2px;
    height: 100px;
    transform: translateX(-50%) rotate(45deg);
    transform-origin: top;
}

.line-2 {
    top: 50%;
    right: 120px;
    width: 100px;
    height: 2px;
    transform: translateY(-50%);
}

.line-3 {
    bottom: 120px;
    left: 50%;
    width: 2px;
    height: 100px;
    transform: translateX(-50%) rotate(-45deg);
    transform-origin: bottom;
}

.line-4 {
    top: 50%;
    left: 120px;
    width: 100px;
    height: 2px;
    transform: translateY(-50%);
    border-style: dashed;
    opacity: 0.6;
}

/* Tooltip détaillé */
.pathway-tooltip {
    position: absolute;
    background: rgba(255, 255, 255, 0.98);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    max-width: 320px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px);
    transition: all 0.3s ease;
    z-index: 30;
    border: 1px solid rgba(255, 127, 42, 0.2);
}

.pathway-circle:hover .pathway-tooltip {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.tooltip-title {
    color: #ff6b35;
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.tooltip-subtitle {
    color: #333;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.tooltip-content {
    color: #666;
    font-size: 0.85rem;
    line-height: 1.5;
}

.tooltip-list {
    list-style: none;
    padding: 0;
    margin: 0.5rem 0;
}

.tooltip-list li {
    padding: 0.2rem 0;
    position: relative;
    padding-left: 1rem;
}

.tooltip-list li::before {
    content: '•';
    color: #ff6b35;
    position: absolute;
    left: 0;
}

/* Positionnement des tooltips */
.snt-circle .pathway-tooltip {
    top: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(20px);
    margin-top: 1rem;
}

.snt-circle:hover .pathway-tooltip {
    transform: translateX(-50%) translateY(0);
}

.premiere-circle .pathway-tooltip {
    top: 50%;
    right: 100%;
    transform: translateY(-50%) translateX(-20px);
    margin-right: 1rem;
}

.premiere-circle:hover .pathway-tooltip {
    transform: translateY(-50%) translateX(0);
}

.terminale-circle .pathway-tooltip {
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    margin-bottom: 1rem;
}

.terminale-circle:hover .pathway-tooltip {
    transform: translateX(-50%) translateY(0);
}

.superieur-circle .pathway-tooltip {
    top: 50%;
    left: 100%;
    transform: translateY(-50%) translateX(20px);
    margin-left: 1rem;
}

.superieur-circle:hover .pathway-tooltip {
    transform: translateY(-50%) translateX(0);
}

@media (max-width: 768px) {
    .circular-pathway {
        height: 500px;
        max-width: 500px;
    }
    
    .pathway-circle {
        width: 120px;
        height: 120px;
    }
    
    .pathway-tooltip {
        max-width: 280px;
        padding: 1rem;
    }
}
</style>

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
    background: linear-gradient(135deg, rgba(255, 127, 42, 0.1), rgba(255, 107, 53, 0.05));
    border: 1px solid rgba(255, 127, 42, 0.2);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
    position: relative;
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
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: var(--md-default-fg-color);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.contributors-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 0;
}

.contributor-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 127, 42, 0.2);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    min-width: 140px;
    max-width: 160px;
    box-shadow: 0 2px 8px rgba(255, 127, 42, 0.1);
}

.contributor-card:hover {
    transform: translateY(-3px);
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 4px 15px rgba(255, 127, 42, 0.2);
    border-color: rgba(255, 127, 42, 0.4);
}

@media (max-width: 768px) {
    .contributors-grid {
        gap: 0.8rem;
    }
    
    .contributor-card {
        min-width: 120px;
        max-width: 140px;
        padding: 0.8rem;
    }
    
    .contributor-avatar {
        width: 35px;
        height: 35px;
        font-size: 1rem;
    }
    
    .contributor-name {
        font-size: 0.8rem;
    }
    
    .contributor-role {
        font-size: 0.7rem;
    }
}

.contributor-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(255, 127, 42, 0.2), rgba(255, 107, 53, 0.1));
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 0.8rem;
    font-size: 1.2rem;
    border: 2px solid rgba(255, 127, 42, 0.3);
}

.contributor-name {
    font-weight: 600;
    margin-bottom: 0.3rem;
    color: var(--md-default-fg-color);
    font-size: 0.9rem;
    line-height: 1.2;
}

.contributor-role {
    font-size: 0.75rem;
    opacity: 0.8;
    color: var(--md-default-fg-color--light);
    line-height: 1.3;
}

.colleagues-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(0, 0, 0, 0.05);
    position: relative;
}

.colleagues-carousel {
    position: relative;
    overflow: hidden;
    border-radius: 15px;
}

.colleagues-grid {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    gap: 1.5rem;
}

.carousel-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 127, 42, 0.95);
    border: 2px solid white;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 100;
    color: white;
    font-size: 1.4rem;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), 0 2px 8px rgba(255, 127, 42, 0.4);
    backdrop-filter: blur(10px);
}

.carousel-nav:hover {
    background: rgba(255, 127, 42, 1);
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(255, 127, 42, 0.4);
}

.carousel-nav.prev {
    left: 10px;
}

.carousel-nav.next {
    right: 10px;
}

.carousel-nav:disabled {
    opacity: 0.3;
    cursor: not-allowed;
    transform: translateY(-50%) scale(0.9);
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
    background: rgba(255, 127, 42, 0.3);
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
}

.carousel-indicator.active {
    background: rgba(255, 127, 42, 1);
    transform: scale(1.2);
}

@media (max-width: 768px) {
    .colleagues-grid {
        gap: 1rem;
    }
    
    .carousel-nav {
        width: 40px;
        height: 40px;
        font-size: 1rem;
    }
    
    .carousel-nav.prev {
        left: 5px;
    }
    
    .carousel-nav.next {
        right: 5px;
    }
}

.colleague-card {
    background: linear-gradient(135deg, rgba(255, 127, 42, 0.1), rgba(248, 246, 240, 0.1));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 127, 42, 0.2);
    transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 200px;
    min-width: 280px;
    flex-shrink: 0;
    opacity: 1;
    transform: translateY(0);
}

.colleague-card:nth-child(1) { animation-delay: 0.1s; }
.colleague-card:nth-child(2) { animation-delay: 0.2s; }
.colleague-card:nth-child(3) { animation-delay: 0.3s; }
.colleague-card:nth-child(4) { animation-delay: 0.4s; }

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
    
    <div class="colleagues-carousel">
        <button class="carousel-nav prev" onclick="moveCarousel(-2)">‹</button>
        <button class="carousel-nav next" onclick="moveCarousel(2)">›</button>
        
        <div class="colleagues-grid" id="colleaguesGrid">
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
            <div class="colleague-card">
                <div class="colleague-header">
                    <div class="colleague-icon">🚀</div>
                    <h3 class="colleague-name">LEAL Nicolas</h3>
                </div>
                <p style="color: var(--md-default-fg-color--light); margin-bottom: 1rem;">Contenus avancés et méthodologie rigoureuse</p>
                <a href="http://www.prof-leal.fr" class="colleague-link" target="_blank">Visiter le site</a>
            </div>
        </div>
    </div>
    
    <div class="carousel-indicators" id="carouselIndicators">
        <button class="carousel-indicator active" onclick="goToSlide(0)"></button>
        <button class="carousel-indicator" onclick="goToSlide(1)"></button>
        <button class="carousel-indicator" onclick="goToSlide(2)"></button>
        <button class="carousel-indicator" onclick="goToSlide(3)"></button>
        <button class="carousel-indicator" onclick="goToSlide(4)"></button>
    </div>
</div>

<script>
let currentSlide = 0;
const totalSlides = 5;
const slideWidth = 300; // largeur d'une carte + gap

function updateCarousel() {
    const grid = document.getElementById('colleaguesGrid');
    const indicators = document.querySelectorAll('.carousel-indicator');
    const prevBtn = document.querySelector('.carousel-nav.prev');
    const nextBtn = document.querySelector('.carousel-nav.next');
    
    // Mise à jour de la position
    grid.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
    
    // Mise à jour des indicateurs
    indicators.forEach((indicator, index) => {
        indicator.classList.toggle('active', index === currentSlide);
    });
    
    // Mise à jour des boutons
    prevBtn.disabled = currentSlide === 0;
    nextBtn.disabled = currentSlide === totalSlides - 1;
}

function moveCarousel(direction) {
    const newSlide = currentSlide + direction;
    if (newSlide >= 0 && newSlide < totalSlides) {
        currentSlide = newSlide;
        updateCarousel();
    }
}

function goToSlide(slideIndex) {
    if (slideIndex >= 0 && slideIndex < totalSlides) {
        currentSlide = slideIndex;
        updateCarousel();
    }
}

// Auto-play optionnel
setInterval(() => {
    if (currentSlide < totalSlides - 1) {
        moveCarousel(1);
    } else {
        currentSlide = 0;
        updateCarousel();
    }
}, 5000);

// Initialisation
document.addEventListener('DOMContentLoaded', updateCarousel);
</script>

<style>
/* Masquer le footer par défaut de MkDocs */
.md-footer-meta__inner {
    display: none !important;
}
</style>
