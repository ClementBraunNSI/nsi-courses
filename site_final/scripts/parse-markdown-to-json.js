#!/usr/bin/env node

/**
 * Script pour parser une fiche d'exercice markdown en JSON
 * Usage: node scripts/parse-markdown-to-json.js <fichier-markdown> [fichier-sortie]
 */

const fs = require('fs');
const path = require('path');

function parseMarkdownToJSON(markdownContent) {
  const lines = markdownContent.split('\n');
  const result = {};
  
  let currentLevel = null;
  let currentChapter = null;
  let currentDifficulty = null;
  let currentExercise = null;
  let currentSection = null;
  let content = [];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    // Ignorer les lignes vides
    if (!line) {
      if (content.length > 0) {
        content.push('');
      }
      continue;
    }
    
    // Détecter les niveaux de titre
    if (line.startsWith('#')) {
      // Sauvegarder le contenu précédent
      saveCurrentContent();
      
      const level = (line.match(/^#+/) || [''])[0].length;
      const title = line.replace(/^#+\s*/, '').trim();
      
      if (level === 1) {
        // Niveau (ex: # Première)
        currentLevel = normalizeKey(title);
        currentChapter = null;
        currentDifficulty = null;
        currentExercise = null;
        
        if (!result[currentLevel]) {
          result[currentLevel] = {};
        }
      } else if (level === 2) {
        // Chapitre (ex: ## Constructions élémentaires)
        currentChapter = normalizeKey(title);
        currentDifficulty = null;
        currentExercise = null;
        
        if (currentLevel && !result[currentLevel][currentChapter]) {
          result[currentLevel][currentChapter] = {};
        }
      } else if (level === 3) {
        // Difficulté (ex: ### Facile)
        const difficultyMap = {
          'facile': 'facile',
          'easy': 'facile',
          'moyen': 'moyen',
          'medium': 'moyen',
          'difficile': 'difficile',
          'hard': 'difficile',
          'avancé': 'difficile',
          'avance': 'difficile'
        };
        
        currentDifficulty = difficultyMap[normalizeKey(title)] || 'moyen';
        currentExercise = null;
        
        if (currentLevel && currentChapter && !result[currentLevel][currentChapter][currentDifficulty]) {
          result[currentLevel][currentChapter][currentDifficulty] = [];
        }
      } else if (level === 4) {
        // Nom d'exercice (ex: #### Exercice 1: Variables)
        if (currentLevel && currentChapter && currentDifficulty) {
          currentExercise = {
            nom: title,
            enonce: '',
            exemple: '',
            correction: ''
          };
          result[currentLevel][currentChapter][currentDifficulty].push(currentExercise);
        }
      } else if (level === 5) {
        // Section d'exercice (ex: ##### Énoncé)
        const sectionMap = {
          'énoncé': 'enonce',
          'enonce': 'enonce',
          'énoncé:': 'enonce',
          'enonce:': 'enonce',
          'exemple': 'exemple',
          'exemple:': 'exemple',
          'exemples': 'exemple',
          'exemples:': 'exemple',
          'exemple d\'utilisation': 'exemple',
          'exemple d\'utilisation:': 'exemple',
          'correction': 'correction',
          'correction:': 'correction',
          'solution': 'correction',
          'solution:': 'correction'
        };
        
        currentSection = sectionMap[normalizeKey(title)] || null;
        content = [];
      }
    } else {
      // Contenu normal
      content.push(line);
    }
  }
  
  // Sauvegarder le dernier contenu
  saveCurrentContent();
  
  function saveCurrentContent() {
    if (currentExercise && currentSection && content.length > 0) {
      const contentText = content.join('\n').trim();
      if (contentText) {
        currentExercise[currentSection] = contentText;
      }
    }
    content = [];
  }
  
  function normalizeKey(str) {
    return str.toLowerCase()
      .replace(/[àáâãäå]/g, 'a')
      .replace(/[èéêë]/g, 'e')
      .replace(/[ìíîï]/g, 'i')
      .replace(/[òóôõö]/g, 'o')
      .replace(/[ùúûü]/g, 'u')
      .replace(/[ç]/g, 'c')
      .replace(/[^a-z0-9]/g, '_')
      .replace(/_+/g, '_')
      .replace(/^_|_$/g, '');
  }
  
  return result;
}

function validateArgs() {
  const args = process.argv.slice(2);
  
  if (args.length < 1) {
    console.error('❌ Usage: node scripts/parse-markdown-to-json.js <fichier-markdown> [fichier-sortie]');
    console.error('   Exemple: node scripts/parse-markdown-to-json.js fiche_exercices.md exercices_parsed.json');
    process.exit(1);
  }
  
  const inputFile = args[0];
  const outputFile = args[1] || path.join('/Users/clementbraun/nsi-courses/site_final/fiches_parsees_json', path.basename(inputFile).replace(/\.(md|markdown)$/i, '.json'));
  
  if (!fs.existsSync(inputFile)) {
    console.error(`❌ Le fichier ${inputFile} n'existe pas.`);
    process.exit(1);
  }
  
  return { inputFile, outputFile };
}

function main() {
  console.log('🚀 Parsing du fichier markdown vers JSON...');
  
  const { inputFile, outputFile } = validateArgs();
  
  try {
    // Créer le dossier de sortie s'il n'existe pas
    const outputDir = path.dirname(outputFile);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    
    // Lire le fichier markdown
    const markdownContent = fs.readFileSync(inputFile, 'utf8');
    console.log(`📖 Lecture du fichier: ${inputFile}`);
    
    // Parser le contenu
    const jsonResult = parseMarkdownToJSON(markdownContent);
    
    // Écrire le résultat JSON
    fs.writeFileSync(outputFile, JSON.stringify(jsonResult, null, 2));
    console.log(`✅ Fichier JSON créé: ${outputFile}`);
    
    // Afficher un résumé
    console.log('\n📊 Résumé du parsing:');
    Object.keys(jsonResult).forEach(level => {
      console.log(`   📚 Niveau: ${level}`);
      Object.keys(jsonResult[level]).forEach(chapter => {
        console.log(`      📂 Chapitre: ${chapter}`);
        Object.keys(jsonResult[level][chapter]).forEach(difficulty => {
          const exerciseCount = jsonResult[level][chapter][difficulty].length;
          console.log(`         🎯 ${difficulty}: ${exerciseCount} exercice(s)`);
        });
      });
    });
    
    console.log('\n🎉 Parsing terminé avec succès!');
    
  } catch (error) {
    console.error(`❌ Erreur lors du parsing: ${error.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { parseMarkdownToJSON };