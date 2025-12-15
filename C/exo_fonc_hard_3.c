#include <stdio.h>

// Calcule le n-ième terme de la suite de Fibonacci
// u0=0, u1=1, u(n) = u(n-1) + u(n-2)
int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    int a = 0;
    int b = 1;
    int temp;
    
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    printf("Fibonacci(10) = %d\n", fibonacci(10));
    return 0;
}
