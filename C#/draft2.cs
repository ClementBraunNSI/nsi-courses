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

    public static void Main(string[] args)
    {
        // Création d'une instance de Voiture
        Voiture maVoiture = new Voiture("AB-123-CD", "Toyota", "Corolla", 2020, "Rouge");

        // Affichage des informations de la voiture
        Console.WriteLine(maVoiture.ToString());

        // Démarrer la voiture
        maVoiture.Demarrer();

        Console.WriteLine("La voiture est-elle démarrée ? " + maVoiture.EstDemarre);

        // Arrêter la voiture
        maVoiture.Arreter();
    }
}