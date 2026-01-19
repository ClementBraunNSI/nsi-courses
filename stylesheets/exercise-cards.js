// JavaScript pour les fonctionnalités interactives des fiches d'exercices

function toggleSolution(button) {
    const card = button.closest('.exercise-card');
    const solutionWrapper = card.querySelector('.solution-wrapper');
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.classList.contains('show')) {
        solutionWrapper.classList.remove('show');
        button.classList.remove('active');
        button.innerHTML = '<span class="arrow">→</span> Voir la correction';
    } else {
        solutionWrapper.classList.add('show');
        button.classList.add('active');
        button.innerHTML = '<span class="arrow">←</span> Masquer la correction';
    }
}

function showSection(sectionId) {
    // Masquer toutes les sections
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    // Afficher la section sélectionnée
    document.getElementById(sectionId).classList.add('active');
    event.target.classList.add('active');
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    const firstTab = document.querySelector('.section-tab');
    if (firstTab) {
        firstTab.click();
    }
});