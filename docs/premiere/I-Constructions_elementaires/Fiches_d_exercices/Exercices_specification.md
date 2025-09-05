# Fiche d'exercices : Bonnes pratique de développement

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

/* Styles pour les contextes d'exercices difficiles */
.context-container {
    margin-bottom: 2rem;
    border: 2px solid #F44336;
    border-radius: 12px;
    overflow: hidden;
    background: rgba(244, 67, 54, 0.02);
}

.context-header {
    background: linear-gradient(135deg, #F44336 0%, #D32F2F 100%);
    color: white;
    padding: 1rem 1.5rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    user-select: none;
}

.context-header:hover {
    background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
    transform: translateY(-1px);
}

.context-header .arrow {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}

.context-header.active .arrow {
    transform: rotate(90deg);
}

.context-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background: white;
}

.context-content.show {
    max-height: 10000px;
    padding: 1rem;
}

.context-exercises {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

/* Uniformiser la hauteur des cartes d'exercices dans les contextes */
.context-exercises .exercise-card {
    min-height: 200px;
    align-items: stretch;
}

.context-exercises .exercise-content-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100%;
}

.context-exercises .exercise-content {
    flex-grow: 1;
}

.context-exercises .toggle-solution {
    margin-top: auto;
    align-self: flex-start;
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

.exercise-content-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* Modal pour les solutions */
.solution-modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(3px);
}

.solution-modal.show {
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.3s ease;
}

.solution-content {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 2rem;
    max-width: 80%;
    max-height: 80%;
    overflow-y: auto;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    position: relative;
    animation: slideIn 0.3s ease;
}

.solution-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #f44336;
    color: white;
    border: none;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    cursor: pointer;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s ease;
}

.solution-close:hover {
    background: #d32f2f;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideIn {
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.solution-wrapper {
    display: none;
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.intro:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
}

.exercise-card.easy {
    border-left-color: #2196F3;
}

.exercise-card.easy:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(33, 150, 243, 0.4);
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.medium:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 152, 0, 0.4);
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.exercise-card.hard:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(244, 67, 54, 0.4);
}

.exercise-card.important {
    border-left-color: #ff8c42;
    background: linear-gradient(135deg, rgba(255, 140, 66, 0.05) 0%, rgba(255, 140, 66, 0.02) 100%);
}

.exercise-card.important:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 140, 66, 0.4);
}

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.1rem;
    font-weight: 600;
}

.exercise-content {
    margin-bottom: 1rem;
    line-height: 1.6;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.easy {
    background: rgba(33, 150, 243, 0.1);
    color: #2196F3;
}

.difficulty-badge.medium {
    background: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.difficulty-badge.important {
    background: rgba(255, 140, 66, 0.1);
    color: #ff8c42;
}

.toggle-solution {
    background: #cccccc;
    color: #666666;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: not-allowed;
    font-size: 0.9rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    opacity: 0.6;
}

.toggle-solution:hover {
    background: #cccccc;
    color: #666666;
    transform: none;
    box-shadow: none;
}

.toggle-solution.active {
    background: linear-gradient(135deg, #ff7f50 0%, #ff6347 100%);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution {
    height: 100%;
    overflow-y: auto;
}

.solution pre {
    margin: 0;
    font-size: 0.85rem;
}

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
    padding: 0;
}

.section-tab {
    background: #f5f5f5;
    color: #333;
    border: none;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    flex: 1;
    min-width: 200px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.section-content {
    display: none;
    margin-top: 2rem;
    padding: 2rem;
    background: #fafafa;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
}

.section-content.active {
    display: block;
}

/* JavaScript pour les fonctionnalités interactives */
.exercise-script {
    display: none;
}
</style>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices

function toggleSolution(button) {
    // Fonction désactivée - les corrections ne sont pas disponibles
    return false;
}

function closeSolutionModal() {
    const modal = document.getElementById('solution-modal');
    if (modal) {
        modal.classList.remove('show');
        document.body.style.overflow = ''; // Restaurer le scroll de la page
    }
}

// Fermer la modal avec la touche Échap
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeSolutionModal();
    }
});

function showSection(sectionId) {
    // Masquer toutes les sections
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher la section sélectionnée
    document.getElementById(sectionId).classList.add('active');
    event.target.classList.add('active');
}

function toggleContext(header) {
    const content = header.nextElementSibling;
    const arrow = header.querySelector('.arrow');
    
    if (content.classList.contains('show')) {
        content.classList.remove('show');
        header.classList.remove('active');
    } else {
        content.classList.add('show');
        header.classList.add('active');
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    const firstTab = document.querySelector('.section-tab');
    if (firstTab) {
        firstTab.click();
    }
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('entetes')">En-têtes de fonctions</button>
    <button class="section-tab" onclick="showSection('documentation')">Documentation</button>
    <button class="section-tab" onclick="showSection('nommage')">Nommage de variables</button>
</div>

<div id="entetes" class="section-content">
    <h2>En-tête de fonctions</h2>
    <p>Une en-tête de fonction permet de spécifier les types de paramètres en entrée et le type du résultat renvoyé par la fonction.</p>
    
    <p>Elle est constituée ainsi :</p>
    <pre><code class="language-python">def nom_de_fonction(parametre_1 : type, parametre_2 : type , ... ) -> type_du_renvoi :</code></pre>
    
    <p>Cela permet de se rendre compte du premier coup d'œil de ce que la fonction doit faire.</p>
    
    <div class="exercise-cards">
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Fonction multiplier</h3>
                <div class="exercise-content">
                    <p>Écrire l'en-tête d'une fonction <code>multiplier</code> qui prend en paramètre deux nombres entiers et renvoie leur produit.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def multiplier(a: int, b: int) -> int:</code></pre>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Fonction concaténation</h3>
                <div class="exercise-content">
                    <p>Écrire l'en-tête d'une fonction <code>concatenation</code> qui prend en paramètres deux chaînes de caractères et renvoie leur concaténation.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def concatenation(chaine1: str, chaine2: str) -> str:</code></pre>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Fonction est_pair</h3>
                <div class="exercise-content">
                    <p>Écrire l'en-tête d'une fonction <code>est_pair</code> qui prend en paramètre un nombre entier et renvoie True si le nombre est pair, False sinon.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def est_pair(nombre: int) -> bool:</code></pre>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Fonction afficher_somme</h3>
                <div class="exercise-content">
                    <p>Écrire l'en-tête d'une fonction <code>afficher_somme</code> qui prend en paramètres deux nombres entiers et affiche seulement leur somme.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def afficher_somme(a: int, b: int) -> None:</code></pre>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge easy">Facile</span>
                <h3 class="exercise-title">Fonction aire_rectangle</h3>
                <div class="exercise-content">
                    <p>Écrire l'en-tête d'une fonction <code>aire_rectangle</code> qui prend en paramètres deux nombres réels (float) et renvoie leur produit.</p>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def aire_rectangle(longueur: float, largeur: float) -> float:</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div id="documentation" class="section-content">
    <h2>Documentation de fonctions</h2>
    <p>La documentation permet à un utilisateur qui fait une revue de code de comprendre ce que la fonction réalise pour : soit comprendre le code, soit le débugger.</p>
    <p>Elle est souvent conjointe à la définition d'en-tête mais peut la remplacer.</p>
    
    <p>La documentation est primordiale lors d'un travail en projet ou en entreprise. Cela permet aussi de savoir revenir sur un projet après ne pas y avoir travaillé après une certaine durée.</p>
    
    <p>Enfin, cette documentation permet aussi de générer de la documentation automatiquement, souvent utilisé en projets.</p>
    <p>Elle est souvent de la forme :</p>
    
    <pre><code class="language-python">def nom_de_fonction(parametre_1, parametre_2):
    '''
    Paramètres : 
        parametre_1 : type du paramètre
        parametre_2 : type du paramètre
    Retourne : 
        type de la sortie
    Explication courte de ce que fait la fonction
    '''</code></pre>
    
    <div class="exercise-cards">
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Intermédiaire</span>
                <h3 class="exercise-title">Documentation des fonctions</h3>
                <div class="exercise-content">
                    <p>Écrire la spécification des fonctions suivantes :</p>
                    <pre><code class="language-python">def est_voyelle(lettre):
    if lettre == 'a' or lettre == 'e' or lettre == 'o' or lettre == 'i' or lettre == 'y':
        return True
    else :
        return False

def mots(phrase):
    compteur = 0
    for caractere in phrase:
        if caractere == ' ':
            compteur = compteur + 1
    return compteur

def surface(rayon):
    pi = 3.14159
    aire = pi * rayon ** 2
    return aire</code></pre>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def est_voyelle(lettre):
    '''
    Paramètres :
        lettre (str) : Un caractère à tester
    Retourne :
        bool : True si la lettre est une voyelle, False sinon
    Détermine si un caractère est une voyelle
    '''
    if lettre == 'a' or lettre == 'e' or lettre == 'o' or lettre == 'i' or lettre == 'y':
        return True
    else :
        return False

def mots(phrase):
    '''
    Paramètres :
        phrase (str) : Une phrase à analyser
    Retourne :
        int : Le nombre d'espaces dans la phrase
    Compte le nombre d'espaces dans une phrase
    '''
    compteur = 0
    for caractere in phrase:
        if caractere == ' ':
            compteur = compteur + 1
    return compteur

def surface(rayon):
    '''
    Paramètres :
        rayon (float) : Le rayon du cercle
    Retourne :
        float : La surface du cercle
    Calcule la surface d'un cercle à partir de son rayon
    '''
    pi = 3.14159
    aire = pi * rayon ** 2
    return aire</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div id="nommage" class="section-content">
    <h2>Nommage de variables</h2>
    <p>Un code peut être documenté correctement mais si les variables et le nom de fonction ne sont pas compréhensibles, cela peut impacter négativement la compréhension du code.</p>
    <p><strong>Renommer les variables et les fonctions des différents algorithmes pour les rendre plus compréhensibles.</strong></p>
    
    <div class="exercise-cards">
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <span class="difficulty-badge medium">Intermédiaire</span>
                <h3 class="exercise-title">Amélioration du nommage</h3>
                <div class="exercise-content">
                    <p>Renommer les variables et fonctions pour améliorer la lisibilité :</p>
                    <pre><code class="language-python">def f(l):
    """
    Calcule la somme des éléments d'une liste de nombres.
    Paramètres :
        l (list) : Liste contenant des nombres.
    Retourne :
        int : La somme des éléments de la liste.
    """
    s = 0
    for i in l:
        s += i
    return s

def m(a, b):
    """
    Calcule la moyenne de deux nombres.
    Paramètres :
        a (int/float) : Le premier nombre.
        b (int/float) : Le deuxième nombre.
    Retourne :
        float : La moyenne des deux nombres.
    """
    return (a + b) / 2

def p(l, L):
    """
    Calcule le périmètre d'un rectangle.
    Paramètres :
        l (float) : La longueur du rectangle.
        L (float) : La largeur du rectangle.
    Retourne :
        float : Le périmètre du rectangle.
    """
    return 2 * (l + L)</code></pre>
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">🔒 Correction non disponible</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code class="language-python">def calculer_somme_liste(liste_nombres):
    """
    Calcule la somme des éléments d'une liste de nombres.
    Paramètres :
        liste_nombres (list) : Liste contenant des nombres.
    Retourne :
        int : La somme des éléments de la liste.
    """
    somme = 0
    for nombre in liste_nombres:
        somme += nombre
    return somme

def calculer_moyenne(premier_nombre, deuxieme_nombre):
    """
    Calcule la moyenne de deux nombres.
    Paramètres :
        premier_nombre (int/float) : Le premier nombre.
        deuxieme_nombre (int/float) : Le deuxième nombre.
    Retourne :
        float : La moyenne des deux nombres.
    """
    return (premier_nombre + deuxieme_nombre) / 2

def calculer_perimetre_rectangle(longueur, largeur):
    """
    Calcule le périmètre d'un rectangle.
    Paramètres :
        longueur (float) : La longueur du rectangle.
        largeur (float) : La largeur du rectangle.
    Retourne :
        float : Le périmètre du rectangle.
    """
    return 2 * (longueur + largeur)</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>