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
  border-left: 5px solid #4CAF50;
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
  color: #4CAF50;
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

/* Styles modernes pour les cartes */
.chapter-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

.chapter-card {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85));
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.1),
        0 2px 8px rgba(0, 0, 0, 0.05),
        inset 0 1px 0 rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.3);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.chapter-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #4CAF50, #66BB6A, #4CAF50);
    background-size: 200% 100%;
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { background-position: 200% 0; }
    50% { background-position: -200% 0; }
}

.chapter-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 
        0 20px 60px rgba(76, 175, 80, 0.15),
        0 8px 32px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);
    border-color: rgba(76, 175, 80, 0.3);
}

.chapter-card h3 {
    margin: 0 0 1rem 0;
    font-size: 1.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #4CAF50, #388E3C);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
}

.chapter-card p {
    color: #555;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.chapter-links {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 1rem;
}

.chapter-links .btn {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    color: #4CAF50;
    border: 2px solid rgba(76, 175, 80, 0.2);
    border-radius: 12px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.chapter-links .btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.1), transparent);
    transition: left 0.5s ease;
}

.chapter-links .btn:hover {
    background: linear-gradient(135deg, #4CAF50, #388E3C);
    color: white;
    border-color: #4CAF50;
    transform: translateX(5px);
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.chapter-links .btn:hover::before {
    left: 100%;
}

.chapter-links hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.3), transparent);
    margin: 0.5rem 0;
}
</style>

<!-- Bandeau de niveau -->
<div class="level-header">
  <div class="level-header-content">
    <img src="../../images/fox_seconde.png" alt="Seconde" class="level-logo" />
    <div>
      <h1>Seconde SNT</h1>
      <p>Sciences Numériques et Technologie</p>
      <p class="level-description">
        Découverte des enjeux du numérique et de ses impacts sur la société
      </p>
    </div>
  </div>
</div>

<section class="chapter-cards">
    <div class="chapter-card">
        <h3>🌐 I - Internet</h3>
        <div class="chapter-links">
            <a href="../I_-_Internet/Cours/" class="btn">Cours principal</a>
            <a href="../I_-_Internet/Activite/" class="btn">Activité</a>
            <a href="../I_-_Internet/Binaire_Décimal/" class="btn">Binaire/Décimal</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🌍 II - Web</h3>
        <div class="chapter-links">
            <a href="../II_-_Web/Cours/" class="btn">Cours HTML</a>
            <a href="../II_-_Web/Projet_creation_site/" class="btn">Projet création site</a>
            <a href="../II_-_Web/monstres" class="btn">Ensemble des monstres des élèves</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📱 III - Réseaux sociaux</h3>
        <div class="chapter-links">
            <a href="../III_-_Reseaux_sociaux/Cours/" class="btn">Cours réseaux sociaux</a>
            <hr>
            <a href="../III_-_Reseaux_sociaux/TP_reseau_social/" class="btn">TP : Modéliser un réseau social</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🐍 IIII - Programmation Python</h3>
        <div class="chapter-links">
            <hr>
            <a href="../IIII_-_Programmation_Python/Fiche_exercices_python/" class="btn">Exercices Python</a>
            <a href="../IIII_-_Programmation_Python/Fiche_exercices_boucles/" class="btn">Exercices boucles</a>
            <a href="../IIII_-_Programmation_Python/Fiche_exercices_conditions/" class="btn">Exercices conditions</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📸 V - Photographie Numérique</h3>
        <div class="chapter-links">
            <a href="../V_-_Photographie_Numerique/c_1_Photographie_Noir_et_Blanc/" class="btn">Photo Noir et Blanc</a>
            <a href="../V_-_Photographie_Numerique/c_2_Photographie_Couleur/" class="btn">Photo Couleur</a>
            <a href="../V_-_Photographie_Numerique/c_3_Metadonnees/" class="btn">Métadonnées</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📍 VI - Géolocalisation</h3>
        <div class="chapter-links">
            <a href="../VI_-_Geolocalisation/La%20Géolocalisation_22_23/" class="btn">Cours géolocalisation</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🗃️ VII - Données Structurées</h3>
        <div class="chapter-links">
            <a href="../VII_-_Donnees_Structurees/Activité%20blockly/" class="btn">Activité Blockly</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>💡 VIII - Objets Connectés</h3>
        <div class="chapter-links">
            <a href="../VIII_-_Objets_Connectes/activite/" class="btn">Activité Blockly</a>
            <hr>
            <a href="../VIII_-_Objets_Connectes/tp/" class="btn">TP Micro:bit</a>
        </div>
    </div>
</section>

