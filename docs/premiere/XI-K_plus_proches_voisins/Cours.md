<style>
/* Styles pour les cours avec système de cartes */

.course-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 100%;
}

.course-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 4px solid;
    width: 100%;
    max-width: 100%;
    margin: 1rem 0;
}

.course-card.definition {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.02) 100%);
}

.course-card.definition:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.course-card.example {
    border-left-color: #2196F3;
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.02) 100%);
}

.course-card.example:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
}

.course-card.warning {
    border-left-color: #F44336;
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.02) 100%);
}

.course-card.warning:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(244, 67, 54, 0.3);
}

.course-card.tip {
    border-left-color: #FF9800;
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.02) 100%);
}

.course-card.tip:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);
}

.course-card.highlight {
    border-left-color: #9C27B0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.05) 0%, rgba(156, 39, 176, 0.02) 100%);
}

.course-card.highlight:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(156, 39, 176, 0.3);
}

.course-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.course-content {
    margin-bottom: 1rem;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.badge.definition {
    background: rgba(76, 175, 80, 0.15);
    color: #4CAF50;
}

.badge.example {
    background: rgba(33, 150, 243, 0.15);
    color: #2196F3;
}

.badge.warning {
    background: rgba(244, 67, 54, 0.15);
    color: #F44336;
}

.badge.tip {
    background: rgba(255, 152, 0, 0.15);
    color: #FF9800;
}

.badge.highlight {
    background: rgba(156, 39, 176, 0.15);
    color: #9C27B0;
}

.btn {
    background: white;
    color: #4169E1;
    border: 2px solid #4169E1;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    text-decoration: none;
}

.btn:hover {
    background: rgba(65, 105, 225, 0.1);
    border-color: #1E90FF;
    color: #1E90FF;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(65, 105, 225, 0.4);
}

.exercise-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.math-container {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.table tr:hover {
    background: #f8f9fa;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #d63384;
}

pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre code {
    background: none;
    padding: 0;
    color: #495057;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-weight: 600;
}
</style>

# 📚 Fiche de Cours : Algorithme des K Plus Proches Voisins (KNN)

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">1. Qu'est-ce que l'algorithme des K Plus Proches Voisins (KNN) ?</h3>
        <div class="course-content">
            L'algorithme des K Plus Proches Voisins (K-Nearest Neighbors ou KNN) est une méthode d'<strong>apprentissage supervisé</strong> simple et intuitive, utilisée principalement pour des problèmes de <strong>classification</strong> et de <strong>régression</strong>.<br><br>*   <strong>Apprentissage supervisé</strong> : Cela signifie que l'algorithme apprend à partir d'un ensemble de données où les "bonnes réponses" (étiquettes ou valeurs) sont déjà connues.<br>*   <strong>Classification</strong> : Prédire à quelle catégorie appartient un nouvel élément (par exemple, si un email est un spam ou non).<br>*   <strong>Régression</strong> : Prédire une valeur continue pour un nouvel élément (par exemple, estimer le prix d'une maison).<br><br>L'idée centrale de KNN est que des choses similaires existent à proximité les unes des autres. Autrement dit, un nouvel élément sera probablement similaire à ses voisins les plus proches dans l'ensemble de données d'entraînement.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">2. Comment fonctionne KNN ?</h3>
        <div class="course-content">
            L'algorithme KNN fonctionne en plusieurs étapes :<br><br>1.  <strong>Choisir le nombre K</strong> : On définit K, le nombre de voisins les plus proches à considérer. C'est un paramètre important à régler.<br>2.  <strong>Calculer les distances</strong> : Pour un nouvel élément que l'on souhaite classifier (ou pour lequel on veut prédire une valeur), on calcule la distance entre cet élément et tous les autres éléments de l'ensemble de données d'entraînement. La mesure de distance la plus courante est la <strong>distance euclidienne</strong>.<br>3.  <strong>Identifier les K voisins</strong> : On sélectionne les K éléments de l'ensemble d'entraînement qui sont les plus proches du nouvel élément (ceux ayant les plus petites distances).<br>4.  <strong>Prendre une décision</strong> :<br>    *   <strong>Pour la classification</strong> : On regarde la catégorie majoritaire parmi les K voisins. Le nouvel élément est assigné à cette catégorie.<br>    *   <strong>Pour la régression</strong> : On calcule la moyenne (ou parfois la médiane) des valeurs des K voisins. Cette moyenne devient la valeur prédite pour le nouvel élément.<br><br>### Exemple simple de classification :<br><br>Imaginons que nous ayons des points de données de deux catégories (A et B) et un nouveau point inconnu (X). Si nous choisissons K=3 :<br><br>1.  On calcule la distance entre X et tous les autres points.<br>2.  On trouve les 3 points les plus proches de X.<br>3.  Si 2 de ces 3 voisins sont de la catégorie A et 1 est de la catégorie B, alors X sera classifié comme A.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">3. La mesure de distance</h3>
        <div class="course-content">
            La <strong>distance euclidienne</strong> est la plus utilisée. Pour deux points P(p1, p2, ..., pn) et Q(q1, q2, ..., qn) dans un espace à n dimensions, la distance euclidienne est :<br><br><code>d(P, Q) = √((p1-q1)² + (p2-q2)² + ... + (pn-qn)²) </code><br><br>D'autres mesures de distance existent, comme la distance de Manhattan ou la distance de Minkowski.<br><br><strong>Important : La normalisation des données</strong><br>Si les différentes caractéristiques (dimensions) de vos données n'ont pas la même échelle (par exemple, une caractéristique varie de 0 à 1 et une autre de 0 à 1000), celles avec des valeurs plus grandes domineront le calcul de la distance. Il est donc crucial de <strong>normaliser</strong> ou <strong>standardiser</strong> vos données avant d'appliquer KNN.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">4. Choisir la valeur de K</h3>
        <div class="course-content">
            Le choix de K est crucial :<br><br>*   <strong>K petit</strong> (par exemple, K=1) : L'algorithme est très sensible au bruit et aux points aberrants. Le modèle peut être trop spécifique aux données d'entraînement (surapprentissage ou overfitting).<br>*   <strong>K grand</strong> : L'algorithme est plus robuste au bruit, mais peut rendre les frontières de décision moins distinctes. Si K est trop grand (par exemple, K = nombre total d'échantillons), tous les nouveaux points seront classifiés dans la catégorie majoritaire de l'ensemble d'entraînement.<br><br>Il n'y a pas de règle d'or pour choisir K. On utilise souvent des techniques comme la validation croisée pour trouver une valeur optimale de K pour un problème donné. Une pratique courante est de choisir K comme un nombre impair pour éviter les égalités en classification binaire.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">5. Avantages de KNN</h3>
        <div class="course-content">
            *   <strong>Simple à comprendre et à implémenter</strong>.<br>*   <strong>Non paramétrique</strong> : Il ne fait aucune supposition sur la distribution sous-jacente des données.<br>*   <strong>Polyvalent</strong> : Peut être utilisé pour la classification et la régression.<br>*   <strong>S'adapte facilement</strong> : De nouvelles données peuvent être ajoutées sans avoir à ré-entraîner le modèle (on parle d'apprentissage "paresseux" ou "lazy learning" car la majorité du calcul se fait au moment de la prédiction).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">6. Inconvénients de KNN</h3>
        <div class="course-content">
            *   <strong>Coûteux en calcul</strong> : Pour chaque nouvelle prédiction, il faut calculer la distance à tous les points de l'ensemble d'entraînement. Cela peut être très lent pour de grands ensembles de données.<br>*   <strong>Sensible aux dimensions non pertinentes</strong> (le "fléau de la dimensionnalité") : Si l'ensemble de données a beaucoup de caractéristiques (dimensions) et que la plupart ne sont pas informatives, la performance de KNN peut se dégrader.<br>*   <strong>Nécessite une normalisation des données</strong> : Comme mentionné, les échelles des caractéristiques influencent fortement les distances.<br>*   <strong>Nécessite beaucoup de mémoire</strong> : Il faut stocker tout l'ensemble de données d'entraînement.<br>*   <strong>Le choix de K est critique</strong>.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">7. Quand utiliser KNN ?</h3>
        <div class="course-content">
            KNN peut être un bon point de départ pour des problèmes de classification ou de régression, surtout si :<br><br>*   L'ensemble de données n'est pas excessivement grand.<br>*   Les relations entre les caractéristiques et la cible sont complexes et non linéaires.<br>*   Vous avez besoin d'une méthode simple et interprétable.<br><br>Il est souvent utilisé comme baseline pour comparer avec des modèles plus complexes.
        </div>
    </div>
    
</div>