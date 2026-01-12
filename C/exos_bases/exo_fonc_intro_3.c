#include <stdio.h>

// Fonction somme
int somme(int a, int b) {
    return a + b;
}

int main() {
    int res = somme(4, 5);
    printf("Somme de 4 et 5 : %d\n", res);
    return 0;
}
