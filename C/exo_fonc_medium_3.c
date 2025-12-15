#include <stdio.h>

// Somme des entiers de 1 à n
int somme_1_a_n(int n) {
    int somme = 0;
    for (int i = 1; i <= n; i++) {
        somme += i;
    }
    return somme;
}

int main() {
    printf("Somme 1..10 = %d\n", somme_1_a_n(10));
    return 0;
}
