# Stéganographie : l'art de cacher des messages

Vous êtes missionnés par le gouvernement pour passer des tests pour devenir membre du service secret.
Pour se faire, une des missions qui vous est attribuée est de faire passer des messages à un destinataire qui n'a pas accès aux ressources des services secrets.

Comme votre destinataire n'a pas les machines ou services chiffrés et sécurisés de votre services, vous devez réaliser ces transferts d'informations par mail interposés.

Il n'est pas forcément secret de transferer des informations dans le corps d'un mail, donc on vous propose une idée, la **stéganographie**.

La **stéganographie** est l'art de dissimuler des messages par diverses techniques dans d'autres contenus.
Ici, vous devrez *cacher une image dans une autre image*.

## Pré-requis

Avant de réaliser la stéganographie, il faut réaliser quelques rappels.

Une image est une matrice (un tableau à deux dimensions) de pixels. Ces pixels contiennent une information capitale : la valeur de sa couleur, suivant le mode choisi.

Pour des questions de simplicité, on traitera des images en noir et blanc dans ce projet.

### Binaire

On rappelle qu'un pixel contient une valeur mais celle-ci est en binaire et codée sur 1 octet (soient 8 bits).
Cela signifie que l'on doit traiter de valeurs binaire et non en base 10.

Les 4 bits à gauche d'un octet sont appelés **bits de poids fort** tandis que les bits 4 situés à droite sont appelés **bits de poids faible**.
Par exemple pour l'octet $1111 0000_{2}:$

$\underbrace{1111}_{\texttt{bits de poids fort}}\overbrace{0000}^{\texttt{bits de poids faible}}$

### Module Pillow

Pour le traitement des images, on utilise le module *Pillow* de Python qui permet de modifier les valeurs de bits, créer de nouvelles images avec des tailles prédéfinies, dans des modes prédéfinis (RGB, Noir et Blanc, Nuances de gris).

On peut retrouver un tutoriel dans le [cours de seconde](../../seconde/Photographie%20Numérique/c_2_Photographie_Couleur.md).

### Méthode Bin et Int de Python

La méthode `bin` permet de retourner la représentation binaire d'un nombre entier sous chaine de caractère.

!!! Danger
    La méthode bin renverra la représentation de cette forme "**0b**101110".
    Il faudra bien retirer **"0b"** pour convertir en base 10 à la suite.

La méthode `int` permet de convertir une variable en type int. Petite aide pour la suite, on peut convertir une représentation en base 2 en base 10 avec la sytaxe : 

```python
    >>>repr_binaire = "01001110"
    >>>print(repr_binaire)
        "01001110"
    >>>print(int(repr_binaire))
        01001110
    >>>print(int(repr_binaire,2))
        78
```
