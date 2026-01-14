<!-- Navbar des points de cours avec cartes d’exercices -->
<style>
/* Styles pour la navbar des points de cours et cartes d’exercices */
.course-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
    padding: 0;
}
.course-tab {
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
    min-width: 220px;
    text-align: center;
}
.course-tab:hover { background: #e0e0e0; transform: translateY(-2px); }
.course-tab.active {
    background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%); /* Orange */
    color: white;
    box-shadow: 0 4px 12px rgba(255, 152, 0, 0.4);
}
.course-content { display: none; margin-top: 2rem; padding: 2rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.course-content.active { display: block; }

.exercise-cards { display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0; max-width: 100%; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-left: 3px solid; width: 100%; }
.exercise-card.intro { border-left-color: #FF9800; }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.intro { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
</style>

<style>
/* Styles inspirés pour homogénéiser les points de cours */
.course-header {
  background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(245, 124, 0, 0.05));
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  margin: 2rem 0;
  border: 1px solid rgba(255, 152, 0, 0.2);
  text-align: center;
}
.course-subtitle { color: #7f8c8d; font-size: 1rem; font-weight: 300; margin-top: 0.5rem; }
.section-title {
  font-size: 2rem;
  font-weight: 700;
  background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
}
.concept-section {
  background: var(--md-default-bg-color);
  border-radius: 20px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1rem 0; font-size: 1.02rem; }
h3.subsection-title {
  font-size: 1.6rem;
  font-weight: 600;
  color: #E65100;
  margin: 0 0 0.8rem 0;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid rgba(255, 152, 0, 0.25);
}
h4.subsubsection-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 1rem 0 0.6rem 0;
  padding-bottom: 0.3rem;
  border-bottom: 1px dashed rgba(44, 62, 80, 0.3);
}
.definition-box {
  background: linear-gradient(135deg, rgba(255, 152, 0, 0.08), rgba(245, 124, 0, 0.04));
  border-left: 5px solid #FF9800;
  border-radius: 12px;
  padding: 1rem;
  margin: 1rem 0;
}
.definition-title { font-size: 1.1rem; font-weight: 600; color: #E65100; margin-bottom: 0.5rem; }
.definition-content { color: var(--md-default-fg-color); font-size: 1rem; line-height: 1.6; }
</style>

<script>
// Navigation des points de cours par onglets (URL + défilement + ARIA)
function showCourseSection(sectionId, button) {
  const allContents = document.querySelectorAll('.course-content');
  const allTabs = document.querySelectorAll('.course-tab');
  allContents.forEach(c => c.classList.remove('active'));
  allTabs.forEach(t => {
    t.classList.remove('active');
    t.setAttribute('aria-selected', 'false');
  });
  const target = document.getElementById(sectionId);
  if (target) target.classList.add('active');
  if (button) {
    button.classList.add('active');
    button.setAttribute('aria-selected', 'true');
  }
  try {
    const url = new URL(window.location);
    url.hash = sectionId;
    history.replaceState(null, '', url);
  } catch (e) {
    // Ne pas modifier location.hash pour éviter le focus automatique sur l'ancre
  }
  if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
document.addEventListener('DOMContentLoaded', function() {
  const firstTab = document.querySelector('.course-tab');
  if (firstTab) firstTab.click();
});
</script>

<div class="course-header">
    <h2 class="section-title">Types de base et Opérations en C#</h2>
    <p class="course-subtitle">Comprendre les types fondamentaux et comment les manipuler.</p>
</div>

<div class="concept-section">
    <h3 class="subsection-title">Le typage en C#</h3>
    <p class="content-text">Le C# est un langage <strong>fortement typé</strong>. Cela signifie que chaque variable doit avoir un type défini à sa création, et qu'on ne peut pas mettre n'importe quelle donnée n'importe où. Cela aide à éviter de nombreuses erreurs avant même l'exécution du programme.</p>
</div>

<div class="course-tabs" role="tablist" aria-label="Points de cours">
  <button id="tab-entiers" class="course-tab" role="tab" aria-controls="course-entiers" aria-selected="false" onclick="showCourseSection('course-entiers', this)">Entiers (int)</button>
  <button id="tab-reels" class="course-tab" role="tab" aria-controls="course-reels" aria-selected="false" onclick="showCourseSection('course-reels', this)">Nombres à virgule (double)</button>
  <button id="tab-booleens" class="course-tab" role="tab" aria-controls="course-booleens" aria-selected="false" onclick="showCourseSection('course-booleens', this)">Booléens (bool)</button>
  <button id="tab-textes" class="course-tab" role="tab" aria-controls="course-textes" aria-selected="false" onclick="showCourseSection('course-textes', this)">Texte (string/char)</button>
</div>

<!-- SECTION ENTIERS -->
<div id="course-entiers" class="course-content" role="tabpanel" aria-labelledby="tab-entiers">
  <div class="course-header">
    <h2 class="section-title">Les Nombres Entiers</h2>
  </div>
  
  <div class="concept-section">
    <h3 class="subsection-title">Types principaux</h3>
    <p class="content-text">Pour stocker des nombres sans virgule (positifs ou négatifs).</p>
    <div class="definition-box">
        <div class="definition-title">int (Integer)</div>
        <div class="definition-content">Le type standard pour les entiers. Code sur 32 bits.<br>Plage : de -2 milliards à +2 milliards environ.</div>
    </div>
    <div class="definition-box">
        <div class="definition-title">long</div>
        <div class="definition-content">Pour les très grands nombres. Code sur 64 bits.<br>Suffixe <code>L</code> parfois nécessaire (ex: <code>long x = 5000000000L;</code>).</div>
    </div>
    <pre><code class="language-csharp">int age = 20;
int population = 67000000;
long distanceEtoile = 9460730472580800L;</code></pre>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Opérations arithmétiques</h3>
    <p class="content-text">Les opérations classiques s'appliquent.</p>
    <table style="width:100%; text-align:left; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid #ddd;"><th>Symbole</th><th>Opération</th><th>Exemple</th><th>Résultat</th></tr>
        <tr><td><code>+</code></td><td>Addition</td><td><code>10 + 5</code></td><td>15</td></tr>
        <tr><td><code>-</code></td><td>Soustraction</td><td><code>10 - 5</code></td><td>5</td></tr>
        <tr><td><code>*</code></td><td>Multiplication</td><td><code>10 * 5</code></td><td>50</td></tr>
        <tr><td><code>/</code></td><td>Division entière</td><td><code>10 / 3</code></td><td>3 (reste ignoré)</td></tr>
        <tr><td><code>%</code></td><td>Modulo (Reste)</td><td><code>10 % 3</code></td><td>1</td></tr>
    </table>
    <br>
    <p class="content-text"><strong>Incrémentation :</strong></p>
    <pre><code class="language-csharp">int x = 0;
x++; // x vaut 1
x--; // x vaut 0
x += 5; // x vaut 5</code></pre>
  </div>
</div>

<!-- SECTION REELS -->
<div id="course-reels" class="course-content" role="tabpanel" aria-labelledby="tab-reels">
  <div class="course-header">
    <h2 class="section-title">Les Nombres à Virgule</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Types principaux</h3>
    <div class="definition-box">
        <div class="definition-title">double</div>
        <div class="definition-content">Le type par défaut pour les nombres à virgule. Précision double (64 bits). Très utilisé en sciences.</div>
    </div>
    <div class="definition-box">
        <div class="definition-title">float</div>
        <div class="definition-content">Précision simple (32 bits). Moins précis mais prend moins de place. <br><strong>Obligation de mettre le suffixe 'f'.</strong></div>
    </div>
    <div class="definition-box">
        <div class="definition-title">decimal</div>
        <div class="definition-content">Très haute précision, utilisé pour la finance (monnaie). Suffixe 'm'.</div>
    </div>
    <pre><code class="language-csharp">double pi = 3.14159;
float temperature = 25.5f;
decimal prix = 19.99m;</code></pre>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Opérations et Pièges</h3>
    <p class="content-text">Attention à la division ! Si vous divisez deux entiers, le résultat est un entier.</p>
    <pre><code class="language-csharp">double resultat = 5 / 2;   // Donne 2.0 (car 5 et 2 sont vus comme int)
double correct = 5.0 / 2;  // Donne 2.5 (car 5.0 est un double)</code></pre>
    
    <h4 class="subsubsection-title">Bibliothèque Math</h4>
    <p class="content-text">Pour les opérations complexes, utilisez la classe <code>Math</code>.</p>
    <pre><code class="language-csharp">double racine = Math.Sqrt(25); // 5
double puissance = Math.Pow(2, 3); // 2 puissance 3 = 8
double arrondi = Math.Round(3.14159, 2); // 3.14</code></pre>
  </div>
</div>

<!-- SECTION BOOLEENS -->
<div id="course-booleens" class="course-content" role="tabpanel" aria-labelledby="tab-booleens">
  <div class="course-header">
    <h2 class="section-title">Les Booléens</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Vrai ou Faux</h3>
    <p class="content-text">Le type <code>bool</code> ne peut prendre que deux valeurs : <code>true</code> ou <code>false</code>. Il est essentiel pour les conditions (if).</p>
    <pre><code class="language-csharp">bool estMajeur = true;
bool aFini = false;</code></pre>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Opérateurs de comparaison</h3>
    <table style="width:100%; text-align:left; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid #ddd;"><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
        <tr><td><code>==</code></td><td>Égal à</td><td><code>age == 18</code></td></tr>
        <tr><td><code>!=</code></td><td>Différent de</td><td><code>age != 0</code></td></tr>
        <tr><td><code>&lt;</code></td><td>Strictement inférieur</td><td><code>age &lt; 18</code></td></tr>
        <tr><td><code>&gt;</code></td><td>Strictement supérieur</td><td><code>age &gt; 18</code></td></tr>
        <tr><td><code>&lt;=</code></td><td>Inférieur ou égal</td><td><code>age &lt;= 18</code></td></tr>
        <tr><td><code>&gt;=</code></td><td>Supérieur ou égal</td><td><code>age &gt;= 18</code></td></tr>
    </table>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Opérateurs logiques</h3>
    <p class="content-text">Pour combiner plusieurs conditions.</p>
    <div class="definition-box">
        <div class="definition-title">&& (ET)</div>
        <div class="definition-content">Vrai si <strong>les deux</strong> conditions sont vraies.</div>
    </div>
    <div class="definition-box">
        <div class="definition-title">|| (OU)</div>
        <div class="definition-content">Vrai si <strong>au moins une</strong> des conditions est vraie.</div>
    </div>
    <div class="definition-box">
        <div class="definition-title">! (NON)</div>
        <div class="definition-content">Inverse la valeur (Vrai devient Faux).</div>
    </div>
    <pre><code class="language-csharp">bool peutConduire = (age >= 18) && (aPermis == true);
bool gratuit = (age < 5) || (age > 70);</code></pre>
  </div>
</div>

<!-- SECTION TEXTE -->
<div id="course-textes" class="course-content" role="tabpanel" aria-labelledby="tab-textes">
  <div class="course-header">
    <h2 class="section-title">Caractères et Chaînes</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">char vs string</h3>
    <div class="definition-box">
        <div class="definition-title">char (Caractère)</div>
        <div class="definition-content">Un seul caractère. S'écrit avec des <strong>guillemets simples</strong>.</div>
    </div>
    <div class="definition-box">
        <div class="definition-title">string (Chaîne)</div>
        <div class="definition-content">Une suite de caractères. S'écrit avec des <strong>guillemets doubles</strong>.</div>
    </div>
    <pre><code class="language-csharp">char lettre = 'A';
string phrase = "Bonjour tout le monde";</code></pre>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Manipulation de chaînes</h3>
    <p class="content-text">Le type <code>string</code> est très puissant en C#.</p>
    
    <h4 class="subsubsection-title">Concaténation (+)</h4>
    <pre><code class="language-csharp">string nom = "Dupont";
string complet = "Mr " + nom; // "Mr Dupont"</code></pre>

    <h4 class="subsubsection-title">Interpolation ($) - Recommandé !</h4>
    <p class="content-text">Permet d'insérer des variables directement dans le texte.</p>
    <pre><code class="language-csharp">int age = 20;
string message = $"J'ai {age} ans"; // "J'ai 20 ans"</code></pre>

    <h4 class="subsubsection-title">Propriétés et Méthodes utiles</h4>
    <pre><code class="language-csharp">string texte = "Bonjour";
int longueur = texte.Length; // 7
string maj = texte.ToUpper(); // "BONJOUR"
string min = texte.ToLower(); // "bonjour"
bool contient = texte.Contains("jour"); // true</code></pre>
  </div>
</div>
