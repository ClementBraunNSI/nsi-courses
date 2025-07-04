import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/ChapterExerciseButton.css';

const ChapterExerciseButton = ({ exerciseId, chapterTitle, className = '' }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/exercises/${exerciseId}`);
  };

  return (
    <button 
      className={`chapter-exercise-btn ${className}`}
      onClick={handleClick}
      title={`Exercices pour ${chapterTitle}`}
    >
      <span className="exercise-icon">📝</span>
      <span className="exercise-text">Exercices</span>
    </button>
  );
};

export default ChapterExerciseButton;