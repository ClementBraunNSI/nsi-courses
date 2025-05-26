# Fiche d'exercices : Les Dictionnaires en Python

## Moyenne d'une interrogation

Un dictionnaire `notes` contient les noms des élèves en clés et leurs moyennes en valeurs.  
```python
    notes = {'Alice': 15, 'Bob': 12, 'Clara': 17, 'David': 10}
```

!!! fox_exercice "Gestion des notes d'élèves"
    Écrire une fonction `afficher_notes` qui prend en paramètre un dictionnaire et affiche la moyenne de chaque élève sous la forme : `"Alice a une moyenne de 15."`. 
    Ajouter un commentaire selon la moyenne : `"Excellent"` pour une moyenne ≥ 16, `"Bien"` pour une moyenne entre 12 et 15 inclus, et `"À améliorer"` pour une moyenne < 12.

??? fox_correction "Correction"
    ```python
    def afficher_notes(notes):
        for eleve in notes:
            moyenne = notes[eleve]
            print(eleve + "a une moyenne de "+ str(moyenne)+".")
            if moyenne >= 16:
                print("Excellent")
            elif 12 <= moyenne <= 15:
                print("Bien")
            else:
                print("À améliorer")
    ```

!!! fox_exercice "Ajout et modification de notes"
    Écrire une fonction `ajouter_eleve(notes, nom, moyenne)` qui ajoute un nouvel élève au dictionnaire.

??? fox_correction "Correction"
    ```python
    def ajouter_eleve(notes, nom, moyenne):
        # On vérifie d'abord si l'élève existe déjà
        if nom in notes:
            print("L'élève "+nom+" existe déjà !")
        else:
            # Si l'élève n'existe pas, on l'ajoute
            notes[nom] = moyenne
            print("L'élève "+nom+" a été ajouté avec la moyenne de "+str(moyenne))
    ```

!!! fox_exercice "Modification de moyennes"
    Écrire une fonction `modifier_moyenne(notes, nom, nouvelle_moyenne)` qui modifie la moyenne d'un élève.
       - Gérer le cas où l'élève à modifier n'existe pas.

??? fox_correction "Correction"
    ```python
    def modifier_moyenne(notes, nom, nouvelle_moyenne):
        # On vérifie si l'élève existe dans le dictionnaire
        if nom in notes:
            # Si oui, on modifie sa moyenne
            notes[nom] = nouvelle_moyenne
            print("La moyenne de "+nom+" a été mise à jour à "+str(nouvelle_moyenne))
        else:
            print("L'élève "+ nom + " n'existe pas dans la liste")
    ```

!!! fox_exercice "Analyse des mentions"
    Écrire une fonction `eleves_mention(notes, seuil)` qui renvoie la liste des élèves ayant une moyenne ≥ seuil.
       - Afficher également le nombre total d'élèves ayant cette mention.

??? fox_correction "Correction"
    ```python
    def eleves_mention(notes, seuil):
        # On crée une liste vide pour stocker les élèves
        eleves_avec_mention = []
        # On parcourt le dictionnaire
        for eleve in notes:
            if notes[eleve] >= seuil:
                eleves_avec_mention.append(eleve)
        # On affiche le résultat
        print(str(len(eleves_avec_mention))+ " élèves ont une moyenne supérieure ou égale à " + str(seuil))
        return eleves_avec_mention
    ```

---

## Gestion d'un concessionnaire

Un dictionnaire `voitures` contient les modèles en clés et leurs prix en valeurs.
```python
    voitures = {'Clio': 15000, 'Megane': 20000, 'Talisman': 35000}
```

!!! fox_exercice "Affichage des voitures"
    Écrire une fonction `afficher_voitures(voitures)` qui affiche le prix de chaque modèle avec le texte : `"Le prix de la Clio est de 15000 euros."`.

??? fox_correction "Correction"
    ```python
    def afficher_voitures(voitures):
        for modele in voitures:
            print("Le prix de la "+modele+" est de "+ str(voitures[modele])+ " euros.")
    ```


!!! fox_exercice "Gestion des prix"
    Écrire une fonction `ajouter_voiture(voitures, modele, prix)` qui ajoute un nouveau modèle au dictionnaire.
       - Vérifier que le modèle n'existe pas déjà avant de l'ajouter.

??? fox_correction "Correction"
    ```python
    def ajouter_voiture(voitures, modele, prix):
        if modele in voitures:
            print("Le modèle "+modele+" existe déjà !")
        else:
            voitures[modele] = prix
            print("La voiture "+modele+" a été ajoutée au prix de "+str(prix)+" euros")
    ```

!!! fox_exercice "Réductions"
    Écrire une fonction `reduction_prix(voitures, pourcentage)` qui réduit le prix de chaque voiture d'un pourcentage donné.
       - Afficher les prix avant et après réduction.

??? fox_correction "Correction"
    ```python
    def reduction_prix(voitures, pourcentage):
        print("Prix avant réduction :")
        afficher_voitures(voitures)
        # On parcourt et modifie chaque prix
        for modele in voitures:
            prix_initial = voitures[modele]
            reduction = prix_initial * (pourcentage / 100)
            voitures[modele] = prix_initial - reduction
        print("\nPrix après réduction de "+ str(pourcentage)+"% :")
        afficher_voitures(voitures)
    ```

---

## Gestion des bibliothèques

Un dictionnaire `bibliotheques` contient plusieurs bibliothèques.
```python
    bibliotheques = {
        'biblio1': {'nom': 'Bibliothèque Centrale', 'ville': 'Paris', 'livres': 30000},
        'biblio2': {'nom': 'Médiathèque', 'ville': 'Lyon', 'livres': 15000},
        'biblio3': {'nom': 'Bibliothèque Universitaire', 'ville': 'Marseille', 'livres': 50000}
    }
```

!!! fox_exercice "Réseau de bibliothèques"
    
    Écrire une fonction `afficher_bibliotheques` qui affiche les informations sous la forme : `"Bibliothèque Centrale à Paris : 30000 livres."`.

??? fox_correction "Correction"
    ```python
    def afficher_bibliotheques(bibliotheques):
        """
        Affiche les informations de chaque bibliothèque
        """
        for code in bibliotheques:
            biblio = bibliotheques[code]
            print(biblio['nom'] + " à " + biblio['ville'] + " : " + str(biblio['livres']) + " livres.")
    ```

!!! fox_exercice "Ajout de bibliothèque"
    Écrire une fonction `ajouter_bibliotheque` qui ajoute une nouvelle bibliothèque au dictionnaire.

??? fox_correction "Correction"
    ```python
    def ajouter_bibliotheque(bibliotheques, code, nom, ville, nb_livres):
        """
        Ajoute une nouvelle bibliothèque au dictionnaire
        """
        bibliotheques[code] = {
            'nom': nom,
            'ville': ville, 
            'livres': nb_livres
        }
        return bibliotheques
    ```

!!! fox_exercice "Recherche de la plus grande bibliothèque"
    Écrire une fonction `plus_grande_bibliotheque` qui renvoie la bibliothèque ayant le plus de livres.

??? fox_correction "Correction"
    ```python
    def plus_grande_bibliotheque(bibliotheques):
        """
        Renvoie la bibliothèque ayant le plus de livres
        """
        max_livres = 0
        biblio_max = None
        for code in bibliotheques:
            if bibliotheques[code]['livres'] > max_livres:
                max_livres = bibliotheques[code]['livres']
                biblio_max = bibliotheques[code]
        return biblio_max
    ```

!!! fox_exercice "Calcul du total des livres"
    Écrire une fonction `total_livres` qui calcule et renvoie le nombre total de livres.

??? fox_correction "Correction"
    ```python
    def total_livres(bibliotheques):
        """
        Calcule le nombre total de livres dans toutes les bibliothèques
        """
        total = 0
        for code in bibliotheques:
            total = total + bibliotheques[code]['livres']
        return total
    ```

---

## Gestion des employés
Un dictionnaire `employes` contient les informations des employés.
```python
    employes = {
        'emp1': {'nom': 'Alice', 'poste': 'Développeur', 'salaire': 3500},
        'emp2': {'nom': 'Bob', 'poste': 'Designer', 'salaire': 3000},
        'emp3': {'nom': 'Clara', 'poste': 'Chef de projet', 'salaire': 5000}
    }
```

!!! fox_exercice "Base de données des employés"
    Écrire une fonction `afficher_employes` qui affiche les informations sous la forme : `"Alice est Développeur et gagne 3500 euros."`.

??? fox_correction "Correction"
    ```python
    def afficher_employes(employes):
        """
        Affiche les informations de chaque employé
        """
        for code in employes:
            emp = employes[code]
            print(emp['nom'] + " est " + emp['poste'] + " et gagne " + str(emp['salaire']) + " euros.")
    ```

!!! fox_exercice "Ajout d'employé"
    Écrire une fonction `ajouter_employe` qui ajoute un nouvel employé au dictionnaire.

??? fox_correction "Correction"
    ```python
    def ajouter_employe(employes, code, nom, poste, salaire):
        """
        Ajoute un nouvel employé au dictionnaire
        """
        if code not in employes:
            employes[code] = {
                'nom': nom,
                'poste': poste,
                'salaire': salaire
            }
            return employes
    ```

!!! fox_exercice "Augmentation des salaires"
    Écrire une fonction `augmenter_salaires` qui augmente tous les salaires d'un pourcentage donné en paramètres.

??? fox_correction "Correction"
    ```python
    def augmenter_salaires(employes, pourcentage):
        """
        Augmente tous les salaires d'un pourcentage donné
        """
        for code in employes:
            ancien_salaire = employes[code]['salaire']
            augmentation = ancien_salaire * pourcentage / 100
            employes[code]['salaire'] = ancien_salaire + augmentation
    ```

!!! fox_exercice "Recherche du salaire maximum"
    Écrire une fonction `employe_salaire_max` qui renvoie l'employé ayant le salaire le plus élevé.

??? fox_correction "Correction"
    ```python
    def employe_salaire_max(employes):
        """
        Renvoie l'employé ayant le salaire le plus élevé
        """
        max_salaire = 0
        emp_max = None
        for code in employes:
            if employes[code]['salaire'] > max_salaire:
                max_salaire = employes[code]['salaire']
                emp_max = employes[code]
        return emp_max
    ```

---

## Gestion des contacts
Un dictionnaire `contacts` contient les informations personnelles des contacts.
```python
    contacts = {
        'Jean Dupont': {'téléphone': '0612345678', 'email': 'jean.dupont@email.com', 'ville': 'Paris'},
        'Marie Martin': {'téléphone': '0687654321', 'email': 'marie.martin@email.com', 'ville': 'Lyon'}
    }
```

!!! fox_exercice "Livre de contacts téléphoniques"
    Écrire une fonction `rechercher_contact` qui renvoie les détails d'un contact par son nom.

??? fox_correction "Correction"
    ```python
    def rechercher_contact(contacts, nom):
        """
        Renvoie les détails d'un contact par son nom
        """
        if nom in contacts:
            return contacts[nom]
        return "Contact non trouvé"
    ```

!!! fox_exercice "Gestion des contacts"
    Écrire une fonction `ajouter_contact` qui ajoute un nouveau contact.

??? fox_correction "Correction"
    ```python
    def ajouter_contact(contacts, nom, telephone, email, ville):
        """
        Ajoute un nouveau contact au dictionnaire
        """
        contacts[nom] = {
            'téléphone': telephone,
            'email': email,
            'ville': ville
        }
    ```
!!! fox_exercice "Contacts par ville"
    Écrire une fonction `contacts_par_ville` qui renvoie la liste des contacts d'une ville donnée.

??? fox_correction "Correction"
    ```python
    def contacts_par_ville(contacts, ville):
        """
        Renvoie la liste des contacts d'une ville donnée
        """
        contacts_ville = []
        for nom in contacts:
            if contacts[nom]['ville'] == ville:
                contacts_ville.append(nom)
        return contacts_ville
    ```
!!! fox_exercice "Mettre à jour un contact"
    Écrire une fonction `mettre_a_jour_contact` qui permet de modifier un champ spécifique d'un contact.

??? fox_correction "Correction"
    ```python
    def mettre_a_jour_contact(contacts, nom, champ, nouvelle_valeur):
        """
        Modifie un champ spécifique d'un contact
        """
        if nom in contacts:
            if champ in contacts[nom]:
                contacts[nom][champ] = nouvelle_valeur
                return "Contact mis à jour"
        return "Contact ou champ non trouvé"
    ```
    
---

## Résultats de sondage 

Un dictionnaire `resultats_sondage` représente les réponses à un sondage.
```python
    resultats_sondage = {
        'Satisfait': 45,
        'Neutre': 30,
        'Insatisfait': 25
    }
```

!!! fox_exercice "Analyse de sondage" 
    1. Écrire une fonction `calculer_pourcentages` qui convertit les nombres en pourcentages.

??? fox_correction "Correction"
    ```python
    def calculer_pourcentages(resultats):
        """
        Convertit les nombres en pourcentages
        """
        total = 0
        pourcentages = {}
        # Calcul du total
        for reponse in resultats:
            total = total + resultats[reponse]
        # Calcul des pourcentages
        for reponse in resultats:
            pourcentage = (resultats[reponse] / total) * 100
            pourcentages[reponse] = pourcentage
        return pourcentages
    ```

!!! fox_exercice "Comparaison et visualisation de sondages"
    1. Écrire une fonction `comparer_sondages` qui compare deux sondages.
    2. Écrire une fonction `visualiser_resultats` qui génère une représentation textuelle des résultats.
    3. Écrire une fonction `sondage_plus_representatif` qui identifie le sondage avec l'échantillon le plus grand.

??? fox_correction "Correction"
    ```python
    def comparer_sondages(sondage1, sondage2):
        """
        Compare deux sondages et renvoie les différences
        """
        differences = {}
        for reponse in sondage1:
            if reponse in sondage2:
                difference = sondage1[reponse] - sondage2[reponse]
                differences[reponse] = difference
        return differences

    def visualiser_resultats(resultats):
        """
        Génère une représentation textuelle des résultats
        """
        for reponse in resultats:
            nombre = resultats[reponse]
            barre = "*" * int(nombre/2)  # Une étoile pour chaque tranche de 2 réponses
            print(reponse + ": " + barre + " (" + str(nombre) + ")")

    def sondage_plus_representatif(sondage1, sondage2):
        """
        Identifie le sondage avec l'échantillon le plus grand
        """
        total1 = sum(sondage1.values())
        total2 = sum(sondage2.values())
        return "sondage1" if total1 > total2 else "sondage2"
    ```


---

## Gestion d'un inventaire de jeux-vidéos

Un dictionnaire `jeux` stocke des informations sur différents jeux vidéo.
```python
    jeux = {
        'Mario Kart': {'plateforme': 'Switch', 'genre': 'Course', 'note': 9.2},
        'Zelda': {'plateforme': 'Switch', 'genre': 'Action-Aventure', 'note': 9.7}
    }
```

!!! fox_exercice "Gestion des jeux vidéo"
    
    1. Écrire une fonction `filtrer_jeux` qui filtre les jeux selon la plateforme, le genre ou la note minimale.
    2. Écrire une fonction `meilleur_jeu_par_genre` qui renvoie le jeu avec la meilleure note pour chaque genre.

??? fox_correction "Correction"
    ```python
    def filtrer_jeux(jeux, plateforme=None, genre=None, note_min=None):
        """
        Filtre les jeux selon les critères donnés
        """
        jeux_filtres = {}
        for jeu in jeux:
            valide = True
            if plateforme and jeux[jeu]['plateforme'] != plateforme:
                valide = False
            if genre and jeux[jeu]['genre'] != genre:
                valide = False
            if note_min and jeux[jeu]['note'] < note_min:
                valide = False
            
            if valide:
                jeux_filtres[jeu] = jeux[jeu]
        
        return jeux_filtres

    def meilleur_jeu_par_genre(jeux):
        """
        Renvoie le jeu avec la meilleure note pour chaque genre
        """
        meilleurs = {}
        for jeu in jeux:
            genre = jeux[jeu]['genre']
            note = jeux[jeu]['note']
            if genre not in meilleurs or note > meilleurs[genre]['note']:
                meilleurs[genre] = {'nom': jeu, 'note': note}
        return meilleurs
    ```

!!! fox_exercice "Gestion des jeux (suite)"
    3. Écrire une fonction `ajouter_jeu` qui ajoute un nouveau jeu.
    4. Écrire une fonction `calculer_moyenne_notes` qui calcule la moyenne des notes pour tous les jeux.

??? fox_correction "Correction"
    ```python
    def ajouter_jeu(jeux, nom, plateforme, genre, note):
        """
        Ajoute un nouveau jeu
        """
        jeux[nom] = {
            'plateforme': plateforme,
            'genre': genre,
            'note': note
        }

    def calculer_moyenne_notes(jeux):
        """
        Calcule la moyenne des notes pour tous les jeux
        """
        if not jeux:
            return 0
        total = sum(jeu['note'] for jeu in jeux.values())
        return total / len(jeux)
    ```

---

## Analyse de performances d'athletes

Un dictionnaire `athletes` permet de suivre les performances.
```python
    athletes = {
        'Pierre': {'sport': 'marathon', 'temps': [2.15, 2.18, 2.16]},
        'Sophie': {'sport': 'marathon', 'temps': [2.20, 2.22, 2.19]}
    }
```

!!! fox_exercice "Performances sportives"
    
    Écrire les fonctions suivantes :  
    1. `calculer_moyenne_performances` qui calcule la moyenne des performances  
    2. `meilleur_temps` qui trouve l'athlète avec le meilleur temps pour un sport donné  
    3. `progression_athlete` qui calcule la progression entre les performances  
    4. `ajouter_performance` qui ajoute une nouvelle performance  

??? fox_correction "Correction"
    ```python
    def calculer_moyenne_performances(athletes):
        moyennes = {}
        for athlete in athletes:
            temps = athletes[athlete]['temps']
            moyennes[athlete] = sum(temps) / len(temps)
        return moyennes

    def meilleur_temps(athletes, sport):
        meilleur_athlete = None
        meilleur_performance = float('inf')
        for athlete in athletes:
            if athletes[athlete]['sport'] == sport:
                meilleur_temps_athlete = min(athletes[athlete]['temps'])
                if meilleur_temps_athlete < meilleur_performance:
                    meilleur_performance = meilleur_temps_athlete
                    meilleur_athlete = athlete
        return meilleur_athlete, meilleur_performance

    def progression_athlete(athletes, nom):
        if nom not in athletes or len(athletes[nom]['temps']) < 2:
            return 0
        premier_temps = athletes[nom]['temps'][0]
        dernier_temps = athletes[nom]['temps'][-1]
        return ((premier_temps - dernier_temps) / premier_temps) * 100

    def ajouter_performance(athletes, nom, nouveau_temps):
        if nom in athletes:
            athletes[nom]['temps'].append(nouveau_temps)
            return "Performance ajoutée"
        return "Athlète non trouvé"
    ```