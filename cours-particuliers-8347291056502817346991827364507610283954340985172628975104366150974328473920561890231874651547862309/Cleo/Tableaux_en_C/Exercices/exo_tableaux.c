#include <stdio.h>
#include <stdlib.h>

// Fonctions
int somme_tableau(int* tab , int taille){
    int somme = 0;
    for ( int i = 0; i<taille; i++){
        somme = somme + tab[i];
    }
    return somme;
}

float moyenne(int tab [], int taille){
    return somme_tableau( tab, taille)/taille;
}

void afficher_inverse(int* tab, int taille){
    for ( int i = taille-1; i>=0; i--){
        printf("%d\n", tab[i]);
    }
}

int recherche_sequentielle(int* tab, int taille, int valeur){
    for ( int i = 0; i < taille; i++){
        if (valeur == tab[i]){
            return i;
        }
    }
    return -1;
}

int index_minimum(int* tab, int taille){
    int indice = 0;
    for ( int i = 0; i<taille; i++){
        if( tab[indice]>tab[i]){
            indice = i;
        }
    }
    return indice;
}

int valeur_maximum(int tab[], int taille){
    int valeur = tab[0];
    for (int i = 0; i<taille; i++){
        if(tab[i]>valeur){
            valeur = tab[i];
        }
    }
    return valeur;
}

int* fusion_tableau(int tab1[], int taille1, int tab2[]){
    int* tab3 = (int*)malloc(2*taille1 * sizeof(int));
    for (int i = 0; i<taille1; i++){
        tab3[i]=tab1[i];
    }
    for (int j = 0; j<taille1; j++){
        int indice = taille1 + j ;
        tab3[taille1 + j] = tab2[j];
    }
    return tab3;
}

//Bac a sable
int main (void){

    // variables
    /*int taille;
    scanf("%d", &taille);
    int tab[taille];
    for (int i = 0; i<taille; i++){
        scanf("%d", & tab[i]);
    }*/
    int tab [5]={36, 57, 89,10, 28};
    int tab2 [5]={47,28,30,73,3};
    int* tab3 = fusion_tableau(tab,5, tab2);
    for ( int i = 0; i<10; i++){
        printf("%d ", tab3[i]);
    }
    //Appel aux fonctions
    //printf("La somme de mon tableau est : %d", somme_tableau(tab, taille));
    //printf("%f", moyenne(tab,5));
    //afficher_inverse(tab, sizeof(tab)/sizeof(tab[0]));
    //printf("%d", recherche_sequentielle(tab, 5, 10));
    //printf("%d", index_minimum(tab, 5));
    //printf("%d", valeur_maximum(tab,5));
    
}
