# Fiche d'exercices : Web et HTTP

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

.exercise-card {
    background: var(--md-default-bg-color);
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 3px solid;
    width: 100%;
    max-width: 100%;
    min-height: fit-content;
}

.exercise-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background-color: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.medium {
    background-color: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background-color: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.exercise-title {
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: var(--md-default-fg-color);
}

.exercise-content {
    color: var(--md-default-fg-color--light);
    line-height: 1.5;
    margin-bottom: 1rem;
}

.toggle-solution {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.toggle-solution:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution-wrapper {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
}

.solution-wrapper.show {
    max-height: 2000px;
    margin-top: 1rem;
}

.solution {
    background: rgba(102, 126, 234, 0.05);
    border-radius: 8px;
    padding: 1rem;
    border-left: 3px solid #667eea;
}

.solution pre {
    background: rgba(0, 0, 0, 0.05);
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
    margin: 0;
}

.solution code {
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
}
</style>

## 📚 Partie 1 : Protocole HTTP et URLs

<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 1 - Anatomie d'une URL</h4>
        <div class="exercise-content">
            <strong>Analysez cette URL et identifiez ses composants :</strong><br><br>
            <code>https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section</code><br><br>
            Identifiez :<br>
            1. Le protocole<br>
            2. Le nom de domaine<br>
            3. Le port<br>
            4. Le chemin<br>
            5. Les paramètres de requête<br>
            6. L'ancre (fragment)
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Composants de l'URL :</strong><br>
                1. <strong>Protocole :</strong> https<br>
                2. <strong>Nom de domaine :</strong> www.example.com<br>
                3. <strong>Port :</strong> 8080<br>
                4. <strong>Chemin :</strong> /path/to/page<br>
                5. <strong>Paramètres :</strong> param1=value1&param2=value2<br>
                6. <strong>Ancre :</strong> section
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 2 - Méthodes HTTP</h4>
        <div class="exercise-content">
            <strong>Associez chaque méthode HTTP à son usage :</strong><br><br>
            <strong>Méthodes :</strong> GET, POST, PUT, DELETE, HEAD, PATCH<br><br>
            <strong>Usages :</strong><br>
            1. Récupérer des données sans les modifier<br>
            2. Envoyer des données pour créer une ressource<br>
            3. Remplacer complètement une ressource<br>
            4. Supprimer une ressource<br>
            5. Récupérer seulement les en-têtes<br>
            6. Modifier partiellement une ressource
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Associations :</strong><br>
                • GET → 1. Récupérer des données sans les modifier<br>
                • POST → 2. Envoyer des données pour créer une ressource<br>
                • PUT → 3. Remplacer complètement une ressource<br>
                • DELETE → 4. Supprimer une ressource<br>
                • HEAD → 5. Récupérer seulement les en-têtes<br>
                • PATCH → 6. Modifier partiellement une ressource
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 3 - Codes de statut HTTP</h4>
        <div class="exercise-content">
            <strong>Expliquez la signification de ces codes de statut :</strong><br><br>
            1. 200<br>
            2. 301<br>
            3. 404<br>
            4. 401<br>
            5. 500<br>
            6. 403<br>
            7. 302<br>
            8. 418
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Significations :</strong><br>
                1. <strong>200 OK :</strong> Requête réussie<br>
                2. <strong>301 Moved Permanently :</strong> Redirection permanente<br>
                3. <strong>404 Not Found :</strong> Ressource non trouvée<br>
                4. <strong>401 Unauthorized :</strong> Authentification requise<br>
                5. <strong>500 Internal Server Error :</strong> Erreur serveur<br>
                6. <strong>403 Forbidden :</strong> Accès interdit<br>
                7. <strong>302 Found :</strong> Redirection temporaire<br>
                8. <strong>418 I'm a teapot :</strong> Code humoristique (RFC 2324)
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 4 - En-têtes HTTP</h4>
        <div class="exercise-content">
            <strong>Analysez cette requête HTTP et répondez aux questions :</strong><br><br>
            <pre>
GET /api/users HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer abc123
Content-Type: application/json
            </pre><br>
            1. Quelle est la méthode utilisée ?<br>
            2. Quel type de contenu est accepté ?<br>
            3. Comment l'utilisateur s'authentifie-t-il ?<br>
            4. Y a-t-il une erreur dans cette requête ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse :</strong><br>
                1. <strong>Méthode :</strong> GET<br>
                2. <strong>Type accepté :</strong> application/json<br>
                3. <strong>Authentification :</strong> Bearer token (abc123)<br>
                4. <strong>Erreur :</strong> Content-Type ne devrait pas être présent dans une requête GET (pas de corps)
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 5 - Session et cookies</h4>
        <div class="exercise-content">
            <strong>Analysez cet échange HTTP et expliquez le mécanisme :</strong><br><br>
            <strong>Requête 1 :</strong><br>
            <pre>POST /login HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username=alice&password=secret</pre><br>
            <strong>Réponse 1 :</strong><br>
            <pre>HTTP/1.1 200 OK
Set-Cookie: sessionid=xyz789; HttpOnly; Secure
Location: /dashboard</pre><br>
            <strong>Requête 2 :</strong><br>
            <pre>GET /dashboard HTTP/1.1
Cookie: sessionid=xyz789</pre><br>
            1. Que se passe-t-il dans la première requête ?<br>
            2. Que fait le serveur avec Set-Cookie ?<br>
            3. Pourquoi HttpOnly et Secure sont-ils importants ?<br>
            4. Comment le client prouve-t-il son identité dans la requête 2 ?
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Analyse du mécanisme :</strong><br>
                1. <strong>Requête 1 :</strong> L'utilisateur envoie ses identifiants de connexion<br>
                2. <strong>Set-Cookie :</strong> Le serveur crée une session et envoie un identifiant de session<br>
                3. <strong>Sécurité :</strong><br>
                   • HttpOnly : empêche l'accès JavaScript (protection XSS)<br>
                   • Secure : transmission uniquement en HTTPS<br>
                4. <strong>Requête 2 :</strong> Le client renvoie automatiquement le cookie pour prouver son identité
            </div>
        </div>
    </div>
</div>

## 📚 Partie 2 : HTML et CSS

<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="difficulty-badge intro">Introduction 🦊</div>
        <h4 class="exercise-title">Exercice 6 - Structure HTML</h4>
        <div class="exercise-content">
            <strong>Corrigez ce code HTML qui contient des erreurs :</strong><br><br>
            <pre>
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Ma page
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Titre principal&lt;/h1&gt;
    &lt;p&gt;Un paragraphe avec &lt;b&gt;du texte en gras&lt;/p&gt;
    &lt;img src="image.jpg"&gt;
    &lt;ul&gt;
        &lt;li&gt;Item 1
        &lt;li&gt;Item 2&lt;/li&gt;
    &lt;/ul&gt;
&lt;/body&gt;
            </pre>
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Code corrigé :</strong><br>
                <pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Ma page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Titre principal&lt;/h1&gt;
    &lt;p&gt;Un paragraphe avec &lt;b&gt;du texte en gras&lt;/b&gt;&lt;/p&gt;
    &lt;img src="image.jpg" alt="Description"&gt;
    &lt;ul&gt;
        &lt;li&gt;Item 1&lt;/li&gt;
        &lt;li&gt;Item 2&lt;/li&gt;
    &lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;
                </pre>
                <strong>Erreurs corrigées :</strong><br>
                • Ajout du DOCTYPE<br>
                • Fermeture de la balise title<br>
                • Fermeture de la balise b<br>
                • Fermeture de la balise p<br>
                • Ajout de l'attribut alt à img<br>
                • Fermeture de la première balise li<br>
                • Fermeture de la balise html
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 7 - Sélecteurs CSS</h4>
        <div class="exercise-content">
            <strong>Écrivez les sélecteurs CSS pour :</strong><br><br>
            1. Tous les paragraphes<br>
            2. L'élément avec l'id "header"<br>
            3. Tous les éléments avec la classe "highlight"<br>
            4. Les liens dans les listes<br>
            5. Le premier paragraphe de chaque article<br>
            6. Les éléments survolés par la souris
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Sélecteurs CSS :</strong><br>
                1. <code>p</code><br>
                2. <code>#header</code><br>
                3. <code>.highlight</code><br>
                4. <code>li a</code> ou <code>ul a</code><br>
                5. <code>article p:first-child</code><br>
                6. <code>:hover</code>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 8 - Responsive Design</h4>
        <div class="exercise-content">
            <strong>Créez un CSS responsive pour cette structure :</strong><br><br>
            <pre>
&lt;div class="container"&gt;
    &lt;div class="sidebar"&gt;Menu&lt;/div&gt;
    &lt;div class="content"&gt;Contenu principal&lt;/div&gt;
&lt;/div&gt;
            </pre><br>
            <strong>Contraintes :</strong><br>
            • Desktop : sidebar 25%, content 75%<br>
            • Tablet : sidebar 30%, content 70%<br>
            • Mobile : sidebar au-dessus, pleine largeur
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>CSS Responsive :</strong><br>
                <pre>
.container {
    display: flex;
}

.sidebar {
    width: 25%;
    background: #f0f0f0;
}

.content {
    width: 75%;
    padding: 1rem;
}

/* Tablet */
@media (max-width: 768px) {
    .sidebar {
        width: 30%;
    }
    .content {
        width: 70%;
    }
}

/* Mobile */
@media (max-width: 480px) {
    .container {
        flex-direction: column;
    }
    .sidebar, .content {
        width: 100%;
    }
}
                </pre>
            </div>
        </div>
    </div>
</div>

## 📚 Partie 3 : JavaScript et interactivité

<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="difficulty-badge medium">Moyen 🦊🦊</div>
        <h4 class="exercise-title">Exercice 9 - Manipulation du DOM</h4>
        <div class="exercise-content">
            <strong>Écrivez le JavaScript pour :</strong><br><br>
            1. Changer le texte d'un élément avec l'id "title"<br>
            2. Ajouter la classe "active" à tous les boutons<br>
            3. Créer un nouvel élément &lt;p&gt; et l'ajouter au body<br>
            4. Supprimer tous les éléments avec la classe "temp"
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Code JavaScript :</strong><br>
                <pre>
// 1. Changer le texte
document.getElementById('title').textContent = 'Nouveau titre';

// 2. Ajouter une classe à tous les boutons
document.querySelectorAll('button').forEach(btn => {
    btn.classList.add('active');
});

// 3. Créer et ajouter un paragraphe
const p = document.createElement('p');
p.textContent = 'Nouveau paragraphe';
document.body.appendChild(p);

// 4. Supprimer les éléments temporaires
document.querySelectorAll('.temp').forEach(el => {
    el.remove();
});
                </pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
        <h4 class="exercise-title">Exercice 10 - Requêtes AJAX</h4>
        <div class="exercise-content">
            <strong>Créez une fonction qui :</strong><br><br>
            1. Fait une requête GET vers "/api/users"<br>
            2. Affiche les données dans une liste HTML<br>
            3. Gère les erreurs de réseau<br>
            4. Affiche un indicateur de chargement
        </div>
        <button class="toggle-solution" onclick="toggleSolution(this)">
            <span class="arrow">→</span> Voir la correction
        </button>
        <div class="solution-wrapper">
            <div class="solution">
                <strong>Fonction AJAX complète :</strong><br>
                <pre>
async function loadUsers() {
    const loadingEl = document.getElementById('loading');
    const usersList = document.getElementById('users-list');
    const errorEl = document.getElementById('error');
    
    try {
        // Afficher le chargement
        loadingEl.style.display = 'block';
        errorEl.style.display = 'none';
        
        // Faire la requête
        const response = await fetch('/api/users');
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const users = await response.json();
        
        // Afficher les utilisateurs
        usersList.innerHTML = '';
        users.forEach(user => {
            const li = document.createElement('li');
            li.textContent = user.name;
            usersList.appendChild(li);
        });
        
    } catch (error) {
        // Gérer les erreurs
        errorEl.textContent = 'Erreur: ' + error.message;
        errorEl.style.display = 'block';
    } finally {
        // Cacher le chargement
        loadingEl.style.display = 'none';
    }
}
                </pre>
            </div>
        </div>
    </div>
</div>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices
function toggleSolution(button) {
    const wrapper = button.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (wrapper.classList.contains('show')) {
        wrapper.classList.remove('show');
        arrow.textContent = '→';
        arrow.style.transform = 'rotate(0deg)';
    } else {
        wrapper.classList.add('show');
        arrow.textContent = '↓';
        arrow.style.transform = 'rotate(90deg)';
    }
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Aucune initialisation spécifique nécessaire pour cette fiche
});
</script>