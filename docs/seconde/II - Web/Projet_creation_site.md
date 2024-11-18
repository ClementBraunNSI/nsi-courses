# Projet : Création du Bestiaire

Pour la création du bestiaire, téléchargez l'archive correspondante en cliquant sur le lien hypertexte suivant : [maquette_vide](./projet_site_eleve.zip).

Vous retrouverez : 

- un fichier `index.html` qui correspond au site web à remplir.
- un dossier `image` qui contiendra l'image de votre monstre.
- un dossier `style` qui contiendra tous les éléments de style de votre page.

## Partie 1 : Remplir le site comme la maquette

Voici ce que vous devez reproduire lors de la première séance: 

![a_reproduire](./a_reproduire.png)

Chacun des blocs de couleur correspond à une partie bien précise du site.
On les nomme `div` pour division d'une page web. Ils permettent de scinder la page en diverses parties.

Le site est aussi régi par une feuille de style qui n'est pas à modifier pour cette première étape.

![base](./base.png)

À cause d'un soucis d'affichage, le Nom du monstre correspond au bloc violet.

Vous allez devoir pour cette première partie : 

**Modifier le Nom du monstre pour qu'il corresponde à un titre de niveau 1.**

**Dans le bloc bleu : Ajouter un paragraphe expliquant la rivalité/l'amitié entre votre monstre/personnage et ses rivaux/amis.**

**Dans le bloc turquoise : Ajouter chacune des localisations où l'on peut retrouver votre monstre (Conservez la liste si vous souhaitez une liste, sinon supprimez la et écrivez un paragraphe).**

**Dans le bloc turquoise : Ajouter une liste à puce correspondant à ses statistiques si l'on souhaite transformer ce bestiaire en un jeu de rôle sinon une histoire par rapport à son lieu d'habitat.**

**Ajouter dans le bloc contenant la description et l'histoire de son monstre, un petit titre de niveau 3 permettant de structurer la page et un paragraphe expliquant l'histoire du monstre/personnage.**

Par la suite, on ajoutera les images des rivaux/personnages (quand votre monstre est disponible [ici](./monstres.md)).

**Ajouter à la place de `image du monstre` l'image du monstre associée.**

Pour se faire, vous rajouterez la balise suivante :  

```html
    <img class = "image_principale" align="left" height="400px" width="400px" src="image/votre_prenom.jpg" alt="nom_du_monstre"/>
```

**Ajouter l'image du rival avec la balise suivante.**

```html
    <img class = "image_rival" width="30%"  src="image/rival2.jpg" alt="Rival 2"/>
```

## Partie 2 : Style du site

Le fichier CSS correspondant à toutes les propriétés de style est déjà fourni pour aligner les éléments au bon endroit.

On peut associer une **classe** à chacun des attributs que l'on écrit dans un fichier HTML (une division, une image, une liste etc...).

En analysant le fichier de la partie 2 à trouver ([partie 2](./index_partie_2.html)), **ajouter chacune des classes aux balises que vous avez créées.**

Ce fichier de partie 2 correspond aussi à une correction de la partie 1.

Si tout est bien réalisé, que toutes les balises sont bien ajoutées et que tous les styles sont bien ajoutés : 

Vous devrez avoir cet affichage pour le site.

![final](./presque_fini.png)

## Partie 3 : Modifications finales

La dernière étape de ce projet correspond au fait de retirer chacune des bordures.
Elles sont dans le fichier `style.css` dans chacune des classe. Retirer tous les attributs en rapport à la bordure (indice : `border`).

En vous renseignant sur internet :

- **Ajouter dans la classe container l'instruction qui modifie l'image de fond. Celle-ci est stockée dans le dossier `image` avec pour nom `background.png`**  
- **Modifier le fichier de style pour avoir les couleurs de texte correspondant à la maquette.**  

Vous devez avoir ainsi :

![fini](./final.png)