#include <stdio.h>

// Puissance
int puissance(int nombre, int exposant) {
    int res = 1;
    for (int i = 0; i < exposant; i++) {
        res = res * nombre;
    }
    return res;
}

int main() {
    printf("2^3 = %d\n", puissance(2, 3));
    return 0;
}
