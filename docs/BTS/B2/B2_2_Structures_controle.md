# 🔄 B2.2 - Structures de contrôle en C#

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

.warning-box {
    background: linear-gradient(135deg, rgba(220, 53, 69, 0.1), rgba(255, 107, 107, 0.05));
    border: 1px solid rgba(220, 53, 69, 0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
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
    box-shadow: 0 6px 18px rgba(220, 38, 127, 0.2);
    background: rgba(220, 38, 127, 0.15);
}
</style>

## 📋 Objectifs du cours

À la fin de ce cours, vous serez capable de :
- ✅ Utiliser les structures conditionnelles (if, else, switch)
- ✅ Maîtriser les différents types de boucles (for, while, foreach)
- ✅ Contrôler l'exécution avec break et continue
- ✅ Imbriquer les structures de contrôle
- ✅ Optimiser vos algorithmes

---

<h3 class="custom-h3">🤔 Structures conditionnelles</h3>

<div class="concept-card">
<span class="concept-icon">🔀</span>
<div class="concept-name">Qu'est-ce qu'une condition ?</div>
<div class="concept-description">
Les structures conditionnelles permettent d'exécuter différents blocs de code selon qu'une condition est vraie ou fausse. Elles sont essentielles pour créer des programmes qui s'adaptent aux situations.
</div>
</div>

<h4 class="custom-h4">🎯 La structure if</h4>

<div class="code-example">
```csharp
// Structure if simple
int age = 20;

if (age >= 18)
{
    Console.WriteLine("Vous êtes majeur !");
}

// if avec else
if (age >= 18)
{
    Console.WriteLine("Vous êtes majeur !");
}
else
{
    Console.WriteLine("Vous êtes mineur !");
}
```
</div>

<h4 class="custom-h4">🔗 La structure if-else if</h4>

<div class="code-example">
```csharp
int note = 85;

if (note >= 90)
{
    Console.WriteLine("Excellent ! Note A");
}
else if (note >= 80)
{
    Console.WriteLine("Très bien ! Note B");
}
else if (note >= 70)
{
    Console.WriteLine("Bien ! Note C");
}
else if (note >= 60)
{
    Console.WriteLine("Passable ! Note D");
}
else
{
    Console.WriteLine("Échec ! Note F");
}
```
</div>

<h4 class="custom-h4">🎛️ La structure switch</h4>

<div class="code-example">
```csharp
// Switch classique
int jour = 3;

switch (jour)
{
    case 1:
        Console.WriteLine("Lundi");
        break;
    case 2:
        Console.WriteLine("Mardi");
        break;
    case 3:
        Console.WriteLine("Mercredi");
        break;
    case 4:
        Console.WriteLine("Jeudi");
        break;
    case 5:
        Console.WriteLine("Vendredi");
        break;
    case 6:
    case 7:
        Console.WriteLine("Week-end !");
        break;
    default:
        Console.WriteLine("Jour invalide");
        break;
}
```
</div>

<div class="highlight-fact">
<strong>💡 Astuce C# 8.0+ :</strong> Vous pouvez utiliser la nouvelle syntaxe switch expression pour un code plus concis !
</div>

<div class="code-example">
```csharp
// Switch expression (C# 8.0+)
string nomJour = jour switch
{
    1 => "Lundi",
    2 => "Mardi",
    3 => "Mercredi",
    4 => "Jeudi",
    5 => "Vendredi",
    6 or 7 => "Week-end",
    _ => "Jour invalide"
};

Console.WriteLine(nomJour);
```
</div>

<h4 class="custom-h4">❓ Opérateur ternaire</h4>

<div class="code-example">
```csharp
// Syntaxe : condition ? valeurSiVrai : valeurSiFaux
int age = 20;
string statut = age >= 18 ? "Majeur" : "Mineur";

// Équivalent à :
string statut2;
if (age >= 18)
    statut2 = "Majeur";
else
    statut2 = "Mineur";

// Utilisation dans l'affichage
Console.WriteLine($"Vous êtes {(age >= 18 ? "majeur" : "mineur")}");
```
</div>

---

<h3 class="custom-h3">🔄 Les boucles</h3>

<div class="concept-card">
<span class="concept-icon">🔁</span>
<div class="concept-name">Pourquoi utiliser des boucles ?</div>
<div class="concept-description">
Les boucles permettent de répéter un bloc de code plusieurs fois sans avoir à l'écrire plusieurs fois. Elles sont essentielles pour traiter des collections de données ou répéter des actions.
</div>
</div>

<h4 class="custom-h4">🔢 La boucle for</h4>

<div class="code-example">
```csharp
// Syntaxe : for (initialisation; condition; incrémentation)
for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"Itération {i}");
}

// Affichage des nombres pairs de 0 à 20
for (int i = 0; i <= 20; i += 2)
{
    Console.WriteLine(i);
}

// Boucle décroissante
for (int i = 10; i >= 0; i--)
{
    Console.WriteLine($"Compte à rebours : {i}");
}
```
</div>

<h4 class="custom-h4">⏳ La boucle while</h4>

<div class="code-example">
```csharp
// Boucle while - condition testée avant l'exécution
int compteur = 0;
while (compteur < 5)
{
    Console.WriteLine($"Compteur : {compteur}");
    compteur++;
}

// Exemple pratique : saisie utilisateur
string reponse;
do
{
    Console.Write("Voulez-vous continuer ? (oui/non) : ");
    reponse = Console.ReadLine().ToLower();
} while (reponse != "oui" && reponse != "non");
```
</div>

<h4 class="custom-h4">🔄 La boucle do-while</h4>

<div class="code-example">
```csharp
// Boucle do-while - condition testée après l'exécution
int nombre;
do
{
    Console.Write("Entrez un nombre entre 1 et 10 : ");
    string input = Console.ReadLine();
    int.TryParse(input, out nombre);
    
    if (nombre < 1 || nombre > 10)
    {
        Console.WriteLine("Nombre invalide !");
    }
} while (nombre < 1 || nombre > 10);

Console.WriteLine($"Merci ! Vous avez saisi : {nombre}");
```
</div>

<h4 class="custom-h4">📋 La boucle foreach</h4>

<div class="code-example">
```csharp
// Parcours d'un tableau
int[] nombres = { 1, 2, 3, 4, 5 };

foreach (int nombre in nombres)
{
    Console.WriteLine($"Nombre : {nombre}");
}

// Parcours d'une chaîne de caractères
string mot = "Bonjour";
foreach (char lettre in mot)
{
    Console.WriteLine($"Lettre : {lettre}");
}
```
</div>

---

<h3 class="custom-h3">🎮 Contrôle d'exécution</h3>

<h4 class="custom-h4">🛑 L'instruction break</h4>

<div class="code-example">
```csharp
// Break dans une boucle for
for (int i = 0; i < 10; i++)
{
    if (i == 5)
    {
        Console.WriteLine("Arrêt à 5 !");
        break; // Sort de la boucle
    }
    Console.WriteLine(i);
}

// Break dans un switch
int choix = 2;
switch (choix)
{
    case 1:
        Console.WriteLine("Option 1");
        break;
    case 2:
        Console.WriteLine("Option 2");
        break; // Obligatoire en C#
    default:
        Console.WriteLine("Option par défaut");
        break;
}
```
</div>

<h4 class="custom-h4">⏭️ L'instruction continue</h4>

<div class="code-example">
```csharp
// Continue dans une boucle for
for (int i = 0; i < 10; i++)
{
    if (i % 2 == 0) // Si le nombre est pair
    {
        continue; // Passe à l'itération suivante
    }
    Console.WriteLine($"Nombre impair : {i}");
}

// Affiche seulement : 1, 3, 5, 7, 9
```
</div>

<div class="warning-box">
<strong>⚠️ Attention :</strong> 
<ul>
<li><code>break</code> sort complètement de la boucle</li>
<li><code>continue</code> passe à l'itération suivante</li>
<li>Dans les boucles imbriquées, ils n'affectent que la boucle la plus proche</li>
</ul>
</div>

---

<h3 class="custom-h3">🏗️ Structures imbriquées</h3>

<h4 class="custom-h4">🔄 Boucles imbriquées</h4>

<div class="code-example">
```csharp
// Table de multiplication
for (int i = 1; i <= 5; i++)
{
    Console.WriteLine($"Table de {i} :");
    for (int j = 1; j <= 10; j++)
    {
        Console.WriteLine($"{i} x {j} = {i * j}");
    }
    Console.WriteLine(); // Ligne vide
}

// Matrice 3x3
for (int ligne = 0; ligne < 3; ligne++)
{
    for (int colonne = 0; colonne < 3; colonne++)
    {
        Console.Write($"[{ligne},{colonne}] ");
    }
    Console.WriteLine(); // Nouvelle ligne
}
```
</div>

<h4 class="custom-h4">🤔 Conditions imbriquées</h4>

<div class="code-example">
```csharp
int age = 25;
bool aPermis = true;
bool aVoiture = false;

if (age >= 18)
{
    Console.WriteLine("Vous êtes majeur.");
    
    if (aPermis)
    {
        Console.WriteLine("Vous avez le permis.");
        
        if (aVoiture)
        {
            Console.WriteLine("Vous pouvez conduire votre voiture !");
        }
        else
        {
            Console.WriteLine("Il vous faut une voiture.");
        }
    }
    else
    {
        Console.WriteLine("Il vous faut passer le permis.");
    }
}
else
{
    Console.WriteLine("Vous êtes mineur, pas de conduite !");
}
```
</div>

---

<h3 class="custom-h3">🎯 Exercices pratiques</h3>

<div class="exercise-box">
<h4>🏋️ Exercice 1 : Calculateur de notes</h4>

Créez un programme qui :
1. Demande le nombre d'étudiants
2. Pour chaque étudiant, demande sa note
3. Calcule et affiche la moyenne
4. Indique combien d'étudiants ont eu plus de 10/20

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 2 : Jeu de devinette</h4>

Créez un jeu où :
1. L'ordinateur choisit un nombre aléatoire entre 1 et 100
2. L'utilisateur doit deviner le nombre
3. Le programme indique si le nombre est trop grand ou trop petit
4. Le jeu continue jusqu'à ce que l'utilisateur trouve

```csharp
// Indice : utilisez Random random = new Random();
// int nombreSecret = random.Next(1, 101);
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 3 : Menu interactif</h4>

Créez un menu qui propose :
1. Calculer l'aire d'un rectangle
2. Calculer l'aire d'un cercle
3. Convertir Celsius vers Fahrenheit
4. Quitter

Le menu doit se répéter jusqu'à ce que l'utilisateur choisisse "Quitter".

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 4 : Pyramide d'étoiles</h4>

Créez un programme qui affiche une pyramide d'étoiles :
```
    *
   ***
  *****
 *******
*********
```

L'utilisateur doit pouvoir choisir la hauteur de la pyramide.

```csharp
// Votre code ici
```
</div>

---

<h3 class="custom-h3">🚀 Optimisations et bonnes pratiques</h3>

<div class="concept-card">
<span class="concept-icon">⚡</span>
<div class="concept-name">Conseils d'optimisation</div>
<div class="concept-description">

**1. Évitez les boucles infinies :**
```csharp
// ❌ Mauvais
while (true)
{
    // Code sans condition de sortie
}

// ✅ Bon
bool continuer = true;
while (continuer)
{
    // Code avec condition de sortie
    if (conditionSortie)
        continuer = false;
}
```

**2. Utilisez foreach quand c'est possible :**
```csharp
int[] tableau = {1, 2, 3, 4, 5};

// ❌ Moins lisible
for (int i = 0; i < tableau.Length; i++)
{
    Console.WriteLine(tableau[i]);
}

// ✅ Plus lisible
foreach (int element in tableau)
{
    Console.WriteLine(element);
}
```

**3. Évitez les conditions complexes :**
```csharp
// ❌ Difficile à lire
if (age >= 18 && age <= 65 && salaire > 30000 && !estEtudiant)
{
    // Code
}

// ✅ Plus clair
bool estAdulteActif = age >= 18 && age <= 65;
bool aSalaireCorrect = salaire > 30000;
bool peutEmprunter = estAdulteActif && aSalaireCorrect && !estEtudiant;

if (peutEmprunter)
{
    // Code
}
```

</div>
</div>

---

<h3 class="custom-h3">📚 Points clés à retenir</h3>

<div class="highlight-fact">
<strong>🎯 Résumé du chapitre :</strong>
<ul>
<li><strong>Conditions :</strong> if/else, switch, opérateur ternaire</li>
<li><strong>Boucles :</strong> for (compteur), while (condition), foreach (collection)</li>
<li><strong>Contrôle :</strong> break (sortir), continue (passer)</li>
<li><strong>Imbrication :</strong> Possible mais attention à la lisibilité</li>
<li><strong>Bonnes pratiques :</strong> Code lisible, éviter les boucles infinies</li>
</ul>
</div>

---

## 🔗 Liens utiles

- [Structures conditionnelles C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/language-reference/statements/selection-statements)
- [Boucles en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/language-reference/statements/iteration-statements)
- [Switch expressions C# 8.0](https://docs.microsoft.com/fr-fr/dotnet/csharp/language-reference/operators/switch-expression)

---

**Étape précédente :** [B2.1 - Les bases du C#](B2_1_Bases_CSharp.md)  
**Prochaine étape :** [B2.3 - Listes et collections](B2_3_Listes_collections.md)