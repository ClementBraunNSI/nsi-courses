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

On peut retrouver un tutoriel dans le [cours de seconde](../seconde/Photographie%20Numérique/c_2_Photographie_Couleur.md).

### Méthode Bin et Int de Python

La méthode `bin` permet de retourner la représentation binaire d'un nombre entier sous chaine de caractère.

!!! Danger
    La méthode bin renverra la représentation de cette forme "**0b**101110".
    Il faudra bien retirer **"0b"** pour convertir en base 10 à la suite.

La méthode `int` permet de convertir une variable en type int. Petite aide pour la suite, on peut convertir une représentation en base 2 en base 10 avec la sytaxe : 

```{.python}
    >>>repr_binaire = "01001110"
    >>>print(repr_binaire)
        "01001110"
    >>>print(int(repr_binaire))
        01001110
    >>>print(int(repr_binaire,2))
        78
```

## Méthode

Pour réaliser "cacher" le message codé dans une image, il faut pouvoir modifier l'image qui servira de contenant sans que cela se remarque.
Chaque pixel a une valeur codée sur 8 bits et les bits de poids fort permettent de faire varier la valeur du pixel de 16 à 255.
Cela veut dire que les bits de poids faible n'ont que peu d'impact sur la représentation de la couleur.

La méthode à employer consistera à remplacer les bits de poids faible de la représentation de chaque pixel par les bits de poids fort de l'image à cacher. Cela n'impactera peu la couleur du pixel et permettra de dissimuler le message à transmettre.

En clair :
$$
\texttt{pixel de l'image de transport} : \textbf{1100}~1100 \newline
\texttt{pixel de l'image à cacher} : \textbf{0110}~0010 \newline
\texttt{pixel de l'image finale} : \textbf{1100~0110}
$$

!!! Warning Important
    Pour que l'opération fonctionne correctement, il faut utiliser des images de départ en format **non compressé**.
    Utiliser des formats compressés comme le PNG, le JPEG peut poser des problèmes lors de l'opération de chiffrement.
    *On utilisera le format pgm qui est non compressé.*


## À réaliser

On doit manipuler la représentation binaire de nombres.  

### Fonction de représentation des bits d'un pixel

Implanter une fonction `representation_binaire` qui prend en paramètre un entier et renvoie sa représentation binaire en chaine de caractère. 
**Cette fonction prendra soin de rajouter des 0 au début de la représentation si celle-ci n'est pas déjà sur 8 bits.**

!!! tip Astuce
    * Vous pouvez utiliser la méthode `bin` qui donne la représentation en chaine de caractère sous forme "**0b**abcd" avec a,b,c et d des bits.  
    * Pour retrancher les deux caractères **0b**, la syntaxe permet d'avoir une chaîne de caractère omettant les 2 premiers caractères.
    ``` python 
        chainte_caractère = "0b1010"
        chaine_finale = chaine_caractere[2:]
        >>>print(chaine_finale)
        "1010"
    ``` 
    
### Chiffrage d'une image dans une autre

Compléter la fonction suivante `chiffrer_image` qui prend en paramètre 2 images du module PIL et renvoie une nouvelle image qui cache l'une des deux dans l'autre.

```python
def chiffrer_image(img1, img2):
    """
    params : 
    img1 : image du module PIL
    img2 : image du module PIL
    returns :
    image_chiffree : image du module PIL

    Chiffre une image de transport avec une image à transmettre de manière cachée.
    """
    largeur, hauteur = img1.size
    image_chiffree = Image.new("L", (largeur, hauteur))
    for i in range(...):
        for j in range(...):
            pixel_img1 = img1.getpixel((i,j))
            pixel_img2 = img2.getpixel((i,j))
            ...
            ...
            image_chiffree.putpixel((i,j), ... )
    return image_chiffree
```

### Déchiffrage d'une image chiffrée pour récupérer le message.

Pour déchiffrer l'image et récupérer le message, il suffit de retrouver les bits de poids faible de l'image chiffrée pour composer un octet contenant ces bits de poids faible et 4 zéros.

Implanter une fonction `dechiffre_image` qui prend en paramètre une image `img` du module PIL et renvoie une image qui affichera celle qui est cachée.

Vous utiliserez la même structure de fonction que pour la fonction `chiffrer_image`.

### Qui est le coupable?

Vous avez été missionné pour chercher qui a volé le stock de croquette du magasin à côté du lycée.

Une image du ou de la coupable est chiffrée dans l'image `image_chiffree.pgm`.
