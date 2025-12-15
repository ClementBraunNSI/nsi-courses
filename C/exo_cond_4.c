#include <stdio.h>

int main() {
    int a, b, c;
    printf("Entrez trois nombres : ");
    scanf("%d %d %d", &a, &b, &c);

    int max = a;
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }

    printf("Le maximum est %d\n", max);

    return 0;
}
