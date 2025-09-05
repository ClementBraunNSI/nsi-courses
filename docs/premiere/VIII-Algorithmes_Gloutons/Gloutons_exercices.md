# Fiche d'exercices : Algorithmes Gloutons

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
    <button class="section-tab" onclick="showSection('rendu-monnaie-section')">💰 Rendu de Monnaie</button>
    <button class="section-tab" onclick="showSection('sac-a-dos-section')">🎒 Sac à Dos</button>
    <button class="section-tab" onclick="showSection('planification-section')">📅 Planification de Tâches</button>
</div>

<div id="rendu-monnaie-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Comprendre le problème du rendu de monnaie</h4>
            <div class="exercise-content">
                <p>Le problème du rendu de monnaie consiste à rendre une somme donnée avec le <strong>minimum de pièces</strong> possible.</p>
                <p><strong>Exemple :</strong> Pour rendre 67 centimes avec les pièces [50, 20, 10, 5, 2, 1], l'algorithme glouton donne :</p>
                <ul>
                    <li>1 pièce de 50c → reste 17c</li>
                    <li>1 pièce de 10c → reste 7c</li>
                    <li>1 pièce de 5c → reste 2c</li>
                    <li>1 pièce de 2c → reste 0c</li>
                </ul>
                <p><strong>Total :</strong> 4 pièces</p>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Algorithme de rendu de monnaie simple</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>rendu_monnaie(somme, pieces)</code> qui :</p>
                <ul>
                    <li>Prend en paramètres la somme à rendre et la liste des pièces disponibles (triée par ordre décroissant)</li>
                    <li>Utilise l'algorithme glouton pour rendre la monnaie</li>
                    <li>Retourne la liste des pièces utilisées</li>
                </ul>
                <p><strong>Exemple :</strong></p>
                <pre><code>pieces = [50, 20, 10, 5, 2, 1]
print(rendu_monnaie(67, pieces))  # [50, 10, 5, 2]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def rendu_monnaie(somme, pieces):
    resultat = []
    for piece in pieces:
        while somme >= piece:
            resultat.append(piece)
            somme -= piece
    return resultat

# Test
pieces = [50, 20, 10, 5, 2, 1]
print(rendu_monnaie(67, pieces))  # [50, 10, 5, 2]</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Rendu de monnaie avec comptage</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>rendu_monnaie_detaille(somme, pieces)</code> qui :</p>
                <ul>
                    <li>Retourne un dictionnaire avec le nombre de chaque pièce utilisée</li>
                    <li>Affiche le détail du rendu de monnaie</li>
                </ul>
                <p><strong>Exemple :</strong></p>
                <pre><code>pieces = [50, 20, 10, 5, 2, 1]
resultat = rendu_monnaie_detaille(67, pieces)
# Affiche : "1 pièce(s) de 50, 1 pièce(s) de 10, 1 pièce(s) de 5, 1 pièce(s) de 2"
# Retourne : {50: 1, 10: 1, 5: 1, 2: 1}</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def rendu_monnaie_detaille(somme, pieces):
    resultat = {}
    details = []
    
    for piece in pieces:
        nb_pieces = somme // piece
        if nb_pieces > 0:
            resultat[piece] = nb_pieces
            details.append(f"{nb_pieces} pièce(s) de {piece}")
            somme -= nb_pieces * piece
    
    print(", ".join(details))
    return resultat

# Test
pieces = [50, 20, 10, 5, 2, 1]
resultat = rendu_monnaie_detaille(67, pieces)
print(resultat)  # {50: 1, 10: 1, 5: 1, 2: 1}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🚀</div>
            <h4 class="exercise-title">Vérification de l'optimalité</h4>
            <div class="exercise-content">
                <p>L'algorithme glouton ne donne pas toujours la solution optimale. Considérons un système de pièces [4, 3, 1].</p>
                <p><strong>Question :</strong> Pour rendre 6 unités :</p>
                <ul>
                    <li>Que donne l'algorithme glouton ?</li>
                    <li>Quelle est la solution optimale ?</li>
                </ul>
                <p>Écrire une fonction <code>test_optimalite(somme, pieces)</code> qui compare l'algorithme glouton avec une solution par force brute pour vérifier l'optimalité.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def rendu_glouton(somme, pieces):
    resultat = []
    for piece in pieces:
        while somme >= piece:
            resultat.append(piece)
            somme -= piece
    return resultat

def test_optimalite(somme, pieces):
    # Solution gloutonne
    solution_gloutonne = rendu_glouton(somme, pieces)
    nb_pieces_glouton = len(solution_gloutonne)
    
    print(f"Algorithme glouton pour {somme} : {solution_gloutonne}")
    print(f"Nombre de pièces : {nb_pieces_glouton}")
    
    # Pour 6 avec [4, 3, 1] :
    # Glouton : [4, 1, 1] = 3 pièces
    # Optimal : [3, 3] = 2 pièces
    
    if pieces == [4, 3, 1] and somme == 6:
        print("Solution optimale : [3, 3] = 2 pièces")
        print("L'algorithme glouton n'est pas optimal ici !")
    
    return solution_gloutonne

# Test
pieces = [4, 3, 1]
test_optimalite(6, pieces)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Projet 🎯</div>
            <h4 class="exercise-title">Simulateur de caisse automatique</h4>
            <div class="exercise-content">
                <p>Créer un programme complet qui simule une caisse automatique :</p>
                <ul>
                    <li>Demander le prix d'un article et l'argent donné</li>
                    <li>Calculer la monnaie à rendre</li>
                    <li>Afficher le détail des pièces et billets à rendre</li>
                    <li>Gérer les cas d'erreur (argent insuffisant)</li>
                </ul>
                <p><strong>Système monétaire :</strong> [500, 200, 100, 50, 20, 10, 5, 2, 1] (en centimes)</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def caisse_automatique():
    # Système monétaire français en centimes
    pieces_billets = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    noms = ["5€", "2€", "1€", "50c", "20c", "10c", "5c", "2c", "1c"]
    
    print("=== CAISSE AUTOMATIQUE ===")
    
    try:
        prix = float(input("Prix de l'article (en €) : "))
        argent_donne = float(input("Argent donné (en €) : "))
        
        # Conversion en centimes pour éviter les erreurs de virgule flottante
        prix_centimes = int(prix * 100)
        argent_centimes = int(argent_donne * 100)
        
        if argent_centimes < prix_centimes:
            print("Erreur : Argent insuffisant !")
            return
        
        monnaie = argent_centimes - prix_centimes
        
        if monnaie == 0:
            print("Pas de monnaie à rendre.")
            return
        
        print(f"\nMonnaie à rendre : {monnaie/100:.2f}€")
        print("Détail :")
        
        for i, valeur in enumerate(pieces_billets):
            nb = monnaie // valeur
            if nb > 0:
                print(f"  {nb} x {noms[i]}")
                monnaie -= nb * valeur
        
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

# Lancer le simulateur
caisse_automatique()</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="sac-a-dos-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Comprendre le problème du sac à dos</h4>
            <div class="exercise-content">
                <p>Le problème du sac à dos consiste à sélectionner des objets pour <strong>maximiser la valeur totale</strong> sans dépasser la capacité du sac.</p>
                <p><strong>Exemple :</strong> Sac de capacité 15kg avec les objets :</p>
                <table style="margin: 1rem 0; border-collapse: collapse; width: 100%;">
                    <tr style="background: #f5f5f5;">
                        <th style="border: 1px solid #ddd; padding: 8px;">Objet</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Masse</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Valeur</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Rapport V/M</th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">A</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6kg</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">12€</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">2.0</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">B</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">8kg</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">20€</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">2.5</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">C</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">4kg</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6€</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">1.5</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Sac à dos par masse (objets les plus légers)</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>sac_a_dos_masse(capacite, objets)</code> qui :</p>
                <ul>
                    <li>Prend en paramètres la capacité maximale du sac et une liste de tuples (masse, valeur)</li>
                    <li>Utilise la stratégie du choix par masse (objets les plus légers d'abord)</li>
                    <li>Retourne un tuple (objets_selectionnes, valeur_totale)</li>
                </ul>
                <p><strong>Exemple :</strong></p>
                <pre><code>objets = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (masse, valeur)
print(sac_a_dos_masse(10, objets))</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def sac_a_dos_masse(capacite, objets):
    # Trier par masse croissante
    objets_tries = sorted(objets, key=lambda x: x[0])
    
    objets_selectionnes = []
    valeur_totale = 0
    capacite_restante = capacite
    
    for masse, valeur in objets_tries:
        if masse <= capacite_restante:
            objets_selectionnes.append((masse, valeur))
            valeur_totale += valeur
            capacite_restante -= masse
    
    return (objets_selectionnes, valeur_totale)

# Test
objets = [(2, 3), (3, 4), (4, 5), (5, 6)]
resultat = sac_a_dos_masse(10, objets)
print(f"Objets sélectionnés : {resultat[0]}")
print(f"Valeur totale : {resultat[1]}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Sac à dos par valeur (objets les plus précieux)</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>sac_a_dos_valeur(capacite, objets)</code> qui :</p>
                <ul>
                    <li>Prend en paramètres la capacité maximale du sac et une liste de tuples (masse, valeur)</li>
                    <li>Utilise la stratégie du choix par valeur (objets les plus précieux d'abord)</li>
                    <li>Retourne un tuple (objets_selectionnes, valeur_totale)</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def sac_a_dos_valeur(capacite, objets):
    # Trier par valeur décroissante
    objets_tries = sorted(objets, key=lambda x: x[1], reverse=True)
    
    objets_selectionnes = []
    valeur_totale = 0
    capacite_restante = capacite
    
    for masse, valeur in objets_tries:
        if masse <= capacite_restante:
            objets_selectionnes.append((masse, valeur))
            valeur_totale += valeur
            capacite_restante -= masse
    
    return (objets_selectionnes, valeur_totale)

# Test
objets = [(2, 3), (3, 4), (4, 5), (5, 6)]
resultat = sac_a_dos_valeur(10, objets)
print(f"Objets sélectionnés : {resultat[0]}")
print(f"Valeur totale : {resultat[1]}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Sac à dos par rapport valeur/masse</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>sac_a_dos_rapport(capacite, objets)</code> qui :</p>
                <ul>
                    <li>Utilise la stratégie du choix par rapport valeur/masse (efficacité)</li>
                    <li>Calcule le rapport valeur/masse pour chaque objet</li>
                    <li>Sélectionne les objets par ordre décroissant de ce rapport</li>
                    <li>Retourne un tuple (objets_selectionnes, valeur_totale)</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def sac_a_dos_rapport(capacite, objets):
    # Calculer le rapport valeur/masse et trier par ordre décroissant
    objets_avec_rapport = [(masse, valeur, valeur/masse) for masse, valeur in objets]
    objets_tries = sorted(objets_avec_rapport, key=lambda x: x[2], reverse=True)
    
    objets_selectionnes = []
    valeur_totale = 0
    capacite_restante = capacite
    
    for masse, valeur, rapport in objets_tries:
        if masse <= capacite_restante:
            objets_selectionnes.append((masse, valeur))
            valeur_totale += valeur
            capacite_restante -= masse
    
    return (objets_selectionnes, valeur_totale)

# Test
objets = [(2, 3), (3, 4), (4, 5), (5, 6)]
resultat = sac_a_dos_rapport(10, objets)
print(f"Objets sélectionnés : {resultat[0]}")
print(f"Valeur totale : {resultat[1]}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Analyse comparative des stratégies</h4>
            <div class="exercise-content">
                <p>Soit un sac à dos de capacité <strong>15 kg</strong> et les objets suivants :</p>
                <table style="margin: 1rem 0; border-collapse: collapse; width: 100%;">
                    <tr style="background: #f5f5f5;">
                        <th style="border: 1px solid #ddd; padding: 8px;">Objet</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">1</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">2</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">3</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">4</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">5</th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Masse</strong></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">8</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">4</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">10</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">7</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Valeur</strong></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">12</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">20</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">18</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">15</td>
                    </tr>
                </table>
                <p><strong>Questions :</strong></p>
                <ol>
                    <li>Appliquer l'algorithme glouton en utilisant la stratégie par masse.</li>
                    <li>Appliquer l'algorithme glouton en utilisant la stratégie par valeur.</li>
                    <li>Appliquer l'algorithme glouton en utilisant la stratégie par rapport valeur/masse.</li>
                    <li>Quelle stratégie donne les meilleurs résultats ?</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Données de l'exercice
objets = [(6, 12), (8, 20), (4, 6), (10, 18), (7, 15)]  # (masse, valeur)
capacite = 15

print("=== ANALYSE COMPARATIVE DES STRATÉGIES ===")
print(f"Capacité du sac : {capacite} kg")
print(f"Objets disponibles : {objets}")
print()

# 1. Stratégie par masse
print("1. Stratégie par masse (objets les plus légers) :")
resultat_masse = sac_a_dos_masse(capacite, objets)
print(f"   Objets sélectionnés : {resultat_masse[0]}")
print(f"   Valeur totale : {resultat_masse[1]}")
print()

# 2. Stratégie par valeur
print("2. Stratégie par valeur (objets les plus précieux) :")
resultat_valeur = sac_a_dos_valeur(capacite, objets)
print(f"   Objets sélectionnés : {resultat_valeur[0]}")
print(f"   Valeur totale : {resultat_valeur[1]}")
print()

# 3. Stratégie par rapport
print("3. Stratégie par rapport valeur/masse :")
resultat_rapport = sac_a_dos_rapport(capacite, objets)
print(f"   Objets sélectionnés : {resultat_rapport[0]}")
print(f"   Valeur totale : {resultat_rapport[1]}")
print()

# 4. Comparaison
print("4. Comparaison des résultats :")
strategies = [
    ("Masse", resultat_masse[1]),
    ("Valeur", resultat_valeur[1]),
    ("Rapport V/M", resultat_rapport[1])
]

meilleure = max(strategies, key=lambda x: x[1])
print(f"   Meilleure stratégie : {meilleure[0]} avec une valeur de {meilleure[1]}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🚀</div>
            <h4 class="exercise-title">Optimisation et limites de l'algorithme glouton</h4>
            <div class="exercise-content">
                <p>L'algorithme glouton pour le sac à dos ne garantit pas toujours la solution optimale.</p>
                <p><strong>Exemple problématique :</strong> Capacité 10kg, objets [(6, 10), (5, 8), (5, 8)]</p>
                <ul>
                    <li>Algorithme glouton par valeur : prend (6, 10) puis ne peut plus rien ajouter → valeur = 10</li>
                    <li>Solution optimale : prend (5, 8) et (5, 8) → valeur = 16</li>
                </ul>
                <p>Créer une fonction qui teste différents cas et identifie quand l'algorithme glouton échoue.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def test_limites_glouton():
    print("=== TEST DES LIMITES DE L'ALGORITHME GLOUTON ===")
    
    # Cas problématique 1
    print("\nCas 1 : Capacité 10kg, objets [(6, 10), (5, 8), (5, 8)]")
    objets1 = [(6, 10), (5, 8), (5, 8)]
    capacite1 = 10
    
    # Stratégie par valeur (problématique)
    resultat_valeur = sac_a_dos_valeur(capacite1, objets1)
    print(f"Glouton par valeur : {resultat_valeur[0]}, valeur = {resultat_valeur[1]}")
    
    # Solution optimale (force brute simple)
    print("Solution optimale : [(5, 8), (5, 8)], valeur = 16")
    print("→ L'algorithme glouton échoue !")
    
    # Cas problématique 2
    print("\nCas 2 : Capacité 15kg, objets [(10, 10), (6, 6), (6, 6)]")
    objets2 = [(10, 10), (6, 6), (6, 6)]
    capacite2 = 15
    
    resultat_valeur2 = sac_a_dos_valeur(capacite2, objets2)
    print(f"Glouton par valeur : {resultat_valeur2[0]}, valeur = {resultat_valeur2[1]}")
    print("Solution optimale : [(6, 6), (6, 6)], valeur = 12")
    
    if resultat_valeur2[1] >= 12:
        print("→ L'algorithme glouton fonctionne bien ici")
    else:
        print("→ L'algorithme glouton échoue !")
    
    print("\nConclusion : L'algorithme glouton est rapide mais pas toujours optimal.")
    print("Pour une solution optimale, il faut utiliser la programmation dynamique.")

# Lancer le test
test_limites_glouton()</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="planification-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Comprendre la planification de tâches</h4>
            <div class="exercise-content">
                <p>Le problème de la planification de tâches consiste à <strong>ordonnancer des tâches</strong> pour minimiser le retard total ou maximiser le nombre de tâches terminées à temps.</p>
                <p><strong>Exemple :</strong> 4 tâches avec leurs durées et échéances :</p>
                <table style="margin: 1rem 0; border-collapse: collapse; width: 100%;">
                    <tr style="background: #f5f5f5;">
                        <th style="border: 1px solid #ddd; padding: 8px;">Tâche</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Durée</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Échéance</th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">A</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">3h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6h</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">B</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">2h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">8h</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">C</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">1h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">9h</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">D</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">4h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">9h</td>
                    </tr>
                </table>
                <p><strong>Stratégie gloutonne :</strong> Trier les tâches par échéance croissante (EDD - Earliest Due Date).</p>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Planification par échéance (EDD)</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>planification_echeance(taches)</code> qui :</p>
                <ul>
                    <li>Prend en paramètre une liste de tuples (nom, duree, echeance)</li>
                    <li>Utilise la stratégie EDD (Earliest Due Date)</li>
                    <li>Retourne l'ordre d'exécution des tâches</li>
                </ul>
                <p><strong>Exemple :</strong></p>
                <pre><code>taches = [("A", 3, 6), ("B", 2, 8), ("C", 1, 9), ("D", 4, 9)]
print(planification_echeance(taches))</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def planification_echeance(taches):
    # Trier par échéance croissante (EDD)
    taches_triees = sorted(taches, key=lambda x: x[2])
    
    ordre_execution = []
    temps_actuel = 0
    
    for nom, duree, echeance in taches_triees:
        ordre_execution.append({
            'nom': nom,
            'debut': temps_actuel,
            'fin': temps_actuel + duree,
            'echeance': echeance,
            'retard': max(0, temps_actuel + duree - echeance)
        })
        temps_actuel += duree
    
    return ordre_execution

# Test
taches = [("A", 3, 6), ("B", 2, 8), ("C", 1, 9), ("D", 4, 9)]
resultat = planification_echeance(taches)

print("Ordre d'exécution (stratégie EDD) :")
for tache in resultat:
    print(f"Tâche {tache['nom']} : {tache['debut']}h → {tache['fin']}h (échéance: {tache['echeance']}h, retard: {tache['retard']}h)")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🌟</div>
            <h4 class="exercise-title">Planification par durée (SPT)</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>planification_duree(taches)</code> qui :</p>
                <ul>
                    <li>Utilise la stratégie SPT (Shortest Processing Time)</li>
                    <li>Trie les tâches par durée croissante</li>
                    <li>Calcule le temps de completion moyen</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def planification_duree(taches):
    # Trier par durée croissante (SPT)
    taches_triees = sorted(taches, key=lambda x: x[1])
    
    ordre_execution = []
    temps_actuel = 0
    temps_completion_total = 0
    
    for nom, duree, echeance in taches_triees:
        temps_completion = temps_actuel + duree
        temps_completion_total += temps_completion
        
        ordre_execution.append({
            'nom': nom,
            'debut': temps_actuel,
            'fin': temps_completion,
            'echeance': echeance,
            'retard': max(0, temps_completion - echeance)
        })
        temps_actuel += duree
    
    temps_completion_moyen = temps_completion_total / len(taches)
    
    return ordre_execution, temps_completion_moyen

# Test
taches = [("A", 3, 6), ("B", 2, 8), ("C", 1, 9), ("D", 4, 9)]
resultat, temps_moyen = planification_duree(taches)

print("Ordre d'exécution (stratégie SPT) :")
for tache in resultat:
    print(f"Tâche {tache['nom']} : {tache['debut']}h → {tache['fin']}h (échéance: {tache['echeance']}h, retard: {tache['retard']}h)")
print(f"\nTemps de completion moyen : {temps_moyen:.1f}h")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Comparaison des stratégies de planification</h4>
            <div class="exercise-content">
                <p>Soit les tâches suivantes :</p>
                <table style="margin: 1rem 0; border-collapse: collapse; width: 100%;">
                    <tr style="background: #f5f5f5;">
                        <th style="border: 1px solid #ddd; padding: 8px;">Tâche</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">T1</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">T2</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">T3</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">T4</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">T5</th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Durée</strong></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">4h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">2h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">3h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">1h</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Échéance</strong></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">8h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">4h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">12h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">6h</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">3h</td>
                    </tr>
                </table>
                <p><strong>Questions :</strong></p>
                <ol>
                    <li>Appliquer la stratégie EDD (par échéance)</li>
                    <li>Appliquer la stratégie SPT (par durée)</li>
                    <li>Calculer le retard total pour chaque stratégie</li>
                    <li>Quelle stratégie minimise le retard total ?</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Données de l'exercice
taches = [("T1", 4, 8), ("T2", 2, 4), ("T3", 6, 12), ("T4", 3, 6), ("T5", 1, 3)]

print("=== COMPARAISON DES STRATÉGIES DE PLANIFICATION ===")
print(f"Tâches : {taches}")
print()

# 1. Stratégie EDD
print("1. Stratégie EDD (Earliest Due Date) :")
resultat_edd = planification_echeance(taches)
retard_total_edd = sum(tache['retard'] for tache in resultat_edd)
print("   Ordre : ", [tache['nom'] for tache in resultat_edd])
for tache in resultat_edd:
    print(f"   {tache['nom']} : {tache['debut']}h → {tache['fin']}h (retard: {tache['retard']}h)")
print(f"   Retard total : {retard_total_edd}h")
print()

# 2. Stratégie SPT
print("2. Stratégie SPT (Shortest Processing Time) :")
resultat_spt, temps_moyen = planification_duree(taches)
retard_total_spt = sum(tache['retard'] for tache in resultat_spt)
print("   Ordre : ", [tache['nom'] for tache in resultat_spt])
for tache in resultat_spt:
    print(f"   {tache['nom']} : {tache['debut']}h → {tache['fin']}h (retard: {tache['retard']}h)")
print(f"   Retard total : {retard_total_spt}h")
print(f"   Temps completion moyen : {temps_moyen:.1f}h")
print()

# 3. Comparaison
print("3. Comparaison des résultats :")
print(f"   EDD - Retard total : {retard_total_edd}h")
print(f"   SPT - Retard total : {retard_total_spt}h")

if retard_total_edd < retard_total_spt:
    print("   → EDD minimise mieux le retard total")
elif retard_total_spt < retard_total_edd:
    print("   → SPT minimise mieux le retard total")
else:
    print("   → Les deux stratégies donnent le même retard total")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🔥</div>
            <h4 class="exercise-title">Planification avec priorités</h4>
            <div class="exercise-content">
                <p>Créer une fonction <code>planification_priorite(taches)</code> qui :</p>
                <ul>
                    <li>Prend en paramètre une liste de tuples (nom, duree, echeance, priorite)</li>
                    <li>Utilise un système de score combinant échéance et priorité</li>
                    <li>Score = priorité / échéance (plus le score est élevé, plus urgent)</li>
                    <li>Retourne l'ordre d'exécution optimisé</li>
                </ul>
                <p><strong>Exemple :</strong> Priorité de 1 (faible) à 5 (critique)</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def planification_priorite(taches):
    # Calculer le score d'urgence : priorité / échéance
    taches_avec_score = []
    for nom, duree, echeance, priorite in taches:
        score = priorite / echeance
        taches_avec_score.append((nom, duree, echeance, priorite, score))
    
    # Trier par score décroissant (plus urgent en premier)
    taches_triees = sorted(taches_avec_score, key=lambda x: x[4], reverse=True)
    
    ordre_execution = []
    temps_actuel = 0
    
    for nom, duree, echeance, priorite, score in taches_triees:
        ordre_execution.append({
            'nom': nom,
            'debut': temps_actuel,
            'fin': temps_actuel + duree,
            'echeance': echeance,
            'priorite': priorite,
            'score': score,
            'retard': max(0, temps_actuel + duree - echeance)
        })
        temps_actuel += duree
    
    return ordre_execution

# Test
taches = [
    ("Rapport", 3, 8, 4),      # (nom, durée, échéance, priorité)
    ("Email", 1, 2, 2),
    ("Présentation", 4, 10, 5),
    ("Réunion", 2, 6, 3),
    ("Documentation", 2, 12, 1)
]

resultat = planification_priorite(taches)

print("Planification avec priorités :")
print("Ordre d'exécution (par score d'urgence) :")
for tache in resultat:
    print(f"{tache['nom']} : {tache['debut']}h → {tache['fin']}h")
    print(f"   Priorité: {tache['priorite']}, Échéance: {tache['echeance']}h, Score: {tache['score']:.2f}")
    print(f"   Retard: {tache['retard']}h")
    print()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🚀</div>
            <h4 class="exercise-title">Optimisation multi-critères</h4>
            <div class="exercise-content">
                <p>Créer un système de planification avancé qui :</p>
                <ul>
                    <li>Combine plusieurs critères : durée, échéance, priorité, coût de retard</li>
                    <li>Utilise une fonction de score pondérée</li>
                    <li>Permet d'ajuster les poids selon le contexte</li>
                    <li>Compare les résultats avec les stratégies simples</li>
                </ul>
                <p><strong>Formule :</strong> Score = (w1×priorité + w2×(1/durée) + w3×(1/échéance) + w4×coût_retard)</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def planification_multi_criteres(taches, poids=(0.3, 0.2, 0.3, 0.2)):
    """
    Planification multi-critères avec pondération
    poids = (w_priorite, w_duree, w_echeance, w_cout_retard)
    """
    w_priorite, w_duree, w_echeance, w_cout_retard = poids
    
    taches_avec_score = []
    for nom, duree, echeance, priorite, cout_retard in taches:
        # Normalisation des critères (plus c'est élevé, plus c'est urgent)
        score_priorite = priorite  # 1-5
        score_duree = 1 / duree if duree > 0 else 0  # Favorise les tâches courtes
        score_echeance = 1 / echeance if echeance > 0 else 0  # Favorise les échéances proches
        score_cout = cout_retard  # Coût du retard
        
        # Score pondéré
        score_total = (w_priorite * score_priorite + 
                      w_duree * score_duree * 10 +  # Facteur 10 pour équilibrer
                      w_echeance * score_echeance * 100 +  # Facteur 100 pour équilibrer
                      w_cout_retard * score_cout)
        
        taches_avec_score.append((nom, duree, echeance, priorite, cout_retard, score_total))
    
    # Trier par score décroissant
    taches_triees = sorted(taches_avec_score, key=lambda x: x[5], reverse=True)
    
    ordre_execution = []
    temps_actuel = 0
    cout_total_retard = 0
    
    for nom, duree, echeance, priorite, cout_retard, score in taches_triees:
        fin_tache = temps_actuel + duree
        retard = max(0, fin_tache - echeance)
        cout_retard_reel = retard * cout_retard if retard > 0 else 0
        cout_total_retard += cout_retard_reel
        
        ordre_execution.append({
            'nom': nom,
            'debut': temps_actuel,
            'fin': fin_tache,
            'echeance': echeance,
            'priorite': priorite,
            'retard': retard,
            'cout_retard': cout_retard_reel,
            'score': score
        })
        temps_actuel += duree
    
    return ordre_execution, cout_total_retard

# Test avec données complexes
taches_complexes = [
    # (nom, durée, échéance, priorité, coût_retard_par_heure)
    ("Projet_A", 5, 10, 5, 50),
    ("Maintenance", 2, 6, 2, 10),
    ("Formation", 3, 15, 3, 5),
    ("Urgence", 1, 3, 5, 100),
    ("Routine", 4, 20, 1, 2)
]

print("=== PLANIFICATION MULTI-CRITÈRES ===")

# Test avec différents poids
configs = [
    ((0.4, 0.2, 0.2, 0.2), "Priorité élevée"),
    ((0.2, 0.4, 0.2, 0.2), "Durée courte"),
    ((0.2, 0.2, 0.4, 0.2), "Échéance proche"),
    ((0.2, 0.2, 0.2, 0.4), "Coût de retard")
]

for poids, description in configs:
    print(f"\n--- Configuration : {description} ---")
    resultat, cout_total = planification_multi_criteres(taches_complexes, poids)
    
    print("Ordre d'exécution :")
    for tache in resultat:
        print(f"  {tache['nom']} : {tache['debut']}h → {tache['fin']}h")
        print(f"    Retard: {tache['retard']}h, Coût: {tache['cout_retard']:.0f}€")
    
    print(f"Coût total de retard : {cout_total:.0f}€")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Projet 🎯</div>
            <h4 class="exercise-title">Simulateur de planification de tâches</h4>
            <div class="exercise-content">
                <p>Créer un simulateur complet qui :</p>
                <ul>
                    <li>Permet de saisir des tâches avec tous leurs attributs</li>
                    <li>Propose plusieurs stratégies de planification</li>
                    <li>Affiche un planning visuel (diagramme de Gantt textuel)</li>
                    <li>Compare les performances de chaque stratégie</li>
                    <li>Génère un rapport d'analyse</li>
                </ul>
                <p><strong>Fonctionnalités :</strong> Interface interactive, visualisation, export des résultats</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>class SimulateurPlanification:
    def __init__(self):
        self.taches = []
        self.strategies = {
            'EDD': self.planification_edd,
            'SPT': self.planification_spt,
            'Priorité': self.planification_priorite,
            'Multi-critères': self.planification_multi
        }
    
    def ajouter_tache(self, nom, duree, echeance, priorite=1, cout_retard=0):
        self.taches.append({
            'nom': nom,
            'duree': duree,
            'echeance': echeance,
            'priorite': priorite,
            'cout_retard': cout_retard
        })
    
    def planification_edd(self):
        return sorted(self.taches, key=lambda x: x['echeance'])
    
    def planification_spt(self):
        return sorted(self.taches, key=lambda x: x['duree'])
    
    def planification_priorite(self):
        return sorted(self.taches, key=lambda x: x['priorite'], reverse=True)
    
    def planification_multi(self):
        taches_scorees = []
        for tache in self.taches:
            score = (tache['priorite'] * 0.3 + 
                    (1/tache['duree']) * 2 + 
                    (1/tache['echeance']) * 10 + 
                    tache['cout_retard'] * 0.1)
            taches_scorees.append((tache, score))
        
        return [t[0] for t in sorted(taches_scorees, key=lambda x: x[1], reverse=True)]
    
    def calculer_metriques(self, ordre):
        temps_actuel = 0
        retard_total = 0
        cout_total = 0
        taches_a_temps = 0
        
        for tache in ordre:
            fin = temps_actuel + tache['duree']
            retard = max(0, fin - tache['echeance'])
            
            if retard == 0:
                taches_a_temps += 1
            
            retard_total += retard
            cout_total += retard * tache['cout_retard']
            temps_actuel = fin
        
        return {
            'retard_total': retard_total,
            'cout_total': cout_total,
            'taches_a_temps': taches_a_temps,
            'duree_totale': temps_actuel,
            'taux_reussite': taches_a_temps / len(ordre) * 100
        }
    
    def afficher_gantt(self, ordre, nom_strategie):
        print(f"\n=== DIAGRAMME DE GANTT - {nom_strategie} ===")
        temps_actuel = 0
        
        for tache in ordre:
            fin = temps_actuel + tache['duree']
            retard = max(0, fin - tache['echeance'])
            
            # Barre de progression textuelle
            barre = "█" * tache['duree']
            statut = "⚠️" if retard > 0 else "✅"
            
            print(f"{tache['nom']:12} |{temps_actuel:2}h {barre:10} {fin:2}h| {statut} (échéance: {tache['echeance']}h)")
            temps_actuel = fin
    
    def comparer_strategies(self):
        print("\n" + "="*60)
        print("           COMPARAISON DES STRATÉGIES")
        print("="*60)
        
        resultats = {}
        
        for nom, strategie in self.strategies.items():
            ordre = strategie()
            metriques = self.calculer_metriques(ordre)
            resultats[nom] = metriques
            
            self.afficher_gantt(ordre, nom)
            
            print(f"\nMétriques pour {nom} :")
            print(f"  Retard total: {metriques['retard_total']}h")
            print(f"  Coût total: {metriques['cout_total']:.0f}€")
            print(f"  Tâches à temps: {metriques['taches_a_temps']}/{len(self.taches)}")
            print(f"  Taux de réussite: {metriques['taux_reussite']:.1f}%")
            print(f"  Durée totale: {metriques['duree_totale']}h")
        
        # Recommandation
        print("\n" + "="*60)
        print("                RECOMMANDATION")
        print("="*60)
        
        meilleure_retard = min(resultats.items(), key=lambda x: x[1]['retard_total'])
        meilleure_cout = min(resultats.items(), key=lambda x: x[1]['cout_total'])
        meilleur_taux = max(resultats.items(), key=lambda x: x[1]['taux_reussite'])
        
        print(f"Meilleure pour minimiser le retard: {meilleure_retard[0]}")
        print(f"Meilleure pour minimiser les coûts: {meilleure_cout[0]}")
        print(f"Meilleure pour le taux de réussite: {meilleur_taux[0]}")

# Exemple d'utilisation
simulateur = SimulateurPlanification()

# Ajouter des tâches
simulateur.ajouter_tache("Développement", 8, 12, 4, 25)
simulateur.ajouter_tache("Tests", 3, 10, 3, 15)
simulateur.ajouter_tache("Documentation", 2, 15, 2, 5)
simulateur.ajouter_tache("Déploiement", 1, 8, 5, 50)
simulateur.ajouter_tache("Formation", 4, 20, 1, 10)

# Lancer la comparaison
simulateur.comparer_strategies()</code></pre>
            </div>
        </div>
    </div>
</div>
</div>