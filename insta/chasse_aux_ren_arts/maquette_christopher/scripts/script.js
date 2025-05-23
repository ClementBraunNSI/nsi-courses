const modeToggle = document.getElementById("modeToggle");

modeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    const isDark = document.body.classList.contains("dark-mode");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    modeToggle.textContent = isDark ? "☀️ Mode Jour" : "🌙 Mode Nuit";
});

// Charge la préférence sauvegardée
window.addEventListener("DOMContentLoaded", () => {
    const modeToggle = document.getElementById("modeToggle"); // S'assurer que modeToggle est défini
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
        if(modeToggle) modeToggle.textContent = "☀️ Mode Jour";
    } else {
        document.body.classList.remove("dark-mode"); // S'assurer que le mode clair est appliqué si ce n'est pas sombre
        if(modeToggle) modeToggle.textContent = "🌙 Mode Nuit";
    }
});
document.addEventListener('DOMContentLoaded', function() {
    // 1. Effet de survol sur le tableau
    const tableauImage = document.getElementById('tableau');
    if (tableauImage) {
        const tableauOriginal = 'image/Le_Semeur_par_Van_Gogh.png';
        const tableauRenard = 'image/raw.png';
        
        
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
            const reponse3 = document.querySelector('input[name="question3"]:checked');
            const reponse4 = document.querySelector('input[name="question4"]:checked');
            
            // Vérifier les réponses
            let score = 0;
            let message = '';
            
            if (!reponse1 || !reponse2 || !reponse3 || !reponse4) { // Vérification des 4 réponses
                message = 'Veuillez répondre à toutes les questions.';
            } else {
                if (reponse1.value === 'correct') {
                    score++;
                }
                if (reponse2.value === 'correct') {
                    score++;
                }
                if (reponse3.value === 'correct') {
                    score++;
                }
                if (reponse4.value === 'correct') {
                    score++;
                }
                
                // Messages personnalisés selon le score (pour 4 points)
                if (score === 0) {
                    message = 'Vous avez obtenu 0 point sur 4. Réessayez!';
                } else if (score === 1) {
                    message = 'Vous avez obtenu 1 point sur 4. Peut mieux faire.';
                } else if (score === 2) {
                    message = 'Vous avez obtenu 2 points sur 4. Pas mal!';
                } else if (score === 3) {
                    message = 'Vous avez obtenu 3 points sur 4. Très bien!';
                } else { // score === 4
                    message = "Bravo! Vous avez obtenu 4 points sur 4! Excellent!";
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
    // Le DOMContentLoaded imbriqué a été supprimé.
    // La logique pour 'boutonVerifier' a été enlevée car la soumission du formulaire est déjà gérée.
    // Il est conseillé de s'assurer que le bouton de soumission du quiz dans le HTML est de type 'submit'
    // et de retirer l'attribut 'onclick' s'il existe, pour éviter les conflits.
});
document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('background-music'); // Correction de l'ID
    const playPauseBtn = document.getElementById('playPauseBtn');
    const volumeSlider = document.getElementById('volumeSlider');
    const volumeValue = document.getElementById('volumeValue');

    if (audio && playPauseBtn && volumeSlider && volumeValue) {
        // Gestion du bouton lecture/pause
        playPauseBtn.addEventListener('click', function() {
            if (audio.paused) {
                audio.play();
                playPauseBtn.textContent = '⏸️ Pause';
            } else {
                audio.pause();
                playPauseBtn.textContent = '▶️ Lecture';
            }
        });
        forwardBtn.addEventListener('click', function() {
            audio.currentTime = Math.min(audio.currentTime + 10, audio.duration);
        });
        // Gestion du volume
        volumeSlider.addEventListener('input', function() {
            const volume = this.value / 100;
            audio.volume = volume;
            volumeValue.textContent = this.value + '%';
        });

        // Initialisation du volume
        audio.volume = volumeSlider.value / 100;
    }
});