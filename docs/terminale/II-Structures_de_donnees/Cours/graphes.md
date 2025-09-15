<style>
.concept-section {
    margin: 2rem 0;
    padding: 1.5rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-left: 4px solid #007bff;
}

.section-title {
    color: #2c3e50;
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
    text-align: center;
    font-weight: 600;
}

.definition-box {
    background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-left: 4px solid #2196f3;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.definition-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #1565c0;
    margin-bottom: 0.8rem;
}

.definition-content {
    color: #37474f;
    line-height: 1.6;
    font-size: 1rem;
}

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.concept-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border: 1px solid #e0e0e0;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.concept-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.concept-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
    color: #555;
    line-height: 1.6;
    text-align: left;
}

.code-example {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 3px solid #28a745;
}

.code-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: #28a745;
    margin-bottom: 0.5rem;
}

.code-example pre {
    margin: 0;
    background: none;
    padding: 0;
    border: none;
}

.graph-diagram {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
    border: 2px dashed #6c757d;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.comparison-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.comparison-table td {
    padding: 1rem;
    border-bottom: 1px solid #e0e0e0;
    color: #37474f;
}

.comparison-table tr:nth-child(even) {
    background: #f8f9fa;
}

.highlight-fact {
    background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
    border-radius: 8px;
    padding: 1rem;
    margin: 1.5rem 0;
    border-left: 4px solid #ffc107;
    color: #856404;
    font-weight: 500;
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.method-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-left: 4px solid #17a2b8;
}

.method-type {
    font-size: 1.1rem;
    font-weight: 600;
    color: #17a2b8;
    margin-bottom: 1rem;
}

.algorithm-card {
    background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-left: 4px solid #4caf50;
}

.algorithm-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2e7d32;
    margin-bottom: 1rem;
}

@media (max-width: 768px) {
    .concept-grid, .method-grid {
        grid-template-columns: 1fr;
    }
    
    .concept-section {
        padding: 1rem;
    }
    
    .section-title {
        font-size: 1.5rem;
    }
}
</style>

# 🌐 Les Graphes

<div class="concept-section">
    <h2 class="section-title">🎯 Introduction aux Graphes</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Qu'est-ce qu'un graphe ?</div>
        <div class="definition-content">
            Un <strong>graphe</strong> est une structure de données fondamentale qui modélise des <strong>relations entre des objets</strong>. Il constitue l'une des abstractions les plus puissantes en informatique pour représenter des connexions complexes.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔵</div>
            <div class="concept-name">Sommets (Nœuds)</div>
            <div class="concept-description">
                Les <strong>objets</strong> ou <strong>entités</strong> du graphe. Ils représentent les éléments que l'on souhaite connecter.
                <br><br>
                <em>Exemples :</em> Personnes, villes, pages web, ordinateurs...
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Arêtes (Arcs)</div>
            <div class="concept-description">
                Les <strong>relations</strong> ou <strong>connexions</strong> entre les sommets. Elles matérialisent les liens qui unissent les objets.
                <br><br>
                <em>Exemples :</em> Amitiés, routes, liens hypertextes, câbles réseau...
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🌍 <strong>Omniprésence :</strong> Les graphes sont partout en informatique : réseaux sociaux, GPS, Internet, circuits électroniques, intelligence artificielle...
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Types de Graphes</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">↔️</div>
            <div class="concept-name">Graphe Non Orienté</div>
            <div class="concept-description">
                Les arêtes n'ont <strong>pas de direction</strong>. Si A est relié à B, alors B est automatiquement relié à A.
                
                <div class="graph-diagram">
                    <pre>A ---- B
|      |
C ---- D</pre>
                </div>
                
                <em>Exemple :</em> Réseau d'amitié (relation symétrique)
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">➡️</div>
            <div class="concept-name">Graphe Orienté</div>
            <div class="concept-description">
                Les arêtes ont une <strong>direction</strong> précise (représentée par des flèches).
                
                <div class="graph-diagram">
                    <pre>A ---> B
^      |
C <--- D</pre>
                </div>
                
                <em>Exemple :</em> Réseau de followers (relation asymétrique)
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚖️</div>
            <div class="concept-name">Graphe Pondéré</div>
            <div class="concept-description">
                Les arêtes possèdent un <strong>poids</strong> (coût, distance, temps, capacité...).
                
                <div class="graph-diagram">
                    <pre>A --5-- B
|       |
3       2
|       |
C --1-- D</pre>
                </div>
                
                <em>Exemple :</em> Réseau routier avec distances
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💾 Représentations en Mémoire</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Choix de représentation</div>
        <div class="definition-content">
            Le choix de la représentation dépend de la <strong>densité du graphe</strong> et des <strong>opérations les plus fréquentes</strong>. Chaque approche a ses avantages selon le contexte d'utilisation.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📊 Matrice d'Adjacence</div>
            <div class="concept-description">
                Tableau 2D où <code>matrice[i][j]</code> indique s'il y a une arête entre le sommet i et le sommet j.
                
                <div class="code-example">
                    <div class="code-title">💻 Exemple de matrice</div>
                    <pre><code># Graphe A-B-C avec A relié à B et C
matrice = [
    [0, 1, 1],  # A : relié à B(1) et C(2)
    [1, 0, 0],  # B : relié à A(0)
    [1, 0, 0]   # C : relié à A(0)
]</code></pre>
                </div>
                
                <div style="margin-top: 1rem;">
                    <strong style="color: #28a745;">✅ Avantages :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Vérification d'adjacence en O(1)</li>
                        <li>Simple à implémenter</li>
                        <li>Idéal pour les graphes denses</li>
                    </ul>
                    
                    <strong style="color: #dc3545;">❌ Inconvénients :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Espace O(n²) même pour graphes peu denses</li>
                        <li>Parcours des voisins en O(n)</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">📋 Liste d'Adjacence</div>
            <div class="concept-description">
                Chaque sommet maintient une liste de ses voisins directs.
                
                <div class="code-example">
                    <div class="code-title">💻 Exemple de liste</div>
                    <pre><code># Même graphe en liste d'adjacence
graphe = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}</code></pre>
                </div>
                
                <div style="margin-top: 1rem;">
                    <strong style="color: #28a745;">✅ Avantages :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Espace O(n + m) où m = nombre d'arêtes</li>
                        <li>Parcours des voisins efficace</li>
                        <li>Idéal pour les graphes peu denses</li>
                    </ul>
                    
                    <strong style="color: #dc3545;">❌ Inconvénients :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Vérification d'adjacence en O(degré)</li>
                        <li>Plus complexe à implémenter</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Opération</th>
                <th>Matrice d'Adjacence</th>
                <th>Liste d'Adjacence</th>
                <th>Recommandation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Vérifier adjacence</td>
                <td>O(1)</td>
                <td>O(degré)</td>
                <td>Matrice pour fréquent</td>
            </tr>
            <tr>
                <td>Parcourir voisins</td>
                <td>O(n)</td>
                <td>O(degré)</td>
                <td>Liste plus efficace</td>
            </tr>
            <tr>
                <td>Espace mémoire</td>
                <td>O(n²)</td>
                <td>O(n + m)</td>
                <td>Liste pour graphes peu denses</td>
            </tr>
            <tr>
                <td>Ajouter arête</td>
                <td>O(1)</td>
                <td>O(1)</td>
                <td>Équivalent</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="concept-section">
    <h2 class="section-title">🏗️ Implémentation en Python</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Classe Graphe Complète</div>
        <div class="definition-content">
            Implémentation robuste utilisant les <strong>listes d'adjacence</strong> avec support des graphes orientés/non-orientés et pondérés.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏛️</div>
            <div class="concept-name">Structure de base</div>
            <div class="concept-description">
                Initialisation et gestion des sommets avec flexibilité d'orientation.
                
                <div class="code-example">
                    <div class="code-title">💻 Constructeur et ajout de sommets</div>
                    <pre><code>class Graphe:
    def __init__(self, oriente=False):
        self.sommets = {}  # dictionnaire : sommet -> liste des voisins
        self.oriente = oriente
    
    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe"""
        if sommet not in self.sommets:
            self.sommets[sommet] = []</code></pre>
                </div>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Gestion des arêtes</div>
            <div class="concept-description">
                Ajout et suppression d'arêtes avec gestion automatique de l'orientation.
                
                <div class="code-example">
                    <div class="code-title">💻 Méthodes d'arêtes</div>
                    <pre><code>def ajouter_arete(self, sommet1, sommet2, poids=1):
    """Ajoute une arête entre deux sommets"""
    self.ajouter_sommet(sommet1)
    self.ajouter_sommet(sommet2)
    
    # Ajouter l'arête
    self.sommets[sommet1].append((sommet2, poids))
    
    # Si non orienté, ajouter l'arête inverse
    if not self.oriente:
        self.sommets[sommet2].append((sommet1, poids))</code></pre>
                </div>
            </div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🔍 Méthodes d'analyse</div>
            <div class="concept-description">
                Fonctions utilitaires pour analyser la structure du graphe.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Analyse et vérification</div>
                <pre><code>def voisins(self, sommet):
    """Retourne la liste des voisins d'un sommet"""
    return self.sommets.get(sommet, [])

def est_adjacent(self, sommet1, sommet2):
    """Vérifie si deux sommets sont adjacents"""
    return any(voisin == sommet2 for voisin, _ in self.voisins(sommet1))

def degre(self, sommet):
    """Retourne le degré d'un sommet"""
    return len(self.voisins(sommet))</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🗑️ Suppression d'arêtes</div>
            <div class="concept-description">
                Gestion de la suppression avec respect de l'orientation.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Suppression intelligente</div>
                <pre><code>def supprimer_arete(self, sommet1, sommet2):
    """Supprime une arête"""
    if sommet1 in self.sommets:
        self.sommets[sommet1] = [(v, p) for v, p in self.sommets[sommet1] 
                                if v != sommet2]
    
    if not self.oriente and sommet2 in self.sommets:
        self.sommets[sommet2] = [(v, p) for v, p in self.sommets[sommet2] 
                                if v != sommet1]</code></pre>
            </div>
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🚀 Exemple d'utilisation pratique</div>
        
        <div class="code-example">
            <div class="code-title">💻 Construction et manipulation</div>
            <pre><code># Création d'un graphe non orienté
g = Graphe(oriente=False)

# Ajout des arêtes avec pondération
g.ajouter_arete('A', 'B', 5)
g.ajouter_arete('A', 'C', 3)
g.ajouter_arete('B', 'D', 2)
g.ajouter_arete('C', 'D', 1)

# Analyse du graphe
print(f"Degré de A: {g.degre('A')}")  # 2
print(f"A et D adjacents: {g.est_adjacent('A', 'D')}")  # False
print(f"Voisins de B: {g.voisins('B')}")  # [('A', 5), ('D', 2)]</code></pre>
        </div>
        
        <div class="highlight-fact">
            💡 <strong>Flexibilité :</strong> Cette implémentation supporte automatiquement les graphes orientés, non-orientés et pondérés selon les paramètres fournis.
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Algorithmes de Parcours</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Stratégies d'exploration</div>
        <div class="definition-content">
            Les algorithmes de parcours permettent d'<strong>explorer systématiquement</strong> tous les sommets d'un graphe. Chaque stratégie a ses propres caractéristiques et applications spécifiques.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📊 Parcours en Largeur (BFS)</div>
            <div class="concept-description">
                Explore le graphe <strong>niveau par niveau</strong> en utilisant une <strong>file (FIFO)</strong>. Idéal pour trouver le plus court chemin.
                
                <div style="margin: 1rem 0; padding: 1rem; background: #e8f4fd; border-radius: 8px; border-left: 3px solid #2196f3;">
                    <strong>🎯 Principe :</strong> Visiter tous les voisins directs avant d'explorer plus loin
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Implémentation BFS</div>
                    <pre><code>from collections import deque

def parcours_largeur(graphe, sommet_depart):
    """Parcours en largeur (BFS)"""
    visites = set()
    file = deque([sommet_depart])
    ordre_visite = []
    
    while file:
        sommet = file.popleft()  # FIFO
        
        if sommet not in visites:
            visites.add(sommet)
            ordre_visite.append(sommet)
            
            # Ajouter les voisins non visités
            for voisin, _ in graphe.voisins(sommet):
                if voisin not in visites:
                    file.append(voisin)
    
    return ordre_visite</code></pre>
                </div>
                
                <div style="margin-top: 1rem;">
                    <strong style="color: #28a745;">✅ Applications :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem; font-size: 0.9rem;">
                        <li>Plus court chemin (non pondéré)</li>
                        <li>Détection de composantes connexes</li>
                        <li>Analyse de réseaux sociaux</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔄 Parcours en Profondeur (DFS)</div>
            <div class="concept-description">
                Explore le graphe en allant <strong>le plus loin possible</strong> avant de revenir en arrière. Utilise une <strong>pile (LIFO)</strong> ou la récursion.
                
                <div style="margin: 1rem 0; padding: 1rem; background: #f0f8e8; border-radius: 8px; border-left: 3px solid #4caf50;">
                    <strong>🎯 Principe :</strong> Aller au bout d'un chemin avant d'explorer les alternatives
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Version récursive</div>
                    <pre><code>def parcours_profondeur_recursif(graphe, sommet, visites=None):
    """Parcours en profondeur récursif (DFS)"""
    if visites is None:
        visites = set()
    
    visites.add(sommet)
    print(sommet, end=' ')
    
    for voisin, _ in graphe.voisins(sommet):
        if voisin not in visites:
            parcours_profondeur_recursif(graphe, voisin, visites)</code></pre>
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Version itérative</div>
                    <pre><code>def parcours_profondeur_iteratif(graphe, sommet_depart):
    """Parcours en profondeur itératif (DFS)"""
    visites = set()
    pile = [sommet_depart]
    ordre_visite = []
    
    while pile:
        sommet = pile.pop()  # LIFO
        
        if sommet not in visites:
            visites.add(sommet)
            ordre_visite.append(sommet)
            
            # Ajouter les voisins (ordre inverse)
            for voisin, _ in reversed(graphe.voisins(sommet)):
                if voisin not in visites:
                    pile.append(voisin)
    
    return ordre_visite</code></pre>
                </div>
                
                <div style="margin-top: 1rem;">
                    <strong style="color: #28a745;">✅ Applications :</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem; font-size: 0.9rem;">
                        <li>Détection de cycles</li>
                        <li>Tri topologique</li>
                        <li>Résolution de labyrinthes</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Critère</th>
                <th>BFS (Largeur)</th>
                <th>DFS (Profondeur)</th>
                <th>Recommandation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Structure de données</td>
                <td>File (FIFO)</td>
                <td>Pile (LIFO) / Récursion</td>
                <td>Selon l'objectif</td>
            </tr>
            <tr>
                <td>Complexité temporelle</td>
                <td>O(V + E)</td>
                <td>O(V + E)</td>
                <td>Équivalent</td>
            </tr>
            <tr>
                <td>Complexité spatiale</td>
                <td>O(V)</td>
                <td>O(h) où h = hauteur</td>
                <td>DFS pour économiser l'espace</td>
            </tr>
            <tr>
                <td>Plus court chemin</td>
                <td>✅ Optimal</td>
                <td>❌ Non optimal</td>
                <td>BFS pour distances</td>
            </tr>
            <tr>
                <td>Détection de cycles</td>
                <td>✅ Possible</td>
                <td>✅ Plus naturel</td>
                <td>DFS plus simple</td>
            </tr>
        </tbody>
    </table>
    
    <div class="highlight-fact">
        🧠 <strong>Choix stratégique :</strong> BFS pour l'exploration systématique et les distances, DFS pour l'analyse structurelle et la détection de motifs.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🧮 Algorithmes Avancés sur les Graphes</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Algorithmes fondamentaux</div>
        <div class="definition-content">
            Ces algorithmes résolvent des <strong>problèmes classiques</strong> sur les graphes : détection de cycles, calcul de plus courts chemins, et analyse de connectivité.
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🔄 Détection de Cycle</div>
        
        <div class="concept-description">
            Algorithme utilisant DFS pour détecter la présence de cycles dans un graphe non orienté.
            
            <div style="margin: 1rem 0; padding: 1rem; background: #fff3cd; border-radius: 8px; border-left: 3px solid #ffc107;">
                <strong>💡 Principe :</strong> Un cycle existe si on rencontre un sommet déjà visité qui n'est pas le parent direct
            </div>
        </div>
        
        <div class="code-example">
            <div class="code-title">💻 Implémentation détection de cycle</div>
            <pre><code>def a_un_cycle(graphe):
    """Détecte s'il y a un cycle dans un graphe non orienté"""
    visites = set()
    
    def dfs(sommet, parent):
        visites.add(sommet)
        
        for voisin, _ in graphe.voisins(sommet):
            if voisin not in visites:
                if dfs(voisin, sommet):
                    return True
            elif voisin != parent:  # Cycle détecté !
                return True
        
        return False
    
    # Vérifier chaque composante connexe
    for sommet in graphe.sommets:
        if sommet not in visites:
            if dfs(sommet, None):
                return True
    
    return False</code></pre>
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🛣️ Algorithme de Dijkstra</div>
        
        <div class="concept-description">
            Calcule le plus court chemin depuis un sommet source vers tous les autres sommets dans un graphe pondéré.
            
            <div style="margin: 1rem 0; padding: 1rem; background: #e8f5e8; border-radius: 8px; border-left: 3px solid #4caf50;">
                <strong>⚡ Complexité :</strong> O((V + E) log V) avec une file de priorité
            </div>
        </div>
        
        <div class="method-grid">
            <div class="method-card">
                <div class="method-type">🎯 Algorithme principal</div>
                
                <div class="code-example">
                    <div class="code-title">💻 Dijkstra complet</div>
                    <pre><code>import heapq

def dijkstra(graphe, depart):
    """Algorithme de Dijkstra pour le plus court chemin"""
    distances = {sommet: float('inf') for sommet in graphe.sommets}
    distances[depart] = 0
    predecesseurs = {}
    
    # File de priorité : (distance, sommet)
    file_priorite = [(0, depart)]
    
    while file_priorite:
        distance_actuelle, sommet_actuel = heapq.heappop(file_priorite)
        
        # Optimisation : ignorer si déjà traité
        if distance_actuelle > distances[sommet_actuel]:
            continue
        
        # Examiner tous les voisins
        for voisin, poids in graphe.voisins(sommet_actuel):
            nouvelle_distance = distance_actuelle + poids
            
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = sommet_actuel
                heapq.heappush(file_priorite, (nouvelle_distance, voisin))
    
    return distances, predecesseurs</code></pre>
                </div>
            </div>
            
            <div class="method-card">
                <div class="method-type">🔄 Reconstruction de chemin</div>
                
                <div class="code-example">
                    <div class="code-title">💻 Récupération du chemin</div>
                    <pre><code>def reconstruire_chemin(predecesseurs, depart, arrivee):
    """Reconstruit le chemin à partir des prédécesseurs"""
    chemin = []
    sommet = arrivee
    
    while sommet is not None:
        chemin.append(sommet)
        sommet = predecesseurs.get(sommet)
    
    chemin.reverse()
    return chemin if chemin[0] == depart else []

# Exemple d'utilisation
distances, predecesseurs = dijkstra(graphe, 'A')
chemin_vers_D = reconstruire_chemin(predecesseurs, 'A', 'D')
print(f"Plus court chemin A→D: {chemin_vers_D}")
print(f"Distance: {distances['D']}")</code></pre>
                </div>
            </div>
        </div>
        
        <div class="highlight-fact">
            🚀 <strong>Performance :</strong> Dijkstra est optimal pour les graphes avec poids positifs. Pour les poids négatifs, utiliser Bellman-Ford.
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌍 Applications Pratiques des Graphes</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Domaines d'application</div>
        <div class="definition-content">
            Les graphes modélisent de nombreux <strong>systèmes réels</strong> : réseaux sociaux, systèmes de navigation, réseaux informatiques, analyse de données, etc.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">👥</div>
            <div class="concept-name">Réseaux Sociaux</div>
            <div class="concept-description">
                <strong>Modélisation :</strong> Utilisateurs = sommets, Relations = arêtes
                <br><strong>Algorithmes :</strong> Suggestions d'amis, communautés, influence
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🗺️</div>
            <div class="concept-name">Navigation GPS</div>
            <div class="concept-description">
                <strong>Modélisation :</strong> Intersections = sommets, Routes = arêtes pondérées
                <br><strong>Algorithmes :</strong> Plus court chemin, optimisation de trajets
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌐</div>
            <div class="concept-name">Réseaux Informatiques</div>
            <div class="concept-description">
                <strong>Modélisation :</strong> Routeurs = sommets, Connexions = arêtes
                <br><strong>Algorithmes :</strong> Routage, détection de pannes, optimisation
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Analyse de Données</div>
            <div class="concept-description">
                <strong>Modélisation :</strong> Entités = sommets, Relations = arêtes
                <br><strong>Algorithmes :</strong> Clustering, classification, recommandations
            </div>
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">👥 Exemple : Réseau Social</div>
        
        <div class="code-example">
            <div class="code-title">💻 Implémentation réseau social</div>
            <pre><code>class ReseauSocial:
    def __init__(self):
        self.graphe = Graphe(oriente=False)
    
    def ajouter_personne(self, nom):
        self.graphe.ajouter_sommet(nom)
    
    def ajouter_amitie(self, personne1, personne2):
        self.graphe.ajouter_arete(personne1, personne2)
    
    def amis_communs(self, personne1, personne2):
        """Trouve les amis communs entre deux personnes"""
        amis1 = {voisin for voisin, _ in self.graphe.voisins(personne1)}
        amis2 = {voisin for voisin, _ in self.graphe.voisins(personne2)}
        return amis1.intersection(amis2)
    
    def suggestions_amis(self, personne):
        """Suggère des amis basé sur les amis d'amis"""
        amis_directs = {voisin for voisin, _ in self.graphe.voisins(personne)}
        suggestions = set()
        
        for ami in amis_directs:
            for ami_dami, _ in self.graphe.voisins(ami):
                if ami_dami != personne and ami_dami not in amis_directs:
                    suggestions.add(ami_dami)
        
        return suggestions
    
    def degre_separation(self, personne1, personne2):
        """Calcule le degré de séparation (distance) entre deux personnes"""
        distances, _ = dijkstra(self.graphe, personne1)
        return distances.get(personne2, float('inf'))</code></pre>
        </div>
        
        <div class="highlight-fact">
            💡 <strong>Algorithme de suggestion :</strong> Basé sur le principe "les amis de mes amis sont mes amis potentiels"
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🗺️ Exemple : Système de Navigation</div>
        
        <div class="code-example">
            <div class="code-title">💻 Implémentation GPS</div>
            <pre><code>class CarteRoutiere:
    def __init__(self):
        self.graphe = Graphe(oriente=False)
    
    def ajouter_route(self, ville1, ville2, distance):
        self.graphe.ajouter_arete(ville1, ville2, distance)
    
    def plus_court_chemin(self, depart, arrivee):
        """Trouve le plus court chemin entre deux villes"""
        distances, predecesseurs = dijkstra(self.graphe, depart)
        
        if distances[arrivee] == float('inf'):
            return None, float('inf')
        
        chemin = reconstruire_chemin(predecesseurs, depart, arrivee)
        return chemin, distances[arrivee]
    
    def itineraire_complet(self, depart, arrivee):
        """Retourne un itinéraire détaillé"""
        chemin, distance = self.plus_court_chemin(depart, arrivee)
        
        if chemin is None:
            return None
        
        return {
            'chemin': chemin,
            'distance_totale': distance,
            'etapes': len(chemin) - 1,
            'villes_traversees': len(chemin)
        }

# Exemple d'utilisation
carte = CarteRoutiere()
carte.ajouter_route("Paris", "Lyon", 465)
carte.ajouter_route("Lyon", "Marseille", 315)

itineraire = carte.itineraire_complet("Paris", "Marseille")
if itineraire:
    print(f"Trajet: {' → '.join(itineraire['chemin'])}")
    print(f"Distance: {itineraire['distance_totale']} km")</code></pre>
        </div>
        
        <div class="highlight-fact">
            🚗 <strong>Optimisation réelle :</strong> Les GPS modernes intègrent trafic, péages, préférences utilisateur
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚡ Analyse de Complexité</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Comparaison des performances</div>
        <div class="definition-content">
            Le choix de la représentation impacte directement les <strong>performances</strong> selon les opérations effectuées.
        </div>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Opération</th>
                <th>Matrice d'adjacence</th>
                <th>Liste d'adjacence</th>
                <th>Meilleur choix</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ajouter sommet</td>
                <td>O(n²)</td>
                <td>O(1)</td>
                <td>Liste d'adjacence</td>
            </tr>
            <tr>
                <td>Ajouter arête</td>
                <td>O(1)</td>
                <td>O(1)</td>
                <td>Équivalent</td>
            </tr>
            <tr>
                <td>Supprimer arête</td>
                <td>O(1)</td>
                <td>O(degré)</td>
                <td>Matrice d'adjacence</td>
            </tr>
            <tr>
                <td>Vérifier adjacence</td>
                <td>O(1)</td>
                <td>O(degré)</td>
                <td>Matrice d'adjacence</td>
            </tr>
            <tr>
                <td>Parcours complet</td>
                <td>O(n²)</td>
                <td>O(n + m)</td>
                <td>Liste pour graphes peu denses</td>
            </tr>
            <tr>
                <td>Espace mémoire</td>
                <td>O(n²)</td>
                <td>O(n + m)</td>
                <td>Liste pour graphes peu denses</td>
            </tr>
        </tbody>
    </table>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📈</div>
            <div class="concept-name">Notation Big O</div>
            <div class="concept-description">
                <strong>n</strong> = nombre de sommets<br>
                <strong>m</strong> = nombre d'arêtes<br>
                <strong>degré</strong> = nombre de voisins d'un sommet<br>
                <strong>V</strong> = vertices (sommets)<br>
                <strong>E</strong> = edges (arêtes)
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Règles de choix</div>
            <div class="concept-description">
                <strong>Matrice :</strong> Graphes denses, vérifications fréquentes<br>
                <strong>Liste :</strong> Graphes peu denses, parcours fréquents<br>
                <strong>Seuil :</strong> m ≈ n²/2 pour choisir
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎓 Synthèse et Conclusion</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌟 Les graphes : une abstraction fondamentale</div>
        <div class="definition-content">
            Les graphes constituent l'une des <strong>structures de données les plus polyvalentes</strong> en informatique, permettant de modéliser et résoudre une multitude de problèmes complexes.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔧</div>
            <div class="concept-name">Concepts Fondamentaux</div>
            <div class="concept-description">
                <strong>• Structure :</strong> Sommets + Arêtes<br>
                <strong>• Types :</strong> Orienté/Non-orienté, Pondéré<br>
                <strong>• Représentations :</strong> Matrice vs Liste<br>
                <strong>• Flexibilité :</strong> Adaptation au contexte
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🚀</div>
            <div class="concept-name">Algorithmes Essentiels</div>
            <div class="concept-description">
                <strong>• Parcours :</strong> BFS (largeur) et DFS (profondeur)<br>
                <strong>• Chemins :</strong> Dijkstra pour plus courts chemins<br>
                <strong>• Analyse :</strong> Détection de cycles, connectivité<br>
                <strong>• Complexité :</strong> O(V + E) pour la plupart
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌍</div>
            <div class="concept-name">Applications Réelles</div>
            <div class="concept-description">
                <strong>• Réseaux sociaux :</strong> Relations, suggestions<br>
                <strong>• Navigation :</strong> GPS, optimisation de trajets<br>
                <strong>• Internet :</strong> Routage, pages web<br>
                <strong>• IA :</strong> Recherche, planification
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚖️</div>
            <div class="concept-name">Choix Stratégiques</div>
            <div class="concept-description">
                <strong>• Densité :</strong> Critère de choix principal<br>
                <strong>• Opérations :</strong> Fréquence d'utilisation<br>
                <strong>• Mémoire :</strong> Contraintes d'espace<br>
                <strong>• Performance :</strong> Optimisation ciblée
            </div>
        </div>
    </div>
    
    <div class="algorithm-card">
        <div class="algorithm-title">🎯 Points Clés à Retenir</div>
        
        <div class="highlight-fact">
            🧠 <strong>Modélisation :</strong> Identifier les entités (sommets) et leurs relations (arêtes) est la première étape cruciale
        </div>
        
        <div class="highlight-fact">
            ⚡ <strong>Performance :</strong> Le choix matrice vs liste dépend de la densité : liste pour graphes peu denses (m << n²)
        </div>
        
        <div class="highlight-fact">
            🔍 <strong>Algorithmes :</strong> BFS pour distances minimales, DFS pour exploration exhaustive et détection de cycles
        </div>
        
        <div class="highlight-fact">
            🌐 <strong>Universalité :</strong> Les graphes sont omniprésents : du GPS aux réseaux sociaux, en passant par l'IA
        </div>
        
        <div class="highlight-fact">
            🚀 <strong>Évolutivité :</strong> Les algorithmes sur graphes s'adaptent naturellement aux gros volumes de données
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔮 Perspectives d'approfondissement</div>
        <div class="definition-content">
            <strong>Algorithmes avancés :</strong> Bellman-Ford, Floyd-Warshall, Kruskal, Prim<br>
            <strong>Graphes spécialisés :</strong> Arbres, DAG, graphes bipartites<br>
            <strong>Applications avancées :</strong> Machine Learning, analyse de réseaux, optimisation
        </div>
    </div>
</div>