#include "simplepoly.h"

// Prototypes
void s_poly_Affiche(s_polyZ *P);
QRz* s_horner_Z(s_polyZ* p, long a);
QRz* s_division_euclidienne_Z(s_polyZ* p, s_polyZ* q);
bool s_est_divisible_Z(s_polyZ *P, s_polyZ *Q);

int main(void)
{
    // Vos tests ici
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
