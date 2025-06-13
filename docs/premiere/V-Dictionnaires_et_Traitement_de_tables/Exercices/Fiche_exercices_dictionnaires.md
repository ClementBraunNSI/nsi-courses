# Fiche d'exercices : Dictionnaires

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
}

/* Styles pour les contextes d'exercices difficiles */
.context-container {
    margin-bottom: 2rem;
    border: 2px solid #F44336;
    border-radius: 12px;
    overflow: hidden;
    background: rgba(244, 67, 54, 0.02);
}

.context-header {
    background: linear-gradient(135deg, #F44336 0%, #D32F2F 100%);
    color: white;
    padding: 1rem 1.5rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    user-select: none;
}

.context-header:hover {
    background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
    transform: translateY(-1px);
}

.context-header .arrow {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}

.context-header.active .arrow {
    transform: rotate(90deg);
}

.context-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background: white;
}

.context-content.show {
    max-height: 10000px;
    padding: 1rem;
}

.context-exercises {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

/* Uniformiser la hauteur des cartes d'exercices dans les contextes */
.context-exercises .exercise-card {
    min-height: 200px;
    align-items: stretch;
}

.context-exercises .exercise-content-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100%;
}

.context-exercises .exercise-content {
    flex-grow: 1;
}

.context-exercises .toggle-solution {
    margin-top: auto;
    align-self: flex-start;
}

.exercise-card {
    background: var(--md-default-bg-color);
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 3px solid;
    width: 100%;
    max-width: 100%;
    min-height: fit-content;
}

.exercise-content-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* Modal pour les solutions */
.solution-modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(3px);
}

.solution-modal.show {
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.3s ease;
}

.solution-content {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 2rem;
    max-width: 80%;
    max-height: 80%;
    overflow-y: auto;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    position: relative;
    animation: slideIn 0.3s ease;
}

.solution-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #f44336;
    color: white;
    border: none;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    cursor: pointer;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s ease;
}

.solution-close:hover {
    background: #d32f2f;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideIn {
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.solution-wrapper {
    display: none;
}

.exercise-card.intro {
    border-left-color: #4CAF50;
}

.exercise-card.intro:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
}

.exercise-card.easy {
    border-left-color: #2196F3;
}

.exercise-card.easy:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(33, 150, 243, 0.4);
}

.exercise-card.medium {
    border-left-color: #FF9800;
}

.exercise-card.medium:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 152, 0, 0.4);
}

.exercise-card.hard {
    border-left-color: #F44336;
}

.exercise-card.hard:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(244, 67, 54, 0.4);
}

.exercise-card.important {
    border-left-color: #ff8c42;
    background: linear-gradient(135deg, rgba(255, 140, 66, 0.05) 0%, rgba(255, 140, 66, 0.02) 100%);
}

.exercise-card.important:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 15px rgba(255, 140, 66, 0.4);
}

.exercise-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.1rem;
    font-weight: 600;
}

.exercise-content {
    margin-bottom: 1rem;
    line-height: 1.6;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro {
    background: rgba(76, 175, 80, 0.1);
    color: #4CAF50;
}

.difficulty-badge.easy {
    background: rgba(33, 150, 243, 0.1);
    color: #2196F3;
}

.difficulty-badge.medium {
    background: rgba(255, 152, 0, 0.1);
    color: #FF9800;
}

.difficulty-badge.hard {
    background: rgba(244, 67, 54, 0.1);
    color: #F44336;
}

.difficulty-badge.important {
    background: rgba(255, 140, 66, 0.1);
    color: #ff8c42;
}

.toggle-solution {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
}

.toggle-solution:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.toggle-solution.active {
    background: linear-gradient(135deg, #ff7f50 0%, #ff6347 100%);
}

.arrow {
    transition: transform 0.3s ease;
}

.solution {
    height: 100%;
    overflow-y: auto;
}

.solution pre {
    margin: 0;
    font-size: 0.85rem;
}

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
    padding: 0;
}

.section-tab {
    background: #f5f5f5;
    color: #333;
    border: none;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    flex: 1;
    min-width: 200px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 179, 71, 0.4);
}

.section-content {
    display: none;
    margin-top: 2rem;
    padding: 2rem;
    background: #fafafa;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
}

.section-content.active {
    display: block;
}

/* JavaScript pour les fonctionnalités interactives */
.exercise-script {
    display: none;
}
</style>

<script>
// JavaScript pour les fonctionnalités interactives des fiches d'exercices

function toggleSolution(button) {
    const card = button.closest('.exercise-card');
    const solutionWrapper = card.querySelector('.solution-wrapper');
    
    // Créer la modal si elle n'existe pas déjà
    let modal = document.getElementById('solution-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'solution-modal';
        modal.className = 'solution-modal';
        document.body.appendChild(modal);
        
        // Fermer la modal en cliquant à l'extérieur
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeSolutionModal();
            }
        });
    }
    
    // Créer le contenu de la modal
    const exerciseTitle = card.querySelector('.exercise-title').textContent;
    const solutionContent = solutionWrapper.innerHTML;
    
    modal.innerHTML = `
        <div class="solution-content">
            <button class="solution-close" onclick="closeSolutionModal()">×</button>
            <h3>Correction : ${exerciseTitle}</h3>
            ${solutionContent}
        </div>
    `;
    
    // Afficher la modal
    modal.classList.add('show');
    document.body.style.overflow = 'hidden'; // Empêcher le scroll de la page
}

function closeSolutionModal() {
    const modal = document.getElementById('solution-modal');
    if (modal) {
        modal.classList.remove('show');
        document.body.style.overflow = ''; // Restaurer le scroll de la page
    }
}

// Fermer la modal avec la touche Échap
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeSolutionModal();
    }
});

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

function toggleContext(header) {
    const content = header.nextElementSibling;
    const arrow = header.querySelector('.arrow');
    
    if (content.classList.contains('show')) {
        content.classList.remove('show');
        header.classList.remove('active');
    } else {
        content.classList.add('show');
        header.classList.add('active');
    }
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    const firstTab = document.querySelector('.section-tab');
    if (firstTab) {
        firstTab.click();
    }
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau Facile</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau Intermédiaire</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau Difficile</button>
</div>

<div id="intro-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Moyenne d'une interrogation</h4>
            <div class="exercise-content">
                <p>Un dictionnaire <code>notes</code> représente les notes d'une interrogation.</p>
                <pre><code>notes = {
    'Alice': 15,
    'Bob': 12,
    'Charlie': 18,
    'Diana': 14
}</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Création et accès</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>afficher_notes</code> qui prend en paramètre un dictionnaire et affiche la moyenne de chaque élève sous la forme : <code>"Alice a une moyenne de 15."</code>.</p>
                <p>Ajouter un commentaire selon la moyenne : <code>"Excellent"</code> pour une moyenne ≥ 16, <code>"Bien"</code> pour une moyenne entre 12 et 15 inclus, et <code>"À améliorer"</code> pour une moyenne < 12.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def afficher_notes(notes):
    for eleve in notes:
        moyenne = notes[eleve]
        print(eleve + "a une moyenne de "+ str(moyenne)+".")
        if moyenne >= 16:
            print("Excellent")
        elif 12 <= moyenne <= 15:
            print("Bien")
        else:
            print("À améliorer")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🦊</div>
            <h4 class="exercise-title">Modification et ajout</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>ajouter_eleve(notes, nom, moyenne)</code> qui ajoute un nouvel élève au dictionnaire.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def ajouter_eleve(notes, nom, moyenne):
    # On vérifie d'abord si l'élève existe déjà
    if nom in notes:
        print("L'élève "+nom+" existe déjà !")
    else:
        # Si l'élève n'existe pas, on l'ajoute
        notes[nom] = moyenne
        print("L'élève "+nom+" a été ajouté avec la moyenne de "+str(moyenne))</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="easy-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Parcours de dictionnaire</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>modifier_moyenne(notes, nom, nouvelle_moyenne)</code> qui modifie la moyenne d'un élève.</p>
                <p>Gérer le cas où l'élève à modifier n'existe pas.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def modifier_moyenne(notes, nom, nouvelle_moyenne):
    # On vérifie si l'élève existe dans le dictionnaire
    if nom in notes:
        # Si oui, on modifie sa moyenne
        notes[nom] = nouvelle_moyenne
        print("La moyenne de "+nom+" a été mise à jour à "+str(nouvelle_moyenne))
    else:
        print("L'élève "+ nom + " n'existe pas dans la liste")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊🦊</div>
            <h4 class="exercise-title">Dictionnaire de notes</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>eleves_mention(notes, seuil)</code> qui renvoie la liste des élèves ayant une moyenne ≥ seuil.</p>
                <p>Afficher également le nombre total d'élèves ayant cette mention.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def eleves_mention(notes, seuil):
    # On crée une liste vide pour stocker les élèves
    eleves_avec_mention = []
    # On parcourt le dictionnaire
    for eleve in notes:
        if notes[eleve] >= seuil:
            eleves_avec_mention.append(eleve)
    # On affiche le résultat
    print(str(len(eleves_avec_mention)) + " élèves ont une mention")
    return eleves_avec_mention</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Gestion d'un concessionnaire</h4>
            <div class="exercise-content">
                <p>Un dictionnaire <code>voitures</code> stocke des informations sur les voitures d'un concessionnaire.</p>
                <pre><code>voitures = {
    'Peugeot 208': {'prix': 15000, 'couleur': 'rouge', 'année': 2020},
    'Renault Clio': {'prix': 12000, 'couleur': 'bleu', 'année': 2019}
}</code></pre>
                <p>Écrire une fonction <code>voitures_par_couleur</code> qui renvoie la liste des voitures d'une couleur donnée.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def voitures_par_couleur(voitures, couleur):
    """
    Renvoie la liste des voitures d'une couleur donnée
    """
    voitures_couleur = []
    for voiture in voitures:
        if voitures[voiture]['couleur'] == couleur:
            voitures_couleur.append(voiture)
    return voitures_couleur</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Voitures dans un budget</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>voitures_budget</code> qui renvoie les voitures dont le prix est inférieur ou égal à un budget donné.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def voitures_budget(voitures, budget):
    """
    Renvoie les voitures dans le budget
    """
    voitures_abordables = []
    for voiture in voitures:
        if voitures[voiture]['prix'] <= budget:
            voitures_abordables.append(voiture)
    return voitures_abordables</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Gestion des bibliothèques</h4>
            <div class="exercise-content">
                <p>Un dictionnaire <code>bibliotheque</code> stocke des informations sur les livres.</p>
                <pre><code>bibliotheque = {
    'Le Petit Prince': {'auteur': 'Saint-Exupéry', 'genre': 'Fiction', 'disponible': True},
    '1984': {'auteur': 'Orwell', 'genre': 'Science-fiction', 'disponible': False}
}</code></pre>
                <p>Écrire une fonction <code>livres_disponibles</code> qui renvoie la liste des livres disponibles.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def livres_disponibles(bibliotheque):
    """
    Renvoie la liste des livres disponibles
    """
    livres_dispo = []
    for livre in bibliotheque:
        if bibliotheque[livre]['disponible']:
            livres_dispo.append(livre)
    return livres_dispo</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Emprunter un livre</h4>
            <div class="exercise-content">
                <p>Écrire une fonction <code>emprunter_livre</code> qui permet d'emprunter un livre (le marquer comme non disponible).</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def emprunter_livre(bibliotheque, titre):
    """
    Emprunte un livre s'il est disponible
    """
    if titre in bibliotheque:
        if bibliotheque[titre]['disponible']:
            bibliotheque[titre]['disponible'] = False
            return "Livre emprunté avec succès"
        else:
            return "Livre déjà emprunté"
    return "Livre non trouvé"</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Gestion des employés</h4>
            <div class="exercise-content">
                <p>Un dictionnaire <code>employes</code> stocke des informations sur les employés d'une entreprise.</p>
                <pre><code>employes = {
    'Alice': {'poste': 'Développeur', 'salaire': 45000, 'anciennete': 3},
    'Bob': {'poste': 'Designer', 'salaire': 40000, 'anciennete': 2}
}</code></pre>
                <p>Écrire une fonction <code>augmentation_salaire</code> qui augmente le salaire d'un employé de 10% s'il a plus de 2 ans d'ancienneté.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def augmentation_salaire(employes, nom):
    """
    Augmente le salaire si l'ancienneté > 2 ans
    """
    if nom in employes:
        if employes[nom]['anciennete'] > 2:
            employes[nom]['salaire'] = int(employes[nom]['salaire'] * 1.1)
            return "Augmentation accordée"
        else:
            return "Ancienneté insuffisante"
    return "Employé non trouvé"</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Gestion des contacts</h4>
            <div class="exercise-content">
                <p>Un dictionnaire <code>contacts</code> stocke des informations de contact.</p>
                <pre><code>contacts = {
    'Alice': {'téléphone': '0123456789', 'email': 'alice@email.com', 'ville': 'Paris'},
    'Bob': {'téléphone': '0987654321', 'email': 'bob@email.com', 'ville': 'Lyon'}
}</code></pre>
                <p>Écrire une fonction <code>rechercher_contact(nom)</code> qui affiche toutes les informations d'un contact</p>
                <p>Écrire une fonction <code>contacts_par_ville(ville)</code> qui retourne la liste des noms des personnes habitant dans une ville donnée</p>
                <p>Écrire une fonction <code>modifier_telephone(nom, nouveau_telephone)</code> qui modifie le numéro de téléphone d'un contact</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def rechercher_contact(nom):
    """Affiche toutes les informations d'un contact"""
    if nom in contacts:
        print(f"Informations de {nom}:")
        for cle, valeur in contacts[nom].items():
            print(f"  {cle}: {valeur}")
    else:
        print(f"Contact {nom} non trouvé.")

def contacts_par_ville(ville):
    """Retourne la liste des contacts d'une ville"""
    personnes_ville = []
    for nom, infos in contacts.items():
        if infos['ville'] == ville:
            personnes_ville.append(nom)
    return personnes_ville

def modifier_telephone(nom, nouveau_telephone):
    """Modifie le numéro de téléphone d'un contact"""
    if nom in contacts:
        contacts[nom]['telephone'] = nouveau_telephone
        print(f"Téléphone de {nom} mis à jour.")
    else:
        print(f"Contact {nom} non trouvé.")

# Tests des fonctions
rechercher_contact('Alice Martin')
print("Contacts à Paris:", contacts_par_ville('Paris'))
modifier_telephone('Bob Dupont', '06.99.88.77.66')</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🦊</div>
            <h4 class="exercise-title">Inventaire de magasin</h4>
            <div class="exercise-content">
                <p>Un magasin utilise un dictionnaire pour gérer son inventaire :</p>
                <pre><code>inventaire = {
    'pommes': {'prix': 2.5, 'stock': 50},
    'bananes': {'prix': 1.8, 'stock': 30},
    'oranges': {'prix': 3.0, 'stock': 25}
}</code></pre>
                <p>Écrire les fonctions suivantes :</p>
                <ol>
                    <li><code>afficher_inventaire()</code> : affiche tous les produits avec leur prix et stock</li>
                    <li><code>produits_en_rupture()</code> : retourne la liste des produits avec un stock ≤ 10</li>
                    <li><code>valeur_totale_stock()</code> : calcule la valeur totale du stock (prix × quantité pour chaque produit)</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>inventaire = {
    'pommes': {'prix': 2.5, 'stock': 50},
    'bananes': {'prix': 1.8, 'stock': 30},
    'oranges': {'prix': 3.0, 'stock': 25}
}

def afficher_inventaire():
    """Affiche tous les produits avec prix et stock"""
    print("=== INVENTAIRE ===")
    for produit, infos in inventaire.items():
        print(f"{produit}: {infos['prix']}€ - Stock: {infos['stock']}")

def produits_en_rupture():
    """Retourne les produits avec stock ≤ 10"""
    rupture = []
    for produit, infos in inventaire.items():
        if infos['stock'] <= 10:
            rupture.append(produit)
    return rupture

def valeur_totale_stock():
    """Calcule la valeur totale du stock"""
    total = 0
    for produit, infos in inventaire.items():
        total += infos['prix'] * infos['stock']
    return total

# Tests
afficher_inventaire()
print("Produits en rupture:", produits_en_rupture())
print(f"Valeur totale du stock: {valeur_totale_stock()}€")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="medium-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Système de notes - Partie 1</h4>
            <div class="exercise-content">
                <div class="context-box">
                    <div class="context-title">🎓 Contexte : Gestion des notes d'une classe</div>
                    <p>Vous développez un système pour gérer les notes des élèves d'une classe. Chaque élève a plusieurs matières avec plusieurs notes par matière.</p>
                </div>
                <p>Créer un dictionnaire <code>classe</code> qui stocke pour chaque élève ses notes par matière :</p>
                <pre><code>classe = {
    'Alice': {
        'Maths': [15, 12, 18],
        'Français': [14, 16, 13],
        'Histoire': [17, 15]
    },
    'Bob': {
        'Maths': [10, 14, 12],
        'Français': [13, 11, 15],
        'Histoire': [12, 14, 16]
    }
}</code></pre>
                <p>Écrire une fonction <code>moyenne_matiere(eleve, matiere)</code> qui calcule la moyenne d'un élève dans une matière donnée.</p>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>classe = {
    'Alice': {
        'Maths': [15, 12, 18],
        'Français': [14, 16, 13],
        'Histoire': [17, 15]
    },
    'Bob': {
        'Maths': [10, 14, 12],
        'Français': [13, 11, 15],
        'Histoire': [12, 14, 16]
    }
}

def moyenne_matiere(eleve, matiere):
    """Calcule la moyenne d'un élève dans une matière"""
    if eleve in classe and matiere in classe[eleve]:
        notes = classe[eleve][matiere]
        if len(notes) > 0:
            moyenne = sum(notes) / len(notes)
            return round(moyenne, 2)
        else:
            return 0
    else:
        print(f"Élève {eleve} ou matière {matiere} non trouvé(e)")
        return None

# Tests
print(f"Moyenne d'Alice en Maths: {moyenne_matiere('Alice', 'Maths')}")
print(f"Moyenne de Bob en Français: {moyenne_matiere('Bob', 'Français')}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Système de notes - Partie 2</h4>
            <div class="exercise-content">
                <div class="context-box">
                    <div class="context-title">🎓 Contexte : Gestion des notes d'une classe (suite)</div>
                    <p>Continuons le développement de notre système de notes avec des fonctionnalités plus avancées.</p>
                </div>
                <p>En utilisant le dictionnaire <code>classe</code> de l'exercice précédent :</p>
                <ol>
                    <li>Écrire une fonction <code>moyenne_generale(eleve)</code> qui calcule la moyenne générale d'un élève (moyenne de toutes ses matières)</li>
                    <li>Écrire une fonction <code>ajouter_note(eleve, matiere, note)</code> qui ajoute une note à un élève dans une matière</li>
                    <li>Écrire une fonction <code>bulletin_classe()</code> qui affiche le bulletin de tous les élèves avec leurs moyennes par matière et leur moyenne générale</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>def moyenne_generale(eleve):
    """Calcule la moyenne générale d'un élève"""
    if eleve in classe:
        moyennes_matieres = []
        for matiere, notes in classe[eleve].items():
            if len(notes) > 0:
                moyenne_mat = sum(notes) / len(notes)
                moyennes_matieres.append(moyenne_mat)
        
        if len(moyennes_matieres) > 0:
            return round(sum(moyennes_matieres) / len(moyennes_matieres), 2)
        else:
            return 0
    else:
        print(f"Élève {eleve} non trouvé")
        return None

def ajouter_note(eleve, matiere, note):
    """Ajoute une note à un élève dans une matière"""
    if eleve in classe:
        if matiere in classe[eleve]:
            classe[eleve][matiere].append(note)
        else:
            classe[eleve][matiere] = [note]
        print(f"Note {note} ajoutée pour {eleve} en {matiere}")
    else:
        print(f"Élève {eleve} non trouvé")

def bulletin_classe():
    """Affiche le bulletin de toute la classe"""
    print("=== BULLETIN DE CLASSE ===")
    for eleve in classe:
        print(f"\n--- {eleve} ---")
        for matiere, notes in classe[eleve].items():
            moyenne_mat = moyenne_matiere(eleve, matiere)
            print(f"{matiere}: {moyenne_mat}/20")
        print(f"Moyenne générale: {moyenne_generale(eleve)}/20")

# Tests
ajouter_note('Alice', 'Maths', 16)
bulletin_classe()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
            <h4 class="exercise-title">Analyse de ventes</h4>
            <div class="exercise-content">
                <p>Une entreprise stocke ses données de ventes dans un dictionnaire :</p>
                <pre><code>ventes = {
    'Janvier': {'produit_A': 150, 'produit_B': 200, 'produit_C': 100},
    'Février': {'produit_A': 180, 'produit_B': 150, 'produit_C': 120},
    'Mars': {'produit_A': 200, 'produit_B': 180, 'produit_C': 90}
}</code></pre>
                <p>Écrire les fonctions suivantes :</p>
                <ol>
                    <li><code>ventes_totales_mois(mois)</code> : calcule le total des ventes d'un mois</li>
                    <li><code>ventes_totales_produit(produit)</code> : calcule le total des ventes d'un produit sur tous les mois</li>
                    <li><code>meilleur_mois_produit(produit)</code> : trouve le mois où un produit s'est le mieux vendu</li>
                    <li><code>produit_le_plus_vendu()</code> : trouve le produit avec le plus de ventes totales</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code>ventes = {
    'Janvier': {'produit_A': 150, 'produit_B': 200, 'produit_C': 100},
    'Février': {'produit_A': 180, 'produit_B': 150, 'produit_C': 120},
    'Mars': {'produit_A': 200, 'produit_B': 180, 'produit_C': 90}
}

def ventes_totales_mois(mois):
    """Calcule le total des ventes d'un mois"""
    if mois in ventes:
        return sum(ventes[mois].values())
    else:
        print(f"Mois {mois} non trouvé")
        return 0

def ventes_totales_produit(produit):
    """Calcule le total des ventes d'un produit sur tous les mois"""
    total = 0
    for mois, produits in ventes.items():
        if produit in produits:
            total += produits[produit]
    return total

def meilleur_mois_produit(produit):
    """Trouve le mois où un produit s'est le mieux vendu"""
    meilleur_mois = None
    meilleures_ventes = 0
    
    for mois, produits in ventes.items():
        if produit in produits and produits[produit] > meilleures_ventes:
            meilleures_ventes = produits[produit]
            meilleur_mois = mois
    
    return meilleur_mois, meilleures_ventes

def produit_le_plus_vendu():
    """Trouve le produit avec le plus de ventes totales"""
    # Calculer les ventes totales pour chaque produit
    totaux_produits = {}
    
    # Récupérer tous les produits
    tous_produits = set()
    for mois_data in ventes.values():
        tous_produits.update(mois_data.keys())
    
    # Calculer le total pour chaque produit
    for produit in tous_produits:
        totaux_produits[produit] = ventes_totales_produit(produit)
    
    # Trouver le maximum
    meilleur_produit = max(totaux_produits, key=totaux_produits.get)
    return meilleur_produit, totaux_produits[meilleur_produit]

# Tests
print(f"Ventes totales de Janvier: {ventes_totales_mois('Janvier')}")
print(f"Ventes totales du produit_A: {ventes_totales_produit('produit_A')}")
mois, ventes_max = meilleur_mois_produit('produit_B')
print(f"Meilleur mois pour produit_B: {mois} ({ventes_max} ventes)")
produit, total = produit_le_plus_vendu()
print(f"Produit le plus vendu: {produit} ({total} ventes)")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="hard-section" class="section-content">

<!-- Contexte Inventaire -->
<div class="context-container">
    <div class="context-header" onclick="toggleContext(this)">
        <span>📦 Gestion d'inventaire de magasin</span>
        <span class="arrow">▶</span>
    </div>
    <div class="context-content">
        <div class="context-exercises">
            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Inventaire - Valeur totale</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>valeur_totale_inventaire</code> qui calcule la valeur totale d'un inventaire de magasin.</strong><br>
                        <pre><code>inventaire = {
    'pommes': {'quantite': 50, 'prix': 2.5, 'categorie': 'fruits'},
    'bananes': {'quantite': 30, 'prix': 1.8, 'categorie': 'fruits'},
    'carottes': {'quantite': 25, 'prix': 1.2, 'categorie': 'legumes'}
}</code></pre>
                        <p>La fonction doit calculer et retourner la valeur totale de l'inventaire (quantité × prix pour chaque produit).</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def valeur_totale_inventaire(inventaire):
    """Calcule la valeur totale de l'inventaire"""
    valeur_totale = 0
    for produit, infos in inventaire.items():
        valeur_totale += infos['quantite'] * infos['prix']
    return valeur_totale

# Test
inventaire = {
    'pommes': {'quantite': 50, 'prix': 2.5, 'categorie': 'fruits'},
    'bananes': {'quantite': 30, 'prix': 1.8, 'categorie': 'fruits'},
    'carottes': {'quantite': 25, 'prix': 1.2, 'categorie': 'legumes'}
}

print(f"Valeur totale: {valeur_totale_inventaire(inventaire)}€")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Inventaire - Produit le plus cher</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>produit_plus_cher</code> qui trouve le produit le plus cher dans l'inventaire.</strong><br>
                        <p>Utiliser le même dictionnaire <code>inventaire</code> que l'exercice précédent.</p>
                        <p>La fonction doit retourner le nom du produit le plus cher et son prix.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def produit_plus_cher(inventaire):
    """Trouve le produit le plus cher"""
    produit_cher = None
    prix_max = 0
    
    for produit, infos in inventaire.items():
        if infos['prix'] > prix_max:
            prix_max = infos['prix']
            produit_cher = produit
    
    return produit_cher, prix_max

# Test
produit, prix = produit_plus_cher(inventaire)
print(f"Produit le plus cher: {produit} ({prix}€)")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Inventaire - Filtrage par catégorie</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>produits_par_categorie</code> qui liste les produits d'une catégorie donnée.</strong><br>
                        <p>La fonction prend en paramètres l'inventaire et une catégorie, et retourne la liste des noms des produits de cette catégorie.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def produits_par_categorie(inventaire, categorie):
    """Liste les produits d'une catégorie donnée"""
    produits = []
    for produit, infos in inventaire.items():
        if infos['categorie'] == categorie:
            produits.append(produit)
    return produits

# Test
fruits = produits_par_categorie(inventaire, 'fruits')
legumes = produits_par_categorie(inventaire, 'legumes')
print(f"Fruits: {fruits}")
print(f"Légumes: {legumes}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Inventaire - Mise à jour des quantités</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>mettre_a_jour_quantite</code> qui met à jour la quantité d'un produit.</strong><br>
                        <p>La fonction prend en paramètres l'inventaire, le nom du produit et la nouvelle quantité.</p>
                        <p>Elle doit gérer le cas où le produit n'existe pas dans l'inventaire.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def mettre_a_jour_quantite(inventaire, produit, nouvelle_quantite):
    """Met à jour la quantité d'un produit"""
    if produit in inventaire:
        ancienne_quantite = inventaire[produit]['quantite']
        inventaire[produit]['quantite'] = nouvelle_quantite
        print(f"Quantité de {produit} mise à jour: {ancienne_quantite} → {nouvelle_quantite}")
        return True
    else:
        print(f"Erreur: Le produit '{produit}' n'existe pas dans l'inventaire")
        return False

# Test
mettre_a_jour_quantite(inventaire, 'pommes', 75)
mettre_a_jour_quantite(inventaire, 'oranges', 20)  # Produit inexistant</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Contexte Ventes -->
<div class="context-container">
    <div class="context-header" onclick="toggleContext(this)">
        <span>📊 Analyse de données de ventes</span>
        <span class="arrow">▶</span>
    </div>
    <div class="context-content">
        <div class="context-exercises">
            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Ventes - Total par mois</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>ventes_totales_par_mois</code> qui calcule les ventes totales pour chaque mois.</strong><br>
                        <pre><code>ventes = {
    'janvier': {'produit_A': 150, 'produit_B': 200, 'produit_C': 100},
    'fevrier': {'produit_A': 180, 'produit_B': 150, 'produit_C': 120},
    'mars': {'produit_A': 200, 'produit_B': 180, 'produit_C': 90}
}</code></pre>
                        <p>La fonction doit retourner un dictionnaire avec le total des ventes pour chaque mois.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def ventes_totales_par_mois(ventes):
    """Calcule les ventes totales pour chaque mois"""
    ventes_par_mois = {}
    for mois, produits in ventes.items():
        total_mois = sum(produits.values())
        ventes_par_mois[mois] = total_mois
    return ventes_par_mois

# Test
ventes = {
    'janvier': {'produit_A': 150, 'produit_B': 200, 'produit_C': 100},
    'fevrier': {'produit_A': 180, 'produit_B': 150, 'produit_C': 120},
    'mars': {'produit_A': 200, 'produit_B': 180, 'produit_C': 90}
}

resultat = ventes_totales_par_mois(ventes)
print("Ventes totales par mois:")
for mois, total in resultat.items():
    print(f"{mois}: {total}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Ventes - Total par produit</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>ventes_totales_par_produit</code> qui calcule les ventes totales pour chaque produit sur tous les mois.</strong><br>
                        <p>Utiliser le même dictionnaire <code>ventes</code> que l'exercice précédent.</p>
                        <p>La fonction doit retourner un dictionnaire avec le total des ventes pour chaque produit.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def ventes_totales_par_produit(ventes):
    """Calcule les ventes totales pour chaque produit"""
    ventes_par_produit = {}
    for mois, produits in ventes.items():
        for produit, quantite in produits.items():
            if produit not in ventes_par_produit:
                ventes_par_produit[produit] = 0
            ventes_par_produit[produit] += quantite
    return ventes_par_produit

# Test
resultat = ventes_totales_par_produit(ventes)
print("Ventes totales par produit:")
for produit, total in resultat.items():
    print(f"{produit}: {total}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Ventes - Meilleur mois par produit</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>meilleur_mois_par_produit</code> qui trouve le meilleur mois de vente pour chaque produit.</strong><br>
                        <p>La fonction doit retourner un dictionnaire où chaque produit est associé à son meilleur mois et la quantité vendue ce mois-là.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def meilleur_mois_par_produit(ventes):
    """Trouve le meilleur mois pour chaque produit"""
    meilleur_mois_produit = {}
    
    for mois, produits in ventes.items():
        for produit, quantite in produits.items():
            if produit not in meilleur_mois_produit:
                meilleur_mois_produit[produit] = {'mois': mois, 'quantite': quantite}
            elif quantite > meilleur_mois_produit[produit]['quantite']:
                meilleur_mois_produit[produit] = {'mois': mois, 'quantite': quantite}
    
    return meilleur_mois_produit

# Test
resultat = meilleur_mois_par_produit(ventes)
print("Meilleur mois par produit:")
for produit, info in resultat.items():
    print(f"{produit}: {info['mois']} ({info['quantite']} ventes)")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Ventes - Moyenne par produit</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>moyenne_ventes_par_produit</code> qui calcule la moyenne des ventes pour chaque produit.</strong><br>
                        <p>La fonction doit calculer la moyenne des ventes de chaque produit sur tous les mois disponibles.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def moyenne_ventes_par_produit(ventes):
    """Calcule la moyenne des ventes pour chaque produit"""
    # D'abord calculer les totaux par produit
    ventes_par_produit = ventes_totales_par_produit(ventes)
    
    # Calculer le nombre de mois
    nb_mois = len(ventes)
    
    # Calculer les moyennes
    moyenne_par_produit = {}
    for produit, total in ventes_par_produit.items():
        moyenne_par_produit[produit] = round(total / nb_mois, 2)
    
    return moyenne_par_produit

# Test
resultat = moyenne_ventes_par_produit(ventes)
print("Moyenne des ventes par produit:")
for produit, moyenne in resultat.items():
    print(f"{produit}: {moyenne}")</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="context-container">
    <div class="context-header" onclick="toggleContext(this)">
        <span>📚 Système de notation d'étudiants</span>
        <span class="arrow">▶</span>
    </div>
    <div class="context-content">
        <div class="context-exercises">
            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Notes - Moyenne par matière</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>moyenne_matiere</code> qui calcule la moyenne d'un étudiant dans une matière donnée.</strong><br>
                        <pre><code>etudiants = {
    'Alice': {'maths': [15, 12, 18], 'francais': [14, 16], 'histoire': [13, 15, 17]},
    'Bob': {'maths': [10, 14, 12], 'francais': [15, 13], 'histoire': [11, 14]}
}</code></pre>
                        <p>La fonction prend en paramètres le dictionnaire des étudiants, le nom de l'étudiant et la matière.</p>
                        <p>Elle doit gérer les cas d'erreur (étudiant ou matière inexistants).</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def moyenne_matiere(etudiants, etudiant, matiere):
    """Calcule la moyenne d'un étudiant dans une matière"""
    if etudiant in etudiants and matiere in etudiants[etudiant]:
        notes = etudiants[etudiant][matiere]
        if notes:
            return round(sum(notes) / len(notes), 2)
        else:
            return 0
    else:
        print(f"Erreur: Étudiant '{etudiant}' ou matière '{matiere}' non trouvé(e)")
        return None

# Test
etudiants = {
    'Alice': {'maths': [15, 12, 18], 'francais': [14, 16], 'histoire': [13, 15, 17]},
    'Bob': {'maths': [10, 14, 12], 'francais': [15, 13], 'histoire': [11, 14]}
}

print(f"Moyenne d'Alice en maths: {moyenne_matiere(etudiants, 'Alice', 'maths')}")
print(f"Moyenne de Bob en français: {moyenne_matiere(etudiants, 'Bob', 'francais')}")
print(f"Test erreur: {moyenne_matiere(etudiants, 'Charlie', 'maths')}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Notes - Moyenne générale</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>moyenne_generale</code> qui calcule la moyenne générale d'un étudiant.</strong><br>
                        <p>Utiliser le même dictionnaire <code>etudiants</code> que l'exercice précédent.</p>
                        <p>La fonction doit calculer la moyenne de toutes les matières de l'étudiant.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def moyenne_generale(etudiants, etudiant):
    """Calcule la moyenne générale d'un étudiant"""
    if etudiant in etudiants:
        moyennes_matieres = []
        for matiere, notes in etudiants[etudiant].items():
            if notes:  # Vérifier que la liste n'est pas vide
                moyenne = sum(notes) / len(notes)
                moyennes_matieres.append(moyenne)
        
        if moyennes_matieres:
            return round(sum(moyennes_matieres) / len(moyennes_matieres), 2)
        else:
            return 0
    else:
        print(f"Erreur: Étudiant '{etudiant}' non trouvé")
        return None

# Test
print(f"Moyenne générale d'Alice: {moyenne_generale(etudiants, 'Alice')}")
print(f"Moyenne générale de Bob: {moyenne_generale(etudiants, 'Bob')}")
print(f"Test erreur: {moyenne_generale(etudiants, 'Charlie')}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Notes - Classement par matière</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>classement_matiere</code> qui classe les étudiants dans une matière donnée.</strong><br>
                        <p>La fonction doit retourner une liste de tuples (étudiant, moyenne) triée par moyenne décroissante.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def classement_matiere(etudiants, matiere):
    """Classe les étudiants dans une matière"""
    moyennes = []
    for etudiant in etudiants:
        if matiere in etudiants[etudiant]:
            moyenne = moyenne_matiere(etudiants, etudiant, matiere)
            if moyenne is not None:
                moyennes.append((etudiant, moyenne))
    
    # Tri par moyenne décroissante
    moyennes.sort(key=lambda x: x[1], reverse=True)
    return moyennes

# Test
print("Classement en maths:")
classement = classement_matiere(etudiants, 'maths')
for i, (etudiant, moyenne) in enumerate(classement, 1):
    print(f"{i}. {etudiant}: {moyenne}")

print("\nClassement en français:")
classement = classement_matiere(etudiants, 'francais')
for i, (etudiant, moyenne) in enumerate(classement, 1):
    print(f"{i}. {etudiant}: {moyenne}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Notes - Ajout de notes</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>ajouter_note</code> qui ajoute une note à un étudiant dans une matière.</strong><br>
                        <p>La fonction doit gérer les cas où l'étudiant existe mais n'a pas encore de notes dans cette matière.</p>
                        <p>Elle doit aussi gérer le cas où l'étudiant n'existe pas.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def ajouter_note(etudiants, etudiant, matiere, note):
    """Ajoute une note à un étudiant"""
    if etudiant in etudiants:
        if matiere in etudiants[etudiant]:
            etudiants[etudiant][matiere].append(note)
            print(f"Note {note} ajoutée pour {etudiant} en {matiere}")
        else:
            etudiants[etudiant][matiere] = [note]
            print(f"Nouvelle matière '{matiere}' créée pour {etudiant} avec la note {note}")
        return True
    else:
        print(f"Erreur: Étudiant '{etudiant}' non trouvé")
        return False

# Test
print("État initial d'Alice en maths:", etudiants['Alice']['maths'])
ajouter_note(etudiants, 'Alice', 'maths', 16)
print("Après ajout:", etudiants['Alice']['maths'])

# Ajouter une nouvelle matière
ajouter_note(etudiants, 'Alice', 'physique', 14)
print("Nouvelles matières d'Alice:", list(etudiants['Alice'].keys()))

# Test avec étudiant inexistant
ajouter_note(etudiants, 'Charlie', 'maths', 15)</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="context-container">
    <div class="context-header" onclick="toggleContext(this)">
        <span>📝 Analyse de fréquence de mots</span>
        <span class="arrow">▶</span>
    </div>
    <div class="context-content">
        <div class="context-exercises">
            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Texte - Comptage de fréquence</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>compter_mots</code> qui compte la fréquence de chaque mot dans un texte.</strong><br>
                        <em>Exemple de texte :</em>
                        <pre><code>texte = "Python est un langage de programmation. Python est facile à apprendre."</code></pre>
                        <p>La fonction doit ignorer la casse et la ponctuation, et retourner un dictionnaire avec les fréquences.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def compter_mots(texte):
    """Compte la fréquence de chaque mot dans un texte"""
    import string
    
    # Nettoyer le texte : enlever la ponctuation et convertir en minuscules
    texte_propre = texte.lower()
    for caractere in string.punctuation:
        texte_propre = texte_propre.replace(caractere, '')
    
    # Diviser en mots
    mots = texte_propre.split()
    
    # Compter la fréquence de chaque mot
    frequences = {}
    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1
    
    return frequences

# Test
texte = "Python est un langage de programmation. Python est facile à apprendre."
frequences = compter_mots(texte)
print("Fréquences des mots:")
for mot, freq in frequences.items():
    print(f"{mot}: {freq}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Texte - Mots les plus fréquents</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>mots_plus_frequents</code> qui trouve les N mots les plus fréquents dans un texte.</strong><br>
                        <p>Utiliser la fonction <code>compter_mots</code> de l'exercice précédent.</p>
                        <p>La fonction prend en paramètres le texte et le nombre N de mots à retourner.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def mots_plus_frequents(texte, n=3):
    """Trouve les N mots les plus fréquents"""
    # Utiliser la fonction précédente
    frequences = compter_mots(texte)
    
    # Convertir en liste de tuples pour le tri
    mots_tries = []
    for mot, freq in frequences.items():
        mots_tries.append((mot, freq))
    
    # Tri par fréquence décroissante
    mots_tries.sort(key=lambda x: x[1], reverse=True)
    
    # Retourner les N premiers
    return mots_tries[:n]

# Test
texte = "Python est un langage de programmation. Python est facile à apprendre."
top_3 = mots_plus_frequents(texte, 3)
print(f"Top 3 des mots les plus fréquents: {top_3}")

top_5 = mots_plus_frequents(texte, 5)
print(f"Top 5 des mots les plus fréquents: {top_5}")</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Texte - Mots uniques</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>compter_mots_uniques</code> qui compte le nombre de mots uniques dans un texte.</strong><br>
                        <p>La fonction doit retourner le nombre total de mots différents (sans répétition).</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def compter_mots_uniques(texte):
    """Compte le nombre de mots uniques dans un texte"""
    frequences = compter_mots(texte)
    return len(frequences)

def statistiques_texte(texte):
    """Affiche des statistiques complètes sur un texte"""
    import string
    
    # Nettoyer le texte pour compter le total de mots
    texte_propre = texte.lower()
    for caractere in string.punctuation:
        texte_propre = texte_propre.replace(caractere, '')
    mots_total = len(texte_propre.split())
    
    # Calculer les statistiques
    mots_uniques = compter_mots_uniques(texte)
    
    print(f"Nombre total de mots: {mots_total}")
    print(f"Nombre de mots uniques: {mots_uniques}")
    print(f"Pourcentage de mots uniques: {round(mots_uniques/mots_total*100, 1)}%")
    
    return mots_total, mots_uniques

# Test
resultat = statistiques_texte(texte)</code></pre>
                    </div>
                </div>
            </div>

            <div class="exercise-card hard">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge hard">Difficile 🦊🦊🦊</div>
                    <h4 class="exercise-title">Texte - Mots répétés</h4>
                    <div class="exercise-content">
                        <strong>Écrire une fonction <code>mots_repetes</code> qui trouve tous les mots qui apparaissent plus d'une fois dans un texte.</strong><br>
                        <p>La fonction doit retourner une liste de tuples (mot, fréquence) pour les mots répétés.</p>
                    </div>
                    <button class="toggle-solution" onclick="toggleSolution(this)">
                        <span class="arrow">→</span> Voir la correction
                    </button>
                </div>
                <div class="solution-wrapper">
                    <div class="solution">
                        <pre><code>def mots_repetes(texte):
    """Trouve les mots qui apparaissent plus d'une fois"""
    frequences = compter_mots(texte)
    
    mots_frequents = []
    for mot, freq in frequences.items():
        if freq > 1:
            mots_frequents.append((mot, freq))
    
    # Trier par fréquence décroissante
    mots_frequents.sort(key=lambda x: x[1], reverse=True)
    
    return mots_frequents

def analyse_complete_texte(texte):
    """Analyse complète d'un texte"""
    print("=== ANALYSE COMPLÈTE DU TEXTE ===")
    print(f"Texte analysé: '{texte}'")
    print()
    
    # Statistiques générales
    statistiques_texte(texte)
    print()
    
    # Mots les plus fréquents
    top_3 = mots_plus_frequents(texte, 3)
    print(f"Top 3 des mots les plus fréquents: {top_3}")
    
    # Mots répétés
    repetes = mots_repetes(texte)
    if repetes:
        print(f"Mots répétés: {repetes}")
    else:
        print("Aucun mot répété")

# Test
analyse_complete_texte(texte)</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
</div>