#include <stdio.h>

// Factorielle
int factorielle(int n) {
    int res = 1;
    for (int i = 1; i <= n; i++) {
        res = res * i;
    }
    return res;
}

int main() {
    printf("5! = %d\n", factorielle(5));
    return 0;
}
