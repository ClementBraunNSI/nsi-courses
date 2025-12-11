# Idées de sujets BAC NSI — Thème « Renards & biodiversité »

- Habitudes alimentaires du renard
  - Jeu de données proies par observation
  - Calcul des parts, top-3 des proies, normalisation, tests

- Prédiction du régime alimentaire par habitat
  - KNN/K-Means sur caractéristiques (végétation, eau, urbanisation, proies)
  - Évaluer précision, confusion matrix, correction de code bogué

- Activité temporelle (nocturne/diurne)
  - Parsing logs de capteurs, histogrammes, moyenne glissante
  - Détection d’anomalies (jours atypiques), visualisations

- Simulation chaîne trophique locale
  - Modèle simple proies/renards (règles, reproduction, mortalité)
  - Scénarios, métriques (stabilité), analyse de complexité

- Planification de déplacements (points d’eau/terriers)
  - Graphe pondéré, BFS/Dijkstra, contraintes (zones interdites)
  - Comparaison routes et coûts, cas tests

- Nettoyage de données capteurs (IoT)
  - Traitement valeurs manquantes/bruit, lissage
  - Encodage/décodage, validation schémas, agrégations

- Reconstitution de trajet GPS
  - Distance Haversine, simplification (Douglas–Peucker)
  - Classification segments (chasse, repos, transit)

- Base de données d’observations
  - Schéma SQL (observations, habitats, proies)
  - Requêtes d’agrégation, jointures, vues, indices

- Collecte web (arrêtés municipaux/associations)
  - Scraping HTML, extraction texte/méta, nettoyage
  - Constitution corpus, stats par commune

- Vision par ordinateur — empreintes
  - Features simples (contours), k-NN/Naive Bayes
  - Jeu de tests, précision, erreurs typiques

- Cryptographie — données collier GPS
  - Chiffrement symétrique, MAC/HMAC, formats de messages
  - Menaces, intégrité/confidentialité, clés et rotation

- Réseau — pipeline d’ingestion
  - MQTT/HTTP, file tampon, retry/backoff
  - Journalisation, monitoring, tolérance aux pannes

- POO — modèle Animal/Habitat/Sensor
  - Hiérarchie, polymorphisme, composition
  - Sérialisation JSON, tests unitaires

- Performance — tri et recherche sur gros volumes
  - Bench tri (Timsort/merge/quick), recherche (binaire/hash)
  - Profils mémoire/temps, complexité empirique

- Tri de photos de terrain
  - Métadonnées EXIF, hash de similarité, déduplication
  - Pipeline de classement et renommage
