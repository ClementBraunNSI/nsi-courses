# Scripts utilitaires pour les exercices NSI

## add-exercise.js

Script pour ajouter automatiquement un nouvel exercice au système.

### Usage

```bash
node scripts/add-exercise.js <exercise-id> <title> <description>
```

### Paramètres

- **exercise-id** : Identifiant unique de l'exercice (utilisé dans l'URL)
- **title** : Titre affiché de l'exercice
- **description** : Description courte de l'exercice

### Exemples

```bash
# Ajouter des exercices sur les fonctions
node scripts/add-exercise.js "fonctions" "Exercices sur les Fonctions" "Apprenez à créer et utiliser des fonctions"

# Ajouter des exercices sur les dictionnaires
node scripts/add-exercise.js "dictionnaires" "Exercices sur les Dictionnaires" "Manipulez les structures de données associatives"

# Ajouter des exercices d'algorithmique
node scripts/add-exercise.js "algorithmes" "Exercices d'Algorithmique" "Résolvez des problèmes algorithmiques complexes"
```

### Ce que fait le script

1. **Crée le fichier JSON** : `public/exercises/exercices_<id>.json`
   - Contient un template avec des exercices d'exemple
   - Structure avec 3 niveaux : facile, moyen, difficile

2. **Met à jour la configuration** : `src/config/exerciseConfig.js`
   - Ajoute l'exercice à la liste des exercices disponibles
   - Configure le titre, le chemin du fichier et la description

3. **Rend l'exercice accessible** : `/exercises/<id>`
   - L'exercice devient immédiatement accessible via l'URL
   - Apparaît dans la navigation des exercices

### Structure du fichier JSON généré

```json
{
  "facile": [
    {
      "nom": "Premier exercice facile",
      "enonce": "Écrivez un programme qui affiche 'Hello World'.",
      "exemple": "Exemple :\n>>> print('Hello World')\nHello World",
      "correction": "print('Hello World')"
    }
  ],
  "moyen": [
    {
      "nom": "Premier exercice moyen",
      "enonce": "Créez une fonction qui calcule la somme de deux nombres.",
      "exemple": "Exemple :\n>>> somme(3, 5)\n8",
      "correction": "def somme(a, b):\n    return a + b"
    }
  ],
  "difficile": [
    {
      "nom": "Premier exercice difficile",
      "enonce": "Implémentez un algorithme de tri par sélection.",
      "exemple": "Exemple :\n>>> tri_selection([3, 1, 4, 1, 5])\n[1, 1, 3, 4, 5]",
      "correction": "def tri_selection(liste):\n    for i in range(len(liste)):\n        min_idx = i\n        for j in range(i+1, len(liste)):\n            if liste[j] < liste[min_idx]:\n                min_idx = j\n        liste[i], liste[min_idx] = liste[min_idx], liste[i]\n    return liste"
    }
  ]
}
```

### Après l'exécution du script

1. **Éditez le fichier JSON** pour remplacer les exercices d'exemple par vos propres exercices
2. **Redémarrez le serveur** si nécessaire (généralement pas requis)
3. **Testez l'exercice** en naviguant vers `http://localhost:3000/exercises/<id>`

### Gestion des erreurs

Le script vérifie :
- Si l'exercice existe déjà (évite les doublons)
- Si les paramètres sont corrects
- Si les fichiers peuvent être créés/modifiés

### Conseils

- Utilisez des IDs courts et descriptifs (ex: `boucles`, `listes`, `fonctions`)
- Les IDs ne doivent contenir que des lettres, chiffres et tirets
- Les titres et descriptions peuvent contenir des accents et caractères spéciaux
- Pensez à tester l'exercice après l'avoir créé

### Dépannage

**Erreur "fichier existe déjà"** :
- L'exercice a déjà été créé
- Vérifiez `public/exercises/` et `src/config/exerciseConfig.js`

**Erreur de permissions** :
- Vérifiez que vous avez les droits d'écriture
- Exécutez depuis la racine du projet

**Erreur de syntaxe** :
- Vérifiez que les paramètres ne contiennent pas de guillemets non échappés
- Utilisez des guillemets simples ou doubles selon le contexte