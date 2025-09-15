# 🌳 Fiche d'exercice : Les Arbres

!!! danger "⚠️ Attention"
      Tous les exercices doivent être implémentés en respectant les structures de données d'arbres binaires.
      ```python
         class Noeud:
             def __init__(self, valeur):
                 self.valeur = valeur
                 self.gauche = None
                 self.droite = None
      ```

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
    <button class="section-tab" onclick="showSection('knowledge-section')">📚 À connaître</button>
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau Facile</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau Difficile</button>
</div>

<div id="knowledge-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">À connaître 🦊</div>
            <h4 class="exercise-title">🌳 Parcours Préfixe (Préordre)</h4>
            <div class="exercise-content">
                <strong>Ordre de visite :</strong> Racine → Sous-arbre gauche → Sous-arbre droite<br>
                <strong>Utilisation :</strong> Copie d'arbre, évaluation d'expressions préfixées<br>
                <em>Exemple d'implémentation :</em>
                <pre><code class="language-python">def parcours_prefixe(noeud):
    if noeud is not None:
        print(noeud.valeur)  # Traiter la racine
        parcours_prefixe(noeud.gauche)  # Parcourir à gauche
        parcours_prefixe(noeud.droite)  # Parcourir à droite</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">À connaître 🦊</div>
            <h4 class="exercise-title">🌳 Parcours Infixe (Inordre)</h4>
            <div class="exercise-content">
                <strong>Ordre de visite :</strong> Sous-arbre gauche → Racine → Sous-arbre droite<br>
                <strong>Utilisation :</strong> Affichage trié des ABR, conversion d'expressions<br>
                <em>Exemple d'implémentation :</em>
                <pre><code class="language-python">def parcours_infixe(noeud):
    if noeud is not None:
        parcours_infixe(noeud.gauche)  # Parcourir à gauche
        print(noeud.valeur)  # Traiter la racine
        parcours_infixe(noeud.droite)  # Parcourir à droite</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">À connaître 🦊</div>
            <h4 class="exercise-title">🌳 Parcours Postfixe (Postordre)</h4>
            <div class="exercise-content">
                <strong>Ordre de visite :</strong> Sous-arbre gauche → Sous-arbre droite → Racine<br>
                <strong>Utilisation :</strong> Suppression d'arbre, évaluation d'expressions postfixées<br>
                <em>Exemple d'implémentation :</em>
                <pre><code class="language-python">def parcours_postfixe(noeud):
    if noeud is not None:
        parcours_postfixe(noeud.gauche)  # Parcourir à gauche
        parcours_postfixe(noeud.droite)  # Parcourir à droite
        print(noeud.valeur)  # Traiter la racine</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">À connaître 🦊</div>
            <h4 class="exercise-title">🔍 Insertion dans un ABR</h4>
            <div class="exercise-content">
                <strong>Principe :</strong> Comparer la valeur avec la racine et insérer récursivement<br>
                <strong>Complexité :</strong> O(log n) en moyenne, O(n) dans le pire cas<br>
                <em>Exemple d'implémentation :</em>
                <pre><code class="language-python">def inserer(racine, valeur):
    if racine is None:
        return Noeud(valeur)
    if valeur < racine.valeur:
        racine.gauche = inserer(racine.gauche, valeur)
    else:
        racine.droite = inserer(racine.droite, valeur)
    return racine</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">À connaître 🦊</div>
            <h4 class="exercise-title">🗑️ Suppression dans un ABR</h4>
            <div class="exercise-content">
                <strong>3 cas à gérer :</strong><br>
                • <strong>Cas 1 :</strong> Nœud feuille → Suppression directe<br>
                • <strong>Cas 2 :</strong> Nœud avec un enfant → Remplacer par l'enfant<br>
                • <strong>Cas 3 :</strong> Nœud avec deux enfants → Remplacer par le successeur<br>
                <em>Le successeur est le plus petit élément du sous-arbre droit</em>
            </div>
        </div>
    </div>
</div>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Exercice 1 - Création d'un arbre simple</h4>
            <div class="exercise-content">
                <strong>Créer un arbre binaire avec une racine de valeur 10, un enfant gauche de valeur 5 et un enfant droit de valeur 15.</strong><br>
                <strong>Afficher les valeurs des trois nœuds.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

# Création de l'arbre
racine = Noeud(10)
racine.gauche = Noeud(5)
racine.droite = Noeud(15)

# Affichage
print(f"Racine: {racine.valeur}")
print(f"Enfant gauche: {racine.gauche.valeur}")
print(f"Enfant droit: {racine.droite.valeur}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Exercice 2 - Parcours préfixe simple</h4>
            <div class="exercise-content">
                <strong>Implémenter une fonction de parcours préfixe qui affiche les valeurs des nœuds.</strong><br>
                <strong>Tester avec l'arbre créé dans l'exercice 1.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def parcours_prefixe(noeud):
    if noeud is not None:
        print(noeud.valeur)
        parcours_prefixe(noeud.gauche)
        parcours_prefixe(noeud.droite)

# Test avec l'arbre précédent
parcours_prefixe(racine)
# Affiche: 10, 5, 15</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Exercice 3 - Insertion simple dans un ABR</h4>
            <div class="exercise-content">
                <strong>Créer un ABR vide et y insérer les valeurs 8, 3, 10, 1, 6, 14, 4, 7, 13.</strong><br>
                <strong>Afficher l'arbre avec un parcours infixe pour vérifier l'ordre.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def inserer(racine, valeur):
    if racine is None:
        return Noeud(valeur)
    if valeur < racine.valeur:
        racine.gauche = inserer(racine.gauche, valeur)
    else:
        racine.droite = inserer(racine.droite, valeur)
    return racine

def parcours_infixe(noeud):
    if noeud is not None:
        parcours_infixe(noeud.gauche)
        print(noeud.valeur, end=" ")
        parcours_infixe(noeud.droite)

# Création de l'ABR
abr = None
valeurs = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for val in valeurs:
    abr = inserer(abr, val)

# Affichage trié
parcours_infixe(abr)
# Affiche: 1 3 4 6 7 8 10 13 14</code></pre>
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
            <h4 class="exercise-title">Exercice 4 - Calcul de la hauteur</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction qui calcule la hauteur d'un arbre binaire.</strong><br>
                <em>La hauteur d'un arbre vide est -1, celle d'une feuille est 0.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def hauteur(noeud):
    if noeud is None:
        return -1
    hauteur_gauche = hauteur(noeud.gauche)
    hauteur_droite = hauteur(noeud.droite)
    return 1 + max(hauteur_gauche, hauteur_droite)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Exercice 5 - Recherche dans un ABR</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction qui recherche une valeur dans un ABR et renvoie True si elle existe, False sinon.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def rechercher(racine, valeur):
    if racine is None:
        return False
    if racine.valeur == valeur:
        return True
    elif valeur < racine.valeur:
        return rechercher(racine.gauche, valeur)
    else:
        return rechercher(racine.droite, valeur)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Exercice 6 - Compter les nœuds</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction qui compte le nombre total de nœuds dans un arbre binaire.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def compter_noeuds(noeud):
    if noeud is None:
        return 0
    return 1 + compter_noeuds(noeud.gauche) + compter_noeuds(noeud.droite)</code></pre>
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
            <h4 class="exercise-title">Exercice 7 - Suppression d'une feuille</h4>
            <div class="exercise-content">
                <strong>Implémenter la suppression d'un nœud feuille dans un ABR.</strong><br>
                <em>Gérer uniquement le cas où le nœud à supprimer est une feuille.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def supprimer_feuille(racine, valeur):
    if racine is None:
        return None
    
    if valeur < racine.valeur:
        racine.gauche = supprimer_feuille(racine.gauche, valeur)
    elif valeur > racine.valeur:
        racine.droite = supprimer_feuille(racine.droite, valeur)
    else:
        # Nœud trouvé
        if racine.gauche is None and racine.droite is None:
            # C'est une feuille
            return None
        else:
            print(f"Le nœud {valeur} n'est pas une feuille")
    
    return racine</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Exercice 8 - Parcours en largeur</h4>
            <div class="exercise-content">
                <strong>Implémenter un parcours en largeur (niveau par niveau) d'un arbre binaire.</strong><br>
                <em>Utiliser une file (queue) pour l'implémentation.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">from collections import deque

def parcours_largeur(racine):
    if racine is None:
        return
    
    file = deque([racine])
    
    while file:
        noeud = file.popleft()
        print(noeud.valeur, end=" ")
        
        if noeud.gauche:
            file.append(noeud.gauche)
        if noeud.droite:
            file.append(noeud.droite)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Exercice 9 - Minimum et Maximum d'un ABR</h4>
            <div class="exercise-content">
                <strong>Écrire deux fonctions pour trouver la valeur minimale et maximale dans un ABR.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def minimum_abr(racine):
    if racine is None:
        return None
    while racine.gauche is not None:
        racine = racine.gauche
    return racine.valeur

def maximum_abr(racine):
    if racine is None:
        return None
    while racine.droite is not None:
        racine = racine.droite
    return racine.valeur</code></pre>
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
            <h4 class="exercise-title">Exercice 10 - Suppression complète dans un ABR</h4>
            <div class="exercise-content">
                <strong>Implémenter la suppression complète d'un nœud dans un ABR (gérer les 3 cas).</strong><br>
                <em>Cas 1: feuille, Cas 2: un enfant, Cas 3: deux enfants</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def supprimer(racine, valeur):
    if racine is None:
        return None
    
    if valeur < racine.valeur:
        racine.gauche = supprimer(racine.gauche, valeur)
    elif valeur > racine.valeur:
        racine.droite = supprimer(racine.droite, valeur)
    else:
        # Nœud trouvé
        # Cas 1: Nœud feuille
        if racine.gauche is None and racine.droite is None:
            return None
        
        # Cas 2: Nœud avec un seul enfant
        elif racine.gauche is None:
            return racine.droite
        elif racine.droite is None:
            return racine.gauche
        
        # Cas 3: Nœud avec deux enfants
        else:
            # Trouver le successeur (minimum du sous-arbre droit)
            successeur = racine.droite
            while successeur.gauche is not None:
                successeur = successeur.gauche
            
            # Remplacer la valeur
            racine.valeur = successeur.valeur
            
            # Supprimer le successeur
            racine.droite = supprimer(racine.droite, successeur.valeur)
    
    return racine</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
            <h4 class="exercise-title">Exercice 11 - Vérifier si un arbre est un ABR</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction qui vérifie si un arbre binaire donné respecte les propriétés d'un ABR.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def est_abr(racine, min_val=float('-inf'), max_val=float('inf')):
    if racine is None:
        return True
    
    if racine.valeur <= min_val or racine.valeur >= max_val:
        return False
    
    return (est_abr(racine.gauche, min_val, racine.valeur) and
            est_abr(racine.droite, racine.valeur, max_val))</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
            <h4 class="exercise-title">Exercice 12 - Reconstruction d'un ABR</h4>
            <div class="exercise-content">
                <strong>À partir d'un parcours infixe et préfixe, reconstruire l'ABR original.</strong><br>
                <em>Exemple: Infixe [1,3,4,6,7,8,10,13,14], Préfixe [8,3,1,6,4,7,10,14,13]</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def reconstruire_abr(prefixe, infixe):
    if not prefixe or not infixe:
        return None
    
    # La racine est le premier élément du parcours préfixe
    racine_val = prefixe[0]
    racine = Noeud(racine_val)
    
    # Trouver la position de la racine dans le parcours infixe
    idx_racine = infixe.index(racine_val)
    
    # Diviser les parcours
    infixe_gauche = infixe[:idx_racine]
    infixe_droite = infixe[idx_racine + 1:]
    
    prefixe_gauche = prefixe[1:1 + len(infixe_gauche)]
    prefixe_droite = prefixe[1 + len(infixe_gauche):]
    
    # Construire récursivement les sous-arbres
    racine.gauche = reconstruire_abr(prefixe_gauche, infixe_gauche)
    racine.droite = reconstruire_abr(prefixe_droite, infixe_droite)
    
    return racine</code></pre>
            </div>
        </div>
    </div>
</div>
</div>