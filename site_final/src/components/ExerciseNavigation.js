import React from 'react';
import { useNavigate } from 'react-router-dom';
import { getAvailableExercises } from '../config/exerciseConfig';
import '../styles/ExerciseNavigation.css';

const ExerciseNavigation = ({ showTitle = true, compact = false }) => {
  const navigate = useNavigate();
  const availableExercises = getAvailableExercises();

  const handleExerciseClick = (exerciseId) => {
    navigate(`/exercises/${exerciseId}`);
  };

  if (compact) {
    return (
      <div className="exercise-navigation-compact">
        <h3>🏋️ Exercices pratiques</h3>
        <div className="exercise-grid-compact">
          {availableExercises.map((exercise) => (
            <button
              key={exercise.id}
              className="exercise-card-compact"
              onClick={() => handleExerciseClick(exercise.id)}
              title={exercise.description}
            >
              <span className="exercise-icon">📝</span>
              <span className="exercise-name">{exercise.title.replace('Exercices sur les ', '')}</span>
            </button>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="exercise-navigation">
      {showTitle && (
        <div className="exercise-nav-header">
          <h2>🏋️ Exercices pratiques</h2>
          <p>Mettez en pratique vos connaissances avec nos exercices interactifs</p>
        </div>
      )}
      
      <div className="exercise-grid">
        {availableExercises.map((exercise) => (
          <div key={exercise.id} className="exercise-card">
            <div className="exercise-card-header">
              <span className="exercise-icon">📝</span>
              <h3>{exercise.title}</h3>
            </div>
            
            <p className="exercise-description">{exercise.description}</p>
            
            <button 
              className="exercise-button"
              onClick={() => handleExerciseClick(exercise.id)}
            >
              Commencer les exercices →
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ExerciseNavigation;