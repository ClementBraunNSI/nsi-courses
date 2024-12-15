# Jour 1 : Calculer le prix des courses du Reveillon

Le reveillon du Nouvel An est une fête généralement partagée en famille ou entre amis.

Une organisation généralement proposée est de partager les frais pour éviter que tout le monde ramène des denrées et limiter les doublons ou le gachis.

Vous préparez votre soirée du nouvel an et prévoyez d'inviter 20 personnes.

Le problème est que la machine qui sort le ticket de caisse est tombée en panne à l'édition du ticket et que l'on ne peut pas voir le prix total du ticket.

## Informations necessaires

On considère **un ticket de caisse** modélisé sous la forme d'une **liste** Python et le **nombre d'invités** un nombre **entier** (évidemment un personne ne peut pas être divisée).
Ce ticket de caisse retrace pour chaque article leur prix.
On considère uniquement les prix totaux, on ne considère pas la quantité de produits.

## Exercice Principal

On aimerait savoir quelle somme va dépenser chacun des participant à la petite fête pour qu'ils puissent anticiper le remboursement de l'hôte qui a avancé les frais.


!!! fox_correction "Somme totale du ticket"

    **Écrire une fonction `somme_totale_ticket` qui prend en paramètre un ticket de caisse et renvoie la somme totale des articles.**

    *Rappel : Le ticket correspond à une liste de `float`.*

    **Essayer la fonction avec le ticket de caisse suivant : **

    ```python
        ticket_caisse = [
        12.99, 8.49, 4.59, 15.89, 3.99, 7.49, 19.99, 2.59, 9.99, 5.79,
        13.49, 4.79, 6.99, 11.59, 8.79, 14.49, 3.69, 7.99, 10.49, 2.79,
        5.99, 16.89, 9.49, 6.79, 12.59, 4.29, 3.89, 10.99, 8.59, 15.99,
        7.89, 9.79, 6.39, 13.99, 4.69, 11.99, 14.59, 3.79, 10.79, 5.89,
        8.39, 16.49, 7.59, 12.89, 9.39, 4.59, 5.49, 13.59, 6.89, 8.99
        ]
    ```

Maintenant que nous connaissons le prix global du ticket, on voudrait savoir quelle est la participation de chacun des invités de la soirée.

!!! fox_correction "Participation des invités"

    **Écrire une fonction `participation des invités` qui prend en paramètre un ticket de caisse et un nombre d'invités et renvoie la participation de chaque invité.**

    *Indication : Cette fonction devra utiliser la fonction précédente.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi que la somme que chaque invité doit payer.**