#include <stdio.h>

int main() {
    int a, b;
    int choix;

    printf("Entrez deux nombres : ");
    scanf("%d %d", &a, &b);

    printf("1. Addition\n2. Soustraction\n3. Multiplication\nVotre choix ? ");
    scanf("%d", &choix);

    if (choix == 1) {
        printf("Résultat : %d\n", a + b);
    } else if (choix == 2) {
        printf("Résultat : %d\n", a - b);
    } else if (choix == 3) {
        printf("Résultat : %d\n", a * b);
    } else {
        printf("Choix invalide.\n");
    }

    return 0;
}
