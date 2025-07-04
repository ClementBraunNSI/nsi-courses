import React from 'react';
import { Link } from 'react-router-dom';
import ChapterExerciseSection from '../components/ChapterExerciseSection';
import '../styles/LevelPage.css';

const SecondePage = () => {
  const chapters = [
    {
      id: 'I_-_Internet',
      title: '🌐 I - Internet',
      description: 'Découverte d\'Internet et des réseaux',
      courses: [
        { name: 'Cours', file: 'Cours' },
        { name: 'Activité', file: 'Activite' },
        { name: 'Activité 2', file: 'Activite_2' },
        { name: 'Binaire/Décimal', file: 'Binaire_Décimal' }
      ]
    },
    {
      id: 'II_-_Web',
      title: '🌍 II - Web',
      description: 'HTML, CSS et création de sites web',
      courses: [
        { name: 'Cours', file: 'Cours', type: 'course' },
        { name: 'Cours HTML', file: 'Cours_html', type: 'course' },
        { name: 'Projet création site', file: 'Projet_creation_site', type: 'practical' },
        { name: 'Monstres', file: 'monstres', type: 'course' }
      ]
    },
    {
      id: 'III_-_Reseaux_sociaux',
      title: '📱 III - Réseaux sociaux',
      description: 'Analyse et modélisation des réseaux sociaux',
      courses: [
        { name: 'Cours', file: 'Cours' },
        { name: 'TP réseau social', file: 'TP_reseau_social' }
      ]
    },
    {
      id: 'IIII_-_Programmation_Python',
      title: '🐍 IIII - Programmation Python',
      description: 'Initiation à la programmation avec Python',
      courses: [

        { name: 'Structures conditionnelles', file: 'structures_conditionnelles' }
      ]
    },
    {
      id: 'V_-_Photographie_Numerique',
      title: '📸 V - Photographie Numérique',
      description: 'Traitement et analyse d\'images numériques',
      courses: [
        { name: 'Photographie Noir et Blanc', file: 'Cours_V_-_Photographie_Numerique_1' },
        { name: 'Photographie Couleur', file: 'Cours_V_-_Photographie_Numerique_2' },
        { name: 'Métadonnées', file: 'Cours_V_-_Photographie_Numerique_3' }
      ]
    },
    {
      id: 'VI_-_Geolocalisation',
      title: '🗺️ VI - Géolocalisation',
      description: 'GPS, cartographie et géolocalisation',
      courses: [
        { name: 'La Géolocalisation', file: 'La Géolocalisation_22_23' }
      ]
    },
    {
      id: 'VII_-_Donnees_Structurees',
      title: '📊 VII - Données Structurées',
      description: 'Organisation et traitement des données',
      courses: [
        { name: 'Activité Blockly', file: 'Activité blockly' }
      ]
    },
    {
      id: 'VIII_-_Objets_Connectes',
      title: '🔗 VIII - Objets Connectés',
      description: 'IoT et programmation d\'objets connectés',
      courses: [
        { name: 'Activité', file: 'activite' },
        { name: 'TP', file: 'tp' }
      ]
    }
  ];

  return (
    <div className="level-page seconde">
      <div className="level-header seconde">
        <div className="level-header-content">
          <img src="/fox_seconde.png" alt="Seconde" className="level-logo" />
          <div>
            <h1>Seconde SNT</h1>
            <p>Sciences Numériques et Technologie</p>
            <p className="level-description">
              Découverte des enjeux du numérique dans notre société moderne
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
                {(() => {
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
                          to={`/seconde/${chapter.id}/${course.file}`}
                          className={`course-link ${course.type === 'practical' ? 'practical-link' : ''}`}
                        >
                          {course.name}
                        </Link>
                      ))}
                      {exercises.length > 0 && courses.length > 0 && <hr className="course-separator" />}
                      {exercises.map((course) => (
                        <Link
                          key={course.file}
                          to={`/seconde/${chapter.id}/${course.file}`}
                          className="course-link exercise-link"
                        >
                          {course.name}
                        </Link>
                      ))}
                      <ChapterExerciseSection 
                        level="seconde" 
                        chapterId={chapter.id} 
                        chapterTitle={chapter.title}
                      />
                    </>
                  );
                })()}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SecondePage;