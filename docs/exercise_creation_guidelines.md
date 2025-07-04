# Directives pour la Création d'Exercices

## Vue d'ensemble

Ce document établit les standards et bonnes pratiques pour créer des fiches d'exercices cohérentes et de qualité dans le système NSI.

## Structure Standardisée

### 1. Métadonnées Requises

Chaque fiche d'exercices doit inclure :

```json
{
  "metadata": {
    "title": "Titre de la fiche",
    "subtitle": "Sous-titre optionnel",
    "subject": "python|algorithms|data-structures|networks|databases|web|other",
    "level": "seconde|premiere|terminale",
    "chapter": "Identifiant du chapitre",
    "version": "1.0.0",
    "author": "Nom de l'auteur",
    "created_date": "YYYY-MM-DD",
    "tags": ["tag1", "tag2"]
  }
}
```

### 2. Structure HTML Obligatoire

#### Navigation par Onglets
```html
<div class="section-tabs">
    <button class="tab-button active" data-section="intro">Introduction</button>
    <button class="tab-button" data-section="easy">Facile</button>
    <button class="tab-button" data-section="medium">Intermédiaire</button>
    <button class="tab-button" data-section="hard">Difficile</button>
</div>
```

#### Sections Requises
- `section-intro` : Introduction et concepts clés
- `section-easy` : Exercices de niveau facile
- `section-medium` : Exercices de niveau intermédiaire
- `section-hard` : Exercices de niveau difficile

#### Structure des Cartes d'Exercices
```html
<div class="exercise-card [difficulty]">
    <h3>Exercice [numéro] : [titre]</h3>
    <div class="exercise-content">
        <!-- Énoncé de l'exercice -->
    </div>
    <button class="toggle-solution" onclick="toggleSolution(this)">→ Voir la correction</button>
    <div class="solution-wrapper">
        <div class="solution">
            <h4>💡 Solution :</h4>
            <!-- Solution détaillée -->
        </div>
    </div>
</div>
```

## Niveaux de Difficulté

### Introduction
- **Objectif** : Présenter les concepts clés
- **Contenu** : Définitions, exemples, conseils
- **Format** : Pas d'exercices, uniquement informatif

### Facile
- **Objectif** : Application directe des concepts
- **Caractéristiques** :
  - Énoncés courts et clairs
  - Une seule notion par exercice
  - Solutions en 5-10 lignes de code maximum
- **Exemples** : Création de variables, boucles simples, fonctions basiques

### Intermédiaire
- **Objectif** : Combinaison de plusieurs concepts
- **Caractéristiques** :
  - Énoncés plus complexes
  - Contraintes supplémentaires
  - Solutions en 10-30 lignes de code
  - Indices optionnels
- **Exemples** : Algorithmes de tri simples, manipulation de structures

### Difficile
- **Objectif** : Résolution de problèmes complexes
- **Caractéristiques** :
  - Énoncés ouverts nécessitant réflexion
  - Plusieurs approches possibles
  - Analyse de complexité
  - Solutions alternatives
- **Exemples** : Algorithmes optimisés, structures de données avancées

## Standards de Qualité

### Énoncés d'Exercices

1. **Clarté** :
   - Utiliser un langage simple et précis
   - Éviter les ambiguïtés
   - Fournir des exemples concrets

2. **Progressivité** :
   - Commencer par des cas simples
   - Augmenter graduellement la complexité
   - Réutiliser les concepts précédents

3. **Contexte** :
   - Donner des exemples d'utilisation réelle
   - Expliquer l'intérêt pratique
   - Lier aux concepts théoriques

### Solutions

1. **Complétude** :
   - Code fonctionnel et testé
   - Gestion des cas particuliers
   - Commentaires explicatifs

2. **Pédagogie** :
   - Explication du raisonnement
   - Justification des choix techniques
   - Alternatives possibles

3. **Bonnes Pratiques** :
   - Code lisible et bien structuré
   - Noms de variables explicites
   - Respect des conventions Python

## Processus de Création

### 1. Planification

1. **Définir les objectifs pédagogiques**
   - Quels concepts enseigner ?
   - Quel niveau de maîtrise atteindre ?
   - Comment évaluer la compréhension ?

2. **Analyser le public cible**
   - Niveau des étudiants
   - Prérequis nécessaires
   - Temps disponible

3. **Structurer la progression**
   - Ordre logique des exercices
   - Liens entre les concepts
   - Points de difficulté

### 2. Rédaction

1. **Utiliser le format JSON standardisé**
   ```bash
   # Créer un nouveau fichier d'exercices
   cp examples/example_exercise_data.json new_exercise.json
   # Éditer le contenu
   # Générer le HTML
   python3 scripts/generate_exercise_html.py new_exercise.json output.html
   ```

2. **Respecter la structure des templates**
   - Utiliser les templates existants
   - Maintenir la cohérence visuelle
   - Tester sur différents navigateurs

3. **Valider le contenu**
   ```bash
   # Valider la structure
   python3 scripts/validate_exercise_sheets.py output.html
   ```

### 3. Révision et Test

1. **Révision par les pairs**
   - Vérification de la clarté
   - Test des solutions
   - Validation pédagogique

2. **Test utilisateur**
   - Faire tester par des étudiants
   - Mesurer le temps de résolution
   - Identifier les points de blocage

3. **Itération**
   - Corriger les problèmes identifiés
   - Améliorer la clarté
   - Optimiser la difficulté

## Outils et Ressources

### Scripts Disponibles

- `generate_exercise_html.py` : Génération HTML depuis JSON
- `validate_exercise_sheets.py` : Validation de structure
- `fix_exercise_sheets.py` : Correction automatique

### Templates

- `base_exercise_template.html` : Template de base
- `exercise_card_template.html` : Templates de cartes

### Validation Automatique

- CI/CD intégré via GitHub Actions
- Vérification de structure HTML
- Détection de sections vides
- Validation des ressources CSS/JS

## Exemples de Bonnes Pratiques

### Énoncé Bien Structuré

```html
<div class="exercise-content">
    <p>Écrivez une fonction <code>fibonacci(n)</code> qui calcule le n-ième terme de la suite de Fibonacci.</p>
    
    <div class="constraints">
        <p><strong>Contraintes :</strong></p>
        <ul>
            <li>n ≥ 0</li>
            <li>Utiliser une approche itérative</li>
        </ul>
    </div>
    
    <p><em>Exemple :</em> <code>fibonacci(5)</code> retourne <code>5</code></p>
    
    <div class="hints">
        <p><strong>💡 Indice :</strong> F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)</p>
    </div>
</div>
```

### Solution Complète

```html
<div class="solution">
    <h4>💡 Solution :</h4>
    <pre><code>def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    
    return b</code></pre>
    
    <p><strong>Explication :</strong> Cette solution utilise une approche itérative avec deux variables pour éviter la récursion coûteuse.</p>
    
    <p><strong>Complexité :</strong> O(n) en temps, O(1) en espace</p>
</div>
```

## Maintenance et Évolution

### Versioning

- Utiliser le versioning sémantique (MAJOR.MINOR.PATCH)
- Documenter les changements dans les métadonnées
- Maintenir la compatibilité ascendante

### Feedback et Amélioration

- Collecter les retours des enseignants
- Analyser les difficultés des étudiants
- Mettre à jour régulièrement le contenu

### Archivage

- Conserver les anciennes versions
- Documenter les raisons des changements
- Maintenir un historique des modifications

---

*Ce document est un guide vivant qui évolue avec les besoins pédagogiques et les retours d'expérience.*