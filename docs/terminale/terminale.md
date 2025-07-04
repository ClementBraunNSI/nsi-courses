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

/* Design moderne et épuré */
.chapter-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 1.5rem;
    padding: 2rem 0;
}

/* Styles pour les boutons des sections */
.data-section {
    margin-bottom: 1.5rem;
}

.data-section h3 {
    margin: 0 0 1rem 0;
    font-size: 1.3rem;
    font-weight: 700;
    color: #2d3748;
}

.data-section .btn {
    background: #f7fafc;
    color: #4a5568;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    display: inline-block;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

.data-section .btn:hover {
    background: #805ad5;
    color: white;
    border-color: #805ad5;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(128, 90, 213, 0.25);
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
    background: linear-gradient(90deg, #805ad5 0%, #6b46c1 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.chapter-card:hover::before {
    transform: scaleX(1);
}

.chapter-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(128, 90, 213, 0.15);
    border-color: #805ad5;
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
    background: #805ad5;
    color: white;
    border-color: #805ad5;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(128, 90, 213, 0.25);
}

.chapter-links hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 0.75rem 0;
    opacity: 0.6;
}

/* Style spécial pour la section Structures de données */
.structures-card {
    grid-column: 1 / -1; /* Prend toute la largeur */
    background: #ffffff;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #f0f0f0;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.structures-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #805ad5 0%, #6b46c1 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.structures-card:hover::before {
    transform: scaleX(1);
}

.structures-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(128, 90, 213, 0.15);
    border-color: #805ad5;
}

.structures-content {
    display: grid;
    grid-template-columns: 1fr 1px 1fr 1px 1fr;
    gap: 2rem;
    margin-top: 1rem;
}

.structures-section {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.structures-section h4 {
    margin: 0 0 1rem 0;
    background: linear-gradient(135deg, #9C27B0, #7B1FA2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 1.1rem;
    font-weight: 600;
    text-align: center;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(156, 39, 176, 0.3);
}

.structures-section .btn {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    color: #9C27B0;
    border: 2px solid rgba(156, 39, 176, 0.2);
    border-radius: 12px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.structures-section .btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(156, 39, 176, 0.1), transparent);
    transition: left 0.5s ease;
}

.structures-section .btn:hover {
    background: linear-gradient(135deg, #9C27B0, #7B1FA2);
    color: white;
    border-color: #9C27B0;
    transform: translateX(5px);
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.3);
}

.structures-section .btn:hover::before {
    left: 100%;
}

.vertical-separator {
    background: linear-gradient(to bottom, transparent, var(--md-primary-fg-color), transparent);
    width: 1px;
    margin: 1rem 0;
}

@media (max-width: 768px) {
    .structures-content {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .vertical-separator {
        display: none;
    }
    
    .structures-section {
        border-bottom: 1px solid var(--md-primary-fg-color);
        padding-bottom: 1rem;
    }
    
    .structures-section:last-child {
        border-bottom: none;
        padding-bottom: 0;
    }
}
</style>

<!-- Bandeau de niveau -->
<div class="level-header">
  <div class="level-header-content">
    <img src="../../images/fox_terminale.png" alt="Terminale" class="level-logo" />
    <div>
      <h1>Terminale NSI</h1>
      <p>Numérique et Sciences Informatiques</p>
      <p class="level-description">
        Maîtrise des concepts avancés et préparation au supérieur
      </p>
    </div>
  </div>
</div>

<section class="chapter-cards">
    <!-- I. Rappels de Première -->
    <div class="chapter-card">
        <h3>I. 🔄 Rappels de Première</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Révision des concepts fondamentaux : variables, structures de contrôle, fonctions et listes</p>
        <div class="chapter-links">
            <a href="../I-Rappels/Cours/variables_et_types/" class="btn">Variables et types</a>
            <a href="../I-Rappels/Cours/structures_conditionnelles_boucles/" class="btn">Conditions et boucles</a>
            <a href="../I-Rappels/Cours/fonctions/" class="btn">Fonctions</a>
            <a href="../I-Rappels/Cours/listes_tableaux/" class="btn">Listes et tableaux</a>
            <a href="../I-Rappels/Exercices/fiche_exercices_rappels/" class="btn">Exercices de révision</a>
        </div>
    </div>

    <!-- II. Structures de données -->
    <div class="structures-card">
        <h3>II. 🏗️ Structures de données</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Structures de données, interface et implémentation - Programmation objet</p>
        <div class="structures-content">
            <!-- Section Piles/Files -->
            <div class="structures-section">
                <h4>📚 Listes, Piles, Files</h4>
                <a href="../II-Structures_de_donnees/Cours/listes_piles_files/" class="btn">Cours : Structures linéaires</a>
                <a href="../II-Structures_de_donnees/Exercices/fiche_exercices_listes_piles_files/" class="btn">Exercices : Listes, piles et files</a>
            </div>
            
            <div class="vertical-separator"></div>
            
            <!-- Section Arbres -->
            <div class="structures-section">
                <h4>🌳 Arbres</h4>
                <a href="../II-Structures_de_donnees/Cours/arbres/" class="btn">Cours : Arbres binaires</a>
                <a href="../II-Structures_de_donnees/Exercices/fiche_exercices_arbres/" class="btn">Exercices : Arbres</a>
            </div>
            
            <div class="vertical-separator"></div>
            
            <!-- Section Graphes -->
            <div class="structures-section">
                <h4>🕸️ Graphes</h4>
                <a href="../II-Structures_de_donnees/Cours/graphes/" class="btn">Cours : Graphes</a>
                <a href="../II-Structures_de_donnees/Exercices/fiche_exercices_graphes/" class="btn">Exercices : Graphes</a>
            </div>
        </div>
    </div>

    <!-- III. Bases de données -->
    <div class="chapter-card">
        <h3>III. 🗄️ Bases de données</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Modèle relationnel - Système de gestion de bases de données - Langage SQL</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/Cours/modele_relationnel/" class="btn">Modèle relationnel</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/Cours/sgbd/" class="btn">Systèmes de gestion</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/Cours/langage_sql/" class="btn">Langage SQL</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/Exercices/fiche_exercices_sql/" class="btn">Exercices SQL</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/TP/tp_gestion_bibliotheque/" class="btn">TP : Gestion bibliothèque</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/III-Bases_de_donnees/TP/tp_conception_bdd/" class="btn">TP : Conception BDD</a>
        </div>
    </div>

    <!-- IV. Architectures matérielles, systèmes d'exploitation et réseaux -->
    <div class="chapter-card">
        <h3>IV. 🖥️ Architectures matérielles et réseaux</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Composants intégrés - Gestion des processus - Protocoles de routage - Sécurisation</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/Cours/systemes_sur_puce/" class="btn">Systèmes sur puce</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/Cours/gestion_processus/" class="btn">Gestion des processus</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/Cours/protocoles_routage/" class="btn">Protocoles de routage</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/Cours/securisation/" class="btn">Sécurisation des communications</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/Exercices/fiche_exercices_reseaux/" class="btn">Exercices réseaux</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/IV-Architectures_et_reseaux/TP/tp_simulation_reseau/" class="btn">TP : Simulation réseau</a>
        </div>
    </div>

    <!-- V. Langages et programmation -->
    <div class="chapter-card">
        <h3>V. 💻 Langages et programmation</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Calculabilité, décidabilité - Récursivité - Modularité - Paradigmes de programmation</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/calculabilite_decidabilite/" class="btn">Calculabilité et décidabilité</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/recursivite/" class="btn">Récursivité</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/modularite/" class="btn">Modularité</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/paradigmes/" class="btn">Paradigmes de programmation</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/poo_avancee/" class="btn">POO avancée</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Cours/mise_au_point/" class="btn">Mise au point des programmes</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/Exercices/fiche_recursivite/" class="btn">Exercices récursivité</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/V-Langages_et_programmation/TP/tp_poo_avance/" class="btn">TP : POO avancé</a>
        </div>
    </div>

    <!-- VI. Algorithmique -->
    <div class="chapter-card">
        <h3>VI. 🧮 Algorithmique</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Algorithmes sur les arbres et graphes - Diviser pour régner - Programmation dynamique - Recherche textuelle</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Cours/algorithmes_arbres/" class="btn">Algorithmes sur les arbres</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Cours/algorithmes_graphes/" class="btn">Algorithmes sur les graphes</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Cours/diviser_pour_regner/" class="btn">Diviser pour régner</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Cours/programmation_dynamique/" class="btn">Programmation dynamique</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Cours/recherche_textuelle/" class="btn">Recherche textuelle</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Exercices/fiche_complexite/" class="btn">Exercices complexité</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/Exercices/fiche_algorithmes_avances/" class="btn">Exercices algorithmes avancés</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VI-Algorithmique/TP/tp_algorithmes_avances/" class="btn">TP : Algorithmes avancés</a>
        </div>
    </div>

    <!-- VII. Projets -->
    <div class="chapter-card">
        <h3>VII. 🚀 Projets</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Projets dirigés par les élèves (minimum 25% du temps de formation)</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/methodologie_projet/" class="btn">Méthodologie de projet</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/reseau_social_avance/" class="btn">Réseau social avancé</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/moteur_recherche/" class="btn">Moteur de recherche</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/jeu_strategie/" class="btn">Jeu de stratégie</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/analyse_donnees/" class="btn">Analyse de données</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/cryptographie/" class="btn">Projet cryptographie</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VII-Projets/intelligence_artificielle/" class="btn">Projet IA</a>
        </div>
    </div>

    <!-- VIII. Préparation au bac -->
    <div class="chapter-card">
        <h3>VIII. 📝 Préparation au bac</h3>
        <p style="margin-bottom: 1rem; color: var(--md-default-fg-color--light); font-style: italic;">Épreuve écrite (3h30) et épreuve pratique (1h) - Sujets types et méthodologie</p>
        <div class="chapter-links">
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/epreuve_ecrite/" class="btn">Épreuve écrite</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/epreuve_pratique/" class="btn">Épreuve pratique</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/sujets_types/" class="btn">Sujets types</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/methodologie/" class="btn">Méthodologie</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/revisions/" class="btn">Fiches de révisions</a>
            <a href="https://clementbraunnsi.github.io/nsi-courses/terminale/VIII-Preparation_bac/annales/" class="btn">Annales corrigées</a>
        </div>
    </div>
</section>

