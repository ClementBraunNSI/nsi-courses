const body = document.body;
const button = document.getElementById("theme");
const savedTheme = localStorage.getItem("theme") || "light";

body.classList.add(savedTheme);

function text_button() {
    if (body.classList.contains("dark")) {
        button.textContent = "Clair ☀️";
    } else {
        button.textContent = "Sombre 🌙";
    }
}

function change_theme() {
    const is_light = body.classList.contains("light");
    body.classList.replace(is_light ? "light" : "dark", is_light ? "dark" : "light");
    localStorage.setItem("theme", is_light ? "dark" : "light");
    text_button();
}

button.addEventListener("click", change_theme);



document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur l'image du tableau
    const tableauImage = document.getElementById('tableau');
    if (tableauImage) {
        const tableauOriginal = 'real.jpg';
        const tableauRenard = 'fox.png';
        
        // Quand la souris passe sur l'image
        tableauImage.addEventListener('mouseover', function() {
            tableauImage.src = tableauRenard;
        });
        
        // Quand la souris quitte l'image
        tableauImage.addEventListener('mouseout', function() {
            tableauImage.src = tableauOriginal;
        });
    }

    // Quiz
    const quizForm = document.getElementById('quiz-form');
    const resultatQuiz = document.getElementById('resultat-quiz');
    
    if (quizForm && resultatQuiz) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Empêche l'envoi du formulaire
            
            const reponse1 = document.querySelector('input[name="question1"]:checked');
            const reponse2 = document.querySelector('input[name="question2"]:checked');
            const reponse3 = document.querySelector('input[name="question3"]:checked');
            const reponse4 = document.querySelector('input[name="question4"]:checked');

       
            let score = 0;
            let message = '';

            if (!reponse1 || !reponse2 || !reponse3 || !reponse4) {
                message = 'Veuillez répondre à toutes les questions.';
            } else {
                if (reponse1.value === 'correct') score++;
                if (reponse2.value === 'correct') score++;
                if (reponse3.value === 'correct') score++;
                if (reponse4.value === 'correct') score++;

    
                if (score === 0) message = 'Vous avez obtenu 0 point sur 4. Réessayez!';
                else if (score === 1) message = 'Vous avez obtenu 1 point sur 4. Pas mal!';
                else if (score === 2) message = 'Vous avez obtenu 2 points sur 4. Bien joué!';
                else if (score === 3) message = 'Vous avez obtenu 3 points sur 4. Très bien!';
                else message = 'Bravo! Vous avez obtenu 4 points sur 4!';
            }


    	    resultatQuiz.textContent = message;
            resultatQuiz.style.display = 'block'; // Afficher le résultat

     
            setTimeout(function() {
            resultatQuiz.classList.add('resultat-anime');
      	    }, 100); // L'animation démarre après 100ms pour une transition fluide

     
      	    setTimeout(function() {
            resultatQuiz.classList.remove('resultat-anime');
            }, 1500); // L'animation dure 1.5s
        });
    }
});  


