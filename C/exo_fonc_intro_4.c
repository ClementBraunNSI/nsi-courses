#include <stdio.h>

// Fonction qui calcule le carré d'un nombre
int carre(int n) {
    return n * n;
}

int main() {
    int nombre = 5;
    printf("Le carre de %d est %d\n", nombre, carre(nombre));
    return 0;
}
