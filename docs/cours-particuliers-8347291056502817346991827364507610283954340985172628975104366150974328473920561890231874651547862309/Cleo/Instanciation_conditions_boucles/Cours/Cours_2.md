<style>
/* Cours C débutante — Structures de Contrôle */
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
  <h1 class="course-title">🔀 C — Structures de Contrôle</h1>
  <p class="course-subtitle">Conditions, choix et boucles pour diriger vos programmes</p>
</div>

<div class="concept-section">
  <h2 class="section-title">🚦 Les Conditions (if / else)</h2>
  
  <div class="definition-box">
    <div class="definition-title">🎯 Décisions</div>
    <div class="definition-content">
      Pour exécuter du code seulement si une condition est vraie.
      <ul>
        <li><code>if (condition) { ... }</code> : Si c'est vrai.</li>
        <li><code>else if (condition) { ... }</code> : Sinon si...</li>
        <li><code>else { ... }</code> : Sinon (si rien d'autre n'était vrai).</li>
      </ul>
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Exemple : Vérifier la majorité</div>
    <pre><code>#include &lt;stdio.h&gt;

int main(void) {
  int age;
  printf("Votre age ? ");
  scanf("%d", &age);

  if (age >= 18) {
    printf("Vous êtes majeur.\n");
  } else {
    printf("Vous êtes mineur.\n");
  }
  return 0;
}
</code></pre>
  </div>
  
  <div class="highlight-fact">
    ⚠️ <strong>Syntaxe C :</strong> N'oubliez pas les parenthèses <code>( )</code> autour de la condition et les accolades <code>{ }</code> pour délimiter les blocs de code !
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🔗 Opérateurs Logiques</h2>
  <div class="definition-box">
    <div class="definition-title">Combiner des conditions</div>
    <div class="definition-content">
      <ul>
        <li><code>&&</code> (ET) : Tout doit être vrai. (Ex: <code>age > 18 && permis == 1</code>)</li>
        <li><code>||</code> (OU) : Au moins un est vrai. (Ex: <code>malade || fatigue</code>)</li>
        <li><code>!</code> (NON) : Inverse la condition. (Ex: <code>!vrai</code> devient faux)</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🔄 Les Boucles</h2>
  
  <div class="definition-box">
    <div class="definition-title">🎯 Répéter du code</div>
    <div class="definition-content">
      Deux types principaux :
      <ul>
        <li><strong>while</strong> (tant que) : Tant qu'une condition est vraie.</li>
        <li><strong>for</strong> (pour) : Pour un nombre précis de répétitions (compteur).</li>
      </ul>
    </div>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Boucle WHILE (Tant que)</div>
    <pre><code>int i = 0;
while (i < 5) {
  printf("Compteur : %d\n", i);
  i++; // Important : incrémenter pour éviter la boucle infinie !
}
</code></pre>
  </div>

  <div class="code-example">
    <div class="code-title">💻 Boucle FOR (Compteur)</div>
    <pre><code>// for (initialisation; condition; pas)
for (int i = 0; i < 5; i++) {
  printf("Tour numéro %d\n", i);
}
</code></pre>
  </div>

  <div class="highlight-fact">
    💡 <strong>Astuce :</strong> Préférez <code>for</code> quand vous savez combien de fois répéter (ex: 10 fois). Utilisez <code>while</code> quand la fin dépend d'un événement (ex: tant que l'utilisateur ne tape pas 0).
  </div>
</div>
