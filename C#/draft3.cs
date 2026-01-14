using System;
using System.Security.Cryptography.X509Certificates;

public class Program{
    public static void Afficher_Bienvenue(){
        Console.WriteLine("Bienvenue en C#");
    }

    public static void SePresenter(string prenom, string ville)
    {
        Console.WriteLine($"Je m'appelle {prenom} et j'habite à {ville}");
    }

    public static int AgeDans10Ans(int ageActuel)
    {
        return ageActuel+10;
    }

    public static int Maximum(int a, int b)
    {
        if (a > b)
        {
            return a;
        }
        else
        {
            return b;
        }
    }

    public static bool EstMotLong(string mot)
    {
        /*return mot.Length > 5;*/
        if (mot.Length > 5)
        {
            return true;
        }
        else
        {
            return false;
        }

    }

    public static string CategorieAge(int age)
    {
        if(age >= 59)
        {
            return "Senior";
        }
        else if (age >= 17)
        {
            return "Adulte";
        }
        else if (age >= 12)
        {
            return "Ado";
        }
        else
        {
            return "Enfant";
        }

    }

    public static double CalculerPrixTrain(int age, double km)
    {
        double prix_base = km * 0.2;

        if(age >= 65)
        {
            prix_base = prix_base * 0.7;
        }
        else if(age < 12)
        {
            prix_base = prix_base*0.5;
        }

        if(km > 200)
        {
            prix_base = prix_base - 10;
        }

        return prix_base;
    }

    public static void CompterJusqua(int n)
    {
        for( int i = 0; i <= n ; i++)
        {
            Console.WriteLine(i);
        }
    }

    public static void AfficherTable(int n)
    {
        for (int i = 0; i <= 10; i++)
        {
            Console.WriteLine($"{n} x {i} = {n*i}");
        }
    }

    public static int SommeJusqua(int n)
    {
        int somme = 0;
        for (int i = 0; i <= n ; i++)
        {
            somme += i;
        }
        return somme;
    }

    public static int CompterVoyelles(string mot)
    {   
        int compteur = 0;
        string voyelles = "AEIOUYaeiouy";
        foreach (char c in mot)
        {
            if (voyelles.Contains(c)){
                compteur++;
            }
        }
        return compteur;
    }

    public static string Inverser(string texte)
    {
        string res = "";
        for (int i = texte.Length - 1 ; i >= 0; i--)
        {
            res+= texte[i];
        }
        return res;
    }

    public static bool estPremier(int n)
    {
        int nb_diviseurs = 0;

        if (n < 2)
        {
            return false;
        }
        for (int i = 2 ; i < n; i++)
        {
            if ((n % i) == 0)
            {
                nb_diviseurs++;
            }
        }
        return nb_diviseurs == 0;
    }

    public static bool Palindrome(string mot)
    {
        return Inverser(mot) == mot;
    }

    public static int SommeListe(List<int> nombres)
    {
        int somme = 0;
        foreach (int c in nombres)
        {
            somme += c;
        }
        return somme;
    }

    public static List<int> FiltrerSuperieurA(List<int> liste, int seuil)
    {
        List<int> resultat = new List<int>();
        foreach (int c in liste)
        {
            if (c > seuil)
            {
                resultat.Add(c);
            }
        }
        return resultat;
    }

    public static List<int> Concatener(List<int>l1, List<int> l2)
    {
        List<int> resultat = new List<int>();
        resultat.AddRange(l1);
        resultat.AddRange(l2);
        return resultat;
    }

    public static void Main(){
        Afficher_Bienvenue();
        SePresenter("Clément", "Villeneuve d'Ascq");
        Console.WriteLine(AgeDans10Ans(25));
        Console.WriteLine(Maximum(10,15));
        Console.WriteLine(EstMotLong("Coucou"));
        Console.WriteLine(CategorieAge(75));
        Console.WriteLine(CalculerPrixTrain(69,50));
        CompterJusqua(100);
        AfficherTable(10);
        Console.WriteLine(SommeJusqua(5));
        Console.WriteLine(CompterVoyelles("Renard"));
        Console.WriteLine(Inverser("Renard"));

        Console.WriteLine(estPremier(5));

        Console.WriteLine(Palindrome("yakak"));
        List<int> maListe = new List<int>{19,20,21,22};
        Console.WriteLine(SommeListe(maListe));

        Console.WriteLine(string.Join(",",FiltrerSuperieurA(maListe, 19)));
        Console.WriteLine(string.Join(" ", Concatener(maListe, maListe)));
    }

    
}