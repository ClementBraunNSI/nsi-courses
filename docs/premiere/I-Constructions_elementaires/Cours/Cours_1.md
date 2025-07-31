# 📚 Constructions élémentaires en Python

## 📖 Qu'est ce qu'un programme ?

**Défintion:** On définit un **programme** comme étant une suite d'instruction élémentaires destinées à être exécutées par un ordinateur.

Le langage python est un langage dit de haut niveau. Cela veut dire qu'il est plus proche de nous (utilisateurs) que de l'ordinateur (du processeur).

Ce langage est basé sur nos ordinateurs qui réalisent des instructions de manière séquentielle (c'est à dire réalisées les unes après les autres).

On peut dénombrer un certain nombre d'instructions élémentaires qui permettent de créer un programme.
Ces instructions élémentaires peuvent utiliser des opérateurs.

**Définition:** Un opérateur est un caractère ou un ensemble de caractère qui correspond à une opération pouvant être réalisée par le processeur.

## 📖 Instanciation

L'instanciation est une instruction qui permet d'associer une **valeur** à une **variable**.
Une variable en python est une chaîne de caractère que l'on associe à une **type** (domaine de valeurs).

L'instanciation utilise l'opérateur `=`.
Pour la machine, cela revient à associer un espace mémoire à la valeur désignée.

Par exemple :

```python
# Instancier a à la valeur 42
a = 42

#Instancier ma_chaine_de_caractere à la valeur 'Hello World!'
ma_chaine_de_caractere = 'Hello World!'
```

On a donc ici, l'explicitation des types entiers ou chaînes de caractères mais il en existe un certain nombre : tableaux, listes, nombres réels (réels à virgule flottante) ou d'autres objets que l'on peut créer nous même.

Cette opération est la base de la programmation. On utilisera le terme **instancier** pour définir le fait d'associer à une variable une valeur donnée.

## 📖 Opérations mathématiques

Le langage python est un langage informatique. En informatique, il est nécessaire de réaliser des opérations qui peuvent être du domaine mathématique.

Il existe un certain nombre d'opérations mathématiques qui sont associées à des opérateurs.
On peut citer :

- $+$: addition
- $-$: soustraction
- $\ast$: multiplication
- $/$ : division

Ces opérateurs utilisent 2 valeurs, à l'instar de nos opérations que l'on peut écrire sur papier.
Il en parait nécessaire d'instancier une variable à une opération, comme par exemple nos fonctions mathématiques $y = 3x+2$.

Par exemple:

```python
a = 3 + 2 
b = 5 - 3
c = a * b
d = b / a
```

Les exemples précédents montrent que l'on peut réaliser des opérations sur les différentes variables que l'on a déjà créée.

Il faut cependant prendre compte d'une chose importante : **le type des variables utilisées**.
En effet, les opérations **mathématiques** sont réservées à des variables de type entiers ou nombres réels. Il faut cependant faire attention aux nombres réels (flottants) à cause des imprécisions (cf cours précédent).

## 📖 Opérations de comparaisons

Comme les opérations mathématiques, il est possible de réaliser des comparaisons sur des variables.

> **⚠️ Attention**
> **On ne peut comparer des éléments uniquement s'ils sont du même type** !  
> Si jamais lors d'un programme on compare deux éléments de types différents, on pourrait faire face à ce que l'on appelle une erreur (**TypeError**).

Il existe un certain nombre d'opérateurs en python qui permettent de réaliser des comparaisons.  

On peut citer :

- $a > b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand que b).
- $a < b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit que b).
- $a >= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus grand ou égal à b).
- $a <= b$ : Cet opérateur correspond à une comparaison d'ordre (a plus petit ou égal à b).
- $a == b$ : Cet opérateur correspond à une comparaison : a est égal à b.

> **⚠️ Attention**
> Il ne faut pas confondre les opérateurs $=$ et $==$.
> En effet, $=$ ne sera utilisé uniquement lors d'**instanciation** de variables. Utiliser l'opérateur $=$ lors d'une **comparaison** peut mener à des erreurs! (**SyntaxError**).

## 📖 Affichage et Demande à l'utilisateur

La fonction `print()` est utilisée pour afficher des informations à l'écran.  
Elle peut afficher des chaînes de caractères, des nombres, ou même les résultats de calculs.  
On peut également concaténer plusieurs éléments à afficher en les séparant par des virgules dans l'appel à print().  
Par exemple, print("Bonjour", "le monde", 42) affichera "Bonjour le monde 42" dans la console.

D'un autre côté, la fonction input() permet de capturer des données saisies par l'utilisateur.  
Elle prend en argument une chaîne de caractères qui est affichée comme un message à l'utilisateur pour l'inviter à entrer une valeur.  
La valeur saisie par l'utilisateur est ensuite renvoyée sous forme de chaîne de caractères.  
Par exemple, nom = input("Quel est votre nom ? ") demandera à l'utilisateur de saisir son nom, qui sera ensuite stocké dans la variable nom.  

> **⚠️ Attention**
> Attention ! La fonction input permet de stocker l'entrée de l'utilisateur dans une variable mais celle-ci sera forcément du type `string`.
> Si l'on souhaite traiter des nombres, il faudra alors modifier le type de la valeur à l'aide des fonctions le permettant.

## 📖 Conditions

Une condition est réalisable en python grâce à l'instruction `if`.

Cette condition permet d'évaluer des comparaisons, des états de variables ou des valeurs associées à des variables.
Si cette condition est validée, alors le bout de code associé est exécuté, sinon il peut exister un bloc de code associé au mot-clef `else`.

Par exemple, on souhaite réaliser un affichage suivant une valeur d'une variable âge qui correspond à l'âge de l'utilisateur qu'il renseigne.

```python
# Demander à l'utilisateur son age
age = input('Quel est votre âge?')

# Lors d'une demande à l'aide d'input, on reçoit une chaîne de caractères, on doit la convertir en entier
age_entier = int(age)

# Condition d'affichage
if age_entier > 18 :
    print('Vous êtes majeur')
else:
    print('Vous êtes mineur')
```

Ce bout de code permet d'afficher si l'utilisateur est majeur ou mineur.

On remarque la présence du bloc else.
Cependant, il existe un autre bloc permettant de réaliser des conditions si une condition n'est pas déjà validée. Ce bloc est le `elif`.

Par exemple, on va réaliser un programme qui permet de mettre une appréciation à une note.

```python
# On demande à l'utilisateur une note (A,B,C)
note = input('Quelle est la note à évaluer?')

if note == 'A' :
    print('Très bien')
elif note == 'B':
    print('Un peu plus pour exceller')
else:
    print("Poursuis tes efforts")
```

> **⚠️ Attention**
> On remaraque que l'on a un bloc elif. Celui-ci est exécuté si la première condition n'est pas validée et ainsi de suite. On peut enchaîner autant de bloc `elif` que nécessaire.
>
> Cependant il faut faire attention au nombre de conditions réalisées car trop détailler peut ralentir la vitesse à laquelle on attend une réponse.
> Chaque condition est évaluée jusqu'à trouver une qui est valide, ou rentrer dans le `else`.

> **💡 Astuce**
> Le bloc `else` n'est pas obligatoire s'il ne doit rien faire. On peut l'omettre
> ```python
> age = 36
> if age < 40:
>     print("Vous êtes né après 1980")
> else:
>     print('')
> ```
> Ici, print('') ne sert pas à grand chose, on peut l'omettre.
> ```python
> age = 36
> if age < 40 :
>     print('Vous êtes né après 1980')
> ```

## 📖 Boucles

Une boucle en python est la répétition d'une certaine partie d'un algorithme un certain nombre de fois ou suivant la validation d'une condition.

Il existe plusieurs types de boucles en python.

### La boucle while

La boucle `while` correspond à une boucle qui s'exécute `tant que` la condition choisie est valide.

Par exemple, on peut réaliser un bout de code tant qu'un nombre est positif, tant qu'un tableau n'est pas vide, tant qu'une chaîne de caractère n'est pas vide ou bien par exemple tant qu'une condition booléenne est valide.

On peut associer la syntaxe python suivante:

```python
n = 30
i = 1
# On veut afficher les nombres de 1 à n choisi en faisant croître un entier i.
while i <= n:
    print(i)
    i = i + 1
```

Ici, ce bout de code incrémente 1 jusqu'à ce qu'il soit supérieur à n. Cela veut dire que la boucle va se dérouler tant que i est inférieur ou égal à n.

> **⚠️ Attention**
> Une boucle `while` peut ne pas s'arrêter !
> Il faut vérifier que la condition est valide jusqu'au point désiré. On parle de **terminaison de boucle**.
> Par exemple, on peut réaliser une boucle infinie en écrivant `while True` ou bien en ayant une condition qui traite un entier positif et ne jamais le décrémenter.

### La boucle for

Il existe un autre type de boucle en python : la boucle `for`.

Une boucle for est une boucle que l'on nomme `boucle pour`. Cette boucle s'exécute à l'aide d'une variable qui va évoluer par rapport à un objet itérable ou une valeur.
Par exemple cette boucle est utilisée peut être utilisée pour chaque valeur d'un tableau, pour une valeur jusqu'une borne etc...

Par exemple :

```python
n = 30
for i in range(1,n+1):
    print(i)
```

Cette boucle permet d'afficher les entiers de 1 à n.
Elle va itérer jusqu'à ce que n soit égal à n et s'arrêter à n+1 avec l'utilisation de la fonction `range`.

> **💡 Astuce**
> La boucle `for` a un net avantage : Elle s'arrête forcément.
> En effet, la boucle `for` itère sur un objet itérable ou sur une variable donc sur un certain nombre d'itération donné.