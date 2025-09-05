<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background: var(--md-default-bg-color);
        min-height: 100vh;
    }
    
    .course-header {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 40px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .course-title {
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
    }
    
    .course-subtitle {
        font-size: 1.2em;
        color: #7f8c8d;
        margin-bottom: 0;
    }
    
    .section-container {
        background: var(--md-default-bg-color);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .section-title {
        font-size: 1.8em;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 20px;
    }
    
    .definition-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
        backdrop-filter: blur(5px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-left: 5px solid #667eea;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .definition-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 10px;
    }
    
    .definition-content {
        color: var(--md-default-fg-color);
        line-height: 1.6;
    }
    
    .model-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    
    .model-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .model-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    .model-icon {
        font-size: 2em;
        margin-bottom: 10px;
    }
    
    .model-name {
        font-size: 1.2em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    
    .model-description {
        color: #7f8c8d;
        line-height: 1.5;
    }
    
    .highlight-fact {
        background: rgba(255, 193, 7, 0.1);
        border-left: 4px solid #ffc107;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .code-example {
        background: #1a202c;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        font-family: 'Courier New', monospace;
        color: #e2e8f0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .code-title {
        color: #4299e1;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .exercise-section {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
    }
    
    .exercise-title {
        font-size: 1.2em;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 15px;
    }
    
    .exercise-content {
        color: var(--md-default-fg-color);
        line-height: 1.6;
    }
    
    .algorithm-step {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-left: 4px solid #667eea;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        position: relative;
    }
    
    .algorithm-step:not(:last-child)::after {
        content: "↓";
        position: absolute;
        bottom: -25px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 1.5rem;
        color: #667eea;
        font-weight: bold;
    }
    
    .steps-container {
        position: relative;
        margin: 2rem 0;
    }
    
    .step-number {
        font-weight: bold;
        color: #667eea;
        margin-right: 10px;
    }
    
    .step-content {
        color: var(--md-default-fg-color);
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    th, td {
        padding: 12px;
        text-align: center;
        border-bottom: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    th {
        background: #667eea;
        color: white;
        font-weight: bold;
    }
    
    td {
        color: var(--md-default-fg-color);
    }
</style>

<div class="course-header">
    <div class="course-title">📚 Algorithmes sur les Tableaux</div>
    <div class="course-subtitle">Optimisation du Tri : Algorithmes de Comparaison</div>
</div>

<div class="section-container">
    <h2 class="section-title">🎯 Définitions et Problématiques</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Qu'est-ce que trier ?</div>
        <div class="definition-content">
            Trier consiste à organiser un ensemble d'éléments dans un ordre précis (généralement croissant ou décroissant).
            C'est une opération fondamentale en informatique, utilisée dans de nombreux domaines.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">Classement de Données</div>
            <div class="model-description">
                Organisation et structuration des informations pour faciliter leur consultation et leur analyse.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⚙️</div>
            <div class="model-name">Préparation Algorithmique</div>
            <div class="model-description">
                Préparation de données pour d'autres algorithmes qui nécessitent des données ordonnées.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🚀</div>
            <div class="model-name">Optimisation des Performances</div>
            <div class="model-description">
                Amélioration significative des performances de recherche et d'accès aux données.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Stratégies de Tri</div>
        <div class="definition-content">
            On peut trier des données de plusieurs manières :
            <ul>
                <li><strong>Par comparaison :</strong> on compare les éléments entre eux</li>
                <li><strong>Sans comparaison :</strong> on utilise des propriétés spécifiques des données</li>
            </ul>
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🔍 Tri par Sélection</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Principe de Fonctionnement</div>
        <div class="definition-content">
            Au début de l'algorithme, on cherche la plus petite valeur de la liste et on l'échange avec la valeur située à la première position.
            À partir de cette itération, on considère que la liste à trier est composée d'<strong>une partie triée</strong> et d'<strong>une partie non triée</strong>.
        </div>
    </div>
    
    <div class="steps-container">
        <div class="algorithm-step">
            <span class="step-number">1.</span>
            <span class="step-content">Chercher la valeur la plus petite de la zone non triée</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">2.</span>
            <span class="step-content">Placer cette valeur au début de la zone non triée</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">3.</span>
            <span class="step-content">Étendre la zone triée d'un élément</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">4.</span>
            <span class="step-content">Répéter jusqu'à ce que toute la liste soit triée</span>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">💡 Exemple Illustratif</div>
        <div class="definition-content">
            Liste initiale : [5, 2, 4, 6, 1, 3]
        </div>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Étapes</th>
                <th>Liste en cours</th>
                <th>Min sélectionné</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Début</td>
                <td>[5, 2, 4, 6, 1, 3]</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Étape 1</td>
                <td>[1, 2, 4, 6, 5, 3]</td>
                <td>2</td>
            </tr>
            <tr>
                <td>Étape 2</td>
                <td>[1, 2, 3, 6, 5, 4]</td>
                <td>3</td>
            </tr>
            <tr>
                <td>...</td>
                <td>...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>Final</td>
                <td>[1, 2, 3, 4, 5, 6]</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>

    <div class="definition-box">
        <div class="definition-title">🐍 Implémentation en Python</div>
        <div class="definition-content">
            On va avoir besoin de <strong>trois fonctions</strong> :
            <ul>
                <li><code>indice_minimum_tranche</code> : trouve l'indice du minimum dans une portion de la liste</li>
                <li><code>echange_valeur</code> : échange deux valeurs dans la liste</li>
                <li><code>tri_selection</code> : réalise le tri complet</li>
            </ul>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Indice de la valeur minimum dans une tranche</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>indice_minimum_tranche</code> qui prend en paramètres une liste, un indice de début et qui renvoie l'indice de la valeur la plus petite dans la tranche donnée.</strong><br><br>
            <em>Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de <strong>Out Of Range</strong>.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> indice_minimum_tranche(liste,1)
4</code></pre>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Échange de valeur à l'aide des indices</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>echange_valeur</code> qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste</strong><br><br>
            <em>Attention, cette fonction fait une modification par effet de bord et ne renvoie rien.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> echange_valeur(liste, 0, 4)
>>> print(liste)
[0,5,2,4,1,8]</code></pre>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Tri par sélection du minimum</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>tri_selection_minimum</code> qui prend en paramètre une liste et renvoie sa permutation triée.</strong><br><br>
            <em>Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> print(tri_selection_minimum(liste))
[0,1,2,4,5,8]</code></pre>
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🔄 Tri par Insertion</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Principe de Fonctionnement</div>
        <div class="definition-content">
            On considère que la liste à trier est composée d'<strong>une partie triée composée d'un élément</strong> et <strong>une partie non triée</strong>.
            À chaque itération <code>i</code> du tri, on va chercher à déplacer la valeur que l'on retrouve à la position <code>i</code> à sa bonne position dans la zone triée.
        </div>
    </div>
    
    <div class="steps-container">
        <div class="algorithm-step">
            <span class="step-number">1.</span>
            <span class="step-content">Considérer le premier élément comme déjà trié</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">2.</span>
            <span class="step-content">Prendre l'élément suivant de la zone non triée</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">3.</span>
            <span class="step-content">L'insérer à sa place dans la zone triée</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">4.</span>
            <span class="step-content">Répéter jusqu'à ce que toute la liste soit triée</span>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">💡 Exemple Illustratif</div>
        <div class="definition-content">
            Liste initiale : [5, 2, 4, 6, 1, 3]
        </div>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Étapes</th>
                <th>Liste en cours</th>
                <th>Élément inséré</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Début</td>
                <td>[5, 2, 4, 6, 1, 3]</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Étape 1</td>
                <td>[2, 5, 4, 6, 1, 3]</td>
                <td>2</td>
            </tr>
            <tr>
                <td>Étape 2</td>
                <td>[2, 4, 5, 6, 1, 3]</td>
                <td>4</td>
            </tr>
            <tr>
                <td>Étape 3</td>
                <td>[2, 4, 5, 6, 1, 3]</td>
                <td>6</td>
            </tr>
            <tr>
                <td>Étape 4</td>
                <td>[1, 2, 4, 5, 6, 3]</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Étape 5</td>
                <td>[1, 2, 3, 4, 5, 6]</td>
                <td>3</td>
            </tr>
            <tr>
                <td>Final</td>
                <td>[1, 2, 3, 4, 5, 6]</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>

    <div class="definition-box">
        <div class="definition-title">🐍 Implémentation en Python</div>
        <div class="definition-content">
            On va avoir besoin de <strong>trois fonctions</strong> :
            <ul>
                <li><code>echange_valeur</code> : échange deux valeurs dans la liste</li>
                <li><code>insertion_zone_triee</code> : insère un élément à sa place dans la zone triée</li>
                <li><code>tri_insertion</code> : réalise le tri complet</li>
            </ul>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Échange de valeur à l'aide des indices</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>echange_valeur</code> qui prend en paramètre une liste et deux indices et échange les positions des deux valeurs dans la liste</strong><br><br>
            <em>Attention, cette fonction fait une modification par effet de bord et ne renvoie rien.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> echange_valeur(liste, 0, 4)
>>> print(liste)
[0,5,2,4,1,8]</code></pre>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Insertion d'une valeur dans une zone triée</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>insertion_zone_triee</code> qui prend en paramètre une liste, et un indice correspondant à celui de la valeur qui est juste après la zone triée. Cette fonction échange la valeur à l'indice avec celles qui sont avant elles pour trouver sa bonne place.</strong><br><br>
            <em>Attention, cette fonction doit bien vérifier que les indices soient bien compris dans la liste pour éviter les erreurs de <strong>Out Of Range</strong>.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> insertion_zone_triee(liste,2)
>>> print(liste)
[1,2,5,4,0,8]</code></pre>
        </div>
    </div>
    
    <div class="exercise-section">
        <div class="exercise-title">🦊 Exercice Important : Tri par insertion</div>
        <div class="exercise-content">
            <strong>Écrire une fonction <code>tri_insertion</code> qui prend en paramètre une liste et renvoie sa permutation triée.</strong><br><br>
            <em>Attention, on ne doit pas modifier la liste passée en paramètre car cela pourrait la changer dans toute la suite du programme et il peut y avoir des cas d'usage où cette liste ne doit pas être modifiée.</em>
        </div>
        <div class="code-example">
            <div class="code-title">💡 Exemple</div>
            <pre><code>>>> liste = [1,5,2,4,0,8]
>>> print(tri_insertion(liste))
[0,1,2,4,5,8]</code></pre>
        </div>
    </div>
</div>

<div class="section-container">
    <h2 class="section-title">🔢 Tris Sans Comparaison</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Définition</div>
        <div class="definition-content">
            Les tris sans comparaison sont des algorithmes qui n'utilisent pas de comparaisons entre éléments mais exploitent des propriétés spécifiques des données pour les organiser.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🧮 Tri par Dénombrement</div>
        <div class="definition-content">
            Le tri par dénombrement est un algorithme de tri qui n'agit pas par comparaisons mais par <strong>comptage des éléments</strong> de la liste.<br><br>
            <strong>Exemple :</strong> Dans la liste L <code>[3,2,1,2]</code>, on peut dénombrer les valeurs de cette manière : une occurence de 1, deux occurences de 2 et une occurence de 3.
        </div>
    </div>
    
    <div class="steps-container">
        <div class="algorithm-step">
            <span class="step-number">1.</span>
            <span class="step-content">Créer une liste d'occurrences de taille max+1</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">2.</span>
            <span class="step-content">Compter les occurrences de chaque élément</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">3.</span>
            <span class="step-content">Reconstruire la liste triée à partir des compteurs</span>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">⚙️ Principe de fonctionnement</div>
        <div class="definition-content">
            On considère la liste L précédente :
            <ul>
                <li>On crée une liste d'occurrences contenant un nombre de 0 équivalent à la valeur maximale + 1 de la liste à trier</li>
                <li>On parcourt la liste L à trier et à chaque élément, on incrémente la valeur à l'indice du nombre rencontré</li>
                <li>On reconstruit la liste triée en parcourant la liste d'occurrences</li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        <strong>Phase 1 : Comptage des occurrences</strong>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Itération</th>
                <th>L</th>
                <th>Occurrences</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>0</td>
                <td>[3,2,1,2]</td>
                <td>[0, 0, 0, 0]</td>
            </tr>
            <tr>
                <td>1</td>
                <td>[<strong>3</strong>, 2, 1, 2]</td>
                <td>[0, 0, 0, 1]</td>
            </tr>
            <tr>
                <td>2</td>
                <td>[3, <strong>2</strong>, 1, 2]</td>
                <td>[0, 0, 1, 1]</td>
            </tr>
            <tr>
                <td>3</td>
                <td>[3, 2, <strong>1</strong>, 2]</td>
                <td>[0, 1, 1, 1]</td>
            </tr>
            <tr>
                <td>4</td>
                <td>[3, 2, 1, <strong>2</strong>]</td>
                <td>[0, 1, 2, 1]</td>
            </tr>
        </tbody>
    </table>
    
    <div class="highlight-fact">
        <strong>Phase 2 : Reconstruction de la liste triée</strong>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Itération</th>
                <th>Occurrences</th>
                <th>Liste triée</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>[<strong>0</strong>, 1, 2, 1]</td>
                <td>[]</td>
            </tr>
            <tr>
                <td>2</td>
                <td>[0, <strong>1</strong>, 2, 1]</td>
                <td>[1]</td>
            </tr>
            <tr>
                <td>3</td>
                <td>[0, 1, <strong>2</strong>, 1]</td>
                <td>[1, 2, 2]</td>
            </tr>
            <tr>
                <td>4</td>
                <td>[0, 1, 2, <strong>1</strong>]</td>
                <td>[1,2,2,3]</td>
            </tr>
        </tbody>
    </table>
</div>