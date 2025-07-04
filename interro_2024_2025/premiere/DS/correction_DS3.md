# Devoir Surveillé 3 : Listes, Dictionnaires, Algorithmes et Renards

## Exercice 1 : Analyse du régime alimentaire des renards (6 points)

!!! fox_correction_eval "1. Compter les proies"
    ```python
    def compter_proies(aliments_trouves: list, proie: str) -> int:
        """Compte le nombre d'occurrences d'une proie dans la liste."""
        compteur = 0
        for aliment in aliments_trouves:
            if aliment == proie:
                compteur += 1
        return compteur
    ```

!!! fox_correction_eval "2. Diversité alimentaire"
    ```python
    def diversite_alimentaire(aliments_trouves: list) -> int:
        """Calcule le nombre de types d'aliments différents."""
        aliments_uniques = []
        for aliment in aliments_trouves:
            if aliment not in aliments_uniques:
                aliments_uniques.append(aliment)
        return len(aliments_uniques)
    ```

!!! fox_correction_eval "3. Aliments rares"
    ```python
    def aliments_rares(aliments_trouves: list, seuil: int) -> list:
        """Renvoie la liste des aliments apparaissant moins de 'seuil' fois."""
        frequences = {}
        for aliment in aliments_trouves:
            frequences[aliment] = compter_proies(aliments_trouves, aliment)

        rares = []
        for aliment, freq in frequences.items():
            if freq < seuil:
                rares.append(aliment)
        return rares
    ```

!!! fox_correction_eval "4. Fréquence par période"
    ```python
    def frequence_aliment_periode(aliments_trouves: list, aliment_cible: str, n: int) -> list:
        """Calcule la fréquence d'un aliment par période de n jours/analyses."""
        resultats_periodes = []
        compteur = 0
        for i in range(0, len(aliments_trouves)):
            if aliments_trouves[i] == aliment_cible:
                compteur += 1
            if i % n == 0:
                resultats_periodes.append(compteur)
                compteur = 0
        return resultats_periodes
    ```

## Exercice 2 : Suivi des terriers de renards (6 points)

!!! fox_correction_eval "1. Ajouter un terrier"
    ```python
    def ajouter_terrier(terriers: list, localisation: str, espece: str, nb_renardeaux: int) -> None:
        """Ajoute un nouveau terrier à la liste avec un ID unique."""
        nouvel_id = len(terriers) + 1
        nouveau_terrier = {
            "id_terrier": nouvel_id,
            "localisation": localisation,
            "espece_renard": espece,
            "nombre_renardeaux": nb_renardeaux,
            "actif": True
        }
        terriers.append(nouveau_terrier)
    ```

!!! fox_correction_eval "2. Recherche par espèce"
    ```python
    def recherche_par_espece(terriers: list, espece_recherchee: str) -> list:
        """Renvoie la liste des terriers actifs occupés par une espèce donnée."""
        terriers_trouves = []
        for terrier in terriers:
            if terrier['espece_renard'] == espece_recherchee and terrier['actif'] == True:
                terriers_trouves.append(terrier)
        return terriers_trouves
    ```

!!! fox_correction_eval "3. Désactiver un terrier"
    ```python
    def desactiver_terrier(terriers: list, id_terrier_cible: int) -> bool:
        """Désactive un terrier par son ID."""
        terrier_trouve = False
        for terrier in terriers:
            if terrier['id_terrier'] == id_terrier_cible:
                if terrier['actif'] == True:
                    terrier['actif'] = False
                    return True # Succès de la désactivation
                else:
                    return False # Déjà inactif
        return False # Terrier non trouvé
    ```

!!! fox_correction_eval "4. Renardeaux par espèce"
    ```python
    def renardeaux_par_espece(terriers_actifs: list) -> dict:
        """Compte le nombre total de renardeaux par espèce dans les terriers actifs."""
        compte_par_espece = {}
        for terrier in terriers_actifs:
            if terrier['actif'] == True:
                if terrier['espece_renard'] not in compte_par_espece:
                    compte_par_espece[terrier['espece_renard']] = terrier['nombre_renardeaux']
                else:
                    compte_par_espece[terrier['espece_renard']] += terrier['nombre_renardeaux']
        return compte_par_espece
    ```

## Exercice 3 : Refuge pour renards (6 points)

!!! fox_correction_eval "1. Tri par sélection (âge)"
    ```python
    def tri_renards_age(renards: list) -> list:
        """Trie une liste de renards par âge croissant (tri par sélection)."""
        n = len(renards)
        # Crée une copie pour ne pas modifier la liste originale
        renards_tries = list(renards)
        for i in range(n):
            # Trouver l'indice du minimum dans la partie non triée
            indice_min = i
            for j in range(i + 1, n):
                if renards_tries[j].get('age', float('inf')) < renards_tries[indice_min].get('age', float('inf')):
                    indice_min = j
            # Échanger l'élément courant avec le minimum trouvé
            renards_tries[i], renards_tries[indice_min] = renards_tries[indice_min], renards_tries[i]
        return renards_tries
    ```

!!! fox_correction_eval "2. Recherche dichotomique (ID)"
    ```python
    def recherche_renard_dichotomique(renards_tries_par_id: list, id_recherche: int) -> dict | None:
        """Recherche un renard par ID dans une liste triée par ID (recherche dichotomique)."""
        debut = 0
        fin = len(renards_tries_par_id) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            id_courant = renards_tries_par_id[milieu]["id"]
            # Gérer le cas où l'ID est manquant ou non comparable
            if id_courant is None:
                 if id_recherche < 0:
                     fin = milieu - 1
                 else:
                     debut = milieu + 1
                 continue # Passe à l'itération suivante

            if id_courant == id_recherche:
                return renards_tries_par_id[milieu]
            elif id_courant < id_recherche:
                debut = milieu + 1
            else: # id_courant > id_recherche
                fin = milieu - 1
        return None # Renard non trouvé
    ```

!!! fox_correction_eval "3. Statistiques par espèce"
    ```python
    def statistiques_especes(renards: list) -> dict:
        """Calcule les statistiques (nombre, âge moyen, poids moyen) par espèce."""
        stats = {}
        # Initialisation et accumulation des données
        for renard in renards:
            espece = renard.get('espece')
            if espece:
                if espece not in stats:
                    stats[espece] = {'nombre': 0, 'total_age': 0, 'total_poids': 0.0}
                stats[espece]['nombre'] += 1
                stats[espece]['total_age'] += renard['age']
                stats[espece]['total_poids'] += renard['poids']

        # Calcul des moyennes
        #TODO
        return resultat_final
    ```

!!! fox_correction_eval "4. Renards à surveiller"
    ```python
    def renards_a_surveiller(renards: list) -> list:
        """Renvoie la liste des renards dont le poids est hors normes (< 3kg ou > 10kg)."""
        a_surveiller = []
        for renard in renards:
            poids = renard['poids']
            if poids is not None and (poids < 3 or poids > 10):
                a_surveiller.append(renard)
        return a_surveiller
    ```