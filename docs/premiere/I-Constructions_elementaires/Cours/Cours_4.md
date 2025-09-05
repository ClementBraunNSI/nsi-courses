
<style>
/* Styles modernes pour le cours Fonctions */
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

.concept-section {
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

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.concept-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.concept-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.concept-description {
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

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.function-structure {
    background: rgba(76, 175, 80, 0.1);
    border-left: 4px solid #4CAF50;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.structure-title {
    color: #4CAF50;
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.best-practice {
    background: rgba(33, 150, 243, 0.1);
    border-left: 4px solid #2196F3;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-weight: 500;
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .concept-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Fonctions en Python</h1>
    <p class="course-subtitle">Modularité et réutilisabilité du code</p>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Qu'est-ce qu'une Fonction ?</div>
        <div class="definition-content">
            Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique. Elle permet de <strong>modulariser</strong> le code et d'éviter les répétitions.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">⚙️</div>
            <div class="concept-name">Fonction</div>
            <div class="concept-description">
                Bloc de code réutilisable qui effectue une tâche précise. Peut recevoir des données et retourner un résultat.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📥</div>
            <div class="concept-name">Paramètre</div>
            <div class="concept-description">
                Variable d'entrée qui permet à la fonction de recevoir des données pour son fonctionnement.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📤</div>
            <div class="concept-name">Valeur de Retour</div>
            <div class="concept-description">
                Résultat que la fonction renvoie après avoir effectué ses calculs ou traitements.
            </div>
        </div>
    </div>
    
    <div class="function-structure">
        <div class="structure-title">📋 Structure d'une Fonction</div>
        <div class="code-example">
            <pre><code>def nom_de_fonction(variable_1: type, variable_2: type) -> type_renvoi:
    """
    Documentation de la fonction :
    - Explications de ce que fait la fonction
    - Description des paramètres
    - Description de la valeur de retour
    """
    # Corps de la fonction
    resultat = # calculs ou traitements
    return resultat  # ou None si pas de retour</code></pre>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Exemple Concret :</strong> Convertir des températures Celsius en Fahrenheit<br>
        Formule : Temperature_Fahrenheit = (Temperature_Celsius × 9/5) + 32
    </div>
</div>

<div class="code-example">
    <div class="code-title">💻 Exemples de Fonctions</div>
    <pre><code>def celsius_vers_fahrenheit(temp_celsius: int) -> float:
    """
    Convertit une température Celsius en Fahrenheit.
    
    Args:
        temp_celsius (int): Température en degrés Celsius
    
    Returns:
        float: Température en degrés Fahrenheit
    """
    temp_fahrenheit = (temp_celsius * (9/5)) + 32
    return temp_fahrenheit

def afficher_bonjour(prenom: str) -> None:
    """
    Affiche un message de salutation personnalisé.
    
    Args:
        prenom (str): Le prénom de la personne à saluer
    
    Returns:
        None: Cette fonction n'a pas de valeur de retour
    """
    print('Bonjour, ' + prenom)

# Utilisation des fonctions
print(celsius_vers_fahrenheit(19))  # Affiche: 66.2
print(celsius_vers_fahrenheit(25))  # Affiche: 77.0
afficher_bonjour('Eudes')           # Affiche: Bonjour, Eudes
afficher_bonjour('Germaine')        # Affiche: Bonjour, Germaine</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Anatomie d'une Fonction</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏷️</div>
            <div class="concept-name">Mot-clé <code>def</code></div>
            <div class="concept-description">
                Indique le début de la définition d'une fonction
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📛</div>
            <div class="concept-name">Nom de fonction</div>
            <div class="concept-description">
                Identifiant unique pour appeler la fonction (ex: <code>celsius_vers_fahrenheit</code>)
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📥</div>
            <div class="concept-name">Paramètres</div>
            <div class="concept-description">
                Variables d'entrée avec leur type (ex: <code>temp_celsius: int</code>)
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📝</div>
            <div class="concept-name">Documentation</div>
            <div class="concept-description">
                Bloc de texte expliquant le rôle, les paramètres et le retour
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚙️</div>
            <div class="concept-name">Corps de fonction</div>
            <div class="concept-description">
                Instructions à exécuter quand la fonction est appelée
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">📤</div>
            <div class="concept-name">Valeur de retour</div>
            <div class="concept-description">
                Résultat renvoyé par <code>return</code> (optionnel)
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ <strong>Attention :</strong> Une fonction sans <code>return</code> renvoie <code>None</code> par défaut.<br>
        Exemple : <code>print(afficher_bonjour('Eudes'))</code> affichera <code>None</code>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌍 Variables Locales et Globales</h2>
    
    <div class="definition-box">
        <div class="definition-title">📍 Portée des Variables</div>
        <div class="definition-content">
            En Python, la <strong>portée</strong> d'une variable détermine où elle peut être utilisée dans le programme.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🏠</div>
            <div class="concept-name">Variable Locale</div>
            <div class="concept-description">
                Définie <strong>à l'intérieur</strong> d'une fonction. Accessible uniquement dans cette fonction.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🌐</div>
            <div class="concept-name">Variable Globale</div>
            <div class="concept-description">
                Définie <strong>en dehors</strong> de toute fonction. Accessible partout dans le programme.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🏠 Exemple : Variable Locale</div>
        <pre><code>def ma_fonction():
    variable_locale = 10  # Variable locale
    print(variable_locale)

ma_fonction()              # Affiche 10 ✅
# print(variable_locale)   # ❌ Erreur ! Variable non accessible ici</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">🌐 Exemple : Variable Globale</div>
        <pre><code>variable_globale = 20  # Variable globale

def ma_fonction():
    print(variable_globale)  # Accès à la variable globale ✅

ma_fonction()                # Affiche 20
print(variable_globale)      # Affiche 20</code></pre>
    </div>
    
    <div class="highlight-fact">
        🔧 <strong>Modification d'une Variable Globale :</strong><br>
        Utilisez le mot-clé <code>global</code> pour modifier une variable globale dans une fonction
    </div>
    
    <div class="code-example">
        <div class="code-title">🔧 Modification avec <code>global</code></div>
        <pre><code>compteur = 0  # Variable globale

def incrementer():
    global compteur  # Déclaration nécessaire pour modification
    compteur += 1

print(compteur)    # Affiche 0
incrémenter()
print(compteur)    # Affiche 1</code></pre>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💡 Bonnes Pratiques</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📝</div>
            <div class="concept-name">Documentation</div>
            <div class="concept-description">
                Utilisez des <strong>docstrings</strong> pour expliquer le rôle, les paramètres et le retour de vos fonctions.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🏷️</div>
            <div class="concept-name">Noms Explicites</div>
            <div class="concept-description">
                Choisissez des noms de fonctions qui décrivent clairement leur action.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Spécialisation</div>
            <div class="concept-description">
                Créez des fonctions courtes qui accomplissent <strong>une seule tâche</strong> efficacement.
            </div>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">📝 Documentation avec Docstrings</div>
        <pre><code>def calculer_aire_rectangle(longueur: float, largeur: float) -> float:
    """
    Calcule l'aire d'un rectangle.
    
    Args:
        longueur (float): La longueur du rectangle
        largeur (float): La largeur du rectangle
    
    Returns:
        float: L'aire du rectangle
    """
    return longueur * largeur</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">🏷️ Noms de Fonctions Explicites</div>
        <pre><code># ✅ Bon : nom explicite
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

# ❌ Moins bon : nom peu clair
def calc(n):
    return sum(n) / len(n)</code></pre>
    </div>
    
    <div class="code-example">
        <div class="code-title">🎯 Fonctions Spécialisées</div>
        <pre><code>def est_pair(nombre):
    """Vérifie si un nombre est pair."""
    return nombre % 2 == 0

def filtrer_nombres_pairs(liste_nombres):
    """Filtre les nombres pairs d'une liste."""
    return [n for n in liste_nombres if est_pair(n)]</code></pre>
    </div>
    
    <div class="highlight-fact">
        🚀 <strong>Conseil :</strong> Une fonction bien écrite est facile à comprendre, tester et réutiliser !
    </div>
