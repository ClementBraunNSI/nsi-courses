/*
    simplepoly une librairie de calculs matriciels à visée pédagogique
    Copyright 2024 Vincent Ledda
    Contact : vincent.ledda@centralelille.fr

    This file is part of simplepoly

    simplepoly is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    simplepoly is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with simplepoly; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

*/

#include "sp_utils.h"

#define INVALID_INDEX "indexes invalides"
#define INVALID_ENTREE "Les données en entrée ne sont pas conformes"
#define INVALID_DIVSION_Z "division par zéro"
#define INVALID_TAB "Le tableau est vide"
#define INVALID_TYPE "Impossible de déterminer le type"
#define INVALID_INCOMPATIBLE "type incompatibles"
#define INVALID_NON_UNITAIRE "division par un polynôme non unitaire"
/* Structures */


/**
 * Définition d'un type polynôme à coefficients réels
 *   ring: le type de polynôme
 *   Degre: le degré du polynôme
 *   *termes: pointeur vers les données de type double
 */
typedef struct polynomial_r
{
  char   ring;
  size_t Degre;
  double *termes;
} s_poly ;

     
/**
 * Définition d'un type polynôme à coefficients entiers
 *  ring: le type de polynôme
 *  Degre: le nombre de terme
 *  *termes: pointeur vers les données de type long
 */
typedef struct polynomial_z
{
  char ring;
  size_t Degre;
  long  *termes;
} s_polyZ ;



/**
 * Quotient et reste
 */
typedef struct qr {
  s_poly* Q;
  s_poly* R;
} QR;


/**
 * Quotient et reste
 */
typedef struct qrz {
  s_polyZ* Q;
  s_polyZ* R;
} QRz;





/* Création des polynômes */

/* constructeur
Allocation de la mémoire d'une matrice
*/
s_poly *s_poly_new(size_t n);
s_polyZ *s_polyZ_new(size_t n);
QRz * s_qrz_new(void);
s_poly *s_poly_alea(unsigned int n,int min,int max);
s_polyZ *s_polyZ_alea(unsigned int n,int min,int max);

s_poly *s_poly_coef(unsigned int n, const double valeurs[],unsigned int nbVal);
s_polyZ *s_polyZ_coef(unsigned int n, const long valeurs[],unsigned int nbVal);

s_poly* s_poly_copie(s_poly* P);
s_polyZ* s_polyZ_copie(s_polyZ* P);

/* Libère la mémoire occupée par un polynôme */
void s_poly_free(s_poly *P);
void s_polyZ_free(s_polyZ *P);
void s_qrz_free(QRz *qr);
void s_qr_free(QR *qr);


/* Misc */
long degre(void *p);
double s_poly_td(s_poly* P);
long s_polyZ_td(s_polyZ* P);



/* Questions */
bool s_estEgal(void* P, void* Q);
bool s_estNul(void* P);

/* Affichage */
void s_poly_affiche(void *p);



/* Opérations */

s_poly* s_somme(s_poly* P,s_poly* Q);
s_poly* s_difference(s_poly* P,s_poly* Q);
s_poly* s_oppose(s_poly* P);
s_poly* s_produit(s_poly* P,s_poly* Q);
s_poly* s_lproduit(s_poly* P,double lambda);

s_polyZ* s_oppose_Z(s_polyZ* P);
s_polyZ* s_somme_Z(s_polyZ* P,s_polyZ* Q);
s_polyZ* s_difference_Z(s_polyZ* P,s_polyZ* Q);
s_polyZ* s_produit_Z(s_polyZ* P, s_polyZ* Q);
s_polyZ* s_lproduit_Z(s_polyZ* P, long lambda);

/* Eval */

double s_poly_eval(void* p ,double a);
long s_polyZ_eval(s_polyZ* p ,long a);


/* diff, int */

//Trop compliqué à gérer pour les étudiants...
//void* s_diff(void* p);
//void* s_int(void* p);

s_polyZ* s_polyZ_diff(s_polyZ* p);
s_poly* s_poly_int(void* p);
s_poly* s_poly_diff(s_poly* p);


