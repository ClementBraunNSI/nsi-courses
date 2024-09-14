# Nombres de Lychrel

## Définition d'un nombre de Lychrel

Dans l'univers mathématique, les nombres ont été étudiés en long, large et travers.
On peut, dans ces études parler des nombres de Lychrel.

On peut définir qu'un nombre n'est pas un nombre de Lychrel si, après un certain nombre d'additions de certains nombres, on ne tombe pas sur un nombre **palindrome**.

Le traitement est le suivant :

1. On choisit un nombre, par exemple $75$.
2. À ce nombre, on ajoute son nombre miroir, ici $57$.
3. On obtient $132$.
4. On réalise ce procédé jusqu'à trouver le palindrome associé : $75 \rightarrow 132 \rightarrow 363$.

Un nombre de Lychrel est un nombre auquel on ne peut pas (ou bien que l'on ne sait pas encore) associer un palindrome.

!!!Tip Objectifs de ce projet
    - Travail sur les **cast** : int -> str ou str -> int
    - Inversion de chaînes de caractères
    - Boucles
    - Fonctions

## Projet

**Écrire une fonction `palindrome` qui prend en paramètre une chaîne de caractère et qui renvoie True si la chaîne est un palindrome, False sinon.**
On rappelle qu'un palindrome correspond à un mot ou une expression qui peut se lire de gauche à droite et de droite à gauche.
Exemple : *kayak* est un palindrome, *$404$ est un palindrome*.

La première étape pour réaliser ce traitement mathématique est de trouver le nombre miroir correspondant au nombre que l'on doit traiter (et successivement additionner).
**Écrire une fonction `nombre_miroir` qui prend en paramètre un nombre entier et renvoie son nombre miroir.**
*Indication : vous utiliserez une boucle `for i in range(...)` qui parcourera la chaîne de caractère et vous concatènerez les différentes chaînes de caractère. Enfin, il faudra changer la chaîne de caractère en nombre entier.*

**Écrire une fonction `nombre_miroir_tq` qui prend en paramètre un nombre entier et renvoie son nombre miroir. Cette fonction devra être implémentée en employant une boucle `while` (tant que).**

Le problème d'avoir deux fonctions qui réalisent la même chose mais avec des opérations différentes est que celles-ci peuvent ne pas donner le résultat.

On doit se munir d'une fonction de vérification pour savoir si les deux fonctionnent de la même manière.

**Écrire une fonction `verification_nombre_miroir` qui prendra en paramètre un nombre entier et renvoie True si les fonctions `nombre_miroir` et `nombre_miroir_tq`**.

**Vous ne choisirez qu'une seule des deux fonctions pour la fonction finale.**

Nous avons une fonction qui teste si une chaîne de caractère est un palindrome et une autre qui permet de trouver le nombre miroir à un nombre passé en paramètre. On peut donc créer notre fonction détectrice de nombres de Lychrel.

**Écrire une fonction `nombreLychrel` qui prend en paramètre un nombre entier et qui renvoie :**

$$
\begin{equation*}
  {nombreLychrel}=
     \begin{cases}
        \text{un nombre entier}& \text{si } \text{avant 50 itérations un palindrome est trouvé} \\
        None & \text{si aucun palindrome n'est trouvé après 50 itérations} 
     \end{cases}
\end{equation*}
$$

Voici le pseudo-code associé à la fonction :

```ps
    fonction nombreLychrel(nb)
        si nb est un palindrome :
            Renvoyer nb
        sinon :
            i <- 0
            tant que nb n'est pas un palindrome
                ajouter à nb son nombre miroir

                si nb est un palindrome:
                    Renvoyer nb
                i <- i + 1
                si i > 3000:
                    Renvoyer None
```

