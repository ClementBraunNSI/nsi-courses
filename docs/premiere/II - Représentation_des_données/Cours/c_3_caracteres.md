# La représentation des caractères

Cette leçon permettra de savoir comment représenter en binaire des caractères textuels.

## Définition

Un caractère est un **symbole** d'écriture représentant en général une **lettre** (A, b, C), un **chiffre** (1,2,3,...) ou un **symbole** (字, Д). 

En informatique, on ne peut pas représenter de but en blanc un caractère de cette manière car **elle ne comprend que des 0 et des 1**.

Il faudra de fait, les coder pour la machine.

Le codage d'un caractère est une association entre celui-ci et une représentation binaire.
On appelle un système de codage est un ensemble de règles pour convertir une information par une autre (ici un caractère avec sa représentation binaire).

## Un système de codage de caractère : ASCII

L'ASCII (American Standard Code for Information Interchange) est un codage qui utilise 7 bits pour représenter des caractères alpha-numériques et d'autres caractères réservés (comme l'espace ou le retour chariot).

En ayant 7 bits pour représenter un caractère, on peut représenter $2^7$ caractères soient 128 caractères.

Pour faciliter la compréhension, on peut dresser une table de correspondance.

| Déc | Hex | Car | Déc | Hex | Car | Déc | Hex | Car | Déc | Hex | Car |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 32  | 20  | (space)  | 48  | 30  | 0   | 64  | 40  | @   | 80  | 50  | P   |
| 33  | 21  | !        | 49  | 31  | 1   | 65  | 41  | A   | 81  | 51  | Q   |
| 34  | 22  | "        | 50  | 32  | 2   | 66  | 42  | B   | 82  | 52  | R   |
| 35  | 23  | #        | 51  | 33  | 3   | 67  | 43  | C   | 83  | 53  | S   |
| 36  | 24  | $        | 52  | 34  | 4   | 68  | 44  | D   | 84  | 54  | T   |
| 37  | 25  | %        | 53  | 35  | 5   | 69  | 45  | E   | 85  | 55  | U   |
| 38  | 26  | &        | 54  | 36  | 6   | 70  | 46  | F   | 86  | 56  | V   |
| 39  | 27  | '        | 55  | 37  | 7   | 71  | 47  | G   | 87  | 57  | W   |
| 40  | 28  | (        | 56  | 38  | 8   | 72  | 48  | H   | 88  | 58  | X   |
| 41  | 29  | )        | 57  | 39  | 9   | 73  | 49  | I   | 89  | 59  | Y   |
| 42  | 2A  | *        | 58  | 3A  | :   | 74  | 4A  | J   | 90  | 5A  | Z   |
| 43  | 2B  | +        | 59  | 3B  | ;   | 75  | 4B  | K   | 91  | 5B  | [   |
| 44  | 2C  | ,        | 60  | 3C  | <   | 76  | 4C  | L   | 92  | 5C  | \   |
| 45  | 2D  | -        | 61  | 3D  | =   | 77  | 4D  | M   | 93  | 5D  | ]   |
| 46  | 2E  | .        | 62  | 3E  | >   | 78  | 4E  | N   | 94  | 5E  | ^   |
| 47  | 2F  | /        | 63  | 3F  | ?   | 79  | 4F  | O   | 95  | 5F  | _   |
| 96  | 60  | `        | 112 | 70  | p   | 128 | 80  | €   | 144 | 90  | É   |
| 97  | 61  | a        | 113 | 71  | q   | 129 | 81  | ‚   | 145 | 91  | ‘   |
| 98  | 62  | b        | 114 | 72  | r   | 130 | 82  | ƒ   | 146 | 92  | ’   |
| 99  | 63  | c        | 115 | 73  | s   | 131 | 83  | „   | 147 | 93  | “   |
| 100 | 64  | d        | 116 | 74  | t   | 132 | 84  | …   | 148 | 94  | ”   |
| 101 | 65  | e        | 117 | 75  | u   | 133 | 85  | †   | 149 | 95  | •   |
| 102 | 66  | f        | 118 | 76  | v   | 134 | 86  | ‡   | 150 | 96  | –   |
| 103 | 67  | g        | 119 | 77  | w   | 135 | 87  | ˆ   | 151 | 97  | —   |
| 104 | 68  | h        | 120 | 78  | x   | 136 | 88  | ‰   | 152 | 98  | ˜   |
| 105 | 69  | i        | 121 | 79  | y   | 137 | 89  | Š   | 153 | 99  | ™   |
| 106 | 6A  | j        | 122 | 7A  | z   | 138 | 8A  | ‹   | 154 | 9A  | š   |
| 107 | 6B  | k        | 123 | 7B  | {   | 139 | 8B  | Œ   | 155 | 9B  | œ   |
| 108 | 6C  | l        | 124 | 7C  | |   | 140 | 8C  |    | 156 | 9C  |    |
| 109 | 6D  | m        | 125 | 7D  | }   | 141 | 8D  |    | 157 | 9D  |    |
| 110 | 6E  | n        | 126 | 7E  | ~   | 142 | 8E  |    | 158 | 9E  |    |
| 111 | 6F  | o        |     |     |     | 143 | 8F  |    | 159 | 9F  |    |

Cependant, à la vue de cette table, on remarque une chose : il n'y a que des symboles d'alphabets latins.
Or, il n'existe pas uniquement les alphabets latins mais aussi le cyrillique ou bien les symboles des alphabets chinois ou japonais.

Pour se faire, on a besoin d'un codage permettant de représenter d'avantage de caractères.

## Un système plus inclusif : Unicode

Unicode est un système de codage de caractère qui utilise un certain nombre de bits en fonction de sa version, plus connu sous le nom de UTF.

On utilise plus souvent le système UTF-8 qui utilise 8 bits pour représenter des caractères. Il peut cependant utiliser 1, 2 voire même 3 groupes de 8 bits (octets) pour représenter d'avantages de caractères.

Chaque symbole possède un **point de code**, qui est l'ensemble des bits permettant sa représentation, souvent représenté en **hexadécimal**.

On peut citer par exemple les caractères 풪 pour point de code *052A*, A (a majuscule) pour point de code *41* ou encore ᛒ (lettre B runique) pour point de code **16D2**.

**Remarque :** Python utilise l'encodage UTF-8 pour coder ses symboles et les représenter. Il est possible cependant d'observer un encodage spécial sur une chaîne de caractère en utilisant la méthode `encode` des chaînes de caractères.

On retrouvera la table UTF-8 à cette adresse : [Table UTF-8](https://www.charset.org/utf-8).