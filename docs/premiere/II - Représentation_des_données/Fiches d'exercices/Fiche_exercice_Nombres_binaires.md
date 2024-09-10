# **Fiche d'Exercices : Nombres en Base 2**

## **1. Conversion Binaire, Décimal, Hexadécimal**

**Exercice 1 : Conversion Binaire vers Décimal**  
Convertissez les nombres binaires suivants en décimal :

- $1101_{2}$
- $10101_{2}$
- $111000_{2}$
- $10010_{2}$
- $110110_{2}$

**Exercice 2 : Conversion Décimal vers Binaire**  
Convertissez les nombres décimaux suivants en binaire :

- $13_{10}$
- $42_{10}$
- $255_{10}$
- $76_{10}$
- $128_{10}$

**Exercice 3 : Conversion Décimal vers Hexadécimal**  
Convertissez les nombres décimaux suivants en hexadécimal :

- $30_{10}$
- $75_{10}$
- $128_{10}$
- $42_{10}$
- $99_{10}$

**Exercice 4 : Conversion Hexadécimal vers Décimal**  
Convertissez les nombres hexadécimaux suivants en décimal :

- $1A_{16}$
- $3F_{16}$
- $7D_{16}$
- $2A_{16}$
- $5E_{16}$

<br/>

**Exercice 5 : Conversion Décimal vers Hexadécimal (Méthode des Divisions Successives)**  
Convertissez les nombres décimaux suivants en hexadécimal en utilisant la méthode des divisions successives :

- $62_{10}$
- $158_{10}$
- $255_{10}$

## **2. Opérations en Base 2**

### **Addition en Base 2 :**

Effectuez les additions binaires suivantes :

- $1101_{2} + 101_{2}$
- $10000_{2} + 1101_{2}$
- $1111_{2} + 10_{2}$
- $10101_{2} + 1101_{2}$
- $11110_{2} + 110_{2}$

### **Soustraction en Base 2 :**

Effectuez les soustractions binaires suivantes :

- $1101_{2} - 101_{2}$
- $10000_{2} - 1101_{2}$
- $1111_{2} - 10_{2}$
- $10101_{2} - 1101_{2}$
- $11110_{2} - 110_{2}$

### **Multiplication en Base 2 :**

Effectuez les multiplications binaires suivantes :

- $1101_{2} \times 101_{2}$
- $10000_{2} \times 1101_{2}$
- $1111_{2} \times 10_{2}$
- $10101_{2} \times 1101_{2}$
- $11110_{2} \times 110_{2}$


## **3. Complément à Deux**

### **Complément à Deux (8 bits) :**

Trouvez le complément à deux des nombres binaires suivants (sur 8 bits) :

- $0110\ 0101_{2}$
- $0001\ 1110_{2}$
- $0100\ 1101_{2}$
- $0011\ 1010_{2}$
- $0111\ 1111_{2}$

### **Complément à Deux (16 bits) :**

Trouvez le complément à deux des nombres binaires suivants (sur 16 bits) :

- $0110\ 0101\ 1010\ 1100_{2}$
- $0001\ 1110\ 0101\ 0111_{2}$
- $0100\ 1101\ 1011\ 1010_{2}$

## **4. Conversion entre Décimal et Complément à Deux**

### **Décimal vers Complément à Deux :**

Convertissez les nombres décimaux suivants en leur représentation binaire sur 8 bits en utilisant le complément à deux :

- $-5_{10}$
- $-18_{10}$
- $-25_{10}$
- $-50_{10}$
- $-100_{10}$

### **Complément à Deux vers Décimal :**

Convertissez les nombres binaires négatifs suivants (en complément à deux sur 8 bits) en décimal :

- $1111\ 1011_{2}$
- $1110\ 1110_{2}$
- $1110\ 0111_{2}$
- $1100\ 1110_{2}$
- $1001\ 1100_{2}$

## **5. Binaire et Python**

**Exercice 1 :**  
En reprenant l'algorithme des divisions successives, réalisez une fonction `base10_vers_binaire`. Cette fonction prendra en paramètre un nombre entier et renverra une chaîne de caractères correspondant à la représentation en base 2 de celui-ci.

**Exercice 2 :**  
Écrivez une fonction `binaire_vers_base10`. Cette fonction prendra en paramètre une représentation en base 2 d'un nombre (chaîne de caractères) et renverra un nombre entier.