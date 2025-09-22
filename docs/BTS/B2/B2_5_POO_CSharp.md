# 🏗️ B2.5 - Programmation Orientée Objet en C#

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
- ✅ Comprendre les concepts fondamentaux de la POO
- ✅ Créer et utiliser des classes et objets
- ✅ Maîtriser l'encapsulation avec les propriétés
- ✅ Implémenter l'héritage et le polymorphisme
- ✅ Utiliser les interfaces et classes abstraites
- ✅ Appliquer les principes SOLID

---

<h3 class="custom-h3">🎯 Introduction à la POO</h3>

<div class="concept-card">
<span class="concept-icon">🏗️</span>
<div class="concept-name">Qu'est-ce que la Programmation Orientée Objet ?</div>
<div class="concept-description">
La POO est un paradigme de programmation qui organise le code autour d'objets plutôt que de fonctions. Un objet combine des données (attributs) et des comportements (méthodes) dans une seule entité cohérente.
</div>
</div>

<div class="highlight-fact">
<strong>🔑 Les 4 piliers de la POO :</strong>
<ul>
<li><strong>Encapsulation :</strong> Regrouper données et méthodes, contrôler l'accès</li>
<li><strong>Héritage :</strong> Créer de nouvelles classes basées sur des classes existantes</li>
<li><strong>Polymorphisme :</strong> Utiliser une interface commune pour différents types</li>
<li><strong>Abstraction :</strong> Simplifier la complexité en cachant les détails</li>
</ul>
</div>

<h4 class="custom-h4">🌍 Analogie du monde réel</h4>

<div class="code-example">
```
🚗 Voiture (Classe)
├── Attributs : marque, modèle, couleur, vitesse
├── Méthodes : démarrer(), accélérer(), freiner(), klaxonner()
└── Objets : maVoiture, voitureDeJean, voitureDeMarie

🏠 Maison (Classe)  
├── Attributs : adresse, superficie, nombrePièces
├── Méthodes : ouvrir(), fermer(), allumerLumière()
└── Objets : maMaison, maisonVoisin, maisonGrandMère
```
</div>

---

<h3 class="custom-h3">🏗️ Classes et Objets</h3>

<h4 class="custom-h4">📝 Création d'une classe simple</h4>

<div class="code-example">
```csharp
// Définition d'une classe Personne
public class Personne
{
    // Champs (attributs privés)
    private string nom;
    private string prenom;
    private int age;
    private string email;
    
    // Constructeur par défaut
    public Personne()
    {
        nom = "";
        prenom = "";
        age = 0;
        email = "";
    }
    
    // Constructeur avec paramètres
    public Personne(string nom, string prenom, int age, string email)
    {
        this.nom = nom;
        this.prenom = prenom;
        this.age = age;
        this.email = email;
    }
    
    // Méthodes publiques
    public void SePresenter()
    {
        Console.WriteLine($"Bonjour, je suis {prenom} {nom}, j'ai {age} ans.");
    }
    
    public void Vieillir()
    {
        age++;
        Console.WriteLine($"{prenom} a maintenant {age} ans.");
    }
    
    public bool EstMajeur()
    {
        return age >= 18;
    }
    
    // Méthode pour afficher les informations
    public void AfficherInfos()
    {
        Console.WriteLine($"Nom : {nom}");
        Console.WriteLine($"Prénom : {prenom}");
        Console.WriteLine($"Âge : {age} ans");
        Console.WriteLine($"Email : {email}");
        Console.WriteLine($"Statut : {(EstMajeur() ? "Majeur" : "Mineur")}");
    }
}

// Utilisation de la classe
class Program
{
    static void Main(string[] args)
    {
        // Création d'objets (instances)
        Personne personne1 = new Personne();
        Personne personne2 = new Personne("Dupont", "Jean", 25, "jean.dupont@email.com");
        
        // Utilisation des méthodes
        personne2.SePresenter();
        personne2.AfficherInfos();
        personne2.Vieillir();
        
        Console.WriteLine($"Jean est-il majeur ? {personne2.EstMajeur()}");
    }
}
```
</div>

<h4 class="custom-h4">🔐 Encapsulation avec les propriétés</h4>

<div class="code-example">
```csharp
public class CompteBancaire
{
    // Champs privés
    private string numeroCompte;
    private double solde;
    private string titulaire;
    private DateTime dateOuverture;
    
    // Propriétés avec accesseurs
    public string NumeroCompte
    {
        get { return numeroCompte; }
        private set { numeroCompte = value; } // Seule la classe peut modifier
    }
    
    public double Solde
    {
        get { return solde; }
        private set { solde = value; }
    }
    
    public string Titulaire
    {
        get { return titulaire; }
        set 
        { 
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("Le nom du titulaire ne peut pas être vide");
            titulaire = value; 
        }
    }
    
    // Propriété auto-implémentée
    public string TypeCompte { get; set; }
    
    // Propriété calculée (lecture seule)
    public int AnneeOuverture
    {
        get { return dateOuverture.Year; }
    }
    
    // Constructeur
    public CompteBancaire(string titulaire, string typeCompte = "Courant")
    {
        this.numeroCompte = GenererNumeroCompte();
        this.titulaire = titulaire;
        this.TypeCompte = typeCompte;
        this.solde = 0;
        this.dateOuverture = DateTime.Now;
    }
    
    // Méthodes publiques
    public bool Deposer(double montant)
    {
        if (montant <= 0)
        {
            Console.WriteLine("Le montant doit être positif");
            return false;
        }
        
        solde += montant;
        Console.WriteLine($"Dépôt de {montant:C} effectué. Nouveau solde : {solde:C}");
        return true;
    }
    
    public bool Retirer(double montant)
    {
        if (montant <= 0)
        {
            Console.WriteLine("Le montant doit être positif");
            return false;
        }
        
        if (montant > solde)
        {
            Console.WriteLine("Solde insuffisant");
            return false;
        }
        
        solde -= montant;
        Console.WriteLine($"Retrait de {montant:C} effectué. Nouveau solde : {solde:C}");
        return true;
    }
    
    public void AfficherReleve()
    {
        Console.WriteLine("=== RELEVÉ DE COMPTE ===");
        Console.WriteLine($"Numéro : {NumeroCompte}");
        Console.WriteLine($"Titulaire : {Titulaire}");
        Console.WriteLine($"Type : {TypeCompte}");
        Console.WriteLine($"Solde : {Solde:C}");
        Console.WriteLine($"Ouvert en : {AnneeOuverture}");
        Console.WriteLine("========================");
    }
    
    // Méthode privée
    private string GenererNumeroCompte()
    {
        Random random = new Random();
        return $"FR{random.Next(10, 100)}{random.Next(1000, 10000)}{random.Next(100000, 1000000)}";
    }
}

// Utilisation
static void Main(string[] args)
{
    CompteBancaire compte = new CompteBancaire("Alice Martin", "Épargne");
    
    compte.Deposer(1000);
    compte.Retirer(250);
    compte.AfficherReleve();
    
    // Accès aux propriétés
    Console.WriteLine($"Titulaire : {compte.Titulaire}");
    Console.WriteLine($"Solde : {compte.Solde}");
    
    // compte.Solde = 5000; // ❌ Erreur : propriété en lecture seule
}
```
</div>

---

<h3 class="custom-h3">🧬 Héritage</h3>

<h4 class="custom-h4">👨‍👩‍👧‍👦 Héritage simple</h4>

<div class="inheritance-diagram">
<strong>Hiérarchie d'héritage</strong><br>
🧑 Personne (classe de base)<br>
├── 👨‍💼 Employe<br>
│   ├── 👨‍💻 Developpeur<br>
│   └── 👨‍💼 Manager<br>
└── 🎓 Etudiant
</div>

<div class="code-example">
```csharp
// Classe de base (parent)
public class Personne
{
    protected string nom;
    protected string prenom;
    protected int age;
    
    public string Nom 
    { 
        get { return nom; } 
        set { nom = value; } 
    }
    
    public string Prenom 
    { 
        get { return prenom; } 
        set { prenom = value; } 
    }
    
    public int Age 
    { 
        get { return age; } 
        set { age = value; } 
    }
    
    // Constructeur
    public Personne(string nom, string prenom, int age)
    {
        this.nom = nom;
        this.prenom = prenom;
        this.age = age;
    }
    
    // Méthode virtuelle (peut être redéfinie)
    public virtual void SePresenter()
    {
        Console.WriteLine($"Je suis {prenom} {nom}, {age} ans.");
    }
    
    public virtual void AfficherInfos()
    {
        Console.WriteLine($"Nom : {nom}");
        Console.WriteLine($"Prénom : {prenom}");
        Console.WriteLine($"Âge : {age} ans");
    }
}

// Classe dérivée (enfant)
public class Employe : Personne
{
    protected string poste;
    protected double salaire;
    protected DateTime dateEmbauche;
    
    public string Poste 
    { 
        get { return poste; } 
        set { poste = value; } 
    }
    
    public double Salaire 
    { 
        get { return salaire; } 
        set { salaire = value; } 
    }
    
    // Constructeur qui appelle le constructeur parent
    public Employe(string nom, string prenom, int age, string poste, double salaire) 
        : base(nom, prenom, age)
    {
        this.poste = poste;
        this.salaire = salaire;
        this.dateEmbauche = DateTime.Now;
    }
    
    // Redéfinition (override) de la méthode parent
    public override void SePresenter()
    {
        Console.WriteLine($"Je suis {prenom} {nom}, {age} ans, {poste} dans l'entreprise.");
    }
    
    public override void AfficherInfos()
    {
        base.AfficherInfos(); // Appel de la méthode parent
        Console.WriteLine($"Poste : {poste}");
        Console.WriteLine($"Salaire : {salaire:C}");
        Console.WriteLine($"Embauché le : {dateEmbauche:dd/MM/yyyy}");
    }
    
    // Nouvelle méthode spécifique à Employe
    public void Travailler()
    {
        Console.WriteLine($"{prenom} travaille en tant que {poste}.");
    }
    
    public virtual double CalculerPrimeAnnuelle()
    {
        return salaire * 0.1; // 10% du salaire
    }
}

// Classe dérivée de Employe
public class Developpeur : Employe
{
    private List<string> langagesProgrammation;
    private string specialite;
    
    public List<string> LangagesProgrammation 
    { 
        get { return langagesProgrammation; } 
    }
    
    public string Specialite 
    { 
        get { return specialite; } 
        set { specialite = value; } 
    }
    
    public Developpeur(string nom, string prenom, int age, double salaire, string specialite) 
        : base(nom, prenom, age, "Développeur", salaire)
    {
        this.specialite = specialite;
        this.langagesProgrammation = new List<string>();
    }
    
    public override void SePresenter()
    {
        Console.WriteLine($"Je suis {prenom} {nom}, développeur {specialite} de {age} ans.");
    }
    
    public override void AfficherInfos()
    {
        base.AfficherInfos();
        Console.WriteLine($"Spécialité : {specialite}");
        Console.WriteLine($"Langages : {string.Join(", ", langagesProgrammation)}");
    }
    
    public void AjouterLangage(string langage)
    {
        if (!langagesProgrammation.Contains(langage))
        {
            langagesProgrammation.Add(langage);
            Console.WriteLine($"{langage} ajouté aux compétences de {prenom}");
        }
    }
    
    public void Programmer()
    {
        Console.WriteLine($"{prenom} programme en {specialite}.");
    }
    
    // Redéfinition du calcul de prime
    public override double CalculerPrimeAnnuelle()
    {
        double primeBase = base.CalculerPrimeAnnuelle();
        double bonusLangages = langagesProgrammation.Count * 500; // 500€ par langage
        return primeBase + bonusLangages;
    }
}

// Autre classe dérivée
public class Etudiant : Personne
{
    private string ecole;
    private string filiere;
    private int anneeEtude;
    
    public string Ecole { get; set; }
    public string Filiere { get; set; }
    public int AnneeEtude { get; set; }
    
    public Etudiant(string nom, string prenom, int age, string ecole, string filiere, int anneeEtude) 
        : base(nom, prenom, age)
    {
        this.ecole = ecole;
        this.filiere = filiere;
        this.anneeEtude = anneeEtude;
    }
    
    public override void SePresenter()
    {
        Console.WriteLine($"Je suis {prenom} {nom}, étudiant en {filiere} (année {anneeEtude}) à {ecole}.");
    }
    
    public override void AfficherInfos()
    {
        base.AfficherInfos();
        Console.WriteLine($"École : {ecole}");
        Console.WriteLine($"Filière : {filiere}");
        Console.WriteLine($"Année : {anneeEtude}");
    }
    
    public void Etudier()
    {
        Console.WriteLine($"{prenom} étudie {filiere}.");
    }
}

// Utilisation
static void Main(string[] args)
{
    // Création d'objets de différents types
    Personne personne = new Personne("Martin", "Paul", 30);
    Employe employe = new Employe("Durand", "Marie", 28, "Comptable", 35000);
    Developpeur dev = new Developpeur("Moreau", "Alex", 26, 45000, "Full-Stack");
    Etudiant etudiant = new Etudiant("Petit", "Julie", 20, "Université Paris", "Informatique", 2);
    
    // Ajout de compétences au développeur
    dev.AjouterLangage("C#");
    dev.AjouterLangage("JavaScript");
    dev.AjouterLangage("Python");
    
    // Polymorphisme : même méthode, comportements différents
    List<Personne> personnes = new List<Personne> { personne, employe, dev, etudiant };
    
    foreach (Personne p in personnes)
    {
        p.SePresenter(); // Appel polymorphe
        p.AfficherInfos();
        Console.WriteLine($"Prime annuelle : {(p is Employe emp ? emp.CalculerPrimeAnnuelle().ToString("C") : "N/A")}");
        Console.WriteLine("---");
    }
}
```
</div>

---

<h3 class="custom-h3">🎭 Polymorphisme</h3>

<h4 class="custom-h4">🔄 Polymorphisme par héritage</h4>

<div class="code-example">
```csharp
// Classe de base abstraite
public abstract class Animal
{
    protected string nom;
    protected int age;
    
    public string Nom { get; set; }
    public int Age { get; set; }
    
    public Animal(string nom, int age)
    {
        this.nom = nom;
        this.age = age;
    }
    
    // Méthode abstraite (doit être implémentée par les classes dérivées)
    public abstract void FaireDuBruit();
    
    // Méthode virtuelle (peut être redéfinie)
    public virtual void SeDeplacer()
    {
        Console.WriteLine($"{nom} se déplace.");
    }
    
    // Méthode concrète
    public void Dormir()
    {
        Console.WriteLine($"{nom} dort paisiblement.");
    }
}

public class Chien : Animal
{
    private string race;
    
    public string Race { get; set; }
    
    public Chien(string nom, int age, string race) : base(nom, age)
    {
        this.race = race;
    }
    
    public override void FaireDuBruit()
    {
        Console.WriteLine($"{nom} aboie : Woof! Woof!");
    }
    
    public override void SeDeplacer()
    {
        Console.WriteLine($"{nom} court joyeusement.");
    }
    
    public void Jouer()
    {
        Console.WriteLine($"{nom} joue avec une balle.");
    }
}

public class Chat : Animal
{
    private string couleur;
    
    public string Couleur { get; set; }
    
    public Chat(string nom, int age, string couleur) : base(nom, age)
    {
        this.couleur = couleur;
    }
    
    public override void FaireDuBruit()
    {
        Console.WriteLine($"{nom} miaule : Miaou! Miaou!");
    }
    
    public override void SeDeplacer()
    {
        Console.WriteLine($"{nom} se faufile silencieusement.");
    }
    
    public void Chasser()
    {
        Console.WriteLine($"{nom} chasse une souris.");
    }
}

public class Oiseau : Animal
{
    private double envergure;
    
    public double Envergure { get; set; }
    
    public Oiseau(string nom, int age, double envergure) : base(nom, age)
    {
        this.envergure = envergure;
    }
    
    public override void FaireDuBruit()
    {
        Console.WriteLine($"{nom} chante : Cui cui!");
    }
    
    public override void SeDeplacer()
    {
        Console.WriteLine($"{nom} vole gracieusement.");
    }
    
    public void Voler()
    {
        Console.WriteLine($"{nom} vole avec une envergure de {envergure}m.");
    }
}

// Utilisation du polymorphisme
static void Main(string[] args)
{
    // Création d'un zoo polymorphe
    List<Animal> zoo = new List<Animal>
    {
        new Chien("Rex", 5, "Berger Allemand"),
        new Chat("Minou", 3, "Gris"),
        new Oiseau("Tweety", 2, 0.3),
        new Chien("Buddy", 7, "Golden Retriever"),
        new Chat("Félix", 4, "Noir et blanc")
    };
    
    Console.WriteLine("=== CONCERT DU ZOO ===");
    foreach (Animal animal in zoo)
    {
        animal.FaireDuBruit(); // Polymorphisme !
    }
    
    Console.WriteLine("\n=== HEURE DE L'EXERCICE ===");
    foreach (Animal animal in zoo)
    {
        animal.SeDeplacer(); // Polymorphisme !
    }
    
    Console.WriteLine("\n=== ACTIVITÉS SPÉCIFIQUES ===");
    foreach (Animal animal in zoo)
    {
        // Vérification de type et casting
        if (animal is Chien chien)
        {
            chien.Jouer();
        }
        else if (animal is Chat chat)
        {
            chat.Chasser();
        }
        else if (animal is Oiseau oiseau)
        {
            oiseau.Voler();
        }
    }
    
    Console.WriteLine("\n=== HEURE DU DODO ===");
    foreach (Animal animal in zoo)
    {
        animal.Dormir(); // Méthode commune
    }
}
```
</div>

<h4 class="custom-h4">🔌 Interfaces</h4>

<div class="code-example">
```csharp
// Interface pour les objets volants
public interface IVolant
{
    double AltitudeMax { get; }
    void Decoller();
    void Atterrir();
    void Voler(double altitude);
}

// Interface pour les véhicules
public interface IVehicule
{
    string Marque { get; set; }
    string Modele { get; set; }
    int AnneeProduction { get; set; }
    bool EstDemarre { get; }
    
    void Demarrer();
    void Arreter();
    void Accelerer();
    void Freiner();
}

// Interface pour les objets électriques
public interface IElectrique
{
    double NiveauBatterie { get; }
    double AutonomieKm { get; }
    
    void Charger();
    bool EstCharge();
}

// Classe qui implémente plusieurs interfaces
public class Avion : IVolant, IVehicule
{
    public string Marque { get; set; }
    public string Modele { get; set; }
    public int AnneeProduction { get; set; }
    public bool EstDemarre { get; private set; }
    public double AltitudeMax { get; private set; }
    
    private double altitudeActuelle;
    private bool estEnVol;
    
    public Avion(string marque, string modele, int annee, double altitudeMax)
    {
        Marque = marque;
        Modele = modele;
        AnneeProduction = annee;
        AltitudeMax = altitudeMax;
        EstDemarre = false;
        altitudeActuelle = 0;
        estEnVol = false;
    }
    
    // Implémentation de IVehicule
    public void Demarrer()
    {
        EstDemarre = true;
        Console.WriteLine($"{Marque} {Modele} : Moteurs démarrés !");
    }
    
    public void Arreter()
    {
        if (estEnVol)
        {
            Console.WriteLine("Impossible d'arrêter en vol !");
            return;
        }
        EstDemarre = false;
        Console.WriteLine($"{Marque} {Modele} : Moteurs arrêtés.");
    }
    
    public void Accelerer()
    {
        if (EstDemarre)
            Console.WriteLine($"{Marque} {Modele} accélère sur la piste.");
    }
    
    public void Freiner()
    {
        Console.WriteLine($"{Marque} {Modele} freine.");
    }
    
    // Implémentation de IVolant
    public void Decoller()
    {
        if (!EstDemarre)
        {
            Console.WriteLine("Démarrez d'abord les moteurs !");
            return;
        }
        
        estEnVol = true;
        altitudeActuelle = 1000;
        Console.WriteLine($"{Marque} {Modele} décolle ! Altitude : {altitudeActuelle}m");
    }
    
    public void Atterrir()
    {
        if (!estEnVol)
        {
            Console.WriteLine("L'avion est déjà au sol !");
            return;
        }
        
        estEnVol = false;
        altitudeActuelle = 0;
        Console.WriteLine($"{Marque} {Modele} atterrit en douceur.");
    }
    
    public void Voler(double altitude)
    {
        if (!estEnVol)
        {
            Console.WriteLine("L'avion doit d'abord décoller !");
            return;
        }
        
        if (altitude > AltitudeMax)
        {
            Console.WriteLine($"Altitude maximale dépassée ! Max : {AltitudeMax}m");
            return;
        }
        
        altitudeActuelle = altitude;
        Console.WriteLine($"{Marque} {Modele} vole à {altitudeActuelle}m d'altitude.");
    }
}

// Classe voiture électrique
public class VoitureElectrique : IVehicule, IElectrique
{
    public string Marque { get; set; }
    public string Modele { get; set; }
    public int AnneeProduction { get; set; }
    public bool EstDemarre { get; private set; }
    public double NiveauBatterie { get; private set; }
    public double AutonomieKm { get; private set; }
    
    private double vitesse;
    
    public VoitureElectrique(string marque, string modele, int annee, double autonomie)
    {
        Marque = marque;
        Modele = modele;
        AnneeProduction = annee;
        AutonomieKm = autonomie;
        NiveauBatterie = 100;
        EstDemarre = false;
        vitesse = 0;
    }
    
    // Implémentation de IVehicule
    public void Demarrer()
    {
        if (NiveauBatterie <= 0)
        {
            Console.WriteLine("Batterie vide ! Rechargez d'abord.");
            return;
        }
        
        EstDemarre = true;
        Console.WriteLine($"{Marque} {Modele} démarre silencieusement ⚡");
    }
    
    public void Arreter()
    {
        EstDemarre = false;
        vitesse = 0;
        Console.WriteLine($"{Marque} {Modele} s'arrête.");
    }
    
    public void Accelerer()
    {
        if (!EstDemarre)
        {
            Console.WriteLine("Démarrez d'abord la voiture !");
            return;
        }
        
        vitesse += 10;
        NiveauBatterie -= 0.5;
        Console.WriteLine($"{Marque} {Modele} accélère à {vitesse} km/h. Batterie : {NiveauBatterie:F1}%");
    }
    
    public void Freiner()
    {
        vitesse = Math.Max(0, vitesse - 15);
        NiveauBatterie += 0.2; // Récupération d'énergie
        Console.WriteLine($"{Marque} {Modele} freine à {vitesse} km/h. Batterie : {NiveauBatterie:F1}%");
    }
    
    // Implémentation de IElectrique
    public void Charger()
    {
        Console.WriteLine($"Chargement de {Marque} {Modele}...");
        NiveauBatterie = 100;
        Console.WriteLine("Chargement terminé ! Batterie : 100%");
    }
    
    public bool EstCharge()
    {
        return NiveauBatterie > 80;
    }
}

// Utilisation des interfaces
static void Main(string[] args)
{
    // Création d'objets
    Avion boeing = new Avion("Boeing", "737", 2020, 12000);
    VoitureElectrique tesla = new VoitureElectrique("Tesla", "Model 3", 2023, 500);
    
    // Utilisation polymorphe via les interfaces
    List<IVehicule> vehicules = new List<IVehicule> { boeing, tesla };
    
    Console.WriteLine("=== DÉMARRAGE DES VÉHICULES ===");
    foreach (IVehicule vehicule in vehicules)
    {
        vehicule.Demarrer();
        vehicule.Accelerer();
    }
    
    Console.WriteLine("\n=== OBJETS VOLANTS ===");
    if (boeing is IVolant avionVolant)
    {
        avionVolant.Decoller();
        avionVolant.Voler(8000);
        avionVolant.Atterrir();
    }
    
    Console.WriteLine("\n=== VÉHICULES ÉLECTRIQUES ===");
    if (tesla is IElectrique vehiculeElectrique)
    {
        Console.WriteLine($"Autonomie : {vehiculeElectrique.AutonomieKm} km");
        Console.WriteLine($"Chargé : {vehiculeElectrique.EstCharge()}");
        
        // Simulation de conduite
        for (int i = 0; i < 10; i++)
        {
            tesla.Accelerer();
        }
        
        vehiculeElectrique.Charger();
    }
}
```
</div>

---

<h3 class="custom-h3">🎯 Exercices pratiques</h3>

<div class="exercise-box">
<h4>🏋️ Exercice 1 : Système de gestion de bibliothèque</h4>

Créez un système de gestion de bibliothèque avec :

1. **Classe abstraite `Document`** avec :
   - Propriétés : Titre, Auteur, AnneePublication, EstEmprunte
   - Méthodes abstraites : Emprunter(), Retourner()
   - Méthode virtuelle : AfficherInfos()

2. **Classes dérivées :**
   - `Livre` : ISBN, NombrePages, Genre
   - `Magazine` : NumeroEdition, Periodicite
   - `DVD` : Duree, Genre, Realisateur

3. **Interface `IEmpruntable`** avec :
   - DateEmprunt, DateRetourPrevue
   - CalculerRetard(), CalculerAmende()

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 2 : Jeu de rôle (RPG)</h4>

Créez un système de personnages pour un jeu de rôle :

1. **Classe de base `Personnage`** :
   - Nom, Niveau, PointsVie, PointsMana
   - Méthodes : Attaquer(), RecevoirDegats(), Guerir()

2. **Classes spécialisées :**
   - `Guerrier` : Force, Armure, AttaqueEpee()
   - `Mage` : Intelligence, LancerSort(), RegenereMana()
   - `Archer` : Agilite, Precision, TirerFleche()

3. **Interfaces :**
   - `ICombattant` : Attaquer(), Defendre()
   - `IMagique` : LancerSort(), ConsommerMana()

```csharp
// Votre code ici
```
</div>

<div class="exercise-box">
<h4>🏋️ Exercice 3 : Système de formes géométriques</h4>

Implémentez un système de calcul de formes :

1. **Classe abstraite `Forme`** :
   - Propriétés : Couleur, Position
   - Méthodes abstraites : CalculerAire(), CalculerPerimetre()
   - Méthode virtuelle : Dessiner()

2. **Classes concrètes :**
   - `Rectangle`, `Cercle`, `Triangle`
   - Chaque classe avec ses propriétés spécifiques

3. **Interface `IRedimensionnable`** :
   - Redimensionner(double facteur)

```csharp
// Votre code ici
```
</div>

---

<h3 class="custom-h3">🏆 Principes SOLID</h3>

<div class="concept-card">
<span class="concept-icon">🎯</span>
<div class="concept-name">Les 5 principes SOLID</div>
<div class="concept-description">

**S - Single Responsibility Principle (SRP)**
Une classe ne doit avoir qu'une seule raison de changer.

**O - Open/Closed Principle (OCP)**  
Les classes doivent être ouvertes à l'extension, fermées à la modification.

**L - Liskov Substitution Principle (LSP)**
Les objets dérivés doivent pouvoir remplacer leurs objets de base.

**I - Interface Segregation Principle (ISP)**
Les clients ne doivent pas dépendre d'interfaces qu'ils n'utilisent pas.

**D - Dependency Inversion Principle (DIP)**
Dépendre d'abstractions, pas de concrétions.

</div>
</div>

<div class="code-example">
```csharp
// Exemple d'application des principes SOLID

// SRP : Chaque classe a une responsabilité unique
public class Utilisateur
{
    public string Nom { get; set; }
    public string Email { get; set; }
}

public class ValidateurUtilisateur
{
    public bool Valider(Utilisateur utilisateur)
    {
        return !string.IsNullOrEmpty(utilisateur.Nom) && 
               !string.IsNullOrEmpty(utilisateur.Email);
    }
}

public class ServiceEmail
{
    public void EnvoyerEmail(string destinataire, string message)
    {
        // Logique d'envoi d'email
    }
}

// OCP : Extensible sans modification
public abstract class CalculateurPrix
{
    public abstract double Calculer(double prixBase);
}

public class CalculateurPrixStandard : CalculateurPrix
{
    public override double Calculer(double prixBase)
    {
        return prixBase;
    }
}

public class CalculateurPrixAvecRemise : CalculateurPrix
{
    private double pourcentageRemise;
    
    public CalculateurPrixAvecRemise(double remise)
    {
        pourcentageRemise = remise;
    }
    
    public override double Calculer(double prixBase)
    {
        return prixBase * (1 - pourcentageRemise / 100);
    }
}

// ISP : Interfaces spécifiques
public interface ILisible
{
    string Lire();
}

public interface IEcrivable
{
    void Ecrire(string contenu);
}

public interface IExecutable
{
    void Executer();
}

// DIP : Dépendance d'abstraction
public interface IRepository<T>
{
    void Ajouter(T item);
    T Obtenir(int id);
    List<T> ObtenirTous();
}

public class ServiceUtilisateur
{
    private readonly IRepository<Utilisateur> repository;
    
    public ServiceUtilisateur(IRepository<Utilisateur> repo)
    {
        repository = repo; // Injection de dépendance
    }
    
    public void CreerUtilisateur(Utilisateur utilisateur)
    {
        repository.Ajouter(utilisateur);
    }
}
```
</div>

---

<h3 class="custom-h3">📚 Points clés à retenir</h3>

<div class="highlight-fact">
<strong>🎯 Résumé du chapitre :</strong>
<ul>
<li><strong>Classes et objets :</strong> Modélisation du monde réel en code</li>
<li><strong>Encapsulation :</strong> Protection des données avec propriétés</li>
<li><strong>Héritage :</strong> Réutilisation et spécialisation de code</li>
<li><strong>Polymorphisme :</strong> Même interface, comportements différents</li>
<li><strong>Interfaces :</strong> Contrats que les classes doivent respecter</li>
<li><strong>SOLID :</strong> Principes pour un code maintenable et extensible</li>
</ul>
</div>

<div class="warning-box">
<strong>⚠️ Erreurs courantes à éviter :</strong>
<ul>
<li><strong>Héritage abusif :</strong> Préférer la composition quand approprié</li>
<li><strong>Classes trop grosses :</strong> Respecter le principe de responsabilité unique</li>
<li><strong>Couplage fort :</strong> Utiliser les interfaces pour découpler</li>
<li><strong>Pas de validation :</strong> Toujours valider dans les propriétés</li>
</ul>
</div>

---

## 🔗 Liens utiles

- [Classes et objets en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/classes-and-structs/)
- [Héritage en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/classes-and-structs/inheritance)
- [Interfaces en C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/interfaces/)
- [Principes SOLID](https://docs.microsoft.com/fr-fr/dotnet/architecture/modern-web-apps-azure/architectural-principles)

---

**Étape précédente :** [B2.4 - Fonctions et méthodes](B2_4_Fonctions_methodes.md)  
**Prochaine étape :** [B2.6 - Projets d'application](B2_6_Projets_applications.md)