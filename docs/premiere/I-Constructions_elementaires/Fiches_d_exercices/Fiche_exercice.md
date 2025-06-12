# Fiche d'exercices : Types en python

<link rel="stylesheet" href="../../../stylesheets/exercise-cards.css">
<script src="../../../stylesheets/exercise-cards.js"></script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau Facile</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau Difficile</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Types en Python</h4>
            <div class="exercise-content">
                <p><strong>Donner les types des valeurs suivantes : <code>13</code>, <code>14.5</code>, <code>'Hello World!'</code>, <code>True</code>, <code>'15.5'</code></strong></p>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Table de vérité XOR</h4>
            <div class="exercise-content">
                <p><strong>À l'aide de python, écrire un programme qui affiche dans le terminal la table de vérité de la fonction booléenne <code>xor</code>.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>print('Table de vérité du XOR')
print('a','b','s')
print(0,0,0)
print(0,1,1)
print(1,0,1)
print(1,1,0)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Somme de deux nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui permet d'afficher la somme de deux nombres entiers de la forme 'La somme est x+y' avec x et y défini précédemment.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>x = 4
y = 3
print('La somme est', x+y)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Affichage amélioré</h4>
            <div class="exercise-content">
                <p><strong>Améliorer le programme précédent pour qu'il affiche 'La somme de x et y est x+y'.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>x = 4
y = 3
print('La somme de',x, ' et ', y, ' est ', x+y)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Concaténation de chaînes</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui instancie deux chaînes de caractères, les concatène et affiche le résultat sous la forme <code>'La chaîne résultante est : [résultat]'</code>.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>chaine_a = "Bonjour"
chaine_b = "Au Revoir"
print("La chaîne résultante est :", chaine_a+chaine_b)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Étude de code</h4>
            <div class="exercise-content">
                <p><strong>Évaluer les valeurs de result à la fin de chaque programme.</strong></p>
                <pre><code>x = 8
y = 6
if x > y:
    result = x - y
else:
    result = y - x</code></pre>
                <pre><code>a = 4
b = 9
if a < b:
    result = a + b
else:
    result = a * b</code></pre>
                <pre><code>m = 7
n = 3
if m % 2 == 0:
    result = m * n
else:
    result = m + n</code></pre>
                <p><strong>À l'aide de python, évaluer les résultats de ces comparaisons avec x = 5, x = 10 et x = -20</strong></p>
                <ol>
                    <li>x < 20 and x > - 20</li>
                    <li>x > 5 or x < 3</li>
                    <li><code>not (x == 10)</code></li>
                    <li><code>x >= 0 and x <= 10</code></li>
                    <li><code>x % 2 == 0 or x % 3 == 0</code></li>
                    <li><code>x < 0 or (x > 0 and x % 2 != 0)</code></li>
                </ol>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Parité d'un nombre</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui affiche dans le terminal si un nombre est pair ou impair.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>a = int(input("Entrez un nombre"))
if a % 2 == 0:  # Si le reste de la division de a par 2 est 0 -> Si 2 divise a
    print("pair")
else:
    print("impair")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="easy-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Maximum entre trois nombres</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui permet de trouver la valeur maximale entre trois variables entières. Ce programme affichera dans la console : "Le nombre <code>x</code> est plus grand que <code>y</code> et <code>z</code>.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>val_1 = int(input("Valeur 1"))
val_2 = int(input("Valeur 2"))
val_3 = int(input("Valeur 3"))
if val_1 > val_2 and val_1 > val_3:
    print(val_1, " est la plus grande")
elif val_2 > val_1 and val_2 > val_3:
    print(val_2, " est la plus grande")
elif val_3 > val_1 and val_3 > val_2:
    print(val_3, " est la plus grande")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Calculatrice basique</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui est une calculatrice basique. Elle demandera à l'utilisateur 2 nombres entiers <code>a</code> et <code>b</code> et un opérateur (<code>+</code>,<code>-</code>,<code>*</code>,<code>/</code>). Ce programme affichera : L'opération <code>a</code> <code>operateur</code> <code>b</code> vaut ...</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>a = int(input("Entrez un premier nombre"))
b = int(input("Entrez un second nombre"))
operateur = input("Entrez un opérateur : + - / *")
if operateur == "+":
    print(a+b)
elif operateur == "-":
    print(a-b)
elif operateur == "*":
    print(a*b)
elif operateur == "/":
    # On ne peut pas diviser par zéro
    if b != 0:
        print(a/b)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Profit ou perte</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui étant donné deux valeurs cout_de_production et prix_de_vente, affiche dans le terminal <code>profit</code> si le cout est inférieur au prix de vente, <code>perte</code> sinon.</strong></p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>prix_de_vente = int(input("Entrez un prix de vente"))
cout_de_production = int(input("Entrez un coût de production"))

if prix_de_vente > cout_de_production:
    print("profit")
elif prix_de_vente == cout_de_production:
    print("pas de marge")
else:
    print("perte")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊🦊</div>
            <h4 class="exercise-title">Mentions au baccalauréat</h4>
            <div class="exercise-content">
                <p><strong>Écrire un programme qui prend une note sur 20 et affiche dans le terminal si l'étudiant a obtenu une mention :</strong></p>
                <ul>
                    <li><code>'Très bien'</code> pour une note supérieure ou égale à 16.</li>
                    <li><code>'Bien'</code> pour une note entre 14 et 15.</li>
                    <li><code>'Assez bien'</code> pour une note entre 12 et 13.</li>
                    <li><code>'Passable'</code> pour une note entre 10 et 11.</li>
                    <li><code>'Échec'</code> pour une note inférieure à 10.</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code># Demander à l'utilisateur de saisir une note
note = float(input("Entrez une note sur 20 : "))

# Vérifier la mention correspondante et afficher le résultat
if note >= 16:
    print("Mention : Très bien")
elif 14 <= note <= 15:
    print("Mention : Bien")
elif 12 <= note <= 13:
    print("Mention : Assez bien")
elif 10 <= note <= 11:
    print("Mention : Passable")
else:
    print("Mention : Échec")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">
<div class="exercise-cards">
    <p>Aucun exercice difficile pour cette fiche.</p>
</div>
</div>
