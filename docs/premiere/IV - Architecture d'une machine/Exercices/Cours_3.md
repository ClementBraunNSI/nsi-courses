# Jeux d'instruction

## Définitions

Un jeu d'instruction correspond à l'ensemble des opérations réalisables et câblées pour un processeur donné.

Les processeurs, par leur composition ne comprennent que le binaire mais le système d'exploitation permet de traduire les langages de programmation en opérations compréhensibles par le processeur.
On appelle **mnémonique** une instruction compréhensible par le processeur.

Suivant le processeur, il existe divers **mnémoniques**, cependant il existe un langage de programmation proche du processeur et compréhensible par l'être humain : **l'assembleur**.

Il existe diverses opérations, comme en python, que l'on peut distinguer :

**Opérations liées aux valeurs et aux registres**

- **MOV A B** : Transférer des données d'un registre **A** à un autre **B**, ou entre la mémoire et un registre.

**Opérations mathématiques**

- **ADD X Y** : Ajouter deux opérandes.
- **SUB X Y** : Soustraire un opérande d'un autre.
- **MUL X Y** : Multiplier deux opérandes.
- **DIV X Y** : Diviser un opérande par un autre.

**Opérations booléennes**

- **AND** : Effectuer une opération logique AND entre deux opérandes.
- **OR** : Effectuer une opération logique OR entre deux opérandes.
- **XOR** : Effectuer une opération logique XOR entre deux opérandes.

**Boucles et conditions**

Pour les boucles, on saute à une certaine étape indiquée dans le code du programme après une comparaison.
Pour les conditions, l'endroit du saut correspond au résultat que l'on souhaite.
On déclare ce que l'on appelle des **ancres** et si la comparaison donne un résultat, on saute à un endroit, sinon à un autre.

- **CMP A B** : Comparer deux opérandes.
- **JE** : Sauter à une autre instruction si les opérandes sont égaux (Jump if Equal).
- **JNE** : Sauter à une autre instruction si les opérandes ne sont pas égaux (Jump if Not Equal).
- **JG** : Sauter à une autre instruction si un opérande est supérieur à l'autre (Jump if Greater).
- **JL** : Sauter à une autre instruction si un opérande est inférieur à l'autre (Jump if Less).

```assembly
    mov eax, 5      ; x = 5
    mov ebx, 10     ; y = 10

    cmp eax, ebx    ; Comparer x et y
    JLE else_part   ; Sauter à else_part si x <= y

    ; Si x > y, exécuter ce code
    mov eax, 4
    mov ebx, 1
    mov ecx, msg_greater
    mov edx, 20
    int 0x80
    JMP end_if      ; Sauter à end_if après le bloc if

    else_part:
        ; Si x <= y, exécuter ce code
        mov eax, 4
        mov ebx, 1
        mov ecx, msg_not_greater
        mov edx, 24
        int 0x80

    end_if:
        ; Fin du programme
        mov eax, 1
        xor ebx, ebx
        int 0x80
```

L'assembleur n'est pas au programme, mais il permet de mieux comprendre le fonctionnement d'un ordinateur et le fait qu'il soit un modèle de machine séquentiel.

## Activité M10

Pour illustrer le fonctionnement d'une machine grâce à l'assembleur, on peut réduire l'ordinateur à un tableau de case ordonnées.
En plus de ce tableau, on se munit d'un jeu d'instructions (pour simplifier : le jeu d'instruction écrit au dessus) et 3 cases supplémentaires représentant 3 registres A B et C.

En suivant le modèle ci-dessous,