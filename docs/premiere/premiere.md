# 🎓 Première NSI

## 📚 Chapitres

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
}

.chapter-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
}
</style>

<section class="chapter-cards">
    <!-- Section Aides et New Year Advent -->
    <div class="chapter-card">
        <h3>🎄 New Year Advent</h3>
        <div class="chapter-links">
            <a href="0-New_Year_Advent/new_year_advent/" class="btn">Explication et calendrier</a>
            <a href="0-New_Year_Advent/Exercices_J1-J9/Jour_1/" class="btn">Jour 1</a>
            <a href="0-New_Year_Advent/Exercices_J1-J9/Jour_2/" class="btn">Jour 2</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📚 Aides et Corrections</h3>
        <div class="chapter-links">
            <a href="/docs/0-Aides/Corrections/trimestre_1/correction_interro_2/" class="btn">Correction Interro 2</a>
            <a href="/docs/0-Aides/Corrections/trimestre_1/correction_ds_1/" class="btn">Correction DS 1</a>
            <a href="/docs/0-Aides/Algorithmes_a_savoir/algo_a_savoir/" class="btn">Algorithmes à savoir</a>
            <a href="/docs/0-Aides/Cheat_Sheets/cheat_sheet/" class="btn">Cheat Sheet</a>
            <a href="/docs/0-Aides/Revisions/exos_boucles/" class="btn">Exercices révisions</a>
        </div>
    </div>
    <!-- Début carte chapitre I -->
    <div class="chapter-card">
        <h3>🛠️ I - Constructions élémentaires</h3>
        <div class="chapter-links">
            <a href="/docs/premiere/I-Constructions_elementaires/Cours/Cours_1/" class="btn">Cours 1 - Bases</a>
            <a href="/docs/premiere/I-Constructions_elementaires/Fiches_d_exercices/Exercices_boucles/" class="btn">Exercices boucles</a>
            <a href="/docs/I-Constructions_elementaires/Fiches_d_exercices/Exercices_fonctions/" class="btn">Exercices fonctions</a>
        </div>
    </div>
    <!-- Fin carte chapitre I -->

    <!-- Début carte chapitre II -->
    <div class="chapter-card">
        <h3>🔢 II - Représentation des données</h3>
        <div class="chapter-links">
            <a href="/docs/II-Representation_des_donnees/Cours/c_1_booleen_et_operations/" class="btn">Cours booléens</a>
            <a href="/docs/II-Representation_des_donnees/Fiches_d_exercices/Fiche_exercice_Nombres_binaires/" class="btn">Exercices binaires</a>
        </div>
    </div>
    <!-- Ajouter les autres chapitres suivant le même modèle -->

    <div class="chapter-card">
        <h3>🧱 III - Structures de données linéaires</h3>
        <div class="chapter-links">
            <a href="/docs/III-Structures_de_donnees_lineaires/Cours/Cours/" class="btn">Cours listes/tuples</a>
            <a href="/docs/III-Structures_de_donnees_lineaires/Fiche_d_exercices/Fiche_exercices_tuples_listes/" class="btn">Exercices pratiques</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>💻 IV - Architecture machine</h3>
        <div class="chapter-links">
            <a href="/docs/IV-Architecture_d_une_machine/Cours/Cours_1/" class="btn">Fonctionnement processeur</a>
            <a href="/docs/IV-Architecture_d_une_machine/Cours/Cours_2/" class="btn">Portes logiques</a>
            <a href="/docs/IV-Architecture_d_une_machine/Exercices/Fiche_Exo/" class="btn">TP architecture</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>📊 V - Traitement de données</h3>
        <div class="chapter-links">
            <a href="/docs/V-Dictionnaires_et_Traitement_de_tables/Cours/Cours_1/" class="btn">Cours dictionnaires</a>
            <a href="/docs/V-Dictionnaires_et_Traitement_de_tables/Exercices/Fiche_exercices_dictionnaires/" class="btn">Exercices dictionnaires</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🌐 VI - Internet et Réseaux</h3>
        <div class="chapter-links">
            <a href="/docs/VI-Internet_et_Reseaux/Cours/" class="btn">Cours principal</a>
            <a href="/docs/VI-Internet_et_Reseaux/bit_alterne/" class="btn">Exercices réseau</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🔍 VII - Algorithmes tableaux</h3>
        <div class="chapter-links">
            <a href="/docs/VII-Algorithmes_sur_les_tableaux/Cours/" class="btn">Cours algorithmique</a>
            <a href="/docs/VII-Algorithmes_sur_les_tableaux/Mesures_de_complexite/mesure_tris/" class="btn">Mesures de complexité</a>
            <a href="/docs/VII-Algorithmes_sur_les_tableaux/dicho/" class="btn">Recherche dichotomique</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🧠 VIII - Algorithmes Gloutons</h3>
        <div class="chapter-links">
            <a href="/docs/VIII-Algorithmes_Gloutons/Algorithmes%20Gloutons_22_23/" class="btn">Stratégies gloutonnes</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🐧 VIIII - Systèmes d'exploitation</h3>
        <div class="chapter-links">
            <a href="/docs/VIIII-Systemes_d_exploitation_et_commandes_Linux/Cours/Cours_1/" class="btn">Principes de base</a>
            <a href="/docs/VIIII-Systemes_d_exploitation_et_commandes_Linux/TP_Commandes_Linux/TP_commandes_linux/" class="btn">TP Commandes Linux</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🌍 X - Web et HTTP</h3>
        <div class="chapter-links">
            <a href="/docs/X-Web_et_HTTP/Cours/Cours/" class="btn">Fonctionnement HTTP</a>
            <a href="/docs/X-Web_et_HTTP/TP/Projet/" class="btn">Création de site web</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🤖 XI - K plus proches voisins</h3>
        <div class="chapter-links">
            <a href="/docs/XI-K_plus_proches_voisins/Cours/" class="btn">Algorithme KNN</a>
            <a href="/docs/XI-K_plus_proches_voisins/TP_KNN/" class="btn">TP application</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🚀 XII - Pour aller plus loin</h3>
        <div class="chapter-links">
            <a href="/docs/XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_cours/" class="btn">Programmation Orientée Objet</a>
            <a href="/docs/XII-Pour_aller_plus_loin/Programmation_Orientee_Objet/fiche_exercices/" class="btn">Exercices POO</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🎨 XIII - Projets</h3>
        <div class="chapter-links">
            <a href="/docs/XIII-Projets/" class="btn">Voir tous les projets</a>
            <a href="/docs/XIII-Projets/Application_bancaire/sujet/" class="btn">Application bancaire</a>
            <a href="/docs/XIII-Projets/Mini_Projets/Devinette/sujet/" class="btn">Mini Projets</a>
        </div>
    </div>

    <div class="chapter-card">
        <h3>🎨 XIII - Projets</h3>
        <div class="chapter-links">
            <a href="/docs/XIIII-TP_notes/Carte_Bleue/verification_carte_bleue/" class="btn">Carte Bleue</a>
            <a href="/docs/XIIII-TP_notes/Code_Barre/code_barre/" class="btn">Code Barre</a>
            <a href="/docs/XIIII-TP_notes/Interro_Algo_a_savoir/sujet1_md/" class="btn">Interro Algo à savoir</a>
        </div>
    </div>
</section>
