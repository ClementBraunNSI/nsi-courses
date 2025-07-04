# Fiche d'exercices : Graphes

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
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Découverte</button>
    <button class="section-tab" onclick="showSection('representation-section')">📊 Représentation</button>
    <button class="section-tab" onclick="showSection('parcours-section')">🔍 Parcours</button>
    <button class="section-tab" onclick="showSection('algorithmes-section')">🚀 Algorithmes</button>
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
                    <li>Dessinez les graphes pour mieux visualiser les problèmes</li>
                    <li>Précisez si le graphe est orienté ou non orienté</li>
                    <li>Indiquez la complexité de vos algorithmes</li>
                    <li>Testez vos implémentations avec plusieurs exemples</li>
                    <li>Gérez les cas particuliers (graphe vide, sommet isolé, etc.)</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Découverte 🌱</div>
            <h4 class="exercise-title">Vocabulaire des graphes</h4>
            <div class="exercise-content">
                <p>Définissez les termes suivants avec des exemples :</p>
                <ol>
                    <li><strong>Sommet</strong> et <strong>Arête</strong></li>
                    <li><strong>Graphe orienté</strong> vs <strong>non orienté</strong></li>
                    <li><strong>Degré</strong> d'un sommet</li>
                    <li><strong>Chemin</strong> et <strong>Cycle</strong></li>
                    <li><strong>Graphe connexe</strong></li>
                    <li><strong>Graphe pondéré</strong></li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Définitions :</h4>
                <ol>
                    <li><strong>Sommet</strong> : nœud du graphe (ex: ville). <strong>Arête</strong> : lien entre deux sommets (ex: route)</li>
                    <li><strong>Orienté</strong> : arêtes avec direction (→). <strong>Non orienté</strong> : arêtes bidirectionnelles (—)</li>
                    <li><strong>Degré</strong> : nombre d'arêtes connectées à un sommet</li>
                    <li><strong>Chemin</strong> : séquence de sommets reliés. <strong>Cycle</strong> : chemin qui revient au point de départ</li>
                    <li><strong>Connexe</strong> : il existe un chemin entre toute paire de sommets</li>
                    <li><strong>Pondéré</strong> : chaque arête a un poids (distance, coût, temps...)</li>
                </ol>
                
                <h4>Exemples concrets :</h4>
                <ul>
                    <li><strong>Réseau routier</strong> : villes (sommets), routes (arêtes), distances (poids)</li>
                    <li><strong>Réseau social</strong> : personnes (sommets), amitiés (arêtes)</li>
                    <li><strong>Internet</strong> : serveurs (sommets), connexions (arêtes orientées)</li>
                    <li><strong>Molécule</strong> : atomes (sommets), liaisons (arêtes)</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Découverte 🌱</div>
            <h4 class="exercise-title">Modélisation avec des graphes</h4>
            <div class="exercise-content">
                <p>Pour chaque situation, proposez une modélisation par graphe :</p>
                <ol>
                    <li>Un réseau de transport en commun</li>
                    <li>Les prérequis entre cours universitaires</li>
                    <li>Un tournoi de tennis</li>
                    <li>Les pages web et leurs liens</li>
                    <li>Un labyrinthe</li>
                </ol>
                <p>Pour chaque cas, précisez : orienté/non orienté, pondéré/non pondéré, et justifiez.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Modélisations :</h4>
                <ol>
                    <li><strong>Transport en commun</strong>
                        <ul>
                            <li>Sommets : stations/arrêts</li>
                            <li>Arêtes : liaisons directes</li>
                            <li>Non orienté (bidirectionnel), pondéré (temps/distance)</li>
                        </ul>
                    </li>
                    <li><strong>Prérequis de cours</strong>
                        <ul>
                            <li>Sommets : cours</li>
                            <li>Arêtes : relation de prérequis</li>
                            <li>Orienté (A → B = A prérequis de B), non pondéré</li>
                        </ul>
                    </li>
                    <li><strong>Tournoi de tennis</strong>
                        <ul>
                            <li>Sommets : joueurs</li>
                            <li>Arêtes : matchs joués</li>
                            <li>Orienté (A → B = A a battu B), pondéré (score)</li>
                        </ul>
                    </li>
                    <li><strong>Pages web</strong>
                        <ul>
                            <li>Sommets : pages web</li>
                            <li>Arêtes : liens hypertextes</li>
                            <li>Orienté (lien unidirectionnel), non pondéré</li>
                        </ul>
                    </li>
                    <li><strong>Labyrinthe</strong>
                        <ul>
                            <li>Sommets : intersections/cases</li>
                            <li>Arêtes : passages possibles</li>
                            <li>Non orienté (bidirectionnel), non pondéré</li>
                        </ul>
                    </li>
                </ol>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🟢</div>
            <h4 class="exercise-title">Propriétés d'un graphe</h4>
            <div class="exercise-content">
                <p>Soit le graphe non orienté suivant :</p>
                <pre>
A ---- B ---- C
|      |      |
D ---- E ---- F
</pre>
                <p>Calculez :</p>
                <ol>
                    <li>Le nombre de sommets et d'arêtes</li>
                    <li>Le degré de chaque sommet</li>
                    <li>La somme des degrés (que remarquez-vous ?)</li>
                    <li>Trouvez tous les chemins de A à F</li>
                    <li>Y a-t-il des cycles ? Lesquels ?</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Analyse du graphe :</h4>
                <ol>
                    <li><strong>Nombre de sommets :</strong> 6 (A, B, C, D, E, F)
                        <br><strong>Nombre d'arêtes :</strong> 7 (AB, BC, AD, BE, CF, DE, EF)</li>
                    
                    <li><strong>Degrés :</strong>
                        <ul>
                            <li>deg(A) = 2 (connecté à B et D)</li>
                            <li>deg(B) = 3 (connecté à A, C et E)</li>
                            <li>deg(C) = 2 (connecté à B et F)</li>
                            <li>deg(D) = 2 (connecté à A et E)</li>
                            <li>deg(E) = 3 (connecté à B, D et F)</li>
                            <li>deg(F) = 2 (connecté à C et E)</li>
                        </ul>
                    </li>
                    
                    <li><strong>Somme des degrés :</strong> 2+3+2+2+3+2 = 14
                        <br><strong>Remarque :</strong> La somme des degrés = 2 × nombre d'arêtes (14 = 2×7)
                        <br>Car chaque arête contribue à 2 degrés (un pour chaque extrémité)</li>
                    
                    <li><strong>Chemins de A à F :</strong>
                        <ul>
                            <li>A → B → C → F (longueur 3)</li>
                            <li>A → B → E → F (longueur 3)</li>
                            <li>A → D → E → F (longueur 3)</li>
                            <li>A → D → E → B → C → F (longueur 5)</li>
                            <li>A → B → E → D → A → B → C → F (avec cycle, longueur 7)</li>
                        </ul>
                    </li>
                    
                    <li><strong>Cycles :</strong>
                        <ul>
                            <li>A → B → E → D → A (cycle de longueur 4)</li>
                            <li>B → C → F → E → B (cycle de longueur 4)</li>
                        </ul>
                    </li>
                </ol>
            </div>
        </div>
    </div>
</div>
</div>

<div id="representation-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Implémentation avec matrice d'adjacence</h4>
            <div class="exercise-content">
                <p>Implémentez une classe <code>GrapheMatrice</code> utilisant une matrice d'adjacence.</p>
                <p><strong>Méthodes à implémenter :</strong></p>
                <ul>
                    <li><code>__init__(nb_sommets, oriente=False)</code></li>
                    <li><code>ajouter_arete(i, j, poids=1)</code></li>
                    <li><code>supprimer_arete(i, j)</code></li>
                    <li><code>est_adjacent(i, j)</code></li>
                    <li><code>voisins(i)</code></li>
                    <li><code>afficher()</code></li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class GrapheMatrice:
    def __init__(self, nb_sommets, oriente=False):
        """Crée un graphe avec une matrice d'adjacence"""
        self.nb_sommets = nb_sommets
        self.oriente = oriente
        # Matrice initialisée à 0 (pas d'arête)
        self.matrice = [[0 for _ in range(nb_sommets)] for _ in range(nb_sommets)]
    
    def ajouter_arete(self, i, j, poids=1):
        """Ajoute une arête entre les sommets i et j"""
        if 0 <= i < self.nb_sommets and 0 <= j < self.nb_sommets:
            self.matrice[i][j] = poids
            
            # Si non orienté, ajouter l'arête inverse
            if not self.oriente:
                self.matrice[j][i] = poids
        else:
            raise ValueError("Indices de sommets invalides")
    
    def supprimer_arete(self, i, j):
        """Supprime l'arête entre les sommets i et j"""
        if 0 <= i < self.nb_sommets and 0 <= j < self.nb_sommets:
            self.matrice[i][j] = 0
            
            if not self.oriente:
                self.matrice[j][i] = 0
        else:
            raise ValueError("Indices de sommets invalides")
    
    def est_adjacent(self, i, j):
        """Vérifie si les sommets i et j sont adjacents"""
        if 0 <= i < self.nb_sommets and 0 <= j < self.nb_sommets:
            return self.matrice[i][j] != 0
        return False
    
    def voisins(self, i):
        """Retourne la liste des voisins du sommet i"""
        if 0 <= i < self.nb_sommets:
            voisins = []
            for j in range(self.nb_sommets):
                if self.matrice[i][j] != 0:
                    voisins.append((j, self.matrice[i][j]))
            return voisins
        return []
    
    def degre(self, i):
        """Calcule le degré du sommet i"""
        return len(self.voisins(i))
    
    def afficher(self):
        """Affiche la matrice d'adjacence"""
        print("Matrice d'adjacence:")
        print("   ", end="")
        for j in range(self.nb_sommets):
            print(f"{j:3}", end="")
        print()
        
        for i in range(self.nb_sommets):
            print(f"{i}: ", end="")
            for j in range(self.nb_sommets):
                print(f"{self.matrice[i][j]:3}", end="")
            print()
    
    def afficher_graphe(self):
        """Affiche le graphe sous forme de liste d'adjacence"""
        print(f"Graphe {'orienté' if self.oriente else 'non orienté'}:")
        for i in range(self.nb_sommets):
            voisins = self.voisins(i)
            if voisins:
                voisins_str = ", ".join([f"{j}({p})" for j, p in voisins])
                print(f"  {i}: {voisins_str}")
            else:
                print(f"  {i}: (isolé)")

# Test de l'implémentation
if __name__ == "__main__":
    # Création d'un graphe non orienté à 4 sommets
    g = GrapheMatrice(4, oriente=False)
    
    # Ajout d'arêtes
    g.ajouter_arete(0, 1, 5)
    g.ajouter_arete(0, 2, 3)
    g.ajouter_arete(1, 3, 2)
    g.ajouter_arete(2, 3, 1)
    
    # Affichage
    g.afficher()
    print()
    g.afficher_graphe()
    
    # Tests
    print(f"\nSommets 0 et 1 adjacents: {g.est_adjacent(0, 1)}")
    print(f"Voisins de 0: {g.voisins(0)}")
    print(f"Degré de 0: {g.degre(0)}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Implémentation avec liste d'adjacence</h4>
            <div class="exercise-content">
                <p>Implémentez une classe <code>GrapheListe</code> utilisant un dictionnaire de listes d'adjacence.</p>
                <p><strong>Avantage :</strong> Plus efficace en mémoire pour les graphes peu denses.</p>
                <p><strong>Bonus :</strong> Ajoutez une méthode pour convertir vers une matrice d'adjacence.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class GrapheListe:
    def __init__(self, oriente=False):
        """Crée un graphe avec des listes d'adjacence"""
        self.sommets = {}  # dictionnaire : sommet -> liste des voisins
        self.oriente = oriente
    
    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe"""
        if sommet not in self.sommets:
            self.sommets[sommet] = []
    
    def ajouter_arete(self, sommet1, sommet2, poids=1):
        """Ajoute une arête entre deux sommets"""
        # S'assurer que les sommets existent
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        
        # Ajouter l'arête (éviter les doublons)
        if not any(v == sommet2 for v, p in self.sommets[sommet1]):
            self.sommets[sommet1].append((sommet2, poids))
        
        # Si non orienté, ajouter l'arête inverse
        if not self.oriente:
            if not any(v == sommet1 for v, p in self.sommets[sommet2]):
                self.sommets[sommet2].append((sommet1, poids))
    
    def supprimer_arete(self, sommet1, sommet2):
        """Supprime une arête"""
        if sommet1 in self.sommets:
            self.sommets[sommet1] = [(v, p) for v, p in self.sommets[sommet1] if v != sommet2]
        
        if not self.oriente and sommet2 in self.sommets:
            self.sommets[sommet2] = [(v, p) for v, p in self.sommets[sommet2] if v != sommet1]
    
    def supprimer_sommet(self, sommet):
        """Supprime un sommet et toutes ses arêtes"""
        if sommet in self.sommets:
            # Supprimer toutes les arêtes vers ce sommet
            for s in self.sommets:
                self.sommets[s] = [(v, p) for v, p in self.sommets[s] if v != sommet]
            
            # Supprimer le sommet
            del self.sommets[sommet]
    
    def voisins(self, sommet):
        """Retourne la liste des voisins d'un sommet"""
        return self.sommets.get(sommet, [])
    
    def est_adjacent(self, sommet1, sommet2):
        """Vérifie si deux sommets sont adjacents"""
        return any(voisin == sommet2 for voisin, _ in self.voisins(sommet1))
    
    def degre(self, sommet):
        """Retourne le degré d'un sommet"""
        return len(self.voisins(sommet))
    
    def nb_sommets(self):
        """Retourne le nombre de sommets"""
        return len(self.sommets)
    
    def nb_aretes(self):
        """Retourne le nombre d'arêtes"""
        total = sum(len(voisins) for voisins in self.sommets.values())
        return total if self.oriente else total // 2
    
    def liste_sommets(self):
        """Retourne la liste des sommets"""
        return list(self.sommets.keys())
    
    def afficher(self):
        """Affiche le graphe"""
        print(f"Graphe {'orienté' if self.oriente else 'non orienté'}:")
        for sommet, voisins in self.sommets.items():
            if voisins:
                voisins_str = ", ".join([f"{v}({p})" for v, p in voisins])
                print(f"  {sommet}: {voisins_str}")
            else:
                print(f"  {sommet}: (isolé)")
    
    def vers_matrice(self):
        """Convertit vers une matrice d'adjacence"""
        sommets_liste = sorted(self.liste_sommets())
        n = len(sommets_liste)
        
        # Créer un mapping sommet -> index
        index_map = {sommet: i for i, sommet in enumerate(sommets_liste)}
        
        # Créer la matrice
        matrice = [[0 for _ in range(n)] for _ in range(n)]
        
        for sommet, voisins in self.sommets.items():
            i = index_map[sommet]
            for voisin, poids in voisins:
                j = index_map[voisin]
                matrice[i][j] = poids
        
        return matrice, sommets_liste
    
    def afficher_matrice(self):
        """Affiche la représentation matricielle"""
        matrice, sommets = self.vers_matrice()
        
        print("Matrice d'adjacence:")
        print("     ", end="")
        for sommet in sommets:
            print(f"{sommet:3}", end="")
        print()
        
        for i, sommet in enumerate(sommets):
            print(f"{sommet:3}: ", end="")
            for j in range(len(sommets)):
                print(f"{matrice[i][j]:3}", end="")
            print()

# Test de l'implémentation
if __name__ == "__main__":
    # Création d'un graphe non orienté
    g = GrapheListe(oriente=False)
    
    # Ajout d'arêtes (les sommets sont créés automatiquement)
    g.ajouter_arete('A', 'B', 5)
    g.ajouter_arete('A', 'C', 3)
    g.ajouter_arete('B', 'D', 2)
    g.ajouter_arete('C', 'D', 1)
    
    # Affichage
    g.afficher()
    print(f"\nNombre de sommets: {g.nb_sommets()}")
    print(f"Nombre d'arêtes: {g.nb_aretes()}")
    
    print(f"\nVoisins de A: {g.voisins('A')}")
    print(f"Degré de A: {g.degre('A')}")
    print(f"A et B adjacents: {g.est_adjacent('A', 'B')}")
    
    print("\n" + "="*40)
    g.afficher_matrice()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Comparaison des représentations</h4>
            <div class="exercise-content">
                <p>Analysez et comparez les deux représentations (matrice vs liste d'adjacence) :</p>
                <ol>
                    <li>Implémentez une fonction de benchmark qui mesure le temps d'exécution</li>
                    <li>Testez sur des graphes de différentes densités (peu dense, dense)</li>
                    <li>Comparez les opérations : ajout d'arête, vérification d'adjacence, parcours des voisins</li>
                    <li>Analysez l'utilisation mémoire</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Analyse théorique des complexités :</h4>
                <table>
                    <tr><th>Opération</th><th>Matrice d'adjacence</th><th>Liste d'adjacence</th></tr>
                    <tr><td>Espace mémoire</td><td>O(n²)</td><td>O(n + m)</td></tr>
                    <tr><td>Ajouter arête</td><td>O(1)</td><td>O(1)</td></tr>
                    <tr><td>Supprimer arête</td><td>O(1)</td><td>O(degré)</td></tr>
                    <tr><td>Vérifier adjacence</td><td>O(1)</td><td>O(degré)</td></tr>
                    <tr><td>Parcourir voisins</td><td>O(n)</td><td>O(degré)</td></tr>
                    <tr><td>Parcourir tout le graphe</td><td>O(n²)</td><td>O(n + m)</td></tr>
                </table>
                
                <h4>Recommandations :</h4>
                <ul>
                    <li><strong>Graphe DENSE (m ≈ n²)</strong> : Matrice d'adjacence</li>
                    <li><strong>Graphe PEU DENSE (m << n²)</strong> : Liste d'adjacence</li>
                    <li><strong>Vérifications d'adjacence fréquentes</strong> : Matrice</li>
                    <li><strong>Parcours de voisins fréquents</strong> : Liste</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</div>

<div id="parcours-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Parcours en largeur (BFS)</h4>
            <div class="exercise-content">
                <p>Implémentez l'algorithme de parcours en largeur (Breadth-First Search).</p>
                <p><strong>Fonctionnalités :</strong></p>
                <ul>
                    <li>Parcours complet depuis un sommet de départ</li>
                    <li>Calcul des distances depuis le sommet de départ</li>
                    <li>Reconstruction du chemin le plus court</li>
                    <li>Vérification de connexité</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">from collections import deque

def bfs_parcours(graphe, sommet_depart):
    """Parcours en largeur depuis un sommet de départ"""
    visites = set()
    file = deque([sommet_depart])
    ordre_visite = []
    
    visites.add(sommet_depart)
    
    while file:
        sommet_actuel = file.popleft()
        ordre_visite.append(sommet_actuel)
        
        # Explorer tous les voisins
        for voisin, _ in graphe.voisins(sommet_actuel):
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)
    
    return ordre_visite

def bfs_distances(graphe, sommet_depart):
    """Calcule les distances depuis un sommet de départ"""
    distances = {sommet_depart: 0}
    predecesseurs = {sommet_depart: None}
    file = deque([sommet_depart])
    
    while file:
        sommet_actuel = file.popleft()
        distance_actuelle = distances[sommet_actuel]
        
        # Explorer tous les voisins
        for voisin, _ in graphe.voisins(sommet_actuel):
            if voisin not in distances:
                distances[voisin] = distance_actuelle + 1
                predecesseurs[voisin] = sommet_actuel
                file.append(voisin)
    
    return distances, predecesseurs

def chemin_plus_court(predecesseurs, sommet_depart, sommet_arrivee):
    """Reconstruit le chemin le plus court"""
    if sommet_arrivee not in predecesseurs:
        return None  # Pas de chemin
    
    chemin = []
    sommet_actuel = sommet_arrivee
    
    while sommet_actuel is not None:
        chemin.append(sommet_actuel)
        sommet_actuel = predecesseurs[sommet_actuel]
    
    return chemin[::-1]  # Inverser pour avoir le bon ordre

def est_connexe(graphe):
    """Vérifie si le graphe est connexe"""
    if graphe.nb_sommets() == 0:
        return True
    
    # Prendre un sommet arbitraire
    premier_sommet = next(iter(graphe.liste_sommets()))
    
    # Faire un BFS depuis ce sommet
    visites = bfs_parcours(graphe, premier_sommet)
    
    # Le graphe est connexe si tous les sommets sont visités
    return len(visites) == graphe.nb_sommets()

def composantes_connexes(graphe):
    """Trouve toutes les composantes connexes"""
    tous_visites = set()
    composantes = []
    
    for sommet in graphe.liste_sommets():
        if sommet not in tous_visites:
            # Nouvelle composante
            composante = bfs_parcours(graphe, sommet)
            composantes.append(composante)
            tous_visites.update(composante)
    
    return composantes

# Test de l'implémentation
if __name__ == "__main__":
    # Créer un graphe de test
    g = GrapheListe(oriente=False)
    
    # Ajouter des arêtes
    g.ajouter_arete('A', 'B')
    g.ajouter_arete('A', 'C')
    g.ajouter_arete('B', 'D')
    g.ajouter_arete('C', 'E')
    g.ajouter_arete('D', 'E')
    g.ajouter_arete('F', 'G')  # Composante séparée
    
    print("Graphe:")
    g.afficher()
    
    # Test du parcours BFS
    print(f"\nParcours BFS depuis A: {bfs_parcours(g, 'A')}")
    
    # Test des distances
    distances, predecesseurs = bfs_distances(g, 'A')
    print(f"\nDistances depuis A: {distances}")
    
    # Test du chemin le plus court
    chemin = chemin_plus_court(predecesseurs, 'A', 'E')
    print(f"Chemin le plus court A → E: {chemin}")
    
    # Test de connexité
    print(f"\nGraphe connexe: {est_connexe(g)}")
    
    # Composantes connexes
    composantes = composantes_connexes(g)
    print(f"Composantes connexes: {composantes}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Parcours en profondeur (DFS)</h4>
            <div class="exercise-content">
                <p>Implémentez l'algorithme de parcours en profondeur (Depth-First Search).</p>
                <p><strong>Versions à implémenter :</strong></p>
                <ul>
                    <li>Version récursive</li>
                    <li>Version itérative avec pile</li>
                    <li>Détection de cycles</li>
                    <li>Tri topologique (pour graphe orienté)</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def dfs_recursif(graphe, sommet_depart, visites=None, ordre_visite=None):
    """Parcours en profondeur récursif"""
    if visites is None:
        visites = set()
    if ordre_visite is None:
        ordre_visite = []
    
    visites.add(sommet_depart)
    ordre_visite.append(sommet_depart)
    
    # Explorer tous les voisins
    for voisin, _ in graphe.voisins(sommet_depart):
        if voisin not in visites:
            dfs_recursif(graphe, voisin, visites, ordre_visite)
    
    return ordre_visite

def dfs_iteratif(graphe, sommet_depart):
    """Parcours en profondeur itératif avec pile"""
    visites = set()
    pile = [sommet_depart]
    ordre_visite = []
    
    while pile:
        sommet_actuel = pile.pop()
        
        if sommet_actuel not in visites:
            visites.add(sommet_actuel)
            ordre_visite.append(sommet_actuel)
            
            # Ajouter les voisins à la pile (en ordre inverse pour garder l'ordre)
            voisins = [v for v, _ in graphe.voisins(sommet_actuel)]
            for voisin in reversed(voisins):
                if voisin not in visites:
                    pile.append(voisin)
    
    return ordre_visite

def detecter_cycle_non_oriente(graphe):
    """Détecte un cycle dans un graphe non orienté"""
    visites = set()
    
    def dfs_cycle(sommet, parent):
        visites.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visites:
                if dfs_cycle(voisin, sommet):
                    return True
            elif voisin != parent:
                # Arête vers un sommet déjà visité (pas le parent) = cycle
                return True
        
        return False
    
    # Tester chaque composante connexe
    for sommet in graphe.liste_sommets():
        if sommet not in visites:
            if dfs_cycle(sommet, None):
                return True
    
    return False

def detecter_cycle_oriente(graphe):
    """Détecte un cycle dans un graphe orienté"""
    BLANC, GRIS, NOIR = 0, 1, 2
    couleurs = {sommet: BLANC for sommet in graphe.liste_sommets()}
    
    def dfs_cycle(sommet):
        couleurs[sommet] = GRIS
        
        for voisin, _ in graphe.voisins(sommet):
            if couleurs[voisin] == GRIS:
                # Arête vers un sommet en cours de visite = cycle
                return True
            elif couleurs[voisin] == BLANC and dfs_cycle(voisin):
                return True
        
        couleurs[sommet] = NOIR
        return False
    
    # Tester chaque sommet
    for sommet in graphe.liste_sommets():
        if couleurs[sommet] == BLANC:
            if dfs_cycle(sommet):
                return True
    
    return False

def tri_topologique(graphe):
    """Tri topologique d'un graphe orienté acyclique"""
    if not graphe.oriente:
        raise ValueError("Le tri topologique nécessite un graphe orienté")
    
    if detecter_cycle_oriente(graphe):
        raise ValueError("Le graphe contient un cycle")
    
    visites = set()
    pile_resultat = []
    
    def dfs_topo(sommet):
        visites.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visites:
                dfs_topo(voisin)
        
        # Ajouter le sommet à la pile après avoir visité tous ses successeurs
        pile_resultat.append(sommet)
    
    # Visiter tous les sommets
    for sommet in graphe.liste_sommets():
        if sommet not in visites:
            dfs_topo(sommet)
    
    # Inverser la pile pour obtenir l'ordre topologique
    return pile_resultat[::-1]

def temps_decouverte_fin(graphe, sommet_depart):
    """Calcule les temps de découverte et de fin pour chaque sommet"""
    temps = [0]  # Utiliser une liste pour pouvoir modifier dans les fonctions imbriquées
    decouverte = {}
    fin = {}
    visites = set()
    
    def dfs_temps(sommet):
        temps[0] += 1
        decouverte[sommet] = temps[0]
        visites.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visites:
                dfs_temps(voisin)
        
        temps[0] += 1
        fin[sommet] = temps[0]
    
    dfs_temps(sommet_depart)
    return decouverte, fin

# Test de l'implémentation
if __name__ == "__main__":
    # Test avec graphe non orienté
    g_non_oriente = GrapheListe(oriente=False)
    g_non_oriente.ajouter_arete('A', 'B')
    g_non_oriente.ajouter_arete('A', 'C')
    g_non_oriente.ajouter_arete('B', 'D')
    g_non_oriente.ajouter_arete('C', 'D')
    
    print("Graphe non orienté:")
    g_non_oriente.afficher()
    
    print(f"\nDFS récursif depuis A: {dfs_recursif(g_non_oriente, 'A')}")
    print(f"DFS itératif depuis A: {dfs_iteratif(g_non_oriente, 'A')}")
    print(f"Cycle détecté: {detecter_cycle_non_oriente(g_non_oriente)}")
    
    # Test avec graphe orienté
    g_oriente = GrapheListe(oriente=True)
    g_oriente.ajouter_arete('A', 'B')
    g_oriente.ajouter_arete('A', 'C')
    g_oriente.ajouter_arete('B', 'D')
    g_oriente.ajouter_arete('C', 'D')
    
    print("\n" + "="*40)
    print("Graphe orienté:")
    g_oriente.afficher()
    
    print(f"\nCycle détecté: {detecter_cycle_oriente(g_oriente)}")
    print(f"Tri topologique: {tri_topologique(g_oriente)}")
    
    # Temps de découverte et fin
    decouverte, fin = temps_decouverte_fin(g_oriente, 'A')
    print(f"\nTemps de découverte: {decouverte}")
    print(f"Temps de fin: {fin}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Applications des parcours</h4>
            <div class="exercise-content">
                <p>Utilisez BFS et DFS pour résoudre des problèmes concrets :</p>
                <ol>
                    <li><strong>Labyrinthe :</strong> Trouvez le chemin le plus court de l'entrée à la sortie</li>
                    <li><strong>Îles :</strong> Comptez le nombre d'îles dans une grille binaire</li>
                    <li><strong>Coloration :</strong> Vérifiez si un graphe est bipartite</li>
                    <li><strong>Planification :</strong> Ordonnez des tâches avec dépendances</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">from collections import deque

def resoudre_labyrinthe(labyrinthe, entree, sortie):
    """Trouve le chemin le plus court dans un labyrinthe"""
    lignes, colonnes = len(labyrinthe), len(labyrinthe[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # droite, bas, gauche, haut
    
    def est_valide(x, y):
        return (0 <= x < lignes and 0 <= y < colonnes and 
                labyrinthe[x][y] != '#')  # '#' = mur
    
    # BFS pour trouver le chemin le plus court
    file = deque([(entree, [entree])])
    visites = {entree}
    
    while file:
        (x, y), chemin = file.popleft()
        
        if (x, y) == sortie:
            return chemin
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if est_valide(nx, ny) and (nx, ny) not in visites:
                visites.add((nx, ny))
                nouveau_chemin = chemin + [(nx, ny)]
                file.append(((nx, ny), nouveau_chemin))
    
    return None  # Pas de chemin trouvé

def compter_iles(grille):
    """Compte le nombre d'îles dans une grille binaire"""
    if not grille or not grille[0]:
        return 0
    
    lignes, colonnes = len(grille), len(grille[0])
    visites = set()
    nb_iles = 0
    
    def dfs_ile(x, y):
        if (x, y) in visites or x < 0 or x >= lignes or y < 0 or y >= colonnes:
            return
        if grille[x][y] == 0:  # Eau
            return
        
        visites.add((x, y))
        
        # Explorer les 4 directions (ou 8 avec diagonales)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs_ile(x + dx, y + dy)
    
    # Parcourir toute la grille
    for i in range(lignes):
        for j in range(colonnes):
            if grille[i][j] == 1 and (i, j) not in visites:
                # Nouvelle île trouvée
                dfs_ile(i, j)
                nb_iles += 1
    
    return nb_iles

def est_bipartite(graphe):
    """Vérifie si un graphe est bipartite (2-coloriable)"""
    couleurs = {}  # 0 ou 1
    
    def bfs_coloration(sommet_depart):
        file = deque([sommet_depart])
        couleurs[sommet_depart] = 0
        
        while file:
            sommet = file.popleft()
            couleur_actuelle = couleurs[sommet]
            
            for voisin, _ in graphe.voisins(sommet):
                if voisin not in couleurs:
                    # Colorier avec la couleur opposée
                    couleurs[voisin] = 1 - couleur_actuelle
                    file.append(voisin)
                elif couleurs[voisin] == couleur_actuelle:
                    # Conflit de couleur = pas bipartite
                    return False
        
        return True
    
    # Tester chaque composante connexe
    for sommet in graphe.liste_sommets():
        if sommet not in couleurs:
            if not bfs_coloration(sommet):
                return False
    
    return True

def planifier_taches(taches_dependances):
    """Ordonne des tâches selon leurs dépendances"""
    # Créer un graphe orienté des dépendances
    graphe = GrapheListe(oriente=True)
    
    # Ajouter toutes les tâches
    for tache, deps in taches_dependances.items():
        graphe.ajouter_sommet(tache)
        for dep in deps:
            graphe.ajouter_sommet(dep)
            # dep doit être fait avant tache
            graphe.ajouter_arete(dep, tache)
    
    try:
        # Tri topologique pour obtenir l'ordre
        return tri_topologique(graphe)
    except ValueError as e:
        return f"Erreur: {e}"

# Tests des applications
if __name__ == "__main__":
    # Test du labyrinthe
    labyrinthe = [
        ['.', '.', '#', '.', '.'],
        ['.', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.']
    ]
    
    chemin = resoudre_labyrinthe(labyrinthe, (0, 0), (4, 4))
    print(f"Chemin dans le labyrinthe: {chemin}")
    
    # Test des îles
    grille_iles = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    
    nb_iles = compter_iles(grille_iles)
    print(f"Nombre d'îles: {nb_iles}")
    
    # Test de bipartition
    g_bipartite = GrapheListe(oriente=False)
    g_bipartite.ajouter_arete('A', 'X')
    g_bipartite.ajouter_arete('A', 'Y')
    g_bipartite.ajouter_arete('B', 'X')
    g_bipartite.ajouter_arete('B', 'Z')
    
    print(f"Graphe bipartite: {est_bipartite(g_bipartite)}")
    
    # Test de planification
    taches = {
        'cuisiner': ['acheter', 'laver'],
        'acheter': [],
        'laver': ['acheter'],
        'manger': ['cuisiner'],
        'nettoyer': ['manger']
    }
    
    ordre = planifier_taches(taches)
    print(f"Ordre des tâches: {ordre}")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

</div>

<script>
function toggleSolution(button) {
    const solutionWrapper = button.parentElement.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.style.display === 'none' || !solutionWrapper.style.display) {
        // Créer et afficher la modal
        const modal = document.createElement('div');
        modal.className = 'solution-modal';
        modal.innerHTML = `
            <div class="solution-content">
                <span class="solution-close" onclick="closeSolutionModal()">&times;</span>
                ${solutionWrapper.innerHTML}
            </div>
        `;
        
        document.body.appendChild(modal);
        modal.style.display = 'block';
        
        // Changer l'apparence du bouton
        arrow.textContent = '↓';
        button.style.backgroundColor = '#e8f5e8';
        button.style.borderColor = '#4CAF50';
    }
}

function closeSolutionModal() {
    const modal = document.querySelector('.solution-modal');
    if (modal) {
        modal.remove();
    }
    
    // Remettre tous les boutons à leur état initial
    const buttons = document.querySelectorAll('.toggle-solution');
    buttons.forEach(btn => {
        const arrow = btn.querySelector('.arrow');
        arrow.textContent = '→';
        btn.style.backgroundColor = '';
        btn.style.borderColor = '';
    });
}

// Fermer la modal avec Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeSolutionModal();
    }
});

function showSection(sectionId) {
    // Cacher toutes les sections
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    
    // Afficher la section sélectionnée
    const targetSection = document.getElementById(sectionId + '-section');
    if (targetSection) {
        targetSection.style.display = 'block';
    }
    
    // Mettre à jour les onglets
    const tabs = document.querySelectorAll('.section-tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    const activeTab = document.querySelector(`[onclick="showSection('${sectionId}')"]`);
    if (activeTab) {
        activeTab.classList.add('active');
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    showSection('decouverte');
});
</script>

</body>
</html>