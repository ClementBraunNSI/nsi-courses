#include "simplepoly.h"

/**
 * s_poly_Affiche - Affiche un polynôme sous forme mathématique
 */

void s_poly_Affiche(s_polyZ *P)
{
    if (s_estNul(P)) {
        printf("0");
        return;
    }
    long deg = degre(P);
    bool premier = true;
    for (long i = deg; i >= 0; i--)
    {
        long c = P->termes[i];
        if (c != 0){
            // Afficher le coefficient pour le terme de plus haut degré (et son signe s'il est négatif)
            if (premier){
                if (c == -1){
                    printf("-");
                }
                else if (c!=1){
                    printf("%ld",c);
                }
            }
            else if (c > 0){
                printf(" + %ld", c); // Si le nombre est positif on affiche le +
            }
            else{
                printf(" %ld", c);  // Le signe - est déjà dans c
            }
            // Afficher X^i
            if (i == 1)
                printf("X"); // Si le terme est de degré 1, pas besoin de ^x
            else if (i > 1)
                printf("X^%ld", i);
            premier = false;
        }
    }
}

/**
 * s_horner_Z - Implémente l'algorithme de Hörner
 */
QRz* s_horner_Z(s_polyZ* p, long a)
{
    long deg = degre(p);
    // Créer la structure quotient / reste
    QRz* result = s_qrz_new();
    
    // Cas d'un polynome constant
    if (deg == 0)
    {
        result->Q = s_polyZ_new(0); // polynome constant "ne peut pas diviser" un polynome de degré supérieur
        result->R = s_polyZ_new(0); // Reste vaut le polynome
        result->R->termes[0] = p->termes[0];
        return result;
    }
    
    // Création des structures : polynome pour Q et polynome constant pour R
    result->Q = s_polyZ_new((size_t)(deg - 1));
    result->R = s_polyZ_new(0);
    
    // Algorithme de Hörner
    result->Q->termes[deg - 1] = p->termes[deg];
    
    for (long i = deg - 1; i >= 1; i--)
        // on prend le coefficient du degré i que l'on multiplie avec le terme fort (a) que l'on ajoute au coefficient de base du polynome
        result->Q->termes[i - 1] = p->termes[i] + a * result->Q->termes[i];
    
    // même étape pour le reste
    result->R->termes[0] = p->termes[0] + a * result->Q->termes[0];
    
    return result;
}

/**
 * s_division_euclidienne_Z - Division euclidienne dans Z[X]
 */
QRz* s_division_euclidienne_Z(s_polyZ* p, s_polyZ* q)
{
    long deg_p = degre(p);
    long deg_q = degre(q);
    
    if (s_polyZ_td(q) != 1)
    {
        fprintf(stderr, "Erreur: le diviseur doit être unitaire\n");
        return NULL;
    }
    
    //Création de la structure Quotient / Reste
    QRz* result = s_qrz_new();
    
    if (deg_p < deg_q) // si le degré du diviseur est supérieur au degré du dividende, on ne peut pas diviser
    {
        result->Q = s_polyZ_new(0);
        result->R = s_polyZ_copie(p);
        return result;
    }
    
    
    // Création des structures : polynome pour Q et polynome constant pour R
    result->Q = s_polyZ_new((size_t)(deg_p - deg_q));
    result->R = s_polyZ_copie(p);
    
    // Division par soustractions successives, i représente le degré que l'on soustrait
    for (long i = deg_p - deg_q; i >= 0; i--)
    {

        // On récupère le coefficient du reste à qui on doit soustraire le quotient
        long coef_quotient = result->R->termes[i + deg_q];
        result->Q->termes[i] = coef_quotient;
        
        // On retire ce coefficicent à chacun des degrés correspondants, donc retirer la plus grande quantité au plus grand degré de ce qui doit être restant
        for (long j = 0; j <= deg_q; j++)
            result->R->termes[i + j] -= coef_quotient * q->termes[j];
    }
    
    return result;
}

/**
 * s_est_divisible_Z - Teste la divisibilité dans Z[X]
 */
bool s_est_divisible_Z(s_polyZ *P, s_polyZ *Q)
{
    // On teste une division
    QRz* qr = s_division_euclidienne_Z(P, Q);

    // Si la division a échoué : pas divisible
    if (qr == NULL)
        return false;
    
    // Vérifier si le reste de la division est nul (si le reste est nul on a true, sinon false)
    bool divisible = s_estNul(qr->R);
    s_qrz_free(qr);
    
    return divisible;
}


int main(void)
{
    // Test 1.1: Polynôme aléatoire
    printf("1.1 - Polynôme aléatoire de degré 10:\n");
    s_polyZ* P1 = s_polyZ_alea(10, -3, 2);
    s_poly_Affiche(P1);
    printf("\n\n");
    s_polyZ_free(P1);
    
    // Test 1.2: Polynôme -X^2 - X + 1
    printf("1.2 - Polynôme avec coefficients donnés:\n");
    long valeurs1[3] = {-1, -1, 1};
    s_polyZ* P2 = s_polyZ_coef(2, valeurs1, 3);
    s_poly_Affiche(P2);
    printf("\n\n");
    s_polyZ_free(P2);
    
    // Test 1.3: Polynôme nul
    printf("1.3 - Polynôme nul:\n");
    s_polyZ* P3 = s_polyZ_new(5);
    s_poly_Affiche(P3);
    printf("\n\n");
    s_polyZ_free(P3);

    // Algo de Horner
    s_polyZ *p;
    QRz *qr;
    long valeurs[8] = {5, 0, 0, 0, 1, 2, 3, 4};
    p = s_polyZ_coef(7, valeurs, 8);
    
    printf("P:\n");
    s_poly_Affiche(p);
    printf("\n");
    
    printf("\nDivision de P par (X - (-2)) = (X + 2):\n\n");
    qr = s_horner_Z(p, -2);
    
    printf("Q:\n");
    s_poly_Affiche(qr->Q);
    printf("\n");
    
    printf("\nR:\n");
    s_poly_Affiche(qr->R);
    printf("\n\n");
    
    s_polyZ_free(p);
    s_qrz_free(qr);

    // Division Euclidienne
    
    s_polyZ *a;
    s_polyZ *b;
    QRz *qr2;
    
    long valeurs_a[8] = {5, 0, 0, 0, 1, 2, -3, 4};
    a = s_polyZ_coef(7, valeurs_a, 8);
    printf("A =\n");
    s_poly_Affiche(a);
    printf("\n");
    
    long valeurs_b[4] = {1, 2, 3, 4};
    b = s_polyZ_coef(3, valeurs_b, 4);
    printf("\nB =\n");
    s_poly_Affiche(b);
    printf("\n");
    
    qr2 = s_division_euclidienne_Z(a, b);
    
    printf("\nQ =\n");
    s_poly_Affiche(qr2->Q);
    printf("\n");
    
    printf("\nR =\n");
    s_poly_Affiche(qr2->R);
    printf("\n");
    
    
    
    s_polyZ_free(a);
    s_polyZ_free(b);
    s_qrz_free(qr2);
    
    // Divisibilité 

    s_polyZ *a2;
    s_polyZ *b2;
    
    long valeurs_a2[6] = {1, -1, -2, -5, -9, 8};
    a2 = s_polyZ_coef(5, valeurs_a2, 6);
    printf("A =\n");
    s_poly_Affiche(a2);
    printf("\n");
    
    long valeurs_b2[3] = {1, 1, -1};
    b2 = s_polyZ_coef(2, valeurs_b2, 3);
    printf("\nB =\n");
    s_poly_Affiche(b2);
    printf("\n");
    
    if(s_est_divisible_Z(a2, b2))
    {
        printf("\n✓ B divise A\n");
    }
    else
    {
        printf("\n✗ B ne divise pas A\n");
    }
    
    s_polyZ_free(a2);
    s_polyZ_free(b2);

    return 0;
}