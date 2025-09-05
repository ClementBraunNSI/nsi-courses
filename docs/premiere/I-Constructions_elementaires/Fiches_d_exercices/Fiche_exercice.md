# Fiche d'exercices : Types en python

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
    background: linear-gradient(135deg, #cccccc 0%, #999999 100%);
    color: #666666;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: not-allowed;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    opacity: 0.5;
}

.toggle-solution:hover {
    /* Pas d'effet hover pour les boutons désactivés */
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
    // Fonction désactivée - les corrections ne sont pas accessibles
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
            <h4 class="exercise-title">Types en Python</h4>
            <div class="exercise-content">
                <p><strong>Donner les types des valeurs suivantes : <code>13</code>, <code>14.5</code>, <code>'Hello World!'</code>, <code>True</code>, <code>'15.5'</code></strong></p>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Table de vérité XOR</h4>
            <div class="exercise-content">
                <p><strong>À l'aide de python, écrire un programme qui affiche dans le terminal la table de vérité de la fonction booléenne <code>xor</code>.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>print('Table de vérité du XOR')
print('a','b','s')
print(0,0,0)
print(0,1,1)
print(1,0,1)
print(1,1,0)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Somme de deux nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui permet d'afficher la somme de deux nombres entiers de la forme 'La somme est x+y' avec x et y défini précédemment.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>x = 4
y = 3
print('La somme est', x+y)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Affichage amélioré</h4>
            <div class="exercise-content">
                <p><strong>Améliorer le programme précédent pour qu'il affiche 'La somme de x et y est x+y'.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>x = 4
y = 3
print('La somme de',x, ' et ', y, ' est ', x+y)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Concaténation de chaînes</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui instancie deux chaînes de caractères, les concatène et affiche le résultat sous la forme <code>'La chaîne résultante est : [résultat]'</code>.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>chaine_a = "Bonjour"
chaine_b = "Au Revoir"
print("La chaîne résultante est :", chaine_a+chaine_b)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Étude de code</h4>
            <div class="exercise-content">
                <p><strong>Évaluer les valeurs de result à la fin de chaque programme.</strong></p>
                <pre><code>x = 8
y = 6
if x > y:
    result = x - y
else:
    result = y - x</code></pre>
                <pre><code>a = 4
b = 9
if a < b:
    result = a + b
else:
    result = a * b</code></pre>
                <pre><code>m = 7
n = 3
if m % 2 == 0:
    result = m * n
else:
    result = m + n</code></pre>
                <p><strong>À l'aide de python, évaluer les résultats de ces comparaisons avec x = 5, x = 10 et x = -20</strong></p>
                <ol>
                    <li>x < 20 and x > - 20</li>
                    <li>x > 5 or x < 3</li>
                    <li><code>not (x == 10)</code></li>
                    <li><code>x >= 0 and x <= 10</code></li>
                    <li><code>x % 2 == 0 or x % 3 == 0</code></li>
                    <li><code>x < 0 or (x > 0 and x % 2 != 0)</code></li>
                </ol>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Parité d'un nombre</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche dans le terminal si un nombre est pair ou impair.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>a = int(input("Entrez un nombre"))
if a % 2 == 0:  # Si le reste de la division de a par 2 est 0 -> Si 2 divise a
    print("pair")
else:
    print("impair")</code></pre>
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
            <h4 class="exercise-title">Maximum entre trois nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui permet de trouver la valeur maximale entre trois variables entières. Ce programme affichera dans la console : "Le nombre <code>x</code> est plus grand que <code>y</code> et <code>z</code>.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>val_1 = int(input("Valeur 1"))
val_2 = int(input("Valeur 2"))
val_3 = int(input("Valeur 3"))
if val_1 > val_2 and val_1 > val_3:
    print(val_1, " est la plus grande")
elif val_2 > val_1 and val_2 > val_3:
    print(val_2, " est la plus grande")
elif val_3 > val_1 and val_3 > val_2:
    print(val_3, " est la plus grande")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Calculatrice basique</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui est une calculatrice basique. Elle demandera à l'utilisateur 2 nombres entiers <code>a</code> et <code>b</code> et un opérateur (<code>+</code>,<code>-</code>,<code>*</code>,<code>/</code>). Ce programme affichera : L'opération <code>a</code> <code>operateur</code> <code>b</code> vaut ...</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>a = int(input("Entrez un premier nombre"))
b = int(input("Entrez un second nombre"))
operateur = input("Entrez un opérateur : + - / *")
if operateur == "+":
    print(a+b)
elif operateur == "-":
    print(a-b)
elif operateur == "*":
    print(a*b)
elif operateur == "/":
    # On ne peut pas diviser par zéro
    if b != 0:
        print(a/b)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Profit ou perte</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui étant donné deux valeurs cout_de_production et prix_de_vente, affiche dans le terminal <code>profit</code> si le cout est inférieur au prix de vente, <code>perte</code> sinon.</strong></p>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>prix_de_vente = int(input("Entrez un prix de vente"))
cout_de_production = int(input("Entrez un coût de production"))

if prix_de_vente > cout_de_production:
    print("profit")
elif prix_de_vente == cout_de_production:
    print("pas de marge")
else:
    print("perte")</code></pre>
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
            <h4 class="exercise-title">Mentions au baccalauréat</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui prend une note sur 20 et affiche dans le terminal si l'étudiant a obtenu une mention :</strong></p>
                <ul>
                    <li><code>'Très bien'</code> pour une note supérieure ou égale à 16.</li>
                    <li><code>'Bien'</code> pour une note entre 14 et 15.</li>
                    <li><code>'Assez bien'</code> pour une note entre 12 et 13.</li>
                    <li><code>'Passable'</code> pour une note entre 10 et 11.</li>
                    <li><code>'Échec'</code> pour une note inférieure à 10.</li>
                </ul>
            </div>
            <button class="toggle-solution" disabled>
                <span class="arrow">🔒</span> Correction non disponible
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Demander à l'utilisateur de saisir une note
note = float(input("Entrez une note sur 20 : "))

# Vérifier la mention correspondante et afficher le résultat
if note >= 16:
    print("Mention : Très bien")
elif 14 <= note <= 15:
    print("Mention : Bien")
elif 12 <= note <= 13:
    print("Mention : Assez bien")
elif 10 <= note <= 11:
    print("Mention : Passable")
else:
    print("Mention : Échec")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">
<div class="exercise-cards">
    <p>Aucun exercice difficile pour cette fiche.</p>
</div>
</div>
