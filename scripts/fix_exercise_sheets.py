#!/usr/bin/env python3
"""
Script pour corriger automatiquement les fiches d'exercices problématiques.
Utilise le système de templates pour standardiser la structure.
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict
from bs4 import BeautifulSoup

class ExerciseSheetFixer:
    def __init__(self, templates_dir: str):
        self.templates_dir = Path(templates_dir)
        
        # Charger le template de base
        base_template_path = self.templates_dir / "base_exercise_template.html"
        if base_template_path.exists():
            with open(base_template_path, 'r', encoding='utf-8') as f:
                self.base_template = f.read()
        else:
            print(f"❌ Template de base non trouvé: {base_template_path}")
            sys.exit(1)
    
    def extract_existing_content(self, html_content: str) -> Dict:
        """
        Extrait le contenu existant d'une fiche d'exercices.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extraire le titre
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else "Fiche d'exercices"
        
        # Extraire le titre principal (h1)
        h1_tag = soup.find('h1')
        main_title = h1_tag.get_text().strip() if h1_tag else title
        
        # Extraire les exercices existants
        exercise_cards = soup.find_all('div', class_='exercise-card')
        
        exercises = {
            'intro': [],
            'easy': [],
            'medium': [],
            'hard': []
        }
        
        for card in exercise_cards:
            # Déterminer la difficulté
            difficulty = 'easy'  # Par défaut
            if 'intro' in card.get('class', []):
                difficulty = 'intro'
            elif 'medium' in card.get('class', []):
                difficulty = 'medium'
            elif 'hard' in card.get('class', []):
                difficulty = 'hard'
            
            # Extraire le contenu
            title_elem = card.find('h3')
            exercise_title = title_elem.get_text().strip() if title_elem else "Exercice"
            
            content_elem = card.find('div', class_='exercise-content')
            exercise_content = str(content_elem) if content_elem else "<p>Contenu à définir</p>"
            
            solution_elem = card.find('div', class_='solution')
            solution_content = str(solution_elem) if solution_elem else "<p>Solution à définir</p>"
            
            exercises[difficulty].append({
                'title': exercise_title,
                'content': exercise_content,
                'solution': solution_content
            })
        
        return {
            'title': title,
            'main_title': main_title,
            'exercises': exercises
        }
    
    def generate_introduction_section(self, subject: str) -> str:
        """
        Génère une section d'introduction basée sur le sujet.
        """
        introductions = {
            'rappels': {
                'topic': 'Rappels de Première',
                'description': 'Cette fiche d\'exercices vous permet de réviser les concepts fondamentaux vus en Première.',
                'tips': 'Prenez le temps de bien comprendre chaque concept avant de passer aux exercices plus complexes.'
            },
            'arbres': {
                'topic': 'Structures d\'arbres',
                'description': 'Les arbres sont des structures de données hiérarchiques fondamentales en informatique.',
                'tips': 'Visualisez toujours la structure de l\'arbre avant d\'écrire votre code.'
            },
            'graphes': {
                'topic': 'Théorie des graphes',
                'description': 'Les graphes permettent de modéliser de nombreux problèmes réels.',
                'tips': 'Identifiez d\'abord le type de graphe (orienté/non-orienté, pondéré/non-pondéré) avant de choisir l\'algorithme.'
            },
            'listes_piles_files': {
                'topic': 'Listes, Piles et Files',
                'description': 'Ces structures de données linéaires ont chacune leurs spécificités et cas d\'usage.',
                'tips': 'Respectez le principe LIFO pour les piles et FIFO pour les files.'
            },
            'sql': {
                'topic': 'Langage SQL',
                'description': 'SQL permet d\'interroger et de manipuler des bases de données relationnelles.',
                'tips': 'Commencez par bien comprendre la structure de la base avant d\'écrire vos requêtes.'
            }
        }
        
        intro_data = introductions.get(subject, {
            'topic': 'Exercices',
            'description': 'Cette fiche d\'exercices vous permettra de pratiquer les concepts étudiés.',
            'tips': 'Lisez attentivement les énoncés et n\'hésitez pas à faire des schémas.'
        })
        
        return f'''
        <div class="exercise-card intro">
            <h3>📚 Introduction - {intro_data['topic']}</h3>
            <div class="exercise-content">
                <p>{intro_data['description']}</p>
                <div class="alert alert-info">
                    <p><strong>💡 Conseils</strong></p>
                    <p>{intro_data['tips']}</p>
                </div>
            </div>
        </div>
        '''
    
    def organize_exercises_by_difficulty(self, exercises: List[Dict]) -> Dict:
        """
        Organise automatiquement les exercices par difficulté.
        """
        organized = {'easy': [], 'medium': [], 'hard': []}
        
        for i, exercise in enumerate(exercises):
            # Heuristiques pour déterminer la difficulté
            title = exercise['title'].lower()
            content = exercise['content'].lower()
            
            # Mots-clés pour difficulté facile
            easy_keywords = ['simple', 'basique', 'introduction', 'rappel', 'définition']
            # Mots-clés pour difficulté difficile
            hard_keywords = ['complexe', 'avancé', 'optimisation', 'algorithme', 'récursif']
            
            if any(keyword in title or keyword in content for keyword in easy_keywords):
                difficulty = 'easy'
            elif any(keyword in title or keyword in content for keyword in hard_keywords):
                difficulty = 'hard'
            elif i < len(exercises) // 3:  # Premier tiers = facile
                difficulty = 'easy'
            elif i < 2 * len(exercises) // 3:  # Deuxième tiers = moyen
                difficulty = 'medium'
            else:  # Dernier tiers = difficile
                difficulty = 'hard'
            
            organized[difficulty].append(exercise)
        
        return organized
    
    def generate_exercise_cards(self, exercises: List[Dict], difficulty: str) -> str:
        """
        Génère les cartes d'exercices pour une difficulté donnée.
        """
        if not exercises:
            return f'''
            <div class="exercise-card {difficulty}">
                <h3>Exercices {difficulty.capitalize()}</h3>
                <div class="exercise-content">
                    <p>Exercices à venir dans cette section...</p>
                </div>
            </div>
            '''
        
        cards_html = []
        for i, exercise in enumerate(exercises, 1):
            card_html = f'''
            <div class="exercise-card {difficulty}">
                <h3>Exercice {i} : {exercise['title']}</h3>
                <div class="exercise-content">
                    {exercise['content']}
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">→ Voir la correction</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <h4>💡 Solution :</h4>
                        {exercise['solution']}
                    </div>
                </div>
            </div>
            '''
            cards_html.append(card_html)
        
        return '\n'.join(cards_html)
    
    def fix_exercise_sheet(self, file_path: str) -> bool:
        """
        Corrige une fiche d'exercices en utilisant le système de templates.
        """
        try:
            # Lire le fichier existant
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Extraire le contenu existant
            extracted = self.extract_existing_content(original_content)
            
            # Déterminer le sujet à partir du nom de fichier
            filename = Path(file_path).name.lower()
            subject = 'exercices'
            if 'rappel' in filename:
                subject = 'rappels'
            elif 'arbre' in filename:
                subject = 'arbres'
            elif 'graphe' in filename:
                subject = 'graphes'
            elif 'liste' in filename or 'pile' in filename or 'file' in filename:
                subject = 'listes_piles_files'
            elif 'sql' in filename:
                subject = 'sql'
            
            # Générer les sections
            intro_html = self.generate_introduction_section(subject)
            
            # Organiser les exercices existants
            all_exercises = []
            for difficulty in ['intro', 'easy', 'medium', 'hard']:
                all_exercises.extend(extracted['exercises'][difficulty])
            
            if all_exercises:
                organized = self.organize_exercises_by_difficulty(all_exercises)
            else:
                # Créer des exercices par défaut si aucun n'existe
                organized = {
                    'easy': [{
                        'title': 'Exercice de base',
                        'content': '<p>Exercice à définir...</p>',
                        'solution': '<p>Solution à définir...</p>'
                    }],
                    'medium': [],
                    'hard': []
                }
            
            easy_html = self.generate_exercise_cards(organized['easy'], 'easy')
            medium_html = self.generate_exercise_cards(organized['medium'], 'medium')
            hard_html = self.generate_exercise_cards(organized['hard'], 'hard')
            
            # Remplacer les placeholders dans le template
            new_content = self.base_template.replace('{{TITLE}}', extracted['title'])
            new_content = new_content.replace('{{SUBTITLE}}', '')
            new_content = new_content.replace('{{INTRO_CONTENT}}', intro_html)
            new_content = new_content.replace('{{EASY_CONTENT}}', easy_html)
            new_content = new_content.replace('{{MEDIUM_CONTENT}}', medium_html)
            new_content = new_content.replace('{{HARD_CONTENT}}', hard_html)
            
            # Sauvegarder le fichier corrigé
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Fiche corrigée: {Path(file_path).name}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de la correction de {file_path}: {e}")
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_exercise_sheets.py <file_or_directory>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    # Chemins des répertoires
    script_dir = Path(__file__).parent
    templates_dir = script_dir.parent / "templates"
    
    # Créer le correcteur
    fixer = ExerciseSheetFixer(str(templates_dir))
    
    files_to_fix = []
    
    if os.path.isfile(target):
        files_to_fix.append(target)
    elif os.path.isdir(target):
        # Trouver tous les fichiers d'exercices
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith('.html') and ('fiche' in file.lower() or 'exercice' in file.lower()):
                    files_to_fix.append(os.path.join(root, file))
    else:
        print(f"❌ Fichier ou répertoire non trouvé: {target}")
        sys.exit(1)
    
    if not files_to_fix:
        print("❌ Aucun fichier d'exercice trouvé")
        sys.exit(1)
    
    print(f"🔧 Correction de {len(files_to_fix)} fichier(s)...")
    
    success_count = 0
    for file_path in files_to_fix:
        if fixer.fix_exercise_sheet(file_path):
            success_count += 1
    
    print(f"\n📊 Résumé: {success_count}/{len(files_to_fix)} fichiers corrigés avec succès")
    
    if success_count == len(files_to_fix):
        print("✅ Toutes les corrections ont été appliquées!")
    else:
        print("⚠️ Certaines corrections ont échoué")

if __name__ == "__main__":
    main()