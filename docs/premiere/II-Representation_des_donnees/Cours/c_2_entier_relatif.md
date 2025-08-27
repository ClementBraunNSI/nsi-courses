<style>
/* Styles pour le cours */
.course-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
}

.course-header h1 {
    margin: 0;
    font-size: 2.5rem;
    font-weight: 700;
}

.timeline-section {
    margin: 2rem 0;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.section-title {
    color: #667eea;
    font-size: 1.8rem;
    margin-bottom: 1rem;
    font-weight: 600;
}

.definition-box {
    background: rgba(102, 126, 234, 0.1);
    border-left: 4px solid #667eea;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.definition-title {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.definition-content {
    line-height: 1.6;
    color: #333;
}

.highlight-fact {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 4px solid #fdcb6e;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(253, 203, 110, 0.3);
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.method-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
}

.method-type {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
    font-size: 1.1rem;
    border-bottom: 2px solid #667eea;
    padding-bottom: 0.5rem;
}

.code-example {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid #667eea;
    font-family: 'Courier New', monospace;
}

.code-title {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 0.5rem;
}

.code-example pre {
    margin: 0;
    white-space: pre-wrap;
    line-height: 1.4;
}

.problem-box {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.problem-title {
    font-weight: 600;
    color: #e74c3c;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.solution-box {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.solution-title {
    font-weight: 600;
    color: #2ecc71;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.comparison-table {
    margin: 1.5rem 0;
    overflow-x: auto;
}

.comparison-table table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.comparison-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.comparison-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid #eee;
}

.comparison-table tr:nth-child(even) {
    background: #f8f9fa;
}

.comparison-table tr:hover {
    background: rgba(102, 126, 234, 0.1);
}

/* Responsive design */
@media (max-width: 768px) {
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header h1 {
        font-size: 2rem;
    }
    
    .timeline-section {
        padding: 1rem;
    }
}
</style>

<div class="course-header">
    <h1>➖ Entiers négatifs en Binaire</h1>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔢 Les entiers négatifs</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Contexte</div>
        <div class="definition-content">
            Le cours précédent a permis d'expliquer comment représenter les <strong>nombres entiers positifs</strong> en base 2 pour en permettre le traitement par un ordinateur.
            <br/><br/>
            Cependant, toutes les grandeurs ne sont pas exclusivement positives :
            <ul>
                <li>Tension alternative</li>
                <li>Accélération d'un freinage</li>
                <li>Température en dessous de zéro</li>
                <li>Coordonnées géographiques</li>
            </ul>
            <br/>
            Pour pouvoir réaliser des simulations ou des traitements, il va falloir pouvoir représenter les <strong>nombres négatifs</strong>.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Première tentative : le bit de signe</h2>
    
    <div class="definition-box">
        <div class="definition-title">💡 Principe</div>
        <div class="definition-content">
            Une première technique de représentation des nombres négatifs est d'ajouter un <strong>bit de poids fort</strong> (tout à gauche) qui représente le signe :
            <ul>
                <li><strong>0</strong> représente un nombre <strong>positif</strong></li>
                <li><strong>1</strong> représente un nombre <strong>négatif</strong></li>
            </ul>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemples</div>
        <pre><code>1001₂ représente sur 4 bits signés le chiffre -1
0100₂ représente sur 4 bits signés le chiffre +4</code></pre>
    </div>
    
    <div class="problem-box">
        <div class="problem-title">⚠️ Problèmes identifiés</div>
        <div class="definition-content">
            Cela pourrait sembler être une bonne tentative, cependant <strong>deux problèmes majeurs</strong> se posent :
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">❌ Problème 1 : Double représentation du zéro</div>
            <div class="definition-content">
                En effet, 0 n'est ni positif ni négatif. On peut donc en déduire <strong>2 représentations</strong> sur 4 bits par exemple :
                <ul>
                    <li>1000₂ (zéro "négatif")</li>
            <li>0000₂ (zéro "positif")</li>
                </ul>
                <br/>
                Avoir 2 représentations pour un même chiffre n'est pas concevable notamment pour les représentations en mémoire ou bien pour les opérations.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">❌ Problème 2 : Opérations incorrectes</div>
            <div class="definition-content">
                Les opérations arithmétiques ne donnent pas les bons résultats.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Test : -13 + 13 sur 5 bits</div>
        <pre><code>11101₂ + 01101₂ = 101010₂

Sur 5 bits : 11101₂ + 01101₂ = 01010₂

Résultat attendu : -13 + 13 = 0
Résultat obtenu : 01010₂ = +10₁₀ ❌</code></pre>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🚫 <strong>Conclusion :</strong> Cette représentation n'est pas utilisable pour les calculs informatiques.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">✅ Seconde tentative : le complément à 2</h2>
    
    <div class="solution-box">
        <div class="solution-title">🎯 La solution : le complément à 2</div>
        <div class="definition-content">
            Le <strong>complément à 2</strong> est une technique qui a été proposée pour représenter les nombres négatifs de manière efficace et sans ambiguïté.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🚗 Analogie : le compteur kilométrique</div>
        <div class="definition-content">
            On peut illustrer cela comme un <strong>compteur kilométrique de vieille voiture</strong> :
            <ul>
                <li>Sur les compteurs des vieilles voitures, faire une marche arrière permettait de réduire le nombre de kilomètres affichés</li>
                <li>Si on recule au kilomètre 000000, le compteur étant circulaire, en reculant d'un kilomètre de plus, ce compteur va afficher : 999999</li>
            <li>Cette valeur 999999 peut donc représenter le kilomètre -1</li>
            </ul>
            <br/>
            Cela a donné l'idée pour représenter les nombres négatifs en binaire !
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Principe de représentation</div>
        <pre><code>1₁₀ = 0001₂ → 0₁₀ = 0000₂ → -1₁₀ = 1111₂ → -2₁₀ = 1110₂ → ...</code></pre>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🔧 Méthode de conversion</div>
            <div class="definition-content">
                <strong>Étapes pour convertir un nombre négatif :</strong>
                <ol>
                    <li>Convertir le nombre choisi en base 2</li>
                    <li>Inverser chaque bit : 0 devient 1 et inversement</li>
                    <li>Ajouter 1 à la représentation binaire du nombre inversé</li>
                </ol>
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Représenter -14 en base 2</div>
                <pre><code>Étape 1 : 14₁₀ = 1110₂
Étape 2 : 1110₂ → 0001₂ (inversion)
Étape 3 : 0001₂ + 1₂ = 0010₂ = -14₁₀</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">✅ Vérification des opérations</div>
            <div class="definition-content">
                Testons si cette méthode résout le problème des opérations.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Test : 14 + (-4) sur 4 bits</div>
        <pre><code>-4₁₀ = 1100₂ (complément à 2)
14₁₀ = 1110₂

Calcul : 1110₂ + 1100₂ = 11010₂

Sur 4 bits : on garde les 4 derniers bits : 1010₂
Résultat : 1010₂ = 10₁₀ ✅

Vérification : 14 + (-4) = 10 ✅</code></pre>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ✅ <strong>Succès !</strong> Le complément à 2 permet de réaliser toutes les opérations possibles sans erreur. C'est la méthode utilisée dans tous les ordinateurs modernes.
    </div>
    
    <div class="comparison-table">
        <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Comparaison des méthodes</h4>
        <table>
            <thead>
                <tr>
                    <th>Critère</th>
                    <th>Bit de signe</th>
                    <th>Complément à 2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Représentation unique du zéro</td>
                    <td>❌ Non (deux représentations)</td>
                    <td>✅ Oui (une seule)</td>
                </tr>
                <tr>
                    <td>Opérations arithmétiques correctes</td>
                    <td>❌ Non</td>
                    <td>✅ Oui</td>
                </tr>
                <tr>
                    <td>Simplicité d'implémentation</td>
                    <td>⚠️ Complexe</td>
                    <td>✅ Simple</td>
                </tr>
                <tr>
                    <td>Utilisation actuelle</td>
                    <td>❌ Abandonnée</td>
                    <td>✅ Standard universel</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
