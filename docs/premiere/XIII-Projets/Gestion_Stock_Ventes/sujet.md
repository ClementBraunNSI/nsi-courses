# Projet - Système de Gestion de Stock et Ventes 🛒📦

Ce projet a pour but de simuler un système simple de gestion de stock pour un petit commerce. Il permettra d'ajouter des produits, de mettre à jour leurs quantités, d'enregistrer des ventes et de visualiser l'état du stock.

## Concepts Abordés

- Structures de données : listes de dictionnaires (pour les produits, les ventes).
- Manipulation de fichiers (CSV/JSON pour la persistance des données).
- Fonctions pour chaque opération (ajouter produit, enregistrer vente, etc.).
- Logique de mise à jour des quantités.
- Calculs simples (total d'une vente, valeur du stock).

## Fonctionnalités à Implémenter

### 1. Gestion du Catalogue de Produits

Chaque produit a des attributs spécifiques.

!!! fox_exercice "Structure d'un produit"
    Définir une structure pour un produit en stock. Un dictionnaire est idéal :
    - `id_produit` (chaîne de caractères ou entier, unique, ex: "LIV001", 101)
    - `nom_produit` (chaîne de caractères, ex: "Livre de NSI")
    - `description` (chaîne de caractères)
    - `prix_unitaire_vente` (flottant)
    - `quantite_stock` (entier)
    - `seuil_alerte_stock` (entier, optionnel, pour indiquer un stock bas)

!!! fox_exercice "Catalogue des produits"
    Créer une liste globale `catalogue_produits` pour stocker tous les dictionnaires de produits.

!!! fox_exercice "Ajouter un nouveau produit"
    Créer une fonction `ajouter_produit(catalogue, id_prod, nom, desc, prix, qte_init, seuil_alerte)` qui :
    1. Vérifie si un produit avec `id_prod` existe déjà.
    2. Si non, crée un dictionnaire pour le nouveau produit et l'ajoute au `catalogue_produits`.
    3. Renvoie `True` si le produit est ajouté, `False` sinon.

!!! fox_exercice "Modifier un produit"
    Créer une fonction `modifier_produit(catalogue, id_prod, nouveau_nom=None, nouvelle_desc=None, nouveau_prix=None, nouveau_seuil=None)` qui :
    1. Trouve le produit par `id_prod`.
    2. Si trouvé, met à jour les champs spécifiés (ceux qui ne sont pas `None`).
    3. Renvoie `True` si modifié, `False` si produit non trouvé.
    *Note : La quantité en stock ne sera pas modifiée par cette fonction mais par des fonctions d'entrée/sortie de stock.*

!!! fox_exercice "Afficher les détails d'un produit"
    Créer une fonction `afficher_details_produit(produit)` qui affiche les informations d'un produit de manière lisible.

!!! fox_exercice "Afficher tous les produits"
    Créer une fonction `afficher_catalogue(catalogue)` qui liste tous les produits avec quelques informations clés (ID, nom, prix, quantité).

!!! fox_exercice_test "Tests de la gestion du catalogue"
    1. Initialiser un catalogue vide.
    2. Ajouter plusieurs produits différents.
    3. Essayer d'ajouter un produit avec un ID existant.
    4. Modifier les informations d'un produit existant (nom, prix).
    5. Afficher le catalogue complet.
    6. Afficher les détails d'un produit spécifique.

### 2. Gestion des Stocks

!!! fox_exercice "Mettre à jour la quantité en stock"
    Créer une fonction `maj_quantite_stock(catalogue, id_prod, quantite_ajoutee)` qui :
    1. Trouve le produit par `id_prod`.
    2. Si trouvé, ajoute `quantite_ajoutee` à `quantite_stock` (peut être négatif pour une sortie de stock non liée à une vente, comme une perte).
    3. S'assure que la quantité en stock ne devient pas négative (ou gère ce cas selon la logique métier choisie).
    4. Renvoie la nouvelle quantité en stock, ou `None` si produit non trouvé.

!!! fox_exercice "Alerte stock bas"
    Modifier `afficher_catalogue` ou créez une nouvelle fonction `verifier_stocks_bas(catalogue)` qui liste les produits dont la `quantite_stock` est inférieure ou égale à leur `seuil_alerte_stock`.

!!! fox_exercice_test "Tests de la gestion des stocks"
    1. Ajouter un produit avec une quantité initiale et un seuil d'alerte.
    2. Augmenter le stock de ce produit.\ Vérifier la nouvelle quantité.
    3. Diminuer le stock (simuler une perte). Vérifier.
    4. Diminuer le stock en dessous du seuil d'alerte et vérifier que l'alerte est visible.

### 3. Enregistrement des Ventes

Une vente peut concerner plusieurs produits en différentes quantités.

!!! fox_exercice "Structure d'une ligne de vente"
    Pour chaque produit dans une vente, nous aurons besoin de :
    - `id_produit_vendu`
    - `quantite_vendue`
    - `prix_unitaire_au_moment_vente` (important si les prix changent)

!!! fox_exercice "Structure d'une vente"
    Définir une structure pour une vente (dictionnaire) :
    - `id_vente` (entier, unique)
    - `date_vente` (objet `datetime`)
    - `lignes_vente` (liste de dictionnaires, chacun étant une ligne de vente comme définie ci-dessus)
    - `total_vente` (flottant)

!!! fox_exercice "Base de données des ventes"
    Créer une liste globale `historique_ventes` et un compteur `prochain_id_vente`.

!!! fox_exercice "Enregistrer une nouvelle vente"
    Créer une fonction `enregistrer_vente(catalogue, historique_ventes, details_panier)` où `details_panier` est une liste de tuples `(id_produit, quantite_demandee)`.
    Cette fonction doit :
    1. Pour chaque item dans `details_panier` :
        a. Vérifier si le produit existe et si la `quantite_demandee` est disponible en stock.
        b. Si un produit n'est pas disponible en quantité suffisante, la vente entière échoue (ou vous pouvez gérer les ventes partielles comme extension).
    2. Si tous les produits sont disponibles :
        a. Créer un nouvel objet vente avec un `id_vente` unique et la date actuelle.
        b. Pour chaque item, créer une ligne de vente (en stockant le prix actuel) et l'ajouter à `lignes_vente` de l'objet vente.
        c. Mettre à jour (diminuer) la `quantite_stock` pour chaque produit vendu dans le `catalogue_produits` (utilisez `maj_quantite_stock` avec une quantité négative).
        d. Calculer le `total_vente`.
        e. Ajouter l'objet vente à `historique_ventes`.
        f. Renvoyer `True` et l'ID de la vente.
    3. Si un produit n'est pas disponible, renvoyer `False` et un message d'erreur.

!!! fox_exercice "Afficher l'historique des ventes"
    Créer une fonction `afficher_historique_ventes(historique_ventes)` qui affiche toutes les ventes de manière lisible.

!!! fox_exercice_test "Tests des ventes"
    1. S'assurer d'avoir des produits en stock.
    2. Simuler un panier avec plusieurs produits et quantités.
    3. Enregistrer la vente. Vérifier que les quantités en stock dans le catalogue sont mises à jour et que la vente apparaît dans l'historique.
    4. Essayer d'enregistrer une vente pour un produit avec une quantité insuffisante en stock.
    5. Afficher l'historique des ventes.

### 4. Sauvegarde et Chargement

!!! fox_exercice "Persistance des données"
    - Créer des fonctions `sauvegarder_donnees(catalogue, ventes, nom_fichier_catalogue, nom_fichier_ventes)`.
    - Créer des fonctions `charger_donnees(nom_fichier_catalogue, nom_fichier_ventes)` qui retournent le catalogue et l'historique des ventes chargés.
    Utilisez JSON ou CSV.

### 5. Interface Utilisateur

!!! fox_exercice "Menu principal"
    Créer une interface en mode texte pour :
    1. Gestion Produits (sous-menu : ajouter, modifier, afficher tous, afficher détails, vérifier stock bas).
    2. Enregistrer une nouvelle vente.
    3. Afficher l'historique des ventes.
    4. Sauvegarder les données.
    5. Quitter.

!!! fox_exercice_test "Test de l'application complète"
    Effectuer un cycle complet : ajouter des produits, mettre à jour des stocks, enregistrer plusieurs ventes, vérifier les stocks bas, afficher l'historique, sauvegarder, quitter, relancer et vérifier que les données sont restaurées.

## Pour aller plus loin (Optionnel)

- **Rapports de ventes** : Générer des rapports (produit le plus vendu, total des ventes sur une période).
- **Gestion des fournisseurs** : Ajouter des informations sur les fournisseurs et gérer les commandes d'achat pour réapprovisionner le stock.
- **Codes-barres** : Simuler la lecture de codes-barres pour ajouter des produits à une vente.
- **Interface graphique**.