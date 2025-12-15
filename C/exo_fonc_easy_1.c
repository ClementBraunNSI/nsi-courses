#include <stdio.h>

// Fonction de conversion
float conversion_c_f(float celsius) {
    return celsius * 1.8 + 32;
}

int main() {
    float c = 25.0;
    float f = conversion_c_f(c);
    printf("%.1f C = %.1f F\n", c, f);
    return 0;
}
