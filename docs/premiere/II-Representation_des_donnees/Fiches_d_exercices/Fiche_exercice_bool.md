# 🔄 Fiche d'exercices : Booléens et Comparaisons en Programmation

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */
.exercise-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.exercise-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4);
}

.exercise-title {
    color: #ffffff;
    font-size: 1.3em;
    font-weight: bold;
    margin-bottom: 15px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.difficulty-tabs {
    display: flex;
    margin: 20px 0;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.tab {
    flex: 1;
    padding: 12px 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: bold;
    border: none;
    outline: none;
}

.tab.easy { background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); }
.tab.medium { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
.tab.hard { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }

.tab:hover {
    transform: translateY(-2px);
    filter: brightness(1.1);
}

.solution {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    border-left: 4px solid #4CAF50;
    backdrop-filter: blur(5px);
}

.solution-toggle {
    background: linear-gradient(135deg, #4CAF50, #45a049);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 0.9em;
    transition: all 0.3s ease;
    margin-bottom: 10px;
}

.solution-toggle:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.solution-content {
    display: none;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.code-block {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    padding: 15px;
    font-family: 'Courier New', monospace;
    margin: 10px 0;
    border-left: 3px solid #ff6b6b;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: bold;
}
</style>

## 📚 Partie 1 : Introduction aux Booléens

Un booléen est un type de donnée ayant deux valeurs possibles : `True` (vrai) ou `False` (faux).

### 🎯 Exercice 1 : Comprendre les booléens ⭐

Quel sera le résultat de ces expressions ? `True` ou `False`.

1. `10 > 5` ➔ `______`
2. `7 == 9` ➔ `______`
3. `3 <= 3` ➔ `______`
4. `False != True` ➔ `______`
5. `not False` ➔ `______`
6. `5 != 5` ➔ `______`

## 📚 Partie 2 : Opérateurs de comparaison

Les opérateurs de comparaison sont utilisés pour comparer deux valeurs. Le résultat d'une comparaison est toujours un booléen (`True` ou `False`).

### 📝 Liste des opérateurs:

- `==` : égal à
- `!=` : différent de
- `>` : supérieur à
- `<` : inférieur à
- `>=` : supérieur ou égal à
- `<=` : inférieur ou égal à

### 🎯 Exercice 2 : Comparaisons simples ⭐⭐

Donner le résultat des expressions suivantes :

1. `8 == 8` ➔ `______`
2. `4 != 2` ➔ `______`
3. `7 > 10` ➔ `______`
4. `6 >= 6` ➔ `______`
5. `3 < 8` ➔ `______`

## 📚 Partie 3 : Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs expressions booléennes :

- `and` : renvoie `True` si les deux conditions sont vraies.
- `or` : renvoie `True` si au moins une condition est vraie.
- `not` : inverse la valeur d'une condition.

### 🎯 Exercice 3 : Utiliser les opérateurs logiques ⭐⭐

Pour chaque expression, écrire le résultat (`True` ou `False`).

1. `(5 > 3) and (2 == 2)` ➔ `______`
2. `(4 < 1) or (6 != 5)` ➔ `______`
3. `not (10 == 10)` ➔ `______`
4. `(7 <= 7) and (8 > 9)` ➔ `______`
5. `not ((3 != 3) or (5 < 2))` ➔ `______`

<div class="exercise-card">
<h4 class="exercise-title">Exercice 4 - Expressions booléennes complexes ⭐⭐⭐</h4>

**Évaluer les expressions suivantes étape par étape :**

1. `(3 < 5) and (not (2 == 3)) or (4 >= 4)`
2. `not ((10 > 5) and (7 != 7)) or (3 <= 3)`
3. `(True and False) or (not False and True)`
4. `((5 > 3) or (2 < 1)) and (not (4 == 4))`

<button class="solution-toggle" onclick="toggleSolution('sol4')">💡 Voir les solutions</button>
<div class="solution" id="sol4">
<div class="solution-content">
<strong>Solutions :</strong><br>
1. `True and True or True` = `True`<br>
2. `not (True and False) or True` = `True`<br>
3. `False or True` = `True`<br>
4. `True and False` = `False`
</div>
</div>
</div>

<div class="exercise-card">
<h4 class="exercise-title">Exercice 5 - Fonctions avec booléens ⭐⭐⭐</h4>

**Écrire des fonctions Python qui retournent un booléen :**

1. `est_pair(n)` : retourne `True` si n est pair
2. `est_dans_intervalle(x, a, b)` : retourne `True` si x est entre a et b (inclus)
3. `est_voyelle(lettre)` : retourne `True` si la lettre est une voyelle
4. `est_triangle_rectangle(a, b, c)` : retourne `True` si les côtés forment un triangle rectangle

<button class="solution-toggle" onclick="toggleSolution('sol5')">💡 Voir les solutions</button>
<div class="solution" id="sol5">
<div class="solution-content">
<div class="code-block">
def est_pair(n):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return n % 2 == 0<br><br>
def est_dans_intervalle(x, a, b):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return a <= x <= b<br><br>
def est_voyelle(lettre):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return lettre.lower() in 'aeiou'<br><br>
def est_triangle_rectangle(a, b, c):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
</div>
</div>
</div>
</div>

<div class="exercise-card">
<h4 class="exercise-title">Exercice 6 - Applications pratiques ⭐⭐⭐</h4>

**Résoudre les problèmes suivants avec des expressions booléennes :**

1. Un étudiant réussit son examen s'il a au moins 10/20 ET qu'il n'a pas eu 0 à l'oral. Écrire l'expression.
2. Un nombre est divisible par 6 s'il est divisible par 2 ET par 3. Écrire la fonction `divisible_par_6(n)`.
3. Une année est bissextile si elle est divisible par 4, SAUF si elle est divisible par 100, SAUF si elle est divisible par 400. Écrire la fonction `est_bissextile(annee)`.

<button class="solution-toggle" onclick="toggleSolution('sol6')">💡 Voir les solutions</button>
<div class="solution" id="sol6">
<div class="solution-content">
<strong>1.</strong> `(note >= 10) and (oral != 0)`<br><br>
<strong>2.</strong><br>
<div class="code-block">
def divisible_par_6(n):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return (n % 2 == 0) and (n % 3 == 0)
</div>
<strong>3.</strong><br>
<div class="code-block">
def est_bissextile(annee):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return (annee % 4 == 0) and ((annee % 100 != 0) or (annee % 400 == 0))
</div>
</div>
</div>
</div>

<script>
function toggleSolution(id) {
    const content = document.querySelector(`#${id} .solution-content`);
    if (content.style.display === 'none' || content.style.display === '') {
        content.style.display = 'block';
    } else {
        content.style.display = 'none';
    }
}
</script>
