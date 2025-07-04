#!/usr/bin/env python3
"""
Script de déploiement complet du système de fiches d'exercices.
Automatise la validation, correction et test de toutes les fiches.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

class ExerciseSystemDeployer:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.scripts_dir = self.base_dir / "scripts"
        self.docs_dir = self.base_dir / "docs"
        
        # Vérifier que tous les scripts existent
        required_scripts = [
            "validate_exercise_sheets.py",
            "fix_exercise_sheets.py",
            "test_exercise_sheets.py"
        ]
        
        for script in required_scripts:
            script_path = self.scripts_dir / script
            if not script_path.exists():
                raise FileNotFoundError(f"Script manquant: {script_path}")
    
    def run_script(self, script_name: str, args: list, description: str) -> tuple:
        """Exécute un script et retourne le code de sortie et la sortie."""
        print(f"🔄 {description}...")
        
        cmd = ["python3", str(self.scripts_dir / script_name)] + args
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.base_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes max
            )
            
            if result.returncode == 0:
                print(f"✅ {description} - Succès")
            else:
                print(f"❌ {description} - Échec (code {result.returncode})")
            
            return result.returncode, result.stdout, result.stderr
            
        except subprocess.TimeoutExpired:
            print(f"⏰ {description} - Timeout")
            return -1, "", "Timeout après 5 minutes"
        except Exception as e:
            print(f"💥 {description} - Erreur: {e}")
            return -1, "", str(e)
    
    def validate_directory(self, directory: str) -> dict:
        """Valide toutes les fiches d'un répertoire."""
        print(f"\n📁 Validation du répertoire: {directory}")
        
        code, stdout, stderr = self.run_script(
            "validate_exercise_sheets.py",
            [directory],
            f"Validation de {Path(directory).name}"
        )
        
        return {
            'directory': directory,
            'validation_code': code,
            'validation_output': stdout,
            'validation_errors': stderr
        }
    
    def fix_directory(self, directory: str) -> dict:
        """Corrige toutes les fiches d'un répertoire."""
        print(f"\n🔧 Correction du répertoire: {directory}")
        
        code, stdout, stderr = self.run_script(
            "fix_exercise_sheets.py",
            [directory],
            f"Correction de {Path(directory).name}"
        )
        
        return {
            'directory': directory,
            'fix_code': code,
            'fix_output': stdout,
            'fix_errors': stderr
        }
    
    def test_directory(self, directory: str, report_file: str = None) -> dict:
        """Teste toutes les fiches d'un répertoire."""
        print(f"\n🧪 Test du répertoire: {directory}")
        
        args = [directory]
        if report_file:
            args.append(report_file)
        
        code, stdout, stderr = self.run_script(
            "test_exercise_sheets.py",
            args,
            f"Test de {Path(directory).name}"
        )
        
        return {
            'directory': directory,
            'test_code': code,
            'test_output': stdout,
            'test_errors': stderr,
            'report_file': report_file
        }
    
    def deploy_level(self, level_name: str, level_path: str) -> dict:
        """Déploie complètement un niveau (seconde, premiere, terminale)."""
        print(f"\n{'='*60}")
        print(f"🎯 DÉPLOIEMENT NIVEAU: {level_name.upper()}")
        print(f"{'='*60}")
        
        results = {
            'level': level_name,
            'path': level_path,
            'timestamp': datetime.now().isoformat(),
            'steps': []
        }
        
        # Étape 1: Validation initiale
        validation_result = self.validate_directory(level_path)
        results['steps'].append(('validation_initial', validation_result))
        
        # Étape 2: Correction si nécessaire
        if validation_result['validation_code'] != 0:
            print("\n⚠️ Problèmes détectés, correction en cours...")
            fix_result = self.fix_directory(level_path)
            results['steps'].append(('correction', fix_result))
            
            # Étape 3: Re-validation après correction
            validation_result_2 = self.validate_directory(level_path)
            results['steps'].append(('validation_post_fix', validation_result_2))
        else:
            print("\n✅ Aucune correction nécessaire")
        
        # Étape 4: Tests de qualité
        report_file = str(self.docs_dir / f"test_report_{level_name}.txt")
        test_result = self.test_directory(level_path, report_file)
        results['steps'].append(('quality_tests', test_result))
        
        # Résumé du niveau
        success = test_result['test_code'] == 0
        results['success'] = success
        
        print(f"\n📊 RÉSUMÉ {level_name.upper()}:")
        if success:
            print(f"✅ Déploiement réussi")
        else:
            print(f"❌ Déploiement échoué")
        
        return results
    
    def deploy_all_levels(self, levels_config: dict) -> dict:
        """Déploie tous les niveaux configurés."""
        print(f"\n{'='*80}")
        print(f"🚀 DÉPLOIEMENT COMPLET DU SYSTÈME D'EXERCICES NSI")
        print(f"{'='*80}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        deployment_results = {
            'timestamp': datetime.now().isoformat(),
            'levels': {},
            'summary': {}
        }
        
        # Déployer chaque niveau
        for level_name, level_path in levels_config.items():
            if not os.path.exists(level_path):
                print(f"⚠️ Répertoire non trouvé: {level_path}")
                continue
            
            level_result = self.deploy_level(level_name, level_path)
            deployment_results['levels'][level_name] = level_result
        
        # Générer le résumé global
        total_levels = len(deployment_results['levels'])
        successful_levels = len([r for r in deployment_results['levels'].values() if r.get('success', False)])
        
        deployment_results['summary'] = {
            'total_levels': total_levels,
            'successful_levels': successful_levels,
            'success_rate': (successful_levels / total_levels * 100) if total_levels > 0 else 0,
            'overall_success': successful_levels == total_levels
        }
        
        # Afficher le résumé final
        print(f"\n{'='*80}")
        print(f"📊 RÉSUMÉ GLOBAL DU DÉPLOIEMENT")
        print(f"{'='*80}")
        print(f"Niveaux traités: {total_levels}")
        print(f"Niveaux réussis: {successful_levels}")
        print(f"Taux de réussite: {deployment_results['summary']['success_rate']:.1f}%")
        
        if deployment_results['summary']['overall_success']:
            print(f"\n🎉 DÉPLOIEMENT COMPLET RÉUSSI!")
        else:
            print(f"\n⚠️ Déploiement partiel - Vérifiez les logs")
        
        # Sauvegarder le rapport de déploiement
        report_file = self.docs_dir / f"deployment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(deployment_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Rapport de déploiement sauvegardé: {report_file}")
        
        return deployment_results
    
    def quick_check(self, levels_config: dict) -> bool:
        """Effectue une vérification rapide de tous les niveaux."""
        print(f"\n🔍 VÉRIFICATION RAPIDE")
        print(f"{'='*40}")
        
        all_good = True
        
        for level_name, level_path in levels_config.items():
            if not os.path.exists(level_path):
                print(f"❌ {level_name}: Répertoire non trouvé")
                all_good = False
                continue
            
            # Test rapide
            test_result = self.test_directory(level_path)
            if test_result['test_code'] == 0:
                print(f"✅ {level_name}: OK")
            else:
                print(f"❌ {level_name}: Problèmes détectés")
                all_good = False
        
        return all_good

def main():
    # Configuration par défaut
    base_dir = Path(__file__).parent.parent
    
    # Configuration des niveaux
    levels_config = {
        'terminale': str(base_dir / "site_final/public/courses-html/terminale"),
        # 'premiere': str(base_dir / "site_final/public/courses-html/premiere"),
        # 'seconde': str(base_dir / "site_final/public/courses-html/seconde")
    }
    
    # Créer le déployeur
    try:
        deployer = ExerciseSystemDeployer(str(base_dir))
    except FileNotFoundError as e:
        print(f"❌ Erreur d'initialisation: {e}")
        sys.exit(1)
    
    # Analyser les arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "check":
            # Vérification rapide
            success = deployer.quick_check(levels_config)
            sys.exit(0 if success else 1)
        
        elif command == "deploy":
            # Déploiement complet
            results = deployer.deploy_all_levels(levels_config)
            sys.exit(0 if results['summary']['overall_success'] else 1)
        
        elif command in levels_config:
            # Déploiement d'un niveau spécifique
            level_path = levels_config[command]
            result = deployer.deploy_level(command, level_path)
            sys.exit(0 if result['success'] else 1)
        
        else:
            print(f"❌ Commande inconnue: {command}")
            print("Usage: python deploy_exercise_system.py [check|deploy|terminale|premiere|seconde]")
            sys.exit(1)
    
    else:
        # Par défaut: vérification rapide
        print("ℹ️ Aucune commande spécifiée, vérification rapide...")
        success = deployer.quick_check(levels_config)
        
        if not success:
            print("\n💡 Pour corriger les problèmes: python deploy_exercise_system.py deploy")
        
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()