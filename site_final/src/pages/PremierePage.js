import React from 'react';
import { Link } from 'react-router-dom';
import ChapterExerciseSection from '../components/ChapterExerciseSection';
import '../styles/LevelPage.css';

const PremierePage = () => {
  const chapters = [
    {
      id: 'I-Constructions_elementaires',
      title: '🏗️ I - Constructions élémentaires',
      description: 'Variables, fonctions, boucles et conditions',
      courses: [
        { name: 'Cours 1', file: 'Cours_I-Constructions_elementaires_1' },
        { name: 'Cours 2', file: 'Cours_I-Constructions_elementaires_2' },
        { name: 'Cours 3', file: 'Cours_I-Constructions_elementaires_3' },
        { name: 'Cours 4', file: 'Cours_I-Constructions_elementaires_4' },

      ]
    },
    {
      id: 'II-Representation_des_donnees',
      title: '💾 II - Représentation des données',
      description: 'Binaire, hexadécimal, booléens et caractères',
      courses: [
        { name: 'Booléens et opérations', file: 'c_1_booleen_et_operations_II-Representation_des_donnees' },
        { name: 'Entiers binaire hexa', file: 'c_2_entier_binaire_hexa_II-Representation_des_donnees' },
        { name: 'Entiers relatifs', file: 'c_2_entier_relatif_II-Representation_des_donnees' },
        { name: 'Nombres réels', file: 'c_2_nombres_reels_II-Representation_des_donnees' },
        { name: 'Caractères', file: 'c_3_caracteres_II-Representation_des_donnees' },

      ]
    },
    {
      id: 'III-Structures_de_donnees_lineaires',
      title: '📋 III - Structures de données linéaires',
      description: 'Listes, tuples et tableaux',
      courses: [
        { name: 'Cours', file: 'Cours_III-Structures_de_donnees_lineaires' },

      ]
    },
    {
      id: 'IV-Architecture_d_une_machine',
      title: '🖥️ IV - Architecture d\'une machine',
      description: 'Processeur, mémoire et architecture Von Neumann',
      courses: [
        { name: 'Cours 1', file: 'Cours_IV-Architecture_d_une_machine_1' },
        { name: 'Cours 2', file: 'Cours_IV-Architecture_d_une_machine_2' },
        { name: 'Cours 3', file: 'Cours_IV-Architecture_d_une_machine_3' },
        { name: 'Cours 4', file: 'Cours_IV-Architecture_d_une_machine_4' },

      ]
    },
    {
      id: 'V-Dictionnaires_et_Traitement_de_tables',
      title: '📚 V - Dictionnaires et Traitement de tables',
      description: 'Dictionnaires Python et traitement de données',
      courses: [
        { name: 'Cours 1', file: 'Cours_V-Dictionnaires_et_Traitement_de_tables_1' },
        { name: 'Cours 2', file: 'Cours_V-Dictionnaires_et_Traitement_de_tables_2' },
        { name: 'Cours 3', file: 'Cours_V-Dictionnaires_et_Traitement_de_tables_3' },

      ]
    },
    {
      id: 'VI-Internet_et_Reseaux',
      title: '🌐 VI - Internet et Réseaux',
      description: 'Protocoles réseau et communication',
      courses: [
        { name: 'Cours', file: 'Cours_VI-Internet_et_Reseaux' },
        { name: 'Bit alterné', file: 'bit_alterne_VI-Internet_et_Reseaux' }
      ]
    },
    {
      id: 'VII-Algorithmes_sur_les_tableaux',
      title: '🔍 VII - Algorithmes sur les tableaux',
      description: 'Recherche, tri et complexité',
      courses: [
        { name: 'Cours', file: 'Cours_VII-Algorithmes_sur_les_tableaux' },
        { name: 'Dichotomie', file: 'dicho_VII-Algorithmes_sur_les_tableaux' },
        { name: 'Mesures de complexité', file: 'Mesures_de_complexite/readme_VII-Algorithmes_sur_les_tableaux' },
        { name: 'Sujet mesure tris', file: 'Mesures_de_complexite/sujet_mesure_tris_VII-Algorithmes_sur_les_tableaux' }
      ]
    },
    {
      id: 'VIII-Algorithmes_Gloutons',
      title: '🎯 VIII - Algorithmes Gloutons',
      description: 'Stratégies gloutonnes et optimisation',
      courses: [
        { name: 'Algorithmes Gloutons 22-23', file: 'Algorithmes Gloutons_22_23_VIII-Algorithmes_Gloutons' }
      ]
    },
    {
      id: 'VIIII-Systemes_d_exploitation_et_commandes_Linux',
      title: '🐧 VIIII - Systèmes d\'exploitation et commandes Linux',
      description: 'Linux, shell et ligne de commande',
      courses: [
        { name: 'Cours 1', file: 'Cours_VIIII-Systemes_d_exploitation_et_commandes_Linux_1' },
        { name: 'Cours 2', file: 'Cours_VIIII-Systemes_d_exploitation_et_commandes_Linux_2' },
        { name: 'TP Commandes Linux', file: 'TP_Commandes_Linux/TP_commandes_linux_VIIII-Systemes_d_exploitation_et_commandes_Linux' }
      ]
    },
    {
      id: 'X-Web_et_HTTP',
      title: '🌍 X - Web et HTTP',
      description: 'Protocole HTTP, HTML et développement web',
      courses: [
        { name: 'Cours', file: 'Cours_X-Web_et_HTTP' },
        { name: 'Cours HTML', file: 'cours_html_X-Web_et_HTTP' },
        { name: 'Projet', file: 'TP/Projet_X-Web_et_HTTP' },
        { name: 'Galerie d\'art', file: 'TP/galerie_d_art_X-Web_et_HTTP' }
      ]
    },
    {
      id: 'XI-K_plus_proches_voisins',
      title: '🤖 XI - K plus proches voisins',
      description: 'Intelligence artificielle et classification',
      courses: [
        { name: 'Cours', file: 'Cours_XI-K_plus_proches_voisins' },
        { name: 'TP KNN', file: 'TP_KNN_XI-K_plus_proches_voisins' }
      ]
    },
    {
      id: 'XII-Pour_aller_plus_loin',
      title: '🚀 XII - Pour aller plus loin',
      description: 'Programmation orientée objet et structures avancées',
      courses: [
        { name: 'Fiche cours', file: 'fiche_cours_XII-Pour_aller_plus_loin' },
        { name: 'Fiche exercices', file: 'fiche_exercices_XII-Pour_aller_plus_loin' },
        { name: 'TP piles files', file: 'Programmation_Orientee_Objet/TP_piles_files_XII-Pour_aller_plus_loin' },
        { name: 'Fiche piles files', file: 'Programmation_Orientee_Objet/fiche_piles_files_XII-Pour_aller_plus_loin' }
      ]
    },
    {
      id: 'XIII-Projets',
      title: '🎨 XIII - Projets',
      description: 'Projets pratiques et applications',
      courses: [
        { name: 'Index', file: 'index' },
        { name: 'Application bancaire', file: 'Application_bancaire/sujet' },
        { name: 'Gestion Bibliothèque', file: 'Gestion_Bibliotheque_Numerique/sujet' },
        { name: 'Gestion Jeux Vidéo', file: 'Gestion_Jeux_Video/gestion_jeux_video' },
        { name: 'PokeNSI', file: 'PokeNSI/sujet' }
      ]
    },
    {
      id: 'New_Year_Advent',
      title: '🎄 New Year Advent',
      description: 'Défis de programmation de fin d\'année',
      courses: [
        { name: '🎉 New Year Advent', file: 'landing_New_Year_Advent' },
        { name: 'New Year Advent 24-25', file: 'new_year_advent_24_25' },
        { name: 'New Year Advent 25-26', file: 'new_year_advent_25_26' }
      ]
    },
    {
      id: 'Aides',
      title: '📖 Aides',
      description: 'Ressources et aide-mémoires',
      courses: [
        { name: 'Algorithmes à savoir', file: 'Algorithmes_a_savoir/algo_a_savoir' },
        { name: 'Cheat Sheet', file: 'Cheat_Sheets/cheat_sheet' },
        { name: 'Cheat Sheet boucles', file: 'Cheat_Sheets/cheat_sheet_boucles' },
        { name: 'Cheat Sheet fonctions', file: 'Cheat_Sheets/cheat_sheet_fonctions' },
        { name: 'Cheat Sheet if', file: 'Cheat_Sheets/cheat_sheet_if' },
        { name: 'Cheat Sheet listes', file: 'Cheat_Sheets/cheat_sheet_listes' },
        { name: 'Exercices rappels bases', file: 'exercices_rappels_bases' }
      ]
    }
  ];

  return (
    <div className="level-page premiere">
      <div className="level-header premiere">
        <div className="level-header-content">
          <img src="/fox_premiere.png" alt="Première" className="level-logo" />
          <div>
            <h1>Première NSI</h1>
            <p>Numérique et Sciences Informatiques</p>
            <p className="level-description">
              Approfondissement des concepts informatiques et algorithmiques
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
                          to={`/premiere/${chapter.id}/${course.file}`}
                          className="course-link"
                        >
                          {course.name}
                        </Link>
                      ))}
                      {exercises.length > 0 && courses.length > 0 && <hr className="course-separator" />}
                      {exercises.map((course) => (
                        <Link
                          key={course.file}
                          to={`/premiere/${chapter.id}/${course.file}`}
                          className="course-link exercise-link"
                        >
                          {course.name}
                        </Link>
                      ))}
                      <ChapterExerciseSection 
                        level="premiere" 
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

export default PremierePage;