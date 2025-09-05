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

.property-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.property-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.property-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.property-name {
    font-weight: 600;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
    color: #2c3e50;
}

.property-values {
    font-size: 0.9rem;
    color: #7f8c8d;
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Dictionnaires en Python</h1>
    <p class="course-subtitle">Structures de données clé-valeur</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définition - Définitions</h2>
    
    <div class="definition-box">
        <div class="definition-title">📖 Le dictionnaire</div>
        <div class="definition-content">
            Une des nombreuses structures de Python est <strong>le dictionnaire</strong>.<br><br>
            Le dictionnaire est une structure de données qui n'est pas indexée mais organisée suivant des éléments que l'on nomme <strong>attributs (ou descripteur)</strong>.<br>
            Ces attributs correspondent à des <strong>propriétés</strong> sur l'élément que l'on souhaite modéliser.
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            <strong>💡 Exemple :</strong> On souhaite modéliser un modèle de voiture. Lors de la conception d'une voiture, on peut modifier des éléments pour en créer des déclinaisons.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">🚗 Propriétés d'un modèle de voiture</div>
        <div class="info-content">
            <div class="property-grid">
                <div class="property-card">
                    <div class="property-name">🎨 Couleurs</div>
                    <div class="property-values">rouge, bleu, vert, noir, blanc, gris</div>
                </div>
                <div class="property-card">
                    <div class="property-name">⚡ Motorisations (en ch)</div>
                    <div class="property-values">100, 110, 120, 200</div>
                </div>
                <div class="property-card">
                    <div class="property-name">🛞 Taille de jantes</div>
                    <div class="property-values">16, 17, 18, 19</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            Pour créer ce genre d'objets, on utilise donc la <strong>structure des dictionnaires</strong>.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Définition - Les dictionnaires en Python</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Syntaxe de création</div>
        <div class="definition-content">
            Pour créer un dictionnaire, on utilise les <strong>accolades {}</strong> (à la différence des tableaux (parenthèses <strong>(   )</strong>) ou des listes (crochets <strong>[   ]</strong>)).<br>
            À l'intérieur de ces accolades, on utilise la syntaxe <strong>attribut : valeurs possibles</strong>.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">📝 Caractéristiques des attributs</div>
        <div class="info-content">
            <ul>
                <li>Un <strong>attribut</strong> correspond à une propriété d'un objet que l'on cherche à modéliser</li>
                <li>Il est représenté par une <strong>chaîne de caractères</strong></li>
                <li>Les valeurs peuvent être de types <strong>simples</strong> (entier, chaînes de caractère, booléen) ou <strong>complexes</strong> (listes, dictionnaires, tuples)</li>
                <li>Chaque couple <em>attributs : valeurs</em> est séparé par des <strong>virgules</strong></li>
            </ul>
        </div>
    </div>
    
    <div class="highlight-fact">
        <div class="fact-content">
            De base, un dictionnaire lorsqu'on le crée de cette manière, est <strong>dépourvu d'attributs</strong>.<br>
            Pour créer un dictionnaire avec des attributs déjà connus, il existe <strong>deux méthodes</strong> :
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📋 Méthode 1 : Écrire les propriétés à l'instanciation</div>
        <div class="definition-content">
            <div class="code-example">
                <div class="code-title">💻 Code Python</div>
                <pre>
modele_voiture = {  "couleurs" : ["rouge", "bleu", "vert", "noir", "blanc", "gris"],
                    "motorisation_en_ch" : [100,110,120,200],
                    "taille_jantes" : [16,17,18,19]
                 }
                </pre>
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">📋 Méthode 2 : Rajouter petit à petit les propriétés</div>
        <div class="definition-content">
            <div class="code-example">
                <div class="code-title">💻 Code Python</div>
                <pre>
modele_voiture = {}

modele_voiture["couleurs"] = ["rouge", "bleu", "vert", "noir", "blanc", "gris"]
modele_voiture["motorisation_en_ch"] = [100,110,120,200]
modele_voiture["taille_jantes"] = [16,17,18,19]
                </pre>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔍 Accès et manipulation des dictionnaires</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔑 Accès aux attributs</div>
        <div class="definition-content">
            Pour accéder à un attribut du dictionnaire, on utilise la <strong>structure à crochets</strong> comme pour les listes, mais au lieu d'indiquer un indice, on indique l'<strong>attribut</strong> s'il est déjà renseigné.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">💻 Usage principal des dictionnaires</div>
        <div class="info-content">
            <div class="code-example">
                <div class="code-title">🔧 Opérations courantes</div>
                <pre>
# Pour afficher le dictionnaire complet
print(modele_voiture)

# Pour afficher les couleurs disponibles pour le modèle
print(modele_voiture["couleurs"])

# Pour rajouter des couleurs à celles existantes
modele_voiture["couleurs"] = modele_voiture["couleurs"] + ["beige"]

# Pour retirer une clef et ses valeurs d'un dictionnaire
modele_voiture.pop("taille_jantes")
                </pre>
            </div>
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">⚠️ Ajout de valeurs</div>
        <div class="info-content">
            Pour rajouter des valeurs à un attribut d'un dictionnaire, il faut bien faire attention aux <strong>types</strong>.<br><br>
            Par exemple, pour l'exemple précédent, nos valeurs étaient contenues dans des <strong>listes</strong>. Il faut donc opérer par concaténation de liste avec l'opérateur <strong>+</strong> ou la méthode <strong>.append(valeur)</strong>.
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">🔄 Opérations sur les dictionnaires</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔁 Itérations sur un dictionnaire</div>
        <div class="definition-content">
            Tout comme les listes et les tableaux, on peut itérer sur les valeurs d'un dictionnaire. Cela permet de retrouver des valeurs, de faire des traitements sur des bases de données ou retrouver des valeurs suivant certaines conditions.<br><br>
            Le plus simple est d'itérer à l'aide d'une boucle <strong>for</strong>.<br>
            Un dictionnaire est une structure sur laquelle on peut itérer sur les clefs (à l'instar des tuples ou listes où l'on itère sur les indices).
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔧 Itération sur les clefs et valeurs</div>
        <pre>
# Afficher les clefs du dictionnaire
for clef in modele_voiture:
    print(clef)

#Afficher toutes les valeurs d'un dictionnaire
for clef in modele_voiture:
    print(clef)
    for valeur in modele_voiture[clef]:
        print(valeur)
        </pre>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">✅ Vérification de la présence d'une clef</div>
        <div class="definition-content">
            L'opérateur <strong>in</strong> permet de vérifier si une clef existe dans le dictionnaire.
        </div>
    </div>
    
    <div class="code-example">
        <div class="code-title">🔍 Vérification d'existence</div>
        <pre>
if "couleurs" in modele_voiture:
    print("La clé 'couleurs' existe dans le dictionnaire")
else:
    print("La clé 'couleurs' n'existe pas dans le dictionnaire")
        </pre>
    </div>
    
    <div class="info-box">
        <div class="info-title">💡 Utilité pratique</div>
        <div class="info-content">
            Cela permet de savoir si, par exemple on modifie une base de données pour la rendre plus conséquente, la modification a bien été réalisée.
        </div>
    </div>
</div>