#!/usr/bin/env node

/**
 * Script utilitaire pour ajouter un nouvel exercice au système
 * Usage: node scripts/add-exercise.js <exercise-id> <title> <description> [level] [chapter-id] [chapter-title]
 */

const fs = require('fs');
const path = require('path');

// Configuration des chemins
const EXERCISES_DIR = path.join(__dirname, '..', 'public', 'exercises');
const CONFIG_FILE = path.join(__dirname, '..', 'src', 'config', 'exerciseConfig.js');

// Template pour un nouveau fichier JSON d'exercice
const EXERCISE_TEMPLATE = {
  "facile": [
    {
      "nom": "Premier exercice facile",
      "enonce": "Écrivez un programme qui affiche 'Hello World'.",
      "exemple": "Exemple :\n>>> print('Hello World')\nHello World",
      "correction": "print('Hello World')"
    }
  ],
  "moyen": [
    {
      "nom": "Premier exercice moyen",
      "enonce": "Créez une fonction qui calcule la somme de deux nombres.",
      "exemple": "Exemple :\n>>> somme(3, 5)\n8",
      "correction": "def somme(a, b):\n    return a + b"
    }
  ],
  "difficile": [
    {
      "nom": "Premier exercice difficile",
      "enonce": "Implémentez un algorithme de tri par sélection.",
      "exemple": "Exemple :\n>>> tri_selection([3, 1, 4, 1, 5])\n[1, 1, 3, 4, 5]",
      "correction": "def tri_selection(liste):\n    for i in range(len(liste)):\n        min_idx = i\n        for j in range(i+1, len(liste)):\n            if liste[j] < liste[min_idx]:\n                min_idx = j\n        liste[i], liste[min_idx] = liste[min_idx], liste[i]\n    return liste"
    }
  ]
};

function validateArgs() {
  const args = process.argv.slice(2);
  
  if (args.length < 3) {
    console.error('❌ Usage: node scripts/add-exercise.js <exercise-id> <title> <description> [level] [chapter-id] [chapter-title]');
    console.error('   Exemple: node scripts/add-exercise.js "fonctions" "Exercices sur les Fonctions" "Apprenez à créer et utiliser des fonctions" "premiere" "I-Constructions_elementaires" "Constructions élémentaires"');
    process.exit(1);
  }
  
  return {
    id: args[0],
    title: args[1],
    description: args[2],
    level: args[3] || null,
    chapterId: args[4] || null,
    chapterTitle: args[5] || null
  };
}

function createExerciseFile(exerciseId) {
  const filename = `exercices_${exerciseId}.json`;
  const filepath = path.join(EXERCISES_DIR, filename);
  
  if (fs.existsSync(filepath)) {
    console.warn(`⚠️  Le fichier ${filename} existe déjà.`);
    return false;
  }
  
  try {
    // Créer le dossier exercises s'il n'existe pas
    if (!fs.existsSync(EXERCISES_DIR)) {
      fs.mkdirSync(EXERCISES_DIR, { recursive: true });
    }
    
    fs.writeFileSync(filepath, JSON.stringify(EXERCISE_TEMPLATE, null, 2));
    console.log(`✅ Fichier créé: ${filename}`);
    return true;
  } catch (error) {
    console.error(`❌ Erreur lors de la création du fichier: ${error.message}`);
    return false;
  }
}

function updateConfig(exerciseId, title, description, level, chapterId, chapterTitle) {
  try {
    let configContent = fs.readFileSync(CONFIG_FILE, 'utf8');
    
    // Trouver la fin de l'objet exerciseConfig
    const configEndRegex = /}\s*;\s*$/m;
    const match = configContent.match(configEndRegex);
    
    if (!match) {
      console.error('❌ Impossible de trouver la fin de la configuration');
      return false;
    }
    
    // Vérifier si l'exercice existe déjà
    if (configContent.includes(`'${exerciseId}':`)) {
      console.warn(`⚠️  L'exercice '${exerciseId}' existe déjà dans la configuration.`);
      return false;
    }
    
    // Construire la nouvelle entrée avec les informations optionnelles
    let newEntry = `,\n  '${exerciseId}': {\n    title: '${title}',\n    jsonFile: '/exercises/exercices_${exerciseId}.json',\n    description: '${description}'`;
    
    if (level) {
      newEntry += `,\n    level: '${level}'`;
    }
    
    if (chapterId) {
      newEntry += `,\n    chapterId: '${chapterId}'`;
    }
    
    if (chapterTitle) {
      newEntry += `,\n    chapterTitle: '${chapterTitle}'`;
    }
    
    newEntry += '\n  }';
    
    // Insérer avant la fermeture de l'objet
    const insertPosition = match.index;
    const newContent = configContent.slice(0, insertPosition) + newEntry + '\n' + configContent.slice(insertPosition);
    
    fs.writeFileSync(CONFIG_FILE, newContent);
    console.log(`✅ Configuration mise à jour pour '${exerciseId}'`);
    return true;
  } catch (error) {
    console.error(`❌ Erreur lors de la mise à jour de la configuration: ${error.message}`);
    return false;
  }
}

function main() {
  console.log('🚀 Ajout d\'un nouvel exercice...');
  
  const { id, title, description, level, chapterId, chapterTitle } = validateArgs();
  
  console.log(`📝 ID: ${id}`);
  console.log(`📚 Titre: ${title}`);
  console.log(`📖 Description: ${description}`);
  if (level) console.log(`🎓 Niveau: ${level}`);
  if (chapterId) console.log(`📂 Chapitre ID: ${chapterId}`);
  if (chapterTitle) console.log(`📋 Chapitre: ${chapterTitle}`);
  console.log('');
  
  // Créer le fichier JSON
  const fileCreated = createExerciseFile(id);
  
  // Mettre à jour la configuration
  const configUpdated = updateConfig(id, title, description, level, chapterId, chapterTitle);
  
  if (fileCreated && configUpdated) {
    console.log('');
    console.log('🎉 Exercice ajouté avec succès!');
    console.log(`🌐 Accessible via: /exercises/${id}`);
    console.log(`📁 Fichier: public/exercises/exercices_${id}.json`);
    console.log('');
    console.log('📝 Prochaines étapes:');
    console.log(`   1. Éditez le fichier exercices_${id}.json pour ajouter vos exercices`);
    console.log('   2. Redémarrez le serveur de développement si nécessaire');
    console.log(`   3. Testez l'exercice sur http://localhost:3000/exercises/${id}`);
  } else {
    console.log('');
    console.log('❌ Échec de l\'ajout de l\'exercice');
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { createExerciseFile, updateConfig };