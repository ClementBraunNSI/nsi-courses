#include "simplepoly.h"

// Prototypes
void s_poly_Affiche(s_polyZ *P);
QRz* s_horner_Z(s_polyZ* p, long a);
QRz* s_division_euclidienne_Z(s_polyZ* p, s_polyZ* q);
bool s_est_divisible_Z(s_polyZ *P, s_polyZ *Q);

int main(void)
{
    // 1. Création des polynômes P(X) = X^2 - 3X + 2 et Q(X) = X - 1
    // p = 1*X^2 + (-3)*X + 2
    s_polyZ *p = s_polyZ_new(2);
    p->termes[0] = 2;
    p->termes[1] = -3;
    p->termes[2] = 1;

    // q = 1*X - 1
    s_polyZ *q = s_polyZ_new(1);
    q->termes[0] = -1;
    q->termes[1] = 1;

    // 2. Affichage
    printf("P(X) = ");
    s_poly_Affiche(p);
    printf("\n");

    printf("Q(X) = ");
    s_poly_Affiche(q);
    printf("\n\n");

    // 3. Test de s_horner_Z (Division par X - 1, donc a = 1)
    printf("--- Test Horner (Division de P par X - 1) ---\n");
    QRz *horner = s_horner_Z(p, 1);
    if (horner) {
        printf("Quotient Q(X) = ");
        s_poly_Affiche(horner->Q);
        printf("\n");
        printf("Reste R(X) = ");
        s_poly_Affiche(horner->R);
        printf("\n\n");
        s_qrz_free(horner);
    }

    // 4. Test de s_division_euclidienne_Z
    printf("--- Test Division Euclidienne (P / Q) ---\n");
    QRz *div = s_division_euclidienne_Z(p, q);
    if (div) {
        printf("Quotient Q(X) = ");
        s_poly_Affiche(div->Q);
        printf("\n");
        printf("Reste R(X) = ");
        s_poly_Affiche(div->R);
        printf("\n\n");
        s_qrz_free(div);
    }

    // 5. Test de s_est_divisible_Z
    printf("--- Test Divisibilité ---\n");
    if (s_est_divisible_Z(p, q)) {
        printf("P(X) est divisible par Q(X)\n");
    } else {
        printf("P(X) n'est pas divisible par Q(X)\n");
    }

    // Libération de la mémoire
    s_polyZ_free(p);
    s_polyZ_free(q);

    return 0;
}

/////////////////////
// Votre code ci-dessous
////////////////////

/**
 * s_poly_Affiche affiche un polynôme sous forme mathématique
 */
void s_poly_Affiche(s_polyZ *P)
{
    if (s_estNul(P))
    {
        printf("0");
        return;
    }
    
    long deg = degre(P);
    bool premier = true;
    
    for (long i = deg; i >= 0; i--)
    {
        long c = P->termes[i];
        if (c == 0) continue;
        
        // Afficher le signe
        if (!premier && c > 0) printf(" + ");
        if (!premier && c < 0) printf(" - ");
        if (premier && c < 0) printf("-");
        
        long abs_c = (c < 0) ? -c : c;
        
        // Afficher le coefficient et X
        if (i == 0)
            printf("%ld", abs_c);
        else if (abs_c == 1)
            printf(i == 1 ? "X" : "X^%ld", i);
        else
            printf(i == 1 ? "%ld X" : "%ld X^%ld", abs_c, i);
        
        premier = false;
    }
}

/**
 * s_horner_Z : algorithme de Hörner pour diviser par (X - a)
 */
QRz* s_horner_Z(s_polyZ* p, long a)
{
    long deg = degre(p);
    QRz* result = s_qrz_new();
    
    if (deg == 0)
    {
        result->Q = s_polyZ_new(0);
        result->R = s_polyZ_new(0);
        result->R->termes[0] = p->termes[0];
        return result;
    }
    
    result->Q = s_polyZ_new(deg - 1);
    result->R = s_polyZ_new(0);
    
    // Schéma de Hörner
    result->Q->termes[deg - 1] = p->termes[deg];
    for (long i = deg - 1; i >= 1; i--)
        result->Q->termes[i - 1] = p->termes[i] + a * result->Q->termes[i];
    
    result->R->termes[0] = p->termes[0] + a * result->Q->termes[0];
    
    return result;
}

/**
 * s_division_euclidienne_Z : divise p par q (q unitaire)
 */
QRz* s_division_euclidienne_Z(s_polyZ* p, s_polyZ* q)
{
    long deg_p = degre(p);
    long deg_q = degre(q);
    
    if (s_polyZ_td(q) != 1)
    {
        fprintf(stderr, "Erreur: diviseur non unitaire\n");
        return NULL;
    }
    
    QRz* result = s_qrz_new();
    
    if (deg_p < deg_q)
    {
        result->Q = s_polyZ_new(0);
        result->R = s_polyZ_copie(p);
        return result;
    }
    
    result->Q = s_polyZ_new(deg_p - deg_q);
    result->R = s_polyZ_copie(p);
    
    // Division par soustractions
    for (long i = deg_p - deg_q; i >= 0; i--)
    {
        long coef = result->R->termes[i + deg_q];
        result->Q->termes[i] = coef;
        
        for (long j = 0; j <= deg_q; j++)
            result->R->termes[i + j] -= coef * q->termes[j];
    }
    
    return result;
}

/**
 * s_est_divisible_Z teste si P est divisible par Q
 */
bool s_est_divisible_Z(s_polyZ *P, s_polyZ *Q)
{
    QRz* qr = s_division_euclidienne_Z(P, Q);
    if (qr == NULL) return false;
    
    bool divisible = s_estNul(qr->R);
    s_qrz_free(qr);
    
    return divisible;
}
