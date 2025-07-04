import React from 'react';
import { useNavigate } from 'react-router-dom';
import { getExercisesByChapter } from '../config/exerciseConfig';
import '../styles/ChapterExerciseSection.css';

const ChapterExerciseSection = ({ level, chapterId, chapterTitle }) => {
  const navigate = useNavigate();
  const exercises = getExercisesByChapter(level, chapterId);

  if (exercises.length === 0) {
    return null;
  }

  const handleExerciseClick = (exerciseId) => {
    navigate(`/exercises/${exerciseId}`);
  };

  return (
    <div className="chapter-exercise-section">
      <div className="exercise-section-header">
        <span className="exercise-icon">📝</span>
        <h4>Exercices disponibles</h4>
      </div>
      <div className="exercise-buttons-grid">
        {exercises.map((exercise) => (
          <button
            key={exercise.id}
            className="exercise-button"
            onClick={() => handleExerciseClick(exercise.id)}
            title={exercise.description}
          >
            <span className="exercise-button-title">{exercise.title}</span>
            <span className="exercise-button-description">{exercise.description}</span>
          </button>
        ))}
      </div>
    </div>
  );
};

export default ChapterExerciseSection;