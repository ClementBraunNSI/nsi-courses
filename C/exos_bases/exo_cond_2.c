#include <stdio.h>

int main() {
    int n;
    printf("Entrez un nombre entier : ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Le nombre est pair.\n");
    } else {
        printf("Le nombre est impair.\n");
    }

    return 0;
}
