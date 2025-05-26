# Devoir Surveillé 2 : Listes et Dictionnaires en Python

## Exercice 1 : Relevés de températures (6 points)

!!! fox_correction_eval "Moyenne des températures"
    ```python
    def moyenne(temperatures: list) -> float:
        if len(temperatures) == 0:
            return 0
        total = 0
        for temp in temperatures:
            total += temp
        return total / len(temperatures)
    ```

!!! fox_correction_eval "Maximum et jour"
    ```python
    def max_temperature(temperatures: list) -> tuple:
        temp_max = temperatures[0]
        jour = 1
        for i in range(len(temperatures)):
            if temperatures[i] > temp_max:
                temp_max = temperatures[i]
                jour = i + 1
        return (temp_max, jour+1)
    ```

!!! fox_correction_eval "Jours au-dessus du seuil"
    ```python
    def jours_au_dessus_de(temperatures: list, seuil: float) -> list:
        jours = []
        for i in range(len(temperatures)):
            if temperatures[i] > seuil:
                jours.append(i + 1)
        return jours
    ```

!!! fox_correction_eval "Liste sans valeur"
    ```python
    def liste_sans_valeur(temperatures: list, valeur: float) -> list:
        nouvelle_liste = []
        for t in temperatures:
            if t != valeur:
                nouvelle_liste.append(t)
        return nouvelle_liste
    ```

!!! fox_correction_eval "Recherche de voiture"
    ```python
    def recherche_voiture(concessionnaire: list, modele: str) -> list:
        voitures_trouvees = []
        for voiture in concessionnaire:
            if voiture["modele"] == modele:
                voitures_trouvees.append(voiture)
        return voitures_trouvees
    ```

!!! fox_correction_eval "Soldes par énergie"
    ```python
    def soldes_prix_energie(concessionnaire: list, energie: str) -> None:
        for voiture in concessionnaire:
            if voiture["energie"] == energie:
                voiture["prix"] -= 2500
    ```

!!! fox_correction_eval "Prix moyen"
    ```python
    def prix_moyen(concessionnaire: list, energie: str) -> float:
        total = 0
        count = 0
        for voiture in concessionnaire:
            if voiture["energie"] == energie:
                total += voiture["prix"]
                count += 1
        if count == 0:
            return 0
        return total / count
    ```

!!! fox_correction_eval "Modèle le plus cher"
    ```python
    def modele_le_plus_cher(concessionnaire: list) -> str:
        plus_cher = concessionnaire[0]
        for voiture in concessionnaire:
            if voiture["prix"] > plus_cher["prix"]:
                plus_cher = voiture
        return plus_cher["modele"]
    ```

## Exercice 3 : Gestion d'un Refuge de Renards (6 points)

!!! fox_correction_eval "Ajouter un renard"
    ```python
    def ajouter_renard_listes(renards: list, nouveau_renard: list) -> None:
        renards.append(nouveau_renard)
    ```

!!! fox_correction_eval "Modifier un renard"
    ```python
    def modifier_renard_listes(renards: list, id: int, nom: str, race: str) -> None:
        for renard in renards:
            if renard[0] == id:
                renard[1] = nom
                renard[3] = race
    ```

!!! fox_correction_eval "Afficher les renards rouges"
    ```python
    def afficher_renards_rouges(renards: list) -> None:
        for renard in renards:
            if renard[3] == "Rouge":
                print(renard)
    ```

!!! fox_correction_eval "Explication liste vs dictionnaire"
    Dans une liste de listes, il faut connaître l'indice exact de chaque information (nom à l'indice 1, race à l'indice 3, etc.).
    Cela rend le code moins lisible et plus sujet aux erreurs. De plus, si on veut ajouter une nouvelle information,
    il faut modifier tous les endroits où on manipule ces listes.
    
    Avec un dictionnaire, on accède aux informations par leur nom ("nom", "race", etc.), ce qui rend le code plus
    lisible et plus facile à maintenir. On peut aussi facilement ajouter de nouvelles informations sans impacter
    le code existant.

!!! fox_correction_eval "Conversion en dictionnaires"
    ```python
    def listes_listes_vers_listes_dict(renards: list) -> list:
        cles = ['id', 'nom', 'espece', 'race', 'sexe']
        resultat = []
        for renard in renards:
            nouveau_dict = {}
            for i in range(len(cles)):
                nouveau_dict[cles[i]] = renard[i]
            resultat.append(nouveau_dict)
        return resultat
    ```

!!! fox_correction_eval "Modification version dictionnaire"
    ```python
    def modifier_renard_dict(renards_dict: list, id: int, nom: str, race: str) -> None:
        for renard in renards_dict:
            if renard['id'] == id:
                renard['nom'] = nom
                renard['race'] = race
    ```