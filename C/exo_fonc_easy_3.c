#include <stdio.h>

// Fonction valeur absolue
int valeur_absolue(int n) {
    if (n < 0) {
        return -n;
    }
    return n;
}

int main() {
    printf("Abs(-5) = %d\n", valeur_absolue(-5));
    printf("Abs(10) = %d\n", valeur_absolue(10));
    return 0;
}
