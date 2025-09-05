<style>
/* Styles modernes pour le cours KNN */
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

.timeline-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
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

.fact-content {
    color: var(--md-default-fg-color);
    font-weight: 500;
    line-height: 1.6;
}

.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.info-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.info-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #4299e1;
}

.code-title {
    color: #4299e1;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.step-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.step-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

/* Styles pour les avantages et inconvénients */
.advantages-disadvantages {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 20px 0;
}

.advantage-card, .disadvantage-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.advantage-card {
    border-left: 4px solid #10b981;
}

.disadvantage-card {
    border-left: 4px solid #ef4444;
}

.advantage-card:hover, .disadvantage-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.advantage-card .card-title {
    font-size: 1.1em;
    font-weight: bold;
    color: #10b981;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.disadvantage-card .card-title {
    font-size: 1.1em;
    font-weight: bold;
    color: #ef4444;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-content {
    color: #374151;
    line-height: 1.6;
}

.card-content ul {
    margin: 0;
    padding-left: 20px;
}

.card-content li {
    margin-bottom: 8px;
}

@media (max-width: 768px) {
    .advantages-disadvantages {
        grid-template-columns: 1fr;
    }
}

.step-number {
    background: #667eea;
    color: white;
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    margin-bottom: 1rem;
}

.step-title {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #2c3e50;
}

.step-description {
    font-size: 0.9rem;
    color: #7f8c8d;
    line-height: 1.6;
}

.advantages-disadvantages {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.advantage-card, .disadvantage-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.advantage-card {
    border-left: 5px solid #27ae60;
}

.disadvantage-card {
    border-left: 5px solid #e74c3c;
}

.advantage-card:hover, .disadvantage-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.card-title {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.3rem;
    color: #2c3e50;
}

.card-content {
    font-size: 0.95rem;
    color: #7f8c8d;
    line-height: 1.6;
}

.card-content ul {
    margin: 0.5rem 0;
    padding-left: 1rem;
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Algorithme des K Plus Proches Voisins</h1>
    <p class="course-subtitle">Comprendre l'algorithme KNN et ses applications</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définition</h2>
    
    <div class="definition-box">
        <div class="definition-title">🤖 Qu'est-ce que l'algorithme KNN ?</div>
        <div class="definition-content">
            L'algorithme des K Plus Proches Voisins (K-Nearest Neighbors ou KNN) est une méthode d'<strong>apprentissage supervisé</strong> simple et intuitive, utilisée principalement pour des problèmes de <strong>classification</strong> et de <strong>régression</strong>.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔍 Concepts clés</div>
        <div class="info-content">
            <ul>
                <li><strong>Apprentissage supervisé</strong> : L'algorithme apprend à partir d'un ensemble de données où les "bonnes réponses" (étiquettes ou valeurs) sont déjà connues.</li>
                <li><strong>Classification</strong> : Prédire à quelle catégorie appartient un nouvel élément (par exemple, si un email est un spam ou non).</li>
                <li><strong>Régression</strong> : Prédire une valeur continue pour un nouvel élément (par exemple, estimer le prix d'une maison).</li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>💡 Principe fondamental :</strong> L'idée centrale de KNN est que des choses similaires existent à proximité les unes des autres. Un nouvel élément sera probablement similaire à ses voisins les plus proches dans l'ensemble de données d'entraînement.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">⚙️ Comment fonctionne KNN ?</h2>
    
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">Choisir le nombre K</div>
            <div class="step-description">
                On définit K, le nombre de voisins les plus proches à considérer. C'est un paramètre important à régler.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">Calculer les distances</div>
            <div class="step-description">
                Pour un nouvel élément, on calcule la distance entre cet élément et tous les autres éléments de l'ensemble de données d'entraînement. La mesure de distance la plus courante est la <strong>distance euclidienne</strong>.
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">Identifier les K voisins</div>
            <div class="step-description">
                On sélectionne les K éléments de l'ensemble d'entraînement qui sont les plus proches du nouvel élément (ceux ayant les plus petites distances).
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-number">4</div>
            <div class="step-title">Prendre une décision</div>
            <div class="step-description">
                <strong>Classification :</strong> On regarde la catégorie majoritaire parmi les K voisins.<br>
                <strong>Régression :</strong> On calcule la moyenne des valeurs des K voisins.
            </div>
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">📝 Exemple simple de classification</div>
        <div class="info-content">
            Imaginons que nous ayons des points de données de deux catégories (A et B) et un nouveau point inconnu (X). Si nous choisissons K=3 :
            <ol>
                <li>On calcule la distance entre X et tous les autres points.</li>
                <li>On trouve les 3 points les plus proches de X.</li>
                <li>Si 2 de ces 3 voisins sont de la catégorie A et 1 est de la catégorie B, alors X sera classifié comme A.</li>
            </ol>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📏 La mesure de distance</h2>
    
    <div class="definition-box">
        <div class="definition-title">📐 Distance euclidienne</div>
        <div class="definition-content">
            La <strong>distance euclidienne</strong> est la plus utilisée. Pour deux points P(p1, p2, ..., pn) et Q(q1, q2, ..., qn) dans un espace à n dimensions, la distance euclidienne est :
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">📊 Formule de la distance euclidienne</div>
        <pre>
d(P, Q) = √((p1-q1)² + (p2-q2)² + ... + (pn-qn)²)
        </pre>
    </div>
    
    <div class="info-box">
        <div class="info-title">📏 Autres mesures de distance</div>
        <div class="info-content">
            D'autres mesures de distance existent, comme la distance de Manhattan ou la distance de Minkowski.
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>⚠️ Important - Normalisation des données :</strong> Si les différentes caractéristiques (dimensions) de vos données n'ont pas la même échelle (par exemple, une caractéristique varie de 0 à 1 et une autre de 0 à 1000), celles avec des valeurs plus grandes domineront le calcul de la distance. Il est donc crucial de <strong>normaliser</strong> ou <strong>standardiser</strong> vos données avant d'appliquer KNN.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Choisir la valeur de K</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚖️ L'importance du choix de K</div>
        <div class="definition-content">
            Le choix de K est crucial pour la performance de l'algorithme. Il faut trouver un équilibre entre sensibilité et robustesse.
        </div>
    </div>
    
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-title">📉 K petit (ex: K=1)</div>
            <div class="step-description">
                L'algorithme est très sensible au bruit et aux points aberrants. Le modèle peut être trop spécifique aux données d'entraînement (surapprentissage ou overfitting).
            </div>
        </div>
        
        <div class="step-card">
            <div class="step-title">📈 K grand</div>
            <div class="step-description">
                L'algorithme est plus robuste au bruit, mais peut rendre les frontières de décision moins distinctes. Si K est trop grand, tous les nouveaux points seront classifiés dans la catégorie majoritaire.
            </div>
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">💡 Conseils pour choisir K</div>
        <div class="info-content">
            <ul>
                <li>Il n'y a pas de règle d'or pour choisir K</li>
                <li>On utilise souvent des techniques comme la <strong>validation croisée</strong> pour trouver une valeur optimale</li>
                <li>Une pratique courante est de choisir K comme un <strong>nombre impair</strong> pour éviter les égalités en classification binaire</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">⚖️ Avantages et Inconvénients</h2>
    
    <div class="advantages-disadvantages">
        <div class="advantage-card">
            <div class="card-title">✅ Avantages de KNN</div>
            <div class="card-content">
                <ul>
                    <li><strong>Simple à comprendre et à implémenter</strong></li>
                    <li><strong>Non paramétrique</strong> : Il ne fait aucune supposition sur la distribution sous-jacente des données</li>
                    <li><strong>Polyvalent</strong> : Peut être utilisé pour la classification et la régression</li>
                    <li><strong>S'adapte facilement</strong> : De nouvelles données peuvent être ajoutées sans avoir à ré-entraîner le modèle (apprentissage "paresseux" ou "lazy learning")</li>
                </ul>
            </div>
        </div>
        
        <div class="disadvantage-card">
            <div class="card-title">❌ Inconvénients de KNN</div>
            <div class="card-content">
                <ul>
                    <li><strong>Coûteux en calcul</strong> : Pour chaque nouvelle prédiction, il faut calculer la distance à tous les points de l'ensemble d'entraînement</li>
                    <li><strong>Sensible aux dimensions non pertinentes</strong> ("fléau de la dimensionnalité")</li>
                    <li><strong>Nécessite une normalisation des données</strong> : Les échelles des caractéristiques influencent fortement les distances</li>
                    <li><strong>Nécessite beaucoup de mémoire</strong> : Il faut stocker tout l'ensemble de données d'entraînement</li>
                    <li><strong>Le choix de K est critique</strong></li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Quand utiliser KNN ?</h2>
    
    <div class="info-box">
        <div class="info-title">📋 Cas d'usage recommandés</div>
        <div class="info-content">
            KNN peut être un bon point de départ pour des problèmes de classification ou de régression, surtout si :
            <ul>
                <li>L'ensemble de données n'est pas excessivement grand</li>
                <li>Les relations entre les caractéristiques et la cible sont complexes et non linéaires</li>
                <li>Vous avez besoin d'une méthode simple et interprétable</li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>💡 Utilisation pratique :</strong> KNN est souvent utilisé comme baseline pour comparer avec des modèles plus complexes.
        </div>
    </div>
</div>

</body>
</html>