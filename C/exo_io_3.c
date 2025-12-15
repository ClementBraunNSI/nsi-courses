#include <stdio.h>

int main() {
    double taille;

    printf("Entrez votre taille en mètres (ex: 1.75) : ");
    scanf("%lf", &taille);

    printf("Vous mesurez %.2f mètres.\n", taille);

    return 0;
}
