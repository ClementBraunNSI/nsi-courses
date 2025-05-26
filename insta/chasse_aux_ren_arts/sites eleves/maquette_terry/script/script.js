document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur le tableau
    

    const imgRenard = document.getElementById("tableau");
    if (imgRenard) {
    imgRenard.addEventListener("mouseover", () => {
        imgRenard.src = 'images/modifie.png';
    });
    imgRenard.addEventListener("mouseout", () => {
        imgRenard.src = 'images/original.jpg';
    });
    }

    // 2. Quiz
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
                if (reponse1.value === 'correct') score++;
                if (reponse2.value === 'correct') score++;
                
                // Message selon le score
                if (score === 0) {
                    message = 'Vous avez obtenu 0 point sur 3. Réessayez!';
                } else if (score === 1) {
                    message = 'Vous avez obtenu 1 point sur 3. Pas mal!';
                } else {
                    message = "Bravo! Vous avez obtenu 3 points sur 3! La lettre est A";
                }
            }
            
            // Affichage
            resultatQuiz.textContent = message;
            resultatQuiz.style.display = 'block';
            resultatQuiz.classList.add('resultat-anime');
            
            setTimeout(function() {
                resultatQuiz.classList.remove('resultat-anime');
            }, 1000);
        });
    }
});
