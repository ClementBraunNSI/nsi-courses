#include <stdio.h>

// Max de 3 nombres
int max_trois(int a, int b, int c) {
    int max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    return max;
}

int main() {
    printf("Max(10, 5, 20) = %d\n", max_trois(10, 5, 20));
    return 0;
}
