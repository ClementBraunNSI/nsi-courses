# 📚 Dictionnaires en Python

## 📖 Définition - Définitions

Une des nombreuses structures de Python est **le dictionnaire**.

Le dictionnaire est une structure de données qui n'est pas indexée mais organisées suivant des éléments que l'on nomme **attributs (ou descripteur)**.
Ces attributs correspondent à des propriétés sur l'élément que l'on souhaite modéliser.

*Exemple*:
Par exemple, on souhaite modéliser un modèle de voiture. Lors de la conception d'une voiture, on peut modifier des éléments pour en créer des déclinaisons.
On peut, pour un modèle, dresser un tableau des diverses propriétés à modéliser :

|propriété|valeurs possibles|
|---------|------------------|
|couleurs | rouge, bleu, vert, noir, blanc, gris|
|motorisations (en ch)| 100, 110,120,200|
|taille de jantes|16,17,18,19|

Pour créer ce genre d'objets, on utilise donc la structure des dictionnaires.

## 📖 Définition - Les dictionnaires en Python

Pour créer un dictionnaire, on utilise les accolades **{}** (à la différence des tableaux (parenthèses **(   )**) ou des listes (crochets **[   ]**)).
À l'intérieur de ces accolades, on utilise la syntaxe **attribut : valeurs possibles**.

Un attribut correspond donc à une propriété d'un objet que l'on cherche à modéliser et est représenté par une chaîne de caractères.

Les différentes valeurs possibles peuvent être de types simples (entier, chaines de caractère, booléen) mais aussi de types plus complèxes (listes, dictionnaires ou tuples).

Chacun des couples *attributs : valeurs* sont séparés par des virgules.

De base, un dictionnaire lorsqu'on le créée de cette manière, est dépourvu d'attributs.
Pour créer un dictionnaire avec des attributs déjà connus, il existe deux méthodes :

**Écrire les propriétés déjà connues à l'instanciation**

```python
modele_voiture = {  "couleurs" : ["rouge", "bleu", "vert", "noir", "blanc", "gris"],
                    "motorisation_en_ch" : [100,110,120,200],
                    "taille_jantes" : [16,17,18,19]
                 }
```

**Rajouter petit à petit les propriétés**

```python
modele_voiture = {}

modele_voiture["couleurs"] = ["rouge", "bleu", "vert", "noir", "blanc", "gris"]
modele_voiture["motorisation_en_ch"] = [100,110,120,200]
modele_voiture["taille_jantes"] = [16,17,18,19]
```

Pour accéder à un attribut du dictionnaire, on utilise la structure à crochets comme pour les listes, mais au lieu d'indiquer un indice, on indique l'attribut s'il est déjà renseigné.

Voici l'usage principal des dictionnaires en Python :

```python
# Pour afficher le dictionnaire complet
print(modele_voiture)

# Pour afficher les couleurs disponibles pour le modèle
print(modele_voiture["couleurs"])

# Pour rajouter des couleurs à celles existantes
modele_voiture["couleurs"] = modele_voiture["couleurs"] + ["beige"]

# Pour retirer une clef et ses valeurs d'un dictionnaire
modele_voiture.pop("taille_jantes")
```

> **⚠️ Ajout de valeurs**
> Pour rajouter des valeurs à un attribut d'un dictionnaire, il faut bien faire attention aux types.
> Par exemple, pour l'exemple précédent, nos valeurs étaient contenues dans des listes. Il faut donc opérer par concaténation de liste avec l'opérateur **+** ou la méthode `.append(valeur)`.

## 📖 Définition - Opérations sur les dictionnaires

### Itérations sur un dictionnaire

Tout comme les listes et les tableaux, on peut itérer sur les valeurs d'un dictionnaire. Cela permet de retrouver des valeurs, de faire des traitements sur des bases de données ou retrouver des valeurs suivant certaines conditions.

Le plus simple est d'itérer à l'aide d'une boucle `for`.
Un dictionnaire est une structure sur laquelle on peut itérer sur les clefs (à l'instar des tuples ou listes où l'on itère sur les indices).

```python
    # Afficher les clefs du dictionnaire
    for clef in modele_voiture:
        print(clef)

    #Afficher toutes les valeurs d'un dictionnaire
    for clef in modele_voiture:
        print(clef)
        for valeur in modele_voiture[clef]:
            print(valeur)
```

### Vérification de la présence d'une clef

L'opérateur `in` permet de vérifier si une clef existe dans le dictionnaire.

```python
    if "couleurs" in modele_voiture:
        print("La clé 'couleurs' existe dans le dictionnaire")
    else:
        print("La clé 'couleurs' n'existe pas dans le dictionnaire")
```

Cela permet de savoir si, par exemple on modifie une base de données pour la rendre plus conséquente, la modification a bien été réalisée.