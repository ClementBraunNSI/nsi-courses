# Guide Rapide - Exercices par Chapitre

## 🎯 Objectif

Intégrer des exercices spécifiques directement dans chaque chapitre des pages de niveau, permettant aux étudiants d'accéder facilement aux exercices pertinents depuis les pages de cours.

## 🚀 Utilisation Rapide

### Ajouter un nouvel exercice à un chapitre

```bash
cd /Users/clementbraun/nsi-courses/site_final
node scripts/add-exercise.js "id-exercice" "Titre" "Description" "premiere" "ID-Chapitre" "Titre du Chapitre"
```

**Exemple concret :**
```bash
node scripts/add-exercise.js "dictionnaires" "Exercices sur les Dictionnaires" "Manipulez les dictionnaires Python" "premiere" "V-Dictionnaires_et_Traitement_de_tables" "Dictionnaires et Traitement de tables"
```

### IDs des chapitres de Première

- `I-Constructions_elementaires` - Constructions élémentaires
- `II-Representation_des_donnees` - Représentation des données  
- `III-Structures_de_donnees_lineaires` - Structures de données linéaires
- `IV-Architecture_d_une_machine` - Architecture d'une machine
- `V-Dictionnaires_et_Traitement_de_tables` - Dictionnaires et Traitement de tables
- `VI-Internet_et_Reseaux` - Internet et Réseaux
- `VII-Algorithmes_sur_les_tableaux` - Algorithmes sur les tableaux
- `VIII-Algorithmes_Gloutons` - Algorithmes Gloutons
- `VIIII-Systemes_d_exploitation_et_commandes_Linux` - Systèmes d'exploitation et commandes Linux
- `X-Web_et_HTTP` - Web et HTTP
- `XI-K_plus_proches_voisins` - K plus proches voisins
- `XII-Pour_aller_plus_loin` - Pour aller plus loin

## 📋 Exercices actuellement configurés

### Chapitre I - Constructions élémentaires
- ✅ Exercices sur les Boucles (`boucles`)
- ✅ Exercices sur les Variables (`variables`) 
- ✅ Exercices sur les Fonctions (`fonctions`)

### Chapitre II - Représentation des données
- ✅ Exercices Binaire et Hexadécimal (`binaire-hexa`)

### Chapitre III - Structures de données linéaires
- ✅ Exercices sur les Listes (`listes`)
- ✅ Exercices sur les Listes Python (`listes-python`)

## 🔧 Workflow complet

1. **Créer l'exercice :**
   ```bash
   node scripts/add-exercise.js "mon-exercice" "Mon Titre" "Ma description" "premiere" "III-Structures_de_donnees_lineaires" "Structures de données linéaires"
   ```

2. **Éditer le contenu :**
   - Ouvrir `public/exercises/exercices_mon-exercice.json`
   - Modifier les exercices facile/moyen/difficile
   - Ajouter énoncés, exemples et corrections

3. **Vérifier l'intégration :**
   - Aller sur `http://localhost:3000/premiere`
   - Vérifier que l'exercice apparaît dans le bon chapitre
   - Tester la navigation vers l'exercice

## 🎨 Personnalisation visuelle

Les exercices héritent automatiquement du style du chapitre. Pour personnaliser :

1. **Modifier les couleurs par chapitre :**
   - Éditer `src/styles/ChapterExerciseSection.css`
   - Ajouter des classes spécifiques

2. **Ajuster la mise en page :**
   - Modifier `src/components/ChapterExerciseSection.js`
   - Personnaliser la grille d'affichage

## 📱 Fonctionnalités

- ✅ **Affichage automatique** : Les exercices apparaissent automatiquement dans les chapitres correspondants
- ✅ **Navigation directe** : Clic sur un exercice → redirection vers la page d'exercice
- ✅ **Design responsive** : Adaptation mobile et desktop
- ✅ **Gestion intelligente** : Seuls les chapitres avec exercices affichent la section
- ✅ **Extensibilité** : Facile d'ajouter de nouveaux niveaux

## 🔍 Dépannage

### L'exercice n'apparaît pas dans le chapitre
- Vérifier que `level` et `chapterId` sont corrects dans `exerciseConfig.js`
- Redémarrer le serveur de développement
- Vérifier la console pour les erreurs

### Erreur lors de l'ajout d'exercice
- Vérifier que l'ID n'existe pas déjà
- S'assurer que les guillemets sont bien échappés
- Vérifier les permissions d'écriture

### Problème de navigation
- Vérifier que la route `/exercises/:id` existe dans `App.js`
- Contrôler que le fichier JSON existe dans `public/exercises/`

## 📚 Ressources

- **Documentation complète :** `README_chapter_exercises.md`
- **Documentation exercices :** `README_exercises.md`
- **Scripts :** `scripts/README.md`

## 🎯 Prochaines étapes suggérées

1. **Ajouter des exercices pour tous les chapitres de Première**
2. **Étendre le système à la Terminale**
3. **Créer des exercices transversaux**
4. **Ajouter des statistiques de progression**
5. **Implémenter un système de prérequis**