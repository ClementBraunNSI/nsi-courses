<style>
/* Styles modernes pour le cours Web */
.course-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.timeline-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.highlight-fact {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.fact-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.fact-content {
    color: var(--md-default-fg-color);
    font-weight: 500;
    line-height: 1.6;
}

.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.info-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.info-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #4299e1;
}

.code-title {
    color: #4299e1;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.code-example pre {
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: #e2e8f0;
}

.format-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.format-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.format-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.format-card-title {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.format-card-content {
    color: #7f8c8d;
    line-height: 1.6;
}

.exercise-section {
    background: rgba(255, 193, 7, 0.1);
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.exercise-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
}

.exercise-list {
    list-style: none;
    padding: 0;
}

.exercise-item {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
    margin: 0.8rem 0;
}

/* Styles pour les exercices interactifs */
.section-tabs {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.section-tab {
    background: linear-gradient(135deg, #ff8c00 0%, #ff6347 100%);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 140, 0, 0.3);
}

.section-tab:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 140, 0, 0.4);
}

.section-tab.active {
    background: linear-gradient(135deg, rgba(255, 140, 0, 0.8), rgba(255, 99, 71, 0.8));
    box-shadow: 0 6px 20px rgba(255, 140, 0, 0.4);
}

.section-content {
    display: none;
    animation: fadeIn 0.5s ease-in;
}

.section-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.exercise-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.exercise-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 0;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    overflow: hidden;
    position: relative;
}

.exercise-card.easy {
    border-image: linear-gradient(135deg, #ff8c00 0%, #ff6347 100%) 1;
}

.exercise-card.medium {
    border-image: linear-gradient(135deg, #ff8c00 0%, #ff6347 100%) 1;
}

.exercise-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.exercise-content-wrapper {
    padding: 25px;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.difficulty-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
    margin-bottom: 15px;
    align-self: flex-start;
}

.difficulty-badge.easy {
    background: linear-gradient(135deg, #ff8c00 0%, #ff6347 100%);
    color: white;
}

.difficulty-badge.medium {
    background: linear-gradient(135deg, #ff8c00 0%, #ff6347 100%);
    color: white;
}

.exercise-card .exercise-title {
    color: #2d3748;
    font-size: 1.3em;
    font-weight: 700;
    margin-bottom: 15px;
    line-height: 1.3;
}

.exercise-card .exercise-content {
    color: #4a5568;
    line-height: 1.6;
    flex-grow: 1;
}

.exercise-card .exercise-content p {
    margin: 0;
}

.exercise-card .exercise-content code {
    background: rgba(102, 126, 234, 0.1);
    color: #667eea;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
    font-size: 0.9em;
}
</style>

<div class="course-header">
    <div class="course-title">📚 Traitement de données en tables</div>
    <div class="course-subtitle">Manipulation et analyse de fichiers CSV avec Python</div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Objectifs du cours</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Traitement de données</div>
        <div class="definition-content">
            Les <strong>dictionnaires</strong> de Python permettent de réaliser des traitements sur des données. Ces traitements permettent notamment de <strong>trier</strong>, <strong>organiser</strong>, <strong>sélectionner</strong> des données en fonction de critères.
        </div>
    </div>
    
    <div class="format-grid">
        <div class="format-card">
            <div class="format-card-title">📁 Fichiers CSV</div>
            <div class="format-card-content">
                Le format <strong>CSV</strong> (<em>Comma Separated Values</em>) correspond à un format où les données sont structurées par des <strong>virgules</strong> (ou des <strong>points-virgules</strong>).
            </div>
        </div>
        
        <div class="format-card">
            <div class="format-card-title">📊 Logiciels tableurs</div>
            <div class="format-card-content">
                Ces formats CSV sont manipulables via des logiciels <strong>tableurs</strong> (Excel, Libre Office etc...) mais on peut également réaliser des traitements sur ces fichiers à l'aide de bibliothèques <em>Python</em>.
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 La bibliothèque CSV</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Fonctionnement de la bibliothèque</div>
        <div class="definition-content">
            La bibliothèque <strong>csv</strong> permet de charger des fichiers et stocke les données sous forme de <strong>listes</strong>.
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-title">🔧 Fonction DictReader</div>
        <div class="fact-content">
            On ne traitera que de la fonction <strong>DictReader</strong> qui permet de traduire chaque ligne de notre fichier CSV dans des <strong>dictionnaires</strong>, eux mêmes stockés dans une <strong>liste</strong>.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">💡 Structure d'ouverture</div>
        <div class="info-content">
            Voici la structure de l'ouverture d'un fichier CSV et du remplissage d'une liste organisant nos données :
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔧 Code de base</div>
        <pre>
import csv

liste_a_remplir = []
with open('communes.csv', newline='') as fichier_csv:
   lecteur = csv.DictReader(fichier_csv, delimiter=',')   # Objet DictReader (itérateur)
   for ligne in lecteur:
      liste_a_remplir.append(dict(ligne))
        </pre>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">💡 Exemple pratique</h2>
    
    <div class="info-box">
        <div class="info-title">📁 Fichier d'exemple</div>
        <div class="info-content">
            Le fichier CSV <strong>commune.csv</strong> représente l'ensemble des communes de France, associée à leur code postal, département etc...
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-title">🔧 Fonction complète</div>
        <div class="fact-content">
            Pour "ouvrir" ce fichier CSV et structurer toutes les données le comportant, on utilisera l'exemple de code suivant :
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🏗️ Fonction de création de liste</div>
        <pre>
import csv

def creer_liste_villes(nom_de_fichier : str) -> list:
   villes = []
   with open('communes.csv', newline='') as fichier_csv:
      # Méthode DictReader qui permet de structurer les données contenues dans le fichier CSV 
      # en liste de dictionnaires où chaque descripteur (ou attribut) est renseigné.
      lecteur = csv.DictReader(fichier_csv, delimiter=';')   
      for ligne in lecteur:
         villes.append(dict(ligne))
        </pre>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📊 Descripteurs disponibles</div>
        <div class="definition-content">
            Pour ce fichier CSV, il y a les descripteurs suivants :<br>
            <strong>code_commune_INSEE, nom_commune_postal, code_postal, latitude, longitude, code_commune, nom_commune, nom_commune_complet, code_departement, nom_departement, code_region, nom_region</strong>
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">📄 Aperçu du fichier CSV</div>
        <pre>
code_commune_INSEE;nom_commune_postal;code_postal;latitude;longitude;code_commune;nom_commune;nom_departement
01001;L'Abergement-Clémenciat;01400;46.1667;4.9;1;L'Abergement-Clémenciat;Ain
01002;L'Abergement-de-Varey;01640;46.05;5.4833;1;L'Abergement-de-Varey;Ain
...
        </pre>
    </div>
    
    <div class="info-box">
        <div class="info-title">💡 Rappel important</div>
        <div class="info-content">
            La fonction <strong>DictReader</strong> permet de créer une liste de dictionnaires et chaque dictionnaire correspond à une ligne du fichier CSV à laquelle on associe chacun des attributs à chacune des valeurs de la ligne.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📊 Projection de données</h2>
    
    <div class="definition-box">
        <div class="definition-title">📋 Définition - Projection</div>
        <div class="definition-content">
            On appelle <strong>projection</strong> le fait d'obtenir les valeurs de certains ou tous les attributs d'une table / base de données / fichiers CSV.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">💻 Exemple en Python</div>
        <pre>
# Exemple : Afficher le nom des villes
for ligne in villes:  # Pour chaque ligne dans la liste des villes
   print(ligne["nom_commune"])  # Affiche la valeur associée à la clé 'nom_commune'

# Afficher le nom de toutes les villes
for ligne in villes:
   print(ligne["nom_commune"])

# Afficher le département de chaque ville
for ligne in villes:
   print("La ville ", ligne["nom_commune"], " est dans le département : ", ligne["nom_departement"])
        </pre>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            Cela permet donc d'obtenir dans notre exemple de villes, le nom de celle-ci, le département etc... de toutes les villes <strong>sans aucune contrainte</strong>.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🎯 Sélection de données</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Définition - Sélection</div>
        <div class="definition-content">
            On appelle <strong>sélection</strong> le fait de sélectionner des valeurs suivant certains critères ou condition.<br><br>
            Cela permet donc d'obtenir des informations ou de réaliser des traitements sur les données d'un fichier suivant divers critères (par exemple sur les villes).
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔧 Exemples de sélection</div>
        <pre>
# Afficher le nom des villes qui sont dans le département 59
for ligne in villes:
   if ligne['code_departement'] == '59':
      print(ligne["nom_commune"])

# Afficher les noms des villes commençant par la lettre C
for ligne in villes:
   if ligne["nom_commune"][0] == "C":
      print(ligne["nom_commune"])
        </pre>
    </div>
</div>

<script>
// JavaScript pour les fonctionnalités interactives des exercices
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
</script>

<div class="timeline-section">
    <h2 class="section-title">🎯 Exercices pratiques</h2>
    
    <div class="section-tabs">
        <button class="section-tab" onclick="showSection('easy-exercises')">🌟 Exercices faciles</button>
        <button class="section-tab" onclick="showSection('medium-exercises')">⚡ Exercices intermédiaires</button>
    </div>
    
    <div id="easy-exercises" class="section-content">
        <div class="exercise-cards">
            <div class="exercise-card easy">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge easy">Facile 🦊</div>
                    <h4 class="exercise-title">Afficher les noms des communes</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_noms_communes</code> qui prend une liste de dictionnaires <code>villes</code> en paramètre et affiche le nom de toutes les communes.</p>
                    </div>
                </div>
            </div>
            
            <div class="exercise-card easy">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge easy">Facile 🦊</div>
                    <h4 class="exercise-title">Communes par code postal</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_communes_par_code_postal</code> qui prend une liste de dictionnaires <code>villes</code> et une chaîne <code>code_postal</code> en paramètre, et affiche les noms des communes ayant ce code postal.</p>
                    </div>
                </div>
            </div>
            
            <div class="exercise-card easy">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge easy">Facile 🦊</div>
                    <h4 class="exercise-title">Communes avec coordonnées</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_communes_avec_coordonnees</code> qui prend une liste de dictionnaires <code>villes</code> en paramètre et affiche pour chaque commune son nom, sa latitude et sa longitude.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div id="medium-exercises" class="section-content">
        <div class="exercise-cards">
            <div class="exercise-card medium">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
                    <h4 class="exercise-title">Communes par département</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_communes_par_departement</code> qui prend une liste de dictionnaires <code>villes</code> et une chaîne <code>departement</code> en paramètre, et affiche les noms des communes du département donné.</p>
                    </div>
                </div>
            </div>
            
            <div class="exercise-card medium">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
                    <h4 class="exercise-title">Noms avec longueur minimale</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_noms_longueur_min</code> qui prend une liste de dictionnaires <code>villes</code> et un entier <code>longueur</code> en paramètre, et renvoie la liste des noms des communes ayant un nom d'au moins <code>longueur</code> caractères.</p>
                    </div>
                </div>
            </div>
            
            <div class="exercise-card medium">
                <div class="exercise-content-wrapper">
                    <div class="difficulty-badge medium">Intermédiaire 🦊🦊</div>
                    <h4 class="exercise-title">Communes par latitude</h4>
                    <div class="exercise-content">
                        <p>Écrire une fonction <code>afficher_communes_par_latitude</code> qui prend une liste de dictionnaires <code>villes</code> et une latitude maximale <code>max_latitude</code> en paramètre, et affiche les noms des communes ayant une latitude inférieure à <code>max_latitude</code>.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>