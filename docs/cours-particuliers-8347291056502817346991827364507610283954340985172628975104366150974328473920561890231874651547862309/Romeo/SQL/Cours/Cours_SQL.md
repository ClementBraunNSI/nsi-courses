<style>
/* Cours SQL Style */
.course-header { background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 3rem; margin: 2rem 0; border: 1px solid rgba(102,126,234,0.2); text-align: center; }
.course-title { font-size: 3rem; font-weight: 700; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
.course-subtitle { color: #7f8c8d; font-size: 1.2rem; font-weight: 300; margin-bottom: 2rem; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 2rem; margin: 2rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255,255,255,0.2); }
.section-title { font-size: 2.2rem; font-weight: 600; color: #667eea; margin-bottom: 2rem; text-align: center; }
.definition-box { background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.05)); border-left: 5px solid #667eea; border-radius: 12px; padding: 2rem; margin: 2rem 0; backdrop-filter: blur(10px); }
.definition-title { font-size: 1.3rem; font-weight: 600; color: #667eea; margin-bottom: 1rem; }
.definition-content { color: var(--md-default-fg-color); font-size: 1.05rem; line-height: 1.6; }
.code-example { background: #1a202c; color: #e2e8f0; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; font-family: 'Courier New', monospace; overflow-x: auto; border-left: 4px solid #4299e1; }
.code-title { color: #4299e1; font-weight: 700; margin-bottom: 1rem; font-size: 1rem; }
.highlight-fact { background: rgba(255,193,7,0.1); border-left: 4px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 8px; font-weight: 500; }
@media (max-width: 768px) { .course-title { font-size: 2rem; } .course-header { padding: 2rem; } }
</style>

<div class="course-header">
  <h1 class="course-title">💾 SQL & Bases de Données</h1>
  <p class="course-subtitle">Interroger et manipuler les données relationnelles</p>
</div>

<div class="concept-section">
  <h2 class="section-title">1. Introduction aux Bases de Données Relationnelles</h2>
  
  <div class="definition-box">
    <div class="definition-title">Structure d'une Table</div>
    <div class="definition-content">
      Une base de données relationnelle organise l'information sous forme de <strong>tables</strong> (ou relations).<br>
      Chaque table est composée de :
      <ul>
        <li><strong>Attributs</strong> (colonnes) : les propriétés des données (ex: <code>nom</code>, <code>age</code>).</li>
        <li><strong>Enregistrements</strong> (lignes ou n-uplets) : les données elles-mêmes.</li>
        <li><strong>Domaine</strong> : le type de donnée autorisé pour un attribut (ex: entier, chaîne, date).</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">🔑 Les Clés</div>
    <div class="definition-content">
      <ul>
        <li><strong>Clé Primaire (Primary Key)</strong> : Un attribut qui identifie de manière <strong>unique</strong> chaque ligne (ex: <code>id_eleve</code>).</li>
        <li><strong>Clé Étrangère (Foreign Key)</strong> : Un attribut qui fait référence à la clé primaire d'une autre table pour lier les données (ex: <code>id_classe</code>).</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">2. Le Langage SQL</h2>
  
  <div class="definition-box">
    <div class="definition-title">SELECT ... FROM</div>
    <div class="definition-content">
      La commande de base pour récupérer des données.
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">Syntaxe de base</div>
    <pre><code>SELECT colonnes
FROM table;

-- Exemples :
SELECT * FROM Eleves;           -- Tout sélectionner
SELECT nom, prenom FROM Eleves; -- Seulement nom et prénom</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">3. Filtrer les données : WHERE</h2>
  
  <div class="definition-content" style="margin-bottom: 1rem;">
    La clause <code>WHERE</code> permet de ne garder que les lignes qui respectent une condition.
  </div>

  <div class="code-example">
    <div class="code-title">Exemple de filtre</div>
    <pre><code>SELECT * 
FROM Eleves 
WHERE age >= 16;</code></pre>
  </div>

  <div class="highlight-fact">
    <strong>Opérateurs de comparaison :</strong> <code>=</code>, <code><></code> (différent), <code><</code>, <code>></code>, <code><=</code>, <code>>=</code><br>
    <strong>Opérateurs logiques :</strong> <code>AND</code>, <code>OR</code>, <code>NOT</code>
  </div>

  <div class="code-example">
    <div class="code-title">Conditions multiples</div>
    <pre><code>SELECT * 
FROM Eleves 
WHERE age >= 16 AND classe = 'Terminale';</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">4. Trier et Épurer</h2>

  <div class="definition-box">
    <div class="definition-title">ORDER BY (Trier)</div>
    <div class="definition-content">
      Permet de trier les résultats par ordre croissant (<code>ASC</code>, par défaut) ou décroissant (<code>DESC</code>).
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">Exemple de tri</div>
    <pre><code>SELECT * 
FROM Voitures 
ORDER BY prix DESC; -- Du plus cher au moins cher</code></pre>
  </div>

  <div class="definition-box">
    <div class="definition-title">DISTINCT (Éliminer les doublons)</div>
    <div class="definition-content">
      Pour éviter d'avoir plusieurs fois la même ligne dans le résultat.
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">Exemple sans doublons</div>
    <pre><code>SELECT DISTINCT ville 
FROM Clients;</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">5. Les Jointures : JOIN</h2>

  <div class="definition-box">
    <div class="definition-title">Combiner des tables</div>
    <div class="definition-content">
      Les jointures permettent de combiner les données de plusieurs tables liées par une clé étrangère.
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">Syntaxe de Jointure</div>
    <pre><code>SELECT Eleves.nom, Classes.nom_classe
FROM Eleves
JOIN Classes ON Eleves.id_classe = Classes.id;</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">📝 Résumé des clauses</h2>
  
  <div class="highlight-fact">
    ⚠️ <strong>L'ordre est strict :</strong>
    <ol>
        <li><code>SELECT</code> (Quoi ?)</li>
        <li><code>FROM</code> (D'où ?)</li>
        <li><code>JOIN ... ON ...</code> (Avec qui ?)</li>
        <li><code>WHERE</code> (Quelles conditions ?)</li>
        <li><code>ORDER BY</code> (Quel ordre ?)</li>
    </ol>
  </div>

  <div class="code-example">
    <div class="code-title">La requête complète</div>
    <pre><code>SELECT colonnes
FROM table1
JOIN table2 ON conditions_jointure
WHERE conditions_filtre
ORDER BY colonne_tri;</code></pre>
  </div>
</div>
