# Fiche d'exercices : Les Tableaux en C

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */

.exercise-cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    max-width: 100%;
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
}

.exercise-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.exercise-content-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.exercise-card.intro { border-left-color: #4CAF50; }
.exercise-card.easy { border-left-color: #2196F3; }
.exercise-card.medium { border-left-color: #FF9800; }
.exercise-card.hard { border-left-color: #F44336; }

.difficulty-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.difficulty-badge.intro { background: rgba(76, 175, 80, 0.1); color: #4CAF50; }
.difficulty-badge.easy { background: rgba(33, 150, 243, 0.1); color: #2196F3; }
.difficulty-badge.medium { background: rgba(255, 152, 0, 0.1); color: #FF9800; }
.difficulty-badge.hard { background: rgba(244, 67, 54, 0.1); color: #F44336; }

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

.section-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
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
    min-width: 150px;
    text-align: center;
}

.section-tab:hover {
    background: #e0e0e0;
    transform: translateY(-2px);
}

.section-tab.active {
    background: linear-gradient(135deg, #ead466ff 0%, #e8a508ff 100%);;
    color: white;
    box-shadow: 0 4px 12px rgba(234, 227, 102, 0.4);
}

.section-content {
    display: none;
    animation: fadeIn 0.3s ease;
}

.section-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

pre { margin: 0; font-family: 'Courier New', monospace; }
code { font-family: 'Courier New', monospace; }
</style>

<script>
function showSection(sectionId) {
    const allContents = document.querySelectorAll('.section-content');
    const allTabs = document.querySelectorAll('.section-tab');
    
    allContents.forEach(content => content.classList.remove('active'));
    allTabs.forEach(tab => tab.classList.remove('active'));
    
    document.getElementById(sectionId).classList.add('active');
    
    const buttons = document.getElementsByTagName('button');
    for (let btn of buttons) {
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(sectionId)) {
            btn.classList.add('active');
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    showSection('intro-section');
});
</script>

<div class="section-tabs">
    <button class="section-tab" onclick="showSection('intro-section')">🎯 Exercices d'introduction</button>
    <button class="section-tab" onclick="showSection('easy-section')">🌟 Niveau 1</button>
    <button class="section-tab" onclick="showSection('medium-section')">🔥 Niveau 2</button>
    <button class="section-tab" onclick="showSection('hard-section')">🚀 Niveau 3</button>
</div>

<!-- SECTION 1: INTRODUCTION -->
<div id="intro-section" class="section-content">
    <div class="exercise-cards">
        
        <!-- Exo 1 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Déclaration Simple</h4>
                <div class="exercise-content">
                    <p>Dans une fonction <code>main</code>, déclarer un tableau d'entiers nommé <code>scores</code> capable de contenir 5 valeurs.</p>
                </div>
            </div>
        </div>

        <!-- Exo 2 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Initialisation</h4>
                <div class="exercise-content">
                    <p>Déclarer un tableau <code>premiers</code> et l'initialiser directement avec les 5 premiers nombres premiers (2, 3, 5, 7, 11).</p>
                </div>
            </div>
        </div>

        <!-- Exo 3 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Accès Lecture</h4>
                <div class="exercise-content">
                    <p>À partir du tableau <code>premiers</code> précédent, afficher le 3ème élément (le nombre 5) en utilisant <code>printf</code>.</p>
                </div>
            </div>
        </div>

        <!-- Exo 4 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Accès Écriture</h4>
                <div class="exercise-content">
                    <p>Changer la première valeur du tableau <code>scores</code> (de l'exercice 1) pour lui donner la valeur 100.</p>
                </div>
            </div>
        </div>

        <!-- Exo 5 -->
        <div class="exercise-card intro">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge intro">Introduction</div>
                <h4 class="exercise-title">Affichage complet</h4>
                <div class="exercise-content">
                    <p>Écrire une boucle <code>for</code> qui parcourt le tableau <code>premiers</code> et affiche chaque nombre suivi d'un espace.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 2: NIVEAU 1 -->
<div id="easy-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 6 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Somme des éléments</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int somme_tableau(int tab[], int taille)</code> qui renvoie la somme de tous les éléments du tableau.</p>
                </div>
            </div>
        </div>

        <!-- Exo 7 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Moyenne</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>float moyenne(int tab[], int taille)</code> qui calcule et renvoie la moyenne des valeurs.</p>
                </div>
            </div>
        </div>

        <!-- Exo 8 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Compteur de Zéros</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction qui compte combien de fois le nombre 0 apparaît dans un tableau donné.</p>
                </div>
            </div>
        </div>

        <!-- Exo 9 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Remplissage 1 à N</h4>
                <div class="exercise-content">
                    <p>Écrire une procédure qui remplit un tableau existant avec les nombres 1, 2, 3... jusqu'à la taille du tableau.</p>
                </div>
            </div>
        </div>

        <!-- Exo 10 -->
        <div class="exercise-card easy">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge easy">Niveau 1</div>
                <h4 class="exercise-title">Copie de Tableau</h4>
                <div class="exercise-content">
                    <p>Écrire une procédure qui copie le contenu d'un tableau A vers un tableau B (les deux ont la même taille).</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 3: NIVEAU 2 -->
<div id="medium-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 11 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Le Maximum</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int trouver_max(int tab[], int taille)</code> qui renvoie la plus grande valeur présente dans le tableau.</p>
                </div>
            </div>
        </div>

        <!-- Exo 12 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Index du Minimum</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction qui ne renvoie pas la valeur minimale, mais <strong>l'indice</strong> (la position) où se trouve le minimum.</p>
                </div>
            </div>
        </div>

        <!-- Exo 13 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Affichage Inversé</h4>
                <div class="exercise-content">
                    <p>Afficher le contenu d'un tableau en partant de la fin (dernier élément) jusqu'au début (premier élément).</p>
                </div>
            </div>
        </div>

        <!-- Exo 14 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Recherche séquentielle</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction <code>int recherche(int tab[], int taille, int valeur)</code> qui renvoie l'indice de <code>valeur</code> si elle est trouvée, ou -1 si elle n'est pas dans le tableau.</p>
                </div>
            </div>
        </div>

        <!-- Exo 15 -->
        <div class="exercise-card medium">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge medium">Niveau 2</div>
                <h4 class="exercise-title">Tableaux Identiques ?</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction qui prend deux tableaux et renvoie 1 s'ils contiennent exactement les mêmes éléments dans le même ordre, 0 sinon.</p>
                </div>
            </div>
        </div>

    </div>
</div>

<!-- SECTION 4: NIVEAU 3 -->
<div id="hard-section" class="section-content">
    <div class="exercise-cards">

        <!-- Exo 16 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Palindrome</h4>
                <div class="exercise-content">
                    <p>Vérifier si un tableau est un "palindrome" (se lit pareil dans les deux sens).<br>Ex: {1, 2, 3, 2, 1} est un palindrome.</p>
                </div>
            </div>
        </div>

        <!-- Exo 17 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Rotation à Droite</h4>
                <div class="exercise-content">
                    <p>Déplacer tous les éléments d'un cran vers la droite. Le dernier élément devient le premier.<br>Ex: {1, 2, 3} devient {3, 1, 2}.</p>
                </div>
            </div>
        </div>

        <!-- Exo 18 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Fusion de tableaux</h4>
                <div class="exercise-content">
                    <p>Prendre deux tableaux A et B de même taille, et créer un tableau C deux fois plus grand qui contient A suivi de B.</p>
                </div>
            </div>
        </div>

        <!-- Exo 19 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Détection de Doublons</h4>
                <div class="exercise-content">
                    <p>Écrire une fonction qui renvoie 1 si le tableau contient au moins deux fois la même valeur, 0 sinon.</p>
                </div>
            </div>
        </div>

        <!-- Exo 20 -->
        <div class="exercise-card hard">
            <div class="exercise-content-wrapper">
                <div class="difficulty-badge hard">Niveau 3</div>
                <h4 class="exercise-title">Inversion en place</h4>
                <div class="exercise-content">
                    <p>Inverser l'ordre des éléments d'un tableau <strong>sans utiliser de deuxième tableau</strong> (en modifiant le tableau original directement).</p>
                </div>
            </div>
        </div>

    </div>
</div>
