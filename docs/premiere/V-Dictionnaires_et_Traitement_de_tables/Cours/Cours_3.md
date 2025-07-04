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

# 📚 Introduction aux bases de données et au langage SQL

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Introduction aux Bases de Données</h3>
        <div class="course-content">
            ### Qu’est-ce qu'une Base de Données ?<br><br>Une <strong>base de données</strong> est un ensemble organisé d'informations structurées de manière à pouvoir être facilement accessible, gérée et mise à jour.<br><br>On peut associer cela à un grand tableau organisé en colonnes, nommées attributs (à l'instar des fichiers CSV).<br><br>### Pourquoi utiliser une Base de Données ?<br><br>Le but principal des bases de données est de faciliter :<br><br>- <strong>Le stockage organisé</strong> : Les informations sont rangées de façon structurée, souvent sous forme de tables, ce qui facilite la gestion.<br>- <strong>La recherche efficace</strong> : On peut rapidement trouver des données spécifiques grâce à des requêtes.<br>- <strong>La maintenance</strong> : On peut mettre à jour ou supprimer des informations de façon sécurisée.<br>- <strong>L'intégrité et la sécurité des données</strong> : Les bases de données relationnelles assurent que les données sont fiables et protégées.
        </div>
    </div>
    
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">Historique des Bases de Données Relationnelles</h3>
        <div class="course-content">
            ### Origines  <br><br>Dans les années 1960, les bases de données étaient très basiques et souvent peu optimisées.  <br>En 1970, <strong>Edgar F. Codd</strong> propose le <strong>modèle relationnel</strong>. Son idée était de simplifier la gestion des données en les organisant sous forme de tables reliées par des relations logiques.<br><br>### Le modèle relationnel<br><br>Dans ce modèle, les données sont organisées en <strong>tables</strong>.  <br>Une table est constituée de :<br><br>- <strong>Lignes</strong> (ou enregistrements) : Chaque ligne représente un élément unique (par exemple, un étudiant).<br>- <strong>Colonnes</strong> (ou attributs) : Chaque colonne décrit une caractéristique de cet élément (par exemple, le nom, l'âge, la classe).<br><br>Exemple d'une table <code>Etudiants</code> :<br><br>| id  | nom       | age | classe   |<br>|-----|-----------|-----|----------|<br>| 1   | Alice     | 17  | Terminale|<br>| 2   | Bob       | 16  | Première |<br>| 3   | Charlie   | 18  | Terminale|<br><br>---
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Introduction au SQL</h3>
        <div class="course-content">
            ### Qu'est-ce que le SQL ?<br>Le <strong>SQL</strong> (Structured Query Language) est le langage utilisé pour interagir avec une base de données relationnelle. Il permet de <strong>poser des questions</strong> à la base de données et d’obtenir des réponses sous forme de tables. On parle de <strong>requêtes SQL</strong> pour désigner ces questions.<br><br>### Principes de base du SQL<br><br>Le SQL permet de réaliser des requêtes de demande de données suivant des critères plus facilement et de manière plus sécurisée en communiquant avec une base de données normalisée.<br><br>#### Projeter des données : <code>SELECT</code><br><br>La commande <code>SELECT</code> permet de <strong>récupérer des lignes spécifiques</strong> (appelés <strong>enregistrements</strong>) d'une table.<br><br>!!! danger<br>    Attention, il ne faut pas confondre la commande SELECT avec la sélection. Sélectionner des données revient à réaliser une projection <strong>avec des contraintes</strong>.<br><br>*Exemple* : Supposons que nous voulons obtenir les informations de tous les étudiants.<br><br>``<code>sql<br>SELECT * FROM Etudiants;<br></code>`<code><br><br></code>SELECT *<code> signifie retourner toutes les colonnes”. FROM Etudiants indique que l’on travaille avec la table Etudiants.<br><br>*Exemple* : Supposons que l'on veut afficher uniquement le nom et l'âge des étudiants<br><br></code>`<code>sql<br>SELECT nom, age FROM Etudiants;<br></code>`<code><br><br>#### Sélectionner des attributs<br><br>Pour sélectionner les valeurs suivant des contraintes / conditions, on doit ajouter à notre requête le mot-clef WHERE avec une condition à la suite.<br><br>Par exemple, si l'on souhaite aficher le nom des étudiants qui ont plus de 17 ans, on va utiliser la requête suivante:<br><br></code>`<code>sql<br>SELECT nom FROM Etudiants WHERE age > 17;<br></code>`<code><br><br>Ici, on veut afficher le nom des étudiants avec l'instruction </code>SELECT nom FROM Etudiants<code> mais en ajouter la contrainte </code>WHERE age > 17` permet d'obtenir tous les noms uniquement de ceux ayant plus de 17 ans.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Activité : SQL Murder Mystery</h3>
        <div class="course-content">
            Pour appliquer cela, vous pouvez vous diriger vers le site "SQL Murder Mystery" qui permet de résoudre une enquête d'un crime à l'aide de bases de données et de requête en langage SQL.  <br>*(Attention, le site est uniquement en anglais)*.<br><br>Vous pouvez rejoindre le site [en cliquant ici](https://mystery.knightlab.com)
        </div>
    </div>
    
</div>