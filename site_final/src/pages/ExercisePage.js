import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ExerciseSheet from '../components/ExerciseSheet';
import { getExerciseConfig, getAvailableExercises } from '../config/exerciseConfig';
import '../styles/ExercisePage.css';

const ExercisePage = () => {
  const { exerciseId } = useParams();
  const navigate = useNavigate();
  const [exerciseData, setExerciseData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Configuration des exercices disponibles
  const availableExercises = getAvailableExercises();
  const currentExerciseConfig = getExerciseConfig(exerciseId);

  useEffect(() => {
    const loadExerciseData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Vérifier si l'exercice existe
        if (!currentExerciseConfig) {
          throw new Error(`Exercice "${exerciseId}" non trouvé`);
        }
        
        // Charger le fichier JSON
        const response = await fetch(currentExerciseConfig.jsonFile);
        if (!response.ok) {
          throw new Error(`Erreur lors du chargement: ${response.status}`);
        }
        
        const data = await response.json();
        setExerciseData(data);
      } catch (err) {
        console.error('Erreur lors du chargement des exercices:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadExerciseData();
  }, [exerciseId, currentExerciseConfig]);



  // Rendu de l'état de chargement
  if (loading) {
    return (
      <div className="exercise-page">
        <div className="exercise-loading">
          <div className="loading-spinner"></div>
          <h2>Chargement des exercices...</h2>
          <p>Veuillez patienter pendant le chargement de la fiche d'exercices.</p>
        </div>
      </div>
    );
  }

  // Rendu de l'état d'erreur
  if (error) {
    return (
      <div className="exercise-page">
        <div className="exercise-error">
          <div className="error-icon">⚠️</div>
          <h2>Erreur de chargement</h2>
          <p>{error}</p>
          <div className="error-actions">
            <button className="btn-retry" onClick={() => window.location.reload()}>
              🔄 Réessayer
            </button>
            <button className="btn-back" onClick={() => navigate(-1)}>
              ← Retour
            </button>
          </div>
          
          <div className="available-exercises">
            <h3>Exercices disponibles :</h3>
            <div className="exercise-list">
              {availableExercises.map((exercise) => (
                <button
                  key={exercise.id}
                  className={`exercise-link ${exercise.id === exerciseId ? 'active' : ''}`}
                  onClick={() => navigate(`/exercises/${exercise.id}`)}
                >
                  <span className="exercise-name">{exercise.title}</span>
                  <span className="exercise-desc">{exercise.description}</span>
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Rendu principal
  return (
    <div className="exercise-page">
      <ExerciseSheet 
        jsonData={exerciseData} 
        title={currentExerciseConfig?.title}
      />
      
      
        
    </div>
  );
};

export default ExercisePage;