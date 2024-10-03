# Traitement de données en tables

## Objectifs

Les dictionnaires de Python permettent de réaliser des traitements sur des données. Ces traitements permettent notamment de trier, organiser, sélectionenr des données en fonction de critères.

Il existe un bon nombre de manières de structurer des données en informatique, celle qui nous sera utile sera permise grâce aux fichiers **CSV**.

Le format CSV (*Comma Separated Values*) correspond à un format où les données sont structurées par des virgules (ou des points-virgules).

Ces formats CSV sont manipulables via des logiciels **tableurs** (Excel, Libre Office etc...) mais on peut également réaliser des traitements sur ces fichiers à l'aide de bibliothèques *Python*.

## La bibliothèque `CSV`

La bibliothèque `csv` permet de charger des fichiers et stocke les données sous forme de listes.

On ne traitera que de la fonction `DictReader` qui permet de traduire chaque ligne de notre fichier CSV dans des listes, eux mêmes stockés dans une liste.

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


