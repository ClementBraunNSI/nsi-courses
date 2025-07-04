# Fiche de Cours : Piles et Files en Python (Implémentation POO)

## 1. Introduction aux Structures Linéaires

Les **piles** (LIFO - Last In First Out) et les **files** (FIFO - First In First Out) sont des structures de données fondamentales en informatique. Nous allons les implémenter en Python en utilisant la Programmation Orientée Objet.

## 2. Le Type de Données Abstrait : Pile (Stack)

Une pile est une structure de données linéaire qui suit le principe LIFO (Last In, First Out - Dernier Entré, Premier Sorti). Imaginez une pile d'assiettes : vous ne pouvez ajouter ou retirer une assiette que par le dessus.

### Opérations Fondamentales

Soit $P$ une pile et $e$ un élément :

*   **`creer_pile()` → Pile**
    *   Description : Crée une nouvelle pile vide.
    *   Axiome : `est_vide(creer_pile())` est Vrai.
*   **`empiler(P, e)` → Pile**
    *   Description : Ajoute $e$ au sommet de la pile $P$.
    *   Axiome : `sommet(empiler(P, e))` est $e$.
    *   Axiome : `depiler(empiler(P, e))` est $e$.
*   **`depiler(P)` → Pile**
    *   Description : Retire l'élément au sommet de la pile $P$ et le renvoie. Précondition : $P$ ne doit pas être vide.
    *   Exemple : Si $P = [e_1, e_2, e_3]$, alors `depiler(P)` donne $P = [e_1, e_2]$.
    *   Axiome : `depiler(empiler(creer_pile(), e))` est une pile vide.
*   **`sommet(P)` → Element**
    *   Description : Retourne l'élément au sommet de la pile $P$ sans le retirer. Précondition : $P$ ne doit pas être vide.
    *   Exemple : Si $P = [e_1, e_2, e_3]$, alors `sommet(P)` retourne $e_3$.
*   **`est_vide(P)` → Booléen**
    *   Description : Retourne Vrai si la pile $P$ est vide, Faux sinon.

### Comportement d'une Pile (Exemple Conceptuel)

Supposons que nous ayons une pile `P` initialement vide (`P = creer_pile()`):
1. `empiler(P, 10)`  => La pile $P$ devient `[10]` (10 est au sommet)
2. `empiler(P, 20)`  => La pile $P$ devient `[10, 20]` (20 est au sommet)
3. `sommet(P)`       => Retourne `20` (la pile $P$ reste `[10, 20]`)
4. `depiler(P)`      => La pile $P$ devient `[10]`. L'opération retourne `20`.
5. `est_vide(P)`     => Retourne `Faux`
6. `depiler(P)`      => La pile $P$ devient `[]`. L'opération retourne `10`.
7. `est_vide(P)`     => Retourne `Vrai`

## 3. Le Type de Données Abstrait : File (Queue)

Une file est une structure de données linéaire qui suit le principe FIFO (First In, First Out - Premier Entré, Premier Sorti). Pensez à une file d'attente au cinéma : la première personne arrivée est la première servie.

### Opérations Fondamentales

Soit $F$ une file et $e$ un élément :

*   **`creer_file()` → File**
    *   Description : Crée une nouvelle file vide.
    *   Axiome : `est_vide(creer_file())` est Vrai.
*   **`enfiler(F, e)` → File**
    *   Description : Ajoute $e$ à la fin (queue) de la file $F$.
    *   Exemple : Si $F = [e_1, e_2]$, alors `enfiler(F, e_3)` donne $F = [e_1, e_2, e_3]$.
    *   Axiome : `est_vide(enfiler(F, e))` est Faux.
    *   Axiome (si $F$ est vide) : `tete(enfiler(creer_file(), e))` est $e$.
    *   Axiome (si $F$ n'est pas vide) : `tete(enfiler(F, e))` est `tete(F)`.
*   **`defiler(F)` → File**
    *   Description : Retire l'élément en tête de la file $F$ et le renvoie. Précondition : $F$ ne doit pas être vide.
    *   Exemple : Si $F = [e_1, e_2, e_3]$, alors `defiler(F)` donne $F = [e_2, e_3]$.
    *   Axiome : `defiler(enfiler(creer_file(), e))` est e.
*   **`tete(F)` → Element**
    *   Description : Retourne l'élément en tête de la file $F$ sans le retirer. Précondition : $F$ ne doit pas être vide.
    *   Exemple : Si $F = [e_1, e_2, e_3]$, alors `tete(F)` retourne $e_1$.
*   **`est_vide(F)` → Booléen**
    *   Description : Retourne Vrai si la file $F$ est vide, Faux sinon.
