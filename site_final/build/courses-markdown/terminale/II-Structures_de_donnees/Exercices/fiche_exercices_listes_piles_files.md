# Fiche d'exercices : Listes, Piles et Files

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
    <button class="section-tab" onclick="showSection('implementation-section')">🔧 Implémentation</button>
    <button class="section-tab" onclick="showSection('application-section')">🚀 Applications</button>
    <button class="section-tab" onclick="showSection('expert-section')">🏆 Expert</button>
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
                    <li>Respectez les interfaces définies (noms des méthodes, paramètres)</li>
                    <li>Testez vos implémentations avec plusieurs cas de test</li>
                    <li>Gérez les cas d'erreur (pile vide, indice invalide, etc.)</li>
                    <li>Commentez votre code pour expliquer les choix d'implémentation</li>
                    <li>Analysez la complexité temporelle de vos solutions</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Découverte 🌱</div>
            <h4 class="exercise-title">Interface d'une pile</h4>
            <div class="exercise-content">
                <p>Définissez l'interface d'une pile en listant toutes les opérations nécessaires avec leur signature et leur comportement attendu.</p>
                <p><strong>Questions :</strong></p>
                <ol>
                    <li>Quelles sont les opérations essentielles d'une pile ?</li>
                    <li>Que se passe-t-il si on essaie de dépiler une pile vide ?</li>
                    <li>Donnez un exemple d'utilisation concrète des piles.</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Interface d'une pile :</h4>
                <pre><code class="language-python"># Interface d'une pile
class Pile:
    def __init__(self):
        """Crée une pile vide"""
        pass
    
    def est_vide(self):
        """Retourne True si la pile est vide, False sinon"""
        pass
    
    def empiler(self, element):
        """Ajoute un élément au sommet de la pile"""
        pass
    
    def depiler(self):
        """Retire et retourne l'élément du sommet
        Lève une exception si la pile est vide"""
        pass
    
    def sommet(self):
        """Retourne l'élément du sommet sans le retirer
        Lève une exception si la pile est vide"""
        pass
    
    def taille(self):
        """Retourne le nombre d'éléments dans la pile"""
        pass</code></pre>
                <p><strong>Réponses :</strong></p>
                <ol>
                    <li>Opérations essentielles : empiler, dépiler, est_vide, sommet</li>
                    <li>Lever une exception (IndexError ou exception personnalisée)</li>
                    <li>Exemples : pile d'exécution, évaluation d'expressions, annulation d'opérations</li>
                </ol>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Découverte 🌱</div>
            <h4 class="exercise-title">Principe FIFO vs LIFO</h4>
            <div class="exercise-content">
                <p>Expliquez la différence entre les principes FIFO et LIFO avec des exemples concrets.</p>
                <p><strong>Exercice :</strong> Simulez manuellement les opérations suivantes :</p>
                <ol>
                    <li>Pile : empiler(1), empiler(2), empiler(3), dépiler(), dépiler()</li>
                    <li>File : enfiler(1), enfiler(2), enfiler(3), défiler(), défiler()</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>FIFO vs LIFO :</h4>
                <ul>
                    <li><strong>LIFO (Last In, First Out)</strong> : Le dernier arrivé est le premier servi
                        <br>Exemple : pile d'assiettes, pile d'exécution</li>
                    <li><strong>FIFO (First In, First Out)</strong> : Le premier arrivé est le premier servi
                        <br>Exemple : file d'attente, gestion des processus</li>
                </ul>
                
                <h4>Simulation :</h4>
                <pre><code># Pile (LIFO)
État initial : []
empiler(1) : [1]
empiler(2) : [1, 2]
empiler(3) : [1, 2, 3]
dépiler() : [1, 2] (retourne 3)
dépiler() : [1] (retourne 2)

# File (FIFO)
État initial : []
enfiler(1) : [1]
enfiler(2) : [1, 2]
enfiler(3) : [1, 2, 3]
défiler() : [2, 3] (retourne 1)
défiler() : [3] (retourne 2)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🟢</div>
            <h4 class="exercise-title">Vérification de parenthèses</h4>
            <div class="exercise-content">
                <p>Implémentez une fonction qui vérifie si les parenthèses sont équilibrées dans une expression.</p>
                <p><strong>Exemples :</strong></p>
                <ul>
                    <li><code>"(())"</code> → True</li>
                    <li><code>"(()"</code> → False</li>
                    <li><code>")()"</code> → False</li>
                    <li><code>"([{}])"</code> → True</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def parentheses_equilibrees(expression):
    """Vérifie si les parenthèses sont équilibrées"""
    pile = []
    correspondances = {'(': ')', '[': ']', '{': '}'}
    
    for caractere in expression:
        if caractere in correspondances:  # Parenthèse ouvrante
            pile.append(caractere)
        elif caractere in correspondances.values():  # Parenthèse fermante
            if not pile:  # Pile vide
                return False
            ouvrante = pile.pop()
            if correspondances[ouvrante] != caractere:
                return False
    
    return len(pile) == 0  # Pile doit être vide

# Tests
print(parentheses_equilibrees("(())"))     # True
print(parentheses_equilibrees("(()"))      # False
print(parentheses_equilibrees(")())"))     # False
print(parentheses_equilibrees("([{}])"))   # True
print(parentheses_equilibrees("([)]"))     # False</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="implementation-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Implémentation d'une pile avec liste</h4>
            <div class="exercise-content">
                <p>Implémentez une classe <code>Pile</code> en utilisant une liste Python comme structure de données sous-jacente.</p>
                <p><strong>Méthodes à implémenter :</strong></p>
                <ul>
                    <li><code>__init__()</code> : constructeur</li>
                    <li><code>est_vide()</code> : teste si la pile est vide</li>
                    <li><code>empiler(element)</code> : ajoute un élément</li>
                    <li><code>depiler()</code> : retire et retourne l'élément du sommet</li>
                    <li><code>sommet()</code> : consulte l'élément du sommet</li>
                    <li><code>taille()</code> : retourne le nombre d'éléments</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.elements = []
    
    def est_vide(self):
        """Retourne True si la pile est vide"""
        return len(self.elements) == 0
    
    def empiler(self, element):
        """Ajoute un élément au sommet de la pile"""
        self.elements.append(element)
    
    def depiler(self):
        """Retire et retourne l'élément du sommet"""
        if self.est_vide():
            raise IndexError("Impossible de dépiler : pile vide")
        return self.elements.pop()
    
    def sommet(self):
        """Retourne l'élément du sommet sans le retirer"""
        if self.est_vide():
            raise IndexError("Impossible de consulter : pile vide")
        return self.elements[-1]
    
    def taille(self):
        """Retourne le nombre d'éléments dans la pile"""
        return len(self.elements)
    
    def __str__(self):
        """Représentation textuelle de la pile"""
        return f"Pile({self.elements})"

# Test de l'implémentation
pile = Pile()
print(f"Pile vide : {pile.est_vide()}")  # True

pile.empiler(1)
pile.empiler(2)
pile.empiler(3)
print(f"Pile : {pile}")  # Pile([1, 2, 3])
print(f"Sommet : {pile.sommet()}")  # 3
print(f"Taille : {pile.taille()}")  # 3

print(f"Dépiler : {pile.depiler()}")  # 3
print(f"Pile : {pile}")  # Pile([1, 2])</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Implémentation d'une file avec liste</h4>
            <div class="exercise-content">
                <p>Implémentez une classe <code>File</code> en utilisant une liste Python.</p>
                <p><strong>Attention :</strong> Réfléchissez à l'efficacité de votre implémentation. La méthode <code>pop(0)</code> a une complexité O(n).</p>
                <p><strong>Bonus :</strong> Proposez une implémentation optimisée avec deux indices.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Version simple (inefficace)
class FileSimple:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def enfiler(self, element):
        """Ajoute un élément à la file - O(1)"""
        self.buffer[self.fin] = element
        
        if self.est_pleine():
            # File pleine : avancer le début (écrasement)
            self.debut = (self.debut + 1) % self.taille_max
        else:
            self.taille += 1
        
        self.fin = (self.fin + 1) % self.taille_max
    
    def defiler(self):
        """Retire et retourne le premier élément - O(1)"""
        if self.est_vide():
            raise IndexError("File vide")
        
        element = self.buffer[self.debut]
        self.buffer[self.debut] = None  # Nettoyage optionnel
        self.debut = (self.debut + 1) % self.taille_max
        self.taille -= 1
        
        return element
    
    def premier(self):
        """Retourne le premier élément sans le retirer - O(1)"""
        if self.est_vide():
            raise IndexError("File vide")
        return self.buffer[self.debut]
    
    def dernier(self):
        """Retourne le dernier élément sans le retirer - O(1)"""
        if self.est_vide():
            raise IndexError("File vide")
        index_dernier = (self.fin - 1) % self.taille_max
        return self.buffer[index_dernier]
    
    def taille_actuelle(self):
        """Retourne le nombre d'éléments actuels - O(1)"""
        return self.taille
    
    def capacite(self):
        """Retourne la capacité maximale - O(1)"""
        return self.taille_max
    
    def to_list(self):
        """Convertit la file en liste (pour affichage) - O(n)"""
        if self.est_vide():
            return []
        
        result = []
        index = self.debut
        for _ in range(self.taille):
            result.append(self.buffer[index])
            index = (index + 1) % self.taille_max
        
        return result
    
    def __str__(self):
        return f"FileCirculaire({self.to_list()}) [{self.taille}/{self.taille_max}]"

# Tests de la file circulaire
if __name__ == "__main__":
    print("=== Test File Circulaire ===")
    file = FileCirculaire(3)
    
    # Remplissage normal
    for i in range(1, 4):
        file.enfiler(i)
        print(f"Enfiler {i}: {file}")
    
    print(f"File pleine: {file.est_pleine()}")
    
    # Écrasement (file pleine)
    file.enfiler(4)
    print(f"Enfiler 4 (écrasement): {file}")
    
    file.enfiler(5)
    print(f"Enfiler 5 (écrasement): {file}")
    
    # Défilement
    while not file.est_vide():
        val = file.defiler()
        print(f"Défiler {val}: {file}")

# Application : Cache LRU simple
class CacheLRU:
    def __init__(self, capacite):
        self.capacite = capacite
        self.cache = {}  # clé -> valeur
        self.ordre = FileCirculaire(capacite)  # Ordre d'accès
    
    def get(self, cle):
        if cle in self.cache:
            # Marquer comme récemment utilisé
            self.ordre.enfiler(cle)
            return self.cache[cle]
        return None
    
    def put(self, cle, valeur):
        if len(self.cache) >= self.capacite and cle not in self.cache:
            # Supprimer l'élément le moins récemment utilisé
            if not self.ordre.est_vide():
                ancienne_cle = self.ordre.defiler()
                if ancienne_cle in self.cache:
                    del self.cache[ancienne_cle]
        
        self.cache[cle] = valeur
        self.ordre.enfiler(cle)
    
    def __str__(self):
        return f"Cache: {self.cache}, Ordre: {self.ordre.to_list()}"

# Test du cache LRU
cache = CacheLRU(2)
cache.put("a", 1)
cache.put("b", 2)
print(f"Cache après insertion: {cache}")
print(f"Get 'a': {cache.get('a')}")
cache.put("c", 3)  # Devrait évincer 'b'
print(f"Cache après insertion 'c': {cache}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">Expert 🟣</div>
            <h4 class="exercise-title">Déque (Double-ended queue)</h4>
            <div class="exercise-content">
                <p>Implémentez une structure de données Deque qui permet l'insertion et la suppression aux deux extrémités en O(1).</p>
                <p><strong>Méthodes :</strong> <code>ajouter_debut</code>, <code>ajouter_fin</code>, <code>supprimer_debut</code>, <code>supprimer_fin</code></p>
                <p><strong>Bonus :</strong> Implémentez avec une liste doublement chaînée.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class NoeudDouble:
    def __init__(self, valeur, precedent=None, suivant=None):
        self.valeur = valeur
        self.precedent = precedent
        self.suivant = suivant

class Deque:
    def __init__(self):
        """Crée une deque vide"""
        self.tete = None
        self.queue = None
        self._taille = 0
    
    def est_vide(self):
        return self._taille == 0
    
    def taille(self):
        return self._taille
    
    def ajouter_debut(self, valeur):
        """Ajoute un élément au début - O(1)"""
        nouveau = NoeudDouble(valeur)
        
        if self.est_vide():
            self.tete = self.queue = nouveau
        else:
            nouveau.suivant = self.tete
            self.tete.precedent = nouveau
            self.tete = nouveau
        
        self._taille += 1
    
    def ajouter_fin(self, valeur):
        """Ajoute un élément à la fin - O(1)"""
        nouveau = NoeudDouble(valeur)
        
        if self.est_vide():
            self.tete = self.queue = nouveau
        else:
            nouveau.precedent = self.queue
            self.queue.suivant = nouveau
            self.queue = nouveau
        
        self._taille += 1
    
    def supprimer_debut(self):
        """Supprime et retourne l'élément du début - O(1)"""
        if self.est_vide():
            raise IndexError("Deque vide")
        
        valeur = self.tete.valeur
        
        if self._taille == 1:
            self.tete = self.queue = None
        else:
            self.tete = self.tete.suivant
            self.tete.precedent = None
        
        self._taille -= 1
        return valeur
    
    def supprimer_fin(self):
        """Supprime et retourne l'élément de la fin - O(1)"""
        if self.est_vide():
            raise IndexError("Deque vide")
        
        valeur = self.queue.valeur
        
        if self._taille == 1:
            self.tete = self.queue = None
        else:
            self.queue = self.queue.precedent
            self.queue.suivant = None
        
        self._taille -= 1
        return valeur
    
    def premier(self):
        """Retourne l'élément du début sans le supprimer"""
        if self.est_vide():
            raise IndexError("Deque vide")
        return self.tete.valeur
    
    def dernier(self):
        """Retourne l'élément de la fin sans le supprimer"""
        if self.est_vide():
            raise IndexError("Deque vide")
        return self.queue.valeur
    
    def to_list(self):
        """Convertit en liste pour affichage"""
        result = []
        courant = self.tete
        while courant:
            result.append(courant.valeur)
            courant = courant.suivant
        return result
    
    def __str__(self):
        return f"Deque({self.to_list()})"

# Application : Palindrome checker
def est_palindrome(texte):
    """Vérifie si un texte est un palindrome en utilisant une deque"""
    deque = Deque()
    
    # Nettoyer le texte et l'ajouter à la deque
    texte_propre = ''.join(c.lower() for c in texte if c.isalnum())
    for char in texte_propre:
        deque.ajouter_fin(char)
    
    # Comparer les extrémités
    while deque.taille() > 1:
        if deque.supprimer_debut() != deque.supprimer_fin():
            return False
    
    return True

# Tests
if __name__ == "__main__":
    print("=== Test Deque ===")
    deque = Deque()
    
    # Test des ajouts
    deque.ajouter_debut(2)
    deque.ajouter_debut(1)
    deque.ajouter_fin(3)
    deque.ajouter_fin(4)
    print(f"Après ajouts: {deque}")  # [1, 2, 3, 4]
    
    # Test des suppressions
    print(f"Supprimer début: {deque.supprimer_debut()}")  # 1
    print(f"Supprimer fin: {deque.supprimer_fin()}")      # 4
    print(f"Deque: {deque}")  # [2, 3]
    
    # Test palindromes
    print("\n=== Test Palindromes ===")
    tests = ["radar", "A man a plan a canal Panama", "race a car", "hello"]
    for test in tests:
        print(f"'{test}' est palindrome: {est_palindrome(test)}")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>(self, element):
        self.elements.append(element)  # O(1)
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("Impossible de défiler : file vide")
        return self.elements.pop(0)  # O(n) - inefficace !
    
    def premier(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[0]

# Version optimisée avec deux indices
class File:
    def __init__(self):
        self.elements = []
        self.debut = 0
    
    def est_vide(self):
        return self.debut >= len(self.elements)
    
    def enfiler(self, element):
        self.elements.append(element)  # O(1)
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("Impossible de défiler : file vide")
        
        element = self.elements[self.debut]
        self.debut += 1
        
        # Réorganisation périodique pour éviter la croissance infinie
        if self.debut > len(self.elements) // 2:
            self.elements = self.elements[self.debut:]
            self.debut = 0
        
        return element  # O(1) amorti
    
    def premier(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self.elements[self.debut]
    
    def taille(self):
        return len(self.elements) - self.debut

# Test
file = File()
file.enfiler(1)
file.enfiler(2)
file.enfiler(3)
print(file.defiler())  # 1
print(file.defiler())  # 2
file.enfiler(4)
print(file.defiler())  # 3
print(file.defiler())  # 4</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Liste chaînée</h4>
            <div class="exercise-content">
                <p>Implémentez une liste chaînée avec les opérations de base.</p>
                <p><strong>Classes à créer :</strong></p>
                <ul>
                    <li><code>Noeud</code> : représente un élément de la liste</li>
                    <li><code>ListeChainee</code> : la structure de données</li>
                </ul>
                <p><strong>Méthodes :</strong> <code>inserer_debut</code>, <code>inserer_fin</code>, <code>supprimer</code>, <code>rechercher</code>, <code>afficher</code></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
    
    def __str__(self):
        return str(self.valeur)

class ListeChainee:
    def __init__(self):
        self.tete = None
        self._taille = 0
    
    def est_vide(self):
        return self.tete is None
    
    def taille(self):
        return self._taille
    
    def inserer_debut(self, valeur):
        """Insère un élément au début de la liste - O(1)"""
        nouveau_noeud = Noeud(valeur, self.tete)
        self.tete = nouveau_noeud
        self._taille += 1
    
    def inserer_fin(self, valeur):
        """Insère un élément à la fin de la liste - O(n)"""
        nouveau_noeud = Noeud(valeur)
        
        if self.est_vide():
            self.tete = nouveau_noeud
        else:
            courant = self.tete
            while courant.suivant is not None:
                courant = courant.suivant
            courant.suivant = nouveau_noeud
        
        self._taille += 1
    
    def supprimer(self, valeur):
        """Supprime la première occurrence d'une valeur - O(n)"""
        if self.est_vide():
            return False
        
        # Cas particulier : suppression en tête
        if self.tete.valeur == valeur:
            self.tete = self.tete.suivant
            self._taille -= 1
            return True
        
        # Recherche dans le reste de la liste
        courant = self.tete
        while courant.suivant is not None:
            if courant.suivant.valeur == valeur:
                courant.suivant = courant.suivant.suivant
                self._taille -= 1
                return True
            courant = courant.suivant
        
        return False  # Valeur non trouvée
    
    def rechercher(self, valeur):
        """Recherche une valeur dans la liste - O(n)"""
        courant = self.tete
        position = 0
        
        while courant is not None:
            if courant.valeur == valeur:
                return position
            courant = courant.suivant
            position += 1
        
        return -1  # Non trouvé
    
    def afficher(self):
        """Affiche tous les éléments de la liste"""
        elements = []
        courant = self.tete
        
        while courant is not None:
            elements.append(str(courant.valeur))
            courant = courant.suivant
        
        return " -> ".join(elements) + " -> None"
    
    def __str__(self):
        return self.afficher()

# Test de la liste chaînée
liste = ListeChainee()
liste.inserer_debut(1)
liste.inserer_debut(2)
liste.inserer_fin(3)
print(liste)  # 2 -> 1 -> 3 -> None

print(f"Recherche 1 : position {liste.rechercher(1)}")  # 1
print(f"Suppression de 1 : {liste.supprimer(1)}")  # True
print(liste)  # 2 -> 3 -> None</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="application-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Évaluation d'expression postfixe</h4>
            <div class="exercise-content">
                <p>Implémentez un évaluateur d'expressions en notation postfixe (polonaise inverse) en utilisant une pile.</p>
                <p><strong>Exemple :</strong> <code>"3 4 + 2 *"</code> = <code>(3 + 4) * 2 = 14</code></p>
                <p><strong>Opérateurs supportés :</strong> +, -, *, /</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def evaluer_postfixe(expression):
    """Évalue une expression en notation postfixe"""
    pile = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            # Opérateur : dépiler deux opérandes
            if len(pile) < 2:
                raise ValueError("Expression invalide : pas assez d'opérandes")
            
            b = pile.pop()  # Deuxième opérande
            a = pile.pop()  # Premier opérande
            
            # Calculer le résultat selon l'opérateur
            if token == '+':
                resultat = a + b
            elif token == '-':
                resultat = a - b
            elif token == '*':
                resultat = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division par zéro")
                resultat = a / b
            
            pile.append(resultat)
        else:
            # Nombre : empiler
            try:
                nombre = float(token)
                pile.append(nombre)
            except ValueError:
                raise ValueError(f"Token invalide : {token}")
    
    # À la fin, il doit rester exactement un élément
    if len(pile) != 1:
        raise ValueError("Expression invalide")
    
    return pile[0]

# Tests
print(evaluer_postfixe("3 4 +"))        # 7.0
print(evaluer_postfixe("3 4 + 2 *"))    # 14.0
print(evaluer_postfixe("15 7 1 1 + - / 3 * 2 1 1 + + -"))  # 5.0
print(evaluer_postfixe("5 1 2 + 4 * + 3 -"))  # 14.0

# Fonction bonus : conversion infixe vers postfixe
def infixe_vers_postfixe(expression):
    """Convertit une expression infixe en postfixe (algorithme Shunting Yard)"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    pile_operateurs = []
    sortie = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.replace('.', '').replace('-', '').isdigit():
            # Nombre
            sortie.append(token)
        elif token in precedence:
            # Opérateur
            while (pile_operateurs and 
                   pile_operateurs[-1] != '(' and
                   pile_operateurs[-1] in precedence and
                   precedence[pile_operateurs[-1]] >= precedence[token]):
                sortie.append(pile_operateurs.pop())
            pile_operateurs.append(token)
        elif token == '(':
            pile_operateurs.append(token)
        elif token == ')':
            while pile_operateurs and pile_operateurs[-1] != '(':
                sortie.append(pile_operateurs.pop())
            pile_operateurs.pop()  # Enlever la parenthèse ouvrante
    
    while pile_operateurs:
        sortie.append(pile_operateurs.pop())
    
    return ' '.join(sortie)

# Test de conversion
expression_infixe = "(3 + 4) * 2"
expression_postfixe = infixe_vers_postfixe(expression_infixe)
print(f"Infixe : {expression_infixe}")
print(f"Postfixe : {expression_postfixe}")
print(f"Résultat : {evaluer_postfixe(expression_postfixe)}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Simulation de file d'attente</h4>
            <div class="exercise-content">
                <p>Simulez une file d'attente dans un magasin avec les fonctionnalités suivantes :</p>
                <ul>
                    <li>Arrivée de clients (avec nom et heure d'arrivée)</li>
                    <li>Service d'un client (temps de service variable)</li>
                    <li>Affichage de l'état de la file</li>
                    <li>Calcul du temps d'attente moyen</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">import time
from collections import deque

class Client:
    def __init__(self, nom, heure_arrivee):
        self.nom = nom
        self.heure_arrivee = heure_arrivee
        self.heure_service = None
        self.temps_attente = None
    
    def __str__(self):
        return f"{self.nom} (arrivé à {self.heure_arrivee:.1f}s)"

class FileAttente:
    def __init__(self):
        self.file = deque()
        self.clients_servis = []
        self.temps_debut = time.time()
    
    def temps_actuel(self):
        return time.time() - self.temps_debut
    
    def arrivee_client(self, nom):
        """Un nouveau client arrive"""
        client = Client(nom, self.temps_actuel())
        self.file.append(client)
        print(f"🚶 {client.nom} arrive (file: {len(self.file)} personnes)")
    
    def servir_client(self, temps_service=2.0):
        """Sert le prochain client"""
        if not self.file:
            print("❌ Aucun client à servir")
            return None
        
        client = self.file.popleft()
        client.heure_service = self.temps_actuel()
        client.temps_attente = client.heure_service - client.heure_arrivee
        
        self.clients_servis.append(client)
        
        print(f"✅ Service de {client.nom} (attente: {client.temps_attente:.1f}s)")
        
        # Simuler le temps de service
        time.sleep(temps_service)
        
        return client
    
    def afficher_etat(self):
        """Affiche l'état actuel de la file"""
        print(f"\n📊 État de la file à {self.temps_actuel():.1f}s:")
        print(f"   En attente: {len(self.file)} clients")
        
        if self.file:
            print("   File d'attente:")
            for i, client in enumerate(self.file):
                attente_actuelle = self.temps_actuel() - client.heure_arrivee
                print(f"     {i+1}. {client} (attente actuelle: {attente_actuelle:.1f}s)")
        
        print(f"   Clients servis: {len(self.clients_servis)}")
        
        if self.clients_servis:
            temps_attente_moyen = sum(c.temps_attente for c in self.clients_servis) / len(self.clients_servis)
            print(f"   Temps d'attente moyen: {temps_attente_moyen:.1f}s")
        print()
    
    def statistiques(self):
        """Affiche les statistiques finales"""
        if not self.clients_servis:
            print("Aucun client servi")
            return
        
        temps_attentes = [c.temps_attente for c in self.clients_servis]
        
        print("\n📈 Statistiques finales:")
        print(f"   Clients servis: {len(self.clients_servis)}")
        print(f"   Temps d'attente moyen: {sum(temps_attentes)/len(temps_attentes):.1f}s")
        print(f"   Temps d'attente minimum: {min(temps_attentes):.1f}s")
        print(f"   Temps d'attente maximum: {max(temps_attentes):.1f}s")

# Simulation
if __name__ == "__main__":
    magasin = FileAttente()
    
    # Simulation d'une journée
    magasin.arrivee_client("Alice")
    magasin.arrivee_client("Bob")
    magasin.afficher_etat()
    
    magasin.servir_client(1.0)  # Service rapide
    magasin.arrivee_client("Charlie")
    magasin.afficher_etat()
    
    magasin.servir_client(3.0)  # Service lent
    magasin.servir_client(1.5)
    
    magasin.afficher_etat()
    magasin.statistiques()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Historique de navigation (pile)</h4>
            <div class="exercise-content">
                <p>Implémentez un système d'historique de navigation web avec les fonctionnalités :</p>
                <ul>
                    <li>Visiter une nouvelle page</li>
                    <li>Retour en arrière (bouton "Précédent")</li>
                    <li>Avancer (bouton "Suivant")</li>
                    <li>Affichage de l'historique</li>
                </ul>
                <p><strong>Contrainte :</strong> Utilisez deux piles pour gérer l'historique.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class HistoriqueNavigation:
    def __init__(self):
        self.historique = []  # Pile des pages visitées
        self.futur = []       # Pile des pages "futures" (après retour arrière)
        self.page_actuelle = None
    
    def visiter(self, url):
        """Visite une nouvelle page"""
        if self.page_actuelle is not None:
            self.historique.append(self.page_actuelle)
        
        self.page_actuelle = url
        self.futur.clear()  # Effacer l'historique "futur"
        
        print(f"🌐 Visite de : {url}")
    
    def precedent(self):
        """Retourne à la page précédente"""
        if not self.historique:
            print("❌ Aucune page précédente")
            return False
        
        # Sauvegarder la page actuelle dans le futur
        if self.page_actuelle is not None:
            self.futur.append(self.page_actuelle)
        
        # Récupérer la page précédente
        self.page_actuelle = self.historique.pop()
        
        print(f"⬅️ Retour à : {self.page_actuelle}")
        return True
    
    def suivant(self):
        """Avance vers la page suivante"""
        if not self.futur:
            print("❌ Aucune page suivante")
            return False
        
        # Sauvegarder la page actuelle dans l'historique
        if self.page_actuelle is not None:
            self.historique.append(self.page_actuelle)
        
        # Récupérer la page suivante
        self.page_actuelle = self.futur.pop()
        
        print(f"➡️ Avance vers : {self.page_actuelle}")
        return True
    
    def page_courante(self):
        """Retourne la page actuelle"""
        return self.page_actuelle
    
    def afficher_historique(self):
        """Affiche l'historique complet"""
        print("\n📚 Historique de navigation:")
        
        # Pages précédentes (dans l'ordre chronologique)
        if self.historique:
            print("   Pages précédentes:")
            for i, page in enumerate(reversed(self.historique), 1):
                print(f"     -{i}: {page}")
        
        # Page actuelle
        if self.page_actuelle:
            print(f"   ➤ Actuelle: {self.page_actuelle}")
        
        # Pages futures
        if self.futur:
            print("   Pages suivantes:")
            for i, page in enumerate(reversed(self.futur), 1):
                print(f"     +{i}: {page}")
        
        print()
    
    def peut_reculer(self):
        """Vérifie s'il est possible de reculer"""
        return len(self.historique) > 0
    
    def peut_avancer(self):
        """Vérifie s'il est possible d'avancer"""
        return len(self.futur) > 0

# Simulation d'une session de navigation
if __name__ == "__main__":
    nav = HistoriqueNavigation()
    
    # Simulation de navigation
    nav.visiter("https://www.google.com")
    nav.visiter("https://www.wikipedia.org")
    nav.visiter("https://www.github.com")
    nav.afficher_historique()
    
    # Retours en arrière
    nav.precedent()  # Retour à wikipedia
    nav.precedent()  # Retour à google
    nav.afficher_historique()
    
    # Avancer
    nav.suivant()    # Avance vers wikipedia
    nav.afficher_historique()
    
    # Nouvelle visite (efface l'historique futur)
    nav.visiter("https://www.stackoverflow.com")
    nav.afficher_historique()
    
    # Tests des conditions
    print(f"Peut reculer: {nav.peut_reculer()}")
    print(f"Peut avancer: {nav.peut_avancer()}")
    
    nav.suivant()  # Devrait échouer
    nav.precedent() # Devrait réussir</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="expert-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">Expert 🟣</div>
            <h4 class="exercise-title">Pile avec minimum en O(1)</h4>
            <div class="exercise-content">
                <p>Implémentez une pile qui permet de récupérer l'élément minimum en temps constant O(1).</p>
                <p><strong>Contrainte :</strong> Toutes les opérations (empiler, dépiler, minimum) doivent être en O(1).</p>
                <p><strong>Méthodes :</strong> <code>empiler</code>, <code>depiler</code>, <code>sommet</code>, <code>minimum</code></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class PileAvecMinimum:
    def __init__(self):
        self.pile_principale = []  # Pile des éléments
        self.pile_minimums = []    # Pile des minimums
    
    def est_vide(self):
        return len(self.pile_principale) == 0
    
    def empiler(self, element):
        """Empile un élément - O(1)"""
        self.pile_principale.append(element)
        
        # Mettre à jour la pile des minimums
        if not self.pile_minimums or element <= self.pile_minimums[-1]:
            self.pile_minimums.append(element)
    
    def depiler(self):
        """Dépile un élément - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        
        element = self.pile_principale.pop()
        
        # Mettre à jour la pile des minimums
        if element == self.pile_minimums[-1]:
            self.pile_minimums.pop()
        
        return element
    
    def sommet(self):
        """Retourne l'élément du sommet - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.pile_principale[-1]
    
    def minimum(self):
        """Retourne l'élément minimum - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.pile_minimums[-1]
    
    def taille(self):
        return len(self.pile_principale)
    
    def __str__(self):
        return f"Pile: {self.pile_principale}, Min: {self.pile_minimums}"

# Version alternative avec une seule pile (plus économe en mémoire)
class PileAvecMinimumOptimisee:
    def __init__(self):
        self.pile = []
        self.min_actuel = None
    
    def est_vide(self):
        return len(self.pile) == 0
    
    def empiler(self, element):
        """Empile un élément - O(1)"""
        if self.est_vide():
            self.pile.append(element)
            self.min_actuel = element
        else:
            if element < self.min_actuel:
                # Encoder l'ancien minimum dans la valeur empilée
                self.pile.append(2 * element - self.min_actuel)
                self.min_actuel = element
            else:
                self.pile.append(element)
    
    def depiler(self):
        """Dépile un élément - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        
        element = self.pile.pop()
        
        if element < self.min_actuel:
            # Décoder l'ancien minimum
            ancien_min = self.min_actuel
            self.min_actuel = 2 * self.min_actuel - element
            return ancien_min
        else:
            return element
    
    def sommet(self):
        """Retourne l'élément du sommet - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        
        element = self.pile[-1]
        if element < self.min_actuel:
            return self.min_actuel
        else:
            return element
    
    def minimum(self):
        """Retourne l'élément minimum - O(1)"""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self.min_actuel

# Tests
if __name__ == "__main__":
    print("=== Test Pile avec Minimum (version simple) ===")
    pile = PileAvecMinimum()
    
    # Test d'empilage
    for val in [3, 5, 2, 1, 4]:
        pile.empiler(val)
        print(f"Empiler {val}: {pile}, min = {pile.minimum()}")
    
    print()
    
    # Test de dépilage
    while not pile.est_vide():
        val = pile.depiler()
        min_val = pile.minimum() if not pile.est_vide() else "N/A"
        print(f"Dépiler {val}: {pile}, min = {min_val}")
    
    print("\n=== Test Pile avec Minimum (version optimisée) ===")
    pile_opt = PileAvecMinimumOptimisee()
    
    # Test d'empilage
    for val in [3, 5, 2, 1, 4]:
        pile_opt.empiler(val)
        print(f"Empiler {val}: sommet = {pile_opt.sommet()}, min = {pile_opt.minimum()}")
    
    print()
    
    # Test de dépilage
    while not pile_opt.est_vide():
        val = pile_opt.depiler()
        min_val = pile_opt.minimum() if not pile_opt.est_vide() else "N/A"
        print(f"Dépiler {val}: min = {min_val}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">Expert 🟣</div>
            <h4 class="exercise-title">File circulaire</h4>
            <div class="exercise-content">
                <p>Implémentez une file circulaire (ring buffer) de taille fixe avec les propriétés suivantes :</p>
                <ul>
                    <li>Taille maximale définie à la création</li>
                    <li>Écrasement automatique des anciens éléments si la file est pleine</li>
                    <li>Toutes les opérations en O(1)</li>
                </ul>
                <p><strong>Applications :</strong> Cache, buffer de données, historique limité</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class FileCirculaire:
    def __init__(self, taille_max):
        """Crée une file circulaire de taille maximale donnée"""
        self.taille_max = taille_max
        self.buffer = [None] * taille_max
        self.debut = 0      # Index du premier élément
        self.fin = 0        # Index où insérer le prochain élément
        self.taille = 0     # Nombre d'éléments actuels
        self.pleine = False # Indique si la file a atteint sa capacité max
    
    def est_vide(self):
        """Vérifie si la file est vide - O(1)"""
        return self.taille == 0
    
    def est_pleine(self):
        """Vérifie si la file est pleine - O(1)"""
        return self.taille == self.taille_max
    
    def enfiler