# 📊 Données Structurées

La nécessité d'organiser et de structurer les données remonte aux premiers systèmes informatiques des années 1960. À l'époque, les chercheurs avaient besoin de stocker et de traiter de grandes quantités d'informations de manière efficace, notamment pour les bases de données scientifiques et les systèmes de gestion.

**Le premier objectif était de créer des formats standardisés pour que les machines puissent comprendre et traiter l'information automatiquement.**

C'est dans les années 1970 qu'Edgar F. Codd, un informaticien d'IBM, a révolutionné le domaine en proposant le modèle relationnel pour les bases de données. Ce modèle est devenu la base de la plupart des systèmes de gestion de bases de données modernes.

**Les premières bases de données relationnelles ont vu le jour dans les années 1980.**

<!-- image removed: data_evolution -->

À la suite de cela, dans les années 1990-2000, de nouveaux formats d'échange de données ont émergé avec l'essor d'Internet.
On appelle ces formats des **standards d'échange** car ils permettent à différents systèmes de communiquer.

La manière de structurer les données est organisée selon différents niveaux de complexité.
Ces niveaux correspondent à différents besoins : du simple tableau (CSV) aux structures complexes (JSON, XML).
Dans les années 2000, le format **JSON** a révolutionné l'échange de données sur le web.
Il a été adopté massivement à partir de 2005 pour sa simplicité et sa lisibilité.
Les années 2010 ont vu l'explosion du **Big Data** et des nouvelles approches de stockage de données.

Depuis, les données structurées permettent de gérer des milliards d'informations pour alimenter des applications, des sites web ou des systèmes d'intelligence artificielle.
Par exemple, il existe des formats pour les données tabulaires (CSV), les données hiérarchiques (JSON) ou les documents structurés (XML).

<!-- image removed: data_formats -->

En clair, **les données structurées sont des informations organisées selon des règles précises qui permettent leur traitement automatique par les machines.**

## Définitions

**Une donnée structurée** est une information organisée selon un format prédéfini qui facilite son stockage, sa recherche et son traitement automatique par les machines.
**On retrouve différents types de structures de données qui ont chacune leur propre usage.**

### Les formats de données structurées

Pour qu'un système de données fonctionne, il faut des formats standardisés pour organiser l'information.

**On retrouve :**

| Format | Rôle | Exemple d'usage |
|----------|-------------------------------|-----------------------|
| CSV | Format tabulaire simple pour données en lignes/colonnes | Tableurs, exports de bases de données |
| JSON   | Format hiérarchique pour structures complexes                   | APIs web, configuration d'applications                    |
|XML  | Format de balisage pour documents structurés | Documents officiels, échange entre systèmes    |
| SQL | Langage pour interroger les bases de données relationnelles| Requêtes de bases de données, rapports|

On a défini dans les rôles différents types de structures.
On peut les regrouper en 2 catégories :

- **Données tabulaires** : données organisées en lignes et colonnes (comme un tableau).
- **Données hiérarchiques** : données organisées en arbre avec des niveaux de profondeur.


!!!danger
    On dispose de formats, de structures mais, comment les machines comprennent-elles ces données? Quelles règles sont utilisées?

### Le format CSV pour les données tabulaires

Une donnée tabulaire dispose d'une structure en **lignes et colonnes**. Cette structure permet d'organiser l'information de manière simple et lisible.

Le format CSV utilise des **séparateurs** (généralement des virgules) pour délimiter les colonnes.  
Cette organisation peut aussi être appelée **format délimité** car elle utilise des caractères spéciaux pour séparer les données.  
Ce format est composé d'une ligne d'en-tête suivie des données. 

Exemple : `Nom,Espece,Habitat,Poids`.

**Exemple : Base de données sur les renards**

```csv
Nom,Espece,Habitat,Poids_kg,Longueur_cm
Rusty,Vulpes vulpes,Forêt tempérée,6.5,58
Arctic,Vulpes lagopus,Toundra arctique,3.2,46
Fennec,Vulpes zerda,Désert,1.5,24
Silver,Vulpes vulpes,Forêt boréale,7.1,61
```

### Le format JSON pour les données hiérarchiques

Chaque donnée complexe doit pouvoir être représentée avec ses relations internes.
Sur le web, on utilise ce que l'on appelle **le format JSON** (pour JavaScript Object Notation).  
**Un objet JSON est constitué de paires clé-valeur organisées de manière hiérarchique.**  
Le JSON correspond à une représentation textuelle lisible par l'humain mais aussi par l'ordinateur.  
**Par exemple : {"nom": "Rusty", "poids": 6.5} est un objet JSON simple.**  
Il faut pouvoir représenter ces données de manière **structurée** et **imbriquée**.  
L'objet JSON est constitué de plusieurs types de données :  

**Les types simples : ils permettent de stocker une valeur unique.**  
**Les types complexes : ils permettent de stocker plusieurs valeurs ou d'autres objets.**

Pour organiser ces données, on utilise ce que l'on appelle une **hiérarchie**.  
Elle permet de définir des niveaux de profondeur dans les données. On peut représenter cette hiérarchie de diverses manières.

Exemple :

On dispose de l'objet **renard** qui contient des **caractéristiques** et un **habitat**.

Cela correspond à une structure où l'objet principal contient d'autres objets.  
Ce qui veut dire que l'objet renard est le **parent** et les caractéristiques sont les **enfants**.  

On peut donc définir que l'objet renard contient les propriétés nom, espèce et des sous-objets caractéristiques et habitat.

!!! Warning

    La structure hiérarchique est très importante car elle permet de représenter des relations complexes entre les données.

**Exemple : Fiche détaillée d'un renard**

```json
{
  "renard": {
    "nom": "Rusty",
    "espece": "Vulpes vulpes",
    "caracteristiques": {
      "poids": 6.5,
      "longueur": 58,
      "couleur": "roux",
      "age": 3
    },
    "habitat": {
      "type": "Forêt tempérée",
      "region": "Europe",
      "coordonnees": {
        "latitude": 48.8566,
        "longitude": 2.3522
      }
    },
    "alimentation": ["rongeurs", "oiseaux", "insectes", "fruits"]
  }
}
```

On sait comment les données sont organisées dans les formats simples (CSV, JSON) mais on veut savoir surtout comment stocker et interroger de grandes quantités de données de manière efficace.
Pour gérer des volumes importants, on ne peut pas se contenter de fichiers simples. En effet, les données sont trop nombreuses pour être traitées d'un coup, il faut les organiser. On appelle **base de données** un système organisé pour stocker, gérer et interroger de grandes quantités d'informations.

Le modèle relationnel permet la gestion et l'interrogation de données structurées entre plusieurs **tables** liées entre elles.
Ce modèle est composé de plusieurs concepts :

- Le concept de **table** permet l'organisation des données en lignes et colonnes. 
  Il permet d'être sûr qu'une donnée est stockée de manière cohérente à l'aide de **contraintes**.

- Le concept de **relation** qui permet de lier les tables entre elles à l'aide de **clés**.

Le modèle relationnel fonctionne en plusieurs étapes :

  1. Les données sont organisées en tables avec des colonnes typées et des lignes d'enregistrements.
  2. Les tables sont liées entre elles par des relations (clés étrangères).
  3. Les données sont interrogées à l'aide du langage SQL.
  4. Enfin, un contrôle est réalisé par le système pour s'assurer que les données respectent les **contraintes**, c'est à dire que les données sont cohérentes.
  Si les données ne respectent pas les contraintes, le système refuse l'opération.

### Concept de table

Une **table** est une structure de données organisée en lignes (enregistrements) et colonnes (champs).

**Exemple : Table "Renards"**

| ID | Nom | Espèce | Habitat | Poids (kg) | Région |
|----|-----|--------|---------|------------|--------|
| 1 | Rusty | Vulpes vulpes | Forêt | 6.5 | Europe |
| 2 | Arctic | Vulpes lagopus | Toundra | 3.2 | Arctique |
| 3 | Fennec | Vulpes zerda | Désert | 1.5 | Afrique |
| 4 | Silver | Vulpes vulpes | Forêt | 7.1 | Amérique |
