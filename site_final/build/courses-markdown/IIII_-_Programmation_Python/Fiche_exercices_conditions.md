# Fiche d'exercices : Les conditions en Python

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
    <button class="section-tab" onclick="showSection('advanced-section')">🌟 Conditions composées</button>
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
                    <li>N'oubliez pas les deux points <code>:</code> après la condition</li>
                    <li>Faites attention à l'indentation après une condition</li>
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
            <h4 class="exercise-title">Comparaison simple</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande un nombre à l'utilisateur</li>
                    <li>Affiche "Positif" si le nombre est supérieur à 0</li>
                    <li>Affiche "Négatif" si le nombre est inférieur à 0</li>
                    <li>Affiche "Nul" si le nombre est égal à 0</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre = float(input("Entrez un nombre : "))

if nombre > 0:
    print("Positif")
elif nombre < 0:
    print("Négatif")
else:
    print("Nul")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Pair ou impair</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui détermine si un nombre est pair ou impair.</strong></p>
                <p><em>Utiliser l'opérateur modulo <code>%</code> qui donne le reste de la division</em></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre = int(input("Entrez un nombre entier : "))

if nombre % 2 == 0:
    print(nombre, "est un nombre pair")
else:
    print(nombre, "est un nombre impair")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Permission de sortie</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande l'âge d'une personne</li>
                    <li>Affiche "Tu peux sortir seul" si l'âge est supérieur ou égal à 18</li>
                    <li>Affiche "Tu dois être accompagné" sinon</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">age = int(input("Quel est ton âge ? "))

if age >= 18:
    print("Tu peux sortir seul")
else:
    print("Tu dois être accompagné")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="advanced-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Note et appréciation</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande une note sur 20</li>
                    <li>Affiche "Excellent" si la note est supérieure ou égale à 16</li>
                    <li>Affiche "Bien" si la note est entre 14 et 16</li>
                    <li>Affiche "Assez bien" si la note est entre 12 et 14</li>
                    <li>Affiche "Passable" si la note est entre 10 et 12</li>
                    <li>Affiche "Insuffisant" sinon</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">note = float(input("Entrez votre note sur 20 : "))

if note >= 16:
    print("Excellent")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Calculatrice avec menu</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande deux nombres</li>
                    <li>Demande quelle opération effectuer (1: addition, 2: soustraction, 3: multiplication, 4: division)</li>
                    <li>Affiche le résultat de l'opération choisie</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

print("Quelle opération souhaitez-vous effectuer ?")
print("1: Addition")
print("2: Soustraction")
print("3: Multiplication")
print("4: Division")

choix = int(input("Votre choix (1-4) : "))

if choix == 1:
    resultat = nombre1 + nombre2
    print(nombre1, "+", nombre2, "=", resultat)
elif choix == 2:
    resultat = nombre1 - nombre2
    print(nombre1, "-", nombre2, "=", resultat)
elif choix == 3:
    resultat = nombre1 * nombre2
    print(nombre1, "*", nombre2, "=", resultat)
elif choix == 4:
    if nombre2 == 0:
        print("Erreur: Division par zéro impossible")
    else:
        resultat = nombre1 / nombre2
        print(nombre1, "/", nombre2, "=", resultat)
else:
    print("Choix invalide")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Jeu du plus ou moins</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande un nombre entre 1 et 100</li>
                    <li>Compare avec le nombre 42</li>
                    <li>Affiche "Plus grand" si le nombre est trop petit</li>
                    <li>Affiche "Plus petit" si le nombre est trop grand</li>
                    <li>Affiche "Gagné!" si c'est le bon nombre</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">nombre_mystere = 42

proposition = int(input("Devinez le nombre entre 1 et 100 : "))

if proposition < nombre_mystere:
    print("Plus grand")
elif proposition > nombre_mystere:
    print("Plus petit")
else:
    print("Gagné!")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Tarif de cinéma</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui calcule le prix d'un billet de cinéma:</strong></p>
                <ul>
                    <li>Demande l'âge</li>
                    <li>Demande si on est étudiant (réponse "oui" ou "non")</li>
                    <li>Affiche le tarif:
                        <ul>
                            <li>Moins de 14 ans: 5€</li>
                            <li>Étudiant: 7€</li>
                            <li>Normal: 9€</li>
                        </ul>
                    </li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">age = int(input("Quel est votre âge ? "))
etudiant = input("Êtes-vous étudiant ? (oui/non) : ")

if age < 14:
    tarif = 5
elif etudiant.lower() == "oui":
    tarif = 7
else:
    tarif = 9

print("Le tarif de votre billet est de", tarif, "euros.")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Année bissextile</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui détermine si une année est bissextile.</strong></p>
                <p>Une année est bissextile si:</p>
                <ul>
                    <li>Elle est divisible par 4 mais pas par 100</li>
                    <li>OU elle est divisible par 400</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">annee = int(input("Entrez une année : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(annee, "est une année bissextile")
else:
    print(annee, "n'est pas une année bissextile")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
            <h4 class="exercise-title">Distributeur de boissons</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui simule un distributeur de boissons:</strong></p>
                <ul>
                    <li>Affiche un menu avec: 1-Eau (1€), 2-Soda (2€), 3-Jus (1.5€)</li>
                    <li>Demande le choix de boisson</li>
                    <li>Demande l'argent inséré</li>
                    <li>Affiche si l'achat est possible et la monnaie à rendre</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">print("Distributeur de boissons")
print("1 - Eau (1€)")
print("2 - Soda (2€)")
print("3 - Jus (1.5€)")

choix = int(input("Votre choix (1-3) : "))
argent = float(input("Insérez votre argent (en euros) : "))

if choix == 1:
    prix = 1
    boisson = "Eau"
elif choix == 2:
    prix = 2
    boisson = "Soda"
elif choix == 3:
    prix = 1.5
    boisson = "Jus"
else:
    print("Choix invalide")
    prix = 0
    boisson = ""

if boisson != "":
    if argent >= prix:
        monnaie = argent - prix
        print("Voici votre", boisson)
        print("Monnaie à rendre :", round(monnaie, 2), "euros")
    else:
        print("Argent insuffisant. Il manque", round(prix - argent, 2), "euros")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
            <h4 class="exercise-title">Jeu Pierre-Feuille-Ciseaux</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui:</strong></p>
                <ul>
                    <li>Demande au joueur 1 de choisir entre "pierre", "feuille" ou "ciseaux"</li>
                    <li>Demande au joueur 2 de choisir</li>
                    <li>Affiche qui a gagné selon les règles du jeu</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">joueur1 = input("Joueur 1, choisissez pierre, feuille ou ciseaux : ").lower()
joueur2 = input("Joueur 2, choisissez pierre, feuille ou ciseaux : ").lower()

if joueur1 == joueur2:
    print("Égalité !")
elif joueur1 == "pierre":
    if joueur2 == "ciseaux":
        print("Joueur 1 gagne ! La pierre écrase les ciseaux.")
    else:  # joueur2 == "feuille"
        print("Joueur 2 gagne ! La feuille enveloppe la pierre.")
elif joueur1 == "feuille":
    if joueur2 == "pierre":
        print("Joueur 1 gagne ! La feuille enveloppe la pierre.")
    else:  # joueur2 == "ciseaux"
        print("Joueur 2 gagne ! Les ciseaux coupent la feuille.")
elif joueur1 == "ciseaux":
    if joueur2 == "feuille":
        print("Joueur 1 gagne ! Les ciseaux coupent la feuille.")
    else:  # joueur2 == "pierre"
        print("Joueur 2 gagne ! La pierre écrase les ciseaux.")
else:
    print("Entrée invalide. Utilisez pierre, feuille ou ciseaux.")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Catégories d'âge</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui détermine la catégorie sportive selon l'âge:</strong></p>
                <ul>
                    <li>Moins de 6 ans: "Baby"</li>
                    <li>De 6 à 8 ans: "Poussin"</li>
                    <li>De 9 à 11 ans: "Pupille"</li>
                    <li>De 12 à 14 ans: "Benjamin"</li>
                    <li>15 ans et plus: "Cadet"</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">age = int(input("Quel est l'âge du sportif ? "))

if age < 6:
    categorie = "Baby"
elif age <= 8:
    categorie = "Poussin"
elif age <= 11:
    categorie = "Pupille"
elif age <= 14:
    categorie = "Benjamin"
else:
    categorie = "Cadet"

print("Catégorie sportive :", categorie)</code></pre>
            </div>
        </div>
    </div>
</div>
</div>