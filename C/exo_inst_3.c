#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int temp;

    printf("Avant: a = %d, b = %d\n", a, b);

    // Échange avec une variable temporaire
    temp = a;
    a = b;
    b = temp;

    printf("Après: a = %d, b = %d\n", a, b);

    return 0;
}
