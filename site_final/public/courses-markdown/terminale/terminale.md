# Terminale NSI

---

<style>
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

/* Style spécial pour la section Structures de données */
.structures-card {
    grid-column: 1 / -1; /* Prend toute la largeur */
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
    margin-bottom: 2rem;
}

.structures-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 15px rgba(255, 198, 55, 0.8);
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
    gap: 0.5rem;
}

.structures-section h4 {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.1rem;
    font-weight: 600;
    text-align: center;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--md-primary-fg-color);
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

