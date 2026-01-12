#include <stdio.h>

// Affiche la table de multiplication
void table_multiplication(int n) {
    printf("Table de %d :\n", n);
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }
}

int main() {
    table_multiplication(7);
    return 0;
}
