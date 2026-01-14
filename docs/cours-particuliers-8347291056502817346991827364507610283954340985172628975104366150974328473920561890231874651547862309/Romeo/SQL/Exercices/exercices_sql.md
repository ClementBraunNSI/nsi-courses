# Exercices Progressifs SQL

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

.exercise-card {
    background: var(--md-default-bg-color);
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 3px solid;
    width: 100%;
    max-width: 100%;
}

.exercise-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.exercise-content-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.exercise-card.intro { border-left-color: #4CAF50; }
.exercise-card.easy { border-left-color: #2196F3; }
.exercise-card.medium { border-left-color: #FF9800; }
.exercise-card.hard { border-left-color: #F44336; }

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro { background: rgba(76, 175, 80, 0.1); color: #4CAF50; }
.difficulty-badge.easy { background: rgba(33, 150, 243, 0.1); color: #2196F3; }
.difficulty-badge.medium { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.hard { background: rgba(244, 67, 54, 0.1); color: #F44336; }

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.1rem;
    font-weight: 600;
}

.exercise-content {
    margin-bottom: 1rem;
    line-height: 1.6;
}

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
}

.section-tab {
    background: #f5f5f5;
    color: #333;
    border: none;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    flex: 1;
    min-width: 150px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ead466ff 0%, #e8a508ff 100%);;
    color: white;
    box-shadow: 0 4px 12px rgba(234, 227, 102, 0.4);
}

.section-content {
    display: none;
    animation: fadeIn 0.3s ease;
}

.section-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

pre { margin: 0; font-family: 'Courier New', monospace; }
code { font-family: 'Courier New', monospace; }

/* Table Styles for SQL Context */
.sql-table-container {
    overflow-x: auto;
    margin: 1rem 0;
    border-radius: 8px;
    border: 1px solid #ddd;
}
table { width: 100%; border-collapse: collapse; background: white; }
th { background: #f8f9fa; padding: 10px; border-bottom: 2px solid #ddd; text-align: left; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background-color: #f1f1f1; }

.download-btn {
    display: inline-block;
    background: #f8f9fa;
    color: #333;
    padding: 0.5rem 1rem;
    border: 1px solid #ddd;
    border-radius: 6px;
    text-decoration: none;
    font-size: 0.9rem;
    margin-top: 1rem;
    transition: all 0.2s;
    font-weight: 500;
}
.download-btn:hover {
    background: #e9ecef;
    border-color: #ced4da;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>

<script>
function showSection(sectionId) {
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    document.getElementById(sectionId).classList.add('active');
    
    const buttons = document.getElementsByTagName('button');
    for (let btn of buttons) {
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(sectionId)) {
            btn.classList.add('active');
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    showSection('level1-section');
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('level1-section')">📚 Niveau 1 (Facile)</button>
    <button class="section-tab" onclick="showSection('level2-section')">🚗 Niveau 2 (Intermédiaire)</button>
    <button class="section-tab" onclick="showSection('level3-section')">🦊 Niveau 3 (Difficile)</button>
</div>

<!-- SECTION 1: NIVEAU 1 -->
<div id="level1-section" class="section-content">
    <div class="exercise-cards">
        
        <!-- Context Card -->
        <div class="exercise-card intro" style="border-left-color: #4CAF50;">
            <div class="exercise-content-wrapper">
                <h4 class="exercise-title">Contexte : La Bibliothèque</h4>
                <div class="exercise-content">
                    <p>Vous gérez une petite base de données d'une bibliothèque contenant une seule table <code>Livres</code>.</p>
                    <div class="sql-table-container">
                        <table>
                            <thead>
                                <tr><th>id</th><th>titre</th><th>auteur</th><th>annee_publication</th><th>genre</th><th>disponible</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>1</td><td>1984</td><td>George Orwell</td><td>1949</td><td>SF</td><td>1</td></tr>
                                <tr><td>2</td><td>Le Petit Prince</td><td>Antoine de Saint-Exupéry</td><td>1943</td><td>Conte</td><td>0</td></tr>
                                <tr><td>3</td><td>Dune</td><td>Frank Herbert</td><td>1965</td><td>SF</td><td>1</td></tr>
                                <tr><td>4</td><td>Les Misérables</td><td>Victor Hugo</td><td>1862</td><td>Roman</td><td>1</td></tr>
                                <tr><td>5</td><td>Fondation</td><td>Isaac Asimov</td><td>1951</td><td>SF</td><td>0</td></tr>
                            </tbody>
                        </table>
                    </div>
                    <p><em>(Note : `disponible` est un booléen : 1 = Oui, 0 = Non)</em></p>
                    <a href="bibliotheque.sql" download class="download-btn">📥 Télécharger la base (bibliotheque.sql)</a>
                </div>
            </div>
        </div>

        <!-- Exo 1 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">1. Tout voir</h4>
                <div class="exercise-content">
                    <p>Écrire la requête pour afficher toutes les colonnes de tous les livres.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">2. Titres uniquement</h4>
                <div class="exercise-content">
                    <p>Afficher uniquement le <code>titre</code> et l'<code>auteur</code> de tous les livres.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">3. Science-Fiction</h4>
                <div class="exercise-content">
                    <p>Afficher les titres des livres du genre 'SF'.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">4. Disponibles</h4>
                <div class="exercise-content">
                    <p>Afficher les titres des livres qui sont actuellement disponibles (<code>disponible = 1</code>).</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">5. Après 1950</h4>
                <div class="exercise-content">
                    <p>Afficher les livres publiés strictement après l'année 1950.</p>
                </div>
            </div>
        </div>

        <!-- Exo 6 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">6. Auteurs précis</h4>
                <div class="exercise-content">
                    <p>Afficher les livres écrits par 'George Orwell' OU 'Isaac Asimov'.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 2: NIVEAU 2 -->
<div id="level2-section" class="section-content">
    <div class="exercise-cards">

        <!-- Context Card -->
        <div class="exercise-card intro" style="border-left-color: #FF9800;">
            <div class="exercise-content-wrapper">
                <h4 class="exercise-title">Contexte : La Concession Automobile</h4>
                <div class="exercise-content">
                    <p>Vous analysez le stock d'une concession automobile.</p>
                    <div class="sql-table-container">
                        <table>
                            <thead>
                                <tr><th>id</th><th>marque</th><th>modele</th><th>couleur</th><th>annee</th><th>prix</th><th>kilométrage</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>1</td><td>Renault</td><td>Clio</td><td>Rouge</td><td>2018</td><td>12000</td><td>45000</td></tr>
                                <tr><td>2</td><td>Peugeot</td><td>208</td><td>Blanc</td><td>2020</td><td>15000</td><td>20000</td></tr>
                                <tr><td>3</td><td>Tesla</td><td>Model 3</td><td>Noir</td><td>2022</td><td>35000</td><td>10000</td></tr>
                                <tr><td>4</td><td>Renault</td><td>Mégane</td><td>Bleu</td><td>2015</td><td>8000</td><td>120000</td></tr>
                                <tr><td>5</td><td>Porsche</td><td>911</td><td>Gris</td><td>2019</td><td>95000</td><td>15000</td></tr>
                            </tbody>
                        </table>
                    </div>
                    <a href="concession.zip" download class="download-btn">📥 Télécharger la base (concession.zip)</a>

                    <p>INSERT INTO Voitures (id, marque, modele, couleur, annee, prix, kilometrage) VALUES
                        (1, 'Renault', 'Clio', 'Rouge', 2018, 12000, 45000),
                        (2, 'Peugeot', '208', 'Blanc', 2020, 15000, 20000),
                        (3, 'Tesla', 'Model 3', 'Noir', 2022, 35000, 10000),
                        (4, 'Renault', 'Mégane', 'Bleu', 2015, 8000, 120000),
                        (5, 'Porsche', '911', 'Gris', 2019, 95000, 15000);</p>
                </div>
            </div>
        </div>

        <!-- Exo 1 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">1. Catalogue trié</h4>
                <div class="exercise-content">
                    <p>Afficher toutes les voitures triées par prix croissant (du moins cher au plus cher).</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">2. Les Renault</h4>
                <div class="exercise-content">
                    <p>Afficher le modèle et le prix de toutes les voitures de marque 'Renault'.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">3. Voitures récentes et abordables</h4>
                <div class="exercise-content">
                    <p>Afficher les voitures fabriquées après 2017 (inclus) ET dont le prix est inférieur à 20 000 €.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">4. Couleurs disponibles</h4>
                <div class="exercise-content">
                    <p>Afficher la liste des différentes couleurs disponibles en stock, sans doublons.</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">5. Le kilométrage</h4>
                <div class="exercise-content">
                    <p>Afficher les voitures ayant moins de 50 000 km, triées par kilométrage croissant.</p>
                </div>
            </div>
        </div>

        <!-- Exo 6 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">6. Recherche spécifique</h4>
                <div class="exercise-content">
                    <p>Afficher les voitures qui ne sont PAS de couleur 'Blanc'.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 3: NIVEAU 3 -->
<div id="level3-section" class="section-content">
    <div class="exercise-cards">

        <!-- Context Card -->
        <div class="exercise-card intro" style="border-left-color: #F44336;">
            <div class="exercise-content-wrapper">
                <h4 class="exercise-title">Contexte : Le Refuge des Renards</h4>
                <div class="exercise-content">
                    <p>Vous gérez un refuge pour renards. Les données sont réparties sur trois tables.</p>
                    
                    <strong>Table <code>Renards</code></strong>
                    <div class="sql-table-container">
                        <table>
                            <thead><tr><th>id</th><th>nom</th><th>sexe</th><th>age</th><th>id_enclos</th></tr></thead>
                            <tbody>
                                <tr><td>1</td><td>Rusty</td><td>M</td><td>3</td><td>1</td></tr>
                                <tr><td>2</td><td>Vixey</td><td>F</td><td>2</td><td>1</td></tr>
                                <tr><td>3</td><td>Zorro</td><td>M</td><td>5</td><td>2</td></tr>
                                <tr><td>4</td><td>Luna</td><td>F</td><td>1</td><td>3</td></tr>
                                <tr><td>5</td><td>Shadow</td><td>M</td><td>4</td><td>NULL</td></tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <strong>Table <code>Enclos</code></strong>
                    <div class="sql-table-container">
                        <table>
                            <thead><tr><th>id</th><th>nom_enclos</th><th>surface_m2</th><th>type_sol</th></tr></thead>
                            <tbody>
                                <tr><td>1</td><td>La Forêt</td><td>500</td><td>Terre</td></tr>
                                <tr><td>2</td><td>La Plaine</td><td>300</td><td>Herbe</td></tr>
                                <tr><td>3</td><td>La Tanière</td><td>50</td><td>Sable</td></tr>
                            </tbody>
                        </table>
                    </div>
                    <a href="refuge_renards.sql" download class="download-btn">📥 Télécharger la base (refuge_renards.sql)</a>
                </div>
            </div>
        </div>

        <!-- Exo 1 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">1. Qui est où ?</h4>
                <div class="exercise-content">
                    <p>Afficher le nom du renard et le nom de l'enclos dans lequel il se trouve (nécessite une jointure).</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">2. Les grands espaces</h4>
                <div class="exercise-content">
                    <p>Afficher les noms des renards qui vivent dans un enclos de plus de 200 m².</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">3. Les mâles de la Forêt</h4>
                <div class="exercise-content">
                    <p>Afficher les renards mâles ('M') qui sont dans l'enclos nommé 'La Forêt'.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">4. L'âge des pensionnaires</h4>
                <div class="exercise-content">
                    <p>Afficher la liste des renards et de leur enclos, triée par âge du renard (du plus vieux au plus jeune).</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">5. Sans domicile</h4>
                <div class="exercise-content">
                    <p>Afficher les renards qui ne sont affectés à aucun enclos (<code>id_enclos</code> est NULL).</p>
                </div>
            </div>
        </div>

        <!-- Exo 6 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">6. Inventaire</h4>
                <div class="exercise-content">
                    <p>Afficher le nom de l'enclos et la surface pour tous les enclos qui ont un sol de type 'Herbe' ou 'Terre'.</p>
                </div>
            </div>
        </div>
    </div>
</div>
