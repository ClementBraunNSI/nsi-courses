// Configuration des exercices disponibles
export const exerciseConfig = {
  'boucles': {
    title: 'Exercices sur les Boucles',
    jsonFile: '/exercises/exercices_boucles.json',
    description: 'Exercices pour maîtriser les boucles en Python',
    level: 'premiere',
    chapterId: 'I-Constructions_elementaires',
    chapterTitle: 'Constructions élémentaires'
  },
  'fonctions': {
    title: 'Exercices sur les Fonctions',
    jsonFile: '/exercises/exercices_fonctions.json',
    description: 'Apprenez à créer et utiliser des fonctions en Python',
    level: 'premiere',
    chapterId: 'I-Constructions_elementaires',
    chapterTitle: 'Constructions élémentaires'
  },
  'specification': {
    title: 'Bonnes pratiques de développement',
    jsonFile: '/exercises/exercices_specification.json',
    description: 'Apprenez les bonnes pratiques : en-têtes, documentation et nommage',
    level: 'premiere',
    chapterId: 'I-Constructions_elementaires',
    chapterTitle: 'Constructions élémentaires'
  },
  'types': {
    title: 'Types et représentation des données',
    jsonFile: '/exercises/exercices_types.json',
    description: 'Exercices sur les types de données et leur représentation en Python',
    level: 'premiere',
    chapterId: 'I-Constructions_elementaires',
    chapterTitle: 'Constructions élémentaires'
  },
  'booleens': {
    title: 'Booléens et Comparaisons',
    jsonFile: '/exercises/exercices_booleens.json',
    description: 'Exercices sur les booléens, comparaisons et opérateurs logiques',
    level: 'premiere',
    chapterId: 'II-Representation_des_donnees',
    chapterTitle: 'Représentation des données'
  },
  'binaires': {
    title: 'Nombres en Base 2',
    jsonFile: '/exercises/exercices_binaires.json',
    description: 'Exercices sur les conversions binaires, décimales et hexadécimales',
    level: 'premiere',
    chapterId: 'II-Representation_des_donnees',
    chapterTitle: 'Représentation des données'
  },
  'caracteres': {
    title: 'Encodage des Caractères',
    jsonFile: '/exercises/exercices_caracteres.json',
    description: 'Exercices sur l\'encodage ASCII, UTF-8 et la représentation des caractères',
    level: 'premiere',
    chapterId: 'II-Representation_des_donnees',
    chapterTitle: 'Représentation des données'
  },
  'listes_avancees': {
    title: 'Listes avancées',
    jsonFile: '/exercises/exercices_listes_avancees.json',
    description: 'Exercices avancés sur les matrices et les listes par compréhension',
    level: 'premiere',
    chapterId: 'III-Structures_de_donnees_lineaires',
    chapterTitle: 'Structures de données linéaires'
  },
  'listes_tuples_papier': {
    title: 'Listes et tuples sur papier',
    jsonFile: '/exercises/exercices_listes_tuples_papier.json',
    description: 'Exercices de base sur les listes et tuples à faire sur papier',
    level: 'premiere',
    chapterId: 'III-Structures_de_donnees_lineaires',
    chapterTitle: 'Structures de données linéaires'
  },
  'dictionnaires_intro': {
    title: 'Introduction aux dictionnaires',
    jsonFile: '/exercises/exercices_dictionnaires_intro.json',
    description: 'Exercices d\'introduction aux dictionnaires en Python',
    level: 'premiere',
    chapterId: 'V-Dictionnaires_et_Traitement_de_tables',
    chapterTitle: 'Dictionnaires et Traitement de tables'
  },
  'tuples_listes': {
    title: 'Tuples et Listes',
    jsonFile: '/exercises/exercices_tuples_listes.json',
    description: 'Exercices sur les tuples et listes en Python',
    level: 'premiere',
    chapterId: 'III-Structures_de_donnees_lineaires',
    chapterTitle: 'Structures de données linéaires'
  },
  'dictionnaires_avances': {
    title: 'Dictionnaires avancés',
    jsonFile: '/exercises/exercices_dictionnaires_avances.json',
    description: 'Exercices avancés sur les dictionnaires en Python',
    level: 'premiere',
    chapterId: 'V-Dictionnaires_et_Traitement_de_tables',
    chapterTitle: 'Dictionnaires et Traitement de tables'
  },
  'boucles_seconde': {
    title: 'Boucles - Seconde',
    jsonFile: '/exercises/exercices_boucles_seconde.json',
    description: 'Exercices sur les boucles for et while pour la classe de seconde',
    level: 'seconde',
    chapterId: 'IIII_-_Programmation_Python',
    chapterTitle: 'Programmation Python'
  },
  'conditions_seconde': {
    title: 'Conditions - Seconde',
    jsonFile: '/exercises/exercices_conditions_seconde.json',
    description: 'Exercices sur les structures conditionnelles pour la classe de seconde',
    level: 'seconde',
    chapterId: 'IIII_-_Programmation_Python',
    chapterTitle: 'Programmation Python'
  },
  'python_seconde': {
    title: 'Python - Bases',
    jsonFile: '/exercises/exercices_python_seconde.json',
    description: 'Exercices d\'introduction à Python pour la classe de seconde',
    level: 'seconde',
    chapterId: 'IIII_-_Programmation_Python',
    chapterTitle: 'Programmation Python'
  }
};

// Fonction pour obtenir la liste des exercices disponibles
export const getAvailableExercises = () => {
  return Object.keys(exerciseConfig).map(id => ({
    id,
    ...exerciseConfig[id]
  }));
};

// Fonction pour obtenir la configuration d'un exercice spécifique
export const getExerciseConfig = (exerciseId) => {
  return exerciseConfig[exerciseId] || null;
};

// Fonction pour obtenir les exercices d'un chapitre spécifique
export const getExercisesByChapter = (level, chapterId) => {
  return Object.keys(exerciseConfig)
    .filter(id => {
      const config = exerciseConfig[id];
      return config.level === level && config.chapterId === chapterId;
    })
    .map(id => ({
      id,
      ...exerciseConfig[id]
    }));
};

// Fonction pour vérifier si un chapitre a des exercices
export const hasExercisesForChapter = (level, chapterId) => {
  return getExercisesByChapter(level, chapterId).length > 0;
};