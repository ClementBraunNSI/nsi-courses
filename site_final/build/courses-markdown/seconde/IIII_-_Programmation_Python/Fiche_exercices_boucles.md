# Fiche d'exercices : Les boucles en Python

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

.exercise-content-wrapper {
    width: 100%;
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
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
}

.toggle-solution:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
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
    const card = button.closest('.exercise-card');
    const solutionWrapper = card.querySelector('.solution-wrapper');
    
    // Créer la modal si elle n'existe pas déjà
    let modal = document.getElementById('solution-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'solution-modal';
        modal.className = 'solution-modal';
        document.body.appendChild(modal);
        
        // Fermer la modal en cliquant à l'extérieur
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeSolutionModal();
            }
        });
    }
    
    // Créer le contenu de la modal
    const exerciseTitle = card.querySelector('.exercise-title').textContent;
    const solutionContent = solutionWrapper.innerHTML;
    
    modal.innerHTML = `
        <div class="solution-content">
            <button class="solution-close" onclick="closeSolutionModal()">×</button>
            <h3>Correction : ${exerciseTitle}</h3>
            ${solutionContent}
        </div>
    `;
    
    // Afficher la modal
    modal.classList.add('show');
    document.body.style.overflow = 'hidden'; // Empêcher le scroll de la page
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
            <div class="difficulty-badge intro">Important ⚠️</div>
            <h4 class="exercise-title">Consignes importantes</h4>
            <div class="exercise-content">
                <p><strong>Pour tous les exercices :</strong></p>
                <ul>
                    <li>N'oubliez pas les deux points <code>:</code> après la boucle</li>
                    <li>Faites attention à l'indentation dans la boucle</li>
                    <li>Testez votre code avec différentes valeurs</li>
                    <li>Créez un fichier Python différent pour chaque exercice (ex: <code>exercice1.py</code>, <code>exercice2.py</code>, etc.)</li>
                    <li>Recopiez vos programmes sur votre cahier pour pouvoir les réviser plus tard</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Compte à rebours</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre de départ</li>
                    <li>Affiche le compte à rebours jusqu'à 0</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Tables de multiplication</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre</li>
                    <li>Affiche sa table de multiplication de 1 à 10</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Escalier d'étoiles</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre n</li>
                    <li>Affiche un escalier de n marches avec des étoiles</li>
                </ul>
                <p><em>Astuce : pour afficher <code>x</code> fois un caractère, on peut utiliser la syntaxe <code>'x' * n</code>.</em></p>
                <p><em>La chaîne de caractère "XXXXX" peut être créée via la syntaxe python suivante :</em></p>
                <pre><code>chaine_1 = "XXXXX"
chaine_2 = "X"*5
# avec chaine_1 == chaine_2</code></pre>
                <p><em>Exemple pour n=3:</em></p>
                <pre><code>*
**
***</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Somme des nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre n</li>
                    <li>Calcule la somme des nombres de 1 à n</li>
                    <li>Affiche le résultat</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Puissance de 2</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre n</li>
                    <li>Affiche les puissances de 2 jusqu'à 2^n</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Message répété</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande une phrase</li>
                    <li>Demande un nombre de répétitions</li>
                    <li>Affiche la phrase autant de fois que demandé</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</div>

<div id="easy-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Calculatrice continue</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande deux nombres et une opération</li>
                    <li>Affiche le résultat</li>
                    <li>Demande si on veut continuer (oui/non)</li>
                    <li>Recommence si la réponse est "oui"</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Devinette avec limite</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Donne 5 essais pour deviner un nombre entre 1 et 100</li>
                    <li>Affiche "Perdu!" si le nombre n'est pas trouvé après 5 essais</li>
                    <li>Affiche le nombre d'essais utilisés en cas de victoire</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Caisse enregistreuse</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande le prix des articles un par un</li>
                    <li>S'arrête quand on entre 0</li>
                    <li>Affiche le total des achats</li>
                    <li>Affiche la monnaie à rendre sur un billet de 50€</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
            <h4 class="exercise-title">Pyramide de nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui :</strong></p>
                <ul>
                    <li>Demande un nombre n</li>
                    <li>Affiche une pyramide de nombres</li>
                </ul>
                <p><em>Exemple pour n=3:</em></p>
                <pre><code>1
22
333</code></pre>
            </div>
        </div>
    </div>
</div>
</div>