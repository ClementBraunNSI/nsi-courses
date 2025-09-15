<style>
/* Styles modernes pour le cours Arbres */
.course-header {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(46, 204, 113, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.concept-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2rem;
    font-weight: 600;
    color: #2ecc71;
    margin-bottom: 2rem;
    text-align: center;
}

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-grid.horizontal {
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 20px;
}

.concept-grid.two-columns {
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

@media (max-width: 1200px) {
    .concept-grid.two-columns {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 1200px) {
    .concept-grid.horizontal {
        grid-template-columns: 1fr;
    }
}

.concept-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.concept-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.concept-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    text-align: center;
}

.concept-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    text-align: center;
}

.concept-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.definition-box {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-left: 5px solid #2ecc71;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #2ecc71;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #2ecc71;
    white-space: pre-wrap;
    width: 100%;
    box-sizing: border-box;
}

.code-title {
    color: #2ecc71;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.method-card {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(46, 204, 113, 0.2);
    transition: all 0.3s ease;
    width: 100%;
    max-width: none;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-type {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2ecc71;
    margin-bottom: 1rem;
    text-align: center;
}

.comparison-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(46, 204, 113, 0.2);
    overflow-x: auto;
}

.comparison-table table {
    width: 100%;
    border-collapse: collapse;
}

.comparison-table th {
    background: #2ecc71;
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.comparison-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(46, 204, 113, 0.1);
}

.comparison-table tr:hover {
    background: rgba(46, 204, 113, 0.05);
}

.algorithm-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(155, 89, 182, 0.2);
}

.algorithm-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #9b59b6;
    margin-bottom: 1rem;
    text-align: center;
}

.tree-diagram {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 2rem;
    margin: 1.5rem 0;
    text-align: center;
    font-family: 'Courier New', monospace;
    border: 1px solid rgba(46, 204, 113, 0.2);
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">🌳 Les Arbres</h1>
    <p class="course-subtitle">Maîtrisez les structures hiérarchiques pour organiser et traiter vos données efficacement</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Définition Fondamentale</h2>
    
    <div class="definition-box">
        <div class="definition-title">🌲 Structure arborescente</div>
        <div class="definition-content">
            Un <strong>arbre</strong> est une structure de données hiérarchique composée de <strong>nœuds</strong> reliés par des <strong>arêtes</strong>, sans cycle. C'est un cas particulier de graphe connexe et acyclique, parfait pour représenter des relations hiérarchiques.
        </div>
    </div>
    
    <div class="tree-diagram">
        <h4 style="color: #2ecc71; margin-bottom: 1rem;">📊 Exemple d'arbre</h4>
        <pre>       A (racine)
      / \
     B   C
    /   / \
   D   E   F (feuilles)</pre>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔗</div>
            <div class="concept-name">Structure hiérarchique</div>
            <div class="concept-description">
                Organisation en niveaux avec une racine unique et des relations parent-enfant clairement définies.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🚫</div>
            <div class="concept-name">Sans cycle</div>
            <div class="concept-description">
                Aucun chemin ne permet de revenir au point de départ, garantissant une structure claire et navigable.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Connexe</div>
            <div class="concept-description">
                Tous les nœuds sont accessibles depuis la racine, assurant une cohérence structurelle.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📚 Vocabulaire Essentiel</h2>
    
    <div class="concept-grid two-columns">
        <div class="concept-card">
            <div class="concept-icon">🔵</div>
            <div class="concept-name">Nœud (Sommet)</div>
            <div class="concept-description">
                Élément fondamental de l'arbre contenant une valeur ou des données.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">👑</div>
            <div class="concept-name">Racine</div>
            <div class="concept-description">
                Nœud au sommet de l'arbre, point d'entrée unique sans parent.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🍃</div>
            <div class="concept-name">Feuille</div>
            <div class="concept-description">
                Nœud terminal sans enfants, extrémité de l'arbre.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">👨‍👦</div>
            <div class="concept-name">Parent/Enfant</div>
            <div class="concept-description">
                Relations directes : parent au-dessus, enfant en-dessous.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">👫</div>
            <div class="concept-name">Frères</div>
            <div class="concept-description">
                Nœuds partageant le même parent, au même niveau.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌿</div>
            <div class="concept-name">Sous-arbre</div>
            <div class="concept-description">
                Arbre formé par un nœud et tous ses descendants.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📏 Propriétés Importantes</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📐</div>
            <div class="concept-name">Hauteur</div>
            <div class="concept-description">
                Longueur du plus long chemin de la racine à une feuille. Mesure la "profondeur" maximale de l'arbre.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎚️</div>
            <div class="concept-name">Profondeur d'un nœud</div>
            <div class="concept-description">
                Distance de la racine à ce nœud. La racine a une profondeur de 0.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔢</div>
            <div class="concept-name">Degré d'un nœud</div>
            <div class="concept-description">
                Nombre d'enfants directs d'un nœud. Détermine la "largeur" locale.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Taille</div>
            <div class="concept-description">
                Nombre total de nœuds dans l'arbre. Mesure la complexité globale.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Important :</strong> Ces propriétés sont fondamentales pour analyser la complexité des algorithmes sur les arbres.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌲 Arbres Binaires</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔀 Arbre binaire</div>
        <div class="definition-content">
            Un <strong>arbre binaire</strong> est un arbre où chaque nœud a <strong>au maximum 2 enfants</strong> : un enfant gauche et un enfant droit. Cette contrainte simplifie les algorithmes et optimise les performances.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⚖️</div>
            <div class="concept-name">Structure équilibrée</div>
            <div class="concept-description">
                Limitation à 2 enfants maximum permettant un équilibrage efficace et des opérations optimisées.
                
                <div class="code-example">
                    <div class="code-title">💻 Classe NoeudBinaire</div>
                    <pre><code>class NoeudBinaire:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
    
    def est_feuille(self):
        return self.gauche is None and self.droite is None</code></pre>
                </div>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏗️</div>
            <div class="concept-name">Implémentation Python</div>
            <div class="concept-description">
                Structure de classe simple avec méthodes essentielles pour la manipulation et l'analyse.
                
                <div class="code-example">
                    <div class="code-title">💻 Classe ArbreBinaire</div>
                    <pre><code>class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine
    
    def est_vide(self):
        return self.racine is None</code></pre>
                </div>
            </div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📏 Calcul de hauteur</div>
            <div class="concept-description">
                Algorithme récursif pour déterminer la profondeur maximale de l'arbre.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Méthode hauteur</div>
                <pre><code>def hauteur(self, noeud=None):
    if noeud is None:
        noeud = self.racine
    
    if noeud is None:
        return -1
    
    if noeud.est_feuille():
        return 0
    
    hauteur_gauche = self.hauteur(noeud.gauche) if noeud.gauche else -1
    hauteur_droite = self.hauteur(noeud.droite) if noeud.droite else -1
    
    return 1 + max(hauteur_gauche, hauteur_droite)</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔢 Calcul de taille</div>
            <div class="concept-description">
                Comptage récursif du nombre total de nœuds dans l'arbre.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Méthode taille</div>
                <pre><code>def taille(self, noeud=None):
    if noeud is None:
        noeud = self.racine
    
    if noeud is None:
        return 0
    
    return 1 + self.taille(noeud.gauche) + self.taille(noeud.droite)</code></pre>
            </div>
        </div>
    </div>
    
    <div class="tree-diagram">
        <h4 style="color: #2ecc71; margin-bottom: 1rem;">🏗️ Exemple de construction</h4>
        <pre>       1
      / \
     2   3
    /   / \
   4   5   6</pre>
        
        <div class="code-example">
            <div class="code-title">💻 Construction manuelle</div>
            <pre><code>racine = NoeudBinaire(1)
racine.gauche = NoeudBinaire(2)
racine.droite = NoeudBinaire(3)
racine.gauche.gauche = NoeudBinaire(4)
racine.droite.gauche = NoeudBinaire(5)
racine.droite.droite = NoeudBinaire(6)

arbre = ArbreBinaire(racine)
print(f"Hauteur: {arbre.hauteur()}")  # 2
print(f"Taille: {arbre.taille()}")    # 6</code></pre>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚡ <strong>Performance :</strong> Les arbres binaires équilibrés offrent une complexité O(log n) pour la plupart des opérations.
    </div>
</div>