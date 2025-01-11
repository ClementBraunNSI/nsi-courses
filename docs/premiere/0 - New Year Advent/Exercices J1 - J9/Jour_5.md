# Jour 5 🦊❄️🎉 : Où est passée la liste de courses ?

Jean rentre des courses et reçoit un message de sa compagne qui lui demande s'il a bien pensé à acheter tous les articles de la liste qu'elle lui avait préparée. Le problème est que Jean a perdu la liste de courses en faisant les rayons ! Heureusement, il a gardé son ticket de caisse.

Sa compagne lui renvoie par message les articles qu'il devait acheter, et Jean doit maintenant vérifier s'il a bien tout acheté pour la soirée du réveillon.

## Informations nécessaires

On considère :
- Un **article** est représenté par un **tuple** contenant le nom de l'article et son prix : `(str, float)`
- Le **ticket de caisse** est une **liste** d'articles
- La **liste de courses** est une **liste** de noms d'articles (`str`)

## Exercice Principal

!!! fox_correction "Recherche d'un article"

    **Écrire une fonction `chercher_article` qui prend en paramètre un ticket de caisse et le nom d'un article et renvoie un tuple `(bool, float)` indiquant si l'article est présent et son prix.**

    *Rappel :* 
    - Le nom des articles doit être comparé sans tenir compte de la casse (majuscules/minuscules)
    - Si l'article n'est pas trouvé, la fonction renvoie `(False, 0.0)`

    **Essayer la fonction avec le ticket de caisse suivant :**

    ```python
    ticket_de_caisse = [
        ("foie gras", 19.99),
        ("saumon fumé", 15.50),
        ("champagne", 35.99),
        ("huîtres", 22.90),
        ("bûche glacée", 12.99),
        ("pain surprise", 8.99),
        ("chocolats", 7.50),
        ("crevettes", 13.99),
        ("toasts", 3.99),
        ("biscuits apéritif", 5.49)
    ]
    ```

!!! fox_correction "Articles manquants"

    **Écrire une fonction `articles_manquants` qui prend en paramètre un ticket de caisse et une liste de courses et renvoie la liste des articles qui n'ont pas été achetés.**

    *Indication : Cette fonction devra utiliser la fonction précédente.*

    **Essayer la fonction avec la liste de courses suivante :**
    ```python
    liste_de_courses = [
            "foie gras",
            "champagne",
            "chocolats",
            "caviar",
            "huîtres",
            "saucisson"]
    ```

!!! fox_correction "Articles achetés"

    **Écrire une fonction `articles_non_achetes` qui prend en paramètre un ticket de caisse et une liste de courses et renvoie une liste de tuples `(article, prix)` correspondant aux articles de la liste qui n'ont pas été achetés.**

    *Indication : Cette fonction devra utiliser la première fonction.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi que la liste des articles manquants et la liste des articles achetés avec leur prix pour la liste de courses fournie.**