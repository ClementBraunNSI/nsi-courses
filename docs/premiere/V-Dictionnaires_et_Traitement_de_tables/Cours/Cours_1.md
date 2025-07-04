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

# 📚 Dictionnaires en Python

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définitions</h3>
        <div class="course-content">
            Une des nombreuses structures de Python est <strong>le dictionnaire</strong>.<br><br>Le dictionnaire est une structure de données qui n'est pas indexée mais organisées suivant des éléments que l'on nomme <strong>attributs (ou descripteur)</strong>.<br>Ces attributs correspondent à des propriétés sur l'élément que l'on souhaite modéliser.<br><br>*Exemple*:<br>Par exemple, on souhaite modéliser un modèle de voiture. Lors de la conception d'une voiture, on peut modifier des éléments pour en créer des déclinaisons.<br>On peut, pour un modèle, dresser un tableau des diverses propriétés à modéliser :<br><br>|propriété|valeurs possibles|<br>|---------|-----------------|<br>|couleurs | rouge, bleu, vert, noir, blanc, gris|<br>|motorisations (en ch)| 100, 110,120,200|<br>|taille de jantes|16,17,18,19|<br><br>Pour créer ce genre d'objets, on utilise donc la structure des dictionnaires.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les dictionnaires en Python</h3>
        <div class="course-content">
            Pour créer un dictionnaire, on utilise les accolades <strong>{}</strong> (à la différence des tableaux (parenthèses <strong>(   )</strong>) ou des listes (crochets <strong>[   ]</strong>)).<br>À l'intérieur de ces accolades, on utilise la syntaxe <strong>attribut : valeurs possibles</strong>.<br><br>Un attribut correspond donc à une propriété d'un objet que l'on cherche à modéliser et est représenté par une chaîne de caractères.<br><br>Les différentes valeurs possibles peuvent être de types simples (entier, chaines de caractère, booléen) mais aussi de types plus complèxes (listes, dictionnaires ou tuples).<br><br>Chacun des couples *attributs : valeurs* sont séparés par des virgules.<br><br>De base, un dictionnaire lorsqu'on le créée de cette manière, est dépourvu d'attributs.<br>Pour créer un dictionnaire avec des attributs déjà connus, il existe deux méthodes :<br><br><strong>Écrire les propriétés déjà connues à l'instanciation</strong><br><br>``<code>python<br>modele_voiture = {  "couleurs" : ["rouge", "bleu", "vert", "noir", "blanc", "gris"],<br>                    "motorisation_en_ch" : [100,110,120,200],<br>                    "taille_jantes" : [16,17,18,19]<br>                 }<br></code>`<code><br><br><strong>Rajouter petit à petit les propriétés</strong><br><br></code>`<code>python<br>modele_voiture = {}<br><br>modele_voiture["couleurs"] = ["rouge", "bleu", "vert", "noir", "blanc", "gris"]<br>modele_voiture["motorisation_en_ch"] = [100,110,120,200]<br>modele_voiture["taille_jantes"] = [16,17,18,19]<br></code>`<code><br><br>Pour accéder à un attribut du dictionnaire, on utilise la structure à crochets comme pour les listes, mais au lieu d'indiquer un indice, on indique l'attribut s'il est déjà renseigné.<br><br>Voici l'usage principal des dictionnaires en Python : <br><br></code>`<code>python<br># Pour afficher le dictionnaire complet<br>print(modele_voiture)<br><br># Pour afficher les couleurs disponibles pour le modèle<br>print(modele_voiture["couleurs"])<br><br># Pour rajouter des couleurs à celles existantes<br>modele_voiture["couleurs"] = modele_voiture["couleurs"] + ["beige"]<br><br># Pour retirer une clef et ses valeurs d'un dictionnaire<br>modele_voiture.pop("taille_jantes")<br></code>`<code><br><br>!!! Warning Ajout de valeurs<br>    Pour rajouter des valeurs à un attribut d'un dictionnaire, il faut bien faire attention aux types.<br>    Par exemple, pour l'exemple précédent, nos valeurs étaient contenues dans des listes. Il faut donc opérer par concaténation de liste avec l'opérateur <strong>+</strong> ou la méthode </code>.append(valeur)`.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Opérations sur les dictionnaires</h3>
        <div class="course-content">
            ### Itérations sur un dictionnaire<br><br>Tout comme les listes et les tableaux, on peut itérer sur les valeurs d'un dictionnaire. Cela permet de retrouver des valeurs, de faire des traitements sur des bases de données ou retrouver des valeurs suivant certaines conditions.<br><br>Le plus simple est d'itérer à l'aide d'une boucle <code>for</code>.<br>Un dictionnaire est une structure sur laquelle on peut itérer sur les clefs (à l'instar des tuples ou listes où l'on itère sur les indices).<br><br>``<code>python<br>    # Afficher les clefs du dictionnaire<br>    for clef in modele_voiture:<br>        print(clef)<br><br>    #Afficher toutes les valeurs d'un dictionnaire<br>    for clef in modele_voiture:<br>        print(clef)<br>        for valeur in modele_voiture[clef]:<br>            print(valeur)<br></code>`<code><br><br>### Vérification de la présence d'une clef<br><br>L'opérateur </code>in<code> permet de vérifier si une clef existe dans le dictionnaire.<br><br></code>`<code>python<br>    if "couleurs" in modele_voiture:<br>        print("La clé 'couleurs' existe dans le dictionnaire")<br>    else:<br>        print("La clé 'couleurs' n'existe pas dans le dictionnaire")<br></code>``<br><br>Cela permet de savoir si, par exemple on modifie une base de données pour la rendre plus conséquente, la modification a bien été réalisée.
        </div>
    </div>
    
</div>