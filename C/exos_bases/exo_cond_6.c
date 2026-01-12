#include <stdio.h>

int main() {
    int note;
    printf("Entrez la note sur 20 : ");
    scanf("%d", &note);

    if (note >= 16) {
        printf("Très bien\n");
    } else if (note >= 14) {
        printf("Bien\n");
    } else if (note >= 12) {
        printf("Assez bien\n");
    } else if (note >= 10) {
        printf("Passable\n");
    } else {
        printf("Insuffisant\n");
    }

    return 0;
}
