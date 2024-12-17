# Jour 3 🦊❄️🎉 : Pas de bol, il manque des chips

L'organisateur de la soirée, Jean, se rend compte qu'il n'y aura pas assez de chips pour tout le monde malgré sa liste de courses bien détaillée.

Il se rend donc dans son supermarché préféré *Intramarché*, pour acheter ses paquets de chips. Cependant, il se dit qu'importe la marque et le goût, il doit acheter le plus de chips possibles pour satisfaire tous les convives.

Il se rend donc dans le rayon et se rend compte qu'il y a beaucoup de chips, plus qu'il n'a jamais vu auparavant.

Il se demande donc quel paquet de chips prendre car il a un budget de 25€.

## Informations nécessaires

On considère un **paquet de chips** comme étant un **tuple** tel que : paquet_de_chips = (marque, poids, prix).
Il existe plusieurs manières de choisir quelles chips prendre et on s'interessera à un choix particulier : le prix minimum.

## Exercice Principal

On aimerait savoir combien de paquet de chips, Jean, peut acheter.

Un paquet de chips est de la forme

```python
    ticket_de_caisse = (marque, poids, prix)

    #Exemple
    paquet_chips_1 = ("Vica", 0.150, 1.99)
    paquet_chips_2 = ("Leys", 0.200, 2.49)
```

!!! fox_correction "Quel paquet de chips prendre?"

    **Écrire une fonction `paquet_de_prix_minimal` qui prend en paramètre un paquet de chips et renvoie le nom du paquet de chips le moins cher.**

    *Rappel :* 
    Un paquet de chips est de la forme

    ```python
        ticket_de_caisse = (marque, poids, prix)

        #Exemple
        paquet_chips_1 = ("Vica", 0.150, 1.99)
        paquet_chips_2 = ("Leys", 0.200, 2.49)
    ```


    **Essayer la fonction avec les paquets de chips suivants :**

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

    **Écrire une fonction `nombre_paquets_chips` qui prend en paramètre un paquet de chips (`tuple(str,float,float)`) et un budget (`int`) et renvoie combien de paquet de chips on peut acheter avec le budget passé en paramètre.**


**Pour valider cet exercice, vous devrez rendre à votre enseignant les fonctions construites ainsi que le nombre de paquet de chips possible d'acheter.**