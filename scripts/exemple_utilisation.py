#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'exemple pour utiliser le parser JSON vers HTML
Crée plusieurs fiches d'exercices de démonstration
"""

import json
import os
import subprocess
from pathlib import Path

def create_example_exercises():
    """Crée des fichiers JSON d'exemple pour différents sujets."""
    
    # Exercices sur les variables et types
    variables_exercises = {
        "facile": [
            {
                "nom": "Déclaration de variables",
                "enonce": "Créez trois variables : nom (chaîne), age (entier), et taille (flottant). Affichez leurs valeurs.",
                "exemple": "nom = 'Alice', age = 25, taille = 1.65",
                "correction": "nom = 'Alice'\nage = 25\ntaille = 1.65\nprint(f'Nom: {nom}, Age: {age}, Taille: {taille}m')"
            },
            {
                "nom": "Calculs simples",
                "enonce": "Calculez et affichez la somme, différence, produit et quotient de deux nombres.",
                "exemple": "a = 10, b = 3",
                "correction": "a = 10\nb = 3\nprint(f'Somme: {a + b}')\nprint(f'Différence: {a - b}')\nprint(f'Produit: {a * b}')\nprint(f'Quotient: {a / b}')"
            }
        ],
        "moyen": [
            {
                "nom": "Conversion de types",
                "enonce": "Demandez à l'utilisateur son âge (chaîne), convertissez-le en entier et calculez son âge dans 10 ans.",
                "exemple": "Entrée: '25' → Sortie: 'Dans 10 ans, vous aurez 35 ans'",
                "correction": "age_str = input('Quel est votre âge ? ')\nage = int(age_str)\nage_futur = age + 10\nprint(f'Dans 10 ans, vous aurez {age_futur} ans')"
            }
        ],
        "difficile": [
            {
                "nom": "Calculatrice avec gestion d'erreurs",
                "enonce": "Créez une calculatrice qui demande deux nombres et une opération (+, -, *, /). Gérez la division par zéro.",
                "exemple": "Entrée: 10, 0, '/' → Sortie: 'Erreur: division par zéro'",
                "correction": "try:\n    a = float(input('Premier nombre: '))\n    b = float(input('Second nombre: '))\n    op = input('Opération (+, -, *, /): ')\n    \n    if op == '+': result = a + b\n    elif op == '-': result = a - b\n    elif op == '*': result = a * b\n    elif op == '/': \n        if b == 0: \n            print('Erreur: division par zéro')\n        else: result = a / b\n    else: \n        print('Opération invalide')\n        exit()\n    \n    print(f'Résultat: {result}')\nexcept ValueError:\n    print('Erreur: veuillez entrer des nombres valides')"
            }
        ]
    }
    
    # Exercices sur les listes
    listes_exercises = {
        "facile": [
            {
                "nom": "Création et accès",
                "enonce": "Créez une liste de 5 fruits et affichez le premier et le dernier élément.",
                "exemple": "fruits = ['pomme', 'banane', 'orange', 'kiwi', 'mangue']",
                "correction": "fruits = ['pomme', 'banane', 'orange', 'kiwi', 'mangue']\nprint(f'Premier fruit: {fruits[0]}')\nprint(f'Dernier fruit: {fruits[-1]}')"
            },
            {
                "nom": "Ajout et suppression",
                "enonce": "Créez une liste vide, ajoutez 3 nombres, puis supprimez le deuxième élément.",
                "exemple": "Liste finale: [10, 30]",
                "correction": "nombres = []\nnombres.append(10)\nnombres.append(20)\nnombres.append(30)\nprint(f'Liste avant: {nombres}')\nnombres.pop(1)  # Supprime l'élément à l'index 1\nprint(f'Liste après: {nombres}')"
            }
        ],
        "moyen": [
            {
                "nom": "Recherche dans une liste",
                "enonce": "Écrivez une fonction qui trouve l'index d'un élément dans une liste. Retournez -1 si non trouvé.",
                "exemple": "trouver_index([1, 2, 3, 4], 3) → 2",
                "correction": "def trouver_index(liste, element):\n    for i in range(len(liste)):\n        if liste[i] == element:\n            return i\n    return -1\n\n# Test\nliste = [1, 2, 3, 4]\nprint(trouver_index(liste, 3))  # 2\nprint(trouver_index(liste, 5))  # -1"
            }
        ],
        "difficile": [
            {
                "nom": "Tri par sélection",
                "enonce": "Implémentez l'algorithme de tri par sélection pour trier une liste de nombres.",
                "exemple": "[64, 34, 25, 12] → [12, 25, 34, 64]",
                "correction": "def tri_selection(liste):\n    n = len(liste)\n    for i in range(n):\n        # Trouver l'index du minimum\n        min_idx = i\n        for j in range(i + 1, n):\n            if liste[j] < liste[min_idx]:\n                min_idx = j\n        \n        # Échanger les éléments\n        liste[i], liste[min_idx] = liste[min_idx], liste[i]\n    \n    return liste\n\n# Test\nnombres = [64, 34, 25, 12]\nprint(f'Avant tri: {nombres}')\ntri_selection(nombres)\nprint(f'Après tri: {nombres}')"
            }
        ]
    }
    
    return {
        "variables": variables_exercises,
        "listes": listes_exercises
    }

def generate_html_files(exercises_dict):
    """Génère les fichiers HTML pour chaque sujet d'exercices."""
    
    # Créer le dossier examples s'il n'existe pas
    examples_dir = Path("examples")
    examples_dir.mkdir(exist_ok=True)
    
    for subject, exercises in exercises_dict.items():
        # Créer le fichier JSON
        json_filename = f"examples/exercices_{subject}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(exercises, f, ensure_ascii=False, indent=4)
        
        # Générer le fichier HTML
        html_filename = f"examples/fiche_{subject}.html"
        
        try:
            result = subprocess.run([
                "python3", "scripts/json_to_html_parser.py", 
                json_filename, html_filename
            ], capture_output=True, text=True, check=True)
            
            print(f"✅ Généré: {html_filename}")
            print(f"   JSON: {json_filename}")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de la génération de {html_filename}:")
            print(f"   {e.stderr}")

def main():
    """Fonction principale."""
    print("🚀 Génération d'exemples de fiches d'exercices...\n")
    
    # Créer les exercices d'exemple
    exercises_dict = create_example_exercises()
    
    # Générer les fichiers HTML
    generate_html_files(exercises_dict)
    
    print("\n📋 Résumé des fichiers générés:")
    print("   - examples/exercices_variables.json + fiche_variables.html")
    print("   - examples/exercices_listes.json + fiche_listes.html")
    print("   - examples/exercices_boucles.json + fiche_boucles.html (existant)")
    
    print("\n💡 Pour ouvrir une fiche dans le navigateur:")
    print("   open examples/fiche_variables.html")
    print("   open examples/fiche_listes.html")
    print("   open examples/fiche_boucles.html")
    
    print("\n🔧 Pour créer vos propres fiches:")
    print("   1. Créez un fichier JSON avec la structure appropriée")
    print("   2. Utilisez: python3 scripts/json_to_html_parser.py votre_fichier.json sortie.html")

if __name__ == "__main__":
    main()