<style>
.course-header { background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 3rem; margin: 2rem 0; border: 1px solid rgba(102,126,234,0.2); text-align: center; }
.course-title { font-size: 2.2rem; font-weight: 700; background: linear-gradient(135deg,#667eea,#764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 2rem; margin: 2rem 0; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
.section-title { font-size: 1.6rem; font-weight: 600; color: #667eea; margin-bottom: 1rem; text-align: center; }
.definition-box { background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.05)); border-left: 5px solid #667eea; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; }
.definition-title { font-weight: 600; color: #667eea; margin-bottom: 0.6rem; }
.code-example { background: #1a202c; color: #e2e8f0; padding: 1rem; border-radius: 10px; margin: 1rem 0; font-family: 'Courier New', monospace; overflow-x: auto; border-left: 4px solid #4299e1; }
</style>

<div class="course-header">
  <h1 class="course-title">C – Constructions élémentaires</h1>
  <p>Bases: compilation, entrées/sorties, types, contrôles, boucles, fonctions</p>
</div>

<div class="concept-section">
  <h2 class="section-title">Compiler et exécuter</h2>
  <div class="definition-box">
    <div class="definition-title">Principe</div>
    <div>Le C est compilé: le code source (`.c`) est traduit en binaire exécuté par le système.</div>
  </div>
  <div class="code-example"><div class="code-title">Exemple</div>

```c
#include <stdio.h>

int main(void) {
    printf("Bonjour, C!\n");
    return 0;
}
```

Compilation et exécution (exemple):

```sh
gcc main.c -o main && ./main
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Types et variables</h2>
  <div class="definition-box">
    <div class="definition-title">Types usuels</div>
    <div>`int`, `float`, `double`, `char` (caractère). Déclarer puis initialiser.</div>
  </div>
  <div class="code-example">

```c
int age = 20;
double taille = 1.72;
char initiale = 'C';
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Entrées / sorties</h2>
  <div class="definition-box">
    <div class="definition-title">printf / scanf</div>
    <div>`printf` affiche, `scanf` lit au clavier. Les formats (`%d`, `%f`, `%c`, `%s`) indiquent le type.</div>
  </div>
  <div class="code-example">

```c
#include <stdio.h>

int main(void) {
    int n; 
    printf("Entrez un entier: ");
    scanf("%d", &n);
    printf("Vous avez saisi: %d\n", n);
    return 0;
}
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Conditions</h2>
  <div class="definition-box"><div class="definition-title">if / else</div><div>Tester des conditions pour exécuter des branches de code.</div></div>
  <div class="code-example">

```c
int x = 5;
if (x > 0) {
    printf("Positif\n");
} else {
    printf("Non-positif\n");
}
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Boucles</h2>
  <div class="definition-box"><div class="definition-title">for / while</div><div>Répéter une instruction tant qu’une condition est vraie ou sur un compteur.</div></div>
  <div class="code-example">

```c
for (int i = 0; i < 5; i++) {
    printf("i=%d\n", i);
}

int j = 0;
while (j < 3) {
    printf("j=%d\n", j);
    j++;
}
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Fonctions</h2>
  <div class="definition-box"><div class="definition-title">Définir et appeler</div><div>Une fonction prend des paramètres et renvoie un résultat (ou `void`).</div></div>
  <div class="code-example">

```c
int carre(int n) { return n*n; }

int main(void) {
    printf("carre(4)=%d\n", carre(4));
    return 0;
}
```
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">Tableaux (arrays)</h2>
  <div class="definition-box"><div class="definition-title">Déclaration et parcours</div><div>Suite de valeurs de même type, indexées à partir de 0.</div></div>
  <div class="code-example">

```c
int t[3] = {10, 20, 30};
for (int i = 0; i < 3; i++) {
    printf("t[%d]=%d\n", i, t[i]);
}
```
  </div>
</div>
<script>
(function(){
  try {
    var ok = sessionStorage.getItem('cp_token');
    if (ok !== 'ok') { location.href = '/'; }
  } catch(e) { location.href = '/'; }
})();
</script>
