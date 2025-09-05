<style>
/* Styles modernes pour le cours Structures de données linéaires */
.course-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
    color: #667eea;
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
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
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
    border-left: 4px solid #4299e1;
    white-space: pre-wrap;
    width: 100%;
    box-sizing: border-box;
}

.code-title {
    color: #4299e1;
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
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
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
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
}

.comparison-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.comparison-table table {
    width: 100%;
    border-collapse: collapse;
}

.comparison-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.comparison-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
}

.comparison-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
}

.algorithm-card {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.05));
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(255, 193, 7, 0.2);
}

.algorithm-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #f39c12;
    margin-bottom: 1rem;
    text-align: center;
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
    <h1 class="course-title">📚 Structures de données linéaires</h1>
    <p class="course-subtitle">Maîtrisez les listes et tuples en Python pour organiser vos données efficacement</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Définition Fondamentale</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Structure de données linéaire</div>
        <div class="definition-content">
            Une <strong>structure de données linéaire</strong> est une collection d'<strong>éléments</strong> stockés séquentiellement. En Python, les deux principales implémentations de tableaux sont les <strong>listes</strong> (mutables) et les <strong>tuples</strong> (immuables).
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">Organisation séquentielle</div>
            <div class="concept-description">
                Les éléments sont stockés dans un ordre spécifique, chaque élément ayant une position unique (indice).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔢</div>
            <div class="concept-name">Accès par indice</div>
            <div class="concept-description">
                Chaque élément est accessible via son indice, permettant un accès direct et rapide aux données.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💾</div>
            <div class="concept-name">Stockage efficace</div>
            <div class="concept-description">
                Évite la création de variables distinctes pour chaque élément, optimisant l'utilisation de la mémoire.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Important :</strong> En Python, comme dans la plupart des langages, les indices commencent à <strong>0</strong>.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🆚 Tuples vs Listes</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔒</div>
            <div class="concept-name">Tuples (Immuables)</div>
            <div class="concept-description">
                <strong>Syntaxe :</strong> <code>()</code><br>
                <strong>Caractéristique :</strong> Non modifiables après création<br>
                <strong>Usage :</strong> Données fixes, coordonnées, configurations
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Création d'un tuple</div>
                <pre><code># Tuple vide
mon_tuple_vide = ()

# Tuple avec valeurs
mon_tuple = (312, 354, 1234)
coordonnees = (10.5, 20.3)</code></pre>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔓</div>
            <div class="concept-name">Listes (Mutables)</div>
            <div class="concept-description">
                <strong>Syntaxe :</strong> <code>[]</code><br>
                <strong>Caractéristique :</strong> Modifiables après création<br>
                <strong>Usage :</strong> Collections dynamiques, données évolutives
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Création d'une liste</div>
                <pre><code># Liste vide
ma_liste_vide = []

# Liste avec valeurs
ma_liste = [312, 354, 1234]
notes = [14, 15, 20, 19]</code></pre>
            </div>
        </div>
    </div>
    
    <div class="comparison-table">
        <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Exemple de tableau d'indices</h4>
        <table>
            <thead>
                <tr>
                    <th>Indice</th>
                    <th>Élément</th>
                    <th>Type</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>0</td>
                    <td>312</td>
                    <td>Premier élément</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>354</td>
                    <td>Deuxième élément</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>1234</td>
                    <td>Troisième élément</td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Conseil :</strong> Privilégiez des tableaux contenant des données de même type pour éviter les erreurs et améliorer la lisibilité.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Accès et Manipulation</h2>
    
    <div class="definition-box">
        <div class="definition-title">📏 Taille d'un tableau</div>
        <div class="definition-content">
            La fonction <code>len()</code> permet d'obtenir la longueur d'un tableau, identique au fonctionnement avec les chaînes de caractères.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Obtenir la taille</div>
        <pre><code>tableau_animaux = ("chien", "chat", "oiseau", "poisson")
print(len(tableau_animaux))  # Affiche: 4</code></pre>
    </div>
    
    <div class="concept-card">
        <div class="concept-icon">🎯</div>
        <div class="concept-name">Accès par indice</div>
        <div class="concept-description">
            Utilisez la syntaxe <code>tableau[indice]</code> pour accéder à un élément spécifique.
        </div>
        
        <div class="code-example">
            <div class="code-title">💻 Accès direct</div>
            <pre><code>animaux = ["chien", "chat", "poisson", "vache"]
print(animaux[0])  # "chien"
print(animaux[3])  # "vache"</code></pre>
        </div>
    </div>
    
    <div class="concept-card">
        <div class="concept-icon">🔄</div>
        <div class="concept-name">Parcours avec boucles</div>
        <div class="concept-description">
            Utilisez les boucles <code>for</code> et <code>while</code> pour parcourir tous les éléments.
        </div>
        
        <div class="code-example">
            <div class="code-title">💻 Parcours complet</div>
            <pre><code># Avec for et range
for i in range(len(tableau)):
    print(tableau[i])

# Avec for et in
for element in tableau:
    print(element)</code></pre>
        </div>
    </div>
    
    <div class="concept-card">
        <div class="concept-icon">🔗</div>
        <div class="concept-name">Concaténation</div>
        <div class="concept-description">
            L'opérateur <code>+</code> permet de fusionner plusieurs tableaux.
        </div>
        
        <div class="code-example">
            <div class="code-title">💻 Fusion de tableaux</div>
            <pre><code>tableau_1 = (1, 2, 3)
tableau_2 = (4, 5, 6)
tableau_3 = tableau_1 + tableau_2
# Résultat: (1, 2, 3, 4, 5, 6)</code></pre>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📝 Manipulation des Listes</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Avantages des listes mutables</div>
        <div class="definition-content">
            Les listes permettent d'ajouter, supprimer et modifier des éléments après leur création, offrant une flexibilité essentielle pour les données dynamiques.
        </div>
    </div>
    
    <!-- Section Ajout d'éléments -->
    <div class="method-card">
        <div class="method-type">➕ Ajout d'éléments</div>
        
        <div class="concept-grid horizontal">
            <div class="concept-card">
                <div class="concept-icon">📎</div>
                <div class="concept-name">Méthode append()</div>
                <div class="concept-description">
                    Ajoute un élément à la fin de la liste. Modifie la liste en place.
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Utilisation d'append</div>
                    <pre><code>multiples_de_2 = []
for i in range(0, 11):
    multiples_de_2.append(i * 2)
# Résultat: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]</code></pre>
                </div>
            </div>
            
            <div class="concept-card">
                <div class="concept-icon">🔗</div>
                <div class="concept-name">Concaténation</div>
                <div class="concept-description">
                    Utilise l'opérateur <code>+</code> mais crée une nouvelle liste à chaque opération.
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Concaténation (moins efficace)</div>
                    <pre><code>multiples_de_2 = []
for i in range(0, 11):
    multiples_de_2 = multiples_de_2 + [i * 2]
# Moins efficace car crée une nouvelle liste</code></pre>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Section Suppression d'éléments -->
    <div class="method-card">
        <div class="method-type">➖ Suppression d'éléments</div>
        
        <div class="concept-grid horizontal">
            <div class="concept-card">
                <div class="concept-icon">🎯</div>
                <div class="concept-name">Méthode pop()</div>
                <div class="concept-description">
                    <code>pop(i)</code> : retire l'élément à l'indice i<br>
                    <code>pop()</code> : retire le dernier élément
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Utilisation de pop</div>
                    <pre><code>tableau = [1, 2, 3, 4]
print(tableau.pop(1))  # Affiche: 2
print(tableau.pop())   # Affiche: 4
print(tableau)         # Affiche: [1, 3]</code></pre>
                </div>
            </div>
            
            <div class="concept-card">
                <div class="concept-icon">🔍</div>
                <div class="concept-name">Méthode remove()</div>
                <div class="concept-description">
                    Retire la première occurrence de l'élément spécifié.
                </div>
                
                <div class="code-example">
                    <div class="code-title">💻 Utilisation de remove</div>
                    <pre><code>tableau = [1, 2, 2, 3, 4, 4]
tableau.remove(2)
print(tableau)  # Affiche: [1, 2, 3, 4, 4]</code></pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🚀 Techniques Avancées</h2>
    
    <div class="algorithm-card">
        <div class="algorithm-title">📝 Compréhension de liste</div>
        <div class="definition-content">
            Technique permettant de créer des listes de manière concise et élégante, en une seule ligne de code.
        </div>
        
        <div class="code-example">
            <div class="code-title">💻 Syntaxe de base</div>
            <pre><code># Syntaxe générale
# [expression for element in iterable]
# [expression for element in iterable if condition]

# Exemple: multiples de 3
multiples_de_3 = [i * 3 for i in range(0, 11)]
# Résultat: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Avec condition: nombres pairs
pairs = [i for i in range(20) if i % 2 == 0]
# Résultat: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]</code></pre>
        </div>
        
        <div class="concept-grid">
            <div class="concept-card">
                <div class="concept-icon">⚡</div>
                <div class="concept-name">Avantages</div>
                <div class="concept-description">
                    • Code plus concis et lisible<br>
                    • Performance optimisée<br>
                    • Syntaxe proche des mathématiques
                </div>
            </div>
            
            <div class="concept-card">
                <div class="concept-icon">🎯</div>
                <div class="concept-name">Structure</div>
                <div class="concept-description">
                    • <strong>Expression :</strong> ce qui sera dans la liste<br>
                    • <strong>Itérable :</strong> source des données<br>
                    • <strong>Condition :</strong> filtre optionnel
                </div>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Conseil :</strong> La compréhension de liste est idéale pour les transformations simples. Pour des logiques complexes, préférez les boucles traditionnelles pour maintenir la lisibilité.
    </div>
</div>