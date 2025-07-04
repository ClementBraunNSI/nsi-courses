# Jour 4 🦊❄️🎉 : une soirée de gloutons de chips

Jean, avec son précédent calcul s'est rendu compte qu'il n'avait peut-être pas fait le bon choix car à prendre les chips les moins chères, il a omis une information capitale quand on fait ses courses : **Le prix au kilo**.
En prenant les chips les moins chères, il se rend compte qu'elles n'ont pas le prix au kilo le moins cher. Par conséquent, celles-ci ne sont pas les plus optimales à acheter pour en avoir le plus gros volume.

## Informations nécessaires

On considère un **paquet de chips** comme étant un **tuple** tel que : paquet_de_chips = (marque, poids, prix).
On prendra compte de la méthode suivante : pour chercher le nombre optimal de paquet de chips, on considère le prix au kilo.

## Exercice Principal

On aimerait savoir combien de paquet de chips, Jean, peut acheter.

Un paquet de chips est de la forme :

```python
    ticket_de_caisse = (marque, poids, prix)

    #Exemple
    paquet_chips_1 = ("Vica", 0.150, 1.99)
    paquet_chips_2 = ("Leys", 0.200, 2.49)
```

On considère les paquets de chips suivants :

```python
paquet_chips_1 = ("Chipeur", 0.150, 1.99)
paquet_chips_2 = ("Frites et Cie", 0.200, 2.49)
paquet_chips_3 = ("Pipoles", 0.200, 2.79)
paquet_chips_4 = ("Tay's", 0.300, 3.19)
paquet_chips_5 = ("Bonne Patate", 0.125, 1.69)
paquet_chips_6 = ("Cuisto's", 0.100, 1.49)
paquet_chips_7 = ("Mik'O Chips", 0.250, 2.59)
        
paquets_de_chips = [paquet_chips_1, paquet_chips_2, paquet_chips_3, paquet_chips_4, paquet_chips_5, paquet_chips_6, paquet_chips_7]
```

!!! fox_correction "Prix au kilo"

    On va chercher à calculer le prix au kilo pour chacun des paquets de chips.

    Comme un tuple est **non mutable**, c'est à dire qu'on ne peut en modifier le contenu, on va recréer une liste de tuples avec les bonnes informations.

    Au retour de cette fonction, un paquet de chips sera une **liste** de 4 éléments : `paquet_chips_1 = ["Chipeur", 0.150, 1.99, 13.27]`.

    **Écrire une fonction `prix_kilo` qui prend en paramètre une liste de paquets de chips et renvoie une nouvelle liste contenant des paquets de chips associés à leur prix au kilo.**

!!! fox_correction "Paquet ayant le prix au kilo le plus petit"

    Maintenant que nous connaissons le prix au kilo de tous les paquets de chips, on va chercher à savoir quel paquet à le prix au kilo le plus petit.

    **Écrire une fonction `paquet_prix_kilo_min` qui prend en paramètre une liste de paquets de chips et renvoie le paquet avec le prix au kilo minimum.**

    *Indication : Cette fonction utilisera la fonction précédente.*

!!! fox_correction "Combien de paquet peut-on acheter?"

    On sait maintenant grâce à la fonction précédente quel paquet de chips a le coût au kilo le plus faible. On va donc chercher à savoir combien de paquet on peut acheter et combien en poids cela correspond.

    **Écrire une fonction `paquets_budget` qui prend en paramètre une liste de paquets de chips et un budget à ne pas dépasser (int) et renvoie le nombre de paquets de chips possible d'acheter et la masse totale de chips obtenue.**

    *Indication : Cette fonction utilisera la fonction précédente.*

    ```python
    #Rappel : lorsqu'une fonction renvoie plusieurs valeurs, elle renvoie un tuple de ces plusieurs valeurs.

    def ma_super_fonction(param1:type,; param2:type)->tuple:
        var1 = x
        var2 = y

        return var1, var2
    ```
    
**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi que le nombre de paquet de chips possible d'acheter ainsi que la masse totale de chips obtenue.**
