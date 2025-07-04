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

# 📚 Notice sur HTML et création d'un site web basique

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">1. Qu'est-ce que HTML ?</h3>
        <div class="course-content">
            <strong>HTML</strong> (HyperText Markup Language) est le langage de balisage utilisé pour structurer le contenu des pages web. Chaque page web est un fichier HTML qui contient des balises permettant de définir différents éléments comme des titres, des paragraphes, des images, des liens, etc.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">2. Structure d'un fichier HTML</h3>
        <div class="course-content">
            Un fichier HTML est structuré de manière simple. Voici la structure de base d'un document HTML :<br><br>``<code>html<br><!DOCTYPE html><br><html lang="fr"><br><head><br>    <meta charset="UTF-8"><br>    <meta name="viewport" content="width=device-width, initial-scale=1.0"><br>    <title>Titre de la page</title><br></head><br><body><br>    <!-- Contenu visible de la page --><br>    <h1>Bienvenue sur mon site</h1><br>    <p>Ceci est un paragraphe.</p><br></body><br></html><br></code>``<br><br>Explication :<br><br>	-	<!DOCTYPE html> : Indique que le document utilise HTML5.<br>	-	<html> : La balise qui contient tout le contenu HTML.<br>	-	<head> : Section contenant des informations sur la page (métadonnées), comme le titre.<br>	-	<meta charset="UTF-8"> : Spécifie l’encodage de caractères (UTF-8).<br>	-	<title> : Définit le titre qui apparaît dans l’onglet du navigateur.<br>	-	<body> : Contient le contenu visible par l’utilisateur (titres, paragraphes, images, etc.).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les principales balises HTML</h3>
        <div class="course-content">
            ### Titres<br><br>``<code>html<br>    <h1>Mon titre principal</h1><br>    <h2>Mon sous-titre</h2><br></code>`<code><br>Ces balises Titres vont de h1 à h6, où h1 est le plus grand titre.<br><br>### Paragraphes<br><br>Les paragraphes sont définis par la balise p.<br><br></code>`<code>html<br>    <p>Ceci est un paragraphe.</p><br></code>`<code><br><br>### Liens<br><br>Les liens sont créés à l'aide de la balise a.<br><br></code>`<code>html<br>    <a href="https://www.example.com">Visiter Example.com</a><br></code>`<code><br><br>### Images<br><br>Les images sont insérées par la balise img.<br><br></code>`<code>html<br>    <img src="source de l'image" alt="Mon image"><br></code>`<code><br><br>### Listes Non ordonnées<br><br>Les listes à puces ordonnées sont définies grâce à ul.<br><br></code>`<code>html<br>    <ul><br>        <li>Item 1</li><br>        <li>Item 2</li><br>    </ul><br></code>`<code><br><br>### Listes Ordonnées<br><br>Les listes ordonnées sont définies grâce à ol.<br><br></code>`<code>html<br>    <ol><br>        <li>Item 1</li><br>        <li>Item 2</li><br>    </ol><br></code>``
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">But de la séance</h3>
        <div class="course-content">
            Vous devrez reproduire la page web suivante à l'aide des balises que vous avez vu.<br>Vous avez aussi le site [w3school](https://www.w3schools.com/html/).<br><br>L'image à utiliser : [image de maya](./maya.png)
        </div>
    </div>
    
</div>