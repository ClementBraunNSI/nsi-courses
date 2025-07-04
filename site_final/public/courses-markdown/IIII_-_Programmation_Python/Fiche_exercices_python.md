# Fiche d'exercices : Python

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
    <button class="section-tab" onclick="showSection('interaction-section')">🌟 Interaction utilisateur</button>
    <button class="section-tab" onclick="showSection('application-section')">🔥 Exercices d'application</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Important ⚠️</div>
            <h4 class="exercise-title">Consignes importantes</h4>
            <div class="exercise-content">
                <p><strong>Pour tous les exercices :</strong></p>
                <ul>
                    <li>N'oubliez pas les guillemets <code>"</code> ou <code>'</code> pour les chaînes de caractères</li>
                    <li>Faites attention aux majuscules et minuscules</li>
                    <li>Testez votre code après chaque modification</li>
                    <li>Créez un fichier Python différent pour chaque exercice (ex: <code>exercice1.py</code>, <code>exercice2.py</code>, etc.)</li>
                    <li>Recopiez vos programmes sur votre cahier pour pouvoir les réviser plus tard</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Premier programme</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche "Bonjour tout le monde!" dans le terminal.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">print("Bonjour tout le monde")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Variables simples</h4>
            <div class="exercise-content">
                <p><strong>Créer une variable <code>age</code> qui contient votre âge et une variable <code>prenom</code> qui contient votre prénom.</strong></p>
                <p><strong>Afficher ces variables dans le terminal.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">age = 16
prenom = "Jean"
print(prenom, age)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Calculs simples</h4>
            <div class="exercise-content">
                <p><strong>Créer deux variables <code>nombre1</code> et <code>nombre2</code> contenant respectivement les valeurs 42 et 7.</strong></p>
                <p><strong>Afficher leur somme, leur différence, leur produit et leur division.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre1 = 42
nombre2 = 7
print(nombre1+nombre2, nombre1-nombre2, nombre1*nombre2, nombre1/nombre2)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="interaction-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Demander le prénom</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande le prénom de l'utilisateur et affiche "Bonjour" suivi du prénom.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">prenom = input("Quel est ton prénom ? ")
print("Bonjour", prenom)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Calculatrice simple</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande deux nombres à l'utilisateur et affiche leur somme.</strong></p>
                <p><em>Attention : la fonction <code>input()</code> renvoie une chaîne de caractères, il faut convertir en nombre avec <code>int()</code></em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre1 = int(input("Premier nombre : "))
nombre2 = int(input("Deuxième nombre : "))
somme = nombre1 + nombre2
print("La somme est", somme)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Présentation complète</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande le nom, l'âge et la classe d'un élève, puis affiche une phrase de présentation complète.</strong></p>
                <p><em>Exemple : "Je m'appelle Jean, j'ai 15 ans et je suis en seconde."</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nom = input("Quel est ton nom ? ")
age = input("Quel est ton âge ? ")
classe = input("En quelle classe es-tu ? ")
print("Je m'appelle", nom + ", j'ai", age, "ans et je suis en", classe + ".")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="application-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Convertisseur d'euros</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui convertit un montant en euros vers des dollars (1 euro = 1.09 dollars).</strong></p>
                <p><em>Le programme doit demander le montant en euros et afficher le résultat en dollars.</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">euros = float(input("Montant en euros : "))
taux = 1.09
dollars = euros * taux
print(euros, "euros équivalent à", dollars, "dollars")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Calcul d'âge</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande l'année de naissance d'une personne et calcule son âge en 2024.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">annee_naissance = int(input("Année de naissance : "))
annee_actuelle = 2024
age = annee_actuelle - annee_naissance
print("Vous avez", age, "ans en 2024")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Message personnalisé</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui demande:</strong></p>
                <ul>
                    <li>Le prénom de l'utilisateur</li>
                    <li>Sa matière préférée</li>
                    <li>Sa note dans cette matière</li>
                </ul>
                <p><strong>Puis affiche un message personnalisé comme: "Bravo [prénom], tu as eu [note]/20 en [matière]!"</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">prenom = input("Quel est ton prénom ? ")
matiere = input("Quelle est ta matière préférée ? ")
note = input("Quelle note as-tu eu dans cette matière ? ")
print("Bravo", prenom + ", tu as eu", note + "/20 en", matiere + "!")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Calculateur de moyenne</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande 3 notes à l'utilisateur</li>
                    <li>Calcule la moyenne de ces notes</li>
                    <li>Affiche la moyenne avec un message approprié</li>
                </ul>
                <p><em>N'oubliez pas de convertir les entrées en nombres décimaux avec <code>float()</code></em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))
moyenne = (note1 + note2 + note3) / 3
print("Ta moyenne est de", round(moyenne, 2))</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Générateur de pseudo</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui crée un pseudo à partir:</strong></p>
                <ul>
                    <li>Des 3 premières lettres du prénom</li>
                    <li>Des 2 premières lettres du nom</li>
                    <li>De l'âge</li>
                </ul>
                <p><em>Exemple: Pour "Thomas Dupont, 15 ans" → "ThoDu15"</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">prenom = input("Ton prénom : ")
nom = input("Ton nom : ")
age = input("Ton âge : ")
debut_prenom = prenom[0:3]
debut_nom = nom[0:2]
pseudo = debut_prenom + debut_nom + age
print("Ton pseudo est :", pseudo)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Prix des bonbons</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande le prix d'un bonbon</li>
                    <li>Demande combien de bonbons on veut acheter</li>
                    <li>Affiche le prix total</li>
                    <li>Affiche combien il restera d'argent si on a 10 euros</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">prix_bonbon = float(input("Prix d'un bonbon en euros : "))
nombre_bonbons = int(input("Combien de bonbons veux-tu acheter ? "))
prix_total = prix_bonbon * nombre_bonbons
argent_initial = 10
argent_restant = argent_initial - prix_total
print("Prix total :", prix_total, "euros")
print("Il te restera", argent_restant, "euros sur tes 10 euros")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Convertisseur de temps</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui convertit un nombre de minutes en heures et minutes.</strong></p>
                <p><em>Exemple: 145 minutes = 2 heures et 25 minutes</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">minutes_total = int(input("Nombre de minutes : "))
heures = minutes_total // 60  # Division entière
minutes = minutes_total % 60  # Reste de la division
print(minutes_total, "minutes =", heures, "heures et", minutes, "minutes")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Message décoré</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande un mot à l'utilisateur</li>
                    <li>Affiche ce mot entre des symboles décoratifs</li>
                </ul>
                <p><em>Exemple: Pour le mot "PYTHON" → "*** PYTHON ***"</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">mot = input("Entre un mot : ")
decoration = "*** "
mot_decore = decoration + mot + " ***"
print(mot_decore)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>