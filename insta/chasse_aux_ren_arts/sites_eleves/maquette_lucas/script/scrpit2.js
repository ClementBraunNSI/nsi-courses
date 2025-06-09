document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur le tableau
    const tableauImage = document.getElementById('tableau');
    if (tableauImage) {
        const tableauOriginal = 'images/bansky_1ere.jpg';
        const tableauRenard = 'images/renard_au_ballon.png';

        // Quand la souris passe sur l'image
        tableauImage.addEventListener('mouseover', function() {
            tableauImage.src = tableauOriginal;
        });

        // Quand la souris quitte l'image
        tableauImage.addEventListener('mouseout', function() {
            tableauImage.src = tableauRenard;
        });
    }

    // Gestion du quiz
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

    // Mode nuit
    const boutonMode = document.getElementById('bouton-mode');
    const body = document.body;

    if (boutonMode) {
        boutonMode.addEventListener('click', () => {
            body.classList.toggle('mode-nuit');

            boutonMode.textContent = body.classList.contains('mode-nuit')
                ? 'Mode jour🦊'
                : 'Mode nuit🛌';
        });
    }

    // Musique
    document.getElementById("bouton-musique").addEventListener("click", function () {
        const audio = document.getElementById("musique-pirates");
        
        if (audio.paused) {
            audio.play();
            this.textContent = "Pause musique";
        } else {
            audio.pause();
            this.textContent = "Lancer la musique";
        }
    });
});