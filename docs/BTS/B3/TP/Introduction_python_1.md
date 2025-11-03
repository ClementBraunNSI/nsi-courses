<style>
/* Styles inspirés de la fiche d'exercices pour uniformiser la DA */
.section-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; padding: 0; }
.section-tab { background: #f5f5f5; color: #333; border: none; padding: 0.8rem 1.2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; flex: 1; min-width: 160px; text-align: center; }
.section-tab:hover { background: #e0e0e0; transform: translateY(-2px); }
.section-tab.active { background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%); color: white; box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4); }
.section-content { display: none; margin-top: 1rem; padding: 1rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.section-content.active { display: block; }

.exercise-cards { display: flex; flex-direction: column; gap: 1rem; padding: 0.5rem 0; max-width: 100%; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; border-left: 3px solid; width: 100%; max-width: 100%; }
.exercise-card.intro { border-left-color: #4CAF50; }
.exercise-card.easy { border-left-color: #2196F3; }
.exercise-card.medium { border-left-color: #FF9800; }
.exercise-card.hard { border-left-color: #F44336; }
.exercise-card.important { border-left-color: #ff8c42; background: linear-gradient(135deg, rgba(255,140,66,0.05) 0%, rgba(255,140,66,0.02) 100%); }
.exercise-card:hover { transform: translateY(-2px); box-shadow: 0 0 12px rgba(0,0,0,0.08); }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.difficulty-badge.intro { background: rgba(76,175,80,0.1); color: #4CAF50; }
.difficulty-badge.easy { background: rgba(33,150,243,0.1); color: #2196F3; }
.difficulty-badge.medium { background: rgba(255,152,0,0.1); color: #FF9800; }
.difficulty-badge.hard { background: rgba(244,67,54,0.1); color: #F44336; }
.difficulty-badge.important { background: rgba(255,140,66,0.1); color: #ff8c42; }
.toggle-solution { background: linear-gradient(135deg, #cccccc 0%, #999999 100%); color: #666; border: none; padding: 0.5rem 1rem; border-radius: 8px; cursor: not-allowed; font-size: 0.9rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.5rem; opacity: 0.6; }
.exercise-content { margin-bottom: 0.5rem; line-height: 1.6; }
</style>

<script>
function showSection(sectionId) {
  const contents = document.querySelectorAll('.section-content');
  const tabs = document.querySelectorAll('.section-tab');
  contents.forEach(c => c.classList.remove('active'));
  tabs.forEach(t => t.classList.remove('active'));
  const section = document.getElementById(sectionId);
  if (section) section.classList.add('active');
  event.target.classList.add('active');
}
document.addEventListener('DOMContentLoaded', function() {
  const firstTab = document.querySelector('.section-tab');
  if (firstTab) { firstTab.classList.add('active'); }
  const firstContent = document.querySelector('.section-content');
  if (firstContent) { firstContent.classList.add('active'); }
});
function toggleSolution(button) { return false; }
</script>

# TP1 – Introduction à Python et cybersécurité

<div class="section-tabs">
  <button class="section-tab" onclick="showSection('notice-section')">📝 Notice</button>
  <button class="section-tab" onclick="showSection('part-a')">Partie A</button>
  <button class="section-tab" onclick="showSection('part-b')">Partie B</button>
  <button class="section-tab" onclick="showSection('part-c')">Partie C</button>
  <button class="section-tab" onclick="showSection('part-d')">Partie D</button>
</div>

<div id="notice-section" class="section-content">
  <div class="exercise-cards">
    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Affichage</h4>
      <div class="exercise-content">
        <p><strong>print()</strong></p>
        <pre><code class="language-python">print("Bonjour")  # Affiche Bonjour</code></pre>
        <p>Afficher plusieurs éléments séparés par des espaces :</p>
        <pre><code class="language-python">prenom = "Alice"
age = 17
print("Bonjour", prenom, "vous avez", age, "ans")</code></pre>
        <p>Concaténation :</p>
        <pre><code class="language-python">print("Bonjour " + prenom + ", vous avez " + str(age) + " ans")</code></pre>
      </div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Saisie de l’utilisateur</h4>
      <div class="exercise-content">
        <pre><code class="language-python">prenom = input("Entrez votre prénom : ")</code></pre>
        <p>Retourne toujours une <strong>chaîne</strong>.</p>
        <p>Convertir en entier :</p>
        <pre><code class="language-python">age = int(input("Entrez votre âge : "))</code></pre>
        <p>Convertir en chaîne :</p>
        <pre><code class="language-python">str(age)</code></pre>
      </div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Longueur d’une chaîne</h4>
      <div class="exercise-content">
        <pre><code class="language-python">mdp = "azerty12"
print(len(mdp))  # Affiche 8</code></pre>
      </div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Conditions (if/elif/else)</h4>
      <div class="exercise-content">
        <pre><code class="language-python">age = 18
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")</code></pre>
        <p>Plusieurs conditions :</p>
        <pre><code class="language-python">role = "technicien"
if role == "admin":
    print("Accès complet")
elif role == "technicien":
    print("Accès supervision")
else:
    print("Accès limité")</code></pre>
      </div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Boucles</h4>
      <div class="exercise-content">
        <p>Boucle <code>for</code> :</p>
        <pre><code class="language-python">mot = "Python"
for c in mot:
    print(c)  # Chaque caractère sur une ligne</code></pre>
        <p>Boucle <code>while</code> :</p>
        <pre><code class="language-python">i = 1
while i <= 5:
    print(i)
    i += 1</code></pre>
      </div>
    </div>

    <div class="exercise-card intro">
      <div class="difficulty-badge intro">Introduction 🦊</div>
      <h4 class="exercise-title">Fonctions simples</h4>
      <div class="exercise-content">
        <pre><code class="language-python">def max_deux(a, b):
    if a >= b:
        return a
    else:
        return b</code></pre>
        <p>Fonction mot de passe fort :</p>
        <pre><code class="language-python">def est_fort(mdp):
    if len(mdp) < 8:
        return False
    has_digit = False
    for c in mdp:
        if c.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False
    has_upper = False
    for c in mdp:
        if c.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
    return True</code></pre>
      </div>
    </div>

    <div class="exercise-card important">
      <div class="difficulty-badge important">Référence 🧭</div>
      <h4 class="exercise-title">Méthodes utiles</h4>
      <div class="exercise-content">
        <table>
          <thead>
            <tr><th>Méthode</th><th>Utilité</th><th>Exemple</th></tr>
          </thead>
          <tbody>
            <tr><td><code>.isdigit()</code></td><td>Vérifie si un caractère est un chiffre</td><td><code>'3'.isdigit()</code> → True</td></tr>
            <tr><td><code>.isupper()</code></td><td>Vérifie si un caractère est une majuscule</td><td><code>'A'.isupper()</code> → True</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<div id="part-a" class="section-content">
  <div class="exercise-cards">
    <div class="exercise-card easy">
      <div class="difficulty-badge easy">Bases</div>
      <h4 class="exercise-title">1. Afficher un message de bienvenue</h4>
      <div class="exercise-content">
        <pre><code>Bienvenue dans l’atelier sécurité Python !</code></pre>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">2. Variables & phrases</h4>
      <div class="exercise-content">
        <p>Créer une variable technicien qui a pour valeur "Alice" et une variable poste qui a pour valeur 27 puis afficher :</p>
        <pre><code>Alice est responsable du poste 27.</code></pre>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">3. Entrée & conversion</h4>
      <div class="exercise-content">
        <p>Demander le prénom et l’âge. Afficher :</p>
        <pre><code>Bonjour [prénom], dans 5 ans vous aurez [age+5] ans.</code></pre>
        <p><i>Attention, la valeur qui sera demandée pour l'âge est une chaîne de caractères. On ne peut pas additionner un <code>int</code> et un <code>str</code> et il faudra donc modifier le type de la variable contenant l'âge.</i></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">4. Longueur mot de passe</h4>
      <div class="exercise-content">
        <p>Demander un mot de passe à l'utilisateur et afficher l'afficher avec sa longueur. On utilisera<code>len()</code>.</p>
        <p> Exemple de sortie : <i>Votre mot de passe est renard, 6 caractères</i></p>
      </div>
    </div>
  </div>
</div>

<div id="part-b" class="section-content">
  <div class="exercise-cards">
    <div class="exercise-card medium">
      <div class="difficulty-badge medium">Conditions & sécurité</div>
      <h4 class="exercise-title">5. Authentification simple</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>authentifier(login, mot_de_passe)</code> qui prend comme paramètres un identifiant (chaîne) et un mot de passe (chaîne), et renvoie un booléen. Cette fonction doit renvoyer <code>True</code> si <code>login == "admin"</code> et <code>mot_de_passe == "azerty"</code>, sinon <code>False</code>.</strong></p>
      </div>
    </div>
    <div class="exercise-card medium">
      <h4 class="exercise-title">6. Tentatives limitées</h4>
      <div class="exercise-content">
        <p>Demander à l'utlisateur un mot de passe et autoriser 3 essais. Si le mot de passe est incorrect, afficher "Mot de passe incorrect" et continuer à demander. Si le mot de passe est correct, afficher "Accès autorisé".</p>
        <p> On utilisera une boucle while pour demander le mot de passe 3 fois maximum.</p>
      </div>
    </div>
    <div class="exercise-card medium">
      <h4 class="exercise-title">7. Rôles & droits</h4>
      <div class="exercise-content">
        <p>Demander à l'utilisateur son rôle (<code>admin</code>, <code>technicien</code>, <code>invite</code>) et afficher le droit correspondant</p>
        <p>Si le rôle est <code>admin</code>, afficher "Droits d'administration". Si le rôle est <code>technicien</code>, afficher "Droits de technicien". Si le rôle est <code>invite</code>, afficher "Droits d'invite".</p>
      </div>
    </div>
    <div class="exercise-card medium">
      <h4 class="exercise-title">8. Connexion selon heure</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>connexion_autorisee(role, heure)</code> qui prend comme paramètres un rôle (chaîne de caractère) et une heure (entier), et renvoie un booléen. Cette fonction doit renvoyer <code>True</code> si <code>role == "admin"</code> ou si <code>8 ≤ heure ≤ 18</code>, sinon <code>False</code>.</strong></p>
      </div>
    </div>
  </div>
</div>

<div id="part-c" class="section-content">
  <div class="exercise-cards">
    <div class="exercise-card easy">
      <h4 class="exercise-title">9. Afficher 1 à 100 (for et while)</h4>
      <div class="exercise-content">
        <p><strong>Écrire un programme pour afficher dans le terminal tous les nombres entre 1 et 100 (à l'aide d'une boucle for puis d'une boucle tant que).</strong></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">10. Table de multiplication</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>table_multiplication(n)</code> qui prend comme paramètre un entier <code>n</code> et renvoie <code>None</code>. Cette fonction doit afficher la table de multiplication de <code>n</code> jusqu’à 10.</strong></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">11. Somme 1 à 100</h4>
      <div class="exercise-content">
        <p><strong>Écrire un programme pour réaliser la somme des nombres entiers de 1 jusque 100.</strong></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">12. Nombres pairs 1 à 100</h4>
      <div class="exercise-content">
        <p><strong>Écrire un programme pour afficher dans le terminal tous les nombres pairs entre 1 et 100.</strong></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">13. Compter voyelles</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>compter_voyelle(texte)</code> qui prend comme paramètre une chaîne <code>texte</code> et renvoie un entier. Cette fonction doit compter et renvoyer le nombre de voyelles présentes dans <code>texte</code>.</strong></p>
        <p>On pourra utiliser le mot clef <code>in</code> pour vérifier si une lettre est une voyelle.</p>
        <p><em>Exemple : <code>"a" in "aeiouy"</code> renvoie <code>True</code>, alors que <code>"z" in "aeiouy"</code> renvoie <code>False</code>.</em></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">14. Inverser une chaîne</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>inverser_chaine(texte)</code> qui prend comme paramètre une chaîne <code>texte</code> et renvoie une chaîne. Cette fonction doit renvoyer <code>texte</code> inversé.</strong></p>
        <p><em>Exemple : "bonjour" → "ruojnob".</em></p>
      </div>
    </div>
    <div class="exercise-card easy">
      <h4 class="exercise-title">15. Somme des chiffres d’un nombre</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>somme_chiffres(n)</code> qui prend comme paramètre un entier <code>n</code> et renvoie un entier. Cette fonction doit calculer et renvoyer la somme des chiffres de <code>n</code>.</strong></p>
        <p><em>Exemple : pour 123, il affichera 6.</em></p>
        <p><i>Indication : on pourra convertir le nombre en chaîne de caractère pour pouvoir parcourir chaque chiffre. Puis avec une boucle for, on pourra obtenir chaque chiffre et le convertir en entier pour pouvoir le sommer.</i></p>
      </div>
    </div>
  </div>
</div>

<div id="part-d" class="section-content">
  <div class="exercise-cards">
    <div class="exercise-card medium">
      <h4 class="exercise-title">16. Fonction max_deux(a, b)</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>max_deux(a, b)</code> qui prend comme paramètres deux nombres et renvoie un nombre. Cette fonction doit renvoyer le plus grand des deux.</strong></p>
      </div>
    </div>
    <div class="exercise-card medium">
      <h4 class="exercise-title">17. Fonction est_fort(mdp)</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>est_fort(mdp)</code> qui prend comme paramètre un mot de passe (chaîne) et renvoie un booléen. Cette fonction doit renvoyer <code>True</code> si le mot de passe a au moins 8 caractères, contient au moins une majuscule et au moins un chiffre, sinon <code>False</code>.</strong></p>
      </div>
    </div>
    <div class="exercise-card hard">
      <h4 class="exercise-title">18. Mini-système complet</h4>
      <div class="exercise-content">
        <p><strong>Écrire une fonction <code>mini_systeme_complet(login, mot_de_passe, nouveau_mot)</code> qui prend comme paramètres un identifiant (chaîne), un mot de passe (chaîne) et un nouveau mot de passe (chaîne), et renvoie une chaîne. Cette fonction doit vérifier <code>login == "admin"</code> et <code>mot_de_passe == "azerty123"</code>, puis si l’authentification réussit, vérifier <code>est_fort(nouveau_mot)</code> et renvoyer un message indiquant soit « Accès autorisé » soit « Changez de mot de passe » ; sinon renvoyer « Accès refusé ».</strong></p>
      </div>
    </div>
  </div>
</div>
