# TP - Chiffrement et Déchiffrement
<style>
.course-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 2rem 0; padding: 0; }
.course-tab { background: #f5f5f5; color: #333; border: none; padding: 1rem 1.5rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; flex: 1; min-width: 220px; text-align: center; }
.course-tab:hover { background: #e0e0e0; transform: translateY(-2px); }
.course-tab.active { background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%); color: white; box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4); }
.course-content { display: none; margin-top: 2rem; padding: 2rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.course-content.active { display: block; }
.course-header { background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 2rem; margin: 2rem 0; border: 1px solid rgba(52, 152, 219, 0.2); text-align: center; }
.section-title { font-size: 2rem; font-weight: 700; background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; }
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1rem 0; font-size: 1.02rem; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 1.5rem; margin: 1.5rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); }
h3.subsection-title { font-size: 1.6rem; font-weight: 600; color: #3498db; margin: 0 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 2px solid rgba(52, 152, 219, 0.25); }
h4.subsubsection-title { font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin: 1rem 0 0.6rem 0; padding-bottom: 0.3rem; border-bottom: 1px dashed rgba(44, 62, 80, 0.3); }
.course-subtitle { color: #7f8c8d; font-size: 1rem; font-weight: 300; margin-top: 0.5rem; }
.definition-box { background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05)); border-left: 5px solid #3498db; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; backdrop-filter: blur(10px); }
.definition-title { font-size: 1.2rem; font-weight: 600; color: #3498db; margin-bottom: 0.8rem; }
.definition-content { color: var(--md-default-fg-color); font-size: 1.02rem; line-height: 1.6; }
h3.subsection-title { font-size: 1.6rem; font-weight: 600; color: #3498db; margin: 0 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 2px solid rgba(52, 152, 219, 0.25); }
h4.subsubsection-title { font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin: 1rem 0 0.6rem 0; padding-bottom: 0.3rem; border-bottom: 1px dashed rgba(44, 62, 80, 0.3); }
.exercise-cards { display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0; max-width: 100%; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-left: 3px solid; width: 100%; }
.exercise-title { margin: 0 0 0.5rem 0; color: var(--md-primary-fg-color); font-size: 1.05rem; font-weight: 600; }
.exercise-content { line-height: 1.6; }
.difficulty-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 500; margin-bottom: 0.5rem; }
.exercise-card.cesar { border-left-color: #FF9800; }
.difficulty-badge.cesar { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.exercise-card.vigenere { border-left-color: #3498db; }
.difficulty-badge.vigenere { background: rgba(52, 152, 219, 0.1); color: #3498db; }
.exercise-card.rsa { border-left-color: #9B59B6; }
.difficulty-badge.rsa { background: rgba(155, 89, 182, 0.1); color: #9B59B6; }
</style>

<script>
function showCourseSection(sectionId, button) {
  const allContents = document.querySelectorAll('.course-content');
  const allTabs = document.querySelectorAll('.course-tab');
  allContents.forEach(c => c.classList.remove('active'));
  allTabs.forEach(t => { t.classList.remove('active'); t.setAttribute('aria-selected', 'false'); });
  const target = document.getElementById(sectionId);
  if (target) target.classList.add('active');
  if (button) { button.classList.add('active'); button.setAttribute('aria-selected', 'true'); }
  try { const url = new URL(window.location); url.hash = sectionId; history.replaceState(null, '', url); } catch (e) {}
  if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
document.addEventListener('DOMContentLoaded', function() {
  const firstTab = document.querySelector('.course-tab');
  if (firstTab) firstTab.click();
});
</script>

<div class="course-header">
  <h2 class="section-title">TP – Chiffrement et Déchiffrement</h2>
  <p class="course-subtitle">BTS SIO 1ère année · Bloc B3 : Cybersécurité</p>
  </div>

<div class="concept-section">
  <h3 class="subsection-title">Introduction</h3>
  <div class="content-text">Le chiffrement est une technique fondamentale en cybersécurité qui permet de protéger des informations en les rendant illisibles sans une clé de déchiffrement. Ce TP présente deux méthodes historiques de chiffrement par substitution et une méthode moderne de chiffrement asymétrique.</div>
</div>

<div class="concept-section">
  <h3 class="subsection-title">Contraintes du TP</h3>
  <ul class="content-text">
    <li>Des <strong>lettres majuscules</strong> (A à Z)</li>
    <li><strong>Sans accents</strong> ni caractères spéciaux</li>
    <li>Une chaîne de caractères <code>ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"</code></li>
    <li>L'opérateur <code>%26</code> pour revenir au début de l'alphabet</li>
  </ul>
</div>

<div class="concept-section">
  <h3 class="subsection-title">Rappels utiles</h3>
  <ul class="content-text">
    <li>Longueur d'une chaîne : <code>len("BONJOUR")</code> → 7</li>
    <li>Accès à un caractère : <code>"BONJOUR"[0]</code> → 'B'</li>
    <li>Position d'un caractère : <code>"BONJOUR".index('N')</code> → 2</li>
    <li>L'opérateur <code>%</code> permet de faire des calculs circulaires</li>
  </ul>
</div>

<div class="definition-box">
  <div class="definition-title">Aide-mémoire : opérateur %</div>
  <div class="definition-content">
    <p>L'opérateur modulo <code>%</code> retourne le reste de la division. Il est très utile pour revenir au début d'une séquence :</p>
    <pre><code># Exemples avec %26 pour l'alphabet
25 % 26 = 25  # Z reste Z
26 % 26 = 0   # Retour à A
27 % 26 = 1   # Retour à B
30 % 26 = 4   # Retour à E

# Avec des nombres négatifs (pour le déchiffrement)
-1 % 26 = 25  # Avant A, c'est Z
-2 % 26 = 24  # Avant A de 2, c'est Y</code></pre>
  </div>
</div>

<div class="course-tabs" role="tablist" aria-label="Chiffrements">
  <button id="tab-course-cesar" class="course-tab" role="tab" aria-controls="course-cesar" aria-selected="false" onclick="showCourseSection('course-cesar', this)">César</button>
  <button id="tab-course-vigenere" class="course-tab" role="tab" aria-controls="course-vigenere" aria-selected="false" onclick="showCourseSection('course-vigenere', this)">Vigenère</button>
  <button id="tab-course-rsa" class="course-tab" role="tab" aria-controls="course-rsa" aria-selected="false" onclick="showCourseSection('course-rsa', this)">RSA</button>
  <noscript>Activez JavaScript pour naviguer entre les onglets du TP.</noscript>
</div>

<div id="course-cesar" class="course-content" role="tabpanel" aria-labelledby="tab-course-cesar">
  <div class="course-header">
    <h2 class="section-title">Partie 1 : Chiffrement de César</h2>
  </div>

<div class="concept-section">
  <h3 class="subsection-title">Principe</h3>
  <p class="content-text">Le chiffre de César consiste à décaler chaque lettre de l'alphabet d'un nombre fixe de positions (la clé).</p>
  <ul class="content-text">
    <li>A → D</li>
    <li>B → E</li>
    <li>Z → C (retour au début grâce à %26)</li>
  </ul>
</div>

<div class="concept-section">
  <h4 class="subsubsection-title">Exemple</h4>
  <pre><code>Message : BONJOUR
Clé : 3
Chiffré : ERQMRXU</code></pre>
</div>

<div class="exercise-cards">
  <div class="exercise-card cesar">
    <div class="difficulty-badge cesar">César</div>
    <h4 class="exercise-title">Exercice 1.1 · Fonction indice_dans_alphabet</h4>
    <div class="exercise-content">
      <p class="content-text">Écrire une fonction qui prend une lettre majuscule, retourne son indice dans ALPHABET, et -1 si ce n'est pas une lettre.</p>
      <pre><code>ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"</code></pre>
      <pre><code>print(indice_dans_alphabet('A'))  # Attendu : 0
print(indice_dans_alphabet('Z'))  # Attendu : 25
print(indice_dans_alphabet('M'))  # Attendu : 12
print(indice_dans_alphabet(' '))  # Attendu : -1</code></pre>
    </div>
  </div>

  <div class="exercise-card cesar">
    <div class="difficulty-badge cesar">César</div>
    <h4 class="exercise-title">Exercice 1.2 · Chiffrement d'un caractère</h4>
    <div class="exercise-content">
      <p class="content-text">Écrire <code>chiffrer_caractere_cesar(caractere, cle)</code>. Formule : <code>(indice_actuel + cle) % 26</code>.</p>
      <pre><code>print(chiffrer_caractere_cesar('A', 3))  # D
print(chiffrer_caractere_cesar('Z', 3))  # C
print(chiffrer_caractere_cesar('X', 5))  # C
print(chiffrer_caractere_cesar(' ', 3))  # ' '</code></pre>
    </div>
  </div>

  <div class="exercise-card cesar">
    <div class="difficulty-badge cesar">César</div>
    <h4 class="exercise-title">Exercice 1.3 · Message complet</h4>
    <div class="exercise-content">
      <p class="content-text">Écrire <code>chiffrer_cesar(message, cle)</code> en utilisant la fonction précédente.</p>
      <pre><code>print(chiffrer_cesar("BONJOUR", 3))           # ERQMRXU
print(chiffrer_cesar("HELLO WORLD", 5))       # MJQQT BTWQI
print(chiffrer_cesar("ABC XYZ", 1))           # BCD YZA</code></pre>
    </div>
  </div>

  <div class="exercise-card cesar">
    <div class="difficulty-badge cesar">César</div>
    <h4 class="exercise-title">Exercice 1.4 · Déchiffrement</h4>
    <div class="exercise-content">
      <p class="content-text">Pour déchiffrer, soustraire la clé : <code>(indice_actuel - cle) % 26</code>.</p>
      <pre><code>message = "BONJOUR"
chiffre = chiffrer_cesar(message, 3)
print(chiffre)           # ERQMRXU
dechiffre = dechiffrer_cesar(chiffre, 3)
print(dechiffre)         # BONJOUR</code></pre>
    </div>
  </div>

  <div class="exercise-card cesar">
    <div class="difficulty-badge cesar">César</div>
    <h4 class="exercise-title">Exercice 1.5 · Cassage par force brute</h4>
    <div class="exercise-content">
      <p class="content-text">Tester toutes les clés (0 à 25) et afficher chaque résultat avec la clé.</p>
      <pre><code>Cle 0 : ERQMRXU
Cle 1 : DQPLQWT
Cle 2 : CPOKPVS
Cle 3 : BONJOUR
Cle 4 : ANMINNT
...</code></pre>
      <pre><code>casser_cesar("ERQMRXU")
# Identifier visuellement que la clé 3 donne BONJOUR</code></pre>
    </div>
  </div>
</div>

</div>

<div id="course-vigenere" class="course-content" role="tabpanel" aria-labelledby="tab-course-vigenere">
  <div class="course-header">
    <h2 class="section-title">Partie 2 : Chiffrement de Vigenère</h2>
  </div>

<div class="concept-section">
  <h3 class="subsection-title">Principe</h3>
  <p class="content-text">Le chiffre de Vigenère utilise une clé composée de lettres. Chaque lettre de la clé détermine le décalage de la lettre correspondante du message. La clé se répète si nécessaire.</p>
  <pre><code>Message : BONJOUR (indices: 1,14,13,9,14,20,17)
Clé :     CLE     (indices: 2,11,4 répétés)
Calcul :  (1+2)%26=3→D, (14+11)%26=25→Z, (13+4)%26=17→R,
          (9+2)%26=11→L, (14+11)%26=25→Z, (20+4)%26=24→Y,
          (17+2)%26=19→T
Résultat : DZRLZYT</code></pre>
</div>

<div class="exercise-cards">
  <div class="exercise-card vigenere">
    <div class="difficulty-badge vigenere">Vigenère</div>
    <h4 class="exercise-title">Exercice 2.1 · Conversion lettre → décalage</h4>
    <div class="exercise-content">
      <p class="content-text">Écrire <code>lettre_vers_decalage(lettre)</code> en utilisant <code>indice_dans_alphabet()</code>.</p>
      <pre><code>print(lettre_vers_decalage('A'))  # 0
print(lettre_vers_decalage('C'))  # 2
print(lettre_vers_decalage('Z'))  # 25</code></pre>
    </div>
  </div>

  <div class="exercise-card vigenere">
    <div class="difficulty-badge vigenere">Vigenère</div>
    <h4 class="exercise-title">Exercice 2.2 · Chiffrement de Vigenère</h4>
    <div class="exercise-content">
      <p class="content-text">Écrire <code>chiffrer_vigenere(message, cle)</code>. Ignorer les caractères non alphabétiques, répéter la clé, et calculer <code>(indice_lettre + decalage) % 26</code>.</p>
      <pre><code>print(chiffrer_vigenere("BONJOUR", "CLE"))      # DZRLZYT
print(chiffrer_vigenere("HELLO WORLD", "KEY"))  # RIJVS UYVJN
print(chiffrer_vigenere("AAA", "BCD"))          # BDF

    </code></pre>
    <pre><code>
        function chiffrer_vigenere(message, clef)
            "" -> res
            0 -> indice_clef
            pour chaque lettre dans message
                indice de la lettre dans l'alphabet -> indice_lettre
                si indice == -1
                    res += lettre
                sinon
                    indice_dans_clef = indice_dans_alphabet(clef[indice_clef], ALPHABET)
                    indice_dans_mot = indice_dans_alphabet(lettre, ALPHABET)
                    res += ALPHABET[(indice_dans_mot + indice_dans_clef) % 26]
                    indice_clef = (indice_clef + 1) % len(clef)
            renvoyer res

    </code></pre>
    </div>
  </div>
</div>

</div>

<div id="course-rsa" class="course-content" role="tabpanel" aria-labelledby="tab-course-rsa">
  <div class="course-header">
    <h2 class="section-title">Partie 3 : Chiffrement RSA</h2>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Principe</h3>
    <p class="content-text">Le chiffrement RSA est un algorithme de chiffrement asymétrique. Il utilise deux clés différentes.</p>
    <ul class="content-text">
      <li>Clé publique pour chiffrer (peut être partagée)</li>
      <li>Clé privée pour déchiffrer (doit rester secrète)</li>
    </ul>
    <p class="content-text">RSA repose sur des opérations mathématiques avec de grands nombres premiers.</p>
  </div>

  <div class="concept-section">
    <h3 class="subsection-title">Concepts mathématiques de base</h3>
    <p class="content-text"><strong>Les nombres premiers :</strong> Un nombre premier n'est divisible que par 1 et par lui-même.</p>
    <h4 class="subsubsection-title">Algorithme RSA simplifié</h4>
    <ol class="content-text">
      <li>Choisir deux nombres premiers p et q</li>
      <li>Calculer n = p × q</li>
      <li>Calculer φ(n) = (p - 1) × (q - 1)</li>
      <li>Choisir e tel que 1 &lt; e &lt; φ(n) et e est premier avec φ(n)</li>
      <li>Calculer d tel que (d × e) % φ(n) = 1</li>
    </ol>
    <ol class="content-text">
        n <- p * q
        phi <- (p-1) * (q-1)
        e = 0
        pour i allant de 2 à phi
          si le pgcg de i et phi vaut 1
            e <- i
            sortir de la boucle (break)
        d  <- inverse_modulaire(e,phi)
        renvoyer (e,n),(d,n)
    </ol>
    <p class="content-text"><strong>Clé publique :</strong> (e, n)<br><strong>Clé privée :</strong> (d, n)</p>
    <p class="content-text"><strong>Chiffrement d'un nombre m :</strong> c = (m^e) % n<br><strong>Déchiffrement d'un nombre c :</strong> m = (c^d) % n</p>
  </div>

  <div class="exercise-cards">
    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.1 · Vérifier si un nombre est premier</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>est_premier(n)</code> qui retourne True si le nombre est premier, False sinon.</p>
        <p class="content-text"><strong>Algorithme :</strong></p>
        <ul class="content-text">
          <li>Si n ≤ 1, retourner False</li>
          <li>Si n = 2, retourner True</li>
          <li>Si n est pair, retourner False</li>
          <li>Tester la divisibilité par tous les nombres impairs de 3 à nn</li>
        </ul>
        <pre><code>print(est_premier(2))    # Attendu : True
print(est_premier(17))   # Attendu : True
print(est_premier(20))   # Attendu : False
print(est_premier(97))   # Attendu : True</code></pre>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.2 · Calculer le PGCD</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>pgcd(a, b)</code> qui calcule le Plus Grand Commun Diviseur de deux nombres (algorithme d'Euclide).</p>
        <h4 class="subsubsection-title">Algorithme d'Euclide</h4>
        <pre><code>Tant que b ≠ 0 :
    r = a % b
    a = b
    b = r
Retourner a</code></pre>
        <pre><code>print(pgcd(48, 18))   # Attendu : 6
print(pgcd(17, 13))   # Attendu : 1
print(pgcd(100, 50))  # Attendu : 50</code></pre>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.3 · Calculer l'inverse modulaire</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>inverse_modulaire(e, phi)</code> qui retourne d tel que (d × e) % phi = 1, et None si aucun inverse n'existe.</p>
        <h4 class="subsubsection-title">Algorithme (méthode simple)</h4>
        <pre><code>Pour d allant de 2 à phi :
    Si (d * e) % phi == 1 :
        Retourner d
Retourner None</code></pre>
        <pre><code>print(inverse_modulaire(7, 3120))    # Attendu : 1783
print(inverse_modulaire(17, 3120))   # Attendu : 2753</code></pre>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.4 · Générer les clés RSA</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>generer_cles_rsa(p, q)</code> qui retourne <code>((e, n), (d, n))</code>.</p>
        <ol class="content-text">
          <li>Calculer n = p × q</li>
          <li>Calculer phi = (p - 1) × (q - 1)</li>
          <li>Trouver e tel que pgcd(e, phi) = 1</li>
          <li>Calculer d avec <code>inverse_modulaire(e, phi)</code></li>
          <li>Retourner ((e, n), (d, n))</li>
        </ol>
        <pre><code>cle_pub, cle_priv = generer_cles_rsa(61, 53)
print("Clé publique:", cle_pub)    # Exemple : (7, 3233)
print("Clé privée:", cle_priv)     # Exemple : (1783, 3233)</code></pre>
        <p class="content-text"><em>Note :</em> Utiliser de petits nombres premiers pour l'exercice. En pratique, RSA utilise des nombres de plusieurs centaines de chiffres.</p>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.5 · Chiffrer un nombre avec RSA</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>chiffrer_nombre_rsa(m, cle_publique)</code> qui calcule <code>(m^e) % n</code>. Utiliser <code>pow(m, e, n)</code>.</p>
        <pre><code>cle_pub, cle_priv = generer_cles_rsa(61, 53)
message_num = 123
chiffre = chiffrer_nombre_rsa(message_num, cle_pub)
print(f"Message {message_num} chiffré : {chiffre}")</code></pre>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.6 · Déchiffrer un nombre avec RSA</h4>
      <div class="exercise-content">
        <p class="content-text">Écrire une fonction <code>dechiffrer_nombre_rsa(c, cle_privee)</code> qui calcule <code>(c^d) % n</code>.</p>
        <pre><code>cle_pub, cle_priv = generer_cles_rsa(61, 53)
message_num = 123
chiffre = chiffrer_nombre_rsa(message_num, cle_pub)
dechiffre = dechiffrer_nombre_rsa(chiffre, cle_priv)
print(f"Message déchiffré : {dechiffre}")  # Attendu : 123</code></pre>
      </div>
    </div>

    <div class="exercise-card rsa">
      <div class="difficulty-badge rsa">RSA</div>
      <h4 class="exercise-title">Exercice 3.7 · Chiffrer un message texte avec RSA</h4>
      <div class="exercise-content">
        <p class="content-text">Convertir chaque lettre en indice dans ALPHABET, chiffrer ces indices, puis reconstituer le message.</p>
        <h4 class="subsubsection-title">Fonctions attendues</h4>
        <ul class="content-text">
          <li><code>chiffrer_message_rsa(message, cle_publique)</code></li>
          <li><code>dechiffrer_message_rsa(liste_chiffree, cle_privee)</code></li>
        </ul>
        <pre><code>cle_pub, cle_priv = generer_cles_rsa(61, 53)
message = "HELLO"
liste_chiffree = chiffrer_message_rsa(message, cle_pub)
print("Message chiffré:", liste_chiffree)
message_dechiffre = dechiffrer_message_rsa(liste_chiffree, cle_priv)
print("Message déchiffré:", message_dechiffre)  # Attendu : HELLO</code></pre>
      </div>
    </div>
  </div>
</div>
