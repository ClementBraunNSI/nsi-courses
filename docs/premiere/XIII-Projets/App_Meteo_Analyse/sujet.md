# Projet - Application Météo avec Analyse de Données 🌦️📊

Ce projet consiste à créer une application qui récupère des données météorologiques (simulées ou réelles via une API simple), les stocke, et permet d'effectuer des analyses simples (température moyenne, jours de pluie, etc.).

## Concepts Abordés

- Structures de données : listes de dictionnaires pour les relevés météo.
- Manipulation de fichiers (CSV ou JSON pour stocker les données).
- Traitement de données : calcul de moyennes, comptages, recherche de min/max.
- Utilisation de dates (module `datetime`).
- Fonctions pour organiser les opérations.
- (Optionnel) Interaction avec une API web simple pour récupérer des données réelles.

## Fonctionnalités à Implémenter

### 1. Structure et Stockage des Données Météo

Chaque relevé météo concernera une date spécifique.

!!! fox_exercice "Structure d'un relevé météo"
    Définir une structure pour un relevé météo quotidien. Un dictionnaire est adapté :
    - `date` (chaîne de caractères au format AAAA-MM-JJ ou objet `date`)
    - `temperature_max` (flottant, en °C)
    - `temperature_min` (flottant, en °C)
    - `precipitation_mm` (flottant, quantité de pluie en mm)
    - `description_temps` (chaîne de caractères, ex: "Ensoleillé", "Nuageux", "Pluie légère")

!!! fox_exercice "Base de données des relevés"
    Créer une liste globale `releves_meteo` pour stocker tous les relevés.

!!! fox_exercice "Ajouter un relevé météo"
    Créer une fonction `ajouter_releve(releves_meteo, date_str, temp_max, temp_min, precip, desc)` qui :
    1. Vérifie si un relevé pour `date_str` existe déjà.
    2. Convertit `date_str` en un format de date standard (si ce n'est pas déjà fait).
    3. Crée un dictionnaire de relevé et l'ajoute à `releves_meteo`.
    4. Renvoie `True` si ajouté, `False` sinon (date déjà présente).
    *Pensez à la validation des types de données (ex: températures sont des nombres).*

!!! fox_exercice "Sauvegarde et Chargement des relevés"
    - Créer une fonction `sauvegarder_releves(releves_meteo, nom_fichier)` pour sauvegarder la liste `releves_meteo` dans un fichier CSV ou JSON.
    - Créer une fonction `charger_releves(nom_fichier)` pour charger les relevés depuis le fichier au démarrage de l'application. Si le fichier n'existe pas, retourner une liste vide.
    *Attention à la conversion des types lors du chargement (surtout pour les dates et les nombres).*

!!! fox_exercice_test "Tests de la gestion des données"
    1. Initialiser `releves_meteo` (ou chargez depuis un fichier vide).
    2. Ajouter manuellement plusieurs relevés pour différentes dates.
    3. Essayer d'ajouter un relevé pour une date existante.
    4. Sauvegarder les relevés.
    5. Redémarrer le script (ou effacez la variable) et charger les relevés. Vérifier qu'ils sont corrects.

### 2. Saisie Manuelle des Données

!!! fox_exercice "Interface de saisie"
    Créer une fonction qui permet à l'utilisateur de saisir les informations pour un nouveau relevé météo (date, températures, précipitations, description).
    Cette fonction appellera `ajouter_releve`.
    S'assurer de gérer les erreurs de saisie (par exemple, si l'utilisateur entre du texte pour une température).

### 3. Analyse des Données Météo

!!! fox_exercice "Température moyenne pour une période"
    Créer une fonction `temperature_moyenne_periode(releves_meteo, date_debut_str, date_fin_str)` qui :
    1. Filtre les relevés compris entre `date_debut_str` et `date_fin_str` (incluses).
    2. Calcule la température moyenne ((temp_max + temp_min) / 2) pour chaque jour sélectionné.
    3. Renvoie la moyenne de ces températures moyennes journalières. Si aucun relevé n'est trouvé pour la période, renvoyez `None` ou un message approprié.

!!! fox_exercice "Jour le plus chaud / froid sur une période"
    Créer deux fonctions :
    - `jour_plus_chaud(releves_meteo, date_debut_str, date_fin_str)` : renvoie le dictionnaire du relevé avec la `temperature_max` la plus élevée dans la période.
    - `jour_plus_froid(releves_meteo, date_debut_str, date_fin_str)` : renvoie le dictionnaire du relevé avec la `temperature_min` la plus basse dans la période.

!!! fox_exercice "Nombre de jours de pluie et total précipitations"
    Créer une fonction `stats_precipitation_periode(releves_meteo, date_debut_str, date_fin_str)` qui :
    1. Filtre les relevés pour la période donnée.
    2. Compte le nombre de jours où `precipitation_mm > 0`.
    3. Calcule le total des `precipitation_mm` sur ces jours de pluie.
    4. Renvoie ces deux valeurs (par exemple, sous forme de tuple ou de dictionnaire).

!!! fox_exercice "Afficher les relevés pour un jour donné"
    Créer une fonction `afficher_releve_jour(releves_meteo, date_str)` qui recherche et affiche de manière formatée le relevé météo pour la `date_str` spécifiée, ou un message si aucun relevé n'est trouvé.

!!! fox_exercice_test "Tests des analyses"
    Après avoir saisi ou chargé un ensemble de données de test (par exemple, pour un mois complet) :
    1. Calculer la température moyenne pour ce mois.
    2. Trouver le jour le plus chaud et le jour le plus froid du mois.
    3. Calculer le nombre de jours de pluie et le total des précipitations pour le mois.
    4. Afficher les données pour un jour spécifique.

### 4. Interface Utilisateur

!!! fox_exercice "Menu principal"
    Créer une interface en mode texte pour permettre à l'utilisateur de :
    1. Ajouter un nouveau relevé météo.
    2. Afficher le relevé pour un jour spécifique.
    3. Afficher les statistiques pour une période (température moyenne, jour le plus chaud/froid, stats de pluie).
    4. Sauvegarder les données (si non automatique à chaque ajout).
    5. Quitter.

!!! fox_exercice_test "Test de l'application complète"
    1. Lancer l'application. Charger des données existantes s'il y en a, sinon commencer avec une base vide.
    2. Ajouter quelques relevés pour plusieurs jours.
    3. Demander des statistiques pour différentes périodes.
    4. Afficher des relevés spécifiques.
    5. Sauvegarder et quitter. Relancer pour vérifier la persistance.

## Pour aller plus loin (Optionnel)

- **Graphiques simples** : Utilisez une bibliothèque comme `matplotlib` (si autorisée et installée) pour tracer des graphiques simples (évolution des températures, histogramme des précipitations).
- **Récupération de données réelles** : Utilisez une API météo gratuite (comme OpenWeatherMap, nécessite une clé API) pour récupérer les données d'aujourd'hui ou des prévisions. Cela introduirait la gestion des requêtes HTTP (module `requests`) et l'analyse de JSON complexe.
- **Prévisions basiques** : Si vous avez suffisamment de données historiques, essayez de calculer des moyennes saisonnières pour "prédire" grossièrement le temps.
- **Alertes météo** : Définir des seuils (température très élevée, fortes pluies) et afficher des alertes si les données récentes les dépassent.