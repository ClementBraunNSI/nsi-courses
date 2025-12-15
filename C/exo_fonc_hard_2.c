#include <stdio.h>

// Vérifie si un nombre est premier (1 si oui, 0 sinon)
int est_premier(int n) {
    if (n < 2) return 0;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0; // Divisible par i, donc pas premier
        }
    }
    return 1; // Aucun diviseur trouvé
}

int main() {
    if (est_premier(17)) printf("17 est premier\n");
    if (!est_premier(10)) printf("10 n'est pas premier\n");
    return 0;
}
