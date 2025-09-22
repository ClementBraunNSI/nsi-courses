# 📋 B2.3 - Listes et Collections en C#

<style>
.concept-card {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(255, 193, 7, 0.05));
    border: 1px solid rgba(255, 152, 0, 0.2);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.1);
    transition: all 0.3s ease;
}

.concept-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(255, 152, 0, 0.15);
}

.concept-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    display: block;
}

.concept-name {
    font-size: 1.3rem;
    font-weight: 700;
    color: #ff6f00;
    margin-bottom: 0.8rem;
}

.concept-description {
    color: #2c3e50;
    line-height: 1.6;
}

.highlight-fact {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.1));
    border-left: 4px solid #ff9800;
    padding: 1rem 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0 10px 10px 0;
    box-shadow: 0 2px 10px rgba(255, 152, 0, 0.1);
}

.code-example {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-family: 'Courier New', monospace;
}

.exercise-box {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(255, 193, 7, 0.05));
    border: 1px solid rgba(255, 152, 0, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.custom-h3 {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.9), rgba(255, 193, 7, 0.8));
    color: white;
    padding: 1.2rem 2rem;
    border-radius: 15px;
    margin: 2.5rem 0 1.5rem 0;
    font-size: 1.4rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    box-shadow: 0 8px 20px rgba(255, 152, 0, 0.3);
    border: 1px solid rgba(255, 152, 0, 0.3);
    transition: all 0.3s ease;
    backdrop-filter: blur(5px);
}

.custom-h3:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(255, 152, 0, 0.4);
}

.custom-h4 {
    background: rgba(255, 152, 0, 0.1);
    color: #2c3e50;
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    border-left: 4px solid #ff9800;
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.1);
    transition: all 0.3s ease;
}

.custom-h4:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(255, 152, 0, 0.2);
    background: rgba(255, 152, 0, 0.15);
}
</style>

## 📋 Objectifs du cours

À la fin de ce cours, vous serez capable de :
- ✅ Comprendre la différence entre tableaux et listes
- ✅ Manipuler les tableaux (arrays) en C#
- ✅ Utiliser les listes (List<T>) et leurs méthodes
- ✅ Travailler avec les dictionnaires (Dictionary<K,V>)
- ✅ Choisir la bonne collection selon le contexte

---

<h3 class="custom-h3">📊 Introduction aux collections</h3>

<div class="concept-card">
<span class="concept-icon">📦</span>
<div class="concept-name">Qu'est-ce qu'une collection ?</div>
<div class="concept-description">
Une collection est une structure de données qui permet de stocker et organiser plusieurs éléments du même type ou de types différents. En C#, nous avons plusieurs types de collections adaptées à différents besoins.
</div>
</div>

<div class="comparison-table">
<h4>🔍 Comparaison des principales collections</h4>

| Collection | Taille | Accès | Utilisation |
|------------|--------|-------|-------------|
| **Array** | Fixe | Index | Données de taille connue |
| **List<T>** | Variable | Index | Données dynamiques |
| **Dictionary<K,V>** | Variable | Clé | Associations clé-valeur |

</div>

---

<h3 class="custom-h3">🗂️ Les tableaux (Arrays)</h3>

<h4 class="custom-h4">📝 Déclaration et initialisation</h4>

<div class="code-example">
```csharp
// Déclaration avec taille fixe
int[] nombres = new int[5]; // Tableau de 5 entiers (0 par défaut)

// Déclaration avec initialisation
int[] scores = { 85, 92, 78, 96, 88 };

// Autre syntaxe d'initialisation
string[] noms = new string[] { "Alice", "Bob", "Charlie" };

// Initialisation avec new (C# 3.0+)
var couleurs = new[] { "Rouge", "Vert", "Bleu" };
```
</div>

<h4 class="custom-h4">🎯 Accès et modification</h4>

<div class="code-example">
```csharp
int[] notes = { 15, 18, 12, 16, 14 };

// Accès en lecture
Console.WriteLine($"Première note : {notes[0]}"); // 15
Console.WriteLine($"Dernière note : {notes[notes.Length - 1]}"); // 14

// Modification
notes[2] = 20; // Change 12 en 20

// Parcours avec for
for (int i = 0; i < notes.Length; i++)
{
    Console.WriteLine($"Note {i + 1} : {notes[i]}");
}

// Parcours avec foreach
foreach (int note in notes)
{
    Console.WriteLine($"Note : {note}");
}
```
</div>

<h4 class="custom-h4">🔧 Méthodes utiles pour les tableaux</h4>

<div class="code-example">
```csharp
int[] nombres = { 5, 2, 8, 1, 9, 3 };

// Taille du tableau
Console.WriteLine($"Taille : {nombres.Length}");

// Tri
Array.Sort(nombres);
Console.WriteLine("Trié : " + string.Join(", ", nombres)); // 1, 2, 3, 5, 8, 9

// Recherche
int index = Array.IndexOf(nombres, 5);
Console.WriteLine($"Index de 5 : {index}"); // 3

// Inversion
Array.Reverse(nombres);
Console.WriteLine("Inversé : " + string.Join(", ", nombres)); // 9, 8, 5, 3, 2, 1

// Copie
int[] copie = new int[nombres.Length];
Array.Copy(nombres, copie, nombres.Length);
```
</div>

---

<h3 class="custom-h3">📋 Les listes (List<T>)</h3>

<div class="concept-card">
<span class="concept-icon">📈</span>
<div class="concept-name">Avantages des listes</div>
<div class="concept-description">
Les listes sont des collections dynamiques qui peuvent grandir ou rétrécir pendant l'exécution. Elles offrent plus de flexibilité que les tableaux et de nombreuses méthodes utiles.
</div>
</div>

<h4 class="custom-h4">🚀 Création et initialisation</h4>

<div class="code-example">
```csharp
// Import nécessaire
using System.Collections.Generic;

// Liste vide
List<int> nombres = new List<int>();

// Liste avec capacité initiale
List<string> noms = new List<string>(10);

// Liste avec initialisation
List<double> prix = new List<double> { 19.99, 25.50, 12.75 };

// Syntaxe moderne (C# 9.0+)
List<string> couleurs = new() { "Rouge", "Vert", "Bleu" };
```
</div>

<h4 class="custom-h4">➕ Ajout d'éléments</h4>

<div class="code-example">
```csharp
List<string> fruits = new List<string>();

// Ajouter un élément à la fin
fruits.Add("Pomme");
fruits.Add("Banane");

// Ajouter plusieurs éléments
fruits.AddRange(new[] { "Orange", "Kiwi", "Mangue" });

// Insérer à une position spécifique
fruits.Insert(1, "Poire"); // Insère "Poire" à l'index 1

// Résultat : ["Pomme", "Poire", "Banane", "Orange", "Kiwi", "Mangue"]
Console.WriteLine(string.Join(", ", fruits));
```
</div>

<h4 class="custom-h4">🗑️ Suppression d'éléments</h4>

<div class="code-example">
```csharp
List<int> nombres = new List<int> { 1, 2, 3, 4, 5, 3, 6 };

// Supprimer la première occurrence
nombres.Remove(3); // Supprime le premier 3
// Résultat : [1, 2, 4, 5, 3, 6]

// Supprimer à un index spécifique
nombres.RemoveAt(0); // Supprime l'élément à l'index 0
// Résultat : [2, 4, 5, 3, 6]

// Supprimer une plage
nombres.RemoveRange(1, 2); // Supprime 2 éléments à partir de l'index 1
// Résultat : [2, 3, 6]

// Supprimer tous les éléments qui correspondent à une condition
nombres.RemoveAll(x => x > 3); // Supprime tous les nombres > 3
// Résultat : [2, 3]

// Vider la liste
nombres.Clear();
```
</div>

<h4 class="custom-h4">🔍 Recherche et vérification</h4>

<div class="code-example">
```csharp
List<string> animaux = new List<string> { "Chat", "Chien", "Oiseau", "Poisson" };

// Vérifier si un élément existe
bool aChat = animaux.Contains("Chat"); // true

// Trouver l'index d'un élément
int index = animaux.IndexOf("Chien"); // 1

// Trouver le dernier index
animaux.Add("Chat"); // Ajoute un deuxième "Chat"
int dernierIndex = animaux.LastIndexOf("Chat"); // 4

// Compter les éléments
int total = animaux.Count; // 5

// Vérifier si la liste est vide
bool estVide = animaux.Count == 0; // false

// Recherche avec condition (LINQ)
using System.Linq;
string premierOiseau = animaux.FirstOrDefault(a => a.StartsWith("O")); // "Oiseau"
```
</div>

<h4 class="custom-h4">🔄 Tri et manipulation</h4>

<div class="code-example">
```csharp
List<int> scores = new List<int> { 85, 92, 78, 96, 88 };

// Tri croissant
scores.Sort();
Console.WriteLine(string.Join(", ", scores)); // 78, 85, 88, 92, 96

// Tri décroissant
scores.Sort((a, b) => b.CompareTo(a));
Console.WriteLine(string.Join(", ", scores)); // 96, 92, 88, 85, 78

// Inversion
scores.Reverse();

// Conversion en tableau
int[] tableau = scores.ToArray();

// Copie vers une autre liste
List<int> copie = new List<int>(scores);
```
</div>

---

<h3 class="custom-h3">🗝️ Les dictionnaires (Dictionary<K,V>)</h3>

<div class="concept-card">
<span class="concept-icon">🔑</span>
<div class="concept-name">Principe des dictionnaires</div>
<div class="concept-description">
Un dictionnaire stocke des paires clé-valeur. Chaque clé est unique et permet d'accéder rapidement à sa valeur associée. C'est idéal pour créer des associations ou des index.
</div>
</div>

<h4 class="custom-h4">🏗️ Création et initialisation</h4>

<div class="code-example">
```csharp
// Import nécessaire
using System.Collections.Generic;

// Dictionnaire vide
Dictionary<string, int> ages = new Dictionary<string, int>();

// Dictionnaire avec initialisation
Dictionary<string, string> capitales = new Dictionary<string, string>
{
    { "France", "Paris" },
    { "Espagne", "Madrid" },
    { "Italie", "Rome" }
};

// Syntaxe moderne (C# 6.0+)
var notes = new Dictionary<string, double>
{
    ["Alice"] = 15.5,
    ["Bob"] = 18.0,
    ["Charlie"] = 12.5
};
```
</div>

<h4 class="custom-h4">➕ Ajout et modification</h4>

<div class="code-example">
```csharp
Dictionary<string, int> stock = new Dictionary<string, int>();

// Ajouter des éléments
stock.Add("Pommes", 50);
stock.Add("Bananes", 30);

// Syntaxe avec indexeur (plus simple)
stock["Oranges"] = 25;
stock["Kiwis"] = 15;

// Modifier une valeur existante
stock["Pommes"] = 45; // Change 50 en 45

// Ajouter seulement si la clé n'existe pas
if (!stock.ContainsKey("Mangues"))
{
    stock["Mangues"] = 20;
}

// Méthode TryAdd (C# 7.0+)
stock.TryAdd("Ananas", 10); // Ajoute seulement si la clé n'existe pas
```
</div>

<h4 class="custom-h4">🔍 Accès et recherche</h4>

<div class="code-example">
```csharp
Dictionary<string, double> prix = new Dictionary<string, double>
{
    ["Pain"] = 1.20,
    ["Lait"] = 0.95,
    ["Œufs"] = 2.50
};

// Accès direct (attention aux exceptions !)
double prixPain = prix["Pain"]; // 1.20

// Accès sécurisé avec TryGetValue
if (prix.TryGetValue("Beurre", out double prixBeurre))
{
    Console.WriteLine($"Prix du beurre : {prixBeurre}€");
}
else
{
    Console.WriteLine("Beurre non trouvé");
}

// Vérifier l'existence d'une clé
bool aPain = prix.ContainsKey("Pain"); // true

// Vérifier l'existence d'une valeur
bool aArticleA2Euros = prix.ContainsValue(2.00); // false

// Nombre d'éléments
int nombreArticles = prix.Count; // 3
```
</div>

<h4 class="custom-h4">🔄 Parcours des dictionnaires</h4>

<div class="code-example">
```csharp
Dictionary<string, int> scores = new Dictionary<string, int>
{
    ["Alice"] = 95,
    ["Bob"] = 87,
    ["Charlie"] = 92
};

// Parcours des paires clé-valeur
foreach (KeyValuePair<string, int> kvp in scores)
{
    Console.WriteLine($"{kvp.Key} : {kvp.Value} points");
}

// Syntaxe simplifiée (C# 7.0+)
foreach (var (nom, score) in scores)
{
    Console.WriteLine($"{nom} : {score} points");
}

// Parcours des clés seulement
foreach (string nom in scores.Keys)
{
    Console.WriteLine($"Joueur : {nom}");
}

// Parcours des valeurs seulement
foreach (int score in scores.Values)
{
    Console.WriteLine($"Score : {score}");
}
```
</div>

---

<h3 class="custom-h3">🎯 Exercices pratiques</h3>

<div class="exercise-box">
<h4>🏋️ Exercice 1 : Gestionnaire de notes</h4>

Créez un programme qui :
1. Stocke les notes d'étudiants dans un dictionnaire
2. Permet d'ajouter, modifier et supprimer des notes
3. Calcule et affiche la moyenne de la classe
4. Trouve l'étudiant avec la meilleure note

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 2 : Inventaire de magasin</h4>

Créez un système d'inventaire qui :
1. Utilise un dictionnaire pour stocker les produits et leurs quantités
2. Permet d'ajouter/retirer du stock
3. Affiche les produits en rupture de stock (quantité = 0)
4. Calcule la valeur totale du stock (avec un dictionnaire des prix)

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 3 : Analyseur de texte</h4>

Créez un programme qui :
1. Lit un texte saisi par l'utilisateur
2. Compte le nombre d'occurrences de chaque mot
3. Affiche les mots par ordre de fréquence
4. Ignore la casse et la ponctuation

```csharp
// Indice : utilisez string.Split() et char.IsPunctuation()
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 4 : Carnet d'adresses</h4>

Créez un carnet d'adresses qui :
1. Stocke nom, téléphone et email dans une classe Contact
2. Utilise une List<Contact> pour stocker tous les contacts
3. Permet de rechercher par nom
4. Trie les contacts par ordre alphabétique

```csharp
public class Contact
{
    public string Nom { get; set; }
    public string Telephone { get; set; }
    public string Email { get; set; }
}
```
</div>

---

<h3 class="custom-h3">⚡ Performances et bonnes pratiques</h3>

<div class="concept-card">
<span class="concept-icon">🚀</span>
<div class="concept-name">Conseils d'optimisation</div>
<div class="concept-description">

**1. Choisir la bonne collection :**
```csharp
// ✅ Pour des données de taille fixe
int[] scores = new int[10];

// ✅ Pour des données dynamiques avec accès par index
List<string> noms = new List<string>();

// ✅ Pour des associations clé-valeur
Dictionary<string, int> ages = new Dictionary<string, int>();
```

**2. Initialiser avec la bonne capacité :**
```csharp
// ✅ Si vous connaissez la taille approximative
List<int> nombres = new List<int>(1000); // Évite les redimensionnements
```

**3. Utiliser les bonnes méthodes :**
```csharp
// ❌ Lent pour de grandes collections
for (int i = 0; i < liste.Count; i++)
{
    if (liste[i] == valeur) return i;
}

// ✅ Plus rapide
int index = liste.IndexOf(valeur);
```

**4. Attention aux modifications pendant l'itération :**
```csharp
// ❌ Erreur à l'exécution
foreach (var item in liste)
{
    if (condition)
        liste.Remove(item); // Exception !
}

// ✅ Solution
for (int i = liste.Count - 1; i >= 0; i--)
{
    if (condition)
        liste.RemoveAt(i);
}
```

</div>
</div>

---

<h3 class="custom-h3">📚 Points clés à retenir</h3>

<div class="highlight-fact">
<strong>🎯 Résumé du chapitre :</strong>
<ul>
<li><strong>Tableaux :</strong> Taille fixe, accès rapide par index</li>
<li><strong>Listes :</strong> Taille variable, nombreuses méthodes utiles</li>
<li><strong>Dictionnaires :</strong> Associations clé-valeur, accès rapide par clé</li>
<li><strong>Choix :</strong> Dépend du type de données et des opérations nécessaires</li>
<li><strong>Performance :</strong> Initialiser avec la bonne capacité, choisir les bonnes méthodes</li>
</ul>
</div>

---

## 🔗 Liens utiles

- [Collections en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/concepts/collections)
- [List<T> Class](https://docs.microsoft.com/fr-fr/dotnet/api/system.collections.generic.list-1)
- [Dictionary<TKey,TValue> Class](https://docs.microsoft.com/fr-fr/dotnet/api/system.collections.generic.dictionary-2)

---

**Étape précédente :** [B2.2 - Structures de contrôle](B2_2_Structures_controle.md)  
**Prochaine étape :** [B2.4 - Fonctions et méthodes](B2_4_Fonctions_methodes.md)