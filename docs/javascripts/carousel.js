document.addEventListener('DOMContentLoaded', function() {
  // Fonction pour initialiser tous les carrousels sur la page
  function initCarousels() {
    const carousels = document.querySelectorAll('.carousel-container');
    
    carousels.forEach(carousel => {
      const track = carousel.querySelector('.carousel-track');
      const cards = carousel.querySelectorAll('.carousel-card');
      const prevButton = carousel.querySelector('.carousel-prev');
      const nextButton = carousel.querySelector('.carousel-next');
      
      let currentIndex = 0;
      let cardWidth = cards[0].offsetWidth + 20; // Largeur + gap
      
      // Fonction pour mettre à jour la position du carrousel
      function updateCarouselPosition() {
        track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
      }
      
      // Gestionnaires d'événements pour les boutons
      prevButton.addEventListener('click', () => {
        if (currentIndex > 0) {
          currentIndex--;
          updateCarouselPosition();
        }
      });
      
      nextButton.addEventListener('click', () => {
        if (currentIndex < cards.length - 3) { // Affiche 3 cartes à la fois
          currentIndex++;
          updateCarouselPosition();
        }
      });
      
      // Réinitialiser en cas de redimensionnement
      window.addEventListener('resize', () => {
        cardWidth = cards[0].offsetWidth + 20;
        updateCarouselPosition();
      });
      
      // Ajout de la gestion du trackpad/swipe
      let touchStartX = 0;
      let isScrolling = false;
      
      carousel.addEventListener('touchstart', function(e) {
          touchStartX = e.touches[0].clientX;
      });
      
      carousel.addEventListener('touchmove', function(e) {
          if (!touchStartX) return;
          
          const touchEndX = e.touches[0].clientX;
          const diffX = touchStartX - touchEndX;
          
          if (Math.abs(diffX) > 30) {
              if (diffX > 0 && currentIndex < cards.length - 3) {
                  currentIndex++;
              } else if (diffX < 0 && currentIndex > 0) {
                  currentIndex--;
              }
              updateCarouselPosition();
              touchStartX = null;
              e.preventDefault();
          }
      });
    });
  }
  
  // Initialiser les carrousels
  initCarousels();
});
