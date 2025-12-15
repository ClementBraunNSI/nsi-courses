<style>
/* Cours C débutante — Affectations & Types */
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
.format-table { width: 100%; border-collapse: collapse; margin: 2rem 0; background: rgba(255, 255, 255, 0.5); border-radius: 10px; overflow: hidden; }
.format-table th { background: #667eea; color: white; padding: 1rem; text-align: left; }
.format-table td { padding: 1rem; border-bottom: 1px solid rgba(102, 126, 234, 0.2); }
.format-table tr:last-child td { border-bottom: none; }
.code-tag { background: #edf2f7; color: #c53030; padding: 0.2rem 0.4rem; border-radius: 4px; font-family: monospace; font-weight: bold; }
@media (max-width: 768px) { .course-title { font-size: 2rem; } .course-header { padding: 2rem; } }
</style>

<div class="course-header">
  <h1 class="course-title">🧱 C — Affectations & Types (débutante)</h1>
  <p class="course-subtitle">Variables, opérateurs, entrées/sorties — bases solides</p>
</div>

<div class="concept-section">
  <h2 class="section-title">🔤 Types fondamentaux du C</h2>
  <div class="definition-box">
    <div class="definition-title">🎯 Types</div>
    <div class="definition-content">
      <ul>
        <li><code>int</code> — entier (ex: 42)</li>
        <li><code>double</code> — nombre réel (ex: 3.14)</li>
        <li><code>char</code> — caractère (ex: 'A')</li>
        <li><code>void</code> — absence de valeur/retour</li>
      </ul>
    </div>
  </div>
  <div class="code-example">
    <div class="code-title">💻 Déclarations & affichage</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int a = 5; double pi = 3.14159; char c = 'Z';
  printf("a=%d pi=%.3f c=%c\n", a, pi, c);
  return 0;
}
</code></pre>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">➕ Opérateurs & Affectations</h2>
  <div class="definition-box">
    <div class="definition-title">🎯 Essentiels</div>
    <div class="definition-content">
      <ul>
        <li>Affectation: <code>a = 10;</code></li>
        <li>Arithmétique: <code>+ - * / %</code> (modulo pour entiers)</li>
        <li>Abrégés: <code>a += 2</code>, <code>a -= 1</code>, <code>a *= 3</code></li>
        <li>Incrémentation: <code>a++</code> (post), <code>++a</code> (pré)</li>
      </ul>
    </div>
  </div>
  <div class="highlight-fact">⚠️ <strong>Division entière:</strong> <code>5/2 == 2</code>. Utiliser <code>(double)5/2</code> pour <code>2.5</code>.</div>
</div>

<div class="concept-section">
  <h2 class="section-title">🖨️ Entrées / Sorties progressives</h2>
  
  <div class="definition-box">
    <div class="definition-title">💡 Comment ça marche ?</div>
    <div class="definition-content">
      <ul>
        <li><strong>printf</strong> : pour <em>écrire</em> à l'écran. On utilise des "placeholders" (%d, %f) pour insérer des variables.</li>
        <li><strong>scanf</strong> : pour <em>lire</em> ce que l'utilisateur tape.</li>
      </ul>
      <br>
      <div class="highlight-fact">⚠️ <strong>Attention avec scanf :</strong> Il faut ajouter un <code>&</code> devant le nom de la variable (ex: <code>&age</code>) pour dire "mets la valeur à cette adresse mémoire".</div>
    </div>
  </div>

  <table class="format-table">
    <thead>
      <tr>
        <th>Format</th>
        <th>Type de variable</th>
        <th>Utilisation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="code-tag">%d</span></td>
        <td><code>int</code> (Entier)</td>
        <td>Pour lire ou afficher un nombre entier (ex: 42).</td>
      </tr>
      <tr>
        <td><span class="code-tag">%f</span></td>
        <td><code>double</code> / <code>float</code></td>
        <td>Pour <strong>afficher</strong> un nombre à virgule (printf).</td>
      </tr>
      <tr>
        <td><span class="code-tag">%lf</span></td>
        <td><code>double</code></td>
        <td>Pour <strong>lire</strong> un nombre à virgule avec précision (scanf).</td>
      </tr>
      <tr>
        <td><span class="code-tag">%c</span></td>
        <td><code>char</code> (Caractère)</td>
        <td>Pour un seul caractère (ex: 'A').</td>
      </tr>
      <tr>
        <td><span class="code-tag">%s</span></td>
        <td><code>char[]</code> (Chaîne)</td>
        <td>Pour du texte (plusieurs caractères).</td>
      </tr>
    </tbody>
  </table>

  <div class="definition-box">
    <div class="definition-title">Étape 1 — Afficher (printf)</div>
    <div class="definition-content">Afficher du texte et des variables.</div>
  </div>
  <div class="code-example">
    <div class="code-title">Afficher un entier et un réel</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int a = 7; double b = 2.5;
  printf("a=%d b=%.2f\n", a, b);
  return 0;
}
</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #48bb78;">
    <div class="code-title">Sortie (ce qui s'affiche)</div>
    <pre><code>a=7 b=2.50</code></pre>
  </div>

  <div class="definition-box">
    <div class="definition-title">Étape 2 — Lire un entier (scanf)</div>
    <div class="definition-content">On demande un nombre à l'utilisateur. Notez le <code>&n</code>.</div>
  </div>
  <div class="code-example">
    <div class="code-title">Lecture d’un entier</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int n;
  printf("Entrez un entier : ");
  scanf("%d", &n);
  printf("Vous avez tapé : %d\n", n);
  return 0;
}
</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #ed8936;">
    <div class="code-title">Entrée utilisateur (exemple)</div>
    <pre><code>12 ⏎</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #48bb78;">
    <div class="code-title">Sortie</div>
    <pre><code>Entrez un entier : 12
Vous avez tapé : 12</code></pre>
  </div>

  <div class="definition-box">
    <div class="definition-title">Étape 3 — Lire un réel (double)</div>
    <div class="definition-content">Pour lire un <code>double</code>, on utilise <code>%lf</code> dans scanf (Long Float).</div>
  </div>
  <div class="code-example">
    <div class="code-title">Lecture d’un réel</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  double t;
  printf("Entrez une température : ");
  scanf("%lf", &t);
  printf("Il fait %.1f degrés.\n", t);
  return 0;
}
</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #ed8936;">
    <div class="code-title">Entrée utilisateur</div>
    <pre><code>25.5 ⏎</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #48bb78;">
    <div class="code-title">Sortie</div>
    <pre><code>Entrez une température : 25.5
Il fait 25.5 degrés.</code></pre>
  </div>

  <div class="definition-box">
    <div class="definition-title">Étape 4 — Plusieurs variables</div>
    <div class="definition-content">On peut demander plusieurs valeurs à la suite.</div>
  </div>
  <div class="code-example">
    <div class="code-title">Entier puis Réel</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int age; double taille;
  
  printf("Age ? ");
  scanf("%d", &age);
  
  printf("Taille (en m) ? ");
  scanf("%lf", &taille);
  
  printf("Vous avez %d ans et mesurez %.2fm.\n", age, taille);
  return 0;
}
</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #ed8936;">
    <div class="code-title">Entrées</div>
    <pre><code>16 ⏎
1.75 ⏎</code></pre>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">Étape 5 — Lecture sur une seule ligne</div>
    <div class="definition-content">On peut lire deux nombres séparés par un espace en une seule fois.</div>
  </div>
  <div class="code-example">
    <div class="code-title">Deux entiers d'un coup</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int a, b;
  printf("Entrez deux nombres (ex: 10 20) : ");
  scanf("%d %d", &a, &b);
  printf("Somme = %d\n", a + b);
  return 0;
}
</code></pre>
  </div>
  <div class="code-example" style="border-left-color: #ed8936;">
    <div class="code-title">Entrées</div>
    <pre><code>10 20 ⏎</code></pre>
  </div>
  <div class="highlight-fact">💡 Toujours inclure <code>&lt;stdio.h&gt;</code> et utiliser le format adapté: <code>%d</code> pour <code>int</code>, <code>%lf</code> pour <code>double</code>.</div>
</div>

<div class="concept-section">
  <h2 class="section-title">🧪 Casting & précision</h2>
  <div class="code-example">
    <div class="code-title">💻 Cast explicite</div>
    <pre><code>int a = 5, b = 2;
double r1 = a / b;        // 2.0
double r2 = (double)a / b; // 2.5
</code></pre>
  </div>
  <div class="highlight-fact">💡 <strong>Astuce:</strong> contrôler le type des opérandes pour les divisions.</div>
</div>
