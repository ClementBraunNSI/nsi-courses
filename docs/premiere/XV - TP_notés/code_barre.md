# Vérification d'un Code-barres

## Contexte :
Les codes-barres sont omniprésents dans notre quotidien, utilisés pour identifier des produits dans les magasins, les bibliothèques, et bien d'autres domaines. Dans ce TP, vous allez apprendre à vérifier la validité d'un code-barres en vous familiarisant avec son format et ses règles.

## Objectif :
Développer un programme en Python qui permet de vérifier si un code-barres est correct en fonction des spécifications des codes-barres standards (par exemple, EAN-13).

## Exemple du calcul de la clé de contrôle

Nous allons étudier  le **Code EAN-13** : **4006381333936**

## Décomposition :
- **400** : 3 chiffres dédié au code pays (ici c'est celui de l'Allemagne);
- **6381** : 4 chiffres dédidés au code du fabricant;
- **33393** : 5 chiffre pour le numéro du produit;
- **6** : 1 chiffre dédié pour la clé de contrôle (qu'on devra vérifier)

## Calcul de la clé de contrôle :
1. Prenons les 12 premiers chiffres : **400638133393**.
2. Calculez la somme des :
   - Chiffres en position impaire (1, 3, 5, 7, 9, 11) : 4 + 0 + 6 + 1 + 3 + 3 = **17**
   - Chiffres en position paire (2, 4, 6, 8, 10, 12) : 0 + 6 + 8 + 3 + 9 + 3 = **29**

		**attention ce n'est pas les indices dans le sens python ici.**
3. Multipliez la somme des positions paires par 3 : 29 × 3 = **87**
4. Additionnez la sommes des positions paires par 3 et la sommes des chiffres en position impaire : 17 + 87 = **104**
5. Calculez le modulo 10 de la somme trouvé à l'étape précédente : 104 % 10 = **4**
6. Pour trouver la clé de contrôle il faut soustraire le résultat précédent à 10 : 10 - 4 = **6** (si c'était 10, la clef serait 0)

## Validation :
Dans cet exemple, la clé de contrôle calculée est **6**, et la clé du code-barres est également **6**. Cela signifie que le code-barres **4006381333936** est **valide**.


## Tâches à réaliser :

1. **Choix du code-barres** :
   - Pour ce TP, vous travaillerez avec le format EAN-13.
   - Un code EAN-13 est composé de 13 chiffres.

2. **Vérification du format** :
   - **Écrire une fonction `verifier_longueur` qui prend en paramètre une chaîne de caractères et renvoie `True` si le code-barres contient exactement 13 chiffres, `False` sinon.**.
   - Vérifier que tous les caractères du code-barres sont des chiffres.

3. **Calcul de la clé de contrôle** :
   - Le dernier chiffre d’un code EAN-13 est une clé de contrôle calculée à partir des 12 premiers chiffres.
   - **Écrire l'algorithme suivant pour calculer la clé de contrôle dans une fonction `verification` qui prend en paramètre un code barre sous forme de chaîne de caractère et renvoie clef associée (entier)**:
     - Multipliez les chiffres en positions impaires par 1 et ceux en positions paires par 3.
     - Additionnez tous les résultats.
     - Calculez le modulo 10 de cette somme.
     - Soustrayez ce résultat de 10. Si le résultat est 10, la clé de contrôle est 0.

4. **Validation du code-barres** :
   - Comparer la clé de contrôle calculée avec le dernier chiffre du code-barres pour déterminer sa validité.
   - **Écrire une fonction qui renvoie `True` si le code-barres est valide, sinon `False`**.

5. **Interface utilisateur** :
   - **Écrire une fonction `main` qui ne prend pas de paramètres, qui demande un numéro de carte bancaire à l'utilisateur et renvoie `True` si elle est valide, `False` sinon. Elle utilisera les fonctions précédentes.**
