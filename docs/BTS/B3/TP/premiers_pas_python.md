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
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}
.course-content { display: none; margin-top: 2rem; padding: 2rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.course-content.active { display: block; }

.exercise-cards { display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0; max-width: 100%; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-left: 3px solid; width: 100%; }
.exercise-card.intro { border-left-color: #2196F3; }
.exercise-card.conditions { border-left-color: #FF9800; }
.exercise-card.functions { border-left-color: #4CAF50; }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.intro { background: rgba(33, 150, 243, 0.1); color: #2196F3; }
.difficulty-badge.conditions { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.functions { background: rgba(76, 175, 80, 0.1); color: #4CAF50; }
</style>

<style>
/* Styles inspirés de Introduction_cybersecurite pour homogénéiser les points de cours */
.course-header {
  background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  margin: 2rem 0;
  border: 1px solid rgba(52, 152, 219, 0.2);
  text-align: center;
}
.course-subtitle { color: #7f8c8d; font-size: 1rem; font-weight: 300; margin-top: 0.5rem; }
.section-title {
  font-size: 2rem;
  font-weight: 700;
  background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
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
  color: #3498db;
  margin: 0 0 0.8rem 0;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid rgba(52, 152, 219, 0.25);
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
  background: linear-gradient(135deg, rgba(52, 152, 219, 0.08), rgba(155, 89, 182, 0.04));
  border-left: 5px solid #3498db;
  border-radius: 12px;
  padding: 1rem;
  margin: 1rem 0;
}
.definition-title { font-size: 1.1rem; font-weight: 600; color: #3498db; margin-bottom: 0.5rem; }
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

<div class="course-tabs" role="tablist" aria-label="Points de cours">
  <button id="tab-course-variables" class="course-tab" role="tab" aria-controls="course-variables" aria-selected="false" onclick="showCourseSection('course-variables', this)">Variables · Affichage · Demande</button>
  <button id="tab-course-conditions" class="course-tab" role="tab" aria-controls="course-conditions" aria-selected="false" onclick="showCourseSection('course-conditions', this)">Conditions</button>
  <button id="tab-course-fonctions" class="course-tab" role="tab" aria-controls="course-fonctions" aria-selected="false" onclick="showCourseSection('course-fonctions', this)">Fonctions</button>
  <noscript>Activez JavaScript pour naviguer entre les points de cours.</noscript>
</div>

<div id="course-variables" class="course-content" role="tabpanel" aria-labelledby="tab-course-variables">
  <div class="course-header">
    <h2 class="section-title">Variables · Affichage · Demande</h2>
    
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Affichage avec <code>print()</code></h3>
    <pre><code>print("Hello World!")

prenom = "Maya"
print("Bonjour", prenom)</code></pre>
    <p class="content-text">Affiche un message dans le terminal. Plusieurs éléments peuvent être séparés par des virgules.</p>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Demander à l'utilisateur</h3>
    <p class="content-text">La fonction <code>input()</code> demande une saisie et retourne une chaîne (<code>str</code>). Stocker la réponse pour la réutiliser.</p>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Conversion de types</h3>
    <p class="content-text">Convertir une chaîne en entier ou flottant avec <code>int()</code> et <code>float()</code>; transformer vers chaîne avec <code>str()</code>.</p>
    <pre><code># Demande de l'âge à l'utilisateur
age = input("Quel est votre âge ? ")

# l'utilisateur remplit 19
print(age)  # '19'
type(age)   # str

# convertir en entier
age = int(age)</code></pre>
  </div>
  <div class="exercise-cards">
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 1 — Mon premier message</h4>
      <div class="exercise-content"><strong>Créer un programme qui affiche "Bienvenue en Python !" dans le terminal.</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 2 — Afficher mon prénom</h4>
      <div class="exercise-content"><strong>Créer une variable <code>prenom</code> avec votre prénom, puis l'afficher avec <code>print()</code>.</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 3 — Dire bonjour</h4>
      <div class="exercise-content"><strong>Demander le prénom de l'utilisateur avec <code>input()</code>, puis afficher "Bonjour" suivi de son prénom.</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 4 — Mon âge</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et afficher "Vous avez X ans" (où X est l'âge saisi).</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 5 — Deux informations</h4>
      <div class="exercise-content"><strong>Demander le prénom et la ville de l'utilisateur, puis afficher les deux informations dans une seule phrase.</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 6 — Animal préféré</h4>
      <div class="exercise-content"><strong>Demander l'animal préféré de l'utilisateur, le stocker dans une variable, puis afficher "Mon animal préféré est" suivi de l'animal.</strong></div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>

<div id="course-conditions" class="course-content" role="tabpanel" aria-labelledby="tab-course-conditions">
  <div class="course-header">
    <h2 class="section-title">Conditions</h2>
    
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">La structure <code>if</code></h3>
  <pre><code>age = 18
if age &gt;= 18:
    print("Vous êtes majeur")</code></pre>
  <p class="content-text">Après <code>if</code>, écrire la condition, terminer par <code>:</code> et indenter le bloc exécuté si la condition est vraie.</p>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title"><code>if</code>–<code>else</code></h3>
  <pre><code>age = 15

if age &gt;= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")</code></pre>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title"><code>if</code>–<code>elif</code>–<code>else</code></h3>
    <p class="content-text">Pour tester plusieurs conditions successives, utiliser <code>elif</code>.</p>
  <pre><code>note = 14

if note &gt;= 16:
    print("Très bien")
elif note &gt;= 14:
    print("Bien")
elif note &gt;= 12:
    print("Assez bien")
elif note &gt;= 10:
    print("Passable")
else:
    print("Insuffisant")</code></pre>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Opérateurs de comparaison</h3>
    <p class="content-text">Pour créer des conditions, utiliser les opérateurs suivants :</p>
  <table>
    <thead><tr><th>opérateur</th><th>signification</th><th>exemple</th></tr></thead>
    <tbody>
      <tr><td>&gt;</td><td>supérieur</td><td>3 &gt; 1</td></tr>
      <tr><td>&lt;</td><td>inférieur</td><td>3 &lt; 1</td></tr>
      <tr><td>&gt;=</td><td>supérieur ou égal</td><td>3 &gt;= 1</td></tr>
      <tr><td>&lt;=</td><td>inférieur ou égal</td><td>3 &lt;= 1</td></tr>
      <tr><td>==</td><td>égal à</td><td>3 == 1</td></tr>
      <tr><td>!=</td><td>différent de</td><td>3 != 1</td></tr>
    </tbody>
  </table>
    <p class="content-text"><strong>Attention</strong> à ne pas confondre l'affectation <code>=</code> avec la comparaison <code>==</code>.</p>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Opérateurs logiques</h3>
    <h4 class="subsubsection-title"><code>and</code> (et)</h4>
    <p class="content-text">Les deux conditions doivent être vraies.</p>
  <pre><code>age = 20
permis = True

if age &gt;= 18 and permis == True:
    print("Vous pouvez conduire")</code></pre>
    <h4 class="subsubsection-title"><code>or</code> (ou)</h4>
    <p class="content-text">Au moins une des conditions doit être vraie.</p>
  <pre><code>jour = "samedi"

if jour == "samedi" or jour == "dimanche":
    print("C'est le week-end !")</code></pre>
    <h4 class="subsubsection-title"><code>not</code> (non)</h4>
    <p class="content-text">Inverse la condition.</p>
  <pre><code>pluie = False

if not pluie:
    print("On peut sortir sans parapluie")</code></pre>
  </div>
  <div class="exercise-cards">
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 1 — Comparaison de deux nombres</h4>
      <div class="exercise-content"><strong>Demander deux nombres à l'utilisateur et afficher lequel est le plus grand. Si les deux nombres sont égaux, afficher "Les nombres sont égaux".</strong></div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 2 — Vérification de longueur</h4>
      <div class="exercise-content"><strong>Demander un mot à l'utilisateur. Si le mot contient plus de 5 lettres, afficher "Mot long", sinon afficher "Mot court".</strong><br><em>Indice&nbsp;: <code>len(s)</code> renvoie la longueur de la chaîne <code>s</code>.</em></div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 3 — Catégorie d'âge</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et afficher sa catégorie : 0–12 : Enfant ; 13–17 : Adolescent ; 18–59 : Adulte ; 60+ : Senior.</strong></div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 4 — Calculatrice de moyenne</h4>
      <div class="exercise-content"><strong>Demander deux notes à l'utilisateur et calculer leur moyenne. Si la moyenne ≥ 10 : afficher "Vous passez en classe supérieure" ; sinon : afficher "Vous devez redoubler".</strong></div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 5 — Prix du billet de train</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et la distance du trajet (km). Calculer le prix avec : base = distance × 0.20€ ; enfant (&lt; 12) : −50% ; senior (≥ 65) : −30% ; si distance &gt; 200 : −10€ supplémentaires. Afficher le prix final.</strong></div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>

<div id="course-fonctions" class="course-content" role="tabpanel" aria-labelledby="tab-course-fonctions">
  <div class="course-header">
    <h2 class="section-title">Fonctions</h2>
    
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Qu'est-ce qu'une fonction ?</h3>
    <p class="content-text">Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique. Elle organise le code et évite les répétitions.</p>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Définir et appeler une fonction</h3>
  <pre><code>def dire_bonjour():
    print("Bonjour !")
    print("Comment allez-vous ?")

dire_bonjour()</code></pre>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Paramètres</h3>
  <pre><code>def dire_bonjour(prenom):
    print("Bonjour", prenom)

dire_bonjour("Alice")
dire_bonjour("Bob")</code></pre>
  <p class="content-text">Plusieurs paramètres sont possibles, séparés par des virgules :</p>
  <pre><code>def additionner(a, b):
    resultat = a + b
    print("La somme est :", resultat)

additionner(5, 3)</code></pre>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Retour de valeur avec <code>return</code></h3>
  <pre><code>def additionner(a, b):
    resultat = a + b
    return resultat

somme = additionner(10, 20)
print(somme)  # 30</code></pre>
  <p class="content-text"><strong>print</strong> affiche une valeur, <strong>return</strong> renvoie une valeur pour réutilisation.</p>
  <pre><code>def calculer_double(nombre):
    return nombre * 2

resultat = calculer_double(5)
print("Le double est :", resultat)</code></pre>
  </div>
  <div class="exercise-cards">
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 1 — Ma première fonction</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>afficher_message()</code> qui affiche "Bienvenue dans mon programme !". Appeler cette fonction 3 fois.</strong></div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 2 — Fonction avec paramètre</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>saluer(nom)</code> qui prend un nom et affiche "Bonjour" suivi du nom. Appeler avec différents noms.</strong></div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 3 — Calcul du carré</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>calculer_carre(nombre)</code> qui retourne le carré. Demander un nombre, utiliser la fonction et afficher le résultat.</strong></div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 4 — Vérification de parité</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>est_pair(nombre)</code> qui retourne <code>True</code> si le nombre est pair et <code>False</code> sinon. Demander un nombre et afficher s'il est pair ou impair.</strong> <em>Rappel : pair si <code>nombre % 2 == 0</code>.</em></div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 5 — Calcul de prix TTC</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>calculer_ttc(prix_ht, taux_tva)</code> qui retourne le prix TTC (HT × (1 + taux/100)). Demander les valeurs et afficher le prix TTC.</strong></div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 6 — Calculatrice complète</h4>
      <div class="exercise-content"><strong>Créer <code>addition</code>, <code>soustraction</code>, <code>multiplication</code>, <code>division</code> puis une fonction <code>calculatrice()</code> qui demande deux nombres et une opération, appelle la fonction appropriée et affiche le résultat.</strong></div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>