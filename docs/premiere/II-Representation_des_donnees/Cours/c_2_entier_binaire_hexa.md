<style>
/* Styles modernes pour le cours Entiers Binaires et Hexadécimaux */
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

.conversion-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.conversion-table table {
    width: 100%;
    border-collapse: collapse;
}

.conversion-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.conversion-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
    text-align: center;
}

.conversion-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .model-grid {
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
    <h1 class="course-title">🔢 Entiers Positifs en Binaire et Hexadécimal</h1>
    <p class="course-subtitle">Comprendre les systèmes de numération et les conversions entre bases</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📊 Rappel : Les bases dans la vie courante</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Système de notation en colonnes</div>
        <div class="definition-content">
            Notre système de notation repose sur une disposition en colonnes. Nous comptons avec 10 symboles allant de 0 à 9 que l'on nomme <strong>chiffre</strong>. Une fois que nous avons atteint le chiffre 9, si l'on souhaite rajouter 1, on se rend compte que l'on n'a pas de chiffres supérieurs. On crée ainsi une colonne à gauche qui contiendra un chiffre allant de 1 à 9 en remettant le chiffre de la colonne originelle (ou les suivantes) à 0.
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Exemple :</strong> 426 est composé des chiffres 4, 2 et 6 représentés dans les colonnes des centaines, dizaines et unités.
    </div>

    <div class="definition-content">
        Notre quotidien est entouré de nombres, que ce soit pour les heures qui passent, les notes, le nombre d'œufs dans une boîte. Ils sont partout et font partie de nos vies sans même que l'on s'en rende compte. Mais il existe une quasi infinité de bases !
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🥚</div>
            <div class="model-name">Base 12 - Douzaines</div>
            <div class="model-description">
                Les boîtes d'œufs sont en base 12, issue du fait qu'historiquement nous suivons le compte des œufs avec le nombre de phalanges que l'on a sur une main (sans compter le pouce car celui-ci pointe les phalanges pour compter).
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⏰</div>
            <div class="model-name">Base 60 - Temps</div>
            <div class="model-description">
                Les heures sont divisées en base 60. Il était plus simple de diviser les heures en 60 minutes pour calculer les durées plus facilement. Cela provient des babyloniens qui comptaient dans un système sexagésimal.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📺</div>
            <div class="model-name">Base 4 - Les Shadoks</div>
            <div class="model-description">
                Les personnages de ce dessin animé comptent avec 4 chiffres pour écrire leurs nombres : <strong>GA, BU, ZO, MEU</strong>. Un système de numération créatif et amusant !
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎵</div>
            <div class="model-name">Base 16 - Bibi-binaire</div>
            <div class="model-description">
                Système conçu par le compositeur Boby Lapointe en 1968. Il utilise des consonnes et des voyelles : <strong>H, B, K, D</strong> et <strong>A, E, O, I</strong>. L'avantage : on peut <em>chanter les nombres</em> !
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">💻</div>
            <div class="model-name">Base 8 - Octal</div>
            <div class="model-description">
                Base contenant 8 symboles allant de 0 à 7. Cette base servait aux informaticiens qui développaient en langage machine pour réduire le nombre de bits à écrire.<br/>
                $B_{8} = \{0,1,2,3,4,5,6,7\}$
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Définitions Fondamentales</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Qu'est-ce qu'une base ?</div>
        <div class="definition-content">
            Une base correspond au nombre de symboles qui permettent de représenter les chiffres ou les nombres.
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Base décimale :</strong> $B_{10} = \{0,1,2,...,9\}$
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">⚡</div>
            <div class="model-name">Pourquoi le Binaire ?</div>
            <div class="model-description">
                En informatique, il a été décidé d'utiliser le binaire car <strong>une machine peut facilement détecter la différence entre deux états</strong>. Un processeur est composé de transistors qui traitent deux états : ouverts et fermés à la manière d'un interrupteur.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔢</div>
            <div class="model-name">Base Binaire</div>
            <div class="model-description">
                Le binaire, ou représentation en base 2, est un moyen de représenter les nombres avec 2 symboles : 0 ou 1.<br/>
                $B_{2} = \{0,1\}$
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">Bits et Octets</div>
            <div class="model-description">
                On nomme <strong>bit</strong> les chiffres de la représentation en base 2 et un ensemble de 8 bits est appelé un <em>byte</em> ou <em>octet</em>.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🤔 <strong>Question de réflexion :</strong> <em>Combien de nombres peut-on représenter avec n bits ?</em>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Compter en Base 2</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Principe du comptage binaire</div>
        <div class="definition-content">
            Pour compter en base 2, on opère de la même manière qu'en base 10. On a une colonne qui peut valoir 0 ou 1. Une fois que la colonne atteint 1, on rajoute une colonne à sa gauche à 1 et l'on passe la colonne de droite à 0.
        </div>
    </div>
    
    <h3 class="section-title">🔢 Comment passer de base 2 à base 10 ?</h3>
    
    <div class="definition-box">
        <div class="definition-title">📝 Rappel : Compter en base 10</div>
        <div class="definition-content">
            $154_{(10)} = 1\times10^{2} + 5\times10^{1} + 4\times10^{0}$
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple de conversion binaire → décimal</div>
        <pre><code>$1101_{(2)} = 1\times2^{3} + 1\times2^{2} + 0\times2^{1} + 1\times2^{0}$
$1101_{(2)} = 8 + 4 + 0 + 1 = 13_{(10)}$</code></pre>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Important :</strong> À partir de maintenant, pour écrire un nombre si la base n'est pas explicite, il faut la préciser :
        <ul>
            <li>$154_{(10)}$ avec la base écrite sous le nombre en parenthèses</li>
            <li>$\overline{154}^{(10)}$ avec le nombre surligné et la base indiquée entre parenthèses</li>
        </ul>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">✏️ Exercice : Convertir de binaire en décimal</div>
        <div class="definition-content">
            <ul>
                <li>$1101_{(2)}$</li>
                <li>$1001_{(2)}$</li>
                <li>$1010_{(2)}$</li>
                <li>$1111_{(2)}$</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Comment passer de base 10 à base 2</h2>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">➗ Méthode des divisions successives</div>
            <div class="definition-content">
                Pour passer de la base 10 à la base 2, on peut utiliser la méthode des <strong>divisions successives</strong>. De la même manière que l'on écrit en addition de puissances de bases, on peut réaliser l'opération inverse pour trouver la représentation binaire.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 29 en binaire</div>
                <pre><code>29| 2
  |---
1 | 14 | 2
       |---
     0 | 7 | 2
           |---
         1 | 3 | 2
               |---
             1 | 1 | 2
                   |---
                 1 | 0</code></pre>
            </div>
            
            <div class="definition-content">
                On divise successivement le nombre à convertir par 2. Chaque <strong>reste</strong> correspond au nombre dans la représentation et chaque <strong>quotient</strong> est à diviser à la suite par 2. On répète ces opérations jusqu'à ce que le quotient soit 0 et le reste 1.
            </div>
            
            <div class="highlight-fact">
                📊 <strong>Résultat :</strong> $29_{10} = 11101_{2}$<br/>
                Vérification : $11101_{2} = 1×2^{4} + 1×2^{3} + 1×2^{2} + 0×2^{1} + 1×2^{0} = 16 + 8 + 4 + 0 + 1 = 29_{10}$
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">✏️ Exercice : Convertir de décimal en binaire</div>
        <div class="definition-content">
            <ul>
                <li>$27_{10}$</li>
                <li>$14_{10}$</li>
                <li>$42_{10}$</li>
                <li>$33_{10}$</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">➖ Méthode des soustractions successives</div>
            <div class="definition-content">
                Une autre méthode utilisable est la méthode des <strong>soustractions successives</strong>. Pour ce faire, il suffit de se munir d'un tableau de puissances de 2 et de savoir calculer toutes les puissances de 2.
            </div>
            
            <div class="conversion-table">
                <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Tableau des puissances de 2</h4>
                <table>
                    <thead>
                        <tr>
                            <th>$2^{n}$</th>
                            <th>$2^{n-1}$</th>
                            <th>$2^{n-2}$</th>
                            <th>...</th>
                            <th>$2^{2}$</th>
                            <th>$2^{1}$</th>
                            <th>$2^{0}$</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 42 en binaire</div>
                <pre><code>On choisit 64 > 42 donc on aura un tableau de 7 cases.
Est-ce que 42 ≥ 64 ? Non, on met 0 dans la case du tableau.
Est-ce que 42 ≥ 32 ? Oui, on met 1 dans la case du tableau. 
Reste : 42 - 32 = 10
Est-ce que 10 ≥ 16 ? Non, on met 0 dans le tableau.
Est-ce que 10 ≥ 8 ? Oui, on met 1 dans le tableau.
Reste : 10 - 8 = 2
Et ainsi de suite...</code></pre>
            </div>
            
            <div class="conversion-table">
                <table>
                    <thead>
                        <tr>
                            <th>$2^{6} = 64$</th>
                            <th>$2^{5} = 32$</th>
                            <th>$2^{4} = 16$</th>
                            <th>$2^{3} = 8$</th>
                            <th>$2^{2} = 4$</th>
                            <th>$2^{1} = 2$</th>
                            <th>$2^{0} = 1$</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>0</td>
                            <td>1</td>
                            <td>0</td>
                            <td>1</td>
                            <td>0</td>
                            <td>1</td>
                            <td>0</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="highlight-fact">
                📊 <strong>Résultat :</strong> $42_{10} = 101010_{2}$<br/>
                Vérification : $2^{5} + 2^{3} + 2^{1} = 32 + 8 + 2 = 42$
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔢 Hexadécimal</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Définition</div>
        <div class="definition-content">
            En informatique, une autre base très importante est la base <strong>hexadécimale</strong> (ou <em>hex</em>). Cette base représente les nombres avec <strong>16 symboles</strong>.
            <br/><br/>
            Cette base est très utile pour divers usages notamment :
            <ul>
                <li>La représentation d'adresse mémoire</li>
                <li>La représentation des couleurs</li>
            </ul>
            <br/>
            On peut noter cette base : $B_{16} = \{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F\}$
        </div>
    </div>
    
    <div class="conversion-table">
        <h3 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Table de correspondance Décimal ↔ Hexadécimal</h3>
        <table>
            <thead>
                <tr>
                    <th>Décimal</th>
                    <th>Hexadécimal</th>
                    <th>Décimal</th>
                    <th>Hexadécimal</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>0</td><td>0</td><td>8</td><td>8</td></tr>
                <tr><td>1</td><td>1</td><td>9</td><td>9</td></tr>
                <tr><td>2</td><td>2</td><td>10</td><td>A</td></tr>
                <tr><td>3</td><td>3</td><td>11</td><td>B</td></tr>
                <tr><td>4</td><td>4</td><td>12</td><td>C</td></tr>
                <tr><td>5</td><td>5</td><td>13</td><td>D</td></tr>
                <tr><td>6</td><td>6</td><td>14</td><td>E</td></tr>
                <tr><td>7</td><td>7</td><td>15</td><td>F</td></tr>
            </tbody>
        </table>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Important :</strong> On représente chaque symbole de la représentation en base hexadécimale par un ensemble de <strong>4 bits</strong>.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Convertir en base hexadécimale</h2>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">➗ Méthode des divisions successives</div>
            <div class="definition-content">
                À l'instar de la base 2 (et de toutes les bases), pour convertir on peut utiliser la méthode des <strong>divisions successives</strong> comme développé pour la partie binaire mais en divisant successivement par <strong>16</strong>.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 255 en hexadécimal</div>
                <pre><code>255 ÷ 16 = 15 reste 15 (F)
 15 ÷ 16 = 0  reste 15 (F)

Résultat : 255₁₀ = FF₁₆</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔄 Passer par la base 2</div>
            <div class="definition-content">
                Une autre méthode serait de convertir le nombre que nous avons en base 10 en binaire.
                Ainsi, on regroupe par <strong>paquets de 4 bits</strong> en partant du bit de poids faible et en rajoutant des 0 si jamais le paquet le plus à droite contient moins de 4 bits.
                Enfin, on associe chaque paquet de 4 bits à son équivalent en base 16.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 430₁₀ en hexadécimal</div>
                <pre><code>1. On a 430₁₀. On cherche sa représentation en base 2.
   430₁₀ = 110101110₂

2. On rajoute les 0 à gauche pour créer des paquets de 4 :
   000110101110₂

3. On associe les bits correspondants :
   0001₂ = 1₁₆
   1010₂ = A₁₆ 
   1110₂ = E₁₆

4. Résultat : 430₁₀ = 1AE₁₆</code></pre>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Passage de la base hexadécimale à la base décimale</h2>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">⚡ Puissances de 16</div>
            <div class="definition-content">
                On peut en connaissant les puissances de 16, réaliser les additions de puissances de 16 correspondant à chaque symbole du nombre écrit en hexadécimal.
                Pour rendre cela compréhensible, on peut remplacer chaque symbole hexadécimal par sa représentation en base 10.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 1AE₁₆ en décimal</div>
                <pre><code>1₁₆ = 1₁₀ ; A₁₆ = 10₁₀ ; E₁₆ = 14₁₀

1AE₁₆ = 1×16² + 10×16¹ + 14×16⁰
      = 256₁₀ + 160₁₀ + 14₁₀ 
      = 430₁₀</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🔄 Passage par la base 2</div>
            <div class="definition-content">
                La première étape est de convertir chaque symbole du nombre en base hexadécimale en base 2.
                Ensuite, simplement, on convertit de la base 2 à la base décimale comme vu précédemment.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Exemple : Convertir 1AE₁₆ en décimal</div>
                <pre><code>1. Conversion hex → binaire :
   1AE₁₆ = 0001 1010 1110₂

2. Conversion binaire → décimal :
   000110101110₂ = 1×2⁸ + 1×2⁷ + 1×2⁵ + 1×2³ + 1×2² + 1×2¹
                  = 256 + 128 + 32 + 8 + 4 + 2
                  = 430₁₀</code></pre>
            </div>
        </div>
    </div>
    
    <div class="conversion-table">
        <h4 style="text-align: center; color: #667eea; margin-bottom: 1rem;">📊 Table de correspondance Hexadécimal ↔ Binaire</h4>
        <table>
            <thead>
                <tr>
                    <th>Hexadécimal</th>
                    <th>Binaire</th>
                    <th>Hexadécimal</th>
                    <th>Binaire</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>0</td><td>0000</td><td>8</td><td>1000</td></tr>
                <tr><td>1</td><td>0001</td><td>9</td><td>1001</td></tr>
                <tr><td>2</td><td>0010</td><td>A</td><td>1010</td></tr>
                <tr><td>3</td><td>0011</td><td>B</td><td>1011</td></tr>
                <tr><td>4</td><td>0100</td><td>C</td><td>1100</td></tr>
                <tr><td>5</td><td>0101</td><td>D</td><td>1101</td></tr>
                <tr><td>6</td><td>0110</td><td>E</td><td>1110</td></tr>
                <tr><td>7</td><td>0111</td><td>F</td><td>1111</td></tr>
            </tbody>
        </table>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">✏️ Exercices</div>
        <div class="definition-content">
            <strong>Exercice 1</strong> : Conversion de l'hexadécimal au décimal :<br/>
            Convertir le nombre hexadécimal 1F3₁₆ en décimal.
            <br/><br/>
            <strong>Exercice 2</strong> : Conversion du décimal à l'hexadécimal :<br/>
            Convertir le nombre décimal 393₁₀ en hexadécimal.
        </div>
    </div>
</div>