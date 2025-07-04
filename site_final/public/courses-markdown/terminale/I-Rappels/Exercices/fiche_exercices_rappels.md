# Fiche d'exercices : Rappels de Première

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
    position: relative;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.close-solution {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--md-default-fg-color);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s ease;
}

.close-solution:hover {
    background-color: rgba(0, 0, 0, 0.1);
}

.toggle-solution {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

.toggle-solution:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
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

.exercise-card.expert {
    border-left-color: #9C27B0;
}

.exercise-card.expert:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(156, 39, 176, 0.4);
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

.difficulty-badge.expert {
    background: rgba(156, 39, 176, 0.1);
    color: #9C27B0;
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

// Gestion des onglets de sections
function showSection(sectionName) {
    // Masquer toutes les sections
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Désactiver tous les onglets
    const tabs = document.querySelectorAll('.section-tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Afficher la section sélectionnée
    const targetSection = document.getElementById(sectionName);
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Activer l'onglet correspondant
    const targetTab = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
    if (targetTab) {
        targetTab.classList.add('active');
    }
}

// Gestion des solutions
function toggleSolution(exerciseId) {
    const modal = document.getElementById('solution-modal');
    const content = document.getElementById('solution-content');
    const solutionText = document.getElementById(`solution-${exerciseId}`);
    
    if (solutionText) {
        content.innerHTML = `
            <button class="close-solution" onclick="closeSolutionModal()">&times;</button>
            ${solutionText.innerHTML}
        `;
        modal.classList.add('show');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solution-modal');
    modal.classList.remove('show');
}

// Fermer la modal avec Échap
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeSolutionModal();
    }
});

// Initialiser la première section
document.addEventListener('DOMContentLoaded', function() {
    showSection('variables');
});
</script>

<!-- Modal pour afficher les solutions -->
<div id="solution-modal" class="solution-modal">
    <div id="solution-content" class="solution-content">
        <!-- Le contenu sera injecté ici -->
    </div>
</div>

## Navigation par thèmes

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('variables')">Variables et Types</button>
    <button class="section-tab" onclick="showSection('conditions')">Conditions et Boucles</button>
    <button class="section-tab" onclick="showSection('fonctions')">Fonctions</button>
    <button class="section-tab" onclick="showSection('listes')">Listes et Tableaux</button>
    <button class="section-tab" onclick="showSection('projets')">Projets Intégrés</button>
</div>

<!-- Section Variables et Types -->
<div id="variables" class="section-content">
    <div class="exercise-cards">
        
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge intro">Introduction</span>
                <h3 class="exercise-title">Exercice 1 : Calculatrice personnelle</h3>
                <div class="exercise-content">
                    <p>Créez un programme qui :</p>
                    <ul>
                        <li>Demande le nom de l'utilisateur</li>
                        <li>Demande deux nombres</li>
                        <li>Effectue les quatre opérations de base</li>
                        <li>Affiche les résultats avec un message personnalisé</li>
                    </ul>
                    <p><strong>Exemple :</strong> "Bonjour Alice ! 5 + 3 = 8"</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('calc')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Exercice 2 : Convertisseur d'unités</h3>
                <div class="exercise-content">
                    <p>Écrivez un programme qui convertit :</p>
                    <ul>
                        <li>Des mètres en pieds et pouces</li>
                        <li>Des kilogrammes en livres</li>
                        <li>Des degrés Celsius en Fahrenheit</li>
                    </ul>
                    <p>Le programme doit demander le type de conversion et la valeur à convertir.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('convert')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Moyen</span>
                <h3 class="exercise-title">Exercice 3 : Validateur de données</h3>
                <div class="exercise-content">
                    <p>Créez un programme qui valide :</p>
                    <ul>
                        <li>Un âge (entre 0 et 120)</li>
                        <li>Un email (contient @ et .)</li>
                        <li>Un mot de passe (au moins 8 caractères)</li>
                        <li>Un numéro de téléphone (10 chiffres)</li>
                    </ul>
                    <p>Utilisez des variables booléennes pour stocker les résultats de validation.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('valid')">Voir la solution</button>
            </div>
        </div>

    </div>
</div>

<!-- Section Conditions et Boucles -->
<div id="conditions" class="section-content">
    <div class="exercise-cards">
        
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge intro">Introduction</span>
                <h3 class="exercise-title">Exercice 4 : Système de notes</h3>
                <div class="exercise-content">
                    <p>Créez un programme qui :</p>
                    <ul>
                        <li>Demande une note sur 20</li>
                        <li>Affiche la mention correspondante</li>
                        <li>Indique si l'élève est admis (≥ 10)</li>
                        <li>Propose de saisir une nouvelle note</li>
                    </ul>
                    <p><strong>Mentions :</strong> Très bien (≥16), Bien (≥14), Assez bien (≥12), Passable (≥10)</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('notes')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Exercice 5 : Tables de multiplication</h3>
                <div class="exercise-content">
                    <p>Écrivez un programme qui :</p>
                    <ul>
                        <li>Demande un nombre à l'utilisateur</li>
                        <li>Affiche sa table de multiplication (1 à 10)</li>
                        <li>Utilise une boucle for</li>
                        <li>Formate joliment l'affichage</li>
                    </ul>
                    <p><strong>Bonus :</strong> Permettre de choisir la limite (au lieu de 10)</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('tables')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Moyen</span>
                <h3 class="exercise-title">Exercice 6 : Jeu de devinette amélioré</h3>
                <div class="exercise-content">
                    <p>Créez un jeu qui :</p>
                    <ul>
                        <li>Génère un nombre aléatoire entre 1 et 100</li>
                        <li>Donne des indices (trop grand/petit)</li>
                        <li>Compte le nombre d'essais</li>
                        <li>Propose différents niveaux de difficulté</li>
                        <li>Permet de rejouer</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('guess')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge hard">Difficile</span>
                <h3 class="exercise-title">Exercice 7 : Motifs géométriques</h3>
                <div class="exercise-content">
                    <p>Créez des programmes qui dessinent :</p>
                    <ul>
                        <li>Un triangle d'étoiles de taille variable</li>
                        <li>Un carré creux avec des bordures</li>
                        <li>Un losange centré</li>
                        <li>Une pyramide inversée</li>
                    </ul>
                    <p>La taille doit être paramétrable par l'utilisateur.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('patterns')">Voir la solution</button>
            </div>
        </div>

    </div>
</div>

<!-- Section Fonctions -->
<div id="fonctions" class="section-content">
    <div class="exercise-cards">
        
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge intro">Introduction</span>
                <h3 class="exercise-title">Exercice 8 : Bibliothèque mathématique</h3>
                <div class="exercise-content">
                    <p>Créez des fonctions pour :</p>
                    <ul>
                        <li><code>aire_cercle(rayon)</code> : calcule l'aire d'un cercle</li>
                        <li><code>perimetre_rectangle(longueur, largeur)</code></li>
                        <li><code>moyenne(a, b, c)</code> : moyenne de trois nombres</li>
                        <li><code>est_pair(nombre)</code> : retourne True si pair</li>
                    </ul>
                    <p>Testez chaque fonction avec plusieurs exemples.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('math')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Exercice 9 : Générateur de mots de passe</h3>
                <div class="exercise-content">
                    <p>Créez une fonction qui génère un mot de passe :</p>
                    <ul>
                        <li>Longueur paramétrable</li>
                        <li>Inclut lettres, chiffres et symboles</li>
                        <li>Option pour exclure les caractères ambigus</li>
                        <li>Fonction de validation de la force</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('password')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Moyen</span>
                <h3 class="exercise-title">Exercice 10 : Calculatrice scientifique</h3>
                <div class="exercise-content">
                    <p>Développez un programme avec des fonctions pour :</p>
                    <ul>
                        <li>Opérations de base (+, -, *, /)</li>
                        <li>Puissance et racine carrée</li>
                        <li>Fonctions trigonométriques</li>
                        <li>Menu interactif</li>
                        <li>Historique des calculs</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('calculator')">Voir la solution</button>
            </div>
        </div>

    </div>
</div>

<!-- Section Listes et Tableaux -->
<div id="listes" class="section-content">
    <div class="exercise-cards">
        
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge intro">Introduction</span>
                <h3 class="exercise-title">Exercice 11 : Gestionnaire de notes</h3>
                <div class="exercise-content">
                    <p>Créez un programme qui :</p>
                    <ul>
                        <li>Stocke les notes d'un élève dans une liste</li>
                        <li>Calcule la moyenne</li>
                        <li>Trouve la meilleure et la pire note</li>
                        <li>Compte les notes au-dessus de la moyenne</li>
                        <li>Permet d'ajouter/supprimer des notes</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('grades')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Exercice 12 : Tri et recherche</h3>
                <div class="exercise-content">
                    <p>Implémentez :</p>
                    <ul>
                        <li>Tri par sélection (sans utiliser sort())</li>
                        <li>Recherche linéaire</li>
                        <li>Suppression des doublons</li>
                        <li>Fusion de deux listes triées</li>
                    </ul>
                    <p>Testez avec des listes de nombres et de chaînes.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('search')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Moyen</span>
                <h3 class="exercise-title">Exercice 13 : Jeu du pendu</h3>
                <div class="exercise-content">
                    <p>Développez un jeu du pendu avec :</p>
                    <ul>
                        <li>Liste de mots prédéfinis</li>
                        <li>Affichage du mot avec des tirets</li>
                        <li>Gestion des lettres déjà proposées</li>
                        <li>Compteur d'erreurs avec limite</li>
                        <li>Interface utilisateur claire</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('hangman')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge hard">Difficile</span>
                <h3 class="exercise-title">Exercice 14 : Matrices et opérations</h3>
                <div class="exercise-content">
                    <p>Travaillez avec des matrices (listes de listes) :</p>
                    <ul>
                        <li>Addition et soustraction de matrices</li>
                        <li>Multiplication par un scalaire</li>
                        <li>Transposition</li>
                        <li>Vérification de symétrie</li>
                        <li>Calcul du déterminant (2x2)</li>
                    </ul>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('matrix')">Voir la solution</button>
            </div>
        </div>

    </div>
</div>

<!-- Section Projets Intégrés -->
<div id="projets" class="section-content">
    <div class="exercise-cards">
        
        <div class="exercise-card important">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge expert">Projet</span>
                <h3 class="exercise-title">Projet 1 : Carnet d'adresses</h3>
                <div class="exercise-content">
                    <p>Développez un carnet d'adresses complet :</p>
                    <ul>
                        <li>Ajouter/modifier/supprimer des contacts</li>
                        <li>Recherche par nom ou téléphone</li>
                        <li>Tri alphabétique</li>
                        <li>Sauvegarde dans un fichier texte</li>
                        <li>Interface menu avec options</li>
                    </ul>
                    <p><strong>Compétences :</strong> Listes, fonctions, fichiers, validation</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('contacts')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card important">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge expert">Projet</span>
                <h3 class="exercise-title">Projet 2 : Jeu de bataille navale</h3>
                <div class="exercise-content">
                    <p>Créez une bataille navale simplifiée :</p>
                    <ul>
                        <li>Grille 10x10 avec coordonnées</li>
                        <li>Placement aléatoire des navires</li>
                        <li>Système de tir avec feedback</li>
                        <li>Compteur de coups et de navires coulés</li>
                        <li>Affichage de la grille mise à jour</li>
                    </ul>
                    <p><strong>Compétences :</strong> Matrices, boucles, conditions, fonctions</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('battleship')">Voir la solution</button>
            </div>
        </div>

        <div class="exercise-card important">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge expert">Projet</span>
                <h3 class="exercise-title">Projet 3 : Gestionnaire de bibliothèque</h3>
                <div class="exercise-content">
                    <p>Système de gestion pour une petite bibliothèque :</p>
                    <ul>
                        <li>Base de données de livres (titre, auteur, ISBN)</li>
                        <li>Système d'emprunt et de retour</li>
                        <li>Recherche multicritères</li>
                        <li>Statistiques (livres les plus empruntés)</li>
                        <li>Gestion des retards</li>
                    </ul>
                    <p><strong>Compétences :</strong> Structures de données, algorithmes, validation</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution('library')">Voir la solution</button>
            </div>
        </div>

    </div>
</div>

<!-- Solutions cachées -->
<div class="exercise-script">
    <div id="solution-calc">
        <h3>Solution : Calculatrice personnelle</h3>
        <pre><code>nom = input("Quel est votre nom ? ")
nombre1 = float(input("Premier nombre : "))
nombre2 = float(input("Deuxième nombre : "))

addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2
division = nombre1 / nombre2 if nombre2 != 0 else "Division par zéro!"

print(f"Bonjour {nom} !")
print(f"{nombre1} + {nombre2} = {addition}")
print(f"{nombre1} - {nombre2} = {soustraction}")
print(f"{nombre1} × {nombre2} = {multiplication}")
print(f"{nombre1} ÷ {nombre2} = {division}")</code></pre>
    </div>
    
    <div id="solution-notes">
        <h3>Solution : Système de notes</h3>
        <pre><code>while True:
    note = float(input("Entrez une note sur 20 : "))
    
    if note >= 16:
        mention = "Très bien"
    elif note >= 14:
        mention = "Bien"
    elif note >= 12:
        mention = "Assez bien"
    elif note >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"
    
    if note >= 10:
        resultat = "Admis"
    else:
        resultat = "Refusé"
    
    print(f"Note : {note}/20")
    print(f"Mention : {mention}")
    print(f"Résultat : {resultat}")
    
    continuer = input("Nouvelle note ? (o/n) : ")
    if continuer.lower() != 'o':
        break</code></pre>
    </div>
    
    <div id="solution-math">
        <h3>Solution : Bibliothèque mathématique</h3>
        <pre><code>import math

def aire_cercle(rayon):
    return math.pi * rayon ** 2

def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

def moyenne(a, b, c):
    return (a + b + c) / 3

def est_pair(nombre):
    return nombre % 2 == 0

# Tests
print(f"Aire cercle (r=5) : {aire_cercle(5):.2f}")
print(f"Périmètre rectangle (3x4) : {perimetre_rectangle(3, 4)}")
print(f"Moyenne (10,15,20) : {moyenne(10, 15, 20)}")
print(f"8 est pair : {est_pair(8)}")
print(f"7 est pair : {est_pair(7)}")</code></pre>
    </div>
    
    <div id="solution-grades">
        <h3>Solution : Gestionnaire de notes</h3>
        <pre><code>notes = []

def ajouter_note():
    note = float(input("Nouvelle note : "))
    notes.append(note)
    print(f"Note {note} ajoutée.")

def supprimer_note():
    if notes:
        print(f"Notes actuelles : {notes}")
        index = int(input("Index à supprimer : "))
        if 0 <= index < len(notes):
            note_supprimee = notes.pop(index)
            print(f"Note {note_supprimee} supprimée.")
        else:
            print("Index invalide.")
    else:
        print("Aucune note à supprimer.")

def calculer_statistiques():
    if not notes:
        print("Aucune note enregistrée.")
        return
    
    moyenne = sum(notes) / len(notes)
    meilleure = max(notes)
    pire = min(notes)
    au_dessus_moyenne = len([n for n in notes if n > moyenne])
    
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure}")
    print(f"Pire note : {pire}")
    print(f"Notes au-dessus de la moyenne : {au_dessus_moyenne}")

# Menu principal
while True:
    print("\n1. Ajouter note")
    print("2. Supprimer note")
    print("3. Statistiques")
    print("4. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == '1':
        ajouter_note()
    elif choix == '2':
        supprimer_note()
    elif choix == '3':
        calculer_statistiques()
    elif choix == '4':
        break
    else:
        print("Choix invalide.")</code></pre>
    </div>
    
    <div id="solution-search">
        <h3>Solution : Tri et recherche</h3>
        <pre><code>def tri_selection(liste):
    """Tri par sélection"""
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

def recherche_lineaire(liste, element):
    """Recherche linéaire"""
    for i, valeur in enumerate(liste):
        if valeur == element:
            return i
    return -1

def supprimer_doublons(liste):
    """Supprime les doublons en gardant l'ordre"""
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat

def fusionner_listes_triees(liste1, liste2):
    """Fusionne deux listes triées"""
    resultat = []
    i, j = 0, 0
    
    while i < len(liste1) and j < len(liste2):
        if liste1[i] <= liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    
    # Ajouter les éléments restants
    resultat.extend(liste1[i:])
    resultat.extend(liste2[j:])
    
    return resultat

# Tests
nombres = [64, 34, 25, 12, 22, 11, 90]
print(f"Liste originale : {nombres}")
print(f"Liste triée : {tri_selection(nombres.copy())}")
print(f"Position de 25 : {recherche_lineaire(nombres, 25)}")

liste_doublons = [1, 2, 2, 3, 4, 4, 5]
print(f"Sans doublons : {supprimer_doublons(liste_doublons)}")

liste1 = [1, 3, 5, 7]
liste2 = [2, 4, 6, 8]
print(f"Fusion : {fusionner_listes_triees(liste1, liste2)}")</code></pre>
    </div>
    
    <div id="solution-hangman">
        <h3>Solution : Jeu du pendu</h3>
        <pre><code>import random

def jeu_pendu():
    mots = ["python", "programmation", "ordinateur", "algorithme", 
            "fonction", "variable", "boucle", "condition"]
    
    mot_secret = random.choice(mots).upper()
    lettres_trouvees = set()
    lettres_essayees = set()
    erreurs = 0
    max_erreurs = 6
    
    print("=== JEU DU PENDU ===")
    print(f"Le mot contient {len(mot_secret)} lettres.")
    
    while erreurs < max_erreurs:
        # Affichage du mot avec les lettres trouvées
        mot_affiche = ""
        for lettre in mot_secret:
            if lettre in lettres_trouvees:
                mot_affiche += lettre + " "
            else:
                mot_affiche += "_ "
        
        print(f"\nMot : {mot_affiche}")
        print(f"Lettres essayées : {', '.join(sorted(lettres_essayees))}")
        print(f"Erreurs : {erreurs}/{max_erreurs}")
        
        # Vérifier si le mot est trouvé
        if set(mot_secret) <= lettres_trouvees:
            print(f"\n🎉 Félicitations ! Vous avez trouvé le mot : {mot_secret}")
            break
        
        # Demander une lettre
        lettre = input("Proposez une lettre : ").upper()
        
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue
        
        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue
        
        lettres_essayees.add(lettre)
        
        if lettre in mot_secret:
            lettres_trouvees.add(lettre)
            print(f"✓ Bonne lettre !")
        else:
            erreurs += 1
            print(f"✗ Lettre incorrecte.")
    
    if erreurs >= max_erreurs:
        print(f"\n💀 Perdu ! Le mot était : {mot_secret}")
    
    rejouer = input("\nVoulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() == 'o':
        jeu_pendu()

# Lancer le jeu
jeu_pendu()</code></pre>
    </div>
    
    <div id="solution-matrix">
        <h3>Solution : Matrices et opérations</h3>
        <pre><code>def creer_matrice(lignes, colonnes, valeur=0):
    """Crée une matrice remplie d'une valeur"""
    return [[valeur for _ in range(colonnes)] for _ in range(lignes)]

def afficher_matrice(matrice):
    """Affiche une matrice de façon lisible"""
    for ligne in matrice:
        print(" ".join(f"{x:4}" for x in ligne))
    print()

def additionner_matrices(mat1, mat2):
    """Addition de deux matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    
    resultat = []
    for i in range(len(mat1)):
        ligne = []
        for j in range(len(mat1[0])):
            ligne.append(mat1[i][j] + mat2[i][j])
        resultat.append(ligne)
    return resultat

def multiplier_par_scalaire(matrice, scalaire):
    """Multiplication par un scalaire"""
    resultat = []
    for ligne in matrice:
        nouvelle_ligne = [element * scalaire for element in ligne]
        resultat.append(nouvelle_ligne)
    return resultat

def transposer(matrice):
    """Transposition d'une matrice"""
    lignes = len(matrice)
    colonnes = len(matrice[0])
    
    resultat = creer_matrice(colonnes, lignes)
    for i in range(lignes):
        for j in range(colonnes):
            resultat[j][i] = matrice[i][j]
    return resultat

def est_symetrique(matrice):
    """Vérifie si une matrice est symétrique"""
    if len(matrice) != len(matrice[0]):
        return False
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True

def determinant_2x2(matrice):
    """Calcule le déterminant d'une matrice 2x2"""
    if len(matrice) != 2 or len(matrice[0]) != 2:
        return None
    
    return matrice[0][0] * matrice[1][1] - matrice[0][1] * matrice[1][0]

# Tests
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]

print("Matrice 1 :")
afficher_matrice(mat1)

print("Matrice 2 :")
afficher_matrice(mat2)

print("Addition :")
afficher_matrice(additionner_matrices(mat1, mat2))

print("Multiplication par 3 :")
afficher_matrice(multiplier_par_scalaire(mat1, 3))

print("Transposée de mat1 :")
afficher_matrice(transposer(mat1))

print(f"mat1 est symétrique : {est_symetrique(mat1)}")
print(f"Déterminant de mat1 : {determinant_2x2(mat1)}")</code></pre>
    </div>
    
    <div id="solution-contacts">
        <h3>Solution : Carnet d'adresses</h3>
        <pre><code>import json
import os

class CarnetAdresses:
    def __init__(self, fichier="contacts.json"):
        self.fichier = fichier
        self.contacts = self.charger_contacts()
    
    def charger_contacts(self):
        """Charge les contacts depuis le fichier"""
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def sauvegarder_contacts(self):
        """Sauvegarde les contacts dans le fichier"""
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump(self.contacts, f, indent=2, ensure_ascii=False)
    
    def ajouter_contact(self):
        """Ajoute un nouveau contact"""
        nom = input("Nom : ").strip()
        if not nom:
            print("Le nom est obligatoire.")
            return
        
        telephone = input("Téléphone : ").strip()
        email = input("Email : ").strip()
        adresse = input("Adresse : ").strip()
        
        contact = {
            "nom": nom,
            "telephone": telephone,
            "email": email,
            "adresse": adresse
        }
        
        self.contacts.append(contact)
        self.sauvegarder_contacts()
        print(f"Contact {nom} ajouté avec succès.")
    
    def afficher_contacts(self):
        """Affiche tous les contacts"""
        if not self.contacts:
            print("Aucun contact enregistré.")
            return
        
        contacts_tries = sorted(self.contacts, key=lambda x: x['nom'].lower())
        
        print("\n=== CARNET D'ADRESSES ===")
        for i, contact in enumerate(contacts_tries, 1):
            print(f"{i}. {contact['nom']}")
            if contact['telephone']:
                print(f"   📞 {contact['telephone']}")
            if contact['email']:
                print(f"   📧 {contact['email']}")
            if contact['adresse']:
                print(f"   🏠 {contact['adresse']}")
            print()
    
    def rechercher_contact(self):
        """Recherche un contact"""
        terme = input("Rechercher (nom ou téléphone) : ").strip().lower()
        if not terme:
            return
        
        resultats = []
        for contact in self.contacts:
            if (terme in contact['nom'].lower() or 
                terme in contact['telephone']):
                resultats.append(contact)
        
        if resultats:
            print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
            for contact in resultats:
                print(f"- {contact['nom']} ({contact['telephone']})")
        else:
            print("Aucun contact trouvé.")
    
    def supprimer_contact(self):
        """Supprime un contact"""
        if not self.contacts:
            print("Aucun contact à supprimer.")
            return
        
        self.afficher_contacts()
        try:
            index = int(input("Numéro du contact à supprimer : ")) - 1
            if 0 <= index < len(self.contacts):
                contact_supprime = self.contacts.pop(index)
                self.sauvegarder_contacts()
                print(f"Contact {contact_supprime['nom']} supprimé.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")
    
    def menu_principal(self):
        """Menu principal de l'application"""
        while True:
            print("\n=== CARNET D'ADRESSES ===")
            print("1. Ajouter un contact")
            print("2. Afficher tous les contacts")
            print("3. Rechercher un contact")
            print("4. Supprimer un contact")
            print("5. Quitter")
            
            choix = input("Votre choix : ").strip()
            
            if choix == '1':
                self.ajouter_contact()
            elif choix == '2':
                self.afficher_contacts()
            elif choix == '3':
                self.rechercher_contact()
            elif choix == '4':
                self.supprimer_contact()
            elif choix == '5':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")

# Lancement de l'application
if __name__ == "__main__":
    carnet = CarnetAdresses()
    carnet.menu_principal()</code></pre>
    </div>
    
    <div id="solution-battleship">
        <h3>Solution : Jeu de bataille navale</h3>
        <pre><code>import random

class BatailleNavale:
    def __init__(self):
        self.taille = 10
        self.grille = [['~' for _ in range(self.taille)] for _ in range(self.taille)]
        self.navires = []
        self.coups_tires = 0
        self.navires_coules = 0
        self.total_navires = 5
        
    def placer_navires(self):
        """Place les navires aléatoirement sur la grille"""
        tailles_navires = [5, 4, 3, 3, 2]  # Porte-avions, croiseur, 2 destroyers, sous-marin
        
        for taille in tailles_navires:
            place = False
            tentatives = 0
            
            while not place and tentatives < 100:
                # Direction aléatoire (0=horizontal, 1=vertical)
                direction = random.randint(0, 1)
                
                if direction == 0:  # Horizontal
                    x = random.randint(0, self.taille - taille)
                    y = random.randint(0, self.taille - 1)
                    positions = [(x + i, y) for i in range(taille)]
                else:  # Vertical
                    x = random.randint(0, self.taille - 1)
                    y = random.randint(0, self.taille - taille)
                    positions = [(x, y + i) for i in range(taille)]
                
                # Vérifier si les positions sont libres
                if all(self.grille[pos[1]][pos[0]] == '~' for pos in positions):
                    # Placer le navire
                    for pos in positions:
                        self.grille[pos[1]][pos[0]] = 'N'
                    
                    self.navires.append({
                        'positions': positions,
                        'touches': set(),
                        'coule': False
                    })
                    place = True
                
                tentatives += 1
    
    def afficher_grille(self, montrer_navires=False):
        """Affiche la grille de jeu"""
        print("\n   ", end="")
        for i in range(self.taille):
            print(f"{i:2}", end=" ")
        print()
        
        for i in range(self.taille):
            print(f"{i:2} ", end="")
            for j in range(self.taille):
                cellule = self.grille[i][j]
                
                if cellule == 'N' and not montrer_navires:
                    print(" ~", end=" ")
                elif cellule == 'X':
                    print(" X", end=" ")  # Touché
                elif cellule == 'O':
                    print(" O", end=" ")  # Raté
                elif cellule == 'N' and montrer_navires:
                    print(" N", end=" ")  # Navire (mode debug)
                else:
                    print(" ~", end=" ")  # Eau
            print()
    
    def tirer(self, x, y):
        """Effectue un tir aux coordonnées données"""
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return "Coordonnées invalides"
        
        if self.grille[y][x] in ['X', 'O']:
            return "Déjà tiré ici"
        
        self.coups_tires += 1
        
        if self.grille[y][x] == 'N':
            self.grille[y][x] = 'X'
            
            # Vérifier quel navire a été touché
            for navire in self.navires:
                if (x, y) in navire['positions'] and not navire['coule']:
                    navire['touches'].add((x, y))
                    
                    # Vérifier si le navire est coulé
                    if len(navire['touches']) == len(navire['positions']):
                        navire['coule'] = True
                        self.navires_coules += 1
                        return "Coulé !"
                    else:
                        return "Touché !"
        else:
            self.grille[y][x] = 'O'
            return "Raté"
    
    def jeu_termine(self):
        """Vérifie si tous les navires sont coulés"""
        return self.navires_coules == self.total_navires
    
    def jouer(self):
        """Boucle principale du jeu"""
        print("=== BATAILLE NAVALE ===")
        print(f"Trouvez et coulez les {self.total_navires} navires !")
        print("Entrez les coordonnées sous la forme 'x y' (ex: 3 5)")
        
        self.placer_navires()
        
        while not self.jeu_termine():
            self.afficher_grille()
            print(f"\nCoups tirés : {self.coups_tires}")
            print(f"Navires coulés : {self.navires_coules}/{self.total_navires}")
            
            try:
                coordonnees = input("\nCoordonnées (x y) : ").split()
                if len(coordonnees) != 2:
                    print("Format invalide. Utilisez 'x y'")
                    continue
                
                x, y = int(coordonnees[0]), int(coordonnees[1])
                resultat = self.tirer(x, y)
                print(f"Résultat : {resultat}")
                
            except ValueError:
                print("Veuillez entrer des nombres valides.")
            except KeyboardInterrupt:
                print("\nPartie interrompue.")
                break
        
        if self.jeu_termine():
            self.afficher_grille(montrer_navires=True)
            print(f"\n🎉 Félicitations ! Vous avez coulé tous les navires en {self.coups_tires} coups !")

# Lancement du jeu
if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.jouer()</code></pre>
    </div>
    
    <div id="solution-library">
        <h3>Solution : Gestionnaire de bibliothèque</h3>
        <pre><code>from datetime import datetime, timedelta
import json
import os

class GestionnaireBibliotheque:
    def __init__(self, fichier_livres="livres.json", fichier_emprunts="emprunts.json"):
        self.fichier_livres = fichier_livres
        self.fichier_emprunts = fichier_emprunts
        self.livres = self.charger_donnees(fichier_livres)
        self.emprunts = self.charger_donnees(fichier_emprunts)
        self.duree_emprunt = 14  # jours
    
    def charger_donnees(self, fichier):
        """Charge les données depuis un fichier JSON"""
        if os.path.exists(fichier):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def sauvegarder_donnees(self, donnees, fichier):
        """Sauvegarde les données dans un fichier JSON"""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False)
    
    def ajouter_livre(self):
        """Ajoute un nouveau livre"""
        titre = input("Titre : ").strip()
        auteur = input("Auteur : ").strip()
        isbn = input("ISBN : ").strip()
        
        if not all([titre, auteur, isbn]):
            print("Tous les champs sont obligatoires.")
            return
        
        # Vérifier si l'ISBN existe déjà
        if any(livre['isbn'] == isbn for livre in self.livres):
            print("Un livre avec cet ISBN existe déjà.")
            return
        
        livre = {
            'id': len(self.livres) + 1,
            'titre': titre,
            'auteur': auteur,
            'isbn': isbn,
            'disponible': True,
            'nb_emprunts': 0
        }
        
        self.livres.append(livre)
        self.sauvegarder_donnees(self.livres, self.fichier_livres)
        print(f"Livre '{titre}' ajouté avec succès.")
    
    def afficher_livres(self):
        """Affiche tous les livres"""
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
            return
        
        print("\n=== CATALOGUE DES LIVRES ===")
        for livre in self.livres:
            statut = "📗 Disponible" if livre['disponible'] else "📕 Emprunté"
            print(f"{livre['id']}. {livre['titre']}")
            print(f"   Auteur: {livre['auteur']}")
            print(f"   ISBN: {livre['isbn']}")
            print(f"   Statut: {statut}")
            print(f"   Emprunts: {livre['nb_emprunts']}")
            print()
    
    def rechercher_livres(self):
        """Recherche des livres par titre, auteur ou ISBN"""
        terme = input("Rechercher (titre, auteur ou ISBN) : ").strip().lower()
        if not terme:
            return
        
        resultats = []
        for livre in self.livres:
            if (terme in livre['titre'].lower() or 
                terme in livre['auteur'].lower() or 
                terme in livre['isbn'].lower()):
                resultats.append(livre)
        
        if resultats:
            print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
            for livre in resultats:
                statut = "Disponible" if livre['disponible'] else "Emprunté"
                print(f"- {livre['titre']} par {livre['auteur']} ({statut})")
        else:
            print("Aucun livre trouvé.")
    
    def emprunter_livre(self):
        """Emprunte un livre"""
        self.afficher_livres()
        
        try:
            livre_id = int(input("ID du livre à emprunter : "))
            livre = next((l for l in self.livres if l['id'] == livre_id), None)
            
            if not livre:
                print("Livre introuvable.")
                return
            
            if not livre['disponible']:
                print("Ce livre est déjà emprunté.")
                return
            
            emprunteur = input("Nom de l'emprunteur : ").strip()
            if not emprunteur:
                print("Le nom de l'emprunteur est obligatoire.")
                return
            
            # Créer l'emprunt
            emprunt = {
                'id': len(self.emprunts) + 1,
                'livre_id': livre_id,
                'emprunteur': emprunteur,
                'date_emprunt': datetime.now().isoformat(),
                'date_retour_prevue': (datetime.now() + timedelta(days=self.duree_emprunt)).isoformat(),
                'date_retour_effective': None
            }
            
            # Mettre à jour le livre
            livre['disponible'] = False
            livre['nb_emprunts'] += 1
            
            # Sauvegarder
            self.emprunts.append(emprunt)
            self.sauvegarder_donnees(self.livres, self.fichier_livres)
            self.sauvegarder_donnees(self.emprunts, self.fichier_emprunts)
            
            print(f"Livre emprunté par {emprunteur}.")
            print(f"Date de retour prévue : {datetime.fromisoformat(emprunt['date_retour_prevue']).strftime('%d/%m/%Y')}")
            
        except ValueError:
            print("Veuillez entrer un ID valide.")
    
    def retourner_livre(self):
        """Retourne un livre emprunté"""
        # Afficher les emprunts en cours
        emprunts_actifs = [e for e in self.emprunts if e['date_retour_effective'] is None]
        
        if not emprunts_actifs:
            print("Aucun emprunt en cours.")
            return
        
        print("\n=== EMPRUNTS EN COURS ===")
        for emprunt in emprunts_actifs:
            livre = next((l for l in self.livres if l['id'] == emprunt['livre_id']), None)
            if livre:
                date_retour = datetime.fromisoformat(emprunt['date_retour_prevue'])
                retard = (datetime.now() - date_retour).days
                statut_retard = f" (RETARD: {retard} jours)" if retard > 0 else ""
                
                print(f"{emprunt['id']}. {livre['titre']}")
                print(f"   Emprunteur: {emprunt['emprunteur']}")
                print(f"   Retour prévu: {date_retour.strftime('%d/%m/%Y')}{statut_retard}")
                print()
        
        try:
            emprunt_id = int(input("ID de l'emprunt à retourner : "))
            emprunt = next((e for e in self.emprunts if e['id'] == emprunt_id), None)
            
            if not emprunt or emprunt['date_retour_effective']:
                print("Emprunt introuvable ou déjà retourné.")
                return
            
            # Mettre à jour l'emprunt
            emprunt['date_retour_effective'] = datetime.now().isoformat()
            
            # Mettre à jour le livre
            livre = next((l for l in self.livres if l['id'] == emprunt['livre_id']), None)
            if livre:
                livre['disponible'] = True
            
            # Sauvegarder
            self.sauvegarder_donnees(self.livres, self.fichier_livres)
            self.sauvegarder_donnees(self.emprunts, self.fichier_emprunts)
            
            print("Livre retourné avec succès.")
            
        except ValueError:
            print("Veuillez entrer un ID valide.")
    
    def afficher_statistiques(self):
        """Affiche les statistiques de la bibliothèque"""
        total_livres = len(self.livres)
        livres_disponibles = len([l for l in self.livres if l['disponible']])
        livres_empruntes = total_livres - livres_disponibles
        
        emprunts_actifs = len([e for e in self.emprunts if e['date_retour_effective'] is None])
        total_emprunts = len(self.emprunts)
        
        # Livres les plus empruntés
        livres_populaires = sorted(self.livres, key=lambda x: x['nb_emprunts'], reverse=True)[:5]
        
        # Retards
        retards = 0
        for emprunt in self.emprunts:
            if emprunt['date_retour_effective'] is None:
                date_retour = datetime.fromisoformat(emprunt['date_retour_prevue'])
                if datetime.now() > date_retour:
                    retards += 1
        
        print("\n=== STATISTIQUES ===")
        print(f"Total de livres : {total_livres}")
        print(f"Livres disponibles : {livres_disponibles}")
        print(f"Livres empruntés : {livres_empruntes}")
        print(f"Emprunts actifs : {emprunts_actifs}")
        print(f"Total emprunts historique : {total_emprunts}")
        print(f"Retards : {retards}")
        
        if livres_populaires:
            print("\nLivres les plus empruntés :")
            for i, livre in enumerate(livres_populaires, 1):
                if livre['nb_emprunts'] > 0:
                    print(f"{i}. {livre['titre']} ({livre['nb_emprunts']} emprunts)")
    
    def menu_principal(self):
        """Menu principal de l'application"""
        while True:
            print("\n=== GESTIONNAIRE DE BIBLIOTHÈQUE ===")
            print("1. Ajouter un livre")
            print("2. Afficher tous les livres")
            print("3. Rechercher des livres")
            print("4. Emprunter un livre")
            print("5. Retourner un livre")
            print("6. Statistiques")
            print("7. Quitter")
            
            choix = input("Votre choix : ").strip()
            
            if choix == '1':
                self.ajouter_livre()
            elif choix == '2':
                self.afficher_livres()
            elif choix == '3':
                self.rechercher_livres()
            elif choix == '4':
                self.emprunter_livre()
            elif choix == '5':
                self.retourner_livre()
            elif choix == '6':
                self.afficher_statistiques()
            elif choix == '7':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")

# Lancement de l'application
if __name__ == "__main__":
    bibliotheque = GestionnaireBibliotheque()
    bibliotheque.menu_principal()</code></pre>
    </div>
</div>