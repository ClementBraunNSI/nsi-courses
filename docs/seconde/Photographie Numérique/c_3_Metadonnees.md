# Photographie Numérique 3 : Extension, Format, Traitement et Métadonnées

## Extension et format d'une image

Une image comme tout fichier possède une **extension**.

**Définitions:**

Une extension est une **suite de caractère précédée d’un point**. Elle permet de retrouver quel est le format d’un fichier et d’associer une application à un type de fichier.

Le **format d’un fichier** quant à lui correspond à la **manière d’encoder les bits de la donnée** pour les lire.
On retrouve divers formats d’image qui ont leur propre caractéristiques.
Grâce à la vidéo *taille*, *poids* et *format* d’images de DLT (Digital Learning Tribe), relier le format à sa bonne définition.

![relier](exo_relier.png)

*Indiquer quel est l’utilisation principale de chaque format d’image :*

- Le JPEG est populaire sur les sites internet et sur les réseaux sociaux.
- Le PNG sert notamment à réaliser des logos pour les entreprises ou des illustrations grâce à la transparence.
- Le GIF permet de créer des images avec peu de couleurs ou animées.

## Traitement et Algorithmes

### Traitement sur des images : Conversion nuances de gris et Négatifs

On peut réaliser un bon nombre de traitements sur les images.
Par exemple, la conversion d’une image couleur en image en niveaux de gris permet de bien définir les zones d’ombres ou par exemple de calibrer les appareils photos.
Il existe 3 manières pour convertir une image couleur vers nuances de gris :

**Méthode de la moyenne :**
On réalise la moyenne des composantes de chaque pixels. Cette moyenne correspondra à la valeur de la nuance de gris du pixel.

**Méthode de la couleur vraie :**
Cette méthode prend en compte la vision humaine et sa perception des couleurs. Il a été défini des coefficients pour chaque valeur de pixel.
$I_{pixel} = 0,2126*V_{rouge} + 0,7152*V_{vert} + 0,0722*V_{bleu}$

**Méthode rapide :**
Cette méthode utilise la proportion de vert pour donner la nuance de gris correspondante. Cette méthode permet d’approximer la nuance car l’oeil est beaucoup plus sensible au vert qu’aux autres couleurs.

On utilisera la photo de Maya comme exemple:

![mayagris](maya_gris.png)

On remarque que les différences sont infimes entre les trois modèles mais qu’ils mettent bien en avant les zones de contraste, d’ombre et de lumière de l’image.

Grâce aux valeurs de chaque composantes de pixels, on peut donner le négatif d’une image.
L’inverse d’une composante de couleur se calcule de cette manière :
$\texttt{Inverse couleur} = 255 -\texttt{Valeur de la couleur}$.

![mayainv](mayainv.png)

En inversant chaque composante de chaque pixels, on retrouve l’inverse d’une image.
Ce procédé a été utilisé notamment à l’invention des photos car le négatif des images se retrouvait sur les bandes magnétiques qui recevaient la lumière.
En inversant les négatifs, on retrouvait les images normales.

### Algorithmes de prise de vue (mise au point, stabilisation)

Il existe divers algorithmes qui opèrent de la prise de l’image au traitement de celle-ci.
Les **algorithmes de prise de vue** opèrent à la prise de la photo. Il existe l’a**lgorithme de stabilisation** qui compense le mouvement du photographe et évite le **flou de bougé**.

![stab](stab.png)

L’**algorithme de mise au point** permet d’adapter la distance de la lentille par rapport au capteur pour adapter la **netteté** ou **se mettre au point** sur un objet particulier.

![map](map.png)

### Métadonnées EXIF

Les métadonnées sont des données qui fournissent des informations sur d’autres données.
Pour des images, les métadonnées permettent de tracer une image et aider à leur traitement.
Ces informations sont au standard EXIF et sont produites lors de la prise de vue.

Elles permettent de retrouver par exemple : 

- Les coordonnées GPS du lieu de la prise, le lieu en lui même s’il est connu, la date de prise de vue
  
- Les données techniques : le poids de l’image, la résolution, les dimensions
  
- Les paramètres et configuration de l’appareil : référence et marque de l’appareil, l’ouverture, la distance focale, la sensibilité.
  
- Les données du photographe : le nom, prénom, le nom de la photo, le droit d’usage etc.

Ces données sont accessibles facilement, par exemple sur la photo de Maya :

![exif](exif.png)