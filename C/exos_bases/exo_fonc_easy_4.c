#include <stdio.h>

// Procédure pour vérifier la majorité
void est_majeur(int age) {
    if (age >= 18) {
        printf("Majeur\n");
    } else {
        printf("Mineur\n");
    }
}

int main() {
    est_majeur(20);
    est_majeur(15);
    return 0;
}
