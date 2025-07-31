# 📚 Jeux d'instruction

## 📖 Définitions

Un jeu d'instruction correspond à l'ensemble des opérations réalisables et câblées pour un processeur donné.

Les processeurs, par leur composition ne comprennent que le binaire mais le système d'exploitation permet de traduire les langages de programmation en opérations compréhensibles par le processeur.
On appelle **mnémonique** une instruction compréhensible par le processeur.

Suivant le processeur, il existe divers **mnémoniques**, cependant il existe un langage de programmation proche du processeur et compréhensible par l'être humain : **l'assembleur**.

Il existe diverses opérations, comme en python, que l'on peut distinguer :

**Opérations liées aux valeurs et aux registres**

- **STR X, Val** : Stocke la valeur Val dans le registre X.

- **MOV A B** : Déplace les valeurs d'un registre **A** à un autre **B**.

**Opérations mathématiques**

- **ADD X Y** : Ajouter deux valeurs.
- **SUB X Y** : Soustraire un opérande d'un autre.
- **MUL X Y** : Multiplier deux valeurs.
- **DIV X Y** : Diviser un opérande par un autre.

**Opérations booléennes**

- **AND** : Effectuer une opération logique AND entre deux valeurs.
- **OR** : Effectuer une opération logique OR entre deux valeurs.
- **XOR** : Effectuer une opération logique XOR entre deux valeurs.

**Boucles et conditions**

Pour les boucles, on saute à une certaine étape indiquée dans le code du programme après une comparaison.
Pour les conditions, l'endroit du saut correspond au résultat que l'on souhaite.
On déclare ce que l'on appelle des **ancres** et si la comparaison donne un résultat, on saute à un endroit, sinon à un autre.

- **CMP A B** : Comparer deux valeurs.
- **JE** : Sauter à une autre instruction si les valeurs sont égaux (Jump if Equal).
- **JNE** : Sauter à une autre instruction si les valeurs ne sont pas égaux (Jump if Not Equal).
- **JG** : Sauter à une autre instruction si un opérande est supérieur à l'autre (Jump if Greater).
- **JL** : Sauter à une autre instruction si un opérande est inférieur à l'autre (Jump if Less).

L'assembleur n'est pas au programme, mais il permet de mieux comprendre le fonctionnement d'un ordinateur et le fait qu'il soit un modèle de machine séquentiel.

*Exemple:*

```python
STR A, 15 # Stocke 15 dans A
ADD A, 10 # Ajoute 10 à la valeur dans A
STR B, 10 # Stocke 10 dans B
LOAD A # Met A dans la mémoire active
MUL 10 # Multiplie la valeur dans la mémoire active par 10
STR A # Stocke le résultat de la mémoire active dans A 
CMP A, B
boucle:
JE fin_boucle
STR C, 0
ADD B, 1
ADD C,1
JMP boucle
fin_boucle
```