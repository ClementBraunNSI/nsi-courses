#include <stdio.h>

int main() {
    int n;
    printf("Afficher les nombres pairs jusqu'à : ");
    scanf("%d", &n);

    for (int i = 0; i <= n; i += 2) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
