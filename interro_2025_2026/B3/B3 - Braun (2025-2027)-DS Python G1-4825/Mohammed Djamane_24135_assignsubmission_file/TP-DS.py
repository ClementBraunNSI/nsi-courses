Python 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] on linux
Enter "help" below or click "Help" above for more information.
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c >= 0:
            compteur = c + 1

        
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c >= digits:
            compteur = c + 1
    return digits

nb_chiffres(mot)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    nb_chiffres(mot)
NameError: name 'mot' is not defined
nb_chiffres(5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nb_chiffres(5)
  File "<pyshell#9>", line 4, in nb_chiffres
    for c in chaine:
TypeError: 'int' object is not iterable
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = digits - c
    return compteur

nb_chiffres(012345)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
nb_chiffres(12345)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    nb_chiffres(12345)
  File "<pyshell#12>", line 4, in nb_chiffres
    for c in chaine:
TypeError: 'int' object is not iterable
nb_chiffres(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nb_chiffres(c)
NameError: name 'c' is not defined
nb_chiffres(chaine)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nb_chiffres(chaine)
NameError: name 'chaine' is not defined
nb_chiffres("chaine")
0
nb_chiffres("12345")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    nb_chiffres("12345")
  File "<pyshell#12>", line 6, in nb_chiffres
    compteur = digits - c
TypeError: unsupported operand type(s) for -: 'str' and 'str'
nb_chiffres("c")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c > 0:
            compteur = digits
    return compteur

nb_chiffres("chaine")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nb_chiffres("chaine")
  File "<pyshell#21>", line 5, in nb_chiffres
    if c > 0:
TypeError: '>' not supported between instances of 'str' and 'int'
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = digits - c
    return compteur

nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = c + 1
    return compteur

nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c >= 0:
            compteur = c + 1
    return compteur


nb_chiffres("digits")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    nb_chiffres("digits")
  File "<pyshell#29>", line 5, in nb_chiffres
    if c >= 0:
TypeError: '>=' not supported between instances of 'str' and 'int'
nb_chiffres("5")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nb_chiffres("5")
  File "<pyshell#29>", line 5, in nb_chiffres
    if c >= 0:
TypeError: '>=' not supported between instances of 'str' and 'int'
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c == digits:
            compteur = c + 1
    return compteur

nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if len(c):
            compteur = c + 1
    return compteur

nb_chiffres("digits")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nb_chiffres("digits")
  File "<pyshell#37>", line 6, in nb_chiffres
    compteur = c + 1
TypeError: can only concatenate str (not "int") to str
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if len(digits):
            compteur = c + 1
    return compteur

nb_chiffres("digits")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    nb_chiffres("digits")
  File "<pyshell#40>", line 6, in nb_chiffres
    compteur = c + 1
TypeError: can only concatenate str (not "int") to str
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in len(digits):
            compteur = c + 1
    return compteur

nb_chiffres("digits")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nb_chiffres("digits")
  File "<pyshell#43>", line 5, in nb_chiffres
    if c in len(digits):
TypeError: argument of type 'int' is not iterable
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = "digits" + 1
    return compteur

nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = "0123456789" + 1
    return compteur

nb_chiffres()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    nb_chiffres()
TypeError: nb_chiffres() missing 1 required positional argument: 'chaine'
nb_chiffres(chaine)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    nb_chiffres(chaine)
NameError: name 'chaine' is not defined
nb_chiffres("chaine")
0
nb_chiffres("digits")
0
nb_chiffres("0")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    nb_chiffres("0")
  File "<pyshell#49>", line 6, in nb_chiffres
    compteur = "0123456789" + 1
TypeError: can only concatenate str (not "int") to str
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = "c" + 1
    return compteur

nb_chiffres("0")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    nb_chiffres("0")
  File "<pyshell#56>", line 6, in nb_chiffres
    compteur = "c" + 1
TypeError: can only concatenate str (not "int") to str
nb_chiffres("digits")
0

def repeter_caractere(c: str,n: int):
    a = c * n
    print(a)

    
repeter_caractere('c',5)
ccccc
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = len(c)
    return compteur

nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = len(digits)
    return compteur

nb_chiffres("12")
10
nb_chiffres("digits")
0
nb_chiffres("0")
10
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = len(c)
    return compteur

nb_chiffres("0")
1
nb_chiffres("c")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c == len(digits):
            compteur = c
    return compteur

nb_chiffres("c")
0
nb_chiffres("0")
0
nb_chiffres("digits")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if digits in c:
            compteur = len(c)
    return compteur

nb_chiffres("digits")
0
nb_chiffres("0")
0
nb_chiffres("c")
0
def nb_chiffres(chaine: str) -> int:
    compteur = 0
    digits = "0123456789"
    for c in chaine:
        if c in digits:
            compteur = compteur + 1
    return compteur

nb_chiffres("0")
1
nb_chiffres("158")
3
def nb_lettres(chaine: str) -> int:
    compteur = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in chaine
    
SyntaxError: expected ':'
def nb_lettres(chaine: str) -> int:
    compteur = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in chaine
    
SyntaxError: expected ':'
def nb_lettres(chaine: str) -> int:
    compteur = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in chaine:
        if c in alphabet:
            compteur = compteur + 1
    return compteur

nb_lettres(chaine)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    nb_lettres(chaine)
NameError: name 'chaine' is not defined
nb_lettres("chaine")
6
def contient_majuscule(chaine: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in chaine:
        if c in maj:
            return true
        return false

    
contient_majuscule("ABCD")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    contient_majuscule("ABCD")
  File "<pyshell#109>", line 5, in contient_majuscule
    return true
NameError: name 'true' is not defined. Did you mean: 'True'?
def contient_majuscule(chaine: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in chaine:
        if c in maj:
            return true
        else:
            return false

        
contient_majuscule("ABCD")
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    contient_majuscule("ABCD")
  File "<pyshell#112>", line 5, in contient_majuscule
    return true
NameError: name 'true' is not defined. Did you mean: 'True'?
def contient_majuscule(chaine: str) -> bool:
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
...     for c in chaine:
...         if c in maj:
...             return True
...         else:
...             return False
... 
...         
>>> contient_majuscule("ABCD")
True
>>> contient_majuscule("fff")
False
>>> def contient_special(chaine: str) -> bool:
...     specials = "!@#$%^&*?"
...     for c in chaine:
...         if c in specials:
...             return True
...         else:
...             return False
... 
...         
>>> contient_special("*$")
True
>>> contient_special("ù")
False
>>> def contient_deux_types(chaine: str) -> bool:
...     if nb_lettres(chaine) > 10:
...         a_lettre =
...         
SyntaxError: invalid syntax
>>> def contient_deux_types(chaine: str) -> bool:
...     if nb_lettres(chaine) > 10:
...         a_lettre = nb_lettres(chaine)
...     else:
...         a_lettre = nb_lettres(chaine)
... if nb_chiffres(chaine) > 10:
... a_chiffre = nb_chiffres(chaine)
... else:
... a_chiffre = nb_chiffres(chaine)
... a_special = contient_special(chaine)
... if (a_lettre and a_chiffre) or (a_lettre and a_special) or (a_chiffre and a_special):
... return True
... return False
SyntaxError: invalid syntax
