#!/usr/bin/env python3
"""
Script de test pour vérifier le bon fonctionnement des fiches d'exercices.
Vérifie la structure HTML, le CSS, le JavaScript et l'accessibilité.
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple
from bs4 import BeautifulSoup

class ExerciseSheetTester:
    def __init__(self):
        self.test_results = []
        
    def test_html_structure(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste la structure HTML de base."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        # Test 1: Présence du DOCTYPE
        results['max_score'] += 1
        if soup.find('html'):
            results['tests'].append({'name': 'DOCTYPE HTML5', 'status': 'PASS', 'message': 'DOCTYPE présent'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'DOCTYPE HTML5', 'status': 'FAIL', 'message': 'DOCTYPE manquant'})
        
        # Test 2: Métadonnées de base
        results['max_score'] += 3
        meta_charset = soup.find('meta', {'charset': True})
        if meta_charset:
            results['tests'].append({'name': 'Charset UTF-8', 'status': 'PASS', 'message': 'Charset défini'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Charset UTF-8', 'status': 'FAIL', 'message': 'Charset manquant'})
            
        meta_viewport = soup.find('meta', {'name': 'viewport'})
        if meta_viewport:
            results['tests'].append({'name': 'Viewport', 'status': 'PASS', 'message': 'Viewport défini'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Viewport', 'status': 'FAIL', 'message': 'Viewport manquant'})
            
        title_tag = soup.find('title')
        if title_tag and title_tag.get_text().strip():
            results['tests'].append({'name': 'Titre', 'status': 'PASS', 'message': f'Titre: {title_tag.get_text()[:50]}...'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Titre', 'status': 'FAIL', 'message': 'Titre manquant ou vide'})
        
        return results
    
    def test_css_resources(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste la présence des ressources CSS."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        # Vérifier les liens CSS
        css_links = soup.find_all('link', {'rel': 'stylesheet'})
        required_css = ['exercise-cards.css', 'extra.css']
        
        for css_file in required_css:
            results['max_score'] += 1
            found = any(css_file in link.get('href', '') for link in css_links)
            if found:
                results['tests'].append({'name': f'CSS {css_file}', 'status': 'PASS', 'message': f'{css_file} trouvé'})
                results['score'] += 1
            else:
                results['tests'].append({'name': f'CSS {css_file}', 'status': 'FAIL', 'message': f'{css_file} manquant'})
        
        return results
    
    def test_navigation_structure(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste la structure de navigation par onglets."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        # Test 1: Présence de la navigation
        results['max_score'] += 1
        nav_tabs = soup.find('nav', class_='section-tabs')
        if nav_tabs:
            results['tests'].append({'name': 'Navigation tabs', 'status': 'PASS', 'message': 'Navigation présente'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Navigation tabs', 'status': 'FAIL', 'message': 'Navigation manquante'})
            return results
        
        # Test 2: Boutons de navigation
        required_sections = ['intro', 'easy', 'medium', 'hard']
        tab_buttons = nav_tabs.find_all('button', class_='tab-button')
        
        for section in required_sections:
            results['max_score'] += 1
            found = any(f"showSection('{section}')" in button.get('onclick', '') for button in tab_buttons)
            if found:
                results['tests'].append({'name': f'Bouton {section}', 'status': 'PASS', 'message': f'Bouton {section} présent'})
                results['score'] += 1
            else:
                results['tests'].append({'name': f'Bouton {section}', 'status': 'FAIL', 'message': f'Bouton {section} manquant'})
        
        return results
    
    def test_sections_content(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste le contenu des sections."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        required_sections = {
            'intro-section': 'Introduction',
            'easy-section': 'Facile',
            'medium-section': 'Intermédiaire',
            'hard-section': 'Difficile'
        }
        
        for section_id, section_name in required_sections.items():
            results['max_score'] += 2
            
            # Vérifier la présence de la section
            section = soup.find('div', id=section_id)
            if section:
                results['tests'].append({'name': f'Section {section_name}', 'status': 'PASS', 'message': f'Section {section_name} présente'})
                results['score'] += 1
                
                # Vérifier le contenu
                exercise_cards = section.find_all('div', class_='exercise-card')
                if exercise_cards:
                    results['tests'].append({'name': f'Contenu {section_name}', 'status': 'PASS', 'message': f'{len(exercise_cards)} carte(s) d\'exercice'})
                    results['score'] += 1
                else:
                    results['tests'].append({'name': f'Contenu {section_name}', 'status': 'WARN', 'message': 'Section vide'})
            else:
                results['tests'].append({'name': f'Section {section_name}', 'status': 'FAIL', 'message': f'Section {section_name} manquante'})
                results['tests'].append({'name': f'Contenu {section_name}', 'status': 'FAIL', 'message': 'Impossible de vérifier le contenu'})
        
        return results
    
    def test_javascript_functions(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste la présence des fonctions JavaScript."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        # Récupérer tout le JavaScript
        scripts = soup.find_all('script')
        js_content = ' '.join([script.get_text() for script in scripts if script.get_text()])
        
        required_functions = ['showSection', 'toggleSolution']
        
        for func_name in required_functions:
            results['max_score'] += 1
            if f'function {func_name}' in js_content or f'{func_name}(' in js_content:
                results['tests'].append({'name': f'Fonction {func_name}', 'status': 'PASS', 'message': f'Fonction {func_name} présente'})
                results['score'] += 1
            else:
                results['tests'].append({'name': f'Fonction {func_name}', 'status': 'FAIL', 'message': f'Fonction {func_name} manquante'})
        
        return results
    
    def test_exercise_cards(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste la structure des cartes d'exercices."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        exercise_cards = soup.find_all('div', class_='exercise-card')
        
        if not exercise_cards:
            results['max_score'] += 1
            results['tests'].append({'name': 'Cartes d\'exercices', 'status': 'FAIL', 'message': 'Aucune carte d\'exercice trouvée'})
            return results
        
        results['max_score'] += len(exercise_cards)
        
        for i, card in enumerate(exercise_cards, 1):
            card_valid = True
            issues = []
            
            # Vérifier le titre
            title = card.find('h3')
            if not title or not title.get_text().strip():
                card_valid = False
                issues.append('titre manquant')
            
            # Vérifier le contenu
            content = card.find('div', class_='exercise-content')
            if not content:
                card_valid = False
                issues.append('contenu manquant')
            
            # Vérifier le bouton solution (sauf pour intro)
            if 'intro' not in card.get('class', []):
                solution_btn = card.find('button', class_='toggle-solution')
                if not solution_btn:
                    card_valid = False
                    issues.append('bouton solution manquant')
                
                solution_wrapper = card.find('div', class_='solution-wrapper')
                if not solution_wrapper:
                    card_valid = False
                    issues.append('wrapper solution manquant')
            
            if card_valid:
                results['tests'].append({'name': f'Carte {i}', 'status': 'PASS', 'message': 'Structure valide'})
                results['score'] += 1
            else:
                results['tests'].append({'name': f'Carte {i}', 'status': 'FAIL', 'message': f'Problèmes: {", ".join(issues)}'})
        
        return results
    
    def test_accessibility(self, soup: BeautifulSoup, file_path: str) -> Dict:
        """Teste l'accessibilité de base."""
        results = {
            'file': file_path,
            'tests': [],
            'score': 0,
            'max_score': 0
        }
        
        # Test 1: Attribut lang
        results['max_score'] += 1
        html_tag = soup.find('html')
        if html_tag and html_tag.get('lang'):
            results['tests'].append({'name': 'Attribut lang', 'status': 'PASS', 'message': f'Langue: {html_tag.get("lang")}'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Attribut lang', 'status': 'FAIL', 'message': 'Attribut lang manquant'})
        
        # Test 2: Structure des titres
        results['max_score'] += 1
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if headings:
            results['tests'].append({'name': 'Structure titres', 'status': 'PASS', 'message': f'{len(headings)} titre(s) trouvé(s)'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Structure titres', 'status': 'WARN', 'message': 'Aucun titre trouvé'})
        
        # Test 3: Boutons avec onclick
        results['max_score'] += 1
        buttons = soup.find_all('button')
        buttons_with_onclick = [btn for btn in buttons if btn.get('onclick')]
        if buttons_with_onclick:
            results['tests'].append({'name': 'Boutons interactifs', 'status': 'PASS', 'message': f'{len(buttons_with_onclick)} bouton(s) interactif(s)'})
            results['score'] += 1
        else:
            results['tests'].append({'name': 'Boutons interactifs', 'status': 'WARN', 'message': 'Aucun bouton interactif'})
        
        return results
    
    def test_file(self, file_path: str) -> Dict:
        """Teste un fichier d'exercices complet."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Exécuter tous les tests
            test_results = [
                self.test_html_structure(soup, file_path),
                self.test_css_resources(soup, file_path),
                self.test_navigation_structure(soup, file_path),
                self.test_sections_content(soup, file_path),
                self.test_javascript_functions(soup, file_path),
                self.test_exercise_cards(soup, file_path),
                self.test_accessibility(soup, file_path)
            ]
            
            # Calculer le score global
            total_score = sum(result['score'] for result in test_results)
            total_max_score = sum(result['max_score'] for result in test_results)
            
            return {
                'file': file_path,
                'total_score': total_score,
                'total_max_score': total_max_score,
                'percentage': (total_score / total_max_score * 100) if total_max_score > 0 else 0,
                'test_categories': test_results
            }
            
        except Exception as e:
            return {
                'file': file_path,
                'error': str(e),
                'total_score': 0,
                'total_max_score': 0,
                'percentage': 0
            }
    
    def generate_report(self, results: List[Dict], output_file: str = None) -> str:
        """Génère un rapport détaillé des tests."""
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("RAPPORT DE TEST DES FICHES D'EXERCICES")
        report_lines.append("=" * 80)
        report_lines.append("")
        
        # Statistiques globales
        total_files = len(results)
        passed_files = len([r for r in results if r.get('percentage', 0) >= 80])
        
        report_lines.append(f"📊 STATISTIQUES GLOBALES")
        report_lines.append(f"   Fichiers testés: {total_files}")
        report_lines.append(f"   Fichiers réussis (≥80%): {passed_files}")
        report_lines.append(f"   Taux de réussite: {passed_files/total_files*100:.1f}%")
        report_lines.append("")
        
        # Détails par fichier
        for result in results:
            if 'error' in result:
                report_lines.append(f"❌ {Path(result['file']).name}")
                report_lines.append(f"   Erreur: {result['error']}")
                report_lines.append("")
                continue
            
            percentage = result['percentage']
            status_icon = "✅" if percentage >= 80 else "⚠️" if percentage >= 60 else "❌"
            
            report_lines.append(f"{status_icon} {Path(result['file']).name} ({percentage:.1f}%)")
            report_lines.append(f"   Score: {result['total_score']}/{result['total_max_score']}")
            
            # Détails des tests échoués
            failed_tests = []
            for category in result['test_categories']:
                for test in category['tests']:
                    if test['status'] == 'FAIL':
                        failed_tests.append(f"{test['name']}: {test['message']}")
            
            if failed_tests:
                report_lines.append(f"   Échecs: {'; '.join(failed_tests)}")
            
            report_lines.append("")
        
        report_content = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"📄 Rapport sauvegardé: {output_file}")
        
        return report_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_exercise_sheets.py <file_or_directory> [output_report]")
        sys.exit(1)
    
    target = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    tester = ExerciseSheetTester()
    
    files_to_test = []
    
    if os.path.isfile(target):
        files_to_test.append(target)
    elif os.path.isdir(target):
        # Trouver tous les fichiers d'exercices
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith('.html') and ('fiche' in file.lower() or 'exercice' in file.lower()):
                    files_to_test.append(os.path.join(root, file))
    else:
        print(f"❌ Fichier ou répertoire non trouvé: {target}")
        sys.exit(1)
    
    if not files_to_test:
        print("❌ Aucun fichier d'exercice trouvé")
        sys.exit(1)
    
    print(f"🧪 Test de {len(files_to_test)} fichier(s)...")
    
    results = []
    for file_path in files_to_test:
        print(f"   Testing {Path(file_path).name}...")
        result = tester.test_file(file_path)
        results.append(result)
    
    # Générer le rapport
    report = tester.generate_report(results, output_file)
    print(report)
    
    # Code de sortie basé sur les résultats
    passed_files = len([r for r in results if r.get('percentage', 0) >= 80])
    if passed_files == len(results):
        print("🎉 Tous les tests sont réussis!")
        sys.exit(0)
    else:
        print(f"⚠️ {len(results) - passed_files} fichier(s) ont échoué aux tests")
        sys.exit(1)

if __name__ == "__main__":
    main()