#!/usr/bin/env python3
"""
Generateur automatique de fiches d'exercices HTML à partir de données JSON.
Utilise les templates HTML et le schéma JSON pour créer des fiches cohérentes.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, List
import jsonschema
from jinja2 import Template, Environment, FileSystemLoader

class ExerciseHTMLGenerator:
    def __init__(self, templates_dir: str, schemas_dir: str):
        self.templates_dir = Path(templates_dir)
        self.schemas_dir = Path(schemas_dir)
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        
        # Charger le schéma de validation
        schema_path = self.schemas_dir / "exercise_schema.json"
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.schema = json.load(f)
    
    def validate_exercise_data(self, data: Dict[str, Any]) -> bool:
        """
        Valide les données d'exercice contre le schéma JSON.
        """
        try:
            jsonschema.validate(data, self.schema)
            return True
        except jsonschema.ValidationError as e:
            print(f"❌ Erreur de validation: {e.message}")
            print(f"   Chemin: {' -> '.join(str(p) for p in e.path)}")
            return False
        except jsonschema.SchemaError as e:
            print(f"❌ Erreur de schéma: {e.message}")
            return False
    
    def generate_exercise_cards(self, exercises: List[Dict], difficulty: str) -> str:
        """
        Génère les cartes d'exercices pour une section donnée.
        """
        cards_html = []
        
        for i, exercise in enumerate(exercises, 1):
            # Préparer les données pour le template
            template_data = {
                'NUMBER': exercise.get('number', i),
                'TITLE': exercise['title'],
                'CONTENT': exercise['content'],
                'EXAMPLE': exercise.get('example', ''),
                'SOLUTION_CODE': exercise['solution']['code'],
                'EXPLANATION': exercise['solution'].get('explanation', ''),
                'CONSTRAINTS': exercise.get('constraints', []),
                'HINTS': exercise.get('hints', []),
                'COMPLEXITY': exercise.get('difficulty_indicators', {}).get('complexity', ''),
                'ALTERNATIVE_SOLUTIONS': exercise['solution'].get('alternative_solutions', []),
                'COMPLEXITY_ANALYSIS': exercise['solution'].get('complexity_analysis', '')
            }
            
            # Sélectionner le template approprié
            if difficulty == 'easy':
                template_name = 'easy-exercise-template'
            elif difficulty == 'medium':
                template_name = 'medium-exercise-template'
            else:
                template_name = 'hard-exercise-template'
            
            # Générer la carte d'exercice
            card_html = self.render_exercise_card(template_data, difficulty)
            cards_html.append(card_html)
        
        return '\n'.join(cards_html)
    
    def render_exercise_card(self, data: Dict, difficulty: str) -> str:
        """
        Rend une carte d'exercice individuelle.
        """
        if difficulty == 'easy':
            template = f'''
            <div class="exercise-card easy">
                <h3>Exercice {data['NUMBER']} : {data['TITLE']}</h3>
                <div class="exercise-content">
                    {data['CONTENT']}
                    {f'<p><em>Exemple :</em> <code>{data["EXAMPLE"]}</code></p>' if data['EXAMPLE'] else ''}
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">→ Voir la correction</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <h4>💡 Solution :</h4>
                        <pre><code>{data['SOLUTION_CODE']}</code></pre>
                        {f'<p><strong>Explication :</strong> {data["EXPLANATION"]}</p>' if data['EXPLANATION'] else ''}
                    </div>
                </div>
            </div>
            '''
        elif difficulty == 'medium':
            constraints_html = ''
            if data['CONSTRAINTS']:
                constraints_list = '\n'.join(f'<li>{c}</li>' for c in data['CONSTRAINTS'])
                constraints_html = f'''
                <div class="constraints">
                    <p><strong>Contraintes :</strong></p>
                    <ul>{constraints_list}</ul>
                </div>
                '''
            
            template = f'''
            <div class="exercise-card medium">
                <h3>Exercice {data['NUMBER']} : {data['TITLE']}</h3>
                <div class="exercise-content">
                    {data['CONTENT']}
                    {constraints_html}
                    {f'<p><em>Exemple :</em> <code>{data["EXAMPLE"]}</code></p>' if data['EXAMPLE'] else ''}
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">→ Voir la correction</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <h4>💡 Solution :</h4>
                        <pre><code>{data['SOLUTION_CODE']}</code></pre>
                        {f'<p><strong>Explication :</strong> {data["EXPLANATION"]}</p>' if data['EXPLANATION'] else ''}
                    </div>
                </div>
            </div>
            '''
        else:  # hard
            hints_html = ''
            if data['HINTS']:
                hints_list = '\n'.join(f'<li>{h}</li>' for h in data['HINTS'])
                hints_html = f'''
                <div class="hints">
                    <p><strong>💡 Indices :</strong></p>
                    <ol>{hints_list}</ol>
                </div>
                '''
            
            alternatives_html = ''
            if data['ALTERNATIVE_SOLUTIONS']:
                for i, alt in enumerate(data['ALTERNATIVE_SOLUTIONS']):
                    alternatives_html += f'''
                    <h5>Alternative {i+1} :</h5>
                    <pre><code>{alt['code']}</code></pre>
                    <p>{alt['description']}</p>
                    '''
            
            template = f'''
            <div class="exercise-card hard">
                <h3>Exercice {data['NUMBER']} : {data['TITLE']}</h3>
                <div class="exercise-content">
                    {data['CONTENT']}
                    {hints_html}
                    {f'<p><strong>Complexité attendue :</strong> {data["COMPLEXITY"]}</p>' if data['COMPLEXITY'] else ''}
                    {f'<p><em>Exemple :</em> <code>{data["EXAMPLE"]}</code></p>' if data['EXAMPLE'] else ''}
                </div>
                <button class="toggle-solution" onclick="toggleSolution(this)">→ Voir la correction</button>
                <div class="solution-wrapper">
                    <div class="solution">
                        <h4>💡 Solution :</h4>
                        <pre><code>{data['SOLUTION_CODE']}</code></pre>
                        {alternatives_html}
                        {f'<p><strong>Explication détaillée :</strong> {data["EXPLANATION"]}</p>' if data['EXPLANATION'] else ''}
                        {f'<p><strong>Analyse de complexité :</strong> {data["COMPLEXITY_ANALYSIS"]}</p>' if data['COMPLEXITY_ANALYSIS'] else ''}
                    </div>
                </div>
            </div>
            '''
        
        return template
    
    def generate_introduction_section(self, intro_data: Dict) -> str:
        """
        Génère la section d'introduction.
        """
        key_concepts_html = ''
        if intro_data.get('key_concepts'):
            concepts_list = '\n'.join(
                f'<li><strong>{concept["name"]}</strong> : {concept["description"]}</li>'
                for concept in intro_data['key_concepts']
            )
            key_concepts_html = f'<ul>{concepts_list}</ul>'
        
        tips_html = ''
        if intro_data.get('tips'):
            tips_html = f'''
            <div class="alert alert-info">
                <p><strong>💡 Conseils</strong></p>
                <p>{intro_data['tips']}</p>
            </div>
            '''
        
        return f'''
        <div class="exercise-card intro">
            <h3>📚 Introduction - {intro_data['topic']}</h3>
            <div class="exercise-content">
                <p>{intro_data['description']}</p>
                {key_concepts_html}
                {tips_html}
            </div>
        </div>
        '''
    
    def generate_html_file(self, exercise_data: Dict, output_path: str) -> bool:
        """
        Génère un fichier HTML complet à partir des données d'exercice.
        """
        # Valider les données
        if not self.validate_exercise_data(exercise_data):
            return False
        
        # Charger le template de base
        base_template_path = self.templates_dir / "base_exercise_template.html"
        with open(base_template_path, 'r', encoding='utf-8') as f:
            base_template = f.read()
        
        # Générer les sections
        intro_html = self.generate_introduction_section(exercise_data['introduction'])
        easy_html = self.generate_exercise_cards(exercise_data['sections']['easy']['exercises'], 'easy')
        medium_html = self.generate_exercise_cards(exercise_data['sections']['medium']['exercises'], 'medium')
        hard_html = self.generate_exercise_cards(exercise_data['sections']['hard']['exercises'], 'hard')
        
        # Remplacer les placeholders dans le template
        html_content = base_template.replace('{{TITLE}}', exercise_data['metadata']['title'])
        html_content = html_content.replace('{{SUBTITLE}}', exercise_data['metadata'].get('subtitle', ''))
        html_content = html_content.replace('{{INTRO_CONTENT}}', intro_html)
        html_content = html_content.replace('{{EASY_CONTENT}}', easy_html)
        html_content = html_content.replace('{{MEDIUM_CONTENT}}', medium_html)
        html_content = html_content.replace('{{HARD_CONTENT}}', hard_html)
        
        # Écrire le fichier
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ Fichier généré avec succès: {output_path}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier: {e}")
            return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_exercise_html.py <input_json> <output_html>")
        sys.exit(1)
    
    input_json = sys.argv[1]
    output_html = sys.argv[2]
    
    # Chemins des répertoires
    script_dir = Path(__file__).parent
    templates_dir = script_dir.parent / "templates"
    schemas_dir = script_dir.parent / "schemas"
    
    # Créer le générateur
    generator = ExerciseHTMLGenerator(str(templates_dir), str(schemas_dir))
    
    # Charger les données JSON
    try:
        with open(input_json, 'r', encoding='utf-8') as f:
            exercise_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lors du chargement du fichier JSON: {e}")
        sys.exit(1)
    
    # Générer le fichier HTML
    success = generator.generate_html_file(exercise_data, output_html)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()