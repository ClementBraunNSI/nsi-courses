<style>
/* Styles modernes pour le cours HTML */
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

.tags-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.tag-category {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.tag-category:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.tag-category-title {
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    color: #2c3e50;
}

.tag-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.tag-list li {
    margin: 0.5rem 0;
    padding: 0.3rem 0;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 0.9rem;
    color: #7f8c8d;
}

.tag-list li:last-child {
    border-bottom: none;
}

.tag-list code {
    background: rgba(102, 126, 234, 0.1);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    color: #667eea;
    font-weight: 600;
}
</style>

<div class="course-header">
    <h1 class="course-title">🌐 HTML : le langage du Web</h1>
    <p class="course-subtitle">HyperText Markup Language - Le fondement des pages web</p>
</div>

<div class="timeline-section">
    <div class="definition-box">
        <div class="definition-title">📖 Qu'est-ce que HTML ?</div>
        <div class="definition-content">
            <strong>HTML</strong> (HyperText Markup Language) est le langage de balisage standard utilisé pour créer et structurer le contenu des pages web. Créé par Tim Berners-Lee en 1991, HTML utilise un système de balises pour définir la structure et le contenu d'une page web.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🏗️ Structure d'un document HTML</h2>
    
    <div class="info-box">
        <div class="info-title">📋 Structure de base</div>
        <div class="info-content">
            Voici la structure de base d'un document HTML :
        </div>
    </div>

    <div class="code-example">
        <div class="code-title">💻 Structure HTML complète</div>
        <pre>
&lt;!DOCTYPE html&gt;
&lt;html lang="fr"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Titre de la page&lt;/title&gt;
    &lt;link rel="stylesheet" href="styles.css"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;Titre principal&lt;/h1&gt;
        &lt;nav&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Accueil&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;À propos&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Contact&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/nav&gt;
    &lt;/header&gt;
    
    &lt;main&gt;
        &lt;section&gt;
            &lt;h2&gt;Section 1&lt;/h2&gt;
            &lt;p&gt;Contenu de la section 1.&lt;/p&gt;
        &lt;/section&gt;
        
        &lt;section&gt;
            &lt;h2&gt;Section 2&lt;/h2&gt;
            &lt;p&gt;Contenu de la section 2.&lt;/p&gt;
        &lt;/section&gt;
    &lt;/main&gt;
    
    &lt;footer&gt;
        &lt;p&gt;&copy; 2023 Mon Site Web&lt;/p&gt;
    &lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;
        </pre>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🏷️ Les principales balises HTML</h2>
    
    <div class="info-box">
        <div class="info-title">📚 Classification des balises</div>
        <div class="info-content">
            Les balises HTML sont organisées en différentes catégories selon leur fonction :
        </div>
    </div>
    
    <div class="tags-grid">
        <div class="tag-category">
            <div class="tag-category-title">🏗️ Balises de structure</div>
            <ul class="tag-list">
                <li><code>&lt;!DOCTYPE html&gt;</code> : Déclare le type de document (HTML5)</li>
                <li><code>&lt;html&gt;</code> : Élément racine du document</li>
                <li><code>&lt;head&gt;</code> : Contient les métadonnées</li>
                <li><code>&lt;body&gt;</code> : Contient le contenu visible</li>
                <li><code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;footer&gt;</code> : Balises sémantiques</li>
                <li><code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;nav&gt;</code> : Structure du contenu</li>
            </ul>
        </div>
        
        <div class="tag-category">
            <div class="tag-category-title">📝 Balises de texte</div>
            <ul class="tag-list">
                <li><code>&lt;h1&gt;</code> à <code>&lt;h6&gt;</code> : Titres de différents niveaux</li>
                <li><code>&lt;p&gt;</code> : Paragraphe</li>
                <li><code>&lt;strong&gt;</code> : Texte important (généralement en gras)</li>
                <li><code>&lt;em&gt;</code> : Texte mis en emphase (généralement en italique)</li>
            </ul>
        </div>
        
        <div class="tag-category">
            <div class="tag-category-title">🔗 Balises de lien et média</div>
            <ul class="tag-list">
                <li><code>&lt;a href="url"&gt;</code> : Lien hypertexte</li>
                <li><code>&lt;img src="image.jpg" alt="description"&gt;</code> : Image</li>
                <li><code>&lt;video&gt;</code>, <code>&lt;audio&gt;</code> : Éléments multimédias</li>
            </ul>
        </div>
        
        <div class="tag-category">
            <div class="tag-category-title">📋 Balises de liste</div>
            <ul class="tag-list">
                <li><code>&lt;ul&gt;</code> : Liste non ordonnée (à puces)</li>
                <li><code>&lt;ol&gt;</code> : Liste ordonnée (numérotée)</li>
                <li><code>&lt;li&gt;</code> : Élément de liste</li>
            </ul>
        </div>
        
        <div class="tag-category">
            <div class="tag-category-title">📊 Balises de tableau</div>
            <ul class="tag-list">
                <li><code>&lt;table&gt;</code> : Définit un tableau</li>
                <li><code>&lt;tr&gt;</code> : Ligne de tableau</li>
                <li><code>&lt;th&gt;</code> : Cellule d'en-tête</li>
                <li><code>&lt;td&gt;</code> : Cellule de données</li>
            </ul>
        </div>
        
        <div class="tag-category">
            <div class="tag-category-title">📝 Balises de formulaire</div>
            <ul class="tag-list">
                <li><code>&lt;form&gt;</code> : Définit un formulaire</li>
                <li><code>&lt;input&gt;</code> : Champ de saisie</li>
                <li><code>&lt;textarea&gt;</code> : Zone de texte multiligne</li>
                <li><code>&lt;button&gt;</code> : Bouton</li>
                <li><code>&lt;select&gt;</code> et <code>&lt;option&gt;</code> : Liste déroulante</li>
            </ul>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📝 Formulaires et transmission de données</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Les formulaires HTML</div>
        <div class="definition-content">
            Les formulaires HTML permettent aux utilisateurs d'envoyer des données au serveur. Ils sont définis par la balise <code>&lt;form&gt;</code> et contiennent divers éléments interactifs comme des champs de texte, des cases à cocher, des boutons radio, etc.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🏗️ Structure d'un formulaire</div>
        <div class="info-content">

            <div class="code-example">
                <div class="code-title">💻 Exemple de formulaire</div>
                <pre>
&lt;form action="/traitement.php" method="post"&gt;
    &lt;label for="nom"&gt;Nom :&lt;/label&gt;
    &lt;input type="text" id="nom" name="nom" required&gt;
    
    &lt;label for="email"&gt;Email :&lt;/label&gt;
    &lt;input type="email" id="email" name="email" required&gt;
    
    &lt;label for="message"&gt;Message :&lt;/label&gt;
    &lt;textarea id="message" name="message"&gt;&lt;/textarea&gt;
    
    &lt;button type="submit"&gt;Envoyer&lt;/button&gt;
&lt;/form&gt;
                </pre>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>📌 Attributs importants de la balise &lt;form&gt; :</strong><br>
            • <strong>action</strong> : URL où les données du formulaire seront envoyées<br>
            • <strong>method</strong> : Méthode HTTP utilisée pour envoyer les données (GET ou POST)
        </div>
    </div>
</div>
