# Fiche de Cours : Introduction à la Programmation Orientée Objet (POO) en C#

## 1. Qu'est-ce que la Programmation Orientée Objet ?

La Programmation Orientée Objet (POO) est une manière de concevoir et d'écrire des programmes informatiques. Au lieu de penser uniquement en termes de fonctions et de procédures, on pense en termes d'**objets**.

Un **objet** est une entité qui possède des **attributs** (des données qui le caractérisent, aussi appelés propriétés ou champs) et des **méthodes** (des actions qu'il peut effectuer).

## 2. Les Classes : Modèles pour les Objets

En POO, on utilise des **classes** pour créer des objets. Une classe est comme un plan ou un moule qui définit comment les objets de ce type seront structurés et comment ils se comporteront.

### Exemple : La classe `Voiture`

Regardons un exemple concret avec une classe `Voiture` en C#.

```csharp
using System;

public class Voiture
{
    // Attributs (Propriétés)
    // "get; set;" permet de lire et modifier la valeur facilement
    public string Immatriculation { get; set; }
    public string Marque { get; set; }
    public string Modele { get; set; }
    public int Annee { get; set; }
    public string Couleur { get; set; }
    public bool EstDemarre { get; private set; } // Modifiable uniquement par la classe elle-même

    // Constructeur : Méthode spéciale appelée à la création de l'objet (new Voiture(...))
    public Voiture(string immatriculation, string marque, string modele, int annee, string couleur)
    {
        Immatriculation = immatriculation;
        Marque = marque;
        Modele = modele;
        Annee = annee;
        Couleur = couleur;
        EstDemarre = false; // Par défaut, une voiture est arrêtée
    }

    // Méthode pour afficher les informations
    public override string ToString()
    {
        return $"Voiture {Immatriculation} de marque {Marque} et de modèle {Modele}.";
    }

    // Méthode pour démarrer la voiture
    public void Demarrer()
    {
        EstDemarre = true;
        Console.WriteLine($"La voiture {Immatriculation} démarre.");
    }

    // Méthode pour arrêter la voiture
    public void Arreter()
    {
        EstDemarre = false;
        Console.WriteLine($"La voiture {Immatriculation} s'arrête.");
    }
}
```

**Explications :**

*   **`public class Voiture`** : Définit une nouvelle classe nommée `Voiture`. Le mot-clé `public` signifie qu'elle est accessible partout.
*   **Propriétés (`Immatriculation`, `Marque`, etc.)** : Ce sont les caractéristiques de la voiture. En C#, on utilise souvent des **Propriétés** (`{ get; set; }`) plutôt que de simples variables publiques.
*   **`public Voiture(...)`** : C'est le **constructeur**. Il porte le même nom que la classe. Il est appelé quand on crée une nouvelle instance avec `new`.
*   **`public override string ToString()`** : C'est une **méthode spéciale** héritée de la classe de base `Object`. Elle permet de définir comment l'objet est représenté sous forme de texte (équivalent du `__str__` en Python).
*   **`Demarrer()` et `Arreter()`** : Ce sont des **méthodes** (des actions). Elles modifient l'état de l'objet (ici `EstDemarre`) et peuvent afficher des messages.

### Zoom sur `{ get; set; }` (Les Propriétés)

Cette syntaxe est une spécificité très pratique du C#.
*   **`get`** (getter) : Autorise la **lecture** de la valeur.
*   **`set`** (setter) : Autorise l'**écriture** (modification) de la valeur.
*   En écrivant `{ get; set; }`, on demande à C# de gérer automatiquement le stockage de la variable en arrière-plan.
*   On peut restreindre l'accès : `public bool EstDemarre { get; private set; }` signifie "tout le monde peut lire l'état (`get` public), mais seule la classe peut le modifier (`set` private)".

### Et si on veut contrôler la valeur ? (Full Properties)

C'est la seule raison d'écrire les `get` et `set` soi-même : pour ajouter de la **logique** (validation, calculs).

Imaginons qu'on veuille empêcher une vitesse négative :

```csharp
private int _vitesse; // Variable privée (cachette)

public int Vitesse
{
    get { return _vitesse; } // Lecture simple
    set 
    {
        // Le mot-clé "value" contient la valeur qu'on essaie d'assigner
        if (value < 0) 
        {
            Console.WriteLine("Impossible d'avoir une vitesse négative !");
            _vitesse = 0;
        }
        else 
        {
            _vitesse = value;
        }
    }
}
```

## 3. Créer et Utiliser des Objets (Instances)

Une fois la classe définie, on peut créer des **instances** (des objets spécifiques) de cette classe dans le programme principal (méthode `Main`).

```csharp
public class Program
{
    public static void Main()
    {
        // Création d'objets (instances) de la classe Voiture
        Voiture maPremiereVoiture = new Voiture("AB-123-CD", "BMW", "X1", 2017, "noir");
        Voiture uneAutreVoiture = new Voiture("XY-789-ZW", "Audi", "RS3", 2025, "gris nardo");

        // Accéder aux propriétés
        Console.WriteLine($"La couleur de ma première voiture est : {maPremiereVoiture.Couleur}"); // Affiche: bleu
        Console.WriteLine($"L'année de l'autre voiture est : {uneAutreVoiture.Annee}"); // Affiche: 2022

        // Utiliser les méthodes
        Console.WriteLine(maPremiereVoiture); // Appelle automatiquement ToString()
        
        maPremiereVoiture.Demarrer(); // Affiche: La voiture AB-123-CD démarre.
        Console.WriteLine($"Ma voiture bleue est démarrée : {maPremiereVoiture.EstDemarre}"); // Affiche: True

        uneAutreVoiture.Arreter(); 
        Console.WriteLine($"L'autre voiture est démarrée : {uneAutreVoiture.EstDemarre}"); // Affiche: False
    }
}
```

## 4. L'Héritage : Aller plus loin

L'un des piliers de la POO est l'**Héritage**. Il permet de créer de nouvelles classes basées sur des classes existantes. Cela évite de répéter du code et permet de créer des hiérarchies logiques.

Imaginez que nous voulions aussi représenter des **Motos**. Une moto est aussi un véhicule, comme une voiture. Elle a une marque, une couleur, elle peut démarrer...

Au lieu de tout réécrire, on peut créer une classe générale `Vehicule` (classe mère) et faire en sorte que `Voiture` et `Moto` (classes filles) en héritent.

```csharp
// Classe Mère (ou Base)
public class Vehicule
{
    public string Marque { get; set; }
    public string Couleur { get; set; }

    public Vehicule(string marque, string couleur)
    {
        Marque = marque;
        Couleur = couleur;
    }

    public void Klaxonner()
    {
        Console.WriteLine("Tut tut !");
    }
}

// Classe Fille (ou Dérivée) : Voiture hérite de Vehicule
public class Voiture : Vehicule
{
    public int NombrePortes { get; set; }

    // Le constructeur appelle celui de la classe mère avec "base"
    public Voiture(string marque, string couleur, int nombrePortes) : base(marque, couleur)
    {
        NombrePortes = nombrePortes;
    }
}

// Classe Fille (ou Dérivée) : Moto hérite de Vehicule
public class Moto : Vehicule
{
    // Propriété auto-implémentée : C# crée automatiquement le stockage en mémoire.
    // "get" permet de lire la valeur (ex: if (moto.ATopCase)...)
    // "set" permet de la modifier (ex: moto.ATopCase = true;)
    public bool ATopCase { get; set; }

    public Moto(string marque, string couleur, bool aTopCase) : base(marque, couleur)
    {
        ATopCase = aTopCase;
    }
}
```

**Ce qu'il faut retenir :**
*   `Voiture` et `Moto` possèdent automatiquement les propriétés `Marque` et `Couleur` ainsi que la méthode `Klaxonner()` sans qu'on ait besoin de les réécrire.
*   On peut ajouter des spécificités (`NombrePortes` pour `Voiture`, `ATopCase` pour `Moto`).
