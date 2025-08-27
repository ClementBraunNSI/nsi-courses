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

.character-examples {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.character-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    border: 1px solid rgba(102, 126, 234, 0.2);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.character-symbol {
    font-size: 2rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 0.5rem;
}

.character-type {
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
}

.encoding-table {
    margin: 1.5rem 0;
    overflow-x: auto;
}

.encoding-table table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    font-size: 0.85rem;
}

.encoding-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.8rem 0.5rem;
    text-align: center;
    font-weight: 600;
}

.encoding-table td {
    padding: 0.6rem 0.5rem;
    border-bottom: 1px solid #eee;
    text-align: center;
}

.encoding-table tr:nth-child(even) {
    background: #f8f9fa;
}

.encoding-table tr:hover {
    background: rgba(102, 126, 234, 0.1);
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

.unicode-examples {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.unicode-card {
    background: rgba(46, 204, 113, 0.1);
    border: 2px solid #2ecc71;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
}

.unicode-symbol {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    display: block;
}

.unicode-code {
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #2ecc71;
    font-size: 0.9rem;
}

.unicode-name {
    font-size: 0.8rem;
    color: #666;
    margin-top: 0.5rem;
}

/* Responsive design */
@media (max-width: 768px) {
    .method-grid, .character-examples, .unicode-examples {
        grid-template-columns: 1fr;
    }
    
    .course-header h1 {
        font-size: 2rem;
    }
    
    .timeline-section {
        padding: 1rem;
    }
    
    .encoding-table {
        font-size: 0.75rem;
    }
}
</style>

<div class="course-header">
    <h1>📝 La représentation des caractères</h1>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Objectif du cours</h2>
    
    <div class="definition-box">
        <div class="definition-title">📚 Ce que vous allez apprendre</div>
        <div class="definition-content">
            Cette leçon permettra de savoir comment <strong>représenter en binaire</strong> des caractères textuels.
            <br/><br/>
            Nous découvrirons les différents systèmes de codage et leurs évolutions.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définition</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔤 Qu'est-ce qu'un caractère ?</div>
        <div class="definition-content">
            Un caractère est un <strong>symbole</strong> d'écriture représentant en général :
            <ul>
                <li>Une <strong>lettre</strong> (A, b, C)</li>
                <li>Un <strong>chiffre</strong> (1, 2, 3, ...)</li>
                <li>Un <strong>symbole</strong> (字, Д, @, #)</li>
            </ul>
        </div>
    </div>
    
    <div class="character-examples">
        <div class="character-card">
            <div class="character-symbol">A</div>
            <div class="character-type">Lettre latine</div>
        </div>
        <div class="character-card">
            <div class="character-symbol">5</div>
            <div class="character-type">Chiffre</div>
        </div>
        <div class="character-card">
            <div class="character-symbol">字</div>
            <div class="character-type">Caractère chinois</div>
        </div>
        <div class="character-card">
            <div class="character-symbol">Д</div>
            <div class="character-type">Lettre cyrillique</div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🤖 <strong>Problème informatique :</strong> En informatique, on ne peut pas représenter directement un caractère car <strong>elle ne comprend que des 0 et des 1</strong>. Il faut donc les coder pour la machine.
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Système de codage</div>
        <div class="definition-content">
            <strong>Le codage d'un caractère</strong> est une association entre celui-ci et une représentation binaire.
            <br/><br/>
            Un <strong>système de codage</strong> est un ensemble de règles pour convertir une information par une autre (ici un caractère avec sa représentation binaire).
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🇺🇸 Un système de codage de caractère : ASCII</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 ASCII (American Standard Code for Information Interchange)</div>
        <div class="definition-content">
            L'<strong>ASCII</strong> est un codage qui utilise <strong>7 bits</strong> pour représenter des caractères alpha-numériques et d'autres caractères réservés (comme l'espace ou le retour chariot).
            <br/><br/>
            En ayant 7 bits pour représenter un caractère, on peut représenter <strong>2⁷ = 128 caractères</strong>.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">📊 Capacité d'ASCII</div>
            <div class="definition-content">
                <strong>7 bits = 128 caractères possibles</strong>
                <br/><br/>
                Cela inclut :
                <ul>
                    <li>26 lettres minuscules (a-z)</li>
                    <li>26 lettres majuscules (A-Z)</li>
                    <li>10 chiffres (0-9)</li>
                    <li>Symboles de ponctuation</li>
                    <li>Caractères de contrôle</li>
                </ul>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔢 Exemples de codes ASCII</div>
            <div class="character-examples">
                <div class="character-card">
                    <div class="character-symbol">A</div>
                    <div class="character-type">65 (décimal)</div>
                </div>
                <div class="character-card">
                    <div class="character-symbol">a</div>
                    <div class="character-type">97 (décimal)</div>
                </div>
                <div class="character-card">
                    <div class="character-symbol">0</div>
                    <div class="character-type">48 (décimal)</div>
                </div>
                <div class="character-card">
                    <div class="character-symbol">@</div>
                    <div class="character-type">64 (décimal)</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="definition-content">
        Pour faciliter la compréhension, on peut dresser une table de correspondance.
    </div>

    <div class="encoding-table">
        <h4>📋 Table de correspondance ASCII (extrait)</h4>
        <table>
            <tr>
                <th>Déc</th>
                <th>Hex</th>
                <th>Car</th>
                <th>Déc</th>
                <th>Hex</th>
                <th>Car</th>
                <th>Déc</th>
                <th>Hex</th>
                <th>Car</th>
                <th>Déc</th>
                <th>Hex</th>
                <th>Car</th>
            </tr>
            <tr>
                <td>32</td>
                <td>20</td>
                <td>(espace)</td>
                <td>48</td>
                <td>30</td>
                <td>0</td>
                <td>64</td>
                <td>40</td>
                <td>@</td>
                <td>80</td>
                <td>50</td>
                <td>P</td>
            </tr>
            <tr>
                <td>33</td>
                <td>21</td>
                <td>!</td>
                <td>49</td>
                <td>31</td>
                <td>1</td>
                <td>65</td>
                <td>41</td>
                <td>A</td>
                <td>81</td>
                <td>51</td>
                <td>Q</td>
            </tr>
            <tr>
                <td>34</td>
                <td>22</td>
                <td>"</td>
                <td>50</td>
                <td>32</td>
                <td>2</td>
                <td>66</td>
                <td>42</td>
                <td>B</td>
                <td>82</td>
                <td>52</td>
                <td>R</td>
            </tr>
            <tr>
                <td>97</td>
                <td>61</td>
                <td>a</td>
                <td>113</td>
                <td>71</td>
                <td>q</td>
                <td>122</td>
                <td>7A</td>
                <td>z</td>
                <td>126</td>
                <td>7E</td>
                <td>~</td>
            </tr>
        </table>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Limitation d'ASCII :</strong> À la vue de cette table, on remarque une chose importante : il n'y a que des symboles d'<strong>alphabets latins</strong>.
        <br/><br/>
        Or, il n'existe pas uniquement les alphabets latins mais aussi le <strong>cyrillique</strong> ou bien les symboles des alphabets <strong>chinois</strong> ou <strong>japonais</strong>.
        <br/><br/>
        💡 <strong>Solution :</strong> On a besoin d'un codage permettant de représenter <strong>davantage de caractères</strong>.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🌍 Un système plus inclusif : Unicode</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔤 Unicode - Le standard universel</div>
        <div class="definition-content">
            <strong>Unicode</strong> est un système de codage de caractère qui utilise un certain nombre de bits en fonction de sa version, plus connu sous le nom de <strong>UTF</strong>.
            <br/><br/>
            On utilise plus souvent le système <strong>UTF-8</strong> qui utilise 8 bits pour représenter des caractères. Il peut cependant utiliser 1, 2 voire même 3 groupes de 8 bits (octets) pour représenter davantage de caractères.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🎯 Principe des points de code</div>
            <div class="definition-content">
                Chaque symbole possède un <strong>point de code</strong>, qui est l'ensemble des bits permettant sa représentation, souvent représenté en <strong>hexadécimal</strong>.
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🐍 Utilisation en Python</div>
            <div class="definition-content">
                <strong>Python</strong> utilise l'encodage UTF-8 pour coder ses symboles et les représenter.
                <br/><br/>
                Il est possible d'observer un encodage spécial sur une chaîne de caractère en utilisant la méthode <code>encode</code> des chaînes de caractères.
            </div>
        </div>
    </div>
    
    <div class="unicode-examples">
        <div class="unicode-card">
            <span class="unicode-symbol">풪</span>
            <div class="unicode-code">U+052A</div>
            <div class="unicode-name">Caractère coréen</div>
        </div>
        <div class="unicode-card">
            <span class="unicode-symbol">A</span>
            <div class="unicode-code">U+0041</div>
            <div class="unicode-name">Lettre latine majuscule</div>
        </div>
        <div class="unicode-card">
            <span class="unicode-symbol">ᛒ</span>
            <div class="unicode-code">U+16D2</div>
            <div class="unicode-name">Lettre B runique</div>
        </div>
        <div class="unicode-card">
            <span class="unicode-symbol">字</span>
            <div class="unicode-code">U+5B57</div>
            <div class="unicode-name">Caractère chinois</div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔗 Ressource utile</div>
        <div class="definition-content">
            On retrouvera la table UTF-8 complète à cette adresse : 
            <a href="https://www.charset.org/utf-8" target="_blank">Table UTF-8</a>
        </div>
    </div>
</div>