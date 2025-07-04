# Jour 2 🦊❄️🎉 : Calculer le prix de chaque catégories des articles pour la soirée

Suzanne, une des invitées cherche à quantifier les prix des produits achetés pour la soirée du réveillon.

Le magasin dans lequel les courses ont été faites donne des tickets où les articles sont triés par catégorie mais aucun sous-total n'est indiqué.  
*Exemple : Boulangerie-Pâtisserie, Poissonnerie, Boissons, Boucherie, Nourriture salée, Nourriture sucrée*.

## Informations nécessaires

On considère donc qu'un **article** est représenté par son **prix** (float) qu'une **catégorie d'articles** est une **liste** et que **le ticket de caisse** est une **liste de catégories d'articles**.

## Exercice Principal

On aimerait savoir combien a coûté chacunes des catégories d'articles pour quantifier où étaient les plus gros pôles de dépenses.

Le ticket de caisse est de la forme :

```python
    ticket_de_caisse = [
                        [articles de la poissonnerie], 
                        [articles de la boucherie-venaison],
                        [articles de la boulangerie-patisserie], 
                        [articles de l epicerie salee], 
                        [articles de l epicerie surcree ], 
                        [articles du rayon boisson]
                       ]

```

!!! fox_correction "Somme des catégories"

    **Écrire une fonction `somme_categories` qui prend en paramètre un ticket de caisse et renvoie une liste de `float` correspondant aux prix de chaque catégories.**

    *Rappel :* 
    - *Un article est représenté par son prix `float`.*
    - *Une catégorie est une liste de `float`*
    - *Le ticket correspond à une liste de liste de `float`.*
    - *On fournit une liste avec les noms des catégories où l'indice correspondant au nom est le même dans la liste.*
    ```python
        >>> print(categories[0], ticket_de_caisse[0])
        "Poissonnerie",[12.99, 8.49, 15.89, 3.99, 19.99, 2.59]
    ```


    **Essayer la fonction avec le ticket de caisse suivant :**

    ```python
        categories = ["Poissonnerie","Boucherie-Venaison", "Boulangerie-Pâtisserie", "Épicerie salée", "Épicerie sucrée", "Boissons"]
        ticket_de_caisse = [
                            [12.99, 8.49, 15.89, 3.99, 19.99, 2.59], 
                            [13.49, 6.99, 11.59, 8.79, 14.49, 3.69, 7.99],  
                            [4.59, 5.79, 4.79, 7.49, 6.79, 5.99], 
                            [16.89, 9.49, 12.59, 4.29, 3.89, 15.99],
                            [9.79, 6.39, 13.99, 4.69, 11.99, 8.59],
                            [14.59, 3.79, 10.79, 5.89, 16.49, 7.59, 12.89, 9.39, 8.99]
                        ]
    ```

Maintenant que nous connaissons le prix de chaque catégorie, on a besoin de savoir quels ont été les pôles de dépenses.  
On considère qu'un pôle de dépense est coûteux si elle a coûté plus de 60€.

!!! fox_correction "Participation des invités"

    **Écrire une fonction `poles_couteux` qui prend en paramètre un ticket de caisse (`list[list[float]]`), la liste des catégories (`list[str]`), un seuil (`int`) et renvoie les catégories coûteuses sous la forme d'une liste de tuples (categorie_couteuse, prix_total).**

    *Indication : Cette fonction devra utiliser la fonction précédente.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi que les pôles de dépenses coûteux.**