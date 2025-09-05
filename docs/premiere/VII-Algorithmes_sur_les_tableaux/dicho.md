<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        color: #333;
    }
    
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
        margin: 0;
    }
    
    .section-container {
        background: var(--md-default-bg-color);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .section-title {
        color: #667eea;
        font-size: 2rem;
        font-weight: 600;
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
    
    .model-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .algorithm-step {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        display: flex;
        align-items: center;
        gap: 15px;
        transition: transform 0.3s ease;
    }
    
    .algorithm-step:hover {
        transform: translateY(-2px);
    }
    
    .step-number {
        background: #667eea;
        color: #fff;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
    }
    
    .step-content {
        color: var(--md-default-fg-color);
        font-weight: 500;
    }
    
    .highlight-fact {
        background: rgba(255, 193, 7, 0.1);
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 8px;
        font-weight: 500;
        text-align: center;
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
        color: #e2e8f0;
        font-family: 'Courier New', monospace;
        line-height: 1.4;
        overflow-x: auto;
    }
    
    .code-example code {
        color: #e2e8f0;
    }
</style>

<div class="course-header">
    <h1 class="course-title">🔍 La Recherche Dichotomique</h1>
</div>

<div class="section-container">
    <h2 class="section-title">❓ Qu'est-ce que la recherche dichotomique ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Définition</div>
        <div class="definition-content">
            La dichotomie est une méthode de recherche qui permet de trouver rapidement un élément dans une liste triée en <strong>divisant récursivement l'espace de recherche par deux</strong>.<br><br>
            C'est comme chercher quelqu'un dans un annuaire téléphonique : au lieu de lire page par page, vous ouvrez au milieu et décidez de continuer à gauche ou à droite.
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">⚙️ Principe Fondamental</div>
        <div class="definition-content">
            Le principe de la recherche dichotomique repose sur trois étapes simples :
        </div>
    </div>
    
    <div class="model-grid">
        <div class="algorithm-step">
            <span class="step-number">1</span>
            <span class="step-content">Commencer au milieu de la liste</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">2</span>
            <span class="step-content">Comparer l'élément recherché avec la valeur médiane</span>
        </div>
        
        <div class="algorithm-step">
            <span class="step-number">3</span>
            <span class="step-content">Éliminer la moitié de la liste qui ne peut pas contenir l'élément</span>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚠️ Condition Préalable : La liste doit être triée (par ordre croissant ou décroissant)
    </div>
    
    <div class="code-example">
        <div class="code-title">🐍 Algorithme en Pseudocode</div>
        <pre><code>fonction recherche_dichotomique(liste, valeur):
    debut ← 0
    fin ← longueur(liste) - 1

    tant que debut <= fin:
        milieu ← (debut + fin) // 2
        si liste[milieu] == valeur:
            retourner milieu  # L'indice où se trouve la valeur
        sinon si liste[milieu] < valeur:
            debut ← milieu + 1
        sinon:
            fin ← milieu - 1

    retourner -1  # La valeur n'est pas dans la liste</code></pre>
    </div>
</div>