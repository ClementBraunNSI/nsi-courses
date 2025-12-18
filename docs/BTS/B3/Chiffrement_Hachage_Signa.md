<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B3.2 - Chiffrement et Hachage</title>
    <style>
/* Styles modernes B1 – alignés avec le cours de cybersécurité */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #2c3e50;
    background: #ffffff;
    margin: 0;
    padding: 20px;
}
.course-header {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
    text-align: center;
}
.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
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
    background: white;
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 1.5rem;
    text-align: center;
}

.subsection-title {
    font-size: 1.6rem;
    font-weight: 600;
    color: #3498db;
    margin: 1.5rem 0 0.8rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid rgba(52, 152, 219, 0.25);
}

.subsubsection-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 1.2rem 0 0.6rem 0;
    padding-bottom: 0.3rem;
    border-bottom: 1px dashed rgba(44, 62, 80, 0.3);
}

.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 0.8rem;
}

.definition-content {
    color: #2c3e50;
    font-size: 1.05rem;
    line-height: 1.6;
}

.content-text {
    color: #2c3e50;
    line-height: 1.7;
    margin: 1.2rem 0;
    font-size: 1.05rem;
}

.highlight-fact {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.warning-fact {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.danger-fact {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.scenario-box {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f39c12;
    border-radius: 8px;
    padding: 1.2rem;
    margin: 1rem 0;
}

.exercise-container {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #3498db;
}

.exercise-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2980b9;
    margin-bottom: 1rem;
}

.exercise-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 8px;
    overflow: hidden;
}

.exercise-table th, .exercise-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(52, 152, 219, 0.2);
}

.exercise-table th {
    background: rgba(52, 152, 219, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

.code-block {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 1.5rem;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Courier New', monospace;
    margin: 1rem 0;
}

.visual-diagram {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.05), rgba(155, 89, 182, 0.02));
    border: 2px solid rgba(52, 152, 219, 0.2);
    border-radius: 12px;
    padding: 2rem;
    margin: 1.5rem 0;
    text-align: center;
}

.arrow {
    font-size: 2rem;
    color: #3498db;
    margin: 0.5rem 0;
}

.key-box {
    display: inline-block;
    background: rgba(52, 152, 219, 0.1);
    border: 2px solid #3498db;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    margin: 0.5rem;
    font-weight: 600;
}

ul, ol {
    margin: 1rem 0;
    padding-left: 2rem;
}

li {
    margin: 0.5rem 0;
}

code {
    background: rgba(52, 152, 219, 0.1);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    .course-header {
        padding: 2rem;
    }
}
    </style>
</head>
<body>

<div class="course-header">
    <h1 class="course-title">🔐 B3.2 – Chiffrement et Hachage</h1>
    <p class="course-subtitle">BTS SIO • Bloc 3 – Protection des données et authentification</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Rappels : Les piliers de la sécurité</h2>
    
    <div class="content-text">
        <p>Avant de plonger dans le chiffrement et le hachage, rappelons les quatre propriétés fondamentales que nous cherchons à garantir :</p>
    </div>

    <div class="definition-box">
        <div class="definition-title">🔒 Confidentialité</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Garantir que seules les personnes autorisées peuvent lire l'information.</p>
            <p><strong>Question clé :</strong> "Est-ce que quelqu'un d'autre peut lire mon message ?"</p>
            <p><strong>Solution technique :</strong> Le <strong>chiffrement</strong></p>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">🛡️ Intégrité</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Garantir que l'information n'a pas été modifiée entre l'envoi et la réception.</p>
            <p><strong>Question clé :</strong> "Mon message a-t-il été altéré en chemin ?"</p>
            <p><strong>Solution technique :</strong> Le <strong>hachage</strong></p>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">✅ Authenticité</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Garantir l'identité de l'émetteur du message.</p>
            <p><strong>Question clé :</strong> "Suis-je sûr que c'est bien Alice qui a envoyé ce message ?"</p>
            <p><strong>Solution technique :</strong> La <strong>signature numérique</strong></p>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">📜 Non-répudiation</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Garantir que l'émetteur ne peut pas nier avoir envoyé le message.</p>
            <p><strong>Question clé :</strong> "Alice peut-elle prétendre qu'elle n'a jamais envoyé ce message ?"</p>
            <p><strong>Solution technique :</strong> La <strong>signature numérique</strong> avec certificats</p>
        </div>
    </div>

    <div class="highlight-fact">
        💡 <strong>À retenir :</strong> Le chiffrement protège la <strong>confidentialité</strong>, le hachage protège l'<strong>intégrité</strong>, et la signature numérique garantit l'<strong>authenticité</strong> et la <strong>non-répudiation</strong>.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📚 Définitions essentielles</h2>

    <div class="definition-box">
        <div class="definition-title">🔐 Cryptographie</div>
        <div class="definition-content">
            <p>Science qui regroupe l'ensemble des techniques permettant de protéger les communications et les données.</p>
            <p>Elle inclut : le chiffrement, le déchiffrement, le hachage, les signatures numériques, etc.</p>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">🔒 Chiffrement (Encryption)</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Processus de transformation d'un message clair (lisible) en un message chiffré (illisible) à l'aide d'une <strong>clé de chiffrement</strong>.</p>
            <p><strong>Objectif :</strong> Rendre le message incompréhensible pour quiconque ne possède pas la clé.</p>
            <div class="code-block">
Message clair + Clé de chiffrement = Message chiffré
"Bonjour" + Clé → "X8#mK@2pQ"
            </div>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">🔓 Déchiffrement (Decryption)</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Processus <strong>légitime</strong> de transformation d'un message chiffré en message clair à l'aide de la <strong>clé de déchiffrement appropriée</strong>.</p>
            <p><strong>Important :</strong> Le déchiffrement nécessite la <strong>bonne clé</strong>.</p>
            <div class="code-block">
Message chiffré + Clé de déchiffrement = Message clair
"X8#mK@2pQ" + Clé → "Bonjour"
            </div>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">🔨 Décryptage (Cryptanalysis)</div>
        <div class="definition-content">
            <p><strong>Définition :</strong> Processus <strong>illégitime</strong> visant à retrouver le message clair <strong>sans posséder la clé</strong>.</p>
            <p><strong>C'est l'activité des attaquants !</strong></p>
            <p>Méthodes : force brute, analyse de fréquence, exploitation de failles, etc.</p>
        </div>
    </div>

    <div class="warning-fact">
        ⚠️ <strong>Distinction importante :</strong><br>
        • <strong>Déchiffrement</strong> = avec la clé (légitime)<br>
        • <strong>Décryptage</strong> = sans la clé (attaque)
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🦊 Mise en situation : Alice et les renards</h2>

    <div class="scenario-box">
        <div class="content-text">
            <p><strong>Contexte :</strong></p>
            <p>Alice est biologiste et étudie une colonie de renards roux dans une réserve naturelle. Elle a fait une découverte scientifique majeure : elle a observé un comportement de communication unique chez ces renards, qui pourrait révolutionner notre compréhension de l'intelligence animale.</p>
            
            <p>Elle souhaite partager ses observations détaillées avec son collègue Bob, un autre chercheur, mais elle a un problème...</p>
        </div>
    </div>

    <div class="danger-fact">
        🚨 <strong>Le problème :</strong><br>
        <ul>
            <li>Alice et Bob communiquent par email pour échanger leurs données de recherche</li>
            <li>Un concurrent malveillant, Charlie, surveille le réseau et intercepte tous les emails</li>
            <li>Si Charlie lit les découvertes d'Alice, il pourrait publier les résultats avant elle et s'attribuer la découverte</li>
            <li>Les emails transitent en <strong>clair</strong> sur Internet : n'importe qui peut les lire !</li>
        </ul>
    </div>

    <div class="visual-diagram">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🦊</div>
        <div><strong>Alice</strong> (chercheuse)</div>
        <div class="arrow">📧 ⬇️</div>
        <div style="background: rgba(231, 76, 60, 0.2); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
            <strong style="color: #e74c3c;">⚠️ INTERNET (non sécurisé)</strong><br>
            <span style="font-size: 2rem;">👤</span><br>
            <strong>Charlie</strong> (concurrent espion)<br>
            <em>Peut lire tous les messages en clair !</em>
        </div>
        <div class="arrow">📧 ⬇️</div>
        <div><strong>Bob</strong> (collègue)</div>
    </div>

    <div class="content-text">
        <p><strong>Message qu'Alice veut envoyer :</strong></p>
        <div class="code-block">
"Les renards utilisent 12 vocalisations distinctes pour coordonner 
la chasse nocturne. Comportement jamais observé auparavant. 
Données GPS attachées. Publication prévue dans Nature en mars."
        </div>
    </div>

    <div class="warning-fact">
        ⚠️ <strong>Pourquoi ne peut-on pas envoyer ce message en clair ?</strong><br>
        <ul>
            <li>Charlie peut intercepter et lire le message</li>
            <li>Il pourrait voler la découverte et publier avant Alice</li>
            <li>Les années de recherche d'Alice seraient compromises</li>
            <li>Sa réputation scientifique serait ruinée</li>
        </ul>
    </div>

    <div class="highlight-fact">
        💡 <strong>La solution :</strong> Alice doit <strong>chiffrer</strong> son message avant de l'envoyer !<br>
        Même si Charlie intercepte l'email, il ne pourra lire qu'un charabia incompréhensible.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔤 Les chiffrements monoalphabétique et polyalphabétique</h2>

    <h3 class="subsection-title">1.1 Chiffrement monoalphabétique</h3>

    <div class="definition-box">
        <div class="definition-title">Définition</div>
        <div class="definition-content">
            <p>Un <strong>chiffrement monoalphabétique</strong> remplace chaque lettre du message par une autre lettre selon une règle fixe.</p>
            <p><strong>Caractéristique :</strong> Une même lettre est toujours remplacée par la même lettre chiffrée.</p>
        </div>
    </div>

    <h4 class="subsubsection-title">Exemple : Le chiffrement de César</h4>

    <div class="content-text">
        <p>Le chiffrement de César décale chaque lettre d'un nombre fixe de positions dans l'alphabet.</p>
        <p><strong>Clé :</strong> Le nombre de décalages (exemple : 3)</p>
    </div>

    <div class="visual-diagram">
        <div><strong>Alphabet normal :</strong></div>
        <div style="font-family: monospace; font-size: 1.2rem; margin: 1rem 0;">
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        </div>
        <div class="arrow">⬇️ Décalage de 3 positions</div>
        <div><strong>Alphabet chiffré :</strong></div>
        <div style="font-family: monospace; font-size: 1.2rem; margin: 1rem 0;">
            D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        </div>
    </div>

    <div class="content-text">
        <p><strong>Exemple de chiffrement :</strong></p>
        <ul>
            <li>Message clair : <code>RENARD</code></li>
            <li>Avec décalage de 3 : <code>UHQDUG</code></li>
        </ul>
        <p><strong>Détail :</strong></p>
        <ul>
            <li>R → U (R + 3)</li>
            <li>E → H (E + 3)</li>
            <li>N → Q (N + 3)</li>
            <li>A → D (A + 3)</li>
            <li>R → U (R + 3)</li>
            <li>D → G (D + 3)</li>
        </ul>
    </div>

    <div class="danger-fact">
        🚨 <strong>Faiblesse du chiffrement monoalphabétique :</strong><br>
        Très vulnérable à l'<strong>analyse de fréquence</strong> ! En français, la lettre "E" est la plus fréquente. Si on voit qu'une lettre apparaît souvent dans le message chiffré, c'est probablement le "E" chiffré.
    </div>

    <h3 class="subsection-title">1.2 Chiffrement polyalphabétique</h3>

    <div class="definition-box">
        <div class="definition-title">Définition</div>
        <div class="definition-content">
            <p>Un <strong>chiffrement polyalphabétique</strong> utilise plusieurs alphabets de substitution.</p>
            <p><strong>Caractéristique :</strong> Une même lettre peut être chiffrée différemment selon sa position dans le message.</p>
            <p><strong>Avantage :</strong> Résiste beaucoup mieux à l'analyse de fréquence.</p>
        </div>
    </div>

    <h4 class="subsubsection-title">Exemple : Le chiffrement de Vigenère</h4>

    <div class="content-text">
        <p>Utilise un <strong>mot-clé</strong> qui se répète pour déterminer le décalage de chaque lettre.</p>
    </div>

    <div class="content-text">
        <p><strong>Exemple :</strong></p>
        <ul>
            <li>Message : <code>RENARD</code></li>
            <li>Clé : <code>FOX</code> (qui se répète : FOXFOX)</li>
        </ul>
        <table class="exercise-table">
            <thead>
                <tr>
                    <th>Lettre du message</th>
                    <th>Lettre de la clé</th>
                    <th>Décalage</th>
                    <th>Lettre chiffrée</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>R</td><td>F</td><td>+5</td><td>W</td></tr>
                <tr><td>E</td><td>O</td><td>+14</td><td>S</td></tr>
                <tr><td>N</td><td>X</td><td>+23</td><td>K</td></tr>
                <tr><td>A</td><td>F</td><td>+5</td><td>F</td></tr>
                <tr><td>R</td><td>O</td><td>+14</td><td>F</td></tr>
                <tr><td>D</td><td>X</td><td>+23</td><td>A</td></tr>
            </tbody>
        </table>
        <p><strong>Résultat :</strong> <code>RENARD</code> devient <code>WSKFFA</code></p>
    </div>

    <div class="highlight-fact">
        💡 <strong>Remarque :</strong> Notez que les deux "R" du mot RENARD sont chiffrés différemment (W et F) grâce au mot-clé qui change !
    </div>

    <h3 class="subsection-title">1.3 Chiffrement mathématique</h3>

    <div class="definition-box">
        <div class="definition-title">Définition</div>
        <div class="definition-content">
            <p>Un <strong>chiffrement mathématique</strong> modélise le chiffrement comme une <strong>fonction</strong> appliquée au message, contrôlée par une <strong>clé</strong>.</p>
            <ul>
                <li><strong>Chiffrement :</strong> on note <code>c = E_k(m)</code> où <code>m</code> est le message clair, <code>k</code> la clé, <code>c</code> le message chiffré.</li>
                <li><strong>Déchiffrement :</strong> on note <code>m = D_k(c)</code> avec <code>D_k</code> la fonction inverse associée à la clé.</li>
            </ul>
            <p>Selon les algorithmes, <code>E_k</code> et <code>D_k</code> utilisent des opérations <strong>déterministes</strong> (décalage <em>modulo</em> 26, XOR, arithmétique modulaire, etc.).</p>
        </div>
    </div>

    <div class="highlight-fact">
        ✅ <strong>Propriété fondamentale :</strong> <code>D_k(E_k(m)) = m</code>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔐 Le chiffrement symétrique</h2>

    <div class="definition-box">
        <div class="definition-title">Principe</div>
        <div class="definition-content">
            <p>Le <strong>chiffrement symétrique</strong> utilise <strong>la même clé</strong> pour chiffrer et déchiffrer un message.</p>
            <p><strong>Analogie :</strong> Comme un cadenas avec une seule clé qui peut à la fois verrouiller et déverrouiller.</p>
        </div>
    </div>

    <div class="visual-diagram">
        <div style="display: flex; align-items: center; justify-content: center; gap: 2rem; flex-wrap: wrap;">
            <div>
                <div><strong>Alice</strong> 🦊</div>
                <div style="margin: 1rem 0;">Message clair</div>
                <div class="arrow">🔒 Chiffrement</div>
                <div class="key-box">🔑 Clé K</div>
            </div>
            <div class="arrow" style="font-size: 3rem;">→</div>
            <div style="background: rgba(231, 76, 60, 0.1); padding: 1rem; border-radius: 8px;">
                <strong>Message chiffré</strong><br>
                (incompréhensible)
            </div>
            <div class="arrow" style="font-size: 3rem;">→</div>
            <div>
                <div><strong>Bob</strong> 👨‍🔬</div>
                <div class="key-box">🔑 Clé K</div>
                <div class="arrow">🔓 Déchiffrement</div>
                <div style="margin: 1rem 0;">Message clair</div>
            </div>
        </div>
    </div>

    <div class="content-text">
        <p><strong>Étapes :</strong></p>
        <ol>
            <li>Alice et Bob se mettent d'accord sur une <strong>clé secrète K</strong> (en privé)</li>
            <li>Alice chiffre son message avec la clé K</li>
            <li>Alice envoie le message chiffré à Bob</li>
            <li>Bob déchiffre le message avec la même clé K</li>
        </ol>
    </div>

    <div class="highlight-fact">
        ✅ <strong>Avantage :</strong> Très rapide et efficace pour chiffrer de grandes quantités de données.
    </div>

    <div class="danger-fact">
        ❌ <strong>Inconvénient majeur :</strong> Comment Alice et Bob peuvent-ils se mettre d'accord sur la clé secrète de manière sécurisée ? Si Charlie intercepte la clé, tout est compromis !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🛠️ Exercices pratiques de chiffrement</h2>

    <h3 class="subsection-title">Rappel : La table ASCII</h3>

    <div class="content-text">
        <p>ASCII (American Standard Code for Information Interchange) est une table qui associe chaque caractère à un nombre.</p>
    </div>

    <div class="definition-box">
        <div class="definition-title">Quelques valeurs ASCII importantes</div>
        <div class="definition-content">
            <table class="exercise-table">
                <thead>
                    <tr>
                        <th>Caractère</th>
                        <th>Valeur ASCII (décimale)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>A</td><td>65</td></tr>
                    <tr><td>B</td><td>66</td></tr>
                    <tr><td>...</td><td>...</td></tr>
                    <tr><td>Z</td><td>90</td></tr>
                    <tr><td>a</td><td>97</td></tr>
                    <tr><td>b</td><td>98</td></tr>
                    <tr><td>...</td><td>...</td></tr>
                    <tr><td>z</td><td>122</td></tr>
                    <tr><td>0</td><td>48</td></tr>
                    <tr><td>1</td><td>49</td></tr>
                    <tr><td>Espace</td><td>32</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <h3 class="subsection-title">Exercice 1 : Chiffrement XOR</h3>

    <div class="definition-box">
        <div class="definition-title">Principe du XOR (OU exclusif)</div>
        <div class="definition-content">
            <p>L'opération XOR compare deux bits et retourne :</p>
            <ul>
                <li><strong>0</strong> si les bits sont identiques</li>
                <li><strong>1</strong> si les bits sont différents</li>
            </ul>
            <table class="exercise-table" style="width: 300px;">
                <thead>
                    <tr><th>A</th><th>B</th><th>A XOR B</th></tr>
                </thead>
                <tbody>
                    <tr><td>0</td><td>0</td><td>0</td></tr>
                    <tr><td>0</td><td>1</td><td>1</td></tr>
                    <tr><td>1</td><td>0</td><td>1</td></tr>
                    <tr><td>1</td><td>1</td><td>0</td></tr>
                </tbody>
            </table>
            <p><strong>Propriété magique :</strong> Si on applique XOR deux fois avec la même clé, on retrouve le message original !</p>
            <div class="code-block">
Message XOR Clé = Chiffré
Chiffré XOR Clé = Message
            </div>
        </div>
    </div>

    <div class="exercise-container">
        <div class="exercise-title">📝 Exercice : Chiffrer avec XOR</div>
        <div class="content-text">
            <p><strong>Message :</strong> <code>FOX</code></p>
            <p><strong>Clé :</strong> <code>KEY</code></p>
            <p><strong>Consigne :</strong> Chiffrer le message en utilisant l'opération XOR.</p>
        </div>
        
        <div class="content-text">
            <p><strong>Étape 1 : Convertir en ASCII</strong></p>
            <ul>
                <li>F = 70</li>
                <li>O = 79</li>
                <li>X = 88</li>
                <li>K = 75</li>
                <li>E = 69</li>
                <li>Y = 89</li>
            </ul>
        </div>

        <div class="content-text">
            <p><strong>Étape 2 : Convertir en binaire</strong></p>
            <ul>
                <li>F = 70 = 01000110</li>
                <li>K = 75 = 01001011</li>
            </ul>
        </div>

        <div class="content-text">
            <p><strong>Étape 3 : Appliquer XOR bit par bit</strong></p>
            <div class="code-block">
  01000110  (F)
⊕ 01001011  (K)
-----------
  00001101  = 13
            </div>
            <p>Le caractère ASCII 13 n'est pas imprimable, mais c'est normal en chiffrement !</p>
        </div>

        <div class="content-text">
            <p><strong>Exercice à faire :</strong> Complétez le chiffrement pour O⊕E et X⊕Y.</p>
        </div>
    </div>

    <h3 class="subsection-title">Exercice 2 : Chiffrement de César</h3>

    <div class="exercise-container">
        <div class="exercise-title">📝 Exercice : César avec décalage</div>
        <div class="content-text">
            <p><strong>Message à chiffrer :</strong> <code>RENARD ROUX</code></p>
            <p><strong>Clé (décalage) :</strong> 7</p>
            <p><strong>Consigne :</strong></p>
            <ol>
                <li>Chiffrer le message avec un décalage de 7</li>
                <li>Déchiffrer le message : <code>ZLJHYL</code> (décalage de 7)</li>
            </ol>
        </div>

        <div class="content-text">
            <p><strong>Aide :</strong></p>
            <p>Pour chiffrer, ajoutez 7 à chaque lettre. Si vous dépassez Z, revenez à A.</p>
            <p>Exemple : R + 7 = Y</p>
        </div>
    </div>

    <h3 class="subsection-title">Exercice 3 : Chiffrement de Vigenère</h3>

    <div class="exercise-container">
        <div class="exercise-title">📝 Exercice : Vigenère</div>
        <div class="content-text">
            <p><strong>Message :</strong> <code>ALICE</code></p>
            <p><strong>Clé :</strong> <code>BOB</code></p>
            <p><strong>Consigne :</strong> Chiffrer le message.</p>
        </div>

        <div class="content-text">
            <p><strong>Méthode :</strong></p>
            <ol>
                <li>Répéter la clé : <code>ALICE</code> → <code>BOBBO</code></li>
                <li>Pour chaque lettre, ajouter le décalage correspondant :
                    <ul>
                        <li>A + B (décalage 1) = B</li>
                        <li>L + O (décalage 14) = Z</li>
                        <li>I + B (décalage 1) = J</li>
                        <li>C + B (décalage 1) = D</li>
                        <li>E + O (décalage 14) = S</li>
                    </ul>
                </li>
                <li>Message chiffré : <code>BZJDS</code></li>
            </ol>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔢 Algorithmes de chiffrement modernes</h2>

    <h3 class="subsection-title">AES (Advanced Encryption Standard)</h3>

    <div class="definition-box">
        <div class="definition-title">Présentation</div>
        <div class="definition-content">
            <p><strong>AES</strong> est l'algorithme de chiffrement symétrique le plus utilisé aujourd'hui.</p>
            <ul>
                <li><strong>Adopté en 2001</strong> par le gouvernement américain</li>
                <li><strong>Tailles de clé :</strong> 128, 192 ou 256 bits</li>
                <li><strong>Utilisé partout :</strong> WiFi (WPA2/WPA3), VPN, HTTPS, disques chiffrés</li>
                <li><strong>Sécurité :</strong> Considéré comme incassable avec les moyens actuels</li>
            </ul>
        </div>
    </div>

    <div class="highlight-fact">
        💡 <strong>Exemple :</strong> Quand vous vous connectez à un réseau WiFi protégé, vos données sont chiffrées avec AES !
    </div>

    <div class="content-text">
        <p><strong>Temps pour casser AES-256 par force brute :</strong></p>
        <p>Avec les ordinateurs les plus puissants actuels : environ <strong>plusieurs milliards d'années</strong></p>
    </div>

    <h3 class="subsection-title">DES et 3DES</h3>

    <div class="definition-box">
        <div class="definition-title">DES (Data Encryption Standard)</div>
        <div class="definition-content">
            <ul>
                <li>Ancien standard (1977)</li>
                <li>Clé de 56 bits</li>
                <li><strong>⚠️ Obsolète :</strong> Trop facile à casser aujourd'hui</li>
            </ul>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">3DES (Triple DES)</div>
        <div class="definition-content">
            <ul>
                <li>Applique DES trois fois de suite</li>
                <li>Plus sécurisé que DES</li>
                <li><strong>⚠️ En phase de dépréciation :</strong> Remplacé par AES</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔑 Le problème du chiffrement symétrique : l'échange de clés</h2>

    <div class="danger-fact">
        🚨 <strong>Le grand problème :</strong><br>
        Comment Alice et Bob peuvent-ils échanger la clé secrète de manière sécurisée ?
    </div>

    <div class="visual-diagram">
        <div><strong>Scénario problématique :</strong></div>
        <div style="margin: 2rem 0;">
            <div>🦊 <strong>Alice</strong> : "Bob, utilisons la clé : 🔑 X7k#mP92"</div>
            <div class="arrow">📧 ⬇️</div>
            <div style="background: rgba(231, 76, 60, 0.2); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #e74c3c;">👤 Charlie intercepte la clé !</strong><br>
                Il peut maintenant déchiffrer TOUS les messages !
            </div>
            <div class="arrow">📧 ⬇️</div>
            <div>👨‍🔬 <strong>Bob</strong> : "OK, j'ai la clé !"</div>
        </div>
    </div>

    <div class="content-text">
        <p><strong>Solutions historiques (peu pratiques) :</strong></p>
        <ul>
            <li><strong>Rencontre physique :</strong> Alice et Bob se rencontrent en personne → Impossible à grande échelle</li>
            <li><strong>Courrier sécurisé :</strong> Envoyer la clé par voie postale → Lent et coûteux</li>
            <li><strong>Messager de confiance :</strong> Utiliser un tiers → Risque de compromission</li>
        </ul>
    </div>

    <div class="warning-fact">
        ⚠️ <strong>Problème d'échelle :</strong><br>
        Imaginez une entreprise de 1000 employés. Avec le chiffrement symétrique, chaque paire d'employés doit avoir sa propre clé secrète.<br>
        <strong>Nombre de clés nécessaires :</strong> 1000 × 999 / 2 = <strong>499 500 clés</strong> à gérer ! 😱
    </div>

    <div class="highlight-fact">
        💡 <strong>La solution :</strong> Le chiffrement asymétrique !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔐🔓 Le chiffrement asymétrique (ou à clé publique)</h2>

    <div class="definition-box">
        <div class="definition-title">Principe révolutionnaire</div>
        <div class="definition-content">
            <p>Le <strong>chiffrement asymétrique</strong> utilise <strong>deux clés différentes</strong> :</p>
            <ul>
                <li>Une <strong>clé publique</strong> 🔑 (peut être partagée avec tout le monde)</li>
                <li>Une <strong>clé privée</strong> 🔒 (doit rester secrète)</li>
            </ul>
            <p><strong>Propriété magique :</strong></p>
            <ul>
                <li>Ce qui est chiffré avec la clé <strong>publique</strong> ne peut être déchiffré qu'avec la clé <strong>privée</strong></li>
                <li>Ce qui est chiffré avec la clé <strong>privée</strong> ne peut être déchiffré qu'avec la clé <strong>publique</strong></li>
            </ul>
        </div>
    </div>

    <div class="visual-diagram">
        <div><strong>Configuration des clés :</strong></div>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap; gap: 2rem;">
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1.5rem; border-radius: 12px; flex: 1; min-width: 200px;">
                <div style="font-size: 2rem;">🦊</div>
                <div><strong>Alice</strong></div>
                <div style="margin: 1rem 0;">
                    <div class="key-box" style="background: rgba(46, 204, 113, 0.2); border-color: #27ae60;">🔑 Clé publique A</div>
                    <div style="font-size: 0.9rem; color: #7f8c8d;">(visible par tous)</div>
                </div>
                <div>
                    <div class="key-box" style="background: rgba(231, 76, 60, 0.2); border-color: #e74c3c;">🔒 Clé privée A</div>
                    <div style="font-size: 0.9rem; color: #7f8c8d;">(secrète)</div>
                </div>
            </div>
            <div style="background: rgba(155, 89, 182, 0.1); padding: 1.5rem; border-radius: 12px; flex: 1; min-width: 200px;">
                <div style="font-size: 2rem;">👨‍🔬</div>
                <div><strong>Bob</strong></div>
                <div style="margin: 1rem 0;">
                    <div class="key-box" style="background: rgba(46, 204, 113, 0.2); border-color: #27ae60;">🔑 Clé publique B</div>
                    <div style="font-size: 0.9rem; color: #7f8c8d;">(visible par tous)</div>
                </div>
                <div>
                    <div class="key-box" style="background: rgba(231, 76, 60, 0.2); border-color: #e74c3c;">🔒 Clé privée B</div>
                    <div style="font-size: 0.9rem; color: #7f8c8d;">(secrète)</div>
                </div>
            </div>
        </div>
    </div>

    <h3 class="subsection-title">Comment Alice envoie un message confidentiel à Bob</h3>

    <div class="visual-diagram">
        <div style="text-align: left; max-width: 800px; margin: 0 auto;">
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong>Étape 1 :</strong> Alice récupère la <strong>clé publique de Bob</strong> 🔑 (disponible publiquement)
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong>Étape 2 :</strong> Alice chiffre son message avec la clé publique de Bob<br>
                <code>Message clair + 🔑 Clé publique Bob = Message chiffré</code>
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong>Étape 3 :</strong> Alice envoie le message chiffré (même si Charlie l'intercepte, il ne peut rien faire !)
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(155, 89, 182, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong>Étape 4 :</strong> Bob déchiffre avec sa <strong>clé privée</strong> 🔒 (lui seul la possède)<br>
                <code>Message chiffré + 🔒 Clé privée Bob = Message clair</code>
            </div>
        </div>
    </div>

    <div class="highlight-fact">
        ✅ <strong>Avantages :</strong><br>
        • Pas besoin d'échanger de secret avant de communiquer<br>
        • Les clés publiques peuvent être partagées librement<br>
        • Chaque personne n'a besoin que d'une paire de clés (publique/privée)
    </div>

    <div class="warning-fact">
        ❌ <strong>Inconvénient :</strong><br>
        <strong>Beaucoup plus lent</strong> que le chiffrement symétrique (100 à 1000 fois plus lent).
    </div>

    <div class="highlight-fact">
        💡 <strong>Solution hybride (utilisée dans HTTPS) :</strong><br>
        1. Utiliser le chiffrement asymétrique pour échanger une clé symétrique de manière sécurisée<br>
        2. Utiliser ensuite le chiffrement symétrique (rapide) pour les données<br>
        <strong>Le meilleur des deux mondes !</strong>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔢 RSA : L'algorithme de chiffrement asymétrique</h2>

    <div class="definition-box">
        <div class="definition-title">Présentation</div>
        <div class="definition-content">
            <p><strong>RSA</strong> (Rivest-Shamir-Adleman, 1977) est l'algorithme de chiffrement asymétrique le plus célèbre.</p>
            <ul>
                <li>Basé sur la difficulté de factoriser de très grands nombres</li>
                <li>Tailles de clés courantes : 2048 ou 4096 bits</li>
                <li>Utilisé dans : HTTPS, SSH, signatures numériques, certificats SSL/TLS</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Principe mathématique simplifié</h3>

    <div class="content-text">
        <p><strong>Génération des clés (version très simplifiée) :</strong></p>
        <ol>
            <li>Choisir deux <strong>grands nombres premiers</strong> p et q (exemple : p=61, q=53)</li>
            <li>Calculer <strong>n = p × q</strong> (exemple : n = 61 × 53 = 3233)</li>
            <li>Calculer φ(n) = (p-1) × (q-1) (exemple : φ(n) = 60 × 52 = 3120)</li>
            <li>Choisir e tel que 1 < e < φ(n) et e soit premier avec φ(n) (exemple : e = 17)</li>
            <li>Calculer d tel que (d × e) mod φ(n) = 1 (exemple : d = 2753)</li>
        </ol>
        <p><strong>Résultat :</strong></p>
        <ul>
            <li><strong>Clé publique :</strong> (n, e) = (3233, 17)</li>
            <li><strong>Clé privée :</strong> (n, d) = (3233, 2753)</li>
        </ul>
    </div>

    <div class="warning-fact">
        ⚠️ <strong>Important :</strong> Dans la réalité, p et q sont des nombres premiers de plusieurs centaines de chiffres ! L'exemple ci-dessus est juste pour comprendre le principe.
    </div>

    <div class="content-text">
        <p><strong>Sécurité de RSA :</strong></p>
        <p>La sécurité repose sur le fait qu'il est <strong>extrêmement difficile</strong> de retrouver p et q à partir de n quand n est très grand.</p>
        <p>Exemple : Factoriser un nombre de 2048 bits prendrait <strong>des milliards d'années</strong> avec les ordinateurs actuels.</p>
    </div>

    <h3 class="subsection-title">Autres algorithmes asymétriques</h3>

    <div class="definition-box">
        <div class="definition-title">Courbes elliptiques (ECC - Elliptic Curve Cryptography)</div>
        <div class="definition-content">
            <ul>
                <li><strong>Avantage :</strong> Sécurité équivalente à RSA avec des clés beaucoup plus courtes</li>
                <li>Exemple : Une clé ECC de 256 bits ≈ sécurité d'une clé RSA de 3072 bits</li>
                <li><strong>Utilisé dans :</strong> Bitcoin, appareils mobiles, cartes à puce</li>
                <li><strong>Plus rapide</strong> que RSA</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">👥 Le problème : Human-in-the-Middle</h2>

    <div class="content-text">
        <p>Nous avons vu que le chiffrement asymétrique résout le problème de l'échange de clés. Mais un nouveau problème apparaît : <strong>Comment être sûr qu'on communique avec la bonne personne ?</strong></p>
    </div>

    <div class="danger-fact">
        🚨 <strong>Attaque Human-in-the-Middle (HITM)</strong>
    </div>

    <div class="visual-diagram">
        <div style="text-align: left; max-width: 800px; margin: 0 auto;">
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>1.</strong> 🦊 Alice demande la clé publique de Bob
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(231, 76, 60, 0.2); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>2.</strong> 👤 <strong>Charlie intercepte</strong> et envoie <strong>SA propre clé publique</strong> à Alice en se faisant passer pour Bob
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>3.</strong> 🦊 Alice chiffre son message avec la clé publique de Charlie (qu'elle croit être celle de Bob)
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(231, 76, 60, 0.2); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>4.</strong> 👤 <strong>Charlie déchiffre</strong> le message, le lit, puis le rechiffre avec la vraie clé publique de Bob
            </div>
            <div class="arrow">⬇️</div>
            <div style="background: rgba(155, 89, 182, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>5.</strong> 👨‍🔬 Bob reçoit le message, sans se douter de rien
            </div>
        </div>
    </div>

    <div class="content-text">
        <p><strong>Résultat :</strong> Charlie peut lire et même <strong>modifier</strong> tous les messages entre Alice et Bob sans qu'ils s'en rendent compte !</p>
    </div>

    <div class="warning-fact">
        ⚠️ <strong>Problème fondamental :</strong><br>
        Le chiffrement asymétrique garantit la <strong>confidentialité</strong>, mais pas l'<strong>authenticité</strong> ni l'<strong>intégrité</strong> !<br>
        <strong>Comment être sûr que la clé publique appartient vraiment à Bob ?</strong>
    </div>

    <div class="highlight-fact">
        💡 <strong>La solution :</strong> Les signatures numériques et les certificats !
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">#️⃣ Le hachage : garantir l'intégrité</h2>

    <div class="definition-box">
        <div class="definition-title">Qu'est-ce qu'un hash (hachage) ?</div>
        <div class="definition-content">
            <p>Un <strong>hash</strong> (ou <strong>empreinte numérique</strong>) est le résultat d'une <strong>fonction de hachage</strong> appliquée à des données.</p>
            <p><strong>Fonction de hachage :</strong> Transforme des données de taille quelconque en une chaîne de caractères de taille fixe.</p>
        </div>
    </div>

    <div class="visual-diagram">
        <div style="max-width: 600px; margin: 0 auto; text-align: left;">
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong>Donnée (taille variable) :</strong><br>
                "Les renards roux chassent de nuit"
            </div>
            <div class="arrow">⬇️ Fonction de hachage (SHA-256)</div>
            <div style="background: rgba(155, 89, 182, 0.1); padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                <strong>Hash (taille fixe - 256 bits) :</strong><br>
                <code style="word-break: break-all;">a3f5b8c9e1d...</code>
            </div>
        </div>
    </div>

    <h3 class="subsection-title">Propriétés d'une bonne fonction de hachage</h3>

    <div class="definition-box">
        <div class="definition-content">
            <ol>
                <li><strong>Déterministe :</strong> Le même message donne toujours le même hash</li>
                <li><strong>Rapide à calculer</strong></li>
                <li><strong>Effet avalanche :</strong> Un changement minime dans le message change complètement le hash</li>
                <li><strong>Irréversible :</strong> Impossible de retrouver le message à partir du hash</li>
                <li><strong>Résistance aux collisions :</strong> Très difficile de trouver deux messages différents ayant le même hash</li>
            </ol>
        </div>
    </div>

    <h3 class="subsection-title">Démonstration de l'effet avalanche</h3>

    <div class="content-text">
        <p><strong>Message 1 :</strong> <code>RENARD</code></p>
        <p><strong>Hash SHA-256 :</strong> <code>7a8f3e9c...</code> (64 caractères hexadécimaux)</p>
        <br>
        <p><strong>Message 2 :</strong> <code>RENART</code> (une seule lettre changée !)</p>
        <p><strong>Hash SHA-256 :</strong> <code>b2d4c1f8...</code> (complètement différent !)</p>
    </div>

    <h3 class="subsection-title">Algorithmes de hachage courants</h3>

    <div class="definition-box">
        <div class="definition-title">SHA-256 (Secure Hash Algorithm)</div>
        <div class="definition-content">
            <ul>
                <li>Produit un hash de <strong>256 bits</strong> (64 caractères hexadécimaux)</li>
                <li><strong>Standard actuel</strong> recommandé</li>
                <li>Utilisé dans : Bitcoin, certificats SSL, signatures</li>
            </ul>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">MD5 (Message Digest 5)</div>
        <div class="definition-content">
            <ul>
                <li>Produit un hash de <strong>128 bits</strong> (32 caractères hexadécimaux)</li>
                <li><strong>⚠️ OBSOLÈTE :</strong> Vulnérable aux collisions</li>
                <li>Encore utilisé pour vérifier l'intégrité de fichiers (checksums)</li>
            </ul>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">SHA-1</div>
        <div class="definition-content">
            <ul>
                <li>Produit un hash de <strong>160 bits</strong></li>
                <li><strong>⚠️ Déprécié :</strong> Collisions trouvées en 2017</li>
                <li>Remplacé par SHA-256</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Exercice pratique : Calculer un hash</h3>

    <div class="exercise-container">
        <div class="exercise-title">📝 Exercice : Vérifier l'intégrité d'un fichier</div>
        <div class="content-text">
            <p><strong>Contexte :</strong> Alice veut envoyer un fichier de données sur les renards à Bob. Elle veut s'assurer que le fichier n'est pas corrompu pendant le transfert.</p>
            
            <p><strong>Méthode :</strong></p>
            <ol>
                <li>Alice calcule le hash SHA-256 du fichier : <code>a3f5b8c9e1d2...</code></li>
                <li>Alice envoie le fichier ET le hash à Bob (séparément)</li>
                <li>Bob reçoit le fichier et calcule son hash</li>
                <li>Bob compare les deux hash :
                    <ul>
                        <li>✅ <strong>Identiques</strong> → Le fichier est intègre</li>
                        <li>❌ <strong>Différents</strong> → Le fichier a été modifié ou corrompu</li>
                    </ul>
                </li>
            </ol>
        </div>

        <div class="content-text">
            <p><strong>Exercice pratique (Windows) :</strong></p>
            <div class="code-block">
# Ouvrir PowerShell et calculer le hash d'un fichier
Get-FileHash -Algorithm SHA256 nom_fichier.txt
            </div>
        </div>

        <div class="content-text">
            <p><strong>Exercice pratique (Linux/Mac) :</strong></p>
            <div class="code-block">
# Dans le terminal
sha256sum nom_fichier.txt
            </div>
        </div>

        <div class="content-text">
            <p><strong>À faire :</strong> Créez un fichier texte avec votre nom, calculez son hash, modifiez une seule lettre, recalculez le hash et observez la différence !</p>
        </div>
    </div>

    <h3 class="subsection-title">Utilisations du hachage</h3>

    <div class="content-text">
        <ul>
            <li><strong>Vérification d'intégrité :</strong> Téléchargements, sauvegardes</li>
            <li><strong>Stockage de mots de passe :</strong> On ne stocke jamais les mots de passe en clair, seulement leurs hash</li>
            <li><strong>Signatures numériques :</strong> On signe le hash du document, pas le document entier</li>
            <li><strong>Blockchain :</strong> Chaque bloc contient le hash du bloc précédent</li>
            <li><strong>Détection de doublons :</strong> Deux fichiers identiques ont le même hash</li>
        </ul>
    </div>
</div>


<div class="concept-section">
    <h2 class="section-title">✍️ La signature numérique</h2>

    <div class="definition-box">
        <div class="definition-title">Principe</div>
        <div class="definition-content">
            <p>Une <strong>signature numérique</strong> est l'équivalent électronique d'une signature manuscrite.</p>
            <p>Elle permet de garantir :</p>
            <ul>
                <li><strong>Authenticité :</strong> Le message provient bien de l'expéditeur prétendu</li>
                <li><strong>Intégrité :</strong> Le message n'a pas été modifié</li>
                <li><strong>Non-répudiation :</strong> L'expéditeur ne peut pas nier avoir envoyé le message</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Comment fonctionne la signature numérique ?</h3>

    <div class="visual-diagram">
        <div style="text-align: left; max-width: 800px; margin: 0 auto;">
            <div style="background: rgba(52, 152, 219, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
                <strong>📝 ÉTAPE 1 : Alice signe son message</strong>
                <div style="margin-top: 1rem;">
                    <div>1️⃣ Alice calcule le <strong>hash</strong> de son message</div>
                    <div class="code-block" style="margin: 0.5rem 0;">
Message : "Les renards roux..."
↓ SHA-256
Hash : a3f5b8c9e1d2f4a7...
                    </div>
                    <div>2️⃣ Alice chiffre le hash avec sa <strong>clé privée</strong> 🔒</div>
                    <div class="code-block" style="margin: 0.5rem 0;">
Hash + 🔒 Clé privée Alice = ✍️ SIGNATURE
                    </div>
                    <div>3️⃣ Alice envoie : <strong>Message + Signature</strong></div>
                </div>
            </div>

            <div class="arrow">📧 ⬇️ Transmission</div>

            <div style="background: rgba(155, 89, 182, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
                <strong>✅ ÉTAPE 2 : Bob vérifie la signature</strong>
                <div style="margin-top: 1rem;">
                    <div>1️⃣ Bob calcule le <strong>hash</strong> du message reçu</div>
                    <div class="code-block" style="margin: 0.5rem 0;">
Message reçu
↓ SHA-256
Hash calculé : a3f5b8c9e1d2f4a7...
                    </div>
                    <div>2️⃣ Bob déchiffre la signature avec la <strong>clé publique d'Alice</strong> 🔑</div>
                    <div class="code-block" style="margin: 0.5rem 0;">
✍️ Signature + 🔑 Clé publique Alice = Hash original
                    </div>
                    <div>3️⃣ Bob compare les deux hash :</div>
                    <div class="code-block" style="margin: 0.5rem 0;">
Hash calculé == Hash original ?
✅ OUI → Message authentique et intègre
❌ NON → Message modifié ou fausse signature
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="highlight-fact">
        ✅ <strong>Garanties de la signature numérique :</strong><br>
        • <strong>Authenticité :</strong> Seule Alice possède sa clé privée, donc seule elle peut créer cette signature<br>
        • <strong>Intégrité :</strong> Si le message est modifié, le hash ne correspondra plus<br>
        • <strong>Non-répudiation :</strong> Alice ne peut pas nier avoir signé (sa clé privée est unique)
    </div>

    <h3 class="subsection-title">Différence entre chiffrement et signature</h3>

    <div class="content-text">
        <table class="exercise-table">
            <thead>
                <tr>
                    <th>Aspect</th>
                    <th>Chiffrement</th>
                    <th>Signature</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Objectif</strong></td>
                    <td>Confidentialité</td>
                    <td>Authenticité + Intégrité</td>
                </tr>
                <tr>
                    <td><strong>Clé utilisée pour créer</strong></td>
                    <td>🔑 Clé publique du destinataire</td>
                    <td>🔒 Clé privée de l'émetteur</td>
                </tr>
                <tr>
                    <td><strong>Clé utilisée pour lire</strong></td>
                    <td>🔒 Clé privée du destinataire</td>
                    <td>🔑 Clé publique de l'émetteur</td>
                </tr>
                <tr>
                    <td><strong>Protège contre</strong></td>
                    <td>Lecture non autorisée</td>
                    <td>Usurpation d'identité et modification</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="warning-fact">
        💡 <strong>Mnémotechnique :</strong><br>
        • <strong>Chiffrer</strong> = Utiliser la clé publique du <strong>DESTINATAIRE</strong> (je veux que lui seul puisse lire)<br>
        • <strong>Signer</strong> = Utiliser la clé privée de l'<strong>ÉMETTEUR</strong> (je prouve que c'est moi qui envoie)
    </div>

    <h3 class="subsection-title">Exercice : Chiffrement ET Signature</h3>

    <div class="exercise-container">
        <div class="exercise-title">📝 Exercice : Combiner confidentialité et authenticité</div>
        <div class="content-text">
            <p><strong>Contexte :</strong> Alice veut envoyer un message à Bob qui soit à la fois <strong>confidentiel</strong> ET <strong>authentifié</strong>.</p>
            
            <p><strong>Question :</strong> Dans quel ordre Alice doit-elle effectuer les opérations ?</p>
            
            <p><strong>Option A :</strong></p>
            <ol>
                <li>Signer le message avec sa clé privée</li>
                <li>Chiffrer le message (+ signature) avec la clé publique de Bob</li>
            </ol>

            <p><strong>Option B :</strong></p>
            <ol>
                <li>Chiffrer le message avec la clé publique de Bob</li>
                <li>Signer le message chiffré avec sa clé privée</li>
            </ol>

            <p><strong>Réponse :</strong> <strong>Option A</strong> est la bonne pratique !</p>
            <ul>
                <li>On signe d'abord (pour prouver que c'est Alice)</li>
                <li>Puis on chiffre tout (pour la confidentialité)</li>
            </ul>
        </div>

        <div class="visual-diagram">
            <div style="text-align: left;">
                <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                    <strong>1.</strong> Message original : "Découverte sur les renards..."
                </div>
                <div class="arrow">⬇️ Signature (clé privée Alice)</div>
                <div style="background: rgba(52, 152, 219, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                    <strong>2.</strong> Message + Signature d'Alice
                </div>
                <div class="arrow">⬇️ Chiffrement (clé publique Bob)</div>
                <div style="background: rgba(231, 76, 60, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                    <strong>3.</strong> Tout est chiffré (illisible pour Charlie)
                </div>
                <div class="arrow">⬇️ Bob reçoit</div>
                <div style="background: rgba(155, 89, 182, 0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                    <strong>4.</strong> Bob déchiffre (clé privée Bob)<br>
                    <strong>5.</strong> Bob vérifie la signature (clé publique Alice)<br>
                    ✅ Message confidentiel + authentifié
                </div>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🏛️ Les autorités de certification (CA)</h2>

    <div class="content-text">
        <p>Nous avons vu que les signatures numériques résolvent le problème d'authenticité. Mais une question demeure : <strong>Comment être sûr que la clé publique d'Alice appartient vraiment à Alice ?</strong></p>
    </div>

    <div class="definition-box">
        <div class="definition-title">Qu'est-ce qu'une Autorité de Certification ?</div>
        <div class="definition-content">
            <p>Une <strong>Autorité de Certification (CA - Certificate Authority)</strong> est une entité de confiance qui :</p>
            <ul>
                <li>Vérifie l'identité des demandeurs</li>
                <li>Émet des <strong>certificats numériques</strong> qui lient une clé publique à une identité</li>
                <li>Signe ces certificats avec sa propre clé privée</li>
            </ul>
            <p><strong>Exemples de CA :</strong> DigiCert, Let's Encrypt, GlobalSign, Sectigo</p>
        </div>
    </div>

    <div class="definition-box">
        <div class="definition-title">Qu'est-ce qu'un certificat numérique ?</div>
        <div class="definition-content">
            <p>Un <strong>certificat numérique</strong> est un document électronique qui contient :</p>
            <ul>
                <li>L'identité du propriétaire (nom, organisation, domaine)</li>
                <li>Sa clé publique</li>
                <li>La période de validité</li>
                <li>La signature de l'Autorité de Certification</li>
            </ul>
            <p><strong>Standard :</strong> X.509</p>
        </div>
    </div>

    <h3 class="subsection-title">Chaîne de confiance</h3>

    <div class="visual-diagram">
        <div style="text-align: left; max-width: 700px; margin: 0 auto;">
            <div style="background: linear-gradient(135deg, rgba(46, 204, 113, 0.2), rgba(39, 174, 96, 0.1)); padding: 1.5rem; border-radius: 12px; border: 2px solid #27ae60; margin: 1rem 0;">
                <div style="text-align: center; font-size: 2rem;">🏛️</div>
                <strong>AC Racine (Root CA)</strong><br>
                <em style="font-size: 0.9rem;">Préinstallée dans votre navigateur/OS<br>Auto-signée, hautement sécurisée</em>
            </div>
            <div class="arrow">⬇️ Signe</div>
            <div style="background: rgba(52, 152, 219, 0.2); padding: 1.5rem; border-radius: 12px; border: 2px solid #3498db; margin: 1rem 0;">
                <div style="text-align: center; font-size: 2rem;">🏢</div>
                <strong>AC Intermédiaire</strong><br>
                <em style="font-size: 0.9rem;">Utilisée au quotidien pour émettre des certificats</em>
            </div>
            <div class="arrow">⬇️ Signe</div>
            <div style="background: rgba(155, 89, 182, 0.2); padding: 1.5rem; border-radius: 12px; border: 2px solid #9b59b6; margin: 1rem 0;">
                <div style="text-align: center; font-size: 2rem;">🌐</div>
                <strong>Certificat du site web</strong><br>
                <em style="font-size: 0.9rem;">Exemple : www.banque.fr</em><br>
                Contient : clé publique du site + identité + signature de l'AC
            </div>
        </div>
    </div>

    <h3 class="subsection-title">Vérification d'un certificat</h3>

    <div class="content-text">
        <p><strong>Quand vous visitez un site HTTPS, votre navigateur :</strong></p>
        <ol>
            <li>Reçoit le certificat du site</li>
            <li>Vérifie la signature de l'AC intermédiaire</li>
            <li>Vérifie la signature de l'AC racine (qui est dans votre navigateur)</li>
            <li>Vérifie la date de validité</li>
            <li>Vérifie que le nom de domaine correspond</li>
        </ol>
        <p><strong>Si tout est OK :</strong> 🔒 Cadenas vert (ou icône de sécurité)</p>
        <p><strong>Si problème :</strong> ⚠️ Avertissement de sécurité</p>
    </div>

    <div class="highlight-fact">
        💡 <strong>Exercice pratique :</strong><br>
        Dans votre navigateur, cliquez sur le cadenas à côté de l'URL d'un site HTTPS et explorez les informations du certificat !<br>
        Vous verrez : l'autorité de certification, la date d'expiration, la clé publique, etc.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌍 Exemples concrets dans la vie courante</h2>

    <h3 class="subsection-title">HTTPS (Navigation web sécurisée)</h3>

    <div class="definition-box">
        <div class="definition-title">Comment fonctionne HTTPS ?</div>
        <div class="definition-content">
            <p><strong>HTTPS = HTTP + TLS/SSL</strong></p>
            <p><strong>Protocole TLS (Transport Layer Security) :</strong></p>
            <ol>
                <li><strong>Handshake (poignée de main) :</strong>
                    <ul>
                        <li>Le serveur envoie son certificat (contenant sa clé publique)</li>
                        <li>Le navigateur vérifie le certificat</li>
                        <li>Le navigateur génère une <strong>clé de session symétrique</strong> aléatoire</li>
                        <li>Le navigateur chiffre cette clé avec la clé publique du serveur</li>
                        <li>Le serveur déchiffre avec sa clé privée</li>
                    </ul>
                </li>
                <li><strong>Communication :</strong>
                    <ul>
                        <li>Tout le reste de la communication utilise le <strong>chiffrement symétrique</strong> (AES) avec la clé de session</li>
                        <li>C'est rapide et sécurisé !</li>
                    </ul>
                </li>
            </ol>
        </div>
    </div>

    <div class="highlight-fact">
        ✅ <strong>HTTPS garantit :</strong><br>
        • <strong>Confidentialité :</strong> Personne ne peut lire vos données<br>
        • <strong>Intégrité :</strong> Les données ne sont pas modifiées<br>
        • <strong>Authenticité :</strong> Vous communiquez bien avec le bon site
    </div>

    <h3 class="subsection-title">WhatsApp - Chiffrement de bout en bout</h3>

    <div class="definition-box">
        <div class="definition-title">Comment fonctionne WhatsApp ?</div>
        <div class="definition-content">
            <p>WhatsApp utilise le <strong>protocole Signal</strong> :</p>
            <ul>
                <li><strong>Chiffrement de bout en bout (E2EE) :</strong> Seuls l'expéditeur et le destinataire peuvent lire les messages</li>
                <li>Même WhatsApp ne peut pas lire vos messages !</li>
                <li>Chaque conversation a ses propres clés de chiffrement</li>
                <li>Les clés changent régulièrement (Perfect Forward Secrecy)</li>
            </ul>
            <p><strong>Technique :</strong></p>
            <ul>
                <li>Échange de clés avec <strong>Diffie-Hellman</strong></li>
                <li>Chiffrement avec <strong>AES-256</strong></li>
                <li>Signatures avec <strong>Curve25519</strong></li>
            </ul>
        </div>
    </div>

    <div class="visual-diagram">
        <div style="font-size: 2rem; margin: 1rem 0;">📱 → 🔒 → 🔐 → 🔓 → 📱</div>
        <div><strong>Alice → Chiffré sur son téléphone → Transit → Déchiffré sur le téléphone de Bob</strong></div>
        <div style="margin-top: 1rem; color: #27ae60; font-weight: 600;">✅ WhatsApp ne peut pas lire les messages !</div>
    </div>

    <h3 class="subsection-title">Telegram - Chiffrement client-serveur (par défaut)</h3>

    <div class="definition-box">
        <div class="definition-title">Différence avec WhatsApp</div>
        <div class="definition-content">
            <p><strong>Mode par défaut (discussions normales) :</strong></p>
            <ul>
                <li>Chiffrement <strong>client-serveur</strong>, pas de bout en bout</li>
                <li>Messages chiffrés entre vous et le serveur Telegram</li>
                <li>Telegram peut techniquement lire vos messages</li>
                <li>Avantage : Synchronisation sur tous vos appareils</li>
            </ul>
            <p><strong>Mode "Secret Chat" :</strong></p>
            <ul>
                <li>Chiffrement de bout en bout (E2EE)</li>
                <li>Pas de synchronisation cloud</li>
                <li>Messages auto-destructibles</li>
                <li>Protocole maison : MTProto 2.0</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Signal - Le champion de la confidentialité</h3>

    <div class="definition-box">
        <div class="definition-title">Pourquoi Signal est recommandé ?</div>
        <div class="definition-content">
            <ul>
                <li><strong>Chiffrement E2EE par défaut</strong> (toujours actif)</li>
                <li><strong>Open source :</strong> Le code est public et auditable</li>
                <li><strong>Métadonnées minimales :</strong> Signal collecte très peu d'informations</li>
                <li><strong>Perfect Forward Secrecy :</strong> Si votre clé est compromise, les anciens messages restent sécurisés</li>
                <li>Recommandé par Edward Snowden et les experts en sécurité</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Email - PGP/GPG</h3>

    <div class="definition-box">
        <div class="definition-title">Pretty Good Privacy (PGP)</div>
        <div class="definition-content">
            <p>PGP permet de chiffrer et signer des emails :</p>
            <ul>
                <li>Chaque utilisateur a une paire de clés (publique/privée)</li>
                <li>Les clés publiques sont partagées (serveurs de clés)</li>
                <li>Permet de chiffrer et signer des emails</li>
                <li><strong>Problème :</strong> Complexe à mettre en place pour les utilisateurs non techniques</li>
            </ul>
            <p><strong>Alternative moderne :</strong> ProtonMail (chiffrement E2EE automatique)</p>
        </div>
    </div>

    <h3 class="subsection-title">VPN (Virtual Private Network)</h3>

    <div class="definition-box">
        <div class="definition-title">Comment fonctionne un VPN ?</div>
        <div class="definition-content">
            <ul>
                <li>Crée un <strong>tunnel chiffré</strong> entre votre appareil et le serveur VPN</li>
                <li>Tout votre trafic passe par ce tunnel</li>
                <li>Chiffrement : généralement <strong>AES-256</strong></li>
                <li>Protocoles : OpenVPN, WireGuard, IKEv2/IPsec</li>
            </ul>
            <p><strong>Avantages :</strong></p>
            <ul>
                <li>Cache votre adresse IP</li>
                <li>Protège sur les réseaux WiFi publics</li>
                <li>Contourne les restrictions géographiques</li>
            </ul>
            <p><strong>⚠️ Important :</strong> Vous devez faire confiance au fournisseur VPN (il peut voir votre trafic) !</p>
        </div>
    </div>

    <h3 class="subsection-title">Blockchain et Bitcoin</h3>

    <div class="definition-box">
        <div class="definition-title">Cryptographie dans la blockchain</div>
        <div class="definition-content">
            <ul>
                <li><strong>Hachage SHA-256 :</strong> Chaque bloc contient le hash du bloc précédent</li>
                <li><strong>Clés publiques/privées :</strong> Votre portefeuille = paire de clés</li>
                <li><strong>Signatures numériques :</strong> Chaque transaction est signée avec votre clé privée</li>
                <li><strong>Preuve de travail :</strong> Mining = trouver un hash avec des contraintes spécifiques</li>
            </ul>
        </div>
    </div>
</div>
