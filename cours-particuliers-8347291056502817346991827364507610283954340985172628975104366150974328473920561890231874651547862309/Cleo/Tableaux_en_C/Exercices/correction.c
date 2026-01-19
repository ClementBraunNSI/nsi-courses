#include <stdio.h>
#include <stdlib.h>

// ==========================================
// NIVEAU 1
// ==========================================

// Exo 6 : Somme des éléments
int somme_tableau(int tab[], int taille) {
    int somme = 0;
    for (int i = 0; i < taille; i++) {
        somme += tab[i];
    }
    return somme;
}

// Exo 7 : Moyenne
float moyenne(int tab[], int taille) {
    if (taille == 0) return 0.0;
    int s = somme_tableau(tab, taille); // Réutilisation de la fonction précédente
    return (float)s / taille;
}

// Exo 8 : Compteur de Zéros
int compte_zeros(int tab[], int taille) {
    int compteur = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i] == 0) {
            compteur++;
        }
    }
    return compteur;
}

// Exo 9 : Remplissage 1 à N
void remplir_1_a_n(int tab[], int taille) {
    for (int i = 0; i < taille; i++) {
        tab[i] = i + 1;
    }
}

// Exo 10 : Copie de Tableau
void copier_tableau(int src[], int dest[], int taille) {
    for (int i = 0; i < taille; i++) {
        dest[i] = src[i];
    }
}

// ==========================================
// NIVEAU 2
// ==========================================

// Exo 11 : Le Maximum
int trouver_max(int tab[], int taille) {
    int max = tab[0];
    for (int i = 1; i < taille; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }
    return max;
}

// Exo 12 : Index du Minimum
int index_min(int tab[], int taille) {
    int index = 0;
    for (int i = 1; i < taille; i++) {
        if (tab[i] < tab[index]) {
            index = i;
        }
    }
    return index;
}

// Exo 13 : Affichage Inversé
void afficher_inverse(int tab[], int taille) {
    for (int i = taille - 1; i >= 0; i--) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}

// Exo 14 : Recherche séquentielle
int recherche(int tab[], int taille, int valeur) {
    for (int i = 0; i < taille; i++) {
        if (tab[i] == valeur) {
            return i; // Trouvé à l'indice i
        }
    }
    return -1; // Pas trouvé
}

// Exo 15 : Tableaux Identiques ?
int sont_identiques(int t1[], int t2[], int taille) {
    for (int i = 0; i < taille; i++) {
        if (t1[i] != t2[i]) {
            return 0; // Faux dès qu'une différence est trouvée
        }
    }
    return 1; // Vrai si on a parcouru tout le tableau sans différence
}

// ==========================================
// NIVEAU 3
// ==========================================

// Exo 16 : Palindrome
int est_palindrome(int tab[], int taille) {
    for (int i = 0; i < taille / 2; i++) {
        if (tab[i] != tab[taille - 1 - i]) {
            return 0; // Pas un palindrome
        }
    }
    return 1; // C'est un palindrome
}

// Exo 17 : Rotation à Droite
void rotation_droite(int tab[], int taille) {
    if (taille <= 1) return;
    
    int dernier = tab[taille - 1];
    // On déplace tout vers la droite en partant de la fin
    for (int i = taille - 1; i > 0; i--) {
        tab[i] = tab[i - 1];
    }
    tab[0] = dernier;
}

// Exo 18 : Fusion de tableaux (nécessite malloc)
int* fusionner(int A[], int B[], int taille) {
    // Allocation d'un tableau de taille double
    int* C = (int*)malloc(2 * taille * sizeof(int));
    if (C == NULL) {
        printf("Erreur d'allocation mémoire\n");
        exit(1);
    }
    
    // Copie de A dans la première moitié
    for (int i = 0; i < taille; i++) {
        C[i] = A[i];
    }
    
    // Copie de B dans la deuxième moitié
    for (int i = 0; i < taille; i++) {
        C[taille + i] = B[i];
    }
    
    return C;
}

// Exo 19 : Détection de Doublons
int a_doublons(int tab[], int taille) {
    for (int i = 0; i < taille; i++) {
        // Pour chaque élément, on regarde les suivants
        for (int j = i + 1; j < taille; j++) {
            if (tab[i] == tab[j]) {
                return 1; // Doublon trouvé
            }
        }
    }
    return 0; // Aucun doublon
}

// Exo 20 : Inversion en place
void inverser_en_place(int tab[], int taille) {
    int temp;
    for (int i = 0; i < taille / 2; i++) {
        // Échange de tab[i] et tab[taille - 1 - i]
        temp = tab[i];
        tab[i] = tab[taille - 1 - i];
        tab[taille - 1 - i] = temp;
    }
}

// Fonction utilitaire pour afficher un tableau (pour le main)
void afficher_tab(int tab[], int taille) {
    printf("[ ");
    for(int i=0; i<taille; i++) {
        printf("%d ", tab[i]);
    }
    printf("]\n");
}

int main() {
    printf("=== CORRECTION EXERCICES TABLEAUX EN C ===\n\n");

    // ==========================================
    // INTRODUCTION
    // ==========================================
    printf("--- INTRODUCTION ---\n");

    // Exo 1 : Déclaration Simple
    int scores[5];
    printf("Exo 1: Tableau scores declare.\n");

    // Exo 2 : Initialisation
    int premiers[] = {2, 3, 5, 7, 11};
    printf("Exo 2: Tableau premiers initialise.\n");

    // Exo 3 : Accès Lecture
    printf("Exo 3: 3eme element de premiers : %d\n", premiers[2]);

    // Exo 4 : Accès Écriture
    scores[0] = 100;
    printf("Exo 4: scores[0] modifie a %d\n", scores[0]);

    // Exo 5 : Affichage complet
    printf("Exo 5: Contenu de premiers : ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", premiers[i]);
    }
    printf("\n\n");

    // ==========================================
    // TESTS NIVEAU 1
    // ==========================================
    printf("--- NIVEAU 1 ---\n");
    
    int tab1[] = {10, 20, 0, 40, 0};
    int t1_size = 5;

    printf("Exo 6 (Somme): %d\n", somme_tableau(tab1, t1_size));
    printf("Exo 7 (Moyenne): %.2f\n", moyenne(tab1, t1_size));
    printf("Exo 8 (Zeros): %d\n", compte_zeros(tab1, t1_size));
    
    int tab_range[5];
    remplir_1_a_n(tab_range, 5);
    printf("Exo 9 (1 a N): ");
    afficher_tab(tab_range, 5);

    int tab_copy[5];
    copier_tableau(tab1, tab_copy, 5);
    printf("Exo 10 (Copie): ");
    afficher_tab(tab_copy, 5);
    printf("\n");

    // ==========================================
    // TESTS NIVEAU 2
    // ==========================================
    printf("--- NIVEAU 2 ---\n");

    int tab2[] = {5, 12, 3, 9, 12};
    printf("Exo 11 (Max): %d\n", trouver_max(tab2, 5));
    printf("Exo 12 (Index Min): %d (valeur: %d)\n", index_min(tab2, 5), tab2[index_min(tab2, 5)]);
    
    printf("Exo 13 (Inverse): ");
    afficher_inverse(tab2, 5);

    printf("Exo 14 (Recherche 9): %d\n", recherche(tab2, 5, 9));
    printf("Exo 14 (Recherche 99): %d\n", recherche(tab2, 5, 99));

    int tab2_bis[] = {5, 12, 3, 9, 12};
    printf("Exo 15 (Identiques): %d\n", sont_identiques(tab2, tab2_bis, 5));
    printf("\n");

    // ==========================================
    // TESTS NIVEAU 3
    // ==========================================
    printf("--- NIVEAU 3 ---\n");

    int palindrome[] = {1, 2, 3, 2, 1};
    int pas_palindrome[] = {1, 2, 3, 4, 5};
    printf("Exo 16 (Palindrome {1,2,3,2,1}): %d\n", est_palindrome(palindrome, 5));
    printf("Exo 16 (Palindrome {1,2,3,4,5}): %d\n", est_palindrome(pas_palindrome, 5));

    int rot[] = {1, 2, 3};
    rotation_droite(rot, 3);
    printf("Exo 17 (Rotation {1,2,3}): ");
    afficher_tab(rot, 3);

    int A[] = {1, 2};
    int B[] = {3, 4};
    int* C = fusionner(A, B, 2);
    printf("Exo 18 (Fusion): ");
    afficher_tab(C, 4);
    free(C); // Important : libérer la mémoire allouée avec malloc

    printf("Exo 19 (Doublons dans tab2): %d\n", a_doublons(tab2, 5));
    printf("Exo 19 (Doublons dans {1,2,3}): %d\n", a_doublons(rot, 3));

    inverser_en_place(pas_palindrome, 5);
    printf("Exo 20 (Inversion en place {1,2,3,4,5}): ");
    afficher_tab(pas_palindrome, 5);

    return 0;
}
