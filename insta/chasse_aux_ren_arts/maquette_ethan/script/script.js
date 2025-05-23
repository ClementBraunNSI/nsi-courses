

document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur le tableau
    const tableauImage = document.getElementById('tableau');
    if (tableauImage) {
        const tableauOriginal = 'images/kanagawa_wave.jpg';
        const tableauRenard = 'images/kanagafox_wave.png';
        
        
        // Quand la souris passe sur l'image
        tableauImage.addEventListener('mouseover', function() {
            tableauImage.src = tableauOriginal;
            
        });
        
        // Quand la souris quitte l'image
        tableauImage.addEventListener('mouseout', function() {
            tableauImage.src = tableauRenard;
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
                    message = 'ta eu 0 point sur 2. mdrr!';
                } else if (score === 1) {
                    message = 'ta obtenu 1 point sur 2. t un naze!';
                } else {
                    message = "bv dep ! ta obtenu 2 points sur 2! La lettre est A";
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
// Bascule entre mode clair et mode sombre
document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('toggle-theme');
    toggleBtn.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
    });
});
