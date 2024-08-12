# Dictionnaires en Python

## Défintions

Une des nombreuses structures de Python est **le dictionnaire**.

Le dictionnaire est une structure de données qui n'est pas indexée mais organisées suivant des éléments que l'on nomme **attributs**.
Ces attributs correspondent à des propriétés sur l'élément que l'on souhaite modéliser.

*Exemple*:
Par exemple, on souhaite modéliser un modèle de voiture. Lors de la conception d'une voiture, on peut modifier des éléments pour en créer des déclinaisons.
On peut, pour un modèle, dresser un tableau des diverses propriétés à modéliser :

|propriété|valeurs possibles|
|---------|-----------------|
|couleurs | rouge, bleu, vert, noir, blanc, gris|
|motorisations (en ch)| 100, 110,120,200|
|taille de jantes|16,17,18,19|

Pour créer ce genre d'objets, on utilise donc la structure des dictionnaires.

Pour créer un dictionnaire, on utilise les accolades **{}** la différence des tableaux (parenthèses **(   )**) ou des listes (crochets **[   ]**).
À l'intérieur de ces crochets, on utilise la syntaxe **attribut : valeurs possibles**. 
Chacun des attributs sont séparés par des virgules.

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

```python
# Pour afficher le dictionnaire complet
print(modele_voiture)

# Pour afficher les couleurs disponibles pour le modèle
print(modele_voiture["couleurs"])

# Pour rajouter des valeurs à un attribut
modele_voiture["couleurs"] = modele_voiture["couleurs"] + ["beige"]

# Pour retirer une clef et ses valeurs d'un dictionnaire
modele_voiture.pop("taille_jantes")
```

!!! Warning Attention pour rajouter des valeurs
    Pour rajouter des valeurs à un attribut d'un dictionnaire, il faut bien faire attention aux types.
    Par exemple, pour l'exemple précédent, nos valeurs étaient contenues dans des listes. Il faut donc opérer par concaténation de liste avec l'opérateur **+**.
