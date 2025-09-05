# Fiche d'exercices : Boucles

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

/* Styles pour les contextes d'exercices difficiles */
.context-container {
    margin-bottom: 2rem;
    border: 2px solid #F44336;
    border-radius: 12px;
    overflow: hidden;
    background: rgba(244, 67, 54, 0.02);
}

.context-header {
    background: linear-gradient(135deg, #F44336 0%, #D32F2F 100%);
    color: white;
    padding: 1rem 1.5rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    user-select: none;
}

.context-header:hover {
    background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
    transform: translateY(-1px);
}

.context-header .arrow {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}

.context-header.active .arrow {
    transform: rotate(90deg);
}

.context-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background: white;
}

.context-content.show {
    max-height: 10000px;
    padding: 1rem;
}

.context-exercises {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

/* Uniformiser la hauteur des cartes d'exercices dans les contextes */
.context-exercises .exercise-card {
    min-height: 200px;
    align-items: stretch;
}

.context-exercises .exercise-content-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100%;
}

.context-exercises .exercise-content {
    flex-grow: 1;
}

.context-exercises .toggle-solution {
    margin-top: auto;
    align-self: flex-start;
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
    min-height: fit-content;
}

.exercise-content-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* Modal pour les solutions */
.solution-modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(3px);
}

.solution-modal.show {
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.3s ease;
}

.solution-content {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 2rem;
    max-width: 80%;
    max-height: 80%;
    overflow-y: auto;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    position: relative;
    animation: slideIn 0.3s ease;
}

.solution-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #f44336;
    color: white;
    border: none;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    cursor: pointer;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s ease;
}

.solution-close:hover {
    background: #d32f2f;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideIn {
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.solution-wrapper {
    display: none;
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.intro:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
}

.exercise-card.easy {
    border-left-color: #2196F3;
}

.exercise-card.easy:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(33, 150, 243, 0.4);
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.medium:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 152, 0, 0.4);
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.exercise-card.hard:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(244, 67, 54, 0.4);
}

.exercise-card.important {
    border-left-color: #ff8c42;
    background: linear-gradient(135deg, rgba(255, 140, 66, 0.05) 0%, rgba(255, 140, 66, 0.02) 100%);
}

.exercise-card.important:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 140, 66, 0.4);
}

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

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.easy {
    background: rgba(33, 150, 243, 0.1);
    color: #2196F3;
}

.difficulty-badge.medium {
    background: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.difficulty-badge.important {
    background: rgba(255, 140, 66, 0.1);
    color: #ff8c42;
}

.toggle-solution {
    background: #cccccc;
    color: #666666;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: not-allowed;
    font-size: 0.9rem;
    font-weight: 500;
    transition: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    opacity: 0.6;
}

.toggle-solution:hover {
    transform: none;
    box-shadow: none;
}

.toggle-solution.active {
    background: linear-gradient(135deg, #ff7f50 0%, #ff6347 100%);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution {
    height: 100%;
    overflow-y: auto;
}

.solution pre {
    margin: 0;
    font-size: 0.85rem;
}

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
    padding: 0;
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
    min-width: 200px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.section-content {
    display: none;
    margin-top: 2rem;
    padding: 2rem;
    background: #fafafa;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
}

.section-content.active {
    display: block;
}

/* JavaScript pour les fonctionnalités interactives */
.exercise-script {
    display: none;
}
</style>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices

function toggleSolution(button) {
    // Fonction désactivée - les corrections ne sont pas disponibles
    return false;
}

function closeSolutionModal() {
    const modal = document.getElementById('solution-modal');
    if (modal) {
        modal.classList.remove('show');
        document.body.style.overflow = ''; // Restaurer le scroll de la page
    }
}

// Fermer la modal avec la touche Échap
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeSolutionModal();
    }
});

function showSection(sectionId) {
    // Masquer toutes les sections
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher la section sélectionnée
    document.getElementById(sectionId).classList.add('active');
    event.target.classList.add('active');
}

function toggleContext(header) {
    const content = header.nextElementSibling;
    const arrow = header.querySelector('.arrow');
    
    if (content.classList.contains('show')) {
        content.classList.remove('show');
        header.classList.remove('active');
    } else {
        content.classList.add('show');
        header.classList.add('active');
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    const firstTab = document.querySelector('.section-tab');
    if (firstTab) {
        firstTab.click();
    }
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau Facile</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau Difficile</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Afficher les nombres de 1 à 100</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche dans le terminal tous les nombres entre 1 et 100. (à l'aide d'une boucle for puis d'une boucle tant que).</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">→</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Utilisation d'une boucle for
for i in range(1, 101):
    print(i)

# Utilisation d'une boucle while
i = 1
while i <= 100:
    print(i)
    i += 1</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Table de multiplication</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui prend un nombre entier et affiche sa table de multiplication (jusqu'à 10).</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Entrez un nombre entier : "))

for i in range(1, 11):
    print(i, "x", nombre, "=", i * nombre)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Somme des nombres de 1 à 100</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui réalise la somme des nombres entiers de 1 jusque 100.</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>somme = 0
for i in range(1, 101):
    somme += i
print("La somme de 1 à 100 est", somme)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="easy-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Afficher les nombres pairs entre 1 à 100</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche dans le terminal tous les nombres pairs entre 1 et 100.</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Utilisation d'une boucle for
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# Utilisation d'une boucle while
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Compter les voyelles</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui lit une chaîne de caractères et affiche le nombre de voyelles présentes dans cette chaîne.</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>phrase = input("Donnez votre phrase : ")
nb_voyelles = 0
for lettre in phrase:
    if lettre in 'aeiouyAEIOUY':
        nb_voyelles += 1
print("La phrase compte", nb_voyelles, "voyelles.")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Inverser une chaîne de caractères</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche les caractères d'une chaîne de caractères dans l'autre sens.</strong></p>
                <p><em>Exemple : "bonjour" → "ruojnob".</em></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>phrase = input("Donnez votre phrase : ")
resultat = ""
for carac in phrase:
    resultat = carac + resultat
print(resultat)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Somme des chiffres d'un nombre</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui calcule la somme des chiffres d'un nombre donné par l'utilisateur.</strong></p>
                <p><em>Exemple : pour 123, il affichera 6.</em></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = input("Donnez votre nombre : ")
resultat = 0
for chiffre in nombre:
    resultat = resultat + int(chiffre)
print("La somme des chiffres est :", resultat)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊🦊</div>
            <h4 class="exercise-title">Boucle jusqu'à un nombre négatif</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande en boucle un nombre à l'utilisateur. Si le nombre est positif, la boucle continue, si le nombre est négatif, la boucle s'arrête.</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Donnez un nombre : "))
while nombre >= 0:
    nombre = int(input("Donnez un autre nombre : "))</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊🦊</div>
            <h4 class="exercise-title">Multiples de 3</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande à l'utilisateur un nombre et affiche les multiples par 3 consécutifs.</strong></p>
                <p><em>Exemple : 1 → 3, 9, 27, 81...</em></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Donnez un nombre : "))
for i in range(10):
    nombre *= 3
    print(nombre)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊🦊</div>
            <h4 class="exercise-title">Divisions par 2</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande un nombre à l'utilisateur et affiche dans le terminal combien de fois celui-ci est divisible par 2.</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Donnez un nombre : "))
compteur = 0
while nombre > 1:
    nombre //= 2
    compteur += 1
print("Nombre de divisions par 2 :", compteur)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊🦊</div>
            <h4 class="exercise-title">Diviseurs et nombres premiers</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande un nombre <code>n</code> à un utilisateur et affiche dans le terminal ses diviseurs (autre que lui-même et 1). S'il n'en a aucun, affiche : "<code>Aucun diviseur, n est premier.</code>"</strong></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Donnez un nombre : "))
for i in range(2, nombre):
    if nombre % i == 0:
        print(i, " divise ", nombre)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊🦊</div>
            <h4 class="exercise-title">Conjecture de Syracuse</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui réalise la conjecture de Syracuse pour un nombre demandé par l'utilisateur. Tant que le nombre n'est pas 1, s'il est pair, on le divise par 2 sinon on le multiplie par 3 et on ajoute 1.</strong></p>
                <p><em>Exemple : 10 → 5 → 16 → 8 → 4 → 2 → 1</em></p>
            </div>
            <button class="toggle-solution">
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>nombre = int(input("Donnez un nombre : "))
while nombre != 1:
    print(nombre)
    if nombre % 2 == 0:
        nombre = nombre // 2
    else:
        nombre = nombre * 3 + 1
print(1)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>