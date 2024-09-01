# Fiche d'exercice : Nombres en base 2

### Conversion binaire, décimal, hexadécimal

1. Convertir les nombres binaires suivants en décimal :
   - $1101_{2}$
   - $10101_{2}$
   - $111000_{2}$
   - $10010_{2}$
   - $110110_{2}$
<br/>

1. Convertir les nombres décimaux suivants en binaire :
   - $13_{10}$
   - $42_{10}$
   - $255_{10}$
   - $76_{10}$
   - $128_{10}$
  
<br/>

<br/>

1. Convertir les nombres décimaux suivants en hexadécimal :
   - $30_{10}$
   - $75_{10}$
   - $128_{10}$
   - $42_{10}$
   - $99_{10}$
<br/>

1. Convertir les nombres hexadécimaux suivants en décimal :
   - $1A_{16}$
   - $3F_{16}$
   - $7D_{16}$
   - $2A_{16}$
   - $5E_{16}$

<br/>

6. Convertir les nombres décimaux suivants en hexadécimal en utilisant la méthode des divisions successives:
   - $62_{10}$
   - $158_{10}$
   - $255_{10}$

### Opération en base 2

**Addition en Base 2 :**

1. $1101_{2} + 101_{2}$
2. $10000_{2} + 1101_{2}$
3. $1111_{2} + 10_{2}$
4. $10101_{2} + 1101_{2}$
5. $11110_{2} + 110_{2}$

**Soustraction en Base 2 :**

6. $1101_{2} - 101_{2}$
7. $10000_{2} - 1101_{2}$
8. $1111_{2} - 10_{2}$
9. $10101_{2} - 1101_{2}$
10. $11110_{2} - 110_{2}$

**Multiplication en Base 2 :**

11. $1101_{2} \times 101_{2}$
12. $10000_{2} \times 1101_{2}$
13. $1111_{2} \times 10_{2}$
14. $10101_{2} \times 1101_{2}$
15. $11110_{2} \times 110_{2}$
  
**Division en Base 2 :**
16. $110110_{2} \div10_{2}$.
17. $10101_{2} \div1_{2}$.
18. $1111101_{2} \div 101_{2}$.
19. $11001_{2} \div10_{2}$.
20. $100111_{2} \div1001_{2}$.

### Complément à deux

Trouver le complément à deux des nombres binaires suivants (sur 8 bits) :

1. $0110\ 0101_{2}$
2. $0001\ 1110_{2}$
3. $0100\ 1101_{2}$
4. $0011\ 1010_{2}$
5. $0111\ 1111_{2}$

Trouver le complément à deux des nombres binaires suivants (sur 16 bits) :

1. $0110\ 0101\ 1010\ 1100_{2}$
2. $0001\ 1110\ 0101\ 0111_{2}$
3. $0100\ 1101\ 1011\ 1010_{2}$
4. $0011\ 1010\ 1100\ 0110_{2}$
5. $0111\ 1111\ 1111\ 1111_{2}$

### Conversion entre décimal et complément à deux

Convertir les nombres décimaux suivants en leur représentation binaire sur 8 bits en utilisant le complément à deux :

1. $-5_{10}$
2. $-18_{10}$
3. $-25_{10}$
4. $-50_{10}$
5. $-100_{10}$

Convertir les nombres binaires négatifs suivants (en complément à deux sur 8 bits) en décimal :

1. $1111\ 1011_{2}$
2. $1110\ 1110_{2}$
3. $1110\ 0111_{2}$
4. $1100\ 1110_{2}$
5. $1001\ 1100_{2}$

## Binaire et Python

1. En reprenant l'algorithme des divisions successives, réaliser une fonction base10_vers_binaire. Cette fonction prendra en paramètre un nombre entier et renverra une chaîne de caractère correspondant à la représentation en base 2 de celui-ci.

2. Écrire une fonction binaire_vers_base10. Cette fonction prendra en paramètre une représentation en base 2 d'un nombre (chaîne de caractère) et renverra un nombre entier.