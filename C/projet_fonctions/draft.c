#include <stdio.h>
#include <stdlib.h> 

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

long* horner_poly(long* valeurs, int degre, int a){
    long* intermediaire = malloc((degre - 1) * sizeof(long));
    long* final = malloc((degre - 1) * sizeof(long));
    if (intermediaire == NULL){
        printf("Erreur d'allocation mémoire\n");
        return NULL;
    }
    final[0] = valeurs[0];
    intermediaire[0] = final[0] * a;
    final[1] = valeurs[1]-intermediaire[0];

    for (int i = 0; i< sizeof(intermediaire)/sizeof(intermediaire[0]) ; i++){
        intermediaire[i] = valeurs[i] * a;
        final[i+1] = valeurs[i+1]-intermediaire[i];
    }
    long reste = intermediaire[(sizeof(intermediaire)/sizeof(intermediaire[0]))-1];

    return final;
}

int main(void){
    long valeurs[6] = {1, 2, 3,0,3,4};
    affiche_poly(valeurs, 6);
    return 0;
}