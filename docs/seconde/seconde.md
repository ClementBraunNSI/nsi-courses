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

/* Design moderne et épuré */
.chapter-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 1.5rem;
    padding: 2rem 0;
}

.chapter-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #f0f0f0;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
}

.chapter-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #48bb78 0%, #38a169 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.chapter-card:hover::before {
    transform: scaleX(1);
}

.chapter-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(72, 187, 120, 0.15);
    border-color: #48bb78;
}

.chapter-card h3 {
    margin: 0 0 1rem 0;
    font-size: 1.5rem;
    font-weight: 800;
    color: #2d3748;
    letter-spacing: -0.025em;
}

.chapter-card p {
    color: #718096;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    font-size: 0.95rem;
}

.chapter-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
}

.chapter-links .btn {
    background: #f7fafc;
    color: #4a5568;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    position: relative;
    text-align: left;
}

.chapter-links .btn:hover {
    background: #48bb78;
    color: white;
    border-color: #48bb78;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(72, 187, 120, 0.25);
}

.chapter-links hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 0.75rem 0;
    opacity: 0.6;
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

