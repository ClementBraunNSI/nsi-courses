#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour parser un fichier JSON d'exercices et générer un fichier HTML
avec template interactif et animations slide pour les corrections.

Usage:
    python json_to_html_parser.py input.json output.html
"""

import json
import sys
import os
from pathlib import Path

def escape_html(text):
    """Échappe les caractères HTML spéciaux."""
    if not text:
        return ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))

def format_code(code):
    """Formate le code Python avec coloration syntaxique basique."""
    if not code:
        return ""
    
    # Remplace les retours à la ligne par des <br> et ajoute la coloration
    lines = code.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Échappe d'abord le HTML
        escaped_line = escape_html(line)
        
        # Ajoute une coloration basique
        if line.strip().startswith('#'):
            escaped_line = f'<span class="comment">{escaped_line}</span>'
        elif any(keyword in line for keyword in ['def ', 'for ', 'while ', 'if ', 'else:', 'elif ']):
            escaped_line = f'<span class="keyword">{escaped_line}</span>'
        elif 'print(' in line:
            escaped_line = f'<span class="function">{escaped_line}</span>'
        
        formatted_lines.append(escaped_line)
    
    return '<br>'.join(formatted_lines)

def generate_exercise_card(exercise, difficulty, exercise_number):
    """Génère le HTML pour une carte d'exercice."""
    nom = escape_html(exercise.get('nom', ''))
    enonce = escape_html(exercise.get('enonce', ''))
    exemple = escape_html(exercise.get('exemple', ''))
    correction = format_code(exercise.get('correction', ''))
    
    # Icônes de difficulté
    difficulty_icons = {
        'facile': '🦊',
        'moyen': '🦊🦊', 
        'difficile': '🦊🦊🦊'
    }
    
    difficulty_colors = {
        'facile': 'easy',
        'moyen': 'medium',
        'difficile': 'hard'
    }
    
    icon = difficulty_icons.get(difficulty, '🦊')
    color_class = difficulty_colors.get(difficulty, 'easy')
    
    exemple_html = f'<p class="example"><em>Exemple :</em> {exemple}</p>' if exemple else ''
    
    return f"""
    <div class="exercise-card {color_class}" id="exercise-{difficulty}-{exercise_number}">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge {color_class}">{icon} {difficulty.capitalize()}</div>
            <h3 class="exercise-title">Exercice {exercise_number} : {nom}</h3>
            <div class="exercise-content">
                <p>{enonce}</p>
                {exemple_html}
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>💡 Solution :</h4>
                <pre class="code-block"><code>{correction}</code></pre>
            </div>
        </div>
    </div>
    """

def generate_html_template(exercises_data, title="Fiche d'exercices"):
    """Génère le template HTML complet."""
    
    # Génère les sections d'exercices
    sections = {
        'facile': '',
        'moyen': '',
        'difficile': ''
    }
    
    for difficulty in ['facile', 'moyen', 'difficile']:
        if difficulty in exercises_data:
            exercises = exercises_data[difficulty]
            for i, exercise in enumerate(exercises, 1):
                sections[difficulty] += generate_exercise_card(exercise, difficulty, i)
    
    # Template HTML complet
    html_template = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_html(title)}</title>
    <style>
        /* Styles pour les fiches d'exercices avec animations slide */
        * {{
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        
        .exercise-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        
        .exercise-header h1 {{
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
        }}
        
        .section-tabs {{
            display: flex;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .tab-button {{
            flex: 1;
            background: none;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            border-bottom: 3px solid transparent;
        }}
        
        .tab-button:hover {{
            background: #e9ecef;
        }}
        
        .tab-button.active {{
            background: white;
            border-bottom-color: #667eea;
            color: #667eea;
        }}
        
        .section-content {{
            display: none;
            padding: 2rem;
        }}
        
        .section-content.active {{
            display: block;
        }}
        
        .exercise-cards {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}
        
        .exercise-card {{
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 4px solid;
            display: flex;
            min-height: 200px;
        }}
        
        .exercise-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }}
        
        .exercise-card.easy {{
            border-left-color: #28a745;
        }}
        
        .exercise-card.medium {{
            border-left-color: #ffc107;
        }}
        
        .exercise-card.hard {{
            border-left-color: #dc3545;
        }}
        
        .exercise-content-wrapper {{
            flex: 1;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
        }}
        
        .difficulty-badge {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 1rem;
            width: fit-content;
        }}
        
        .difficulty-badge.easy {{
            background: rgba(40, 167, 69, 0.1);
            color: #28a745;
        }}
        
        .difficulty-badge.medium {{
            background: rgba(255, 193, 7, 0.1);
            color: #ffc107;
        }}
        
        .difficulty-badge.hard {{
            background: rgba(220, 53, 69, 0.1);
            color: #dc3545;
        }}
        
        .exercise-title {{
            margin: 0 0 1rem 0;
            font-size: 1.3rem;
            font-weight: 600;
            color: #2c3e50;
        }}
        
        .exercise-content {{
            flex: 1;
            margin-bottom: 1rem;
        }}
        
        .example {{
            background: #f8f9fa;
            padding: 0.8rem;
            border-radius: 6px;
            border-left: 3px solid #6c757d;
            margin: 1rem 0;
            font-style: italic;
        }}
        
        .toggle-solution {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            width: fit-content;
        }}
        
        .toggle-solution:hover {{
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}
        
        .arrow {{
            transition: transform 0.3s ease;
            font-size: 1.2rem;
        }}
        
        .toggle-solution.active .arrow {{
            transform: rotate(90deg);
        }}
        
        .solution-wrapper {{
            width: 0;
            overflow: hidden;
            transition: width 0.4s ease;
            background: #f8f9fa;
            border-left: 1px solid #e9ecef;
        }}
        
        .solution-wrapper.show {{
            width: 45%;
            padding: 1.5rem;
        }}
        
        .solution h4 {{
            margin: 0 0 1rem 0;
            color: #28a745;
            font-size: 1.1rem;
        }}
        
        .code-block {{
            background: #2d3748;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            line-height: 1.4;
        }}
        
        .code-block .comment {{
            color: #68d391;
        }}
        
        .code-block .keyword {{
            color: #63b3ed;
        }}
        
        .code-block .function {{
            color: #f6ad55;
        }}
        
        @media (max-width: 768px) {{
            .exercise-card {{
                flex-direction: column;
            }}
            
            .solution-wrapper.show {{
                width: 100%;
                border-left: none;
                border-top: 1px solid #e9ecef;
            }}
            
            .section-tabs {{
                flex-direction: column;
            }}
            
            .exercise-header h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="exercise-header">
            <h1>{escape_html(title)}</h1>
            <p>Exercices interactifs avec corrections</p>
        </header>

        <!-- Navigation par onglets -->
        <nav class="section-tabs">
            <button class="tab-button active" onclick="showSection('facile')">🦊 Facile</button>
            <button class="tab-button" onclick="showSection('moyen')">🦊🦊 Moyen</button>
            <button class="tab-button" onclick="showSection('difficile')">🦊🦊🦊 Difficile</button>
        </nav>

        <!-- Section Facile -->
        <div id="facile-section" class="section-content active">
            <div class="exercise-cards">
                {sections['facile'] if sections['facile'] else '<p>Aucun exercice facile disponible.</p>'}
            </div>
        </div>

        <!-- Section Moyen -->
        <div id="moyen-section" class="section-content">
            <div class="exercise-cards">
                {sections['moyen'] if sections['moyen'] else '<p>Aucun exercice moyen disponible.</p>'}
            </div>
        </div>

        <!-- Section Difficile -->
        <div id="difficile-section" class="section-content">
            <div class="exercise-cards">
                {sections['difficile'] if sections['difficile'] else '<p>Aucun exercice difficile disponible.</p>'}
            </div>
        </div>
    </div>

    <script>
        // Fonction pour changer de section
        function showSection(sectionName) {{
            // Masquer toutes les sections
            const sections = document.querySelectorAll('.section-content');
            sections.forEach(section => {{
                section.classList.remove('active');
            }});

            // Désactiver tous les boutons
            const buttons = document.querySelectorAll('.tab-button');
            buttons.forEach(button => {{
                button.classList.remove('active');
            }});

            // Afficher la section sélectionnée
            const targetSection = document.getElementById(sectionName + '-section');
            if (targetSection) {{
                targetSection.classList.add('active');
            }}

            // Activer le bouton correspondant
            const targetButton = document.querySelector(`[onclick="showSection('${{sectionName}}')"`);
            if (targetButton) {{
                targetButton.classList.add('active');
            }}
        }}

        // Fonction pour afficher/masquer les solutions avec animation slide
        function toggleSolution(button) {{
            const card = button.closest('.exercise-card');
            const solutionWrapper = card.querySelector('.solution-wrapper');
            const arrow = button.querySelector('.arrow');
            
            if (solutionWrapper.classList.contains('show')) {{
                // Masquer la solution
                solutionWrapper.classList.remove('show');
                button.classList.remove('active');
                button.innerHTML = '<span class="arrow">→</span> Voir la correction';
            }} else {{
                // Afficher la solution
                solutionWrapper.classList.add('show');
                button.classList.add('active');
                button.innerHTML = '<span class="arrow">→</span> Masquer la correction';
            }}
        }}

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {{
            console.log('Fiche d\'exercices chargée avec succès!');
        }});
    </script>
</body>
</html>
    """
    
    return html_template

def main():
    """Fonction principale du script."""
    if len(sys.argv) != 3:
        print("Usage: python json_to_html_parser.py input.json output.html")
        print("Exemple: python json_to_html_parser.py exercices_boucles.json fiche_boucles.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Vérifier que le fichier d'entrée existe
    if not os.path.exists(input_file):
        print(f"Erreur: Le fichier {input_file} n'existe pas.")
        sys.exit(1)
    
    try:
        # Charger le fichier JSON
        with open(input_file, 'r', encoding='utf-8') as f:
            exercises_data = json.load(f)
        
        # Générer le titre basé sur le nom du fichier
        title = Path(input_file).stem.replace('_', ' ').title()
        
        # Générer le HTML
        html_content = generate_html_template(exercises_data, title)
        
        # Sauvegarder le fichier HTML
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Fichier HTML généré avec succès: {output_file}")
        print(f"📊 Exercices traités:")
        for difficulty in ['facile', 'moyen', 'difficile']:
            if difficulty in exercises_data:
                count = len(exercises_data[difficulty])
                print(f"   - {difficulty.capitalize()}: {count} exercice(s)")
    
    except json.JSONDecodeError as e:
        print(f"Erreur: Le fichier JSON n'est pas valide: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()