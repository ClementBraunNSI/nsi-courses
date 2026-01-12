#include <stdio.h>

int main() {
    int n, somme = 0;
    printf("Somme des entiers jusqu'à : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        somme += i;
    }

    printf("La somme est : %d\n", somme);
    return 0;
}
