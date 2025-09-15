# Fiche d'exercices : K plus proches voisins (k-NN)

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
    min-height: fit-content;
}

.exercise-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background-color: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.medium {
    background-color: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background-color: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.exercise-title {
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: var(--md-default-fg-color);
}

.exercise-content {
    color: var(--md-default-fg-color--light);
    line-height: 1.5;
    margin-bottom: 1rem;
}

.toggle-solution {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.toggle-solution:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution-wrapper {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
}

.solution-wrapper.show {
    max-height: 2000px;
    margin-top: 1rem;
}

.solution {
    background: rgba(102, 126, 234, 0.05);
    border-radius: 8px;
    padding: 1rem;
    border-left: 3px solid #667eea;
}

.solution pre {
    background: rgba(0, 0, 0, 0.05);
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
    margin: 0;
}

.solution code {
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
}

.data-table {
    border-collapse: collapse;
    width: 100%;
    margin: 1rem 0;
}

.data-table th, .data-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}

.data-table th {
    background-color: #f2f2f2;
    font-weight: bold;
}

.highlight-row {
    background-color: #fff3cd;
}
</style>

## 📚 Partie 1 : Concepts fondamentaux du k-NN

<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 1 - Principe de base</h4>
        <div class="exercise-content">
            <strong>Expliquez le principe de l'algorithme k-NN :</strong><br><br>
            1. Que signifie "k-NN" ?<br>
            2. Comment fonctionne la classification avec k-NN ?<br>
            3. Quelle est la différence entre k=1 et k=5 ?<br>
            4. Pourquoi utilise-t-on généralement un k impair ?<br>
            5. Quels sont les avantages et inconvénients de k-NN ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Explications :</strong><br>
                1. <strong>k-NN :</strong> k-Nearest Neighbors (k plus proches voisins)<br><br>
                2. <strong>Fonctionnement :</strong><br>
                   • Calculer la distance entre le point à classifier et tous les points d'entraînement<br>
                   • Sélectionner les k points les plus proches<br>
                   • Attribuer la classe majoritaire parmi ces k voisins<br><br>
                3. <strong>Différence k=1 vs k=5 :</strong><br>
                   • k=1 : Classification basée sur le voisin le plus proche uniquement<br>
                   • k=5 : Classification basée sur le vote des 5 voisins les plus proches<br><br>
                4. <strong>k impair :</strong> Évite les égalités lors du vote (pas d'ex-aequo)<br><br>
                5. <strong>Avantages :</strong> Simple, pas d'hypothèse sur les données, efficace pour données non-linéaires<br>
                   <strong>Inconvénients :</strong> Coûteux en calcul, sensible aux données aberrantes, nécessite beaucoup de mémoire
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 2 - Calcul de distance</h4>
        <div class="exercise-content">
            <strong>Calculez la distance euclidienne entre ces points :</strong><br><br>
            Point A : (2, 3)<br>
            Point B : (5, 7)<br>
            Point C : (1, 1)<br><br>
            <strong>Questions :</strong><br>
            1. Distance entre A et B<br>
            2. Distance entre A et C<br>
            3. Distance entre B et C<br>
            4. Quel point est le plus proche de A ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Calculs (formule : √[(x₂-x₁)² + (y₂-y₁)²]) :</strong><br><br>
                1. <strong>Distance A-B :</strong><br>
                   √[(5-2)² + (7-3)²] = √[3² + 4²] = √[9 + 16] = √25 = 5<br><br>
                2. <strong>Distance A-C :</strong><br>
                   √[(1-2)² + (1-3)²] = √[(-1)² + (-2)²] = √[1 + 4] = √5 ≈ 2.24<br><br>
                3. <strong>Distance B-C :</strong><br>
                   √[(1-5)² + (1-7)²] = √[(-4)² + (-6)²] = √[16 + 36] = √52 ≈ 7.21<br><br>
                4. <strong>Plus proche de A :</strong> Point C (distance ≈ 2.24)
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 3 - Classification simple</h4>
        <div class="exercise-content">
            <strong>Données d'entraînement (Taille, Poids, Classe) :</strong><br><br>
            <table class="data-table">
                <tr><th>Point</th><th>Taille (cm)</th><th>Poids (kg)</th><th>Classe</th></tr>
                <tr><td>1</td><td>160</td><td>50</td><td>A</td></tr>
                <tr><td>2</td><td>170</td><td>65</td><td>B</td></tr>
                <tr><td>3</td><td>155</td><td>45</td><td>A</td></tr>
                <tr><td>4</td><td>180</td><td>80</td><td>B</td></tr>
                <tr><td>5</td><td>165</td><td>55</td><td>A</td></tr>
            </table><br>
            <strong>Nouveau point à classifier :</strong> (162, 52)<br>
            Utilisez k=3 pour classifier ce point.
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Calcul des distances :</strong><br><br>
                Point à classifier : (162, 52)<br><br>
                <table class="data-table">
                    <tr><th>Point</th><th>Distance</th><th>Classe</th></tr>
                    <tr class="highlight-row"><td>1</td><td>√[(162-160)² + (52-50)²] = √8 ≈ 2.83</td><td>A</td></tr>
                    <tr><td>2</td><td>√[(162-170)² + (52-65)²] = √233 ≈ 15.26</td><td>B</td></tr>
                    <tr class="highlight-row"><td>3</td><td>√[(162-155)² + (52-45)²] = √98 ≈ 9.90</td><td>A</td></tr>
                    <tr><td>4</td><td>√[(162-180)² + (52-80)²] = √1108 ≈ 33.29</td><td>B</td></tr>
                    <tr class="highlight-row"><td>5</td><td>√[(162-165)² + (52-55)²] = √18 ≈ 4.24</td><td>A</td></tr>
                </table><br>
                <strong>3 plus proches voisins :</strong> Points 1, 5, 3<br>
                <strong>Classes :</strong> A, A, A<br>
                <strong>Classification :</strong> Classe A (vote unanime)
            </div>
        </div>
    </div>
</div>

## 📚 Partie 2 : Implémentation en Python

<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 4 - Fonction de distance</h4>
        <div class="exercise-content">
            <strong>Implémentez une fonction qui calcule la distance euclidienne :</strong><br><br>
            <pre>
def distance_euclidienne(point1, point2):
    """
    Calcule la distance euclidienne entre deux points
    point1 et point2 sont des listes [x, y]
    """
    # À compléter
    pass
            </pre><br>
            <strong>Testez avec :</strong><br>
            • distance_euclidienne([0, 0], [3, 4]) → doit retourner 5.0<br>
            • distance_euclidienne([1, 1], [4, 5]) → doit retourner 5.0
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Implémentation :</strong><br>
                <pre>
import math

def distance_euclidienne(point1, point2):
    """
    Calcule la distance euclidienne entre deux points
    point1 et point2 sont des listes [x, y]
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Tests
print(distance_euclidienne([0, 0], [3, 4]))  # 5.0
print(distance_euclidienne([1, 1], [4, 5]))  # 5.0
                </pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 5 - Trouver les k plus proches voisins</h4>
        <div class="exercise-content">
            <strong>Implémentez une fonction qui trouve les k plus proches voisins :</strong><br><br>
            <pre>
def k_plus_proches_voisins(point_test, donnees_entrainement, k):
    """
    Trouve les k plus proches voisins d'un point
    point_test : [x, y]
    donnees_entrainement : liste de [x, y, classe]
    k : nombre de voisins à retourner
    """
    # À compléter
    pass
            </pre>
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Implémentation :</strong><br>
                <pre>
def k_plus_proches_voisins(point_test, donnees_entrainement, k):
    """
    Trouve les k plus proches voisins d'un point
    point_test : [x, y]
    donnees_entrainement : liste de [x, y, classe]
    k : nombre de voisins à retourner
    """
    distances = []
    
    # Calculer la distance pour chaque point d'entraînement
    for donnee in donnees_entrainement:
        point_entrainement = [donnee[0], donnee[1]]
        classe = donnee[2]
        dist = distance_euclidienne(point_test, point_entrainement)
        distances.append((dist, classe, donnee))
    
    # Trier par distance croissante
    distances.sort(key=lambda x: x[0])
    
    # Retourner les k premiers
    return distances[:k]

# Exemple d'utilisation
donnees = [[160, 50, 'A'], [170, 65, 'B'], [155, 45, 'A']]
voisins = k_plus_proches_voisins([162, 52], donnees, 2)
print(voisins)
                </pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 6 - Algorithme k-NN complet</h4>
        <div class="exercise-content">
            <strong>Implémentez l'algorithme k-NN complet :</strong><br><br>
            <pre>
def classifier_knn(point_test, donnees_entrainement, k):
    """
    Classifie un point avec l'algorithme k-NN
    Retourne la classe prédite
    """
    # À compléter
    pass

def evaluer_knn(donnees_test, donnees_entrainement, k):
    """
    Évalue la précision de l'algorithme k-NN
    Retourne le pourcentage de bonnes classifications
    """
    # À compléter
    pass
            </pre>
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Implémentation complète :</strong><br>
                <pre>
def classifier_knn(point_test, donnees_entrainement, k):
    """
    Classifie un point avec l'algorithme k-NN
    Retourne la classe prédite
    """
    # Trouver les k plus proches voisins
    voisins = k_plus_proches_voisins(point_test, donnees_entrainement, k)
    
    # Compter les votes pour chaque classe
    votes = {}
    for distance, classe, donnee in voisins:
        if classe in votes:
            votes[classe] += 1
        else:
            votes[classe] = 1
    
    # Retourner la classe avec le plus de votes
    classe_predite = max(votes, key=votes.get)
    return classe_predite

def evaluer_knn(donnees_test, donnees_entrainement, k):
    """
    Évalue la précision de l'algorithme k-NN
    Retourne le pourcentage de bonnes classifications
    """
    bonnes_predictions = 0
    total_predictions = len(donnees_test)
    
    for donnee_test in donnees_test:
        point_test = [donnee_test[0], donnee_test[1]]
        vraie_classe = donnee_test[2]
        
        classe_predite = classifier_knn(point_test, donnees_entrainement, k)
        
        if classe_predite == vraie_classe:
            bonnes_predictions += 1
    
    precision = (bonnes_predictions / total_predictions) * 100
    return precision

# Exemple d'utilisation
entrainement = [[160, 50, 'A'], [170, 65, 'B'], [155, 45, 'A'], 
                [180, 80, 'B'], [165, 55, 'A']]
test = [[162, 52, 'A'], [175, 70, 'B']]

print(f"Précision avec k=3: {evaluer_knn(test, entrainement, 3):.1f}%")
                </pre>
            </div>
        </div>
    </div>
</div>

## 📚 Partie 3 : Applications pratiques

<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 7 - Choix de k optimal</h4>
        <div class="exercise-content">
            <strong>Analysez l'impact de différentes valeurs de k :</strong><br><br>
            Données : 100 points d'entraînement, 2 classes équilibrées<br><br>
            <table class="data-table">
                <tr><th>k</th><th>Précision (%)</th><th>Temps (ms)</th></tr>
                <tr><td>1</td><td>85</td><td>10</td></tr>
                <tr><td>3</td><td>92</td><td>12</td></tr>
                <tr><td>5</td><td>94</td><td>15</td></tr>
                <tr><td>10</td><td>91</td><td>25</td></tr>
                <tr><td>20</td><td>88</td><td>45</td></tr>
                <tr><td>50</td><td>82</td><td>95</td></tr>
            </table><br>
            <strong>Questions :</strong><br>
            1. Quelle valeur de k choisiriez-vous ?<br>
            2. Pourquoi k=1 donne-t-il une précision plus faible ?<br>
            3. Pourquoi k=50 donne-t-il une précision plus faible ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse :</strong><br><br>
                1. <strong>Choix optimal :</strong> k=5 (meilleure précision 94% avec temps raisonnable)<br><br>
                2. <strong>Problème k=1 :</strong><br>
                   • Très sensible au bruit et aux données aberrantes<br>
                   • Pas de lissage, décisions trop locales<br>
                   • Overfitting possible<br><br>
                3. <strong>Problème k=50 :</strong><br>
                   • k trop grand par rapport à la taille des données (50% des données)<br>
                   • Perte de la structure locale des données<br>
                   • Tendance vers la classe majoritaire globale<br>
                   • Underfitting<br><br>
                <strong>Règle générale :</strong> k ≈ √n où n est le nombre de points d'entraînement
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 8 - Système de recommandation</h4>
        <div class="exercise-content">
            <strong>Créez un système de recommandation de films avec k-NN :</strong><br><br>
            <strong>Données utilisateurs (notes sur 5) :</strong><br>
            <table class="data-table">
                <tr><th>Utilisateur</th><th>Action</th><th>Comédie</th><th>Drame</th><th>Sci-Fi</th></tr>
                <tr><td>Alice</td><td>5</td><td>2</td><td>4</td><td>1</td></tr>
                <tr><td>Bob</td><td>1</td><td>5</td><td>2</td><td>4</td></tr>
                <tr><td>Charlie</td><td>4</td><td>3</td><td>5</td><td>2</td></tr>
                <tr><td>Diana</td><td>2</td><td>4</td><td>1</td><td>5</td></tr>
            </table><br>
            <strong>Nouvel utilisateur :</strong> Eve (Action: 4, Comédie: 1, Drame: 5, Sci-Fi: ?)<br>
            Prédisez la note de Eve pour les films Sci-Fi avec k=2.
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Solution :</strong><br><br>
                <strong>1. Calcul des distances (sans Sci-Fi) :</strong><br>
                Eve : [4, 1, 5]<br><br>
                • Alice [5, 2, 4] : √[(4-5)² + (1-2)² + (5-4)²] = √3 ≈ 1.73<br>
                • Bob [1, 5, 2] : √[(4-1)² + (1-5)² + (5-2)²] = √34 ≈ 5.83<br>
                • Charlie [4, 3, 5] : √[(4-4)² + (1-3)² + (5-5)²] = √4 = 2.00<br>
                • Diana [2, 4, 1] : √[(4-2)² + (1-4)² + (5-1)²] = √29 ≈ 5.39<br><br>
                <strong>2. Les 2 plus proches voisins :</strong><br>
                • Alice (distance 1.73, Sci-Fi: 1)<br>
                • Charlie (distance 2.00, Sci-Fi: 2)<br><br>
                <strong>3. Prédiction :</strong><br>
                Moyenne pondérée par l'inverse de la distance :<br>
                Poids Alice = 1/1.73 ≈ 0.58<br>
                Poids Charlie = 1/2.00 = 0.50<br><br>
                Note prédite = (1×0.58 + 2×0.50) / (0.58 + 0.50) ≈ 1.46<br><br>
                <strong>Prédiction pour Eve en Sci-Fi : ≈ 1.5/5</strong>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 9 - Optimisations et variantes</h4>
        <div class="exercise-content">
            <strong>Analysez ces améliorations de l'algorithme k-NN :</strong><br><br>
            1. <strong>k-NN pondéré :</strong> Les voisins plus proches ont plus d'influence<br>
            2. <strong>Normalisation :</strong> Mettre toutes les features à la même échelle<br>
            3. <strong>Distance de Manhattan :</strong> |x₁-x₂| + |y₁-y₂|<br>
            4. <strong>Réduction de dimensionnalité :</strong> PCA avant k-NN<br><br>
            <strong>Questions :</strong><br>
            • Quand utiliser chaque amélioration ?<br>
            • Implémentez la distance de Manhattan<br>
            • Pourquoi normaliser les données ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse des améliorations :</strong><br><br>
                <strong>1. k-NN pondéré :</strong><br>
                • Utilisation : Quand la proximité est très importante<br>
                • Poids = 1/distance ou exp(-distance)<br><br>
                <strong>2. Normalisation :</strong><br>
                • Nécessaire quand les features ont des échelles différentes<br>
                • Exemple : âge (0-100) vs salaire (20000-100000)<br>
                <pre>
def normaliser(donnees):
    # Min-Max normalization
    for i in range(len(donnees[0])-1):  # -1 pour exclure la classe
        valeurs = [point[i] for point in donnees]
        min_val, max_val = min(valeurs), max(valeurs)
        for point in donnees:
            point[i] = (point[i] - min_val) / (max_val - min_val)
    return donnees
                </pre><br>
                <strong>3. Distance de Manhattan :</strong><br>
                <pre>
def distance_manhattan(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))
                </pre>
                • Utilisation : Données avec features indépendantes, moins sensible aux outliers<br><br>
                <strong>4. Réduction de dimensionnalité :</strong><br>
                • Utilisation : Données haute dimension, réduction du bruit
                • Améliore les performances et réduit la malédiction de la dimensionnalité
            </div>
        </div>
    </div>
</div>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices
function toggleSolution(button) {
    const wrapper = button.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (wrapper.classList.contains('show')) {
        wrapper.classList.remove('show');
        arrow.textContent = '→';
        arrow.style.transform = 'rotate(0deg)';
    } else {
        wrapper.classList.add('show');
        arrow.textContent = '↓';
        arrow.style.transform = 'rotate(90deg)';
    }
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Aucune initialisation spécifique nécessaire pour cette fiche
});
</script>