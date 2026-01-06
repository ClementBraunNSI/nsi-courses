<style>
/* Cours C débutante — Tableaux */
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
  <h1 class="course-title">📦 C — Les Tableaux</h1>
  <p class="course-subtitle">Stocker et manipuler plusieurs variables ensemble</p>
</div>

<div class="concept-section">
  <h2 class="section-title">📚 Qu'est-ce qu'un tableau ?</h2>
  
  <div class="definition-box">
    <div class="definition-title">🎯 Définition</div>
    <div class="definition-content">
      Un tableau (array) est une variable spéciale qui peut contenir <strong>plusieurs valeurs</strong> du <strong>même type</strong>.
      <ul>
        <li>Les valeurs sont stockées côte à côte en mémoire (bloc contigu).</li>
        <li>La taille du tableau est fixée à la création et ne peut pas changer (en C statique).</li>
      </ul>
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Exemple Visuel</div>
    <pre><code>int notes[5]; // Un tableau de 5 entiers

// En mémoire, cela ressemble à ça :
// [ 12 ] [ 15 ] [ 08 ] [ 20 ] [ 10 ]
//   ^      ^      ^      ^      ^
// Index 0 Index 1 Index 2 Index 3 Index 4</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">📝 Déclaration et Initialisation</h2>

  <div class="definition-box">
    <div class="definition-title">Créer un tableau</div>
    <div class="definition-content">
      Syntaxe : <code>type nom_du_tableau[taille];</code>
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Exemples de déclaration</div>
    <pre><code>// 1. Déclarer sans initialiser (valeurs inconnues/aléatoires au début !)
int scores[10]; 

// 2. Déclarer et remplir directement
int nombres[3] = {10, 20, 30};

// 3. Laisser le compilateur deviner la taille
float prix[] = {10.5, 99.99, 5.0}; // Taille automatique : 3
</code></pre>
  </div>
  
  <div class="highlight-fact">
    ⚠️ <strong>Attention :</strong> Si vous déclarez <code>int tab[5];</code> sans l'initialiser, il contient ce qui traînait en mémoire ("garbage values"). Initialisez-le toujours si possible !
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🔍 Accéder et Modifier</h2>
  
  <div class="definition-box">
    <div class="definition-title">Les Indices (Index)</div>
    <div class="definition-content">
      Pour accéder à une case, on utilise son <strong>indice</strong> entre crochets <code>[ ]</code>.
      <br><br>
      <strong>Règle d'Or :</strong> Les indices commencent toujours à <strong>0</strong> !
      <ul>
        <li>Premier élément : <code>tab[0]</code></li>
        <li>Dernier élément (pour taille N) : <code>tab[N-1]</code></li>
      </ul>
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Manipulation</div>
    <pre><code>int tab[3] = {10, 20, 30};

printf("%d", tab[0]); // Affiche 10
printf("%d", tab[2]); // Affiche 30

// Modifier une valeur
tab[1] = 50; 
// Le tableau est maintenant : {10, 50, 30}
</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🔄 Parcourir un Tableau</h2>
  
  <div class="definition-box">
    <div class="definition-title">La boucle FOR</div>
    <div class="definition-content">
      Comme on connaît la taille du tableau, la boucle <code>for</code> est l'outil parfait pour visiter chaque case une par une.
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Afficher tout le tableau</div>
    <pre><code>int notes[4] = {12, 15, 8, 19};

// i va de 0 à 3 (car i < 4)
for (int i = 0; i < 4; i++) {
    printf("Note numéro %d : %d\n", i, notes[i]);
}
</code></pre>
  </div>
  
  <div class="highlight-fact">
    🚫 <strong>Erreur fatale :</strong> Ne jamais dépasser la taille !
    <br>Si vous écrivez <code>tab[4]</code> dans un tableau de taille 4 (indices 0 à 3), votre programme plantera (Segmentation Fault) ou aura un comportement imprévisible.
  </div>
</div>
