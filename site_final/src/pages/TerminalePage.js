import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/LevelPage.css';

const TerminalePage = () => {
  const chapters = [
    {
      id: 'I-Rappels',
      title: '🔄 I - Rappels',
      description: 'Révision des concepts fondamentaux',
      courses: [
        { name: 'Variables et types', file: 'Cours/variables_et_types' },
        { name: 'Fonctions', file: 'Cours/fonctions' },
        { name: 'Listes et tableaux', file: 'Cours/listes_tableaux' },
        { name: 'Structures conditionnelles et boucles', file: 'Cours/structures_conditionnelles_boucles' },
        { name: 'Fiche exercices rappels', file: 'Exercices/fiche_exercices_rappels' }
      ]
    },
    {
      id: 'II-Structures_de_donnees',
      title: '🌳 II - Structures de données',
      description: 'Arbres, graphes, piles et files',
      courses: [
        { name: 'Listes, piles et files', file: 'Cours/listes_piles_files' },
        { name: 'Arbres', file: 'Cours/arbres' },
        { name: 'Graphes', file: 'Cours/graphes' },
        { name: 'Exercices listes piles files', file: 'Exercices/fiche_exercices_listes_piles_files' },
        { name: 'Exercices arbres', file: 'Exercices/fiche_exercices_arbres' },
        { name: 'Exercices graphes', file: 'Exercices/fiche_exercices_graphes' }
      ]
    },
    {
      id: 'III-Bases_de_donnees',
      title: '🗄️ III - Bases de données',
      description: 'Modèle relationnel, SQL et SGBD',
      courses: [
        { name: 'Modèle relationnel', file: 'Cours/modele_relationnel' },
        { name: 'Langage SQL', file: 'Cours/langage_sql' },
        { name: 'SGBD', file: 'Cours/sgbd' },
        { name: 'Exercices SQL', file: 'Exercices/fiche_exercices_sql' }
      ]
    },
    {
      id: 'IV-Architectures_et_reseaux',
      title: '🏗️ IV - Architectures et réseaux',
      description: 'Architecture matérielle et réseaux informatiques',
      courses: [
        { name: 'Architectures matérielles', file: 'Cours/architectures_materielles' },
        { name: 'Réseaux', file: 'Cours/reseaux' }
      ]
    },
    {
      id: 'V-Langages_et_programmation',
      title: '💻 V - Langages et programmation',
      description: 'Paradigmes de programmation et langages',
      courses: [
        { name: 'Paradigmes programmation', file: 'Cours/paradigmes_programmation' }
      ]
    },
    {
      id: 'VI-Algorithmique',
      title: '🧮 VI - Algorithmique',
      description: 'Algorithmes avancés et complexité',
      courses: [
        // Cours et exercices seront ajoutés selon le contenu disponible
      ]
    },
    {
      id: 'VII-Projets',
      title: '🎯 VII - Projets',
      description: 'Projets de fin d\'études',
      courses: [
        // Projets seront ajoutés selon le contenu disponible
      ]
    },
    {
      id: 'VIII-Preparation_bac',
      title: '🎓 VIII - Préparation BAC',
      description: 'Préparation aux épreuves du baccalauréat',
      courses: [
        // Contenus de préparation seront ajoutés selon le contenu disponible
      ]
    }
  ];

  return (
    <div className="level-page">
      <div className="level-header terminale">
        <div className="level-header-content">
          <img src="/fox_terminale.png" alt="Terminale" className="level-logo" />
          <div>
            <h1>Terminale NSI</h1>
            <p>Numérique et Sciences Informatiques</p>
            <p className="level-description">
              Approfondissement et spécialisation pour la préparation au baccalauréat
            </p>
          </div>
        </div>
      </div>

      <div className="chapters-container">
        <div className="chapters-grid">
          {chapters.map((chapter) => (
            <div key={chapter.id} className="chapter-card">
              <h3>{chapter.title}</h3>
              <p className="chapter-description">{chapter.description}</p>
              <div className="chapter-courses">
                {chapter.courses.length > 0 ? (
                  (() => {
                    const courses = chapter.courses.filter(course => 
                      !course.name.toLowerCase().includes('exercice') && 
                      !course.name.toLowerCase().includes('fiche') && 
                      !course.name.toLowerCase().includes('tp')
                    );
                    const exercises = chapter.courses.filter(course => 
                      course.name.toLowerCase().includes('exercice') || 
                      course.name.toLowerCase().includes('fiche') || 
                      course.name.toLowerCase().includes('tp')
                    );
                    
                    return (
                      <>
                        {courses.map((course) => (
                          <Link
                            key={course.file}
                            to={`/terminale/${chapter.id}/${course.file}`}
                            className="course-link"
                          >
                            {course.name}
                          </Link>
                        ))}
                        {exercises.length > 0 && courses.length > 0 && <hr className="course-separator" />}
                        {exercises.map((course) => (
                          <Link
                            key={course.file}
                            to={`/terminale/${chapter.id}/${course.file}`}
                            className="course-link exercise-link"
                          >
                            {course.name}
                          </Link>
                        ))}
                      </>
                    );
                  })()
                ) : (
                  <span className="no-courses">Contenu en cours de développement</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TerminalePage;