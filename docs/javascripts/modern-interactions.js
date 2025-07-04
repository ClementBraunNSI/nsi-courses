// Modern Interactions for MkDocs Material

document.addEventListener('DOMContentLoaded', function() {
    // Progress bar for scroll position
    createProgressBar();
    
    // Smooth reveal animations on scroll
    initScrollAnimations();
    
    // Enhanced search functionality
    enhanceSearch();
    
    // Add floating action button
    createFloatingActionButton();
    
    // Initialize tooltips
    initTooltips();
    
    // Add copy code functionality
    enhanceCodeBlocks();
    
    // Theme transition effects
    enhanceThemeToggle();
});

// Create progress bar
function createProgressBar() {
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        progressBar.style.width = scrollPercent + '%';
    });
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.md-typeset h2, .md-typeset h3, .level-card, .admonition');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Enhanced search
function enhanceSearch() {
    const searchInput = document.querySelector('.md-search__input');
    if (searchInput) {
        searchInput.addEventListener('focus', function() {
            this.parentElement.classList.add('search-focused');
        });
        
        searchInput.addEventListener('blur', function() {
            this.parentElement.classList.remove('search-focused');
        });
    }
}

// Floating action button
function createFloatingActionButton() {
    const fab = document.createElement('a');
    fab.href = '#';
    fab.className = 'fab';
    fab.innerHTML = '↑';
    fab.title = 'Retour en haut';
    fab.style.display = 'none';
    
    fab.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    document.body.appendChild(fab);
    
    // Show/hide FAB based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            fab.style.display = 'flex';
        } else {
            fab.style.display = 'none';
        }
    });
}

// Initialize tooltips
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(el => {
        el.classList.add('tooltip');
    });
}

// Enhanced code blocks
function enhanceCodeBlocks() {
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        const pre = block.parentElement;
        
        // Add copy button
        const copyButton = document.createElement('button');
        copyButton.innerHTML = '📋';
        copyButton.className = 'copy-code-btn';
        copyButton.style.cssText = `
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            border-radius: 6px;
            padding: 8px;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s ease;
            backdrop-filter: blur(10px);
        `;
        
        pre.style.position = 'relative';
        pre.appendChild(copyButton);
        
        // Show copy button on hover
        pre.addEventListener('mouseenter', () => {
            copyButton.style.opacity = '1';
        });
        
        pre.addEventListener('mouseleave', () => {
            copyButton.style.opacity = '0';
        });
        
        // Copy functionality
        copyButton.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(block.textContent);
                copyButton.innerHTML = '✅';
                setTimeout(() => {
                    copyButton.innerHTML = '📋';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy code:', err);
            }
        });
    });
}

// Enhanced theme toggle
function enhanceThemeToggle() {
    const themeToggle = document.querySelector('[data-md-component="palette"]');
    if (themeToggle) {
        themeToggle.addEventListener('change', function() {
            // Add transition effect when switching themes
            document.body.style.transition = 'all 0.3s ease';
            setTimeout(() => {
                document.body.style.transition = '';
            }, 300);
        });
    }
}

// Parallax effect for hero section
function initParallax() {
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = scrolled * 0.5;
            heroSection.style.transform = `translateY(${parallax}px)`;
        });
    }
}

// Add smooth hover effects to navigation items
function enhanceNavigation() {
    const navItems = document.querySelectorAll('.md-nav__item');
    navItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(5px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });
}

// Initialize all enhancements
function initAllEnhancements() {
    initParallax();
    enhanceNavigation();
}

// Call additional enhancements after DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAllEnhancements);
} else {
    initAllEnhancements();
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('.md-search__input');
        if (searchInput) {
            searchInput.focus();
        }
    }
    
    // Escape to close search
    if (e.key === 'Escape') {
        const searchInput = document.querySelector('.md-search__input');
        if (searchInput && document.activeElement === searchInput) {
            searchInput.blur();
        }
    }
});

// Add loading animation
function showLoadingAnimation() {
    const loader = document.createElement('div');
    loader.className = 'page-loader';
    loader.innerHTML = '<div class="loading"></div>';
    loader.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        backdrop-filter: blur(10px);
    `;
    
    document.body.appendChild(loader);
    
    // Remove loader after page is fully loaded
    window.addEventListener('load', function() {
        setTimeout(() => {
            loader.style.opacity = '0';
            setTimeout(() => {
                if (loader.parentNode) {
                    loader.parentNode.removeChild(loader);
                }
            }, 300);
        }, 500);
    });
}

// Initialize loading animation
if (document.readyState === 'loading') {
    showLoadingAnimation();
}