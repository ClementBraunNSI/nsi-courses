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

/* Styles existants */
.chapter-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

.chapter-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.chapter-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 15px rgba(255, 198, 55, 0.8);
}

.chapter-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
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

