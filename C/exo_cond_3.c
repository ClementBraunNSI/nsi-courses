#include <stdio.h>

int main() {
    int a, b;
    printf("Entrez deux nombres : ");
    scanf("%d %d", &a, &b);

    if (a > b) {
        printf("Le maximum est %d\n", a);
    } else {
        printf("Le maximum est %d\n", b);
    }

    return 0;
}
