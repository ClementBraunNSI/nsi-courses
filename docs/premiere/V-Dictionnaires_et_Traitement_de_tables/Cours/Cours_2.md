<style>
/* Styles pour les cours avec système de cartes */

.course-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 100%;
}

.course-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 4px solid;
    width: 100%;
    max-width: 100%;
    margin: 1rem 0;
}

.course-card.definition {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.02) 100%);
}

.course-card.definition:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.course-card.example {
    border-left-color: #2196F3;
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.02) 100%);
}

.course-card.example:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
}

.course-card.warning {
    border-left-color: #F44336;
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.02) 100%);
}

.course-card.warning:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(244, 67, 54, 0.3);
}

.course-card.tip {
    border-left-color: #FF9800;
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.02) 100%);
}

.course-card.tip:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);
}

.course-card.highlight {
    border-left-color: #9C27B0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.05) 0%, rgba(156, 39, 176, 0.02) 100%);
}

.course-card.highlight:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(156, 39, 176, 0.3);
}

.course-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.course-content {
    margin-bottom: 1rem;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.badge.definition {
    background: rgba(76, 175, 80, 0.15);
    color: #4CAF50;
}

.badge.example {
    background: rgba(33, 150, 243, 0.15);
    color: #2196F3;
}

.badge.warning {
    background: rgba(244, 67, 54, 0.15);
    color: #F44336;
}

.badge.tip {
    background: rgba(255, 152, 0, 0.15);
    color: #FF9800;
}

.badge.highlight {
    background: rgba(156, 39, 176, 0.15);
    color: #9C27B0;
}

.btn {
    background: white;
    color: #4169E1;
    border: 2px solid #4169E1;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    text-decoration: none;
}

.btn:hover {
    background: rgba(65, 105, 225, 0.1);
    border-color: #1E90FF;
    color: #1E90FF;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(65, 105, 225, 0.4);
}

.exercise-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.math-container {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.table tr:hover {
    background: #f8f9fa;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #d63384;
}

pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre code {
    background: none;
    padding: 0;
    color: #495057;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-weight: 600;
}
</style>

# 📚 Traitement de données en tables

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Objectifs</h3>
        <div class="course-content">
            Les dictionnaires de Python permettent de réaliser des traitements sur des données. Ces traitements permettent notamment de trier, organiser, sélectionenr des données en fonction de critères.<br><br>Il existe un bon nombre de manières de structurer des données en informatique, celle qui nous sera utile sera permise grâce aux fichiers <strong>CSV</strong>.<br><br>Le format CSV (*Comma Separated Values*) correspond à un format où les données sont structurées par des virgules (ou des points-virgules).<br><br>Ces formats CSV sont manipulables via des logiciels <strong>tableurs</strong> (Excel, Libre Office etc...) mais on peut également réaliser des traitements sur ces fichiers à l'aide de bibliothèques *Python*.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">La bibliothèque `CSV`</h3>
        <div class="course-content">
            La bibliothèque <code>csv</code> permet de charger des fichiers et stocke les données sous forme de listes.<br><br>On ne traitera que de la fonction <code>DictReader</code> qui permet de traduire chaque ligne de notre fichier CSV dans des dictionnaires, eux mêmes stockés dans une liste.<br><br>Voici la structure de l'ouverture d'un fichier CSV et du remplissage d'une liste organisant nos données.<br><br>``<code>python<br>import csv<br><br>liste_a_remplir = []<br>with open('communes.csv', newline='') as fichier_csv:<br>   lecteur = csv.DictReader(fichier_csv, delimiter=',')   # Objet DictReader (itérateur)<br>   for ligne in lecteur:<br>      liste_a_remplir.append(dict(ligne))<br></code>`<code><br><br>### Exemple<br><br>Le fichier CSV [commune.csv](./communes.csv) représente l'ensemble des communes de France, associée à leur code postal, département etc...<br><br>Pour "ouvrir" ce fichier </code>csv<code> et structurer toutes les données le comportant, on utilisera un exemple de code ci-dessus.<br><br>On aurait<br><br></code>`<code>python<br>import csv<br><br>def creer_liste_villes(nom_de_fichier : str) -> list:<br>   villes = []<br>   with open('communes.csv', newline='') as fichier_csv:<br>      # Méthode DictReader qui permet de structurer les données contenues dans le fichier CSV en liste de dictionnaires <br>      # où chaque descripteur (ou attribut) est renseigné.<br>      lecteur = csv.DictReader(fichier_csv, delimiter=';')   <br>      for ligne in lecteur:<br>         villes.append(dict(ligne))<br></code>`<code><br><br>Pour ce fichier CSV, il y a les descripteurs suivant (description exhaustive): </code>code_commune_INSEE,nom_commune_postal,code_postal,latitude,longitude,code_commune,nom_commune,nom_commune_complet,code_departement,nom_departement,code_region,nom_region<code>.<br><br></code>`<code><br>code_commune_INSEE;nom_commune_postal;code_postal;latitude;longitude;code_commune;nom_commune;nom_departement<br>01001;L'Abergement-Clémenciat;01400;46.1667;4.9;1;L'Abergement-Clémenciat;Ain<br>01002;L'Abergement-de-Varey;01640;46.05;5.4833;1;L'Abergement-de-Varey;Ain<br>...<br></code>`<code><br>Grâce à tous ces descripteurs, on peut afficher les lignes de nos fichiers CSV suivant différents critères.<br><br>*Rappel, la fonction DictReader permet de créer une liste de dictionnaires et chaque dictionnaire correspond à une ligne du fichier CSV à laquelle on associe chacun des attributs à chacune des valeurs de la ligne.*<br><br>On appelle <strong>projection</strong> le fait d'obtenir les valeurs de certains ou tous les attributs d'une table / base de données / fichiers CSV.<br><br><br>*Exemple en python*<br><br></code>`<code>python<br><br>   # Exemple : Afficher le nom des villes<br>   for ligne in villes:  # Pour chaque ligne dans la liste des villes<br>      print(ligne["nom_commune"])  # Affiche la valeur associée à la clé 'nom_commune'<br><br>   # Afficher le nom de toutes les villes<br>   for ligne in villes:<br>      print(ligne["nom_commune"])<br><br>   # Afficher le département de chaque ville<br>   for ligne in villes:<br>      print("La ville ", ligne["nom_commune"], " est dans le département : ", ligne["nom_departement"])<br></code>`<code><br><br>Cela permet donc d'obtenir dans notre exemple de villes, le nom de celle-ci, le département etc... de toutes les villes <strong>sans aucune contrainte</strong>.<br><br>___<br><br>On appelle <strong>sélection</strong> le fait de sélectionner des valeurs suivant certains critères ou condition.<br><br>Cela permet donc d'obtenir des informations ou de réaliser des traitements sur les données d'un fichier suivant divers critères (par exemple sur les villes).<br><br></code>`<code>python<br>   <br>   # Afficher le nom des villes qui sont dans le département 59<br>   for ligne in villes:<br>      if ligne['code_departement'] == '59':<br>         print(ligne["nom_commune"])<br><br>   # Afficher les noms des villes commençant par la lettre C<br><br>   for ligne in villes:<br>      if ligne["nom_commune"][0] == "C":<br>         print(ligne["nom_commune"])<br></code>`<code><br><br><br>### <strong>Exercices faciles</strong><br><br>1. <strong>Écrire une fonction </code>afficher_noms_communes<code> qui prend une liste de dictionnaires </code>villes<code> en paramètre et affiche le nom de toutes les communes.</strong><br><br>2. <strong>Écrire une fonction </code>afficher_communes_par_code_postal<code> qui prend une liste de dictionnaires </code>villes<code> et une chaîne </code>code_postal<code> en paramètre, et affiche les noms des communes ayant ce code postal.</strong><br><br>3. <strong>Écrire une fonction </code>afficher_communes_avec_coordonnees<code> qui prend une liste de dictionnaires </code>villes<code> en paramètre et affiche pour chaque commune son nom, sa latitude et sa longitude.</strong><br><br>---<br><br>### <strong>Exercices intermédiaires</strong><br><br>1. <strong>Écrire une fonction </code>afficher_communes_par_departement<code> qui prend une liste de dictionnaires </code>villes<code> et une chaîne </code>departement<code> en paramètre, et affiche les noms des communes du département donné.</strong><br><br>2. <strong>Écrire une fonction </code>afficher_noms_longueur_min<code> qui prend une liste de dictionnaires </code>villes<code> et un entier </code>longueur<code> en paramètre, et renvoie la liste des noms des communes ayant un nom d'au moins </code>longueur<code> caractères.</strong><br><br>3. <strong>Écrire une fonction </code>afficher_communes_par_latitude<code> qui prend une liste de dictionnaires </code>villes<code> et une latitude maximale </code>max_latitude<code> en paramètre, et affiche les noms des communes ayant une latitude inférieure à </code>max_latitude`.</strong>
        </div>
    </div>
    
</div>