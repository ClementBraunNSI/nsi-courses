# Traitement de données en tables

## Objectifs

Les dictionnaires de Python permettent de réaliser des traitements sur des données. Ces traitements permettent notamment de trier, organiser, sélectionenr des données en fonction de critères.

Il existe un bon nombre de manières de structurer des données en informatique, celle qui nous sera utile sera permise grâce aux fichiers **CSV**.

Le format CSV (*Comma Separated Values*) correspond à un format où les données sont structurées par des virgules (ou des points-virgules).

Ces formats CSV sont manipulables via des logiciels **tableurs** (Excel, Libre Office etc...) mais on peut également réaliser des traitements sur ces fichiers à l'aide de bibliothèques *Python*.

## La bibliothèque `CSV`

La bibliothèque `csv` permet de charger des fichiers et stocke les données sous forme de listes.

On ne traitera que de la fonction `DictReader` qui permet de traduire chaque ligne de notre fichier CSV dans des dictionnaires, eux mêmes stockés dans une liste.

Voici la structure de l'ouverture d'un fichier CSV et du remplissage d'une liste organisant nos données.

```python
import csv

liste_a_remplir = []
with open('chemin_du_fichier.csv', newline='') as fichier_csv:
   lecteur = csv.DictReader(fichier_csv, delimiter=';')   # Objet DictReader (itérateur)
   for ligne in lecteur:
      liste_a_remplir.append(dict(ligne))
```

### Exemple

Le fichier CSV [commune.csv](./communes.csv) représente l'ensemble des communes de France, associée à leur code postal, département etc...

Pour "ouvrir" ce fichier `csv` et structurer toutes les données le comportant, on utilisera un exemple de code ci-dessus.

On aurait

```python
import csv

def creer_liste_villes(nom_de_fichier : str) -> list:
   villes = []
   with open('communes.csv', newline='') as fichier_csv:
      # Méthode DictReader qui permet de structurer les données contenues dans le fichier CSV en liste de dictionnaires 
      # où chaque descripteur (ou attribut) est renseigné.
      lecteur = csv.DictReader(fichier_csv, delimiter=';')   
      for ligne in lecteur:
         villes.append(dict(ligne))
```

Pour ce fichier CSV, il y a les descripteurs suivant (description exhaustive): `code_commune_INSEE,nom_commune_postal,code_postal,latitude,longitude,code_commune,nom_commune,nom_commune_complet,code_departement,nom_departement,code_region,nom_region`.

```
code_commune_INSEE;nom_commune_postal;code_postal;latitude;longitude;code_commune;nom_commune;nom_departement
01001;L'Abergement-Clémenciat;01400;46.1667;4.9;1;L'Abergement-Clémenciat;Ain
01002;L'Abergement-de-Varey;01640;46.05;5.4833;1;L'Abergement-de-Varey;Ain
...
```
Grâce à tous ces descripteurs, on peut afficher les lignes de nos fichiers CSV suivant différents critères.

*Rappel, la fonction DictReader permet de créer une liste de dictionnaires et chaque dictionnaire correspond à une ligne du fichier CSV à laquelle on associe chacun des attributs à chacune des valeurs de la ligne.*

On appelle **projection** le fait d'obtenir les valeurs de certains ou tous les attributs d'une table / base de données / fichiers CSV.


*Exemple en python*

```python

   # Exemple : Afficher le nom des villes
   for ligne in villes:  # Pour chaque ligne dans la liste des villes
      print(ligne["nom_commune"])  # Affiche la valeur associée à la clé 'nom_commune'

   # Afficher le nom de toutes les villes
   for ligne in villes:
      print(ligne["nom_commune"])

   # Afficher le département de chaque ville
   for ligne in villes:
      print("La ville ", ligne["nom_commune"], " est dans le département : ", ligne["nom_departement"])
```

Cela permet donc d'obtenir dans notre exemple de villes, le nom de celle-ci, le département etc... de toutes les villes **sans aucune contrainte**.

___

On appelle **sélection** le fait de sélectionner des valeurs suivant certains critères ou condition.

Cela permet donc d'obtenir des informations ou de réaliser des traitements sur les données d'un fichier suivant divers critères (par exemple sur les villes).

```python
   
   # Afficher le nom des villes qui sont dans le département 59
   for ligne in villes:
      if ligne['code_departement'] == '59':
         print(ligne["nom_commune"])

   # Afficher les noms des villes commençant par la lettre C

   for ligne in villes:
      if ligne["nom_commune"][0] == "C":
         print(ligne["nom_commune"])
```


### Exercice : 

1. Afficher toutes les communes du département 62.
2. Afficher toutes les communes ayant plus de 34000 habitants.
3. Afficher toutes les communes ayant un nom commençant par la lettre C.
4. Afficher toutes les communes ayant un nom commençant par la lettre V et qui ont plus de 35000 habitants.
5. Afficher toutes les communes du département `Morbihan`.
