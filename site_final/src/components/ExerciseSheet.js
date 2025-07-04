import React, { useState, useEffect } from 'react';
import '../styles/ExerciseSheet.css';

const ExerciseSheet = ({ jsonData, title = "Fiche d'exercices" }) => {
  const [activeSection, setActiveSection] = useState('facile');
  const [expandedSolutions, setExpandedSolutions] = useState(new Set());

  // Fonction pour basculer l'affichage d'une solution
  const toggleSolution = (exerciseId) => {
    const newExpanded = new Set(expandedSolutions);
    if (newExpanded.has(exerciseId)) {
      newExpanded.delete(exerciseId);
    } else {
      newExpanded.add(exerciseId);
    }
    setExpandedSolutions(newExpanded);
  };

  // Fonction pour formater le code avec coloration syntaxique Solarized Light
  const formatCode = (code) => {
    if (!code) return '';
    
    // Échapper d'abord les caractères HTML dangereux
    let formattedCode = code
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    
    // Appliquer la coloration syntaxique avec les caractères échappés
    // D'abord les commentaires pour éviter qu'ils interfèrent avec les autres règles
    formattedCode = formattedCode.replace(/(#.*$)/gm, '<span class="comment">$1</span>');
    
    // Ensuite les chaînes de caractères (avec guillemets échappés)
    formattedCode = formattedCode.replace(/("[^"]*"|'[^']*')/g, '<span class="string">$1</span>');
    
    // Puis les mots-clés Python (bleu solarized)
    formattedCode = formattedCode.replace(/\b(def|if|else|elif|for|while|return|import|from|class|try|except|with|as|and|or|not|in|is|True|False|None)\b/g, '<span class="keyword">$1</span>');
    
    // Fonctions built-in (magenta solarized)
    formattedCode = formattedCode.replace(/\b(print|input|len|range|int|float|str|list|dict|set|tuple|type|isinstance|random|randint)\b/g, '<span class="builtin">$1</span>');
    
    // Nombres (cyan solarized)
    formattedCode = formattedCode.replace(/\b(\d+(?:\.\d+)?)\b/g, '<span class="number">$1</span>');
    
    // Remplacer les retours à la ligne par des <br>
    formattedCode = formattedCode.replace(/\n/g, '<br>');
    
    return formattedCode;
  };

  // Fonction pour échapper le HTML
  const escapeHtml = (text) => {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  };

  // Configuration des icônes et couleurs par difficulté
  const difficultyConfig = {
    facile: {
      icon: '🦊',
      color: '#28a745',
      label: 'Facile'
    },
    moyen: {
      icon: '🦊🦊',
      color: '#ffc107',
      label: 'Moyen'
    },
    difficile: {
      icon: '🦊🦊🦊',
      color: '#dc3545',
      label: 'Difficile'
    }
  };

  // Rendu d'une carte d'exercice
  const renderExerciseCard = (exercise, index, difficulty) => {
    const exerciseId = `${difficulty}-${index}`;
    const isExpanded = expandedSolutions.has(exerciseId);
    const config = difficultyConfig[difficulty];

    return (
      <div key={exerciseId} className={`exercise-card ${difficulty}`}>
        <div className="exercise-content-wrapper">
          <div className="difficulty-badge" style={{ backgroundColor: config.color }}>
            {config.icon} {config.label}
          </div>
          
          <h3 className="exercise-title">{exercise.title}</h3>
          
          <div className="exercise-content">
            <div className="exercise-statement">
              <h4>📝 Énoncé :</h4>
              <p>{exercise.enonce}</p>
            </div>
            
            {exercise.example && (
              <div className="exercise-example">
                <h4>💡 Exemple :</h4>
                <pre><code>{exercise.example}</code></pre>
              </div>
            )}
          </div>
          
          <button 
            className={`toggle-solution ${isExpanded ? 'active' : ''}`}
            onClick={() => toggleSolution(exerciseId)}
          >
            <span className="arrow">{isExpanded ? '↓' : '→'}</span>
            {isExpanded ? 'Masquer la correction' : 'Voir la correction'}
          </button>
        </div>
        
        <div className={`solution-wrapper ${isExpanded ? 'show' : ''}`}>
          <div className="solution">
            <h4>✅ Correction :</h4>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: formatCode(exercise.solution) }}></div>
          </div>
        </div>
      </div>
    );
  };

  // Rendu des onglets de section
  const renderSectionTabs = () => {
    return (
      <div className="section-tabs">
        {Object.keys(difficultyConfig).map(difficulty => {
          const config = difficultyConfig[difficulty];
          const exerciseCount = jsonData[difficulty]?.length || 0;
          
          if (exerciseCount === 0) return null;
          
          return (
            <button
              key={difficulty}
              className={`section-tab ${activeSection === difficulty ? 'active' : ''}`}
              onClick={() => setActiveSection(difficulty)}
              style={{
                borderColor: activeSection === difficulty ? config.color : 'transparent'
              }}
            >
              {config.icon} {config.label} ({exerciseCount})
            </button>
          );
        })}
      </div>
    );
  };

  // Rendu du contenu d'une section
  const renderSectionContent = () => {
    const exercises = jsonData[activeSection] || [];
    
    if (exercises.length === 0) {
      return (
        <div className="no-exercises">
          <p>Aucun exercice disponible pour ce niveau de difficulté.</p>
        </div>
      );
    }

    return (
      <div className="exercise-cards">
        {exercises.map((exercise, index) => 
          renderExerciseCard(exercise, index, activeSection)
        )}
      </div>
    );
  };

  if (!jsonData) {
    return (
      <div className="exercise-sheet-loading">
        <div className="loading-spinner"></div>
        <p>Chargement des exercices...</p>
      </div>
    );
  }

  return (
    <div className="exercise-sheet">
      <div className="exercise-sheet-header">
        <h1>{title}</h1>
        <p className="exercise-description">
          Sélectionnez un niveau de difficulté pour commencer les exercices.
        </p>
      </div>
      
      {renderSectionTabs()}
      
      <div className="section-content active">
        {renderSectionContent()}
      </div>
    </div>
  );
};

export default ExerciseSheet;