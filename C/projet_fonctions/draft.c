#include <stdio.h>

void affiche_poly(long valeurs[], int taille) {
    for (int i = taille-1 ; i >= 0; i--){
        if (valeurs[taille - 1 - i] != 0){
            if (i==taille-1){
                printf("%ld", valeurs[0]);
            } else {
                if (valeurs[taille-1-i] > 0){
                    printf("+%ld", valeurs[taille-1-i]);
                }
                else{
                    printf("%ld", valeurs[taille- 1 -i]);
                }
            }
            if (i >=1){
                printf("X^%d", i);
            }
        }
       
    }
}

int main(void){
    long valeurs[6] = {1, 2, 3,0,3,4};
    affiche_poly(valeurs, 6);
    return 0;
}