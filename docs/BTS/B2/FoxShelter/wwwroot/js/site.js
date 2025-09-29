// JavaScript personnalisé pour FoxShelter

// Initialisation au chargement de la page
$(document).ready(function() {
    // Initialiser les tooltips Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialiser les popovers Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Animation d'apparition pour les cartes
    $('.card').addClass('fade-in');

    // Gestion des alertes auto-dismiss
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);

    // Confirmation pour les actions de suppression
    $('.btn-delete').on('click', function(e) {
        if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ?')) {
            e.preventDefault();
        }
    });

    // Validation côté client pour les formulaires
    $('form').on('submit', function(e) {
        var isValid = true;
        
        // Vérifier les champs requis
        $(this).find('[required]').each(function() {
            if ($(this).val() === '') {
                $(this).addClass('is-invalid');
                isValid = false;
            } else {
                $(this).removeClass('is-invalid');
            }
        });

        if (!isValid) {
            e.preventDefault();
            showAlert('Veuillez remplir tous les champs obligatoires.', 'warning');
        }
    });

    // Recherche en temps réel
    $('#searchInput').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        $('.searchable').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    // Filtrage par état de santé
    $('#filtreEtatSante').on('change', function() {
        var selectedState = $(this).val();
        if (selectedState === '') {
            $('.renard-card').show();
        } else {
            $('.renard-card').hide();
            $('.renard-card[data-etat="' + selectedState + '"]').show();
        }
    });

    // Compteur de caractères pour les textarea
    $('textarea[maxlength]').each(function() {
        var maxLength = $(this).attr('maxlength');
        var currentLength = $(this).val().length;
        var counterId = $(this).attr('id') + '_counter';
        
        $(this).after('<small id="' + counterId + '" class="form-text text-muted">' + 
                     currentLength + '/' + maxLength + ' caractères</small>');
        
        $(this).on('input', function() {
            var currentLength = $(this).val().length;
            $('#' + counterId).text(currentLength + '/' + maxLength + ' caractères');
            
            if (currentLength > maxLength * 0.9) {
                $('#' + counterId).removeClass('text-muted').addClass('text-warning');
            } else {
                $('#' + counterId).removeClass('text-warning').addClass('text-muted');
            }
        });
    });
});

// Fonctions utilitaires

/**
 * Affiche une alerte personnalisée
 * @param {string} message - Le message à afficher
 * @param {string} type - Le type d'alerte (success, danger, warning, info)
 */
function showAlert(message, type = 'info') {
    var alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            <i class="fas fa-${getAlertIcon(type)} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    
    $('.container-fluid').prepend(alertHtml);
    
    // Auto-dismiss après 5 secondes
    setTimeout(function() {
        $('.alert').first().fadeOut('slow', function() {
            $(this).remove();
        });
    }, 5000);
}

/**
 * Retourne l'icône appropriée pour le type d'alerte
 * @param {string} type - Le type d'alerte
 * @returns {string} - La classe d'icône FontAwesome
 */
function getAlertIcon(type) {
    switch(type) {
        case 'success': return 'check-circle';
        case 'danger': return 'exclamation-circle';
        case 'warning': return 'exclamation-triangle';
        case 'info': return 'info-circle';
        default: return 'info-circle';
    }
}

/**
 * Confirme une action avec un modal personnalisé
 * @param {string} title - Le titre du modal
 * @param {string} message - Le message de confirmation
 * @param {function} callback - La fonction à exécuter si confirmé
 */
function confirmAction(title, message, callback) {
    var modalHtml = `
        <div class="modal fade" id="confirmModal" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">${title}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        ${message}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Annuler</button>
                        <button type="button" class="btn btn-danger" id="confirmBtn">Confirmer</button>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    $('body').append(modalHtml);
    
    $('#confirmBtn').on('click', function() {
        callback();
        $('#confirmModal').modal('hide');
    });
    
    $('#confirmModal').on('hidden.bs.modal', function() {
        $(this).remove();
    });
    
    $('#confirmModal').modal('show');
}

/**
 * Formate une date en français
 * @param {Date} date - La date à formater
 * @returns {string} - La date formatée
 */
function formatDateFr(date) {
    return new Intl.DateTimeFormat('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

/**
 * Calcule l'âge en années à partir d'une date de naissance
 * @param {Date} dateNaissance - La date de naissance
 * @returns {number} - L'âge en années
 */
function calculerAge(dateNaissance) {
    var today = new Date();
    var birthDate = new Date(dateNaissance);
    var age = today.getFullYear() - birthDate.getFullYear();
    var monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
    return age;
}

/**
 * Valide un email
 * @param {string} email - L'email à valider
 * @returns {boolean} - True si l'email est valide
 */
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Valide un numéro de téléphone français
 * @param {string} phone - Le numéro à valider
 * @returns {boolean} - True si le numéro est valide
 */
function isValidPhoneFr(phone) {
    var phoneRegex = /^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$/;
    return phoneRegex.test(phone);
}

/**
 * Affiche un spinner de chargement
 * @param {string} elementId - L'ID de l'élément où afficher le spinner
 */
function showLoading(elementId) {
    var spinner = '<div class="text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Chargement...</span></div></div>';
    $('#' + elementId).html(spinner);
}

/**
 * Cache le spinner de chargement
 * @param {string} elementId - L'ID de l'élément contenant le spinner
 * @param {string} content - Le contenu à afficher à la place
 */
function hideLoading(elementId, content = '') {
    $('#' + elementId).html(content);
}

/**
 * Copie du texte dans le presse-papiers
 * @param {string} text - Le texte à copier
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showAlert('Texte copié dans le presse-papiers', 'success');
    }, function() {
        showAlert('Erreur lors de la copie', 'danger');
    });
}

/**
 * Génère un ID unique
 * @returns {string} - Un ID unique
 */
function generateUniqueId() {
    return 'id_' + Math.random().toString(36).substr(2, 9);
}

/**
 * Débounce une fonction (limite la fréquence d'exécution)
 * @param {function} func - La fonction à débouncer
 * @param {number} wait - Le délai d'attente en millisecondes
 * @returns {function} - La fonction débouncée
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Gestion des erreurs AJAX globales
$(document).ajaxError(function(event, xhr, settings, thrownError) {
    console.error('Erreur AJAX:', thrownError);
    showAlert('Une erreur est survenue lors de la communication avec le serveur.', 'danger');
});

// Gestion du mode sombre (optionnel)
function toggleDarkMode() {
    $('body').toggleClass('dark-mode');
    localStorage.setItem('darkMode', $('body').hasClass('dark-mode'));
}

// Restaurer le mode sombre au chargement
if (localStorage.getItem('darkMode') === 'true') {
    $('body').addClass('dark-mode');
}

// Gestion de la recherche avec debounce
const debouncedSearch = debounce(function(searchTerm) {
    // Logique de recherche
    console.log('Recherche:', searchTerm);
}, 300);

// Événements pour la recherche
$('#searchInput').on('input', function() {
    debouncedSearch($(this).val());
});

// Gestion des formulaires avec AJAX
function submitFormAjax(formId, successCallback, errorCallback) {
    $('#' + formId).on('submit', function(e) {
        e.preventDefault();
        
        var formData = new FormData(this);
        var url = $(this).attr('action');
        var method = $(this).attr('method') || 'POST';
        
        $.ajax({
            url: url,
            type: method,
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (successCallback) {
                    successCallback(response);
                } else {
                    showAlert('Opération réussie', 'success');
                }
            },
            error: function(xhr, status, error) {
                if (errorCallback) {
                    errorCallback(xhr, status, error);
                } else {
                    showAlert('Une erreur est survenue', 'danger');
                }
            }
        });
    });
}

// Initialisation des graphiques (si Chart.js est disponible)
function initializeCharts() {
    if (typeof Chart !== 'undefined') {
        // Configuration par défaut pour tous les graphiques
        Chart.defaults.font.family = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        Chart.defaults.color = '#6c757d';
    }
}

// Appeler l'initialisation des graphiques
$(document).ready(function() {
    initializeCharts();
});