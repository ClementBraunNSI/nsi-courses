#include <stdio.h>

long minimum_tableau(long* tab, int taille){
    int minimum = tab[0];
    for (int i = 0; i < taille; i++){
        if (tab[i] < minimum){
            minimum = tab[i];
        }
    }
    return minimum;
}

int indice_minimum_tableau(long* tab, int taille){
    int indice_minimum = 0;
    for (int i = 0; i < taille; i++){
        if (tab[i] < tab[indice_minimum]){
            indice_minimum = i;
        }
    }
    return indice_minimum;
}



int main(void){
    long tab[8] = {1,2,4,3,6,0,-15,10};
    long tab2[6] = {1,2,4,3,6,0};
    printf("%ld\n",minimum_tableau(tab, sizeof(tab)/sizeof(tab[0])));
    printf("%d\n",indice_minimum_tableau(tab, sizeof(tab)/sizeof(tab[0])));

    long tab3[(sizeof(tab)/sizeof(tab[0]))+sizeof(tab2)/sizeof(tab2[0])];
    for (int i = 0; i < sizeof(tab)/sizeof(tab[0]); i++){
        tab3[i] = tab[i];
    }
    for (int i = sizeof(tab)/sizeof(tab[0]); i < sizeof(tab3)/sizeof(tab3[0]); i++){
        tab3[i] = tab2[i-sizeof(tab)/sizeof(tab[0])];
    }
    printf("%ld", sizeof(tab3)/sizeof(tab3[0]));
    for (int i = 0; i < sizeof(tab3)/sizeof(tab3[0]); i++){
        printf("%ld ", tab3[i]);
    }
}