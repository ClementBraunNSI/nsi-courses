#!/usr/bin/env python3
"""
Script de validation automatisée pour les fiches d'exercices.
Vérifie la structure HTML, les classes CSS requises, et les fonctions JavaScript.
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple
from bs4 import BeautifulSoup
import json

class ExerciseSheetValidator:
    def __init__(self):
        self.required_css_classes = [
            'exercise-card',
            'intro',
            'easy',
            'medium', 
            'hard',
            'toggle-solution',
            'solution-wrapper',
            'solution'
        ]
        
        self.required_js_functions = [
            'showSection',
            'toggleSolution'
        ]
        
        self.required_sections = [
            'section-intro',
            'section-easy', 
            'section-medium',
            'section-hard'
        ]
        
        self.required_navigation = [
            'section-tabs'
        ]
    
    def validate_html_structure(self, html_content: str) -> Dict[str, bool]:
        """
        Valide la structure HTML de base.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        results = {}
        
        # Vérifier la présence du DOCTYPE
        results['has_doctype'] = html_content.strip().startswith('<!DOCTYPE html>')
        
        # Vérifier les balises essentielles
        results['has_html_tag'] = soup.find('html') is not None
        results['has_head_tag'] = soup.find('head') is not None
        results['has_body_tag'] = soup.find('body') is not None
        results['has_title_tag'] = soup.find('title') is not None
        
        # Vérifier la structure de navigation
        nav_tabs = soup.find('div', class_='section-tabs')
        results['has_navigation'] = nav_tabs is not None
        
        if nav_tabs:
            buttons = nav_tabs.find_all('button')
            expected_buttons = ['intro', 'easy', 'medium', 'hard']
            results['has_all_nav_buttons'] = len(buttons) >= 4
            
            button_data_sections = [btn.get('data-section') for btn in buttons if btn.get('data-section')]
            results['nav_buttons_correct'] = all(section in button_data_sections for section in expected_buttons)
        else:
            results['has_all_nav_buttons'] = False
            results['nav_buttons_correct'] = False
        
        return results
    
    def validate_css_presence(self, html_content: str) -> Dict[str, bool]:
        """
        Valide la présence des classes CSS requises.
        """
        results = {}
        
        # Vérifier le lien vers le CSS externe
        soup = BeautifulSoup(html_content, 'html.parser')
        css_link = soup.find('link', {'rel': 'stylesheet', 'href': re.compile(r'exercise-cards\.css')})
        results['has_css_link'] = css_link is not None
        
        # Vérifier la présence des classes CSS dans le HTML
        for css_class in self.required_css_classes:
            pattern = rf'class=["\'][^"\']* ?{css_class}[ "\']'
            results[f'has_class_{css_class}'] = bool(re.search(pattern, html_content))
        
        return results
    
    def validate_javascript(self, html_content: str) -> Dict[str, bool]:
        """
        Valide la présence des fonctions JavaScript requises.
        """
        results = {}
        
        # Extraire le contenu JavaScript
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tags = soup.find_all('script')
        js_content = '\n'.join(script.get_text() for script in script_tags if script.get_text())
        
        # Vérifier la présence des fonctions
        for func_name in self.required_js_functions:
            pattern = rf'function\s+{func_name}\s*\(|{func_name}\s*=\s*function|{func_name}\s*:\s*function'
            results[f'has_function_{func_name}'] = bool(re.search(pattern, js_content))
        
        return results
    
    def validate_sections(self, html_content: str) -> Dict[str, any]:
        """
        Valide la présence et le contenu des sections.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        results = {}
        
        # Vérifier la présence des sections
        for section_id in self.required_sections:
            section = soup.find('div', id=section_id)
            results[f'has_{section_id}'] = section is not None
            
            if section:
                # Vérifier si la section contient des exercices
                exercise_cards = section.find_all('div', class_='exercise-card')
                results[f'{section_id}_has_content'] = len(exercise_cards) > 0
                results[f'{section_id}_exercise_count'] = len(exercise_cards)
                
                # Vérifier les sections vides (contenant "Exercices à venir" ou similaire)
                section_text = section.get_text().lower()
                empty_indicators = ['exercices à venir', 'à venir', 'coming soon', 'todo']
                results[f'{section_id}_is_empty'] = any(indicator in section_text for indicator in empty_indicators)
            else:
                results[f'{section_id}_has_content'] = False
                results[f'{section_id}_exercise_count'] = 0
                results[f'{section_id}_is_empty'] = True
        
        return results
    
    def validate_exercise_cards(self, html_content: str) -> Dict[str, any]:
        """
        Valide la structure des cartes d'exercices.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        results = {}
        
        exercise_cards = soup.find_all('div', class_='exercise-card')
        results['total_exercise_cards'] = len(exercise_cards)
        
        # Compter par difficulté
        results['intro_cards'] = len(soup.find_all('div', class_=['exercise-card intro', 'exercise-card', 'intro']))
        results['easy_cards'] = len(soup.find_all('div', class_=['exercise-card easy', 'exercise-card', 'easy']))
        results['medium_cards'] = len(soup.find_all('div', class_=['exercise-card medium', 'exercise-card', 'medium']))
        results['hard_cards'] = len(soup.find_all('div', class_=['exercise-card hard', 'exercise-card', 'hard']))
        
        # Vérifier la structure des cartes
        cards_with_solutions = 0
        cards_with_toggle_buttons = 0
        
        for card in exercise_cards:
            # Vérifier la présence du bouton de solution
            toggle_btn = card.find('button', class_='toggle-solution')
            if toggle_btn:
                cards_with_toggle_buttons += 1
            
            # Vérifier la présence de la solution
            solution = card.find('div', class_='solution')
            if solution:
                cards_with_solutions += 1
        
        results['cards_with_solutions'] = cards_with_solutions
        results['cards_with_toggle_buttons'] = cards_with_toggle_buttons
        results['all_cards_have_solutions'] = cards_with_solutions == len(exercise_cards)
        results['all_cards_have_toggle_buttons'] = cards_with_toggle_buttons == len(exercise_cards)
        
        return results
    
    def validate_file(self, file_path: str) -> Dict[str, any]:
        """
        Valide un fichier d'exercice complet.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except Exception as e:
            return {'error': f'Impossible de lire le fichier: {e}'}
        
        results = {
            'file_path': file_path,
            'file_size': len(html_content),
            'validation_timestamp': None
        }
        
        # Effectuer toutes les validations
        results.update(self.validate_html_structure(html_content))
        results.update(self.validate_css_presence(html_content))
        results.update(self.validate_javascript(html_content))
        results.update(self.validate_sections(html_content))
        results.update(self.validate_exercise_cards(html_content))
        
        # Calculer un score global
        total_checks = 0
        passed_checks = 0
        
        for key, value in results.items():
            if isinstance(value, bool) and not key.endswith('_is_empty'):
                total_checks += 1
                if value:
                    passed_checks += 1
            elif key.endswith('_is_empty') and isinstance(value, bool):
                total_checks += 1
                if not value:  # Une section vide est un problème
                    passed_checks += 1
        
        results['validation_score'] = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        results['is_valid'] = results['validation_score'] >= 80  # Seuil de 80%
        
        return results
    
    def generate_report(self, validation_results: List[Dict]) -> str:
        """
        Génère un rapport de validation.
        """
        report = []
        report.append("=" * 80)
        report.append("RAPPORT DE VALIDATION DES FICHES D'EXERCICES")
        report.append("=" * 80)
        report.append("")
        
        total_files = len(validation_results)
        valid_files = sum(1 for r in validation_results if r.get('is_valid', False))
        
        report.append(f"📊 RÉSUMÉ GLOBAL")
        report.append(f"   Fichiers analysés: {total_files}")
        report.append(f"   Fichiers valides: {valid_files}")
        report.append(f"   Fichiers avec problèmes: {total_files - valid_files}")
        report.append(f"   Taux de réussite: {(valid_files/total_files*100):.1f}%")
        report.append("")
        
        # Détails par fichier
        for result in validation_results:
            if 'error' in result:
                report.append(f"❌ {result['file_path']}")
                report.append(f"   Erreur: {result['error']}")
                continue
            
            status = "✅" if result.get('is_valid', False) else "❌"
            score = result.get('validation_score', 0)
            report.append(f"{status} {Path(result['file_path']).name} (Score: {score:.1f}%)")
            
            # Problèmes détectés
            problems = []
            if not result.get('has_css_link', True):
                problems.append("CSS manquant")
            if not result.get('has_navigation', True):
                problems.append("Navigation manquante")
            if not result.get('has_function_showSection', True):
                problems.append("Fonction showSection manquante")
            if not result.get('has_function_toggleSolution', True):
                problems.append("Fonction toggleSolution manquante")
            
            # Vérifier les sections vides
            empty_sections = []
            for section in ['intro', 'easy', 'medium', 'hard']:
                if result.get(f'section-{section}_is_empty', False):
                    empty_sections.append(section)
            
            if empty_sections:
                problems.append(f"Sections vides: {', '.join(empty_sections)}")
            
            if problems:
                report.append(f"   Problèmes: {'; '.join(problems)}")
            
            # Statistiques des exercices
            total_cards = result.get('total_exercise_cards', 0)
            if total_cards > 0:
                report.append(f"   Exercices: {total_cards} cartes au total")
            
            report.append("")
        
        return "\n".join(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_exercise_sheets.py <directory_path> [output_report.txt]")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    validator = ExerciseSheetValidator()
    
    # Trouver tous les fichiers HTML d'exercices
    html_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html') and ('Fiche' in file or 'fiche' in file or 'exercice' in file):
                html_files.append(os.path.join(root, file))
    
    if not html_files:
        print(f"❌ Aucun fichier HTML trouvé dans {directory_path}")
        sys.exit(1)
    
    print(f"🔍 Validation de {len(html_files)} fichiers...")
    
    # Valider tous les fichiers
    results = []
    for file_path in sorted(html_files):
        print(f"   Validation de {Path(file_path).name}...")
        result = validator.validate_file(file_path)
        results.append(result)
    
    # Générer le rapport
    report = validator.generate_report(results)
    
    # Afficher le rapport
    print("\n" + report)
    
    # Sauvegarder le rapport si demandé
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n📄 Rapport sauvegardé dans {output_file}")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
    
    # Code de sortie basé sur les résultats
    valid_count = sum(1 for r in results if r.get('is_valid', False))
    sys.exit(0 if valid_count == len(results) else 1)

if __name__ == "__main__":
    main()