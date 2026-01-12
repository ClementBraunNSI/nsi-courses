#include <stdio.h>

// Fonction qui calcule l'aire
float aire_rectangle(float longueur, float largeur) {
    return longueur * largeur;
}

int main() {
    float l = 5.0;
    float L = 3.0;
    float aire = aire_rectangle(l, L);
    printf("L'aire est : %.2f\n", aire);
    return 0;
}
