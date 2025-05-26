

document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur le tableau IA
    const imageIA = document.getElementById('image_ia');
    if (imageIA) {
        const originalSrc = imageIA.src; // Sauvegarde la source originale
        const hoverSrc = 'images/ia_texte.png'; // Chemin vers l'image de survol

        // Quand la souris passe sur l'image
        imageIA.addEventListener('mouseover', function() {
            imageIA.src = hoverSrc;
        });

        // Quand la souris quitte l'image
        imageIA.addEventListener('mouseout', function() {
            imageIA.src = originalSrc; // Rétablit l'image originale
        });
    }

    const quizForm = document.getElementById('quiz-form');
    const resultatQuiz = document.getElementById('resultat-quiz');
    
    if (quizForm && resultatQuiz) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Empêche l'envoi du formulaire
            
            // Récupérer les réponses
            const reponse1 = document.querySelector('input[name="question1"]:checked');
            const reponse2 = document.querySelector('input[name="question2"]:checked');
            
            // Vérifier les réponses
            let score = 0;
            let message = '';
            
            if (!reponse1 || !reponse2) {
                message = 'Veuillez répondre à toutes les questions.';
            } else {
                if (reponse1.value === 'correct') {
                    score++;
                }
                if (reponse2.value === 'correct') {
                    score++;
                }
                
                // Messages personnalisés selon le score
                if (score === 0) {
                    message = 'Vous avez obtenu 0 point sur 2. Réessayez!';
                } else if (score === 1) {
                    message = 'Vous avez obtenu 1 point sur 2. Pas mal!';
                } else {
                    message = "Bravo! Vous avez obtenu 2 points sur 2! La lettre est A";
                }
            }
            
            // Afficher le résultat
            resultatQuiz.textContent = message;
            resultatQuiz.style.display = 'block';
            
            // Ajouter une classe pour l'animation
            resultatQuiz.classList.add('resultat-anime');
            
            // Retirer la classe après l'animation
            setTimeout(function() {
                resultatQuiz.classList.remove('resultat-anime');
            }, 1000);
        });
    }
});

