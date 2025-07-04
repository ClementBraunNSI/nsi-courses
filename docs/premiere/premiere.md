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
  border-left: 5px solid #2196F3;
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
  color: #2196F3;
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
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.chapter-card:hover::before {
    transform: scaleX(1);
}

.chapter-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(102, 126, 234, 0.15);
    border-color: #667eea;
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
    background: #667eea;
    color: white;
    border-color: #667eea;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.25);
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
    <img src="../../images/fox_premiere.png" alt="Première" class="level-logo" />
    <div>
      <h1>Première NSI</h1>
      <p>Numérique et Sciences Informatiques</p>
      <p class="level-description">
        Approfondissement des concepts informatiques et algorithmiques
      </p>
    </div>
  </div>
</div>

<section class="chapter-cards">
    <!-- Section Aides et New Year Advent -->
    <div class="chapter-card">
        <h3>🎄 New Year Advent 2025-2026</h3>
        <div class="chapter-links">
            <a href="../New_Year_Advent/new_year_advent/" class="btn">Explication et calendrier</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📚 Aides et Corrections</h3>
        <div class="chapter-links">
            <a href="../Aides/Corrections/trimestre_1/correction_interro_2/" class="btn">Correction Interro 2</a>
            <a href="../Aides/Corrections/trimestre_1/correction_ds_1/" class="btn">Correction DS 1</a>
            <a href="../Aides/Algorithmes_a_savoir/algo_a_savoir/" class="btn">Algorithmes à savoir</a>
            <a href="../Aides/Cheat_Sheets/cheat_sheet/" class="btn">Cheat Sheet</a>
            <a href="../Aides/Revisions/exos_boucles/" class="btn">Exercices révisions</a>
        </div>
    </div>
    <!-- Début carte chapitre I -->
    <div class="chapter-card">
        <h3>🛠️ I - Constructions élémentaires</h3>
        <div class="chapter-links">
            <a href="../I-Constructions_elementaires/Cours/Cours_1/" class="btn">Cours 1 - Bases</a>
            <a href="../I-Constructions_elementaires/Cours/Cours_2/" class="btn">Cours 2</a>
            <a href="../I-Constructions_elementaires/Cours/Cours_3/" class="btn">Cours 3</a>
            <a href="../I-Constructions_elementaires/Cours/Cours_4/" class="btn">Cours 4</a>
            <hr>
            <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_boucles/" class="btn">Exercices boucles</a>
            <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_fonctions/" class="btn">Exercices fonctions</a>
            <a href="../I-Constructions_elementaires/Fiches_d_exercices/Exercices_specification/" class="btn">Exercices spécification</a>
            <a href="../I-Constructions_elementaires/Fiches_d_exercices/Fiche_exercice/" class="btn">Fiche exercice</a>
        </div>
    </div>
    <!-- Fin carte chapitre I -->

    <!-- Début carte chapitre II -->
    <div class="chapter-card">
        <h3>🔢 II - Représentation des données</h3>
        <div class="chapter-links">
            <a href="../II-Representation_des_donnees/Cours/c_1_booleen_et_operations/" class="btn">Cours booléens</a>
            <a href="../II-Representation_des_donnees/Cours/c_2_entier_binaire_hexa/" class="btn">Cours binaire/hexa</a>
            <a href="../II-Representation_des_donnees/Cours/c_2_entier_relatif/" class="btn">Cours entiers relatifs</a>
            <a href="../II-Representation_des_donnees/Cours/c_2_nombres_reels/" class="btn">Cours nombres réels</a>
            <a href="../II-Representation_des_donnees/Cours/c_3_caracteres/" class="btn">Cours caractères</a>
            <hr>
            <a href="../II-Representation_des_donnees/Fiches_d_exercices/Fiche_exercice_Nombres_binaires/" class="btn">Exercices binaires</a>
            <a href="../II-Representation_des_donnees/Fiches_d_exercices/Fiche_exercice_bool/" class="btn">Exercices booléens</a>
            <a href="../II-Representation_des_donnees/Fiches_d_exercices/Fiche_exercices_Caracteres/" class="btn">Exercices caractères</a>
        </div>
    </div>
    <!-- Ajouter les autres chapitres suivant le même modèle -->

    <div class="chapter-card">
        <h3>🧱 III - Structures de données linéaires</h3>
        <div class="chapter-links">
            <a href="../III-Structures_de_donnees_lineaires/Cours/Cours/" class="btn">Cours listes/tuples</a>
            <hr>
            <a href="../III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercices_tuples_listes/" class="btn">Exercices tuples/listes</a>
            <a href="../III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercices_tuples_listes_v2/" class="btn">Exercices tuples/listes v2</a>
            <a href="../III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercice_supplementaire/" class="btn">Exercices supplémentaires</a>
            <a href="../III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercices_papier/" class="btn">Exercices papier</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>💻 IV - Architecture machine</h3>
        <div class="chapter-links">
            <a href="../IV-Architecture_d_une_machine/Cours/Cours_1/" class="btn">Fonctionnement processeur</a>
            <a href="../IV-Architecture_d_une_machine/Cours/Cours_2/" class="btn">Portes logiques</a>
            <a href="../IV-Architecture_d_une_machine/Exercices/Fiche_Exo/" class="btn">TP architecture</a>
            <a href="../IV-Architecture_d_une_machine/Cours/Cours_4/" class="btn">Ludopédagogie : Minecraft et Redstone</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📊 V - Traitement de données</h3>
        <div class="chapter-links">
            <a href="../V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_1/" class="btn">Cours dictionnaires</a>
            <a href="../V-Dictionnaires_et_Traitement_de_tables/Exercices/Fiche_exercices_dictionnaires/" class="btn">Exercices dictionnaires</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🌐 VI - Internet et Réseaux</h3>
        <div class="chapter-links">
            <a href="../VI-Internet_et_Reseaux/Cours/" class="btn">Cours principal</a>
            <a href="../VI-Internet_et_Reseaux/bit_alterne/" class="btn">Bit alterné</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🔍 VII - Algorithmes tableaux</h3>
        <div class="chapter-links">
            <a href="../VII-Algorithmes_sur_les_tableaux/Cours/" class="btn">Cours algorithmique</a>
            <a href="../VII-Algorithmes_sur_les_tableaux/Mesures_de_complexite/mesure_tris/sujets_mesure_tris/" class="btn">Mesures de complexité</a>
            <a href="../VII-Algorithmes_sur_les_tableaux/dicho/" class="btn">Recherche dichotomique</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🧠 VIII - Algorithmes Gloutons</h3>
        <div class="chapter-links">
            <a href="../VIII-Algorithmes_Gloutons/Algorithmes%20Gloutons_22_23/" class="btn">Stratégies gloutonnes</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🐧 VIIII - Systèmes d'exploitation</h3>
        <div class="chapter-links">
            <a href="../VIIII-Systemes_d_exploitation_et_commandes_Linux/Cours/Cours_1/" class="btn">Principes de base</a>
            <a href="../VIIII-Systemes_d_exploitation_et_commandes_Linux/TP_Commandes_Linux/TP_commandes_linux/" class="btn">TP Commandes Linux</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🌍 X - Web et HTTP</h3>
        <div class="chapter-links">
            <a href="../X-Web_et_HTTP/Cours/" class="btn">Fonctionnement HTTP</a>
            <a href="../X-Web_et_HTTP/TP/Projet/" class="btn">Création de site web</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🤖 XI - K plus proches voisins</h3>
        <div class="chapter-links">
            <a href="../XI-K_plus_proches_voisins/Cours/" class="btn">Algorithme KNN</a>
            <a href="../XI-K_plus_proches_voisins/TP_KNN/" class="btn">TP application</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🚀 XII - Pour aller plus loin</h3>
        <div class="chapter-links">
            <a href="../XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_cours/" class="btn">Programmation Orientée Objet</a>
            <a href="../XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_exercices/" class="btn">Exercices POO</a>
            <a href="../XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_piles_files/" class="btn">Les piles et les files</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🎨 XIII - Projets</h3>
        <div class="chapter-links">
            <a href="../XIII-Projets/" class="btn">Voir tous les projets</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📝 XIIII - TP Notés</h3>
        <div class="chapter-links">
            <a href="../XIIII-TP_notes/Carte_Bleue/verification_carte_bleue/" class="btn">Carte Bleue</a>
            <a href="../XIIII-TP_notes/Code_Barre/code_barre/" class="btn">Code Barre</a>
            <a href="../XIIII-TP_notes/Interro_Algo_a_savoir/sujet1_md/" class="btn">Interro Algo à savoir</a>
        </div>
    </div>
</section>
