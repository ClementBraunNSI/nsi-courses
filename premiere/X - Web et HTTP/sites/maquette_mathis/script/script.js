document.addEventListener('DOMContentLoaded', function() {
    const tableauImage = document.getElementById('tableau');
    if (tableauImage) {
        const tableauOriginal = 'images/Vertumne de Arcimboldo.jpg';
        const tableauRenard = 'images/Renartumne de Arcimboldo.png';

        tableauImage.addEventListener('mouseover', function() {
            tableauImage.src = tableauOriginal;
        });

        tableauImage.addEventListener('mouseout', function() {
            tableauImage.src = tableauRenard;
        });
    }

    const quizForm = document.getElementById('quiz-form');
    const resultatQuiz = document.getElementById('resultat-quiz');

    if (quizForm && resultatQuiz) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault();

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

                switch (score) {
                    case 0:
                        message = 'Vous avez obtenu 0 point sur 4. Réessayez!';
                        break;
                    case 1:
                        message = 'Vous avez obtenu 1 point sur 4. Continuez encore!';
                        break;
                    case 2:
                        message = 'Vous avez obtenu 2 points sur 4. Vous êtes sur la bonne voie!';
                        break;
                    case 3:
                        message = "Vous avez obtenu 3 points sur 4. Presque! Plus qu'un!";
                        break;
                    case 4:
                        message = "Bravo! Vous avez obtenu 4 points sur 4! Bravo! La lettre est A";
                        break;
                }
            }

            resultatQuiz.textContent = message;
            resultatQuiz.style.display = 'block';
            resultatQuiz.classList.add('resultat-anime');
            setTimeout(() => {
                resultatQuiz.classList.remove('resultat-anime');
            }, 1000);
        });
    }

    const boutonMode = document.getElementById('bouton-mode');
    const boutonValider = document.getElementById('bouton-valider');
    const body = document.body;

    if (boutonMode) {
        boutonMode.addEventListener('click', function () {
            body.classList.toggle('mode-nuit');
            boutonMode.textContent = body.classList.contains('mode-nuit') ? 'Mode jour' : 'Mode nuit';
            if (boutonValider) boutonValider.src = 'images/bouton.png';
        });
    }

    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', () => {
            let imgSrc = null;
            const labelText = input.closest('label')?.textContent.toLowerCase();

            if (!labelText) return;

            if (input.name === "question1" && labelText.includes("astérion")) {
                imgSrc = "images/asterion.jpg";
            } else if (input.name === "question2" && labelText.includes("pâtes")) {
                imgSrc = "images/pates.jpg";
            } else if (input.name === "question3" && labelText.includes("steve")) {
                imgSrc = "images/steve_poisson.jpg";
            } else if (input.name === "question4" && labelText.includes("mastu")) {
                imgSrc = "images/mastu_citrouille.png";
            }

            if (imgSrc) {
                const img = document.createElement("img");
                img.src = imgSrc;
                img.className = "fly-image";

                // Récupérer l'élément label et sa position
                const label = input.closest('label');
                if (label) {
                    const rect = label.getBoundingClientRect();
                    img.style.position = 'absolute';
                    img.style.top = `${rect.top + window.scrollY}px`;
                    img.style.left = `${rect.right + 10 + window.scrollX}px`; // Décalage de 10px à droite
                }

                // Ajouter l'image dans le body
                document.body.appendChild(img);

                // Animation de l'image et suppression après 1 seconde
                setTimeout(() => {
                    img.remove();
                }, 1000);
            }
        });
    });
});

