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
.exercise-card.loops { border-left-color: #9C27B0; }
.exercise-card.lists { border-left-color: #3F51B5; }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.intro { background: rgba(33, 150, 243, 0.1); color: #2196F3; }
.difficulty-badge.conditions { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.functions { background: rgba(76, 175, 80, 0.1); color: #4CAF50; }
.difficulty-badge.loops { background: rgba(156, 39, 176, 0.1); color: #9C27B0; }
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
.see-solution-btn { background: #3498db; color: #fff; border: none; padding: 0.5rem 0.9rem; border-radius: 6px; cursor: pointer; margin-top: 0.6rem; }
.see-solution-btn:hover { background: #2980b9; }
.exercise-solution { display: none; background: #fff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 0.8rem; margin-top: 0.6rem; }
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

function toggleSolution(id, btn) {
  var el = document.getElementById(id);
  if (!el) return;
  var show = el.style.display !== 'block';
  el.style.display = show ? 'block' : 'none';
  if (btn) btn.setAttribute('aria-expanded', show ? 'true' : 'false');
}
</script>

<div class="course-tabs" role="tablist" aria-label="Points de cours">
  <button id="tab-course-variables" class="course-tab" role="tab" aria-controls="course-variables" aria-selected="false" onclick="showCourseSection('course-variables', this)">Variables · Affichage · Demande</button>
  <button id="tab-course-conditions" class="course-tab" role="tab" aria-controls="course-conditions" aria-selected="false" onclick="showCourseSection('course-conditions', this)">Conditions</button>
  <button id="tab-course-fonctions" class="course-tab" role="tab" aria-controls="course-fonctions" aria-selected="false" onclick="showCourseSection('course-fonctions', this)">Fonctions</button>
  <button id="tab-course-boucles" class="course-tab" role="tab" aria-controls="course-boucles" aria-selected="false" onclick="showCourseSection('course-boucles', this)">Boucles</button>
  <button id="tab-course-listes" class="course-tab" role="tab" aria-controls="course-listes" aria-selected="false" onclick="showCourseSection('course-listes', this)">Listes · Tuples</button>
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
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-1', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-1" class="exercise-solution">
        <pre><code>print("Bienvenue en Python !")</code></pre>
      </div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 2 — Afficher mon prénom</h4>
      <div class="exercise-content"><strong>Créer une variable <code>prenom</code> avec votre prénom, puis l'afficher avec <code>print()</code>.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-2', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-2" class="exercise-solution">
        <pre><code>prenom = "Alice"
print(prenom)</code></pre>
      </div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 3 — Dire bonjour</h4>
      <div class="exercise-content"><strong>Demander le prénom de l'utilisateur avec <code>input()</code>, puis afficher "Bonjour" suivi de son prénom.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-3', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-3" class="exercise-solution">
        <pre><code>prenom = input("Quel est votre prénom ? ")
print("Bonjour", prenom)</code></pre>
      </div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 4 — Mon âge</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et afficher "Vous avez X ans" (où X est l'âge saisi).</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-4', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-4" class="exercise-solution">
        <pre><code>age = input("Quel est votre âge ? ")
print("Vous avez " + age + " ans")</code></pre>
      </div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 5 — Deux informations</h4>
      <div class="exercise-content"><strong>Demander le prénom et la ville de l'utilisateur, puis afficher les deux informations dans une seule phrase.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-5', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-5" class="exercise-solution">
        <pre><code>prenom = input("Votre prénom ? ")
ville = input("Votre ville ? ")
print("Je m'appelle " + prenom + " et j'habite " + ville)</code></pre>
      </div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 6 — Animal préféré</h4>
      <div class="exercise-content"><strong>Demander l'animal préféré de l'utilisateur, le stocker dans une variable, puis afficher "Mon animal préféré est" suivi de l'animal.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-variables-6', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-variables-6" class="exercise-solution">
        <pre><code>animal = input("Votre animal préféré ? ")
print("Mon animal préféré est " + animal)</code></pre>
      </div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>

<div id="course-listes" class="course-content" role="tabpanel" aria-labelledby="tab-course-listes">
  <div class="course-header">
    <h2 class="section-title">Listes · Tuples</h2>
    <p class="course-subtitle">Structures linéaires : listes (mutables) et tuples (immuables), parcours et opérations courantes, puis exercices sous forme de fonctions.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Créer et manipuler une liste</h3>
    <pre><code># Création
notes = [12, 15, 9, 18]

# Accès par indice
premiere = notes[0]   # 12
derniere = notes[-1]  # 18

# Longueur
taille = len(notes)   # 4

# Parcours par valeur
for n in notes:
    print(n)

# Parcours par indice
for i in range(len(notes)):
    print(i, notes[i])

# Compréhension de liste
carres = [x*x for x in range(5)]  # [0,1,4,9,16]</code></pre>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Méthodes utiles sur les listes</h3>
    <p class="content-text">Méthodes courantes pour ajouter, retirer, trier, copier et interroger une liste.</p>
    <pre><code>liste = [3, 1, 4]

# Ajouter / étendre / insérer
liste.append(2)             # [3, 1, 4, 2]
liste.extend([5, 6])        # [3, 1, 4, 2, 5, 6]
liste.insert(1, 99)         # [3, 99, 1, 4, 2, 5, 6]

# Retirer / dépiler
liste.remove(99)            # supprime la première occurrence de 99
x = liste.pop()             # retire et retourne le dernier élément
y = liste.pop(2)            # retire à l’indice 2

# Compter / trouver indice
c = liste.count(3)          # nombre d’occurrences de 3
i = liste.index(4)          # première position de 4

# Trier / inverser
liste.sort()                # tri croissant
liste.sort(reverse=True)    # tri décroissant
liste.reverse()             # inversion

# Découpage (slicing)
milieu = liste[2:5]
inverse = liste[::-1]

# Copie (pour éviter les alias)
copie1 = liste[:]           # copie par slicing
copie2 = liste.copy()       # copie</code></pre>
    <p class="content-text"><strong>Attention</strong> : les listes sont mutables; utiliser une copie pour conserver l’original si vous devez modifier sans impacter la variable source.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Tuples</h3>
    <p class="content-text">Un tuple est une séquence immuable. On peut l'indexer et le parcourir comme une liste, mais on ne peut pas modifier ses éléments.</p>
    <pre><code>coord = (10, 20)
x = coord[0]  # 10
y = coord[1]  # 20
# coord[0] = 99  # Erreur : tuple immuable</code></pre>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 1 — Somme des éléments</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>somme_elements(liste)</code> qui retourne la somme des éléments de <code>liste</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 2 — Compter les pairs</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_pairs(liste)</code> qui retourne le nombre d'éléments pairs dans <code>liste</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 3 — Longueurs des chaînes</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>longueur_chaines(liste)</code> qui retourne une nouvelle liste contenant la longueur de chaque chaîne de <code>liste</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 4 — Produit des éléments</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>produit_elements(liste)</code> qui retourne le produit des éléments; pour une liste vide, retourner <code>1</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 5 — Occurrences</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_occurrences(liste, valeur)</code> qui retourne le nombre d'occurrences de <code>valeur</code> dans <code>liste</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 6 — Inverser une liste</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>inverser_liste(liste)</code> qui retourne une nouvelle liste avec les éléments dans l'ordre inverse.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 7 — Concaténation</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>concatener_listes(a, b)</code> qui retourne une nouvelle liste contenant les éléments de <code>a</code> suivis de ceux de <code>b</code>.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes · Tuples</div>
      <h4 class="exercise-title">Exercice 8 — Premiers éléments</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>premiers_elements(liste, n)</code> qui retourne les <code>n</code> premiers éléments de <code>liste</code> (ou toute la liste si <code>n</code> est plus grand).</strong></div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;"></p>
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
      <button class="see-solution-btn" onclick="toggleSolution('sol-conditions-1', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-conditions-1" class="exercise-solution">
        <pre><code>a = int(input("Premier nombre ? "))
b = int(input("Deuxième nombre ? "))
if a > b:
    print("Le plus grand est", a)
elif b > a:
    print("Le plus grand est", b)
else:
    print("Les nombres sont égaux")</code></pre>
      </div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 2 — Vérification de longueur</h4>
      <div class="exercise-content"><strong>Demander un mot à l'utilisateur. Si le mot contient plus de 5 lettres, afficher "Mot long", sinon afficher "Mot court".</strong><br><em>Indice&nbsp;: <code>len(s)</code> renvoie la longueur de la chaîne <code>s</code>.</em></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-conditions-2', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-conditions-2" class="exercise-solution">
        <pre><code>mot = input("Entrez un mot : ")
if len(mot) > 5:
    print("Mot long")
else:
    print("Mot court")</code></pre>
      </div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 3 — Catégorie d'âge</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et afficher sa catégorie : 0–12 : Enfant ; 13–17 : Adolescent ; 18–59 : Adulte ; 60+ : Senior.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-conditions-3', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-conditions-3" class="exercise-solution">
        <pre><code>age = int(input("Âge ? "))
if age <= 12:
    print("Enfant")
elif age <= 17:
    print("Adolescent")
elif age <= 59:
    print("Adulte")
else:
    print("Senior")</code></pre>
      </div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 4 — Calculatrice de moyenne</h4>
      <div class="exercise-content"><strong>Demander deux notes à l'utilisateur et calculer leur moyenne. Si la moyenne ≥ 10 : afficher "Vous passez en classe supérieure" ; sinon : afficher "Vous devez redoubler".</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-conditions-4', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-conditions-4" class="exercise-solution">
        <pre><code>a = float(input("Note 1 ? "))
b = float(input("Note 2 ? "))
m = (a + b) / 2
if m >= 10:
    print("Vous passez en classe supérieure")
else:
    print("Vous devez redoubler")</code></pre>
      </div>
    </div>
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 5 — Prix du billet de train</h4>
      <div class="exercise-content"><strong>Demander l'âge de l'utilisateur et la distance du trajet (km). Calculer le prix avec : base = distance × 0.20€ ; enfant (&lt; 12) : −50% ; senior (≥ 65) : −30% ; si distance &gt; 200 : −10€ supplémentaires. Afficher le prix final.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-conditions-5', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-conditions-5" class="exercise-solution">
        <pre><code>age = int(input("Âge ? "))
dist = float(input("Distance (km) ? "))
prix = dist * 0.20
if age < 12:
    prix = prix * 0.5
elif age >= 65:
    prix = prix * 0.7
if dist > 200:
    prix = prix - 10
if prix < 0:
    prix = 0
print("Prix:", prix)</code></pre>
      </div>
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
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-1', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-1" class="exercise-solution">
        <pre><code>def afficher_message():
    print("Bienvenue dans mon programme !")

afficher_message()
afficher_message()
afficher_message()</code></pre>
      </div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 2 — Fonction avec paramètre</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>saluer(nom)</code> qui prend un nom et affiche "Bonjour" suivi du nom. Appeler avec différents noms.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-2', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-2" class="exercise-solution">
        <pre><code>def saluer(nom):
    print("Bonjour", nom)

saluer("Alice")
saluer("Bob")</code></pre>
      </div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 3 — Calcul du carré</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>calculer_carre(nombre)</code> qui retourne le carré. Demander un nombre, utiliser la fonction et afficher le résultat.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-3', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-3" class="exercise-solution">
        <pre><code>def calculer_carre(nombre):
    return nombre * 2 * 0.5 + nombre * nombre - nombre

n = int(input("Nombre ? "))
print(calculer_carre(n))</code></pre>
      </div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 4 — Vérification de parité</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>est_pair(nombre)</code> qui retourne <code>True</code> si le nombre est pair et <code>False</code> sinon. Demander un nombre et afficher s'il est pair ou impair.</strong> <em>Rappel : pair si <code>nombre % 2 == 0</code>.</em></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-4', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-4" class="exercise-solution">
        <pre><code>def est_pair(nombre):
    return nombre % 2 == 0

n = int(input("Nombre ? "))
if est_pair(n):
    print("Pair")
else:
    print("Impair")</code></pre>
      </div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 5 — Calcul de prix TTC</h4>
      <div class="exercise-content"><strong>Créer une fonction <code>calculer_ttc(prix_ht, taux_tva)</code> qui retourne le prix TTC (HT × (1 + taux/100)). Demander les valeurs et afficher le prix TTC.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-5', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-5" class="exercise-solution">
        <pre><code>def calculer_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva / 100)

ht = float(input("Prix HT ? "))
tva = float(input("Taux TVA (%) ? "))
print(calculer_ttc(ht, tva))</code></pre>
      </div>
    </div>
    <div class="exercise-card functions">
      <div class="difficulty-badge functions">Fonctions</div>
      <h4 class="exercise-title">Exercice 6 — Calculatrice complète</h4>
      <div class="exercise-content"><strong>Créer <code>addition</code>, <code>soustraction</code>, <code>multiplication</code>, <code>division</code> puis une fonction <code>calculatrice()</code> qui demande deux nombres et une opération, appelle la fonction appropriée et affiche le résultat.</strong></div>
      <button class="see-solution-btn" onclick="toggleSolution('sol-fonctions-6', this)" aria-expanded="false">Voir la correction</button>
      <div id="sol-fonctions-6" class="exercise-solution">
        <pre><code>def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculatrice():
    a = float(input("Nombre 1 ? "))
    b = float(input("Nombre 2 ? "))
    op = input("Opération (+, -, *, /) ? ")
    if op == "+":
        print(addition(a, b))
    elif op == "-":
        print(soustraction(a, b))
    elif op == "*":
        print(multiplication(a, b))
    elif op == "/":
        print(division(a, b))
    else:
        print("Opération inconnue")

calculatrice()</code></pre>
      </div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>

<div id="course-boucles" class="course-content" role="tabpanel" aria-labelledby="tab-course-boucles">
  <div class="course-header">
    <h2 class="section-title">Boucles</h2>
    <p class="course-subtitle">Rappels sur <code>for</code>, <code>while</code>, <code>range()</code>, <code>break</code>/<code>continue</code>, puis exercices sous forme de fonctions.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Boucle <code>for</code> et <code>range()</code></h3>
    <pre><code># Parcourir une séquence de nombres de 1 à 5
for i in range(1, 6):
    print(i)

# Parcourir une liste
animaux = ["renard", "lapin", "hibou"]
for a in animaux:
    print(a)</code></pre>
    <p class="content-text"><code>range(debut, fin, pas)</code> génère une séquence. Parcourir des listes directement est fréquent.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Boucle <code>while</code></h3>
    <pre><code># Répéter tant qu'une condition est vraie
compteur = 0
while compteur < 3:
    print("tour", compteur)
    compteur += 1</code></pre>
    <p class="content-text">Attention aux conditions et aux mises à jour des variables pour éviter les boucles infinies.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title"><code>break</code> et <code>continue</code></h3>
    <pre><code>for i in range(1, 10):
    if i == 5:
        break      # Arrête la boucle
    if i % 2 == 0:
        continue   # Passe à l'itération suivante
    print(i)</code></pre>
    <p class="content-text">Utiliser <code>break</code> pour arrêter la boucle, <code>continue</code> pour sauter à l'itération suivante.</p>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 1 — 1 à 100</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>liste_de_1_a_100()</code> qui retourne la liste des nombres de 1 à 100.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 2 — Table de multiplication</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>table_multiplication(n)</code> qui retourne une liste de 10 chaînes sous la forme <code>"i x n = produit"</code> pour <code>i</code> allant de 1 à 10.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 3 — Somme de 1 à 100</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>somme_1_a_100()</code> qui retourne la somme des entiers de 1 à 100.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 4 — Pairs 1..100</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>pairs_1_a_100()</code> qui retourne la liste des nombres pairs entre 1 et 100.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 5 — Compter les voyelles</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_voyelles(chaine)</code> qui retourne le nombre de voyelles dans <code>chaine</code>.</strong> <em>Indice&nbsp;: utiliser un ensemble comme <code>voyelles = "aeiouyAEIOUY"</code>.</em></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 6 — Inverser une chaîne</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>inverser_chaine(chaine)</code> qui retourne <code>chaine</code> inversée.</strong></div>
      <p><em>Indice</em> l'opérateur + permet de mettre 2 chaînes de caractères à la suite.</p>
      <code>chaine1 = "bonjour"</code>
      <code>chaine2 = "au revoir"</code>
      <code>chaine1+chaine2 => "bonjouraurevoir"</code>
      <code>chaine2+chaine1 => "aurevoirbonjour"</code>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 7 — Somme des chiffres</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>somme_chiffres(n)</code> qui retourne la somme des chiffres de l'entier <code>n</code>.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 8 — Jusqu'au premier négatif</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_positifs_avant_negatif(entiers)</code> qui parcourt la liste <code>entiers</code> entiers=[1,5,2,-5,1,2,6,-9] et retourne le nombre de valeurs lues avant de rencontrer le premier négatif (ou la longueur si aucun négatif).</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 9 — Multiples de 3</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>multiples_de_trois(start, count)</code> qui retourne la liste obtenue en partant de <code>start</code> et en le multipliant par 3, <code>count</code> fois de suite.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 10 — Divisions par 2</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>nb_divisions_par_2(n)</code> qui retourne le nombre de fois où <code>n</code> est divisible par 2 (division entière) jusqu'à devenir strictement inférieur à 2.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 11 — Diviseurs et primalité</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>diviseurs_propres(n)</code> qui retourne la liste des diviseurs de <code>n</code> (hors 1 et <code>n</code>). Puis écrire <code>est_premier(n)</code> qui retourne <code>True</code> si <code>n</code> est premier.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 12 — Conjecture de Syracuse</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>sequence_syracuse(n)</code> qui retourne la liste des termes de la suite de Syracuse en partant de <code>n</code> jusqu'à 1 (si pair: <code>n // 2</code>, sinon: <code>3*n + 1</code>).</strong></div>
    </div>

    <!-- Exercices supplémentaires — Boucles avec chaînes de caractères -->
    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 13 — Occurrences d’un caractère</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_occurrences_caractere(chaine, c)</code> qui retourne le nombre d’occurrences de <code>c</code> dans <code>chaine</code> en parcourant la chaîne caractère par caractère.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 14 — Supprimer un caractère</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>supprimer_caractere(chaine, c)</code> qui retourne une nouvelle chaîne sans aucune occurrence de <code>c</code>.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 15 — Doubler chaque caractère</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>doubler_caracteres(chaine)</code> qui retourne une chaîne où chaque caractère de <code>chaine</code> est répété deux fois (ex: <code>"abc" → "aabbcc"</code>).</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 16 — Alterner majuscules/minuscules</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>alterner_casse(chaine)</code> qui retourne une chaîne où les caractères d’indice pair sont en majuscule et ceux d’indice impair en minuscule. Utiliser une boucle sur les indices.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 17 — Miroir des mots</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>miroir_mots(phrase)</code> qui retourne une nouvelle phrase où chaque mot est inversé caractère par caractère, en conservant les espaces (ex: <code>"bonjour monde" → "ruojnob ednom"</code>).</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 18 — Compter lettres et chiffres</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>compter_lettres_chiffres(chaine)</code> qui retourne un tuple <code>(nb_lettres, nb_chiffres)</code> en parcourant la chaîne et en classant chaque caractère.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 19 — Palindrome (sans slicing)</h4>
      <div class="exercise-content"><strong>Écrire une fonction <code>est_palindrome(chaine)</code> qui retourne <code>True</code> si <code>chaine</code> est un palindrome en utilisant une boucle (sans <code>[::-1]</code> ni <code>reversed()</code>).</strong></div>
    </div>
  </div>
  <p style="font-size:0.9rem; color:#888;">
</div>