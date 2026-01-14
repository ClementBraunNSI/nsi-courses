<!-- Style inspiré de premiers_pas_csharp.md -->
<style>
.course-header {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
    text-align: center;
}
.course-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}
.course-subtitle { color: #7f8c8d; font-size: 1.2rem; font-weight: 300; margin-bottom: 2rem; }
.concept-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.section-title {
    font-size: 2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 1.5rem;
    border-bottom: 2px solid rgba(52, 152, 219, 0.2);
    padding-bottom: 0.5rem;
}
.subsection-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2980b9;
    margin: 1.5rem 0 1rem 0;
}
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1rem 0; font-size: 1.05rem; }
.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.08), rgba(155, 89, 182, 0.04));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}
.definition-title { font-size: 1.1rem; font-weight: 600; color: #2980b9; margin-bottom: 0.5rem; }
.definition-content { color: var(--md-default-fg-color); font-size: 1rem; line-height: 1.6; }
</style>

<div class="course-header">
    <h1 class="course-title">Les Bases de la POO en C#</h1>
    <p class="course-subtitle">Programmation Orientée Objet : Concepts, Classes et Objets</p>
</div>

<div class="concept-section">
    <h2 class="section-title">1. Introduction</h2>
    <div class="content-text">
        La Programmation Orientée Objet (POO) est un paradigme de programmation qui organise le code autour du concept d'<strong>objets</strong> plutôt que de fonctions et de logique. C'est une approche naturelle qui reflète la façon dont nous pensons au monde réel.
    </div>
    <div class="definition-box">
        <div class="definition-title">Pourquoi la POO ?</div>
        <div class="definition-content">
            <ul>
                <li>✅ <strong>Réutilisabilité</strong> : Le code peut être réutilisé dans différents contextes</li>
                <li>✅ <strong>Maintenabilité</strong> : Plus facile à comprendre et à modifier</li>
                <li>✅ <strong>Modularité</strong> : Le code est organisé en modules logiques</li>
                <li>✅ <strong>Abstraction</strong> : Cache la complexité et montre seulement l'essentiel</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">2. Les Concepts Fondamentaux</h2>

    <h3 class="subsection-title">Qu'est-ce qu'un Objet ?</h3>
    <div class="content-text">
        Un <strong>objet</strong> est une entité qui combine :
        <ul>
            <li>Des <strong>données</strong> (ce qu'il EST) → appelées <strong>attributs</strong> ou <strong>propriétés</strong>.</li>
            <li>Des <strong>comportements</strong> (ce qu'il FAIT) → appelées <strong>méthodes</strong>.</li>
        </ul>
    </div>
    <div class="definition-box">
        <div class="definition-title">Analogie du monde réel</div>
        <div class="definition-content">
            Prenons l'exemple d'un <strong>chien</strong> :
            <ul>
                <li><strong>Données</strong> : nom, race, âge, couleur, poids</li>
                <li><strong>Comportements</strong> : aboyer(), manger(), courir(), dormir()</li>
            </ul>
        </div>
    </div>

    <h3 class="subsection-title">Qu'est-ce qu'une Classe ?</h3>
    <div class="content-text">
        Une <strong>classe</strong> est un <strong>modèle</strong> (blueprint) qui définit la structure et le comportement des objets.
        <br><br>
        <strong>Analogie :</strong>
        <ul>
            <li>La classe = le plan d'architecte d'une maison</li>
            <li>L'objet = la maison construite d'après ce plan</li>
        </ul>
        On peut construire <strong>plusieurs maisons</strong> (objets) à partir du <strong>même plan</strong> (classe).
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">3. Créer sa Première Classe</h2>

    <h3 class="subsection-title">Syntaxe de Base</h3>
    <pre><code class="language-csharp">public class NomDeLaClasse
{
    // Propriétés (données)
    
    // Constructeur (initialisation)
    
    // Méthodes (comportements)
}</code></pre>

    <h3 class="subsection-title">Exemple Concret : La Classe `Chien`</h3>
    <pre><code class="language-csharp">using System;

public class Chien
{
    // ========== PROPRIÉTÉS ==========
    // Ce sont les caractéristiques du chien
    
    public string Nom { get; set; }
    public string Race { get; set; }
    public int Age { get; set; }
    public double Poids { get; set; }
    
    // ========== CONSTRUCTEUR ==========
    // Méthode spéciale appelée lors de la création d'un objet
    // Elle porte le MÊME NOM que la classe
    
    public Chien(string nom, string race, int age, double poids)
    {
        Nom = nom;
        Race = race;
        Age = age;
        Poids = poids;
    }
    
    // ========== MÉTHODES ==========
    // Ce sont les actions que le chien peut faire
    
    public void Aboyer()
    {
        Console.WriteLine($"{Nom} fait : Wouf wouf !");
    }
    
    public void SePresenter()
    {
        Console.WriteLine($"Je m'appelle {Nom}, je suis un {Race} de {Age} ans.");
    }
    
    public void Manger(string nourriture)
    {
        Console.WriteLine($"{Nom} mange {nourriture}.");
        Poids += 0.1; // Le chien prend un peu de poids
    }
    
    public void Vieillir()
    {
        Age++;
        Console.WriteLine($"{Nom} a maintenant {Age} ans.");
    }
}</code></pre>
    <div class="definition-box">
        <div class="definition-title">Explications</div>
        <div class="definition-content">
            <ul>
                <li><strong>`public class Chien`</strong> : Définit le modèle.</li>
                <li><strong>Propriétés</strong> : `Nom`, `Race`, `Age`, `Poids` définissent l'état de l'objet.</li>
                <li><strong>Constructeur</strong> : `public Chien(...)` permet d'initialiser les propriétés lors de la création.</li>
                <li><strong>Méthodes</strong> : `Aboyer`, `SePresenter` définissent le comportement.</li>
            </ul>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">4. Utiliser la Classe (Créer des Objets)</h2>
    <div class="content-text">
        Une fois la classe définie, on peut créer des <strong>instances</strong> (des objets spécifiques) dans le programme principal.
    </div>
    <pre><code class="language-csharp">public class Program
{
    public static void Main()
    {
        // Créer un premier chien
        Chien monChien = new Chien("Rex", "Berger Allemand", 3, 25.5);
        
        // Utiliser les méthodes
        monChien.SePresenter();  // Affiche: Je m'appelle Rex, je suis un Berger Allemand de 3 ans.
        monChien.Aboyer();       // Affiche: Rex fait : Wouf wouf !
        monChien.Manger("des croquettes");  // Affiche: Rex mange des croquettes.
        
        // Accéder aux propriétés
        Console.WriteLine($"Poids de {monChien.Nom} : {monChien.Poids} kg");
        
        // Créer un deuxième chien (même classe, objet différent)
        Chien autreChien = new Chien("Bella", "Labrador", 5, 28.0);
        autreChien.SePresenter();
        autreChien.Aboyer();
        
        // Les deux chiens sont INDÉPENDANTS
        monChien.Vieillir();  // Rex vieillit
        Console.WriteLine($"Âge de Bella : {autreChien.Age}"); // Bella n'a pas vieilli !
    }
}</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">5. Les Propriétés en C#</h2>

    <h3 class="subsection-title">Propriétés Auto-implémentées</h3>
    <pre><code class="language-csharp">public string Nom { get; set; }</code></pre>
    <div class="content-text">
        C'est la syntaxe la plus simple. C# crée automatiquement une variable privée en arrière-plan.
        <ul>
            <li><strong>`get`</strong> : permet de <strong>lire</strong> la valeur.</li>
            <li><strong>`set`</strong> : permet de <strong>modifier</strong> la valeur.</li>
        </ul>
    </div>

    <h3 class="subsection-title">Contrôler l'Accès</h3>
    <pre><code class="language-csharp">public class CompteBancaire
{
    // Lecture publique, modification privée
    public double Solde { get; private set; }
    
    // Propriété en lecture seule (pas de set)
    public string NumeroCompte { get; }
    
    public CompteBancaire(string numero, double soldeInitial)
    {
        NumeroCompte = numero;  // On peut initialiser dans le constructeur
        Solde = soldeInitial;
    }
    
    public void Deposer(double montant)
    {
        if (montant > 0)
        {
            Solde += montant;
            Console.WriteLine($"Dépôt de {montant}€. Nouveau solde : {Solde}€");
        }
    }
}</code></pre>

    <h3 class="subsection-title">Propriétés avec Validation (Full Properties)</h3>
    <div class="content-text">Parfois, on veut valider les valeurs avant de les accepter.</div>
    <pre><code class="language-csharp">public class Personne
{
    private int _age;  // Variable privée (backing field)
    
    public int Age
    {
        get { return _age; }
        set 
        {
            if (value >= 0 && value <= 150) _age = value;
            else Console.WriteLine("Âge invalide !");
        }
    }
}</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">6. Les Constructeurs</h2>

    <h3 class="subsection-title">Constructeur par Défaut</h3>
    <div class="content-text">Si vous ne définissez AUCUN constructeur, C# en crée un automatiquement (vide).</div>
    <pre><code class="language-csharp">public class Point
{
    public int X { get; set; }
    public int Y { get; set; }
    // public Point() { } // Créé automatiquement
}</code></pre>

    <h3 class="subsection-title">Surcharge de Constructeurs</h3>
    <pre><code class="language-csharp">public class Rectangle
{
    public int Largeur { get; set; }
    public int Hauteur { get; set; }
    
    // Constructeur 1 : avec paramètres
    public Rectangle(int largeur, int hauteur)
    {
        Largeur = largeur;
        Hauteur = hauteur;
    }
    
    // Constructeur 2 : pour un carré
    public Rectangle(int cote)
    {
        Largeur = cote;
        Hauteur = cote;
    }
}</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">7. Les Méthodes</h2>

    <h3 class="subsection-title">Types de Méthodes</h3>
    <div class="content-text">
        <ul>
            <li><strong>`void`</strong> : La méthode effectue une action mais ne retourne rien.</li>
            <li><strong>Type (int, string, ...)</strong> : La méthode retourne un résultat.</li>
        </ul>
    </div>
    <pre><code class="language-csharp">public class Calculatrice
{
    public int Additionner(int a, int b)
    {
        return a + b;
    }
}</code></pre>

    <h3 class="subsection-title">Surcharge (Overloading)</h3>
    <div class="content-text">Même nom, paramètres différents.</div>
    <pre><code class="language-csharp">public class Afficheur
{
    public void Afficher(int nombre) { ... }
    public void Afficher(string texte) { ... }
}</code></pre>
</div>

<div class="concept-section">
    <h2 class="section-title">8. Les Piliers de la POO</h2>

    <h3 class="subsection-title">L'Encapsulation</h3>
    <div class="definition-box">
        <div class="definition-title">Définition</div>
        <div class="definition-content">Cacher les détails internes et exposer seulement ce qui est nécessaire.</div>
    </div>
    <div class="content-text">
        <strong>Modificateurs d'accès :</strong>
        <ul>
            <li><strong>`public`</strong> : Accessible de partout.</li>
            <li><strong>`private`</strong> : Accessible seulement dans la classe.</li>
            <li><strong>`protected`</strong> : Accessible dans la classe et ses classes dérivées.</li>
        </ul>
    </div>

    <h3 class="subsection-title">L'Héritage</h3>
    <div class="definition-box">
        <div class="definition-title">Définition</div>
        <div class="definition-content">Une classe peut hériter des propriétés et méthodes d'une autre classe.</div>
    </div>
    <pre><code class="language-csharp">// CLASSE MÈRE
public class Animal
{
    public string Nom { get; set; }
    public Animal(string nom) { Nom = nom; }
    public void Manger() { Console.WriteLine($"{Nom} mange."); }
}

// CLASSE FILLE
public class Chien : Animal  // ":" signifie "hérite de"
{
    public string Race { get; set; }
    
    // "base" appelle le constructeur de la classe mère
    public Chien(string nom, string race) : base(nom)
    {
        Race = race;
    }
    
    public void Aboyer() { Console.WriteLine("Wouf !"); }
}</code></pre>
</div>
