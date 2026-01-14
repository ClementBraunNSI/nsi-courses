using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        // --- TEST INTRO ---
        Console.WriteLine("--- TEST INTRO ---");
        AfficherBienvenue();
        SePresenter("Alice", "Paris");
        Console.WriteLine($"Age dans 10 ans (si 20) : {AgeDans10Ans(20)}");
        
        // --- TEST CONDITIONS ---
        Console.WriteLine("\n--- TEST CONDITIONS ---");
        Console.WriteLine($"Max(5, 10) : {Max(5, 10)}");
        Console.WriteLine($"EstMotLong('Bonjour') : {EstMotLong("Bonjour")}"); // True (7)
        Console.WriteLine($"EstMotLong('Salut') : {EstMotLong("Salut")}");     // False (5)
        Console.WriteLine($"CategorieAge(10) : {CategorieAge(10)}");
        Console.WriteLine($"CategorieAge(65) : {CategorieAge(65)}");
        Console.WriteLine($"PrixTrain(10 ans, 100km) : {CalculerPrixTrain(10, 100)}€"); // 100*0.20 = 20 * 0.5 = 10

        // --- TEST BOUCLES ---
        Console.WriteLine("\n--- TEST BOUCLES ---");
        CompterJusqua(5);
        AfficherTable(5);
        Console.WriteLine($"SommeJusqua(5) : {SommeJusqua(5)}"); // 15
        Console.WriteLine($"Voyelles dans 'Oiseau' : {CompterVoyelles("Oiseau")}");
        Console.WriteLine($"Inverser 'Bonjour' : {Inverser("Bonjour")}");
        Console.WriteLine($"EstPalindrome 'kayak' : {EstPalindrome("kayak")}");

        // --- TEST LISTES ---
        Console.WriteLine("\n--- TEST LISTES ---");
        List<int> maListe = new List<int> { 1, 2, 3, 4, 5, 10, 20 };
        Console.WriteLine($"Somme : {Somme(maListe)}");
        Console.WriteLine($"Pairs : {CompterPairs(maListe)}");
        List<int> filtree = FiltrerSuperieurA(maListe, 5);
        Console.WriteLine($"Filtrés > 5 : {string.Join(", ", filtree)}");
        List<int> l2 = new List<int> { 100, 200 };
        List<int> concat = Concatener(maListe, l2);
        Console.WriteLine($"Concat : {string.Join(", ", concat)}");
    }

    // ==========================================
    // 1. INTRO (VARIABLES & AFFICHAGE)
    // ==========================================

    // Exercice 1
    public static void AfficherBienvenue()
    {
        Console.WriteLine("Bienvenue en C# !");
    }

    // Exercice 2
    public static void SePresenter(string prenom, string ville)
    {
        Console.WriteLine($"Je m'appelle {prenom} et j'habite {ville}");
    }

    // Exercice 3
    public static int AgeDans10Ans(int ageActuel)
    {
        return ageActuel + 10;
    }

    // ==========================================
    // 2. CONDITIONS
    // ==========================================

    // Exercice 1
    public static int Max(int a, int b)
    {
        if (a > b) return a;
        else return b;
    }

    // Exercice 2
    public static bool EstMotLong(string mot)
    {
        return mot.Length > 5;
    }

    // Exercice 3
    public static string CategorieAge(int age)
    {
        if (age <= 12) return "Enfant";
        else if (age <= 17) return "Ado";
        else if (age <= 59) return "Adulte";
        else return "Senior";
    }

    // Exercice 4
    public static double CalculerPrixTrain(int age, double km)
    {
        double prixBase = km * 0.20;

        // Réductions d'âge
        if (age < 12)
        {
            prixBase = prixBase * 0.50; // -50%
        }
        else if (age >= 65)
        {
            prixBase = prixBase * 0.70; // -30%
        }

        // Réduction distance
        if (km > 200)
        {
            prixBase = prixBase - 10;
        }

        // Sécurité : prix ne peut pas être négatif
        if (prixBase < 0) return 0;

        return prixBase;
    }

    // ==========================================
    // 3. BOUCLES
    // ==========================================

    // Exercice 1
    public static void CompterJusqua(int n)
    {
        for (int i = 1; i <= n; i++)
        {
            Console.WriteLine(i);
        }
    }

    // Exercice 2
    public static void AfficherTable(int n)
    {
        Console.WriteLine($"Table de {n} :");
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{n} x {i} = {n * i}");
        }
    }

    // Exercice 3
    public static int SommeJusqua(int n)
    {
        int somme = 0;
        for (int i = 1; i <= n; i++)
        {
            somme += i;
        }
        return somme;
    }

    // Exercice 4
    public static int CompterVoyelles(string texte)
    {
        int compteur = 0;
        string voyelles = "aeiouyAEIOUYéèàêâîôûëïü";
        
        foreach (char c in texte)
        {
            if (voyelles.Contains(c))
            {
                compteur++;
            }
        }
        return compteur;
    }

    // Exercice 5
    public static string Inverser(string texte)
    {
        char[] caracteres = texte.ToCharArray();
        Array.Reverse(caracteres);
        return new string(caracteres);
        
        // Version sans Array.Reverse :
        /*
        string resultat = "";
        for (int i = texte.Length - 1; i >= 0; i--)
        {
            resultat += texte[i];
        }
        return resultat;
        */
    }

    // Exercice 6
    public static bool EstPalindrome(string texte)
    {
        string inversed = Inverser(texte);
        // Comparaison insensible à la casse souvent demandée, mais ici strict :
        return texte == inversed;
    }

    // ==========================================
    // 4. LISTES
    // ==========================================

    // Exercice 1
    public static int Somme(List<int> nombres)
    {
        int total = 0;
        foreach (int n in nombres)
        {
            total += n;
        }
        return total;
    }

    // Exercice 2
    public static int CompterPairs(List<int> nombres)
    {
        int compteur = 0;
        foreach (int n in nombres)
        {
            if (n % 2 == 0)
            {
                compteur++;
            }
        }
        return compteur;
    }

    // Exercice 3
    public static List<int> FiltrerSuperieurA(List<int> nombres, int seuil)
    {
        List<int> result = new List<int>();
        foreach (int n in nombres)
        {
            if (n > seuil)
            {
                result.Add(n);
            }
        }
        return result;
    }

    // Exercice 4
    public static List<int> Concatener(List<int> l1, List<int> l2)
    {
        List<int> result = new List<int>();
        
        // Ajouter tous les éléments de l1
        foreach (int n in l1)
        {
            result.Add(n);
        }
        
        // Ajouter tous les éléments de l2
        foreach (int n in l2)
        {
            result.Add(n);
        }
        
        // Ou plus simplement :
        // result.AddRange(l1);
        // result.AddRange(l2);
        
        return result;
    }
}
