
# Fiche d'exercices : Les Dictionnaires en Python


## 1. Gestion des notes d'élèves
Un dictionnaire `notes` contient les noms des élèves en clés et leurs moyennes en valeurs.  
```python
notes = {'Alice': 15, 'Bob': 12, 'Clara': 17, 'David': 10}
```

1. **Écrire une fonction `afficher_notes(notes)`** qui affiche la moyenne de chaque élève sous la forme : `"Alice a une moyenne de 15."`.
   - Ajouter un commentaire selon la moyenne : `"Excellent"` pour une moyenne ≥ 16, `"Bien"` pour une moyenne entre 12 et 15 inclus, et `"À améliorer"` pour une moyenne < 12.

2. **Écrire une fonction `ajouter_eleve(notes, nom, moyenne)`** qui ajoute un nouvel élève au dictionnaire.
   - Vérifier que l’élève n’existe pas déjà avant de l’ajouter.

3. **Écrire une fonction `modifier_moyenne(notes, nom, nouvelle_moyenne)`** qui modifie la moyenne d’un élève.
   - Gérer le cas où l’élève à modifier n’existe pas.

4. **Écrire une fonction `eleves_mention(notes, seuil)`** qui renvoie la liste des élèves ayant une moyenne ≥ seuil.
   - Afficher également le nombre total d’élèves ayant cette mention.

---

## 2. Gestion d’un concessionnaire automobile

Un dictionnaire `voitures` contient les modèles en clés et leurs prix en valeurs.
```python
voitures = {'Clio': 15000, 'Megane': 20000, 'Talisman': 35000}
```

1. **Écrire une fonction `afficher_voitures(voitures)`** qui affiche le prix de chaque modèle avec le texte : `"Le prix de la Clio est de 15000 euros."`.
   - Ajouter une option pour trier l’affichage des voitures par prix croissant.

2. **Écrire une fonction `ajouter_voiture(voitures, modele, prix)`** qui ajoute un nouveau modèle au dictionnaire.
   - Vérifier que le modèle n’existe pas déjà avant de l’ajouter.

3. **Écrire une fonction `reduction_prix(voitures, pourcentage)`** qui réduit le prix de chaque voiture d’un pourcentage donné.
   - Afficher les prix avant et après réduction.

4. **Écrire une fonction `voitures_abordables(voitures, budget)`** qui renvoie la liste des modèles dont le prix est ≤ au budget donné.
   - Calculer combien d’argent il resterait après l’achat de la voiture la moins chère.

---

## 3. Catalogue de produits
Un catalogue est représenté par une liste de dictionnaires.
```python
catalogue = [
    {'nom': 'Stylo', 'quantité': 100, 'prix_unitaire': 1.5},
    {'nom': 'Cahier', 'quantité': 50, 'prix_unitaire': 3.0},
    {'nom': 'Crayon', 'quantité': 200, 'prix_unitaire': 0.8}
]
```

1. **Écrire une fonction `afficher_catalogue(catalogue)`** qui affiche les détails de chaque produit sous la forme : `"Stylo : 100 unités, prix unitaire 1.5 euros."`.
   - Afficher également la valeur totale pour chaque produit.

2. **Écrire une fonction `ajouter_produit(catalogue, nom, quantité, prix_unitaire)`** qui ajoute un nouveau produit au catalogue.
   - Empêcher l’ajout si le produit existe déjà et proposer de mettre à jour les informations.

3. **Écrire une fonction `valeur_totale_produit(produit)`** qui calcule et renvoie la valeur totale d’un produit (`quantité * prix_unitaire`).
   - Ajouter une fonction `valeur_totale_catalogue(catalogue)` qui calcule la valeur totale de tous les produits.

4. **Écrire une fonction `produit_le_plus_cher(catalogue)`** qui renvoie le produit avec le prix unitaire le plus élevé.
   - Modifier la fonction pour qu’elle renvoie également le produit le moins cher.

---

## 4. Réseau de bibliothèques
Un dictionnaire `bibliotheques` contient plusieurs bibliothèques.
```python
bibliotheques = {
    'biblio1': {'nom': 'Bibliothèque Centrale', 'ville': 'Paris', 'livres': 30000},
    'biblio2': {'nom': 'Médiathèque', 'ville': 'Lyon', 'livres': 15000},
    'biblio3': {'nom': 'Bibliothèque Universitaire', 'ville': 'Marseille', 'livres': 50000}
}
```

1. **Écrire une fonction `afficher_bibliotheques(bibliotheques)`** qui affiche les informations sous la forme : `"Bibliothèque Centrale à Paris : 30000 livres."`.
   - Afficher uniquement les bibliothèques ayant plus d’un certain nombre de livres.

2. **Écrire une fonction `ajouter_bibliotheque(bibliotheques, nom, ville, livres)`** qui ajoute une nouvelle bibliothèque au dictionnaire.
   - Vérifier si une bibliothèque avec le même nom existe déjà.

3. **Écrire une fonction `plus_grande_bibliotheque(bibliotheques)`** qui renvoie la bibliothèque ayant le plus de livres.
   - Modifier la fonction pour qu’elle renvoie également la bibliothèque avec le moins de livres.

4. **Écrire une fonction `total_livres(bibliotheques)`** qui calcule et renvoie le nombre total de livres.
   - Afficher également la moyenne de livres par bibliothèque.

---

## 5. Base de données des employés
Un dictionnaire `employes` contient les informations des employés.
```python
employes = {
    'emp1': {'nom': 'Alice', 'poste': 'Développeur', 'salaire': 3500},
    'emp2': {'nom': 'Bob', 'poste': 'Designer', 'salaire': 3000},
    'emp3': {'nom': 'Clara', 'poste': 'Chef de projet', 'salaire': 5000}
}
```

1. **Écrire une fonction `afficher_employes(employes)`** qui affiche les informations sous la forme : `"Alice est Développeur et gagne 3500 euros."`.
   - Afficher uniquement les employés ayant un salaire supérieur à un seuil.

2. **Écrire une fonction `ajouter_employe(employes, id_employe, nom, poste, salaire)`** qui ajoute un nouvel employé au dictionnaire.
   - Vérifier que l’`id_employe` n’existe pas déjà.

3. **Écrire une fonction `augmenter_salaires(employes, pourcentage)`** qui augmente tous les salaires d’un pourcentage donné.
   - Ajouter une option pour n’augmenter les salaires que des employés ayant un poste spécifique.

4. **Écrire une fonction `employe_salaire_max(employes)`** qui renvoie l’employé ayant le salaire le plus élevé.
   - Modifier la fonction pour renvoyer également l’employé ayant le salaire le plus bas.

## 6. Livre de contacts téléphoniques
Un dictionnaire `contacts` contient les informations personnelles des contacts.
```python
contacts = {
    'Jean Dupont': {'téléphone': '0612345678', 'email': 'jean.dupont@email.com', 'ville': 'Paris'},
    'Marie Martin': {'téléphone': '0687654321', 'email': 'marie.martin@email.com', 'ville': 'Lyon'}
}
```

1. **Écrire une fonction `rechercher_contact(contacts, nom)`** qui renvoie les détails d'un contact par son nom.
   - Gérer le cas où le contact n'existe pas avec un message approprié.

2. **Écrire une fonction `ajouter_contact(contacts, nom, telephone, email, ville)`** qui ajoute un nouveau contact.
   - Vérifier que le contact n'existe pas déjà.
   - Lever une exception si le contact existe.

3. **Écrire une fonction `contacts_par_ville(contacts, ville)`** qui renvoie la liste des contacts d'une ville donnée.
   - Retourner une liste vide si aucun contact n'est trouvé.

4. **Écrire une fonction `mettre_a_jour_contact(contacts, nom, champ, nouvelle_valeur)`** qui permet de modifier un champ spécifique d'un contact.
   - Gérer les cas où le contact ou le champ n'existe pas.

---

## 7. Analyse des résultats d'un sondage
Un dictionnaire `resultats_sondage` représente les réponses à un sondage.
```python
resultats_sondage = {
    'Satisfait': 45,
    'Neutre': 30,
    'Insatisfait': 25
}
```

1. **Écrire une fonction `calculer_pourcentages(resultats_sondage)`** qui convertit les nombres en pourcentages.
   - Arrondir les pourcentages à deux décimales.
   - Vérifier que le total des résultats est bien de 100%.

2. **Écrire une fonction `comparer_sondages(sondage1, sondage2)`** qui compare deux sondages.
   - Calculer les différences de pourcentage pour chaque catégorie.
   - Identifier la catégorie ayant le plus changé.

3. **Écrire une fonction `visualiser_resultats(resultats_sondage)`** qui génère une représentation textuelle des résultats.
   - Utiliser des astérisques pour représenter graphiquement les proportions.

4. **Écrire une fonction `sondage_plus_representatif(list_sondages)`** qui identifie le sondage avec l'échantillon le plus grand.

---

## 8. Gestion d'un inventaire de jeux vidéo
Un dictionnaire `jeux` stocke des informations sur différents jeux vidéo.
```python
jeux = {
    'Mario Kart': {'plateforme': 'Switch', 'genre': 'Course', 'note': 9.2},
    'Zelda': {'plateforme': 'Switch', 'genre': 'Action-Aventure', 'note': 9.7}
}
```

1. **Écrire une fonction `filtrer_jeux(jeux, plateforme=None, genre=None, note_min=0)`** qui filtre les jeux selon différents critères.
   - Permettre le filtrage par plateforme, genre, et note minimale.
   - Retourner un nouveau dictionnaire avec les jeux correspondants.

2. **Écrire une fonction `meilleur_jeu_par_genre(jeux)`** qui renvoie le jeu avec la meilleure note pour chaque genre.
   - Gérer le cas où un genre n'a qu'un seul jeu.

3. **Écrire une fonction `ajouter_jeu(jeux, nom, plateforme, genre, note)`** qui ajoute un nouveau jeu.
   - Vérifier que la note est entre 0 et 10.
   - Empêcher l'ajout de jeux en doublon.

4. **Écrire une fonction `calculer_moyenne_notes(jeux)`** qui calcule la moyenne des notes pour tous les jeux.
   - Distinguer entre moyenne générale et moyenne par genre.

---

## 9. Suivi des performances sportives
Un dictionnaire `athletes` permet de suivre les performances.
```python
athletes = {
    'Pierre': {'sport': 'marathon', 'temps': [2.15, 2.18, 2.16]},
    'Sophie': {'sport': 'marathon', 'temps': [2.20, 2.22, 2.19]}
}
```

1. **Écrire une fonction `calculer_moyenne_performances(athlete)`** qui calcule la moyenne des performances.
   - Gérer les cas de performances manquantes.
   - Permettre de lisser les résultats en retirant les valeurs extrêmes.

2. **Écrire une fonction `meilleur_temps(athletes, sport)`** qui trouve l'athlète avec le meilleur temps pour un sport donné.
   - Gérer le cas où aucun athlète ne pratique le sport.

3. **Écrire une fonction `progression_athlete(athlete)`** qui calcule la progression entre les performances.
   - Retourner un pourcentage de progression.
   - Gérer les cas de performances irrégulières.

4. **Écrire une fonction `ajouter_performance(athletes, nom, sport, temps)`** qui ajoute une nouvelle performance.
   - Créer un nouvel athlète si nécessaire.
   - Vérifier la cohérence des données.

---

