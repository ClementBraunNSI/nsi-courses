# Parser JSON vers HTML pour Fiches d'Exercices

Ce script permet de convertir un fichier JSON contenant des exercices en un fichier HTML interactif avec des animations slide pour les corrections.

## Structure du fichier JSON

Le fichier JSON doit suivre cette structure :

```json
{
    "facile": [
        {
            "nom": "Titre de l'exercice",
            "enonce": "Description de l'exercice",
            "exemple": "Exemple d'utilisation (optionnel)",
            "correction": "Code de la solution"
        }
    ],
    "moyen": [
        {
            "nom": "Exercice plus complexe",
            "enonce": "Description détaillée",
            "exemple": "Exemple avec résultat attendu",
            "correction": "Solution avec commentaires"
        }
    ],
    "difficile": [
        {
            "nom": "Exercice avancé",
            "enonce": "Problème algorithmique complexe",
            "exemple": "Cas d'usage spécifique",
            "correction": "Solution optimisée"
        }
    ]
}
```

## Utilisation

### Commande de base
```bash
python3 scripts/json_to_html_parser.py input.json output.html
```

### Exemple concret
```bash
python3 scripts/json_to_html_parser.py examples/exercices_boucles.json examples/fiche_boucles.html
```

## Fonctionnalités du HTML généré

### Interface interactive
- **Onglets par difficulté** : Navigation entre Facile 🦊, Moyen 🦊🦊, Difficile 🦊🦊🦊
- **Cartes d'exercices** : Chaque exercice est présenté dans une carte avec code couleur
- **Animations slide** : Les corrections s'affichent avec une animation slide depuis la droite
- **Design responsive** : S'adapte aux écrans mobiles et desktop

### Système de couleurs
- **Facile** : Vert (#28a745)
- **Moyen** : Jaune/Orange (#ffc107)
- **Difficile** : Rouge (#dc3545)

### Fonctionnalités JavaScript
- `showSection(sectionName)` : Change d'onglet
- `toggleSolution(button)` : Affiche/masque la correction avec animation
- Coloration syntaxique basique pour le code Python

## Structure du HTML généré

```html
<div class="exercise-card">
    <div class="exercise-content-wrapper">
        <!-- Contenu de l'exercice -->
        <button class="toggle-solution">→ Voir la correction</button>
    </div>
    <div class="solution-wrapper">
        <!-- Correction avec animation slide -->
    </div>
</div>
```

## Personnalisation

### Modifier les styles
Les styles CSS sont intégrés dans le fichier HTML généré. Pour les personnaliser :
1. Modifiez la section `<style>` dans le script `json_to_html_parser.py`
2. Régénérez le fichier HTML

### Ajouter de nouveaux niveaux de difficulté
1. Ajoutez le niveau dans le dictionnaire `difficulty_icons` et `difficulty_colors`
2. Modifiez la boucle de génération des sections
3. Ajoutez l'onglet correspondant dans le template HTML

## Exemples d'utilisation

### Créer une fiche sur les listes
```bash
python3 scripts/json_to_html_parser.py data/exercices_listes.json output/fiche_listes.html
```

### Créer une fiche sur les fonctions
```bash
python3 scripts/json_to_html_parser.py data/exercices_fonctions.json output/fiche_fonctions.html
```

## Dépannage

### Erreur "command not found: python"
Utilisez `python3` au lieu de `python`

### Erreur de format JSON
Vérifiez que votre fichier JSON respecte la structure attendue avec les clés "facile", "moyen", "difficile"

### Problème d'encodage
Assurez-vous que vos fichiers JSON sont encodés en UTF-8

## Intégration avec le site NSI

Pour intégrer les fiches générées dans le site React :
1. Placez les fichiers HTML dans `site_final/public/exercises/`
2. Créez des liens depuis les pages de cours
3. Utilisez les styles existants du site pour une cohérence visuelle