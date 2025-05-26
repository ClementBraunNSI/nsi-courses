document.addEventListener('DOMContentLoaded', () => {
    const image1 = document.getElementById('image1');
    const image2 = document.getElementById('image2');

    if (image1) {
        image1.addEventListener('click', () => {
            alert("Tu as cliqué sur l'image 1 !");
        });
    }

    if (image2) {
        image2.addEventListener('click', () => {
            alert("Tu as cliqué sur l'image 2 !");
        });
    }
});

const boutonMode = document.getElementById('bouton-mode');
    const body = document.body;

    if (boutonMode) {
        boutonMode.addEventListener('click', function() {
            // Ajouter ou retirer la classe 'mode-nuit' au body
            body.classList.toggle('mode-nuit');

            // Changer le texte du bouton
            if (body.classList.contains('mode-nuit')) {
                boutonMode.textContent = 'Mode jour';
            } else {
                boutonMode.textContent = 'Mode nuit';
            }
        });
    }

function validerReponses() {
    const question1 = document.querySelector('input[name="question1"]:checked');
    const question2 = document.querySelector('input[name="question2"]:checked');
    const resultat = document.getElementById("resultat");

    if (!question1 || !question2) {
        resultat.textContent = "Veuillez répondre à toutes les questions.";
        resultat.style.color = "red";
        return;
    }

    let score = 0;
    if (question1.value === "correct") score++;
    if (question2.value === "correct") score++;

    if (score === 2) {
        resultat.textContent = "Excellent ! 2/2 !!";
        resultat.style.color = "green";
    } else {
        resultat.textContent = `Vous avez ${score}/2 bonne(s) réponse(s).`;
        resultat.style.color = "orange";
    }
}