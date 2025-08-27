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

.conversion-table {
    margin: 1.5rem 0;
    overflow-x: auto;
}

.conversion-table table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.conversion-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.conversion-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid #eee;
    text-align: center;
}

.conversion-table tr:nth-child(even) {
    background: #f8f9fa;
}

.conversion-table tr:hover {
    background: rgba(102, 126, 234, 0.1);
}

.warning-box {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.warning-title {
    font-weight: 600;
    color: #ffc107;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.ieee-structure {
    background: rgba(46, 204, 113, 0.1);
    border: 2px solid #2ecc71;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    text-align: center;
}

.ieee-bit {
    display: inline-block;
    padding: 0.5rem 1rem;
    margin: 0.2rem;
    border-radius: 5px;
    font-weight: 600;
    color: white;
}

.sign-bit {
    background: #e74c3c;
}

.exponent-bits {
    background: #f39c12;
}

.mantissa-bits {
    background: #3498db;
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
    <h1>🔢 Nombres réels en Binaire</h1>
</div>

<div class="timeline-section">
    <h2 class="section-title">💫 Les nombres réels en binaire</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Contexte</div>
        <div class="definition-content">
            Après avoir représenté les <strong>nombres entiers</strong>, il est nécessaire de représenter les <strong>nombres réels</strong>, nombres dits décimaux ou à virgule.
            <br/><br/>
            Les nombres décimaux permettent de représenter des valeurs qui peuvent être analogiques :
            <ul>
                <li>π (pi) ≈ 3.14159...</li>
                <li>Température : 36.7°C</li>
                <li>Altitude : 1847.5 mètres</li>
                <li>Coordonnées GPS : 48.8566° N</li>
            </ul>
            <br/>
            La représentation des nombres réels a été approchée de <strong>plusieurs manières différentes</strong>.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h3 class="section-title">✏️ Écriture en binaire de la partie réelle</h3>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Principe</div>
        <div class="definition-content">
            Pour écrire la partie réelle d'un nombre en binaire, on utilise les <strong>puissances négatives de 2</strong>.
            <br/><br/>
            <strong>Rappel des puissances négatives :</strong>
            <ul>
                <li>2⁻¹ = 1/2 = 0,5</li>
                <li>2⁻² = 1/4 = 0,25</li>
                <li>2⁻³ = 1/8 = 0,125</li>
                <li>2⁻⁴ = 1/16 = 0,0625</li>
            </ul>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">📝 Exemple : 0,75 en binaire</div>
        <pre>0,75 = 0,5 + 0,25
      = 2⁻¹ + 2⁻²
      = 0,11₂</pre>
    </div>
</div>

<div class="timeline-section">
    <h3 class="section-title">🔄 Méthode des multiplications successives</h3>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📋 Algorithme</div>
            <div class="definition-content">
                Pour convertir la partie décimale d'un nombre en binaire :
                <ol>
                    <li><strong>Multiplier</strong> la partie décimale par 2</li>
                    <li>Si le résultat ≥ 1 : écrire <strong>1</strong> et soustraire 1</li>
                    <li>Sinon : écrire <strong>0</strong></li>
                    <li><strong>Répéter</strong> avec la nouvelle partie décimale</li>
                </ol>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🎯 Exemple pratique : 14,75</div>
            <div class="definition-content">
                <strong>Partie entière :</strong> 14₁₀ = 1110₂
                <br/><br/>
                <strong>Partie décimale :</strong> 0,75
            </div>
            <div class="conversion-table">
                <table>
                    <tr>
                        <th>Partie décimale</th>
                        <th>Bit</th>
                        <th>Multiplication × 2</th>
                    </tr>
                    <tr>
                        <td>0,75</td>
                        <td>-</td>
                        <td>0,75</td>
                    </tr>
                    <tr>
                        <td><strong>1</strong>,5</td>
                        <td>1</td>
                        <td>0,5</td>
                    </tr>
                    <tr>
                        <td><strong>1</strong>,0</td>
                        <td>1</td>
                        <td>0,0</td>
                    </tr>
                </table>
            </div>
            <div class="code-example">
                <div class="code-title">Résultat final</div>
                <pre>14,75₁₀ = 1110₂ + 0,11₂ = 1110,11₂</pre>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Attention :</strong> Certains nombres décimaux ne peuvent pas être représentés exactement en binaire (ex: 0,1 donne une suite infinie en binaire).
    </div>
</div>

<div class="timeline-section">
    <h3 class="section-title">🧮 Test d'opération</h3>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Vérification pratique</div>
        <div class="definition-content">
            On a vu dans le cours précédent que pour qu'une représentation soit utilisable, elle doit permettre les <strong>opérations sans erreurs</strong>.
            <br/><br/>
            Faisons un test sur l'opération <strong>14,75 + 1,25</strong>.
        </div>
    </div>
    
    <div class="method-card">
        <div class="method-type">📝 Conversion de 1,25₁₀ en binaire</div>
        <div class="definition-content">
            <strong>Partie entière :</strong> 1₁₀ = 1₂
            <br/><br/>
            <strong>Partie décimale :</strong> 0,25
        </div>
        <div class="conversion-table">
            <table>
                <tr>
                    <th>Partie décimale</th>
                    <th>Bit</th>
                    <th>Multiplication × 2</th>
                </tr>
                <tr>
                    <td>0,25</td>
                    <td>-</td>
                    <td>0,25</td>
                </tr>
                <tr>
                    <td><strong>0</strong>,5</td>
                    <td>0</td>
                    <td>0,5</td>
                </tr>
                <tr>
                    <td><strong>1</strong>,0</td>
                    <td>1</td>
                    <td>0,0</td>
                </tr>
                <tr>
                    <td><strong>0</strong>,0</td>
                    <td>0</td>
                    <td>0</td>
                </tr>
            </table>
        </div>
        <div class="code-example">
            <div class="code-title">Résultat</div>
            <pre>0,25₁₀ = 0,010₂
Donc : 1,25₁₀ = 1,010₂</pre>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🧮 Vérification de l'opération</div>
        <pre>14,75₁₀ + 1,25₁₀ = 16₁₀
1110,110₂ + 1,010₂ = 10000,000₂ = 16₁₀ ✅</pre>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Observation :</strong> Cette représentation fonctionne, mais les machines (ordinateurs et smartphones) n'utilisent pas cette méthode. Elles utilisent la méthode de la <strong>virgule flottante</strong>.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🏛️ La Norme IEEE754</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Principe général</div>
        <div class="definition-content">
            La norme <strong>IEEE754</strong> permet de représenter les nombres réels en utilisant le principe de <strong>virgule flottante</strong>.
            <br/><br/>
            Cette norme permet d'écrire chaque nombre comme une <strong>écriture scientifique</strong> avec pour base 2.
            <br/><br/>
            Un nombre N s'écrit : <strong>N = (-1)ˢ × m × 2ⁿ</strong> avec m ∈ [1;2[
        </div>
    </div>
    
    <div class="ieee-structure">
        <h4>🏗️ Structure IEEE754 (32 bits - simple précision)</h4>
        <div style="margin: 1rem 0;">
            <span class="ieee-bit sign-bit">S</span>
            <span class="ieee-bit exponent-bits">E E E E E E E E</span>
            <span class="ieee-bit mantissa-bits">M M M M M M M M M M M M M M M M M M M M M M M</span>
        </div>
        <div style="font-size: 0.9rem; margin-top: 1rem;">
            <div><span class="ieee-bit sign-bit" style="font-size: 0.8rem;">S</span> = <strong>Signe</strong> (1 bit) : 0 = positif, 1 = négatif</div>
            <div><span class="ieee-bit exponent-bits" style="font-size: 0.8rem;">E</span> = <strong>Exposant</strong> (8 bits) : puissance de 2 (biaisée de 127)</div>
            <div><span class="ieee-bit mantissa-bits" style="font-size: 0.8rem;">M</span> = <strong>Mantisse</strong> (23 bits) : partie fractionnaire</div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🎯 Exemple : 14,75 en IEEE754</div>
            <div class="definition-content">
                <strong>Étape 1 : Représenter en base 2</strong>
                <br/>14₁₀ = 1110,110₂
                <br/><br/>
                <strong>Étape 2 : Écriture scientifique</strong>
                <br/>1110,110₂ = 1,110110₂ × 2³
                <br/><br/>
                <strong>Résultat :</strong> s=0, m=110110₂, n=3
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔧 Calcul des composants</div>
            <div class="definition-content">
                <strong>Étape 3 : Exposant biaisé</strong>
                <br/>E = n + 127 = 3 + 127 = 130
                <br/>130₁₀ = 10000010₂
                <br/><br/>
                <strong>Étape 4 : Assemblage final</strong>
                <br/>14,75₁₀ = 0 10000010 11011000000000000000000
            </div>
        </div>
    </div>
</div>


<div class="timeline-section">
    <h2 class="section-title">⚠️ Problème d'imprécision des flottants</h2>
    
    <div class="warning-box">
        <div class="warning-title">🚨 Limitation importante</div>
        <div class="definition-content">
            La représentation des nombres réels en binaire peut poser des <strong>problèmes d'imprécision</strong>.
            <br/><br/>
            Certains nombres décimaux ne peuvent pas être représentés <strong>exactement</strong> en binaire.
            <br/><br/>
            Par exemple, le nombre <strong>0,1</strong> en décimal ne peut pas être représenté exactement en binaire.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🐍 Exemple en Python</div>
            <div class="code-example">
                <div class="code-title">Démonstration du problème</div>
                <pre>>>> 0.1 + 0.2
0.30000000000000004

>>> a = 3.3
>>> b = 2.1
>>> c = 4.2
>>> (a+b)*c
22.680000000000003
>>> a*c + b*c
22.68</pre>
            </div>
            <div class="definition-content">
                Ce problème est dû au fait que <strong>0,1</strong> et <strong>0,2</strong> ne peuvent pas être représentés exactement en binaire.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔧 Solutions pratiques</div>
            <div class="definition-content">
                <strong>Solution 1 : Bibliothèque decimal</strong>
            </div>
            <div class="code-example">
                <div class="code-title">Utilisation de decimal</div>
                <pre>from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)  # 0.3
print(a + b == Decimal('0.3'))  # True</pre>
            </div>
            
            <div class="definition-content">
                <strong>Solution 2 : Tolérance pour comparaisons</strong>
            </div>
            <div class="code-example">
                <div class="code-title">Fonction de comparaison avec tolérance</div>
                <pre>def almost_equal(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

print(almost_equal(0.1 + 0.2, 0.3))  # True</pre>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Conseil :</strong> Toujours être prudent avec les comparaisons de nombres flottants et utiliser des méthodes appropriées selon le contexte d'application.
    </div>
</div>
