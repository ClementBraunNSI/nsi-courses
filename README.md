# Système de Fiches d'Exercices NSI

[![CI/CD](https://github.com/clementbraun/nsi-courses/workflows/CI/badge.svg)](https://github.com/clementbraun/nsi-courses/actions)
[![Quality](https://img.shields.io/badge/quality-100%25-brightgreen)](docs/test_report_terminale.txt)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Système complet et standardisé pour la création, validation et gestion des fiches d'exercices dans le cadre des cours de NSI (Numérique et Sciences Informatiques).

## 🎯 Objectifs

- **Standardisation** : Structure HTML/CSS/JS unifiée pour toutes les fiches
- **Automatisation** : Scripts pour générer, valider et corriger les fiches
- **Qualité** : Validation automatique et tests de conformité
- **Accessibilité** : Respect des standards d'accessibilité web
- **Pédagogie** : Organisation par niveaux de difficulté progressifs

## 🏗️ Architecture

```
nsi-courses/
├── 📁 templates/          # Templates HTML réutilisables
├── 📁 schemas/            # Schémas de validation JSON
├── 📁 scripts/            # Outils d'automatisation
├── 📁 examples/           # Exemples et données de test
├── 📁 docs/               # Documentation complète
└── 📁 site_final/         # Fiches d'exercices finales
```

## 🚀 Démarrage Rapide

### Prérequis

```bash
# Python 3.7+ requis
pip3 install beautifulsoup4 jsonschema jinja2
```

### Vérification du Système

```bash
# Vérification rapide de toutes les fiches
python3 scripts/deploy_exercise_system.py check

# Déploiement complet avec correction automatique
python3 scripts/deploy_exercise_system.py deploy
```

## 📚 Utilisation

### 1. Créer une Nouvelle Fiche

```bash
# 1. Copier l'exemple
cp examples/example_exercise_data.json ma_fiche.json

# 2. Éditer le contenu (voir structure JSON ci-dessous)

# 3. Générer le HTML
python3 scripts/generate_exercise_html.py ma_fiche.json ma_fiche.html

# 4. Valider la fiche
python3 scripts/validate_exercise_sheets.py ma_fiche.html
```

### 2. Corriger des Fiches Existantes

```bash
# Correction automatique d'un répertoire
python3 scripts/fix_exercise_sheets.py /path/to/exercise/files/

# Correction d'un fichier spécifique
python3 scripts/fix_exercise_sheets.py fiche_problematique.html
```

### 3. Valider la Qualité

```bash
# Validation avec rapport détaillé
python3 scripts/validate_exercise_sheets.py /path/to/files/ rapport.txt

# Tests de qualité complets
python3 scripts/test_exercise_sheets.py /path/to/files/ test_report.txt
```

## 📋 Structure des Données JSON

```json
{
  "metadata": {
    "title": "Titre de la fiche",
    "subtitle": "Sous-titre optionnel",
    "subject": "python|algorithms|data-structures|networks|databases|web",
    "level": "seconde|premiere|terminale",
    "chapter": "Identifiant du chapitre",
    "version": "1.0.0",
    "author": "Nom de l'auteur",
    "created_date": "2024-01-15",
    "tags": ["recursion", "trees", "algorithms"]
  },
  "introduction": {
    "key_concepts": ["Concept 1", "Concept 2"],
    "prerequisites": ["Prérequis 1", "Prérequis 2"],
    "learning_objectives": ["Objectif 1", "Objectif 2"]
  },
  "sections": {
    "easy": {
      "exercises": [
        {
          "title": "Exercice de base",
          "statement": "Énoncé de l'exercice...",
          "examples": ["Exemple 1", "Exemple 2"],
          "solution": {
            "code": "def solution():\n    pass",
            "explanation": "Explication détaillée..."
          },
          "difficulty_indicators": {
            "time_estimate": "10-15 minutes",
            "complexity": "O(n)",
            "concepts_used": ["boucles", "conditions"]
          }
        }
      ]
    },
    "medium": { /* Structure similaire */ },
    "hard": { /* Structure similaire */ }
  }
}
```

## 🎨 Structure des Fiches HTML

### Navigation par Onglets
- **Introduction** : Concepts clés, prérequis, conseils
- **Facile** : Application directe (5-10 lignes de code)
- **Intermédiaire** : Combinaison de concepts (10-30 lignes)
- **Difficile** : Problèmes complexes et optimisation

### Fonctionnalités Interactives
- ✅ Navigation fluide entre sections
- ✅ Affichage/masquage des solutions
- ✅ Design responsive
- ✅ Accessibilité complète

## 🛠️ Scripts Disponibles

| Script | Description | Usage |
|--------|-------------|-------|
| `generate_exercise_html.py` | Génère HTML depuis JSON | `python3 scripts/generate_exercise_html.py data.json output.html` |
| `validate_exercise_sheets.py` | Valide la structure des fiches | `python3 scripts/validate_exercise_sheets.py /path/to/files/` |
| `fix_exercise_sheets.py` | Corrige automatiquement les problèmes | `python3 scripts/fix_exercise_sheets.py /path/to/files/` |
| `test_exercise_sheets.py` | Tests de qualité complets | `python3 scripts/test_exercise_sheets.py /path/to/files/ report.txt` |
| `deploy_exercise_system.py` | Déploiement automatisé | `python3 scripts/deploy_exercise_system.py [check\|deploy\|level]` |

## 📊 Critères de Qualité

### Validation Automatique
- ✅ Structure HTML5 valide
- ✅ Métadonnées complètes (charset, viewport, title)
- ✅ Ressources CSS/JS présentes
- ✅ Navigation fonctionnelle
- ✅ Sections bien définies
- ✅ Cartes d'exercices structurées
- ✅ Accessibilité respectée

### Seuils de Réussite
- **≥ 80%** : Fiche acceptée ✅
- **60-79%** : Avertissement ⚠️
- **< 60%** : Correction requise ❌

## 🔄 CI/CD Intégré

Le système inclut une validation automatique via GitHub Actions :

```yaml
# .github/workflows/ci.yml
- name: Validate Exercise Sheets
  run: |
    python3 scripts/validate_exercise_sheets.py site_final/public/courses-html/
    python3 scripts/test_exercise_sheets.py site_final/public/courses-html/
```

## 📈 Résultats Actuels

### Niveau Terminale
- **5 fiches** traitées et corrigées
- **Taux de réussite : 100%** ✅
- **Score moyen : 97.6%** (92.9% à 100%)

### Statistiques de Qualité
- **42/42 tests** réussis pour `fiche_exercices_rappels.html`
- **36/36 tests** réussis pour `fiche_exercices_arbres.html`
- **35/35 tests** réussis pour `fiche_exercices_graphes.html`
- **37/37 tests** réussis pour `fiche_exercices_listes_piles_files.html`
- **26/28 tests** réussis pour `fiche_exercices_sql.html`

## 📖 Documentation

- **[Directives de Création](docs/exercise_creation_guidelines.md)** : Guide complet pour créer des exercices
- **[Synthèse du Projet](docs/project_summary.md)** : Vue d'ensemble et architecture
- **[Rapports de Test](docs/)** : Résultats détaillés des validations

## 🤝 Contribution

### Workflow de Contribution

1. **Fork** le repository
2. **Créer** une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. **Tester** vos modifications (`python3 scripts/deploy_exercise_system.py check`)
4. **Commit** vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
5. **Push** vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
6. **Créer** une Pull Request

### Standards de Code

- **Python 3.7+** requis
- **PEP 8** pour le style de code
- **Docstrings** pour toutes les fonctions
- **Tests** pour les nouvelles fonctionnalités

## 🐛 Dépannage

### Problèmes Courants

**Erreur "Module not found"**
```bash
pip3 install beautifulsoup4 jsonschema jinja2
```

**Fichiers non trouvés**
```bash
# Vérifier la structure des répertoires
find . -name "*.html" -path "*/exercices/*" | head -5
```

**Validation échouée**
```bash
# Correction automatique
python3 scripts/fix_exercise_sheets.py /path/to/problematic/files/
```

### Support

- **Issues GitHub** : Pour signaler des bugs
- **Discussions** : Pour les questions générales
- **Documentation** : Consultez le dossier `docs/`

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- **Communauté NSI** pour les retours et suggestions
- **Contributeurs** pour leurs améliorations
- **Étudiants** pour leurs tests d'utilisation

---

**Système de Fiches d'Exercices NSI** - Créé avec ❤️ pour l'enseignement de l'informatique

*Dernière mise à jour : Janvier 2024*