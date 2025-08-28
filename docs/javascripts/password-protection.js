// Système de protection par mot de passe pour les pages NSI
(function() {
    'use strict';
    
    // Configuration des mots de passe pour chaque niveau
    const passwords = {
        'seconde': 'vulpesmacrotis',
        'premiere': 'vulpeszerda', 
        'terminale': 'vulpesvulpes'
    };
    
    // Noms d'affichage pour chaque niveau
    const levelNames = {
        'seconde': 'SNT - Seconde',
        'premiere': 'NSI - Première',
        'terminale': 'NSI - Terminale'
    };
    
    // Fonction pour créer la boîte de dialogue de mot de passe
    function createPasswordDialog(level, originalUrl) {
        // Créer l'overlay
        const overlay = document.createElement('div');
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(5px);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease;
        `;
        
        // Créer la boîte de dialogue
        const dialog = document.createElement('div');
        dialog.style.cssText = `
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 400px;
            width: 90%;
            text-align: center;
            position: relative;
            animation: slideIn 0.3s ease;
        `;
        
        dialog.innerHTML = `
            <div style="margin-bottom: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🔒</div>
                <h2 style="color: #ff6b35; margin: 0 0 0.5rem 0; font-size: 1.5rem;">Accès protégé</h2>
                <p style="color: #666; margin: 0; font-size: 1rem;">${levelNames[level]}</p>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <input type="password" id="passwordInput" placeholder="Entrez le mot de passe" 
                       style="width: 100%; padding: 0.8rem; border: 2px solid #ddd; border-radius: 8px; 
                              font-size: 1rem; text-align: center; box-sizing: border-box;
                              transition: border-color 0.3s ease;" />
            </div>
            
            <div style="display: flex; gap: 1rem; justify-content: center;">
                <button id="cancelBtn" style="padding: 0.8rem 1.5rem; background: #f5f5f5; color: #666; 
                                             border: none; border-radius: 8px; cursor: pointer; 
                                             font-size: 1rem; transition: all 0.3s ease;">Annuler</button>
                <button id="submitBtn" style="padding: 0.8rem 1.5rem; background: #ff6b35; color: white; 
                                             border: none; border-radius: 8px; cursor: pointer; 
                                             font-size: 1rem; transition: all 0.3s ease;">Accéder</button>
            </div>
            
            <div id="errorMessage" style="color: #e74c3c; margin-top: 1rem; font-size: 0.9rem; display: none;">
                Mot de passe incorrect. Veuillez réessayer.
            </div>
        `;
        
        // Ajouter les styles d'animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideIn {
                from { transform: translateY(-20px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            #passwordInput:focus {
                outline: none;
                border-color: #ff6b35 !important;
                box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
            }
            #cancelBtn:hover {
                background: #e0e0e0;
            }
            #submitBtn:hover {
                background: #e55a2b;
                transform: translateY(-1px);
            }
        `;
        document.head.appendChild(style);
        
        overlay.appendChild(dialog);
        document.body.appendChild(overlay);
        
        // Récupérer les éléments
        const passwordInput = dialog.querySelector('#passwordInput');
        const submitBtn = dialog.querySelector('#submitBtn');
        const cancelBtn = dialog.querySelector('#cancelBtn');
        const errorMessage = dialog.querySelector('#errorMessage');
        
        // Focus sur le champ de saisie
        setTimeout(() => passwordInput.focus(), 100);
        
        // Fonction de vérification du mot de passe
        function checkPassword() {
            const enteredPassword = passwordInput.value.trim();
            
            if (enteredPassword === passwords[level]) {
                // Mot de passe correct - rediriger
                overlay.style.animation = 'fadeOut 0.3s ease';
                setTimeout(() => {
                    document.body.removeChild(overlay);
                    window.location.href = originalUrl;
                }, 300);
            } else {
                // Mot de passe incorrect
                errorMessage.style.display = 'block';
                passwordInput.style.borderColor = '#e74c3c';
                passwordInput.value = '';
                
                // Animation de secousse
                dialog.style.animation = 'shake 0.5s ease';
                
                // Ajouter l'animation de secousse
                if (!document.querySelector('#shakeAnimation')) {
                    const shakeStyle = document.createElement('style');
                    shakeStyle.id = 'shakeAnimation';
                    shakeStyle.textContent = `
                        @keyframes shake {
                            0%, 100% { transform: translateX(0); }
                            25% { transform: translateX(-5px); }
                            75% { transform: translateX(5px); }
                        }
                    `;
                    document.head.appendChild(shakeStyle);
                }
                
                setTimeout(() => {
                    passwordInput.focus();
                    passwordInput.style.borderColor = '#ddd';
                    dialog.style.animation = '';
                }, 500);
            }
        }
        
        // Fonction de fermeture
        function closeDialog() {
            overlay.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => {
                if (document.body.contains(overlay)) {
                    document.body.removeChild(overlay);
                }
            }, 300);
        }
        
        // Gestionnaires d'événements
        submitBtn.addEventListener('click', checkPassword);
        cancelBtn.addEventListener('click', closeDialog);
        
        // Validation avec la touche Entrée
        passwordInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                checkPassword();
            }
        });
        
        // Fermeture avec Échap
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeDialog();
            }
        });
        
        // Fermeture en cliquant sur l'overlay
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeDialog();
            }
        });
        
        // Ajouter l'animation de fadeOut
        const fadeOutStyle = document.createElement('style');
        fadeOutStyle.textContent = `
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
        `;
        document.head.appendChild(fadeOutStyle);
    }
    
    // Fonction pour intercepter les clics sur les liens protégés
    function interceptProtectedLinks() {
        // Sélectionner tous les liens vers les pages protégées
        const protectedLinks = document.querySelectorAll('a[href*="seconde/seconde"], a[href*="premiere/premiere"], a[href*="terminale/terminale"]');
        
        protectedLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                const href = this.getAttribute('href');
                let level = '';
                
                // Déterminer le niveau basé sur l'URL
                if (href.includes('seconde/seconde')) {
                    level = 'seconde';
                } else if (href.includes('premiere/premiere')) {
                    level = 'premiere';
                } else if (href.includes('terminale/terminale')) {
                    level = 'terminale';
                }
                
                if (level && passwords[level]) {
                    createPasswordDialog(level, href);
                }
            });
        });
    }
    
    // Initialiser la protection quand le DOM est chargé
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', interceptProtectedLinks);
    } else {
        interceptProtectedLinks();
    }
    
    // Réinitialiser la protection si le contenu change (pour les SPA)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                // Vérifier si de nouveaux liens ont été ajoutés
                const hasNewLinks = Array.from(mutation.addedNodes).some(node => {
                    return node.nodeType === 1 && (
                        node.querySelector && node.querySelector('a[href*="seconde/seconde"], a[href*="premiere/premiere"], a[href*="terminale/terminale"]') ||
                        (node.tagName === 'A' && (node.href.includes('seconde/seconde') || node.href.includes('premiere/premiere') || node.href.includes('terminale/terminale')))
                    );
                });
                
                if (hasNewLinks) {
                    setTimeout(interceptProtectedLinks, 100);
                }
            }
        });
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
})();