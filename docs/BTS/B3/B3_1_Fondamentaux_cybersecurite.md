<style>
/* Styles modernes pour le cours Cybersécurité BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(220, 38, 127, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #dc267f 0%, #ff6b6b 100%);
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
    color: #dc267f;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    border-left: 5px solid #dc267f;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #dc267f;
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

.highlight-fact {
    background: rgba(220, 38, 127, 0.1);
    border-left: 4px solid #dc267f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.security-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.security-card {
    background: linear-gradient(135deg, rgba(220, 38, 127, 0.1), rgba(255, 107, 107, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(220, 38, 127, 0.2);
    transition: all 0.3s ease;
}

.security-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(220, 38, 127, 0.2);
}

.risk-matrix {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
    text-align: center;
}

.risk-cell {
    padding: 1rem;
    border-radius: 8px;
    font-weight: 600;
    color: white;
}

.risk-low { background: #27ae60; }
.risk-medium { background: #f39c12; }
.risk-high { background: #e74c3c; }
.risk-critical { background: #8e44ad; }

.ebios-step {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.ebios-title {
    color: #3498db;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.1 - Fondamentaux de la Cybersécurité</h1>
    <p class="course-subtitle">Risques, menaces et méthode EBIOS - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Identifier les risques et menaces en cybersécurité
- Comprendre les enjeux de la sécurité informatique en entreprise
- Appliquer la méthode EBIOS pour l'analyse des risques
- Évaluer la criticité des vulnérabilités

---

<div class="concept-section">
<h2 class="section-title">🔐 Les fondamentaux de la cybersécurité</h2>

<div class="definition-box">
<div class="definition-title">Cybersécurité</div>
<div class="definition-content">
La cybersécurité est l'ensemble des technologies, processus et pratiques conçus pour protéger les réseaux, appareils, programmes et données contre les attaques, dommages ou accès non autorisés.
</div>
</div>

<h3>Les trois piliers de la sécurité informatique</h3>

<div class="concept-grid">
<div class="concept-card">
<div class="concept-icon">🔒</div>
<div class="concept-name">Confidentialité</div>
<div class="concept-description">
Garantir que l'information n'est accessible qu'aux personnes autorisées. Protection contre la divulgation non autorisée.
</div>
</div>

<div class="concept-card">
<div class="concept-icon">✅</div>
<div class="concept-name">Intégrité</div>
<div class="concept-description">
Assurer que l'information n'a pas été modifiée de manière non autorisée. Protection contre l'altération des données.
</div>
</div>

<div class="concept-card">
<div class="concept-icon">🌐</div>
<div class="concept-name">Disponibilité</div>
<div class="concept-description">
Garantir l'accès aux informations et services quand ils sont nécessaires. Protection contre les interruptions de service.
</div>
</div>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">⚠️ Risques et menaces</h2>

<div class="definition-box">
<div class="definition-title">Distinction fondamentale</div>
<div class="definition-content">
<strong>Risque :</strong> Probabilité qu'une menace exploite une vulnérabilité et cause un dommage<br>
<strong>Menace :</strong> Cause potentielle d'un incident indésirable<br>
<strong>Vulnérabilité :</strong> Faiblesse qui peut être exploitée par une menace
</div>
</div>

<h3>Types de menaces</h3>

<div class="security-grid">
<div class="security-card">
<h4>🎭 Menaces humaines</h4>
<ul>
<li>Attaquants externes (hackers)</li>
<li>Employés malveillants</li>
<li>Erreurs humaines</li>
<li>Ingénierie sociale</li>
</ul>
</div>

<div class="security-card">
<h4>💻 Menaces techniques</h4>
<ul>
<li>Malwares (virus, trojans)</li>
<li>Failles logicielles</li>
<li>Attaques réseau</li>
<li>Défaillances système</li>
</ul>
</div>

<div class="security-card">
<h4>🌍 Menaces environnementales</h4>
<ul>
<li>Catastrophes naturelles</li>
<li>Pannes électriques</li>
<li>Incendies</li>
<li>Dégâts des eaux</li>
</ul>
</div>

<div class="security-card">
<h4>⚖️ Menaces légales</h4>
<ul>
<li>Non-conformité RGPD</li>
<li>Violations contractuelles</li>
<li>Sanctions réglementaires</li>
<li>Litiges juridiques</li>
</ul>
</div>
</div>

<div class="highlight-fact">
💡 <strong>Fait important :</strong> 95% des cyberattaques réussies sont dues à une erreur humaine. La sensibilisation des utilisateurs est donc cruciale.
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">📊 Méthode EBIOS (Expression des Besoins et Identification des Objectifs de Sécurité)</h2>

<div class="definition-box">
<div class="definition-title">EBIOS Risk Manager</div>
<div class="definition-content">
Méthode française de gestion des risques numériques, développée par l'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information). Elle permet d'identifier et d'analyser les risques pesant sur un système d'information.
</div>
</div>