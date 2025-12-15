#include <stdio.h>

int main() {
    int n;
    
    do {
        printf("Entrez un nombre (0 pour arrêter) : ");
        scanf("%d", &n);
    } while (n != 0);

    printf("Fin du programme.\n");
    return 0;
}
