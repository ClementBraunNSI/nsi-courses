<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction aux bases de données et au langage SQL</title>
</head>
<body>

<style>
/* Styles modernes pour le cours Web */
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

.fact-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
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

.code-example pre {
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: #e2e8f0;
}

.property-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.property-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.property-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.property-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.property-values {
    color: #7f8c8d;
    line-height: 1.6;
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Introduction aux bases de données et au langage SQL</h1>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Introduction aux Bases de Données</h2>
    
    <div class="definition-box">
        <div class="definition-title">🗄️ Qu'est-ce qu'une Base de Données ?</div>
        <div class="definition-content">
            Une <strong>base de données</strong> est un ensemble organisé d'informations structurées de manière à pouvoir être facilement accessible, gérée et mise à jour.<br><br>
            On peut associer cela à un grand tableau organisé en colonnes, nommées attributs (à l'instar des fichiers CSV).
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🎯 Pourquoi utiliser une Base de Données ?</div>
        <div class="info-content">
            Le but principal des bases de données est de faciliter :
            <ul>
                <li><strong>Le stockage organisé</strong> : Les informations sont rangées de façon structurée, souvent sous forme de tables, ce qui facilite la gestion.</li>
                <li><strong>La recherche efficace</strong> : On peut rapidement trouver des données spécifiques grâce à des requêtes.</li>
                <li><strong>La maintenance</strong> : On peut mettre à jour ou supprimer des informations de façon sécurisée.</li>
                <li><strong>L'intégrité et la sécurité des données</strong> : Les bases de données relationnelles assurent que les données sont fiables et protégées.</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Historique des Bases de Données Relationnelles</h2>
    
    <div class="definition-box">
        <div class="definition-title">🕰️ Origines</div>
        <div class="definition-content">
            Dans les années 1960, les bases de données étaient très basiques et souvent peu optimisées.<br>
            En 1970, <strong>Edgar F. Codd</strong> propose le <strong>modèle relationnel</strong>. Son idée était de simplifier la gestion des données en les organisant sous forme de tables reliées par des relations logiques.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🔗 Le modèle relationnel</div>
        <div class="info-content">
            Dans ce modèle, les données sont organisées en <strong>tables</strong>.<br>
            Une table est constituée de :
            <ul>
                <li><strong>Lignes</strong> (ou enregistrements) : Chaque ligne représente un élément unique (par exemple, un étudiant).</li>
                <li><strong>Colonnes</strong> (ou attributs) : Chaque colonne décrit une caractéristique de cet élément (par exemple, le nom, l'âge, la classe).</li>
            </ul>
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <h3>📊 Exemple d'une table `Etudiants`</h3>
            <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
                <thead>
                    <tr style="background: rgba(102, 126, 234, 0.1);">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">id</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">nom</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">age</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">classe</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">1</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Alice</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">17</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Terminale</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">2</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Bob</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">16</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Première</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;">3</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Charlie</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">18</td>
                        <td style="border: 1px solid #ddd; padding: 8px;">Terminale</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

---

<div class="timeline-section">
    <h2 class="section-title">📖 Introduction au SQL</h2>
    
    <div class="definition-box">
        <div class="definition-title">💾 Qu'est-ce que le SQL ?</div>
        <div class="definition-content">
            Le <strong>SQL</strong> (Structured Query Language) est le langage utilisé pour interagir avec une base de données relationnelle. Il permet de <strong>poser des questions</strong> à la base de données et d'obtenir des réponses sous forme de tables. On parle de <strong>requêtes SQL</strong> pour désigner ces questions.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">⚙️ Principes de base du SQL</div>
        <div class="info-content">
            Le SQL permet de réaliser des requêtes de demande de données suivant des critères plus facilement et de manière plus sécurisée en communiquant avec une base de données normalisée.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📊 Projeter des données : SELECT</div>
        <div class="definition-content">
            La commande <code>SELECT</code> permet de <strong>récupérer des lignes spécifiques</strong> (appelés <strong>enregistrements</strong>) d'une table.
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>⚠️ Attention :</strong> Il ne faut pas confondre la commande SELECT avec la sélection. Sélectionner des données revient à réaliser une projection <strong>avec des contraintes</strong>.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple : Obtenir toutes les informations des étudiants</div>
        <pre>SELECT * FROM Etudiants;</pre>
        <p style="color: #a0aec0; margin-top: 1rem; font-size: 0.9rem;"><code>SELECT *</code> signifie "retourner toutes les colonnes". <code>FROM Etudiants</code> indique que l'on travaille avec la table Etudiants.</p>
    </div>
    
    <div class="code-example">
        <div class="code-title">🎯 Exemple : Afficher uniquement le nom et l'âge</div>
        <pre>SELECT nom, age FROM Etudiants;</pre>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔍 Sélectionner des attributs avec WHERE</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Utilisation de WHERE</div>
        <div class="definition-content">
            Pour sélectionner les valeurs suivant des contraintes / conditions, on doit ajouter à notre requête le mot-clef <code>WHERE</code> avec une condition à la suite.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">📝 Exemple : Étudiants de plus de 17 ans</div>
        <pre>SELECT nom FROM Etudiants WHERE age > 17;</pre>
        <p style="color: #a0aec0; margin-top: 1rem; font-size: 0.9rem;">Ici, on veut afficher le nom des étudiants avec l'instruction <code>SELECT nom FROM Etudiants</code> mais en ajoutant la contrainte <code>WHERE age > 17</code> permet d'obtenir tous les noms uniquement de ceux ayant plus de 17 ans.</p>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🕵️ Activité : SQL Murder Mystery</h2>
    
    <div class="info-box">
        <div class="info-title">🎮 Mise en pratique</div>
        <div class="info-content">
            Pour appliquer cela, vous pouvez vous diriger vers le site "SQL Murder Mystery" qui permet de résoudre une enquête d'un crime à l'aide de bases de données et de requête en langage SQL.<br>
            <em>(Attention, le site est uniquement en anglais)</em>.<br><br>
            Vous pouvez rejoindre le site <a href="https://mystery.knightlab.com" target="_blank" style="color: #667eea; text-decoration: none; font-weight: bold;">en cliquant ici</a>
        </div>
    </div>
</div>

</body>
</html>