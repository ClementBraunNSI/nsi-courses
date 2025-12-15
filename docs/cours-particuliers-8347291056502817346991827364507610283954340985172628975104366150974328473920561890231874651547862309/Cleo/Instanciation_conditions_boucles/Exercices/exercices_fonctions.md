# Fiche d'exercices : Fonctions en C

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
    showSection('intro-section');
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau 1</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau 2</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau 3</button>
</div>

<!-- SECTION 1: INTRODUCTION -->
<div id="intro-section" class="section-content">
    <div class="exercise-cards">
        
        <!-- Exo 1 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Afficher Bonjour</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>void dire_bonjour()</code> qui affiche simplement "Bonjour tout le monde !" suivi d'un saut de ligne.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Calcul de l'aire (Fonction)</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>float aire_rectangle(float longueur, float largeur)</code> qui renvoie l'aire du rectangle.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Somme de deux entiers</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int somme(int a, int b)</code> qui renvoie la somme de a et b.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Carré d'un nombre</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int carre(int n)</code> qui renvoie le carré de n.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 2: NIVEAU 1 -->
<div id="easy-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Conversion Celsius -> Fahrenheit</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>float conversion_c_f(float celsius)</code> qui convertit une température en Fahrenheit.<br>
                    Formule : <code>F = C * 1.8 + 32</code></p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Test de Parité</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int est_pair(int n)</code> qui renvoie 1 si le nombre est pair, 0 sinon.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Valeur Absolue</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int valeur_absolue(int n)</code> qui renvoie la valeur absolue de n (si n < 0, renvoie -n).</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Est Majeur (Procédure)</h4>
                <div class="exercise-content">
                    <p>Écrire une procédure <code>void est_majeur(int age)</code> qui affiche "Majeur" si age >= 18, "Mineur" sinon.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 3: NIVEAU 2 -->
<div id="medium-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Maximum de 3 nombres</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int max_trois(int a, int b, int c)</code> qui renvoie le plus grand des trois nombres.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Factorielle</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int factorielle(int n)</code> qui calcule la factorielle de n (n!).<br>
                    Exemple: 5! = 5*4*3*2*1 = 120.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Somme de 1 à n</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int somme_1_a_n(int n)</code> qui calcule la somme des entiers de 1 à n à l'aide d'une boucle.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Table de multiplication</h4>
                <div class="exercise-content">
                    <p>Écrire une procédure <code>void table_multiplication(int n)</code> qui affiche la table de multiplication de n de 1 à 10.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 4: NIVEAU 3 -->
<div id="hard-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 1 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Puissance</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int puissance(int nombre, int exposant)</code> qui calcule nombre^exposant sans utiliser la bibliothèque math.h.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Nombre Premier</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int est_premier(int n)</code> qui renvoie 1 si n est premier, 0 sinon.<br>
                    Un nombre est premier s'il n'est divisible que par 1 et lui-même.</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Suite de Fibonacci</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int fibonacci(int n)</code> qui renvoie le n-ième terme de la suite.<br>
                    u0 = 0, u1 = 1, u(n) = u(n-1) + u(n-2).</p>
                </div>
            </div>
        </div>

    </div>
</div>
