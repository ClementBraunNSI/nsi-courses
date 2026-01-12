#include <stdio.h>

// 1 si pair, 0 sinon
int est_pair(int n) {
    if (n % 2 == 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int n = 4;
    if (est_pair(n)) {
        printf("%d est pair\n", n);
    } else {
        printf("%d est impair\n", n);
    }
    return 0;
}
