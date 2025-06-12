# 📦 II - Fiche d'exercice : Les tuples et les listes

!!! danger "⚠️ Attention"
      Tous les exercices, s'ils sont réalisés par des boucles `for`, doivent être faits avec une boucle sur les indices et une boucle sur les valeurs.
      ```python
         l = [1,2,3,4]
         # for par valeur:
         for elt in l:
            print(l)

         # for par indice (utilisation de len() qui permet d'avoir la taille d'une séquence):
         for i in range(len(l)):
            print(l[i])
      ```

<style>
.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

.exercise-card {
    background: var(--md-default-bg-color);
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 3px solid;
    display: flex;
    overflow: hidden;
    width: 100%;
    max-width: 100%;
}

.exercise-content-wrapper {
    flex: 1 1 auto;
    min-width: 0;
    padding-right: 1rem;
    max-width: 100%;
    overflow: hidden;
}

.solution-wrapper {
    flex: 0 0 0;
    width: 0;
    overflow: hidden;
    transition: flex 0.4s ease, width 0.4s ease;
    border-left: 1px solid #e0e0e0;
    background: rgba(0, 0, 0, 0.02);
}

.solution-wrapper.show {
    flex: 0 0 40%;
    width: 40%;
    padding-left: 1rem;
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.intro:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
}

.exercise-card.easy {
    border-left-color: #2196F3;
}

.exercise-card.easy:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(33, 150, 243, 0.4);
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.medium:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 152, 0, 0.4);
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.exercise-card.hard:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(244, 67, 54, 0.4);
}

.exercise-card.important {
    border-left-color: #ff8c42;
    background: linear-gradient(135deg, rgba(255, 140, 66, 0.05) 0%, rgba(255, 140, 66, 0.02) 100%);
}

.exercise-card.important:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 140, 66, 0.4);
}

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.1rem;
    font-weight: 600;
}

.exercise-content {
    margin-bottom: 1rem;
    line-height: 1.6;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.easy {
    background: rgba(33, 150, 243, 0.1);
    color: #2196F3;
}

.difficulty-badge.medium {
    background: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.difficulty-badge.important {
    background: rgba(255, 140, 66, 0.1);
    color: #ff8c42;
}

.toggle-solution {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
}

.toggle-solution:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.toggle-solution.active {
    background: linear-gradient(135deg, #ff7f50 0%, #ff6347 100%);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution {
    height: 100%;
    overflow-y: auto;
}

.solution pre {
    margin: 0;
    font-size: 0.85rem;
}

.solution pre {
    margin: 0;
}

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
    padding: 0;
}

.section-tab {
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
    min-width: 200px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.section-content {
    display: none;
    margin-top: 2rem;
    padding: 2rem;
    background: #fafafa;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
}

.section-content.active {
    display: block;
}
</style>

<script>
function toggleSolution(button) {
    const card = button.closest('.exercise-card');
    const solutionWrapper = card.querySelector('.solution-wrapper');
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.classList.contains('show')) {
        solutionWrapper.classList.remove('show');
        button.classList.remove('active');
        button.innerHTML = '<span class="arrow">→</span> Voir la correction';
    } else {
        solutionWrapper.classList.add('show');
        button.classList.add('active');
        button.innerHTML = '<span class="arrow">←</span> Masquer la correction';
    }
}

function showSection(sectionId) {
    // Masquer toutes les sections
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher la section sélectionnée
    document.getElementById(sectionId).classList.add('active');
    event.target.classList.add('active');
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.section-tab').click();
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau Facile</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau Difficile</button>
    <button class="section-tab" onclick="showSection('important-section')">⭐ Algorithmes Importants</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐</div>
            <h4 class="exercise-title">Exercice 1 - Création de structures</h4>
            <div class="exercise-content">
                <strong>Créer un tuple nommé <code>mon_tuple</code> qui contient les éléments 1,2,3,4,5 et une liste <code>ma_liste</code> qui contient les éléments suivants 'a','b','c','d','e'.</strong><br>
                <strong>Les afficher dans le terminal.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">mon_tuple = (1,2,3,4,5)
ma_liste = ['a','b','c','d','e']
print(mon_tuple)
print(ma_liste)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐</div>
            <h4 class="exercise-title">Exercice 2 - Accès aux éléments</h4>
            <div class="exercise-content">
                <strong>Afficher dans le terminal le troisième élément de <code>mon_tuple</code> et le premier élément de <code>ma_liste</code>.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">print(mon_tuple[2])  # Troisième élément (index 2)
print(ma_liste[0])   # Premier élément (index 0)</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐</div>
            <h4 class="exercise-title">Exercice 3 - Modification d'éléments</h4>
            <div class="exercise-content">
                <strong>Modifier le deuxième élément de <code>ma_liste</code> par 'z'.<br>
            Vérifier la modification en affichant la liste dans le terminal.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">ma_liste[1] = 'z'  # Modification du deuxième élément
print(ma_liste)     # Vérification</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐</div>
            <h4 class="exercise-title">Exercice 4 - Ajout et suppression</h4>
            <div class="exercise-content">
                <strong>Ajouter l'élément 'f' dans <code>ma_liste</code>.<br>
            Supprimer le premier élément de <code>ma_liste</code>.<br>
            Vérifier les modifications en affichant la liste dans le terminal.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">ma_liste.append('f')  # Ajout de 'f'
ma_liste.pop(0)       # Suppression du premier élément
print(ma_liste)       # Vérification</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐</div>
            <h4 class="exercise-title">Exercice 5 - Parcours avec boucles</h4>
            <div class="exercise-content">
                <strong>Afficher dans le terminal tous les éléments de <code>mon_tuple</code> et <code>ma_liste</code> un à un à l'aide d'une boucle <code>for</code>.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Parcours par valeur
for elt in mon_tuple:
    print(elt)

for elt in ma_liste:
    print(elt)

# Parcours par indice
for i in range(len(mon_tuple)):
    print(mon_tuple[i])

for i in range(len(ma_liste)):
    print(ma_liste[i])</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction ⭐⭐</div>
            <h4 class="exercise-title">Exercice 6 - Exercice complet</h4>
            <div class="exercise-content">
                <strong>Créer une liste <code>nombres</code> qui contient les chiffres allant de 1 à 9. (Proposer une version par compréhension).<br>
            Afficher dans le terminal les 5 premiers éléments de la liste en utilisant une boucle while.<br>
            Afficher les éléments du quatrième au huitième en utilisant une boucle for.<br>
            Afficher les éléments de la liste <code>nombres</code> dans le sens inverse en utilisant une boucle while.</strong>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python"># Création de la liste
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ou par compréhension :
nombres = [i for i in range(1, 10)]

# 5 premiers éléments avec while
i = 0
while i < 5:
    print(nombres[i])
    i += 1

# Éléments du 4ème au 8ème avec for
for i in range(3, 8):  # indices 3 à 7
    print(nombres[i])

# Sens inverse avec while
i = len(nombres) - 1
while i >= 0:
    print(nombres[i])
    i -= 1</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="easy-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">💻 Somme d'éléments</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>somme_elements</code> qui prend une liste de nombres en paramètres et renvoie la somme de tous les éléments.</strong><br>
            <em>Exemple : somme_elements([1, 2, 3, 4]) doit renvoyer 10.</em>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def somme_elements(liste:list)->int:
    somme = 0
    for elt in liste:
        somme = somme + elt
    return somme</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">Compter les nombres pairs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>compter_pairs</code> qui prend une liste d'entiers et renvoie le nombre d'éléments pairs dans cette liste.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> compter_pairs([1,2,3,4,5])
2</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def compter_pairs(liste:list)->int:
    nombre_pairs = 0
    for elt in liste:
        if elt % 2 == 0:
            nombre_pairs = nombre_pairs + 1
    return nombre_pairs</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">Longueur des chaînes</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>longueur_chaines</code> qui prend une liste de chaînes de caractères et renvoie une liste contenant la longueur de chaque chaîne.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> longueur_chaines(["abc", "de", "fghi"])
[3, 2, 4]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def longueur_chaines(liste:list)->list:
    liste_longueurs = []
    for elt in liste:
        taille_elt = len(elt)
        liste_longueurs.append(taille_elt)
    return liste_longueurs</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">Produit d'éléments</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>produit_elements</code> qui prend une liste d'entiers et renvoie le produit de tous les éléments. Attention aux cas où la liste est vide.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> produit_elements([2, 3, 4])
24
>>> produit_elements([])
1</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def produit_elements(liste:list)->int:
    if not liste:  # si la liste est vide
        return 1
    produit = 1
    for elt in liste:
        produit = produit * elt
    return produit</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">Compter les occurrences</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>compter_occurrences</code> qui prend une liste et un élément, et renvoie le nombre de fois que cet élément apparaît dans la liste.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> compter_occurrences([1, 2, 2, 3, 2], 2)
3</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def compter_occurrences(liste:list, valeur: int)->int:
    occurrences = 0
    for elt in liste:
        if elt == valeur:
            occurrences = occurrences + 1
    return occurrences</code></pre>
            </div>
        </div>
    </div>



    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile ⭐</div>
            <h4 class="exercise-title">Calcul de moyenne</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>moyenne</code> qui prend en paramètre une liste d'entiers et renvoie la moyenne de tous les nombres présents dans cette liste.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> moyenne([1, 2, 3, 4, 5])
3.0
>>> moyenne([])
0</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def moyenne(liste:list)->float:
    if not liste:  # si la liste est vide
        return 0
    taille_liste = len(liste)
    somme = 0
    for elt in liste:
        somme = somme + elt
    return somme / taille_liste</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Filtrer les nombres positifs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>filtrer_positifs</code> qui prend une liste de nombres et renvoie une nouvelle liste contenant uniquement les nombres positifs.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> filtrer_positifs([-1, 0, 3, -7, 8])
[3, 8]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def filtrer_positifs(liste:list)->list:
    positifs = []
    for elt in liste:
        if elt > 0:
            positifs.append(elt)
    return positifs</code></pre>
            </div>
        </div>
    </div>



    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Concaténer des chaînes</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>concatener_chaines</code> qui prend une liste de chaînes de caractères et renvoie une seule chaîne qui est la concaténation de toutes les chaînes de la liste.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> concatener_chaines(["Bonjour", " ", "le", " ", "monde"])
"Bonjour le monde"</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def concatener_chaines(liste:list)->str:
    concatenation = ""
    for chaine in liste:
        concatenation = concatenation + chaine
    return concatenation</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Inverser une liste</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>inverser_liste</code> qui prend une liste et renvoie une nouvelle liste avec les éléments dans l'ordre inverse.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> inverser_liste([1, 2, 3])
[3, 2, 1]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def inverser_liste(liste:list)->list:
    liste_inversee = []
    for i in range(len(liste)-1, -1, -1):
        liste_inversee.append(liste[i])
    return liste_inversee</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Valeurs uniques</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>valeurs_uniques</code> qui prend une liste et renvoie une nouvelle liste contenant les éléments sans doublons (dans l'ordre d'apparition).</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> valeurs_uniques([1, 2, 2, 3, 4, 4])
[1, 2, 3, 4]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def valeurs_uniques(liste:list)->list:
    liste_valeurs = []
    for elt in liste:
        if elt not in liste_valeurs:
            liste_valeurs.append(elt)
    return liste_valeurs</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Séparer pairs et impairs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>separer_pairs_impairs</code> qui prend une liste d'entiers et renvoie deux listes : une avec les éléments pairs et une autre avec les éléments impairs.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> separer_pairs_impairs([1, 2, 3, 4, 5])
([2, 4], [1, 3, 5])</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def separer_pairs_impairs(liste:list)->tuple:
    pairs = []
    impairs = []
    for elt in liste:
        if elt % 2 == 0:
            pairs.append(elt)
        else:
            impairs.append(elt)
    return pairs, impairs</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Recherche des diviseurs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>diviseurs</code> qui prend un entier en paramètre et renvoie la liste de ses diviseurs.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> diviseurs(6)
[1, 2, 3, 6]
>>> diviseurs(10)
[1, 2, 5, 10]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def diviseurs(valeur:int)->list:
    diviseurs = []
    for i in range(1, valeur+1):  # On commence à 1 pour éviter la division par 0
        if valeur % i == 0:
            diviseurs.append(i)
    return diviseurs</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Liste croissante</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>est_croissante</code> qui prend une liste d'entiers en paramètre et renvoie True si les éléments de la liste sont dans l'ordre croissant, False sinon.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> est_croissante([1, 2, 3, 4])
True
>>> est_croissante([1, 3, 2, 4])
False</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def est_croissante(liste:list)->bool:
    i = 0
    while i < len(liste) - 1 and liste[i] <= liste[i+1]:
        i = i + 1
    return i == len(liste)-1</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Échange de valeurs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>echange</code> qui prend en paramètres une liste et deux indices, et échange les valeurs aux positions i et j dans la liste passée en paramètres.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> liste1 = [1, 2, 3, 4]
>>> echange(liste1, 1, 2)
>>> liste1
[1, 3, 2, 4]
>>> liste2 = [5, 10, 15]
>>> echange(liste2, 0, 2)
>>> liste2
[15, 10, 5]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">#1ère solution : passer par une troisième valeur
def echange(liste:list, i:int, j:int)->None:
    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp</code></pre>
            <pre><code class="language-python">#2e solution : solution Python-esque
def echange(liste:list, i:int, j:int)->None:
    liste[i], liste[j] = liste[j], liste[i]</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire ⭐⭐</div>
            <h4 class="exercise-title">Rangement de valeurs</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>rangement_valeurs</code> qui prend en paramètre une liste et un élément, et renvoie 3 listes : une liste contenant les valeurs inférieures à l'élément, une liste avec l'élément si présent, et une liste avec les valeurs supérieures.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> rangement_valeurs([1, 7, 4, 3, 6, 2, 8], 5)
([1, 4, 3, 2], [], [7, 6, 8])
>>> rangement_valeurs([1, 2, 4, 3, 6, 2, 8], 2)
([1], [2, 2], [4, 3, 6, 8])</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def rangement_valeurs(liste:list, valeur:int)->tuple[list, list, list]:
    inferieures = []
    egales = []
    superieures = []
    for elt in liste:
        if elt > valeur:
            superieures.append(elt)
        elif elt == valeur:
            egales.append(elt)
        else:
            inferieures.append(elt)
    return inferieures, egales, superieures</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="important-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Algorithme Important ⭐</div>
            <h4 class="exercise-title">🔍 Recherche d'un élément</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>presence</code> qui prend en paramètre une valeur et une liste et renvoie <code>True</code> si la valeur demandée est dans la liste, <code>False</code> sinon.</strong><br>
                <em>Exemple :</em>
                <pre><code>>>> presence(3, [1, 2, 3, 4])
True
>>> presence(5, [1, 2, 3, 4])
False</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def presence(valeur: int, liste: list) -> bool:
    present = False
    for elt in liste:
        if elt == valeur:
            present = True
    return present</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Algorithme Important ⭐</div>
            <h4 class="exercise-title"> Minimum d'une liste</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>minimum</code> qui prend en paramètre une liste et renvoie la valeur minimale dans la liste.</strong><br>
                <em>Exemple :</em>
                <pre><code>>>>  minimum([3, 1, 9, 2])
1</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def minimum(liste: list) -> int:
    mini = liste[0]
    for elt in liste:
        if elt < mini:
            mini = elt</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card important">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge important">Algorithme Important ⭐</div>
            <h4 class="exercise-title"> Maximum d'une liste</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>maximum</code> qui prend en paramètre une liste et renvoie la valeur maximale dans la liste.</strong><br>
                <em>Exemple :</em>
                <pre><code>>>>  maximum([3, 1, 9, 2])
9</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def maximum(liste: list) -> int:
    maxi = liste[0]
    for elt in liste:
        if elt > mini:
            maxi = elt</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile ⭐⭐⭐</div>
            <h4 class="exercise-title">Compteur de voyelles</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>compter_voyelles</code> qui prend une liste de chaînes de caractères et renvoie le nombre total de voyelles présentes dans toutes les chaînes.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> compter_voyelles(["chat", "chien"])
3
>>> compter_voyelles(["bonjour", "python"])
4</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def compter_voyelles(liste:list)->int:
    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = 0
    for mot in liste:
        for lettre in mot:
            if lettre in voyelles:
                nombre_voyelles += 1
    return nombre_voyelles</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile ⭐⭐⭐</div>
            <h4 class="exercise-title">Éléments en double</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>valeurs_en_double</code> qui prend une liste et renvoie une nouvelle liste contenant uniquement les éléments qui apparaissent plus d'une fois (sans répétitions supplémentaires).</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> valeurs_en_double([1, 2, 2, 3, 4, 4, 5])
[2, 4]
>>> valeurs_en_double(["a", "b", "a", "c", "b", "d"])
["a", "b"]</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def valeurs_en_double(liste:list)->list:
    doublons = []
    deja_vus = []
    for elt in liste:
        if elt in deja_vus and elt not in doublons:
            doublons.append(elt)
        else:
            deja_vus.append(elt)
    return doublons</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile ⭐⭐⭐</div>
            <h4 class="exercise-title">Recherche d'indice</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>indice_element</code> qui prend une liste et un élément, et renvoie l'indice de la première occurrence de cet élément dans la liste, ou -1 s'il n'est pas présent.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> indice_element([10, 20, 30], 20)
1
>>> indice_element([10, 20, 30], 40)
-1</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def indice_element(liste:list, valeur:int)->int:
    i = 0
    while i < len(liste) and liste[i] != valeur:
        i += 1
    if i == len(liste):
        return -1
    return i</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile ⭐⭐⭐</div>
            <h4 class="exercise-title">Fusion sans doublons</h4>
            <div class="exercise-content">
                <strong>Écrire une fonction <code>fusionner_sans_doublons</code> qui prend en paramètres deux listes et renvoie une nouvelle liste contenant tous les éléments des deux listes sans doublons.</strong><br>
            <em>Exemple :</em>
            <pre><code>>>> fusionner_sans_doublons([1, 2, 3], [2, 3, 4])
[1, 2, 3, 4]
>>> fusionner_sans_doublons(['a', 'b'], ['b', 'c', 'a'])
['a', 'b', 'c']</code></pre>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
        </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def fusionner_sans_doublons(liste1:list, liste2:list)->list:
    resultat = []
    # On ajoute les éléments de la première liste
    for elt in liste1:
        if elt not in resultat:
            resultat.append(elt)
    # On ajoute les éléments de la deuxième liste
    for elt in liste2:
        if elt not in resultat:
            resultat.append(elt)
    return resultat</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

