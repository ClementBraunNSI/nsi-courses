# Fiche d'exercices : Instanciation ; Entrés / Sorties ; Boucles

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

.exercise-card.inst { border-left-color: #4CAF50; }
.exercise-card.io { border-left-color: #2196F3; }
.exercise-card.cond { border-left-color: #FF9800; }
.exercise-card.loop { border-left-color: #F44336; }

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.inst { background: rgba(76, 175, 80, 0.1); color: #4CAF50; }
.difficulty-badge.io { background: rgba(33, 150, 243, 0.1); color: #2196F3; }
.difficulty-badge.cond { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.loop { background: rgba(244, 67, 54, 0.1); color: #F44336; }

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
    background: linear-gradient(135deg, #ead466ff 0%, #e8a508ff 100%);
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
</style>

<script>
function showSection(sectionId) {
    // Masquer toutes les sections
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher la section sélectionnée
    document.getElementById(sectionId).classList.add('active');
    
    // Activer l'onglet correspondant
    const buttons = document.getElementsByTagName('button');
    for (let btn of buttons) {
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(sectionId)) {
            btn.classList.add('active');
        }
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    showSection('inst-section');
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('inst-section')">📦 Instanciation & Opérations</button>
    <button class="section-tab" onclick="showSection('io-section')">🖨️ Entrées / Sorties</button>
    <button class="section-tab" onclick="showSection('cond-section')">🚦 Conditions</button>
    <button class="section-tab" onclick="showSection('loop-section')">🔄 Boucles</button>
</div>

<!-- SECTION 1: INSTANCIATION -->
<div id="inst-section" class="section-content">
    <div class="exercise-cards">
        
        <!-- Exo 1 -->
        <div class="exercise-card inst">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge inst">Niveau 1</div>
                <h4 class="exercise-title">Déclaration et Affichage</h4>
                <div class="exercise-content">
                    <p>Déclarer une variable entière <code>age</code> (ex: 25) et une variable réelle <code>prix</code> (ex: 19.99).<br>
                    Afficher une phrase : "J'ai [age] ans et le prix est [prix] euros."</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card inst">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge inst">Niveau 1</div>
                <h4 class="exercise-title">Opérations de base</h4>
                <div class="exercise-content">
                    <p>Déclarer deux entiers <code>a = 10</code> et <code>b = 5</code>.<br>
                    Calculer et afficher leur somme, différence, produit et division.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card inst">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge inst">Niveau 2</div>
                <h4 class="exercise-title">Échange de valeurs (Swap)</h4>
                <div class="exercise-content">
                    <p>Déclarer <code>a = 5</code> et <code>b = 10</code>.<br>
                    Échanger les valeurs de <code>a</code> et <code>b</code> (il faut une variable temporaire !).<br>
                    Afficher les valeurs après échange.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 2: ENTRÉES / SORTIES -->
<div id="io-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card io">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge io">Niveau 1</div>
                <h4 class="exercise-title">Lire un entier</h4>
                <div class="exercise-content">
                    <p>Demander à l'utilisateur d'entrer un nombre entier, le lire avec <code>scanf</code>, puis l'afficher.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card io">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge io">Niveau 1</div>
                <h4 class="exercise-title">Somme utilisateur</h4>
                <div class="exercise-content">
                    <p>Demander deux nombres à l'utilisateur et afficher leur somme.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card io">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge io">Niveau 2</div>
                <h4 class="exercise-title">Votre taille</h4>
                <div class="exercise-content">
                    <p>Demander la taille de l'utilisateur en mètres (ex: 1.75) et l'afficher.<br>Attention au type de variable !</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 3: CONDITIONS -->
<div id="cond-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 1</div>
                <h4 class="exercise-title">Positif ou Négatif</h4>
                <div class="exercise-content">
                    <p>Demander un nombre. Afficher s'il est positif, négatif ou nul.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 1</div>
                <h4 class="exercise-title">Pair ou Impair</h4>
                <div class="exercise-content">
                    <p>Demander un entier. Dire s'il est pair ou impair (utiliser le modulo <code>%</code>).</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 1</div>
                <h4 class="exercise-title">Maximum de 2 nombres</h4>
                <div class="exercise-content">
                    <p>Lire deux nombres, afficher le plus grand.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 2</div>
                <h4 class="exercise-title">Maximum de 3 nombres</h4>
                <div class="exercise-content">
                    <p>Lire trois nombres, afficher le plus grand des trois.</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 1</div>
                <h4 class="exercise-title">Majorité</h4>
                <div class="exercise-content">
                    <p>Demander l'âge. Si >= 18, afficher "Majeur", sinon "Mineur".</p>
                </div>
            </div>
        </div>

        <!-- Exo 6 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 2</div>
                <h4 class="exercise-title">Mentions</h4>
                <div class="exercise-content">
                    <p>Lire une note. Afficher la mention :<br>
                    >= 16: Très bien<br>
                    >= 14: Bien<br>
                    >= 12: Assez bien<br>
                    >= 10: Passable<br>
                    Sinon: Insuffisant</p>
                </div>
            </div>
        </div>

        <!-- Exo 7 -->
        <div class="exercise-card cond">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge cond">Niveau 3</div>
                <h4 class="exercise-title">Calculatrice Simple</h4>
                <div class="exercise-content">
                    <p>Demander deux nombres et un choix d'opération (1:+, 2:-, 3:*).<br>
                    Afficher le résultat correspondant.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 4: BOUCLES -->
<div id="loop-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 1</div>
                <h4 class="exercise-title">Compter de 1 à 10</h4>
                <div class="exercise-content">
                    <p>Utiliser une boucle <code>for</code> pour afficher les nombres de 1 à 10.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 1</div>
                <h4 class="exercise-title">Décompte (While)</h4>
                <div class="exercise-content">
                    <p>Utiliser une boucle <code>while</code> pour afficher de 10 à 1.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 2</div>
                <h4 class="exercise-title">Table de multiplication</h4>
                <div class="exercise-content">
                    <p>Demander un nombre <code>n</code> et afficher sa table de multiplication de 1 à 10.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 2</div>
                <h4 class="exercise-title">Somme cumulative</h4>
                <div class="exercise-content">
                    <p>Calculer la somme des entiers de 1 à <code>n</code> (donné par l'utilisateur).</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 2</div>
                <h4 class="exercise-title">Nombres pairs</h4>
                <div class="exercise-content">
                    <p>Afficher tous les nombres pairs entre 0 et <code>n</code>.</p>
                </div>
            </div>
        </div>

        <!-- Exo 6 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 2</div>
                <h4 class="exercise-title">Boucle de saisie</h4>
                <div class="exercise-content">
                    <p>Demander un nombre à l'utilisateur tant qu'il ne saisit pas 0 (boucle <code>do...while</code> ou <code>while</code>).</p>
                </div>
            </div>
        </div>

        <!-- Exo 7 -->
        <div class="exercise-card loop">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge loop">Niveau 3</div>
                <h4 class="exercise-title">Carré d'étoiles</h4>
                <div class="exercise-content">
                    <p>Demander une taille <code>n</code> et afficher un carré de <code>n * n</code> étoiles.</p>
                </div>
            </div>
        </div>

    </div>
</div>
