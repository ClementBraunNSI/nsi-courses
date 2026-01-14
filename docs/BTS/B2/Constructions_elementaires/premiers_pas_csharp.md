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
.exercise-card.conditions { border-left-color: #FF9800; }
.exercise-card.functions { border-left-color: #FF9800; }
.exercise-card.loops { border-left-color: #FF9800; }
.exercise-card.lists { border-left-color: #FF9800; }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.intro { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.conditions { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.functions { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.loops { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.lists { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
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
    <h2 class="section-title">Structure fondamentale en C#</h2>
</div>

<div class="concept-section">
    <h3 class="subsection-title">Tout est dans une classe</h3>
    <p class="content-text">En C#, toutes les fonctions (qu'on appelle alors <strong>méthodes</strong>) doivent être définies à l'intérieur d'une <strong>classe</strong>. Pour exécuter votre code, vous devez également inclure une méthode spéciale appelée <code>Main</code> qui servira de point d'entrée (votre "bac à sable" pour tester vos fonctions).</p>
    <pre><code class="language-csharp">public class Program 
{ 
    // VOS FONCTIONS ICI
    // Le mot-clé "static" permet d'utiliser la fonction sans créer d'objet (comme une fonction mathématique simple)
    public static string Saluer(string nom) 
    { 
        return $"Bonjour, {nom}!"; 
    } 

    // VOTRE BAC À SABLE (Point d'entrée)
    public static void Main() 
    { 
        // C'est ici que vous testez vos fonctions
        Console.WriteLine(Program.Saluer("Alice")); 
    } 
}</code></pre>
</div>

<div class="course-tabs" role="tablist" aria-label="Points de cours">
  <button id="tab-course-variables" class="course-tab" role="tab" aria-controls="course-variables" aria-selected="false" onclick="showCourseSection('course-variables', this)">Variables · Affichage</button>
  <button id="tab-course-conditions" class="course-tab" role="tab" aria-controls="course-conditions" aria-selected="false" onclick="showCourseSection('course-conditions', this)">Conditions</button>
  <button id="tab-course-boucles" class="course-tab" role="tab" aria-controls="course-boucles" aria-selected="false" onclick="showCourseSection('course-boucles', this)">Boucles</button>
  <button id="tab-course-listes" class="course-tab" role="tab" aria-controls="course-listes" aria-selected="false" onclick="showCourseSection('course-listes', this)">Listes</button>
</div>

<div id="course-variables" class="course-content" role="tabpanel" aria-labelledby="tab-course-variables">
  <div class="course-header">
    <h2 class="section-title">Variables et Méthodes simples</h2>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Affichage avec <code>Console.WriteLine()</code></h3>
    <pre><code class="language-csharp">Console.WriteLine("Hello World!");
string prenom = "Maya";
Console.WriteLine($"Bonjour {prenom}"); // Interpolation de chaîne</code></pre>
  </div>
  <div class="concept-section">
    <h3 class="subsection-title">Demander à l'utilisateur</h3>
    <p class="content-text">La méthode <code>Console.ReadLine()</code> retourne une chaîne. Il faut souvent convertir (ex: <code>int.Parse()</code>).</p>
  </div>
  
  <div class="exercise-cards">
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 1 — Message de bienvenue</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static void AfficherBienvenue()</code> qui affiche "Bienvenue en C# !" dans la console. Tester dans Main.</strong></div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 2 — Présentation complète</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static void SePresenter(string prenom, string ville)</code> qui affiche "Je m'appelle [prenom] et j'habite [ville]".</strong></div>
    </div>
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 3 — Calcul d'âge futur</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int AgeDans10Ans(int ageActuel)</code> qui retourne l'âge dans 10 ans. Tester en affichant le résultat.</strong></div>
    </div>
    
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 4 — Conversion de température</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static double CelsiusVersFahrenheit(double celsius)</code>. Formule : <code>(celsius * 9/5) + 32</code>.</strong></div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Niveau Intro</div>
      <h4 class="exercise-title">Exercice 5 — Moyenne de trois notes</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static double Moyenne(double n1, double n2, double n3)</code> qui retourne la moyenne des trois nombres.</strong></div>
    </div>
  </div>
</div>

<div id="course-conditions" class="course-content" role="tabpanel" aria-labelledby="tab-course-conditions">
  <div class="course-header">
    <h2 class="section-title">Conditions</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Structure <code>if</code> / <code>else</code></h3>
    <pre><code class="language-csharp">if (age >= 18) { ... } else { ... }</code></pre>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 1 — Le plus grand</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int Max(int a, int b)</code> qui retourne le plus grand des deux nombres.</strong></div>
    </div>

    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 2 — Vérification de longueur</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static bool EstMotLong(string mot)</code> qui retourne <code>true</code> si le mot fait plus de 5 caractères, sinon <code>false</code>.</strong></div>
    </div>

    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 3 — Catégorie d'âge</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static string CategorieAge(int age)</code> qui retourne "Enfant" (<=12), "Ado" (<=17), "Adulte" (<=59) ou "Senior".</strong></div>
    </div>

    <div class="exercise-card conditions">
      <div class="difficulty-badge conditions">Conditions</div>
      <h4 class="exercise-title">Exercice 4 — Billet de train</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static double CalculerPrixTrain(int age, double km)</code> selon les règles : 0.20€/km. -50% si <12 ans, -30% si >=65 ans. -10€ si >200km.</strong></div>
    </div>
  </div>
</div>

<div id="course-boucles" class="course-content" role="tabpanel" aria-labelledby="tab-course-boucles">
  <div class="course-header">
    <h2 class="section-title">Boucles</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Boucles <code>for</code> et <code>while</code></h3>
    <pre><code class="language-csharp">for (int i = 0; i < 10; i++) { ... }</code></pre>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 1 — Compter jusqu'à N</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static void CompterJusqua(int n)</code> qui affiche les nombres de 1 à n.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 2 — Table de multiplication</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static void AfficherTable(int n)</code> qui affiche la table de multiplication de n (de 1 à 10).</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 3 — Somme 1 à N</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int SommeJusqua(int n)</code> qui calcule la somme des entiers de 1 à n.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 4 — Compter voyelles</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int CompterVoyelles(string texte)</code> qui retourne le nombre de voyelles.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 5 — Inverser chaîne</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static string Inverser(string texte)</code> qui retourne le texte inversé.</strong></div>
    </div>
    
    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 6 — Palindrome</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static bool EstPalindrome(string texte)</code> qui vérifie si le texte est un palindrome.</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 7 — Nombre Premier</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static bool EstPremier(int n)</code> qui retourne true si n est un nombre premier (divisible uniquement par 1 et lui-même).</strong></div>
    </div>

    <div class="exercise-card loops">
      <div class="difficulty-badge loops">Boucles</div>
      <h4 class="exercise-title">Exercice 8 — Pyramide d'étoiles</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static void AfficherPyramide(int hauteur)</code> qui dessine un triangle. Ex (hauteur 3) :<br>*<br>**<br>***</strong></div>
    </div>
  </div>
</div>

<div id="course-listes" class="course-content" role="tabpanel" aria-labelledby="tab-course-listes">
  <div class="course-header">
    <h2 class="section-title">Listes (List&lt;T&gt;)</h2>
    <p class="course-subtitle">Collections dynamiques : création, ajout, accès et parcours.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Manipuler une Liste</h3>
    <pre><code class="language-csharp">List&lt;int&gt; maListe = new List&lt;int&gt;();
maListe.Add(10); /* Ajouter un élément */
List&lt;int&gt; autreListe = new List&lt;int&gt;{10,20,30};
maListe.AddRange(autreListe); /* Ajouter à la fin de maListe le contenu de autreListe */</code></pre>

  </div>

  <div class="exercise-cards">
    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 1 — Somme des éléments</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int Somme(List&lt;int&gt; nombres)</code> qui retourne la somme des éléments.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 2 — Compter les pairs</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int CompterPairs(List&lt;int&gt; nombres)</code> qui retourne le nombre d'éléments pairs.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 3 — Filtrer les grands nombres</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static List&lt;int&gt; FiltrerSuperieurA(List&lt;int&gt; nombres, int seuil)</code> qui retourne une nouvelle liste ne contenant que les nombres > seuil.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 4 — Concaténation</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static List&lt;int&gt; Concatener(List&lt;int&gt; l1, List&lt;int&gt; l2)</code> qui retourne une nouvelle liste contenant l1 suivie de l2.</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 5 — Trouver le Maximum</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int TrouverMax(List&lt;int&gt; nombres)</code> qui retourne la plus grande valeur de la liste (sans utiliser .Max()).</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 6 — Calcul de Moyenne</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static double CalculerMoyenne(List&lt;int&gt; nombres)</code> qui retourne la moyenne des éléments. Attention à la division réelle !</strong></div>
    </div>

    <div class="exercise-card lists">
      <div class="difficulty-badge lists">Listes</div>
      <h4 class="exercise-title">Exercice 7 — Compter les occurrences</h4>
      <div class="exercise-content"><strong>Écrire une méthode <code>static int CompterOccurrences(List&lt;int&gt; nombres, int valeur)</code> qui compte combien de fois 'valeur' apparaît dans la liste.</strong></div>
    </div>
  </div>
</div>
