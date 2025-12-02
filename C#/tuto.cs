
public enum Espece
{
    Renard_roux,
    Renard_polaire,
    Renard_des_sables
}

public class Renard
{
    private string name;
    private int age;
    private string id;
    private Espece couleur;

    public Renard(string name, int age, string id, Espece couleur)
    {
        this.name = name;
        this.age = age;
        this.id = id;
        this.couleur = couleur;
    }

    public void affichage()
    {
        Console.WriteLine("Nom: " + name);
        Console.WriteLine("Âge: " + age);
        Console.WriteLine("ID: " + id);
        Console.WriteLine("Couleur: " + couleur);
    }
}
public class test{
    public static void Main(string[] args){
        Renard renard1 = new Renard("Foxy", 3, "ROO1", Espece.Renard_roux);
        renard1.affichage();
    }
}