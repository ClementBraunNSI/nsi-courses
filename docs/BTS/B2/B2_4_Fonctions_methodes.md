# 🔧 B2.4 - Fonctions et Méthodes en C#

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
    box-shadow: 0 6px 18px rgba(255, 152, 0, 0.2);
    background: rgba(255, 152, 0, 0.15);
}
</style>

## 📋 Objectifs du cours

À la fin de ce cours, vous serez capable de :
- ✅ Comprendre l'utilité des fonctions et méthodes
- ✅ Créer des méthodes avec et sans paramètres
- ✅ Utiliser les valeurs de retour
- ✅ Maîtriser les différents types de paramètres
- ✅ Appliquer les bonnes pratiques de programmation modulaire

---

<h3 class="custom-h3">🎯 Introduction aux méthodes</h3>

<div class="concept-card">
<span class="concept-icon">🔧</span>
<div class="concept-name">Qu'est-ce qu'une méthode ?</div>
<div class="concept-description">
Une méthode est un bloc de code réutilisable qui effectue une tâche spécifique. Elle permet de diviser un programme complexe en parties plus petites et plus gérables, favorisant la réutilisabilité et la lisibilité du code.
</div>
</div>

<div class="highlight-fact">
<strong>💡 Avantages des méthodes :</strong>
<ul>
<li><strong>Réutilisabilité :</strong> Évite la duplication de code</li>
<li><strong>Lisibilité :</strong> Code plus organisé et compréhensible</li>
<li><strong>Maintenance :</strong> Modifications centralisées</li>
<li><strong>Test :</strong> Facilite les tests unitaires</li>
</ul>
</div>

<h4 class="custom-h4">📝 Anatomie d'une méthode</h4>

<div class="code-example">
```csharp
// Syntaxe générale
[modificateur] [type_retour] NomMethode([paramètres])
{
    // Corps de la méthode
    [return valeur;] // Si type_retour != void
}

// Exemple concret
public static int Additionner(int a, int b)
{
    int resultat = a + b;
    return resultat;
}
```
</div>

---

<h3 class="custom-h3">🚀 Méthodes simples</h3>

<h4 class="custom-h4">🔤 Méthodes sans paramètres ni retour</h4>

<div class="code-example">
```csharp
// Méthode qui affiche un message
public static void AfficherBienvenue()
{
    Console.WriteLine("===================");
    Console.WriteLine("  BIENVENUE !  ");
    Console.WriteLine("===================");
}

// Méthode qui affiche la date actuelle
public static void AfficherDate()
{
    DateTime maintenant = DateTime.Now;
    Console.WriteLine($"Nous sommes le {maintenant:dd/MM/yyyy}");
}

// Utilisation dans Main
static void Main(string[] args)
{
    AfficherBienvenue();
    AfficherDate();
}
```
</div>

<h4 class="custom-h4">📤 Méthodes avec valeur de retour</h4>

<div class="code-example">
```csharp
// Méthode qui retourne un nombre aléatoire
public static int GenererNombreAleatoire()
{
    Random random = new Random();
    return random.Next(1, 101); // Entre 1 et 100
}

// Méthode qui retourne l'heure actuelle formatée
public static string ObtenirHeureActuelle()
{
    return DateTime.Now.ToString("HH:mm:ss");
}

// Méthode qui vérifie si une année est bissextile
public static bool EstBissextile(int annee)
{
    return (annee % 4 == 0 && annee % 100 != 0) || (annee % 400 == 0);
}

// Utilisation
static void Main(string[] args)
{
    int nombre = GenererNombreAleatoire();
    string heure = ObtenirHeureActuelle();
    bool bissextile = EstBissextile(2024);
    
    Console.WriteLine($"Nombre : {nombre}");
    Console.WriteLine($"Heure : {heure}");
    Console.WriteLine($"2024 est bissextile : {bissextile}");
}
```
</div>

---

<h3 class="custom-h3">📥 Paramètres de méthodes</h3>

<h4 class="custom-h4">🎯 Paramètres simples</h4>

<div class="code-example">
```csharp
// Méthode avec un paramètre
public static void SaluerPersonne(string nom)
{
    Console.WriteLine($"Bonjour {nom} !");
}

// Méthode avec plusieurs paramètres
public static double CalculerAire(double longueur, double largeur)
{
    return longueur * largeur;
}

// Méthode avec paramètres de types différents
public static void AfficherInfoPersonne(string nom, int age, bool estEtudiant)
{
    Console.WriteLine($"Nom : {nom}");
    Console.WriteLine($"Âge : {age} ans");
    Console.WriteLine($"Statut : {(estEtudiant ? "Étudiant" : "Non étudiant")}");
}

// Utilisation
static void Main(string[] args)
{
    SaluerPersonne("Alice");
    
    double aire = CalculerAire(5.5, 3.2);
    Console.WriteLine($"Aire : {aire} m²");
    
    AfficherInfoPersonne("Bob", 22, true);
}
```
</div>

<h4 class="custom-h4">🔧 Paramètres avec valeurs par défaut</h4>

<div class="code-example">
```csharp
// Paramètres optionnels avec valeurs par défaut
public static void CreerCompte(string nom, string email, bool estActif = true, string role = "Utilisateur")
{
    Console.WriteLine($"Compte créé :");
    Console.WriteLine($"- Nom : {nom}");
    Console.WriteLine($"- Email : {email}");
    Console.WriteLine($"- Actif : {estActif}");
    Console.WriteLine($"- Rôle : {role}");
}

// Méthode de calcul avec paramètres optionnels
public static double CalculerPrix(double prixBase, double tva = 0.20, double remise = 0.0)
{
    double prixAvecTva = prixBase * (1 + tva);
    double prixFinal = prixAvecTva * (1 - remise);
    return prixFinal;
}

// Utilisation avec différentes combinaisons
static void Main(string[] args)
{
    // Tous les paramètres
    CreerCompte("Alice", "alice@email.com", true, "Admin");
    
    // Paramètres par défaut utilisés
    CreerCompte("Bob", "bob@email.com");
    
    // Paramètres nommés
    CreerCompte("Charlie", "charlie@email.com", role: "Modérateur");
    
    // Calculs de prix
    double prix1 = CalculerPrix(100);           // 120€ (TVA 20%)
    double prix2 = CalculerPrix(100, 0.10);     // 110€ (TVA 10%)
    double prix3 = CalculerPrix(100, 0.20, 0.15); // 102€ (TVA 20%, remise 15%)
}
```
</div>

<h4 class="custom-h4">📋 Paramètres params</h4>

<div class="code-example">
```csharp
// Méthode avec nombre variable de paramètres
public static int Additionner(params int[] nombres)
{
    int somme = 0;
    foreach (int nombre in nombres)
    {
        somme += nombre;
    }
    return somme;
}

// Méthode pour formater un message avec plusieurs valeurs
public static string FormaterMessage(string template, params object[] valeurs)
{
    return string.Format(template, valeurs);
}

// Utilisation
static void Main(string[] args)
{
    // Différentes façons d'appeler la méthode
    int somme1 = Additionner(1, 2, 3);           // 6
    int somme2 = Additionner(10, 20, 30, 40);    // 100
    int somme3 = Additionner();                  // 0
    
    // Avec un tableau
    int[] nombres = { 5, 10, 15 };
    int somme4 = Additionner(nombres);           // 30
    
    // Formatage de messages
    string msg = FormaterMessage("Bonjour {0}, vous avez {1} ans", "Alice", 25);
    Console.WriteLine(msg); // "Bonjour Alice, vous avez 25 ans"
}
```
</div>

---

<h3 class="custom-h3">🔄 Paramètres par référence</h3>

<h4 class="custom-h4">📤 Paramètres out</h4>

<div class="code-example">
```csharp
// Méthode qui retourne plusieurs valeurs avec out
public static bool DiviserAvecReste(int dividende, int diviseur, out int quotient, out int reste)
{
    if (diviseur == 0)
    {
        quotient = 0;
        reste = 0;
        return false; // Division impossible
    }
    
    quotient = dividende / diviseur;
    reste = dividende % diviseur;
    return true; // Division réussie
}

// Méthode pour analyser une chaîne de nombres
public static bool AnalyserNombres(string texte, out int minimum, out int maximum, out double moyenne)
{
    minimum = 0;
    maximum = 0;
    moyenne = 0;
    
    string[] parties = texte.Split(',');
    List<int> nombres = new List<int>();
    
    foreach (string partie in parties)
    {
        if (int.TryParse(partie.Trim(), out int nombre))
        {
            nombres.Add(nombre);
        }
    }
    
    if (nombres.Count == 0)
        return false;
    
    minimum = nombres.Min();
    maximum = nombres.Max();
    moyenne = nombres.Average();
    return true;
}

// Utilisation
static void Main(string[] args)
{
    // Division avec reste
    if (DiviserAvecReste(17, 5, out int quotient, out int reste))
    {
        Console.WriteLine($"17 ÷ 5 = {quotient} reste {reste}");
    }
    
    // Analyse de nombres
    string donnees = "10, 25, 8, 33, 12";
    if (AnalyserNombres(donnees, out int min, out int max, out double moy))
    {
        Console.WriteLine($"Min: {min}, Max: {max}, Moyenne: {moy:F2}");
    }
}
```
</div>

<h4 class="custom-h4">🔄 Paramètres ref</h4>

<div class="code-example">
```csharp
// Méthode qui échange deux valeurs
public static void Echanger(ref int a, ref int b)
{
    int temp = a;
    a = b;
    b = temp;
}

// Méthode qui modifie une chaîne
public static void TransformerTexte(ref string texte)
{
    texte = texte.ToUpper().Replace(" ", "_");
}

// Méthode qui applique une remise
public static void AppliquerRemise(ref double prix, double pourcentageRemise)
{
    prix = prix * (1 - pourcentageRemise / 100);
}

// Utilisation
static void Main(string[] args)
{
    // Échange de valeurs
    int x = 10, y = 20;
    Console.WriteLine($"Avant : x={x}, y={y}");
    Echanger(ref x, ref y);
    Console.WriteLine($"Après : x={x}, y={y}");
    
    // Transformation de texte
    string message = "Bonjour le monde";
    Console.WriteLine($"Avant : {message}");
    TransformerTexte(ref message);
    Console.WriteLine($"Après : {message}");
    
    // Application de remise
    double prix = 100.0;
    Console.WriteLine($"Prix initial : {prix}€");
    AppliquerRemise(ref prix, 15); // 15% de remise
    Console.WriteLine($"Prix après remise : {prix}€");
}
```
</div>

---

<h3 class="custom-h3">🏗️ Méthodes avancées</h3>

<h4 class="custom-h4">🔄 Surcharge de méthodes (Overloading)</h4>

<div class="code-example">
```csharp
// Plusieurs versions de la même méthode avec des paramètres différents
public static class Calculatrice
{
    // Addition de deux entiers
    public static int Additionner(int a, int b)
    {
        return a + b;
    }
    
    // Addition de trois entiers
    public static int Additionner(int a, int b, int c)
    {
        return a + b + c;
    }
    
    // Addition de deux doubles
    public static double Additionner(double a, double b)
    {
        return a + b;
    }
    
    // Addition d'un tableau d'entiers
    public static int Additionner(int[] nombres)
    {
        int somme = 0;
        foreach (int nombre in nombres)
        {
            somme += nombre;
        }
        return somme;
    }
}

// Utilisation
static void Main(string[] args)
{
    int somme1 = Calculatrice.Additionner(5, 3);           // 8
    int somme2 = Calculatrice.Additionner(1, 2, 3);        // 6
    double somme3 = Calculatrice.Additionner(2.5, 3.7);    // 6.2
    int somme4 = Calculatrice.Additionner(new int[] { 1, 2, 3, 4 }); // 10
}
```
</div>

<h4 class="custom-h4">🎯 Méthodes d'extension</h4>

<div class="code-example">
```csharp
// Classe statique pour les méthodes d'extension
public static class StringExtensions
{
    // Méthode d'extension pour compter les mots
    public static int CompterMots(this string texte)
    {
        if (string.IsNullOrWhiteSpace(texte))
            return 0;
        
        return texte.Split(new char[] { ' ', '\t', '\n' }, 
                          StringSplitOptions.RemoveEmptyEntries).Length;
    }
    
    // Méthode d'extension pour inverser une chaîne
    public static string Inverser(this string texte)
    {
        if (string.IsNullOrEmpty(texte))
            return texte;
        
        char[] caracteres = texte.ToCharArray();
        Array.Reverse(caracteres);
        return new string(caracteres);
    }
    
    // Méthode d'extension pour capitaliser chaque mot
    public static string CapitaliserMots(this string texte)
    {
        if (string.IsNullOrWhiteSpace(texte))
            return texte;
        
        return System.Globalization.CultureInfo.CurrentCulture.TextInfo.ToTitleCase(texte.ToLower());
    }
}

// Utilisation
static void Main(string[] args)
{
    string phrase = "bonjour le monde";
    
    // Utilisation comme si c'étaient des méthodes de la classe string
    int nombreMots = phrase.CompterMots();           // 3
    string inverse = phrase.Inverser();              // "ednom el ruojnob"
    string capitalise = phrase.CapitaliserMots();    // "Bonjour Le Monde"
    
    Console.WriteLine($"Phrase : {phrase}");
    Console.WriteLine($"Nombre de mots : {nombreMots}");
    Console.WriteLine($"Inversée : {inverse}");
    Console.WriteLine($"Capitalisée : {capitalise}");
}
```
</div>

---

<h3 class="custom-h3">🎯 Exercices pratiques</h3>

<div class="exercise-box">
<h4>🏋️ Exercice 1 : Calculatrice avancée</h4>

Créez une classe Calculatrice avec les méthodes suivantes :
1. `Additionner`, `Soustraire`, `Multiplier`, `Diviser` (avec gestion division par zéro)
2. `Puissance` (nombre élevé à une puissance)
3. `Factorielle` (calcul récursif ou itératif)
4. `EstPremier` (vérifier si un nombre est premier)

```csharp
public static class Calculatrice
{
    // Vos méthodes ici
}
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 2 : Gestionnaire de mots de passe</h4>

Créez des méthodes pour :
1. `GenererMotDePasse(int longueur, bool inclureSymboles = false)`
2. `ValiderMotDePasse(string motDePasse, out string[] erreurs)`
3. `CalculerForce(string motDePasse)` qui retourne un score de 0 à 100

Critères de validation : au moins 8 caractères, une majuscule, une minuscule, un chiffre.

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 3 : Analyseur de fichier texte</h4>

Créez des méthodes pour analyser un texte :
1. `CompterCaracteres(string texte, out int lettres, out int chiffres, out int espaces)`
2. `TrouverMotLePlusLong(string texte)`
3. `CalculerFrequenceMots(string texte)` qui retourne un Dictionary<string, int>
4. `RemplacerMots(ref string texte, Dictionary<string, string> remplacements)`

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 4 : Système de notes</h4>

Créez un système de gestion de notes avec :
1. `AjouterNote(List<double> notes, double note)` avec validation (0-20)
2. `CalculerMoyenne(List<double> notes)`
3. `ObtenirStatistiques(List<double> notes, out double min, out double max, out double ecartType)`
4. `AttribuerMention(double moyenne)` qui retourne "Très bien", "Bien", etc.

```csharp
// Votre code ici
```
</div>

---

<h3 class="custom-h3">🚀 Bonnes pratiques</h3>

<div class="concept-card">
<span class="concept-icon">⭐</span>
<div class="concept-name">Conseils pour de bonnes méthodes</div>
<div class="concept-description">

**1. Nommage clair et descriptif :**
```csharp
// ❌ Mauvais
public static int Calc(int x, int y) { return x + y; }

// ✅ Bon
public static int CalculerSomme(int premier, int second) { return premier + second; }
```

**2. Une méthode = une responsabilité :**
```csharp
// ❌ Fait trop de choses
public static void TraiterUtilisateur(string nom, string email)
{
    // Validation
    // Sauvegarde en base
    // Envoi d'email
    // Logging
}

// ✅ Responsabilités séparées
public static bool ValiderUtilisateur(string nom, string email) { /* ... */ }
public static void SauvegarderUtilisateur(string nom, string email) { /* ... */ }
public static void EnvoyerEmailBienvenue(string email) { /* ... */ }
```

**3. Éviter les méthodes trop longues :**
```csharp
// ✅ Si une méthode fait plus de 20-30 lignes, la diviser
public static void TraiterCommande(Commande commande)
{
    ValiderCommande(commande);
    CalculerPrix(commande);
    AppliquerRemises(commande);
    EnregistrerCommande(commande);
}
```

**4. Gérer les cas d'erreur :**
```csharp
public static double Diviser(double a, double b)
{
    if (b == 0)
        throw new ArgumentException("Division par zéro impossible");
    
    return a / b;
}
```

</div>
</div>

<div class="warning-box">
<strong>⚠️ Erreurs courantes à éviter :</strong>
<ul>
<li><strong>Oublier le return :</strong> Dans une méthode non-void</li>
<li><strong>Modifier des paramètres :</strong> Sans ref/out quand nécessaire</li>
<li><strong>Méthodes trop complexes :</strong> Diviser en sous-méthodes</li>
<li><strong>Pas de validation :</strong> Toujours valider les paramètres d'entrée</li>
</ul>
</div>

---

<h3 class="custom-h3">📚 Points clés à retenir</h3>

<div class="highlight-fact">
<strong>🎯 Résumé du chapitre :</strong>
<ul>
<li><strong>Méthodes :</strong> Blocs de code réutilisables avec paramètres et retour</li>
<li><strong>Paramètres :</strong> Simples, optionnels, params, ref, out</li>
<li><strong>Surcharge :</strong> Plusieurs versions avec paramètres différents</li>
<li><strong>Extensions :</strong> Ajouter des méthodes aux types existants</li>
<li><strong>Bonnes pratiques :</strong> Nommage clair, responsabilité unique, gestion d'erreurs</li>
</ul>
</div>

---

## 🔗 Liens utiles

- [Méthodes en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/classes-and-structs/methods)
- [Paramètres de méthodes](https://docs.microsoft.com/fr-fr/dotnet/csharp/language-reference/keywords/method-parameters)
- [Méthodes d'extension](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/classes-and-structs/extension-methods)

---

**Étape précédente :** [B2.3 - Listes et collections](B2_3_Listes_collections.md)  
**Prochaine étape :** [B2.5 - Programmation Orientée Objet](B2_5_POO_CSharp.md)