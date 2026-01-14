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
    background: linear-gradient(135deg, #3498db 0%, #8e44ad 100%); /* Bleu/Violet pour POO */
    color: white;
    box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
}
.course-content { display: none; margin-top: 2rem; padding: 2rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.course-content.active { display: block; }

.exercise-cards { display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0; max-width: 100%; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-left: 3px solid; width: 100%; }
.exercise-card.classes { border-left-color: #3498db; }
.exercise-card.props { border-left-color: #9b59b6; }
.exercise-card.ctors { border-left-color: #e74c3c; }
.exercise-card.methods { border-left-color: #2ecc71; }
.exercise-card.heritage { border-left-color: #f1c40f; }

.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.classes { background: rgba(52, 152, 219, 0.1); color: #3498db; }
.difficulty-badge.props { background: rgba(155, 89, 182, 0.1); color: #9b59b6; }
.difficulty-badge.ctors { background: rgba(231, 76, 60, 0.1); color: #e74c3c; }
.difficulty-badge.methods { background: rgba(46, 204, 113, 0.1); color: #2ecc71; }
.difficulty-badge.heritage { background: rgba(241, 196, 15, 0.1); color: #f39c12; }

/* Styles communs */
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
  color: #2980b9;
  margin: 0 0 0.8rem 0;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid rgba(52, 152, 219, 0.25);
}
</style>

<script>
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
}
document.addEventListener('DOMContentLoaded', function() {
  const firstTab = document.querySelector('.course-tab');
  if (firstTab) firstTab.click();
});
</script>

<div class="course-header">
    <h2 class="section-title">Exercices : Programmation Orientée Objet C#</h2>
    <p class="course-subtitle">Entraînement progressif : Classes, Objets, Propriétés, Héritage</p>
</div>

<div class="course-tabs" role="tablist" aria-label="Exercices POO">
  <button id="tab-exo-classes" class="course-tab" role="tab" onclick="showCourseSection('exo-classes', this)">1. Classes & Objets</button>
  <button id="tab-exo-props" class="course-tab" role="tab" onclick="showCourseSection('exo-props', this)">2. Propriétés</button>
  <button id="tab-exo-ctors" class="course-tab" role="tab" onclick="showCourseSection('exo-ctors', this)">3. Constructeurs</button>
  <button id="tab-exo-methods" class="course-tab" role="tab" onclick="showCourseSection('exo-methods', this)">4. Méthodes</button>
  <button id="tab-exo-heritage" class="course-tab" role="tab" onclick="showCourseSection('exo-heritage', this)">5. Héritage</button>
</div>

<!-- 1. CLASSES & OBJETS -->
<div id="exo-classes" class="course-content">
  <div class="course-header">
    <h2 class="section-title">Classes et Instances</h2>
  </div>
  
  <div class="concept-section">
    <h3 class="subsection-title">Rappel</h3>
    <p class="content-text">Une classe est un modèle (ex: <code>Livre</code>), une instance est un objet concret créé avec <code>new</code> (ex: <code>monLivre</code>).</p>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card classes">
      <div class="difficulty-badge classes">Débutant</div>
      <h4 class="exercise-title">Exercice 1.1 — La classe Livre</h4>
      <div class="exercise-content">
        Créer une classe <code>Livre</code> avec 3 champs publics : <code>Titre</code> (string), <code>Auteur</code> (string), <code>NombrePages</code> (int).
      </div>
    </div>

    <div class="exercise-card classes">
      <div class="difficulty-badge classes">Débutant</div>
      <h4 class="exercise-title">Exercice 1.2 — Instanciation</h4>
      <div class="exercise-content">
        Dans le <code>Main</code>, créer deux objets <code>Livre</code> différents (ex: "Harry Potter" et "Le Seigneur des Anneaux"). Affecter des valeurs à leurs champs.
      </div>
    </div>

    <div class="exercise-card classes">
      <div class="difficulty-badge classes">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 1.3 — Affichage</h4>
      <div class="exercise-content">
        Écrire une méthode <code>static string AfficherInformations()</code> qui
        affiche dans la console les informations des deux livres sous la forme :<br>
        <code>"Livre : [Titre] écrit par [Auteur] ([Pages] pages)"</code>.
      </div>
    </div>
  </div>
</div>

<!-- 2. PROPRIÉTÉS -->
<div id="exo-props" class="course-content">
  <div class="course-header">
    <h2 class="section-title">Propriétés { get; set; }</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Rappel</h3>
    <p class="content-text">Utilisez les propriétés auto-implémentées <code>public int Age { get; set; }</code> ou complètes pour valider des données.</p>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card props">
      <div class="difficulty-badge props">Débutant</div>
      <h4 class="exercise-title">Exercice 2.1 — Classe Produit</h4>
      <div class="exercise-content">
        Créer une classe <code>Produit</code> avec une propriété <code>Prix</code> (double) et <code>Nom</code> (string).
      </div>
    </div>

    <div class="exercise-card props">
      <div class="difficulty-badge props">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 2.2 — Prix positif uniquement</h4>
      <div class="exercise-content">
        Modifier la propriété <code>Prix</code> pour qu'on ne puisse pas lui affecter une valeur négative (afficher un message d'erreur si on essaie).<br>
        <em>Indice : Utiliser une variable privée <code>_prix</code> et le bloc <code>set</code>.</em>
      </div>
    </div>

    <div class="exercise-card props">
      <div class="difficulty-badge props">Avancé</div>
      <h4 class="exercise-title">Exercice 2.3 — Propriété en lecture seule</h4>
      <div class="exercise-content">
        Ajouter une propriété <code>Reference</code> qui peut être lue (<code>get</code>) mais pas modifiée de l'extérieur (<code>private set</code> ou pas de set), initialisée dans le constructeur.
      </div>
    </div>
  </div>
</div>

<!-- 3. CONSTRUCTEURS -->
<div id="exo-ctors" class="course-content">
  <div class="course-header">
    <h2 class="section-title">Constructeurs</h2>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card ctors">
      <div class="difficulty-badge ctors">Débutant</div>
      <h4 class="exercise-title">Exercice 3.1 — Constructeur Etudiant</h4>
      <div class="exercise-content">
        Créer une classe <code>Etudiant</code> avec <code>Nom</code>, <code>Prenom</code> et <code>Moyenne</code>. Ajouter un constructeur qui prend ces 3 paramètres pour initialiser l'objet.
      </div>
    </div>

    <div class="exercise-card ctors">
      <div class="difficulty-badge ctors">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 3.2 — Surcharge</h4>
      <div class="exercise-content">
        Ajouter un deuxième constructeur qui ne prend que le <code>Nom</code> et le <code>Prenom</code>, et fixe la <code>Moyenne</code> à 10 par défaut.
      </div>
    </div>

    <div class="exercise-card ctors">
      <div class="difficulty-badge ctors">Avancé</div>
      <h4 class="exercise-title">Exercice 3.3 — Chaînage (this)</h4>
      <div class="exercise-content">
        Faire en sorte que le deuxième constructeur appelle le premier en utilisant le mot-clé <code>this</code>.
      </div>
    </div>

    <div class="exercise-card ctors">
      <div class="difficulty-badge ctors">Avancé</div>
      <h4 class="exercise-title">Exercice 3.4 — Méthode Mention</h4>
      <div class="exercise-content">
        Ajouter une méthode <code>string ObtenirMention()</code> qui retourne "Très bien" si moyenne >= 16, "Bien" si >= 14, "Passable" sinon.
      </div>
    </div>
  </div>
</div>

<!-- 4. MÉTHODES -->
<div id="exo-methods" class="course-content">
  <div class="course-header">
    <h2 class="section-title">Méthodes d'instance</h2>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card methods">
      <div class="difficulty-badge methods">Débutant</div>
      <h4 class="exercise-title">Exercice 4.1 — Classe Cercle</h4>
      <div class="exercise-content">
        Créer une classe <code>Cercle</code> avec une propriété <code>Rayon</code> (double).
      </div>
    </div>

    <div class="exercise-card methods">
      <div class="difficulty-badge methods">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 4.2 — Calculs</h4>
      <div class="exercise-content">
        Ajouter deux méthodes :<br>
        - <code>CalculerAire()</code> qui retourne la surface (Pi * R * R).<br>
        - <code>CalculerPerimetre()</code> qui retourne le périmètre (2 * Pi * R).
        <br><em>Utiliser <code>Math.PI</code>.</em>
      </div>
    </div>

    <div class="exercise-card methods">
      <div class="difficulty-badge methods">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 4.3 — Méthode ToString()</h4>
      <div class="exercise-content">
        Surcharger la méthode <code>ToString()</code> (avec <code>override</code>) pour qu'elle retourne : "Cercle de rayon [R]". Tester avec <code>Console.WriteLine(monCercle)</code>.
      </div>
    </div>

    <div class="exercise-card methods">
      <div class="difficulty-badge methods">Avancé</div>
      <h4 class="exercise-title">Exercice 4.4 — Action</h4>
      <div class="exercise-content">
        Ajouter une méthode <code>void Agrandir(double facteur)</code> qui multiplie le rayon par le facteur donné. (Ex: Agrandir(2) double le rayon).
      </div>
    </div>
  </div>
</div>

<!-- 5. HÉRITAGE -->
<div id="exo-heritage" class="course-content">
  <div class="course-header">
    <h2 class="section-title">Héritage & Polymorphisme</h2>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card heritage">
      <div class="difficulty-badge heritage">Débutant</div>
      <h4 class="exercise-title">Exercice 5.1 — Classe Mère Personnage</h4>
      <div class="exercise-content">
        Créer une classe <code>Personnage</code> avec une propriété <code>Nom</code> et une méthode <code>Attaquer()</code> qui affiche "..." dans la console.
      </div>
    </div>

    <div class="exercise-card heritage">
      <div class="difficulty-badge heritage">Intermédiaire</div>
      <h4 class="exercise-title">Exercice 5.2 — Classes Filles</h4>
      <div class="exercise-content">
        Créer deux classes : <code>Guerrier</code> et <code>Magicien</code> qui héritent de <code>Personnage</code>.<br>
        - Le Guerrier doit afficher "Coup d'épée !" quand il attaque.<br>
        - Le Magicien doit afficher "Boule de feu !".
      </div>
    </div>

    <div class="exercise-card heritage">
      <div class="difficulty-badge heritage">Avancé</div>
      <h4 class="exercise-title">Exercice 5.3 — Polymorphisme (Liste de personnages)</h4>
      <div class="exercise-content">
        Dans le Main, créer une <code>List&lt;Personnage&gt;</code>. Ajouter un Guerrier et un Magicien dedans. Faire une boucle <code>foreach</code> pour faire attaquer chaque personnage de la liste.
      </div>
    </div>
  </div>
</div>
