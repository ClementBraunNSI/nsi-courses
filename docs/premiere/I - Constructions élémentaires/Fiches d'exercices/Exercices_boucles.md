# Fiche d'exercices : Boucles

**Écrire un programme qui affiche dans le terminal tous les nombres entre 1 et 100. (à l'aide d'une boucle for puis d'une boucle tant que).**

??? fox_correction "Correction"

    ```python
    # Utilisation d'une boucle for
    for i in range(1, 101):
     print(i)

    # Utilisation d'une boucle while
    i = 1
    while i <= 100:
        print(i)
        i += 1
    ```

**Écrire un programme qui affiche dans le terminal tous les nombres pairs entre 1 et 100.**

??? fox_correction "Correction"

    ```python
     # Utilisation d'une boucle for
    for i in range(1, 101):
        if i % 2 == 0 :
            print(i)

    # Utilisation d'une boucle while
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1
    ```

**Écrire un programme qui prend un nombre entier et affiche sa table de multiplication (jusqu'à 10).**

??? fox_correction "Correction"

    ```python
    # Saisie d'un nombre entier
    nombre = int(input("Entrez un nombre entier: "))

    # Affichage de la table de multiplication
    for i in range(1, 11):
        print(i, " x ", nombre , " = ", i*nombre)
    ```

**Écrire un programme qui réalise la somme des nombres entiers de 1 jusque 100.**

??? fox_correction "Correction"

    ```python
    somme = 0
    for i in range(1,101):
        somme = somme + i
    print("La somme de 1 à 100 est", somme)
    ```

**Écrire un programme qui lit une chaîne de caractères et affiche le nombre de voyelles présentes dans cette chaîne.**
??? fox_correction "Correction"

    ```python
    phrase = input("Donnez votre phrase")
    nb_voyelles = 0
    for lettre in phrase:
        if lettre == 'a' or lettre == 'e' or lettre == 'i' or lettre == 'o' or lettre == 'u' or lettre == 'y':
            nb_voyelles = nb_voyelles + 1
    print("La phrase compte ", nb_voyelles, " voyelles." )
    ```

**Écrire un programme qui affiche les caractères d'une chaîne de caractères dans l'autre sens.**
*Exemple : si ce programme réalise le traitement sur la chaîne "bonjour", il affichera "ruojnob".
??? fox_correction "Correction"

    ```python
    phrase = input("Donnez votre phrase")
    resultat = ""
    for carac in phrase:
        resultat = carac + resultat
    print(resultat)
    ```

**Écrire un programme qui calcule la somme des chiffres d'un nombre donné par l'utilisateur (ex : pour 123, il affichera 6).**
??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    resultat = 0
    for chiffre in nombre:
        a_ajouter = int(chiffre)
        resultat = resultat + a_ajouter
    print(resultat)
    ```

**Écrire un programme qui demande en boucle un nombre à l'utilisateur. Si le nombre est positif, la boucle continue, si le nombre est négatif, la boucle s'arrête.**
??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    nombre = int(nombre)
    while nombre > 0:
        nombre = input("Donnez votre nombre")
        nombre = int(nombre)
        print(nombre)
    ```

**Écrire un programme qui demande à l'utilisateur un nombre et affiche les multiples par 3 consécutifs.**
*Exemple : $1 \rightarrow 3,9,27,81...$*
??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    nombre = int(nombre)
    i = 0
    while i < 10:
        nombre = nombre * 3
        print(nombre)
        i = i+1
    ```

**Écrire un programme qui demande un nombre à l'utilisateur et affiche dans le terminal combien de fois celui-ci est divisible par 2.**
??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    nombre = int(nombre)
    compteur = 0
    while nombre > 1 and nombre != 1:
        nombre = nombre // 2
        compteur = compteur + 1
    ```

**Écrire un programme qui demande un nombre `n` à un utilisateur et affiche dans le terminal ses diviseurs (autre que lui-même et 1). S'il n'en a aucun, affiche dans le terminal "Aucun, `n` est premier".**
*Exemple : $12 \rightarrow 2~3~4~6$ et $13 \rightarrow \texttt{Aucun diviseur, 13 est premier}$*
??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    nombre = int(nombre)
    nombre_diviseurs = 0
    i = 1
    while i != nombre:
        if nombre % i == 0:
            print(i, " divise ", nombre)
            nombre_diviseurs = nombre_diviseurs + 1
        i = i + 1
    # Si 2 diviseurs uniquement : il est divisible par 1 et par lui même uniquement
    if nombre_diviseurs == 2:
        print("Aucun diviseur, ", nombre, " est premier.")
    ```

**Écrire un programme qui réalise la conjecture de Syracuse pour un nombre demandé par l'utilisateur. Tant que le nombre n'est pas 1, s'il est pair on le divise par 2 sinon on le multiplie par 3 et on rajoute 1.**

*Exemple :* $10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$.

??? fox_correction "Correction"

    ```python
    nombre = input("Donnez votre nombre")
    nombre = int(nombre)
    while nombre != 1:
        print(nombre)
        if nombre % 2 == 0 : 
            nombre = nombre // 2
        else:
            nombre = (nombre * 3) + 1
    ```