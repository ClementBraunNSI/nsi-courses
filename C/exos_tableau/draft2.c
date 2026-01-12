#include <stdio.h>
#include <stdlib.h> // Nécessaire pour malloc et free
#include <string.h> // Nécessaire pour strcmp

int somme_tableau(int* tableau, int taille){
    int somme = 0;
    for (int i = 0; i < taille ; i++){
        somme += tableau[i];
    }
    return somme;
}

float moyenne(int* tab, int taille){
    int somme = somme_tableau(tab, taille);
    return (float)somme/taille;
}

int* creer_tableau(int taille){
    int* tab = malloc(taille * sizeof(int)); // allocation de la zone mémoire
    if (tab == NULL) {
        return NULL; // vérification si la zone est bien allouée
    }

    for (int i = 0; i < taille; i++){
        tab[i] = i;
    }
    return tab; // On renvoie l'adresse du bloc mémoire alloué
}

char* retourner_mot(char* mot){
    char* mot_retour = malloc(strlen(mot));
    for (int i = 0; i < strlen(mot); i++){
        mot_retour[i] = mot[i];
    }
    return mot_retour;
}

int palindrome(char* mot1, char* mot2){
    return strcmp(mot1, mot2) == 0;
}

int detection_doublons(int* tab, int taille){
    for (int i = 0; i < taille; i++){
        int compteur = 0;
        for (int j = 0 ; j < taille ; j++){
            if (i != j){
                if (tab[i] == tab[j]){
                    compteur++;
                }
            }
        }
        if (compteur > 0){
            return 1;
        }
    }   
    return 0;
}


int main(void){
    printf("moyenne = %f\n", moyenne((int[]){1, 2, 3, 4, 5}, 5));
    
    int* tab = creer_tableau(5);
    
    if (tab != NULL) {
        for (int i = 0; i < 5; i++){
            printf("%d ", tab[i]);
        }
        printf("\n");
        free(tab);
    }
    char* mot1 = "yakak";
    char* mot2 = retourner_mot("kayak");
    if (palindrome(mot1, mot2)){
        printf("palindrome\n");
        free(mot2);
    }
    else{
        printf("non palindrome\n");
        free(mot2);
    }
    /**/
    if (detection_doublons((int[]){1, 2, 3, 4, 5}, 5)){
        printf("doublons\n");
    }
    else{
        printf("pas de doublons\n");
    }

    if (detection_doublons((int[]){1, 2, 3, 3, 5}, 5)){
        printf("doublons\n");
    }
    else{
        printf("pas de doublons\n");
    }
}