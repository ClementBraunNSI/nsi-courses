// Main JavaScript for NSI Courses Website

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Handle submenu on mobile devices
    const submenuItems = document.querySelectorAll('.dropdown-submenu');
    
    submenuItems.forEach(item => {
        const link = item.querySelector('a');
        const submenu = item.querySelector('.submenu');
        
        // For touch devices
        link.addEventListener('click', function(e) {
            // Check if this is a touch device or small screen
            if (window.innerWidth <= 768 || 'ontouchstart' in window) {
                if (!submenu.classList.contains('submenu-active')) {
                    e.preventDefault();
                    // Close all other open submenus
                    document.querySelectorAll('.submenu').forEach(menu => {
                        if (menu !== submenu) {
                            menu.classList.remove('submenu-active');
                        }
                    });
                    // Toggle current submenu
                    submenu.classList.toggle('submenu-active');
                }
            }
        });
    });
    
    // Close submenus when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown-submenu')) {
            document.querySelectorAll('.submenu').forEach(menu => {
                menu.classList.remove('submenu-active');
            });
        }
    });
    
    // Add more interactivity as needed
});

// Système d'onglets
document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Désactiver tous les onglets
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Activer l'onglet cliqué
            button.classList.add('active');
            const tabId = button.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });
});