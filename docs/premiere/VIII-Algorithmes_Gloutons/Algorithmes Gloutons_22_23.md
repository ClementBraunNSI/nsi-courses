<style>
/* Styles modernes pour le cours Algorithmes Gloutons */
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

.model-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.model-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.model-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.model-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.model-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.model-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.algorithm-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.algorithm-table table {
    width: 100%;
    border-collapse: collapse;
}

.algorithm-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.algorithm-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
}

.algorithm-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
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

.exercise-section {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

/* Styles pour les exercices interactifs */
.section-tabs {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.section-tab {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.section-tab:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.section-tab.active {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.section-content {
    display: none;
    animation: fadeIn 0.5s ease-in;
}

.section-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.exercise-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.exercise-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 0;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    overflow: hidden;
    position: relative;
}

.exercise-card.easy {
    border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
}

.exercise-card.medium {
    border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
}

.exercise-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.exercise-content-wrapper {
    padding: 25px;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.difficulty-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
    margin-bottom: 15px;
    align-self: flex-start;
}

.difficulty-badge.easy {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.difficulty-badge.medium {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.exercise-card .exercise-title {
    color: #2d3748;
    font-size: 1.3em;
    font-weight: 700;
    margin-bottom: 15px;
    line-height: 1.3;
}

.exercise-card .exercise-content {
    color: #4a5568;
    line-height: 1.6;
    flex-grow: 1;
}

.exercise-card .exercise-content p {
    margin: 0;
}

.exercise-card .exercise-content code {
    background: rgba(102, 126, 234, 0.1);
    color: #667eea;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
    font-size: 0.9em;
}
</style>

<div class="course-header">
    <div class="course-title">🧠 Algorithmes Gloutons</div>
    <div class="course-subtitle">Stratégies d'optimisation par choix locaux</div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Définitions et Concepts</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Algorithmes Gloutons</div>
        <div class="definition-content">
            Les algorithmes gloutons sont des algorithmes qui ont pour principe de choisir à chaque étape de leur résolution la <strong>meilleure solution locale</strong>.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">⚡ Principe d'optimisation</div>
        <div class="definition-content">
            Ils peuvent répondre <strong>au problème d'optimisation</strong> en cherchant pour chaque itération un extremum qui <strong>minimise ou maximise (suivant le problème) chacune des sous-étapes</strong>.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🎯</div>
            <div class="model-name">Solution Locale vs Globale</div>
            <div class="model-description">
                En général, ces opérations de recherche d'extremum ne sont pas coûteuses mais <strong>l'ensemble de celles-ci n'est pas forcément la solution optimale globale</strong>.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⚡</div>
            <div class="model-name">Efficacité vs Force Brute</div>
            <div class="model-description">
                Cette méthode est en général plus efficace que la méthode par <strong>force brute</strong>. La méthode <strong>bruteforce</strong> donnera (théoriquement) la solution optimale en testant toutes les combinaisons possibles si la machine a les ressources nécessaires.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Lien avec le chapitre précédent :</strong> On peut faire le lien avec un algorithme vu dans le chapitre précédent : _______
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Exemples Illustratifs</h2>

    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🏔️</div>
            <div class="model-name">Exemple de l'Alpiniste</div>
            <div class="model-description">
                Prenons le cas d'un alpiniste qui gravit la chaîne de montagne <em>Kaizen</em>. Il cherche à monter par les plus grands sommets qui se trouvent à sa droite ou sa gauche. Les conditions météorologiques ne sont pas les meilleures et il y a beaucoup de nuages par plateau qui l'empêchent de voir derrière chacun des pics qu'il rencontre.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔢</div>
            <div class="model-name">Nombre le Plus Grand</div>
            <div class="model-description">
                On dispose d'une liste de chiffres quelconques et on cherche à construire le nombre le plus grand sans trier la liste. Une solution à ce problème est de trouver le chiffre le plus grand de la liste, le mettre dans la "colonne" la plus à gauche du nombre et le retirer de la liste. On réalise cette opération jusqu'à ce que la liste soit vide.
                <br><br>
                <strong>Exemple :</strong><br>
                Liste de départ = [4,2,9,6]<br>
                On cherche le chiffre le plus grand : ___<br>
                On le retire de la liste et on le rajoute dans une chaîne de caractères.<br>
                On réalise cela pour chaque chiffre dans la liste, tant que celle-ci n'est pas vide.<br>
                On obtient : "9642"
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">💰 Le Problème du Rendu de Monnaie</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Principe du Problème</div>
        <div class="definition-content">
            Le problème du rendu de monnaie consiste à rendre une certaine somme en <strong>limitant le nombre de pièces (ou billets) à rendre</strong>. On a une somme qui nous est donnée et on doit rendre la monnaie. On considère que (dans ce monde utopique), on dispose d'une <strong>infinité de billets/pièces de chaque coupure</strong>.
        </div>
    </div>
    
    <div class="algorithm-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">💶 Système Monétaire de Référence</h3>
        <table>
            <thead>
                <tr>
                    <th>1</th>
                    <th>2</th>
                    <th>5</th>
                    <th>10</th>
                    <th>20</th>
                    <th>50</th>
                    <th>100</th>
                    <th>200</th>
                    <th>500</th>
                </tr>
            </thead>
        </table>
    </div>
    
    <div class="algorithm-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📝 Exemple : Rendre 42€</h3>
        <table>
            <thead>
                <tr>
                    <th>Étapes</th>
                    <th>Liste de monnaies rendues</th>
                    <th>Somme restante à rendre</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Initialisation</td>
                    <td>monnaie = [ ]</td>
                    <td>Monnaie_restante = ...</td>
                </tr>
                <tr>
                    <td>Étape 1</td>
                    <td>monnaie = [ ]</td>
                    <td>Monnaie_restante = ...</td>
                </tr>
                <tr>
                    <td>Étape 2</td>
                    <td>monnaie = [ ]</td>
                    <td>Monnaie_restante = ...</td>
                </tr>
                <tr>
                    <td>Étape 3</td>
                    <td>monnaie = [ ]</td>
                    <td>Monnaie_restante = ...</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="exercise-section">
        <h3 style="color: #667eea; margin-bottom: 1rem;">🤔 Exercices de Réflexion</h3>
        <p><strong>On souhaite rendre 49€ à un client.</strong></p>
        
        <div style="margin: 1rem 0;">
            <strong>1.</strong> On dispose d'un système monétaire tel que Système 1 = {1,2,5,10,20,50}.<br>
            <strong>Quelle solution serait obtenue par l'algorithme glouton grâce au Système 1 ?<br>
            Est-elle optimale ?<br>
            Si non, donner une solution optimale.</strong>
        </div>
        
        <div style="margin: 1rem 0;">
            <strong>2.</strong> On dispose d'un système monétaire tel que Système 2 = {1,3,6,12,24,30}.<br>
            <strong>Quelle solution serait obtenue par l'algorithme glouton grâce au Système 2 ?<br>
            Est-elle optimale ?<br>
            Si non, donner une solution optimale.</strong>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">💡 Idée de l'Algorithme</div>
        <div class="definition-content">
            L'algorithme de rendu de monnaie suit une approche gloutonne en sélectionnant à chaque étape la plus grande pièce ou billet possible ne dépassant pas le montant restant à rendre. Voici les étapes principales :
            <br><br>
            <strong>1.</strong> On initialise une liste vide pour stocker les pièces/billets à rendre triée.<br><br>
            <strong>2.</strong> Pour chaque valeur de pièce/billet, en commençant par la plus grande :<br>
            &nbsp;&nbsp;&nbsp;&nbsp;• Tant que la valeur de la pièce/billet est inférieure ou égale au montant restant<br>
            &nbsp;&nbsp;&nbsp;&nbsp;• On ajoute cette pièce/billet à la solution<br>
            &nbsp;&nbsp;&nbsp;&nbsp;• On soustrait sa valeur du montant restant<br><br>
            <strong>3.</strong> On continue jusqu'à ce que le montant restant soit nul et on renvoie la liste de billets / pièces à rendre.
        </div>
    </div>

### Exercice : Rendu de monnaie

!!! fox_exercice
    **Écrire une fonction `rendu_monnaie(montant, systeme)` qui :**

    - Prend en paramètre un montant à rendre et un système monétaire
    - Retourne la liste des pièces/billets à rendre
    - Utilise le moins de pièces possible

    **Exemple** :
    ```python
    systeme = [50,20,10,5,2,1]
    print(rendu_monnaie(53, systeme))  # Devrait afficher [50, 2, 1]
    ```

!!! fox_exercice_test "Tester différents systèmes et montants"
    **Tester votre fonction avec les systèmes monnaie suivants :**  
    - Système 1 = [50, 20, 10, 5, 2, 1]  
    - Système 2 = [25, 20, 10, 5, 4, 1]  
    - Système 3 = [100, 50, 20, 12, 7, 1]  

    **Pour chaque système, tester avec différents montants et analyser si la solution trouvée est optimale.**

______

<div class="timeline-section">
    <h2 class="section-title">📅 Problème de la Planification de Tâches</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Présentation du Problème</div>
        <div class="definition-content">
            Le problème de la planification de tâches consiste à sélectionner un ensemble de tâches à exécuter de manière à maximiser le nombre de tâches accomplies, sachant que chaque tâche a une heure de début et une heure de fin, et qu'aucune tâche ne peut se chevaucher.
        </div>
    </div>
    
    <div class="algorithm-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Exemple de Tâches</h3>
        <table>
            <thead>
                <tr>
                    <th>Tâche</th>
                    <th>Heure de début</th>
                    <th>Heure de fin</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>A</td><td>9h00</td><td>10h30</td></tr>
                <tr><td>B</td><td>10h00</td><td>11h00</td></tr>
                <tr><td>C</td><td>11h00</td><td>12h00</td></tr>
                <tr><td>D</td><td>10h30</td><td>12h30</td></tr>
                <tr><td>E</td><td>12h00</td><td>13h00</td></tr>
            </tbody>
        </table>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Stratégie Gloutonne</div>
        <div class="definition-content">
            Pour résoudre ce problème, nous utilisons la stratégie suivante :<br><br>
            <strong>1.</strong> Trier les tâches par heure de fin croissante<br>
            <strong>2.</strong> Sélectionner la première tâche<br>
            <strong>3.</strong> Pour chaque tâche suivante, la sélectionner si elle ne chevauche pas avec la dernière tâche sélectionnée
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔧 Algorithme de Planification</div>
        <pre><code>def planification_taches(taches):
    # Trier les tâches par heure de fin
    taches_triees = sorted(taches, key=lambda x: x[2])  # x[2] = heure de fin
    
    taches_selectionnees = []
    derniere_fin = 0
    
    for tache in taches_triees:
        nom, debut, fin = tache
        if debut >= derniere_fin:
            taches_selectionnees.append(tache)
            derniere_fin = fin
    
    return taches_selectionnees</code></pre>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">💼 Le Problème du Sac à Dos</h2>

    <div class="definition-box">
        <div class="definition-title">🎯 Principe</div>
        <div class="definition-content">

            Le problème du sac à dos consiste à remplir un sac avec une capacité maximale donnée en choisissant parmi différents objets ayant chacun une masse et une valeur.<br><br>
            L'objectif est de <strong>maximiser la valeur totale des objets dans le sac</strong> tout en respectant la contrainte de capacité.<br><br>
            On considère que chaque objet est unique et ne peut être fractionné.
        </div>
    </div>  

    <div class="algorithm-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">🎒 Exemple : Sac à dos de capacité 15kg</h3>
        <table>
            <thead>
                <tr>
                    <th>Objet</th>
                    <th>A</th>
                    <th>B</th>
                    <th>C</th>
                    <th>D</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Masse</strong></td>
                    <td>4</td>
                    <td>7</td>
                    <td>5</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td><strong>Valeur</strong></td>
                    <td>10</td>
                    <td>15</td>
                    <td>8</td>
                    <td>5</td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <div class="algorithm-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📝 Résolution par Stratégie Gloutonne</h3>
        <table>
            <thead>
                <tr>
                    <th>Étapes</th>
                    <th>Objets dans le sac</th>
                    <th>Masse totale</th>
                    <th>Valeur totale</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Initialisation</td>
                    <td>[]</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>Étape 1</td>
                    <td>[B]</td>
                    <td>7</td>
                    <td>15</td>
                </tr>
                <tr>
                    <td>Étape 2</td>
                    <td>[B, A]</td>
                    <td>11</td>
                    <td>25</td>
                </tr>
                <tr>
                    <td>Étape 3</td>
                    <td>[B, A, D]</td>
                    <td>14</td>
                    <td>30</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">⚖️</div>
            <div class="model-name">Stratégie par Masse</div>
            <div class="model-description">
                Choisir d'abord les objets les plus légers pour maximiser le nombre d'objets dans le sac.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">💎</div>
            <div class="model-name">Stratégie par Valeur</div>
            <div class="model-description">
                Choisir d'abord les objets de plus grande valeur pour maximiser rapidement la valeur totale.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">Stratégie par Rapport</div>
            <div class="model-description">
                Choisir les objets ayant le meilleur rapport valeur/masse pour optimiser l'efficacité.
            </div>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">💡 Idée de l'Algorithme</div>
        <div class="definition-content">
            <strong>1.</strong> On initialise un sac vide avec une masse totale et une valeur totale à 0.<br><br>
            <strong>2.</strong> Pour chaque objet selon la stratégie choisie :<br>
            &nbsp;&nbsp;&nbsp;&nbsp;• Si l'ajout de l'objet ne dépasse pas la capacité du sac :<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- On ajoute l'objet au sac<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- On met à jour la masse totale<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- On met à jour la valeur totale<br><br>
            <strong>3.</strong> On continue jusqu'à ce qu'aucun objet ne puisse plus être ajouté.
        </div>
    </div>
