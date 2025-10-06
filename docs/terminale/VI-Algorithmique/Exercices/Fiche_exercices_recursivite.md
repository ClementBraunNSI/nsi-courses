# 🔄 Fiche d'exercices – Récursivité

!!! info "🎯 Objectif"
    Maîtriser la programmation récursive en implémentant des fonctions qui s'appellent elles-mêmes pour résoudre des problèmes.

!!! tip "💡 Rappel pour tous les exercices"
    - Définir le **cas terminal** (ou cas de base) qui arrête la récursion
    - Définir le **cas général** (comment le problème se réduit à un sous-problème plus simple)
    - Implémenter la fonction **récursive** qui s'appelle elle-même

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
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.style.display === 'none' || solutionWrapper.style.display === '') {
        solutionWrapper.style.display = 'block';
        button.classList.add('active');
        arrow.style.transform = 'rotate(90deg)';
        button.innerHTML = '<span class="arrow" style="transform: rotate(90deg)">→</span> Masquer la correction';
    } else {
        solutionWrapper.style.display = 'none';
        button.classList.remove('active');
        arrow.style.transform = 'rotate(0deg)';
        button.innerHTML = '<span class="arrow">→</span> Voir la correction';
    }
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
    <button class="section-tab" onclick="showSection('basic-section')">🎯 Exercices de Base</button>
    <button class="section-tab" onclick="showSection('intermediate-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('advanced-section')">🚀 Niveau Avancé</button>
</div>

<div id="basic-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Base 🦊</div>
            <h4 class="exercise-title">Exercice 1 – Factorielle</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour la factorielle.<br>
                <strong>2.</strong> Écrire une fonction <code>factorielle(n)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>n = 5</code> et <code>n = 0</code>.<br>
                <em>Indice : le cas terminal est <code>0! = 1</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : 0! = 1
# Cas récursif : n! = n × (n-1)!

def factorielle(n: int) -> int:
    if n == 0:
        return 1
    return n * factorielle(n - 1)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Base 🦊</div>
            <h4 class="exercise-title">Exercice 2 – Suite de Fibonacci</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir les <strong>cas terminaux</strong> de la suite de Fibonacci.<br>
                <strong>2.</strong> Écrire une fonction <code>fibonacci(n)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>n = 6</code> et <code>n = 0</code>.<br>
                <em>Indice : les cas terminaux sont <code>F(0) = 0</code> et <code>F(1) = 1</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminaux : F(0) = 0, F(1) = 1
# Cas récursif : F(n) = F(n-1) + F(n-2)

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Base 🦊</div>
            <h4 class="exercise-title">Exercice 3 – Somme des chiffres</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour la somme des chiffres d'un entier.<br>
                <strong>2.</strong> Écrire une fonction <code>somme_chiffres(n)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>n = 245</code> et <code>n = 1001</code>.<br>
                <em>Indice : le cas terminal est <code>n = 0</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : n = 0
# Cas récursif : somme_chiffres(n) = (n % 10) + somme_chiffres(n // 10)

def somme_chiffres(n: int) -> int:
    if n == 0:
        return 0
    return (n % 10) + somme_chiffres(n // 10)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Exercice 4 – Puissance d'un nombre</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour <code>a^b</code>.<br>
                <strong>2.</strong> Écrire une fonction <code>puissance(a, b)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>a = 2, b = 5</code> et <code>a = 3, b = 0</code>.<br>
                <em>Indice : le cas terminal est <code>b = 0</code> car <code>a^0 = 1</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : exposant = 0, a^0 = 1
# Cas récursif : a^n = a × a^(n-1)

def puissance(a: int, n: int) -> int:
    if n == 0:
        return 1
    return a * puissance(a, n - 1)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Exercice 5 – Inversion de chaîne</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour inverser une chaîne de caractères.<br>
                <strong>2.</strong> Écrire une fonction <code>inverse_chaine(s)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>s = "NSI"</code> et <code>s = "informatique"</code>.<br>
                <em>Indice : le cas terminal est une chaîne vide ou d'un caractère.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : chaîne vide ou un seul caractère
# Cas récursif : inverse_chaine(s) = s[-1] + inverse_chaine(s[:-1])

def inverse_chaine(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + inverse_chaine(s[:-1])</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="intermediate-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Exercice 6 – Liste chaînée (POO)</h4>
            <div class="exercise-content">
                <strong>1.</strong> Créer une classe <code>Noeud</code> avec <code>valeur</code> et <code>suivant</code>.<br>
                <strong>2.</strong> Définir le <strong>cas terminal</strong> pour calculer la longueur d'une liste chaînée.<br>
                <strong>3.</strong> Écrire <code>longueur_liste(noeud)</code> <strong>récursive</strong> : longueur d'un noeud = 1 + longueur du suivant.<br>
                <strong>4.</strong> Créer une liste de 4 noeuds et tester.<br>
                <em>Indice : le cas terminal est un noeud <code>None</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : noeud est None (liste vide)
# Cas récursif : longueur = 1 + longueur du reste de la liste

class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

def longueur_liste(noeud: Noeud) -> int:
    if noeud is None:
        return 0
    return 1 + longueur_liste(noeud.suivant)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Exercice 7 – Recherche dans une liste</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour la recherche d'une valeur.<br>
                <strong>2.</strong> Écrire <code>recherche(liste, valeur)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>liste = [2, 5, 8, 10]</code> et <code>valeur = 5</code>.<br>
                <em>Indice : le cas terminal est une liste vide.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : liste vide (élément non trouvé) ou élément trouvé
# Cas récursif : chercher dans le reste de la liste

def recherche(liste: list, element) -> bool:
    if len(liste) == 0:
        return False
    if liste[0] == element:
        return True
    return recherche(liste[1:], element)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Exercice 8 – Somme des éléments d'une liste</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour la somme d'une liste.<br>
                <strong>2.</strong> Écrire <code>somme_liste(liste)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>liste = [1, 2, 3, 4, 5]</code>.<br>
                <em>Indice : le cas terminal est une liste vide.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : liste vide
# Cas récursif : somme = premier élément + somme du reste

def somme_liste(liste: list) -> int:
    if len(liste) == 0:
        return 0
    return liste[0] + somme_liste(liste[1:])</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="advanced-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Avancé 🚀</div>
            <h4 class="exercise-title">Exercice 9 – Palindrome</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour vérifier si une chaîne est un palindrome.<br>
                <strong>2.</strong> Écrire <code>est_palindrome(s)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>s = "radar"</code> et <code>s = "NSI"</code>.<br>
                <em>Indice : le cas terminal est une chaîne vide ou à un caractère.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : chaîne vide ou un seul caractère
# Cas récursif : premier = dernier ET le milieu est un palindrome

def est_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return est_palindrome(s[1:-1])
    else:
        return False</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Bonus 🦊</div>
            <h4 class="exercise-title">Exercice 10 – Dessin de motifs (bonus)</h4>
            <div class="exercise-content">
                <strong>1.</strong> Définir le <strong>cas terminal</strong> pour le dessin d'un triangle.<br>
                <strong>2.</strong> Écrire <code>triangle(n)</code> <strong>récursive</strong>.<br>
                <strong>3.</strong> Tester avec <code>n = 5</code>.<br>
                <em>Indice : le cas terminal est <code>n = 0</code>.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Cas terminal : n = 0
# Cas récursif : afficher n étoiles puis appel récursif avec n-1

def triangle(n: int) -> None:
    if n == 0:
        return
    print('*' * n)
    triangle(n - 1)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>