<style>
/* Styles modernes pour le cours Architecture d'une machine */
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

.model-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.model-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.model-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.model-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.model-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.model-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
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

.method-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.method-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.method-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.method-type {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 1rem;
    text-align: center;
}

.conversion-table {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(102, 126, 234, 0.2);
    overflow-x: auto;
}

.conversion-table table {
    width: 100%;
    border-collapse: collapse;
}

.conversion-table th {
    background: #667eea;
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 600;
}

.conversion-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(102, 126, 234, 0.1);
    text-align: center;
}

.conversion-table tr:hover {
    background: rgba(102, 126, 234, 0.05);
}

.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
    border-left: 5px solid #667eea;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

@media (max-width: 768px) {
    .course-title {
        font-size: 2rem;
    }
    
    .model-grid {
        grid-template-columns: 1fr;
    }
    
    .method-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header {
        padding: 2rem;
    }
}
</style>

<div class="course-header">
    <h1 class="course-title">📚 Ludopédagogie : Redstone dans Minecraft</h1>
    <p class="course-subtitle">Chapitre IV - Architecture d'une machine</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Pourquoi Minecraft ?</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎮 Minecraft</div>
        <div class="definition-content">
            Minecraft est un jeu vidéo sorti en 2009 qui met le joueur dans un mode en 3D créé aléatoirement en utilisant la méthode procédurale.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🌍</div>
            <div class="model-name">Bruit de Perlin</div>
            <div class="model-description">
                Pour faire court, la génération d'un monde Minecraft est aléatoire grâce à du pseudo-aléatoire au niveau de la création des terrains en utilisant un outil mathématique appelé le <strong>bruit de Perlin</strong>.
                <br><br>
                Le bruit de Perlin est une méthode mathématique utilisée pour générer des paysages réalistes dans les jeux vidéo, comme Minecraft. Il permet de créer des terrains qui semblent naturels, avec des montagnes, des vallées, et d'autres variations progressives.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📦</div>
            <div class="model-name">Voxels</div>
            <div class="model-description">
                Minecraft est un jeu particulier car il met le joueur dans un monde composé de <strong>voxels</strong> qui ne sont que des pixels dans un univers en 3 dimensions (pixels étant un élément dans un univers de 2 dimensions).
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔴</div>
            <div class="model-name">Redstone</div>
            <div class="model-description">
                De plus, ce jeu ayant reçu énormément d'évolutions depuis, a rajouté une mécanique assez novatrice qu'est la <strong>redstone</strong>.
                <br><br>
                La redstone (ou poudre rouge en français) permet de simuler des circuits électriques et de réaliser des opérations logiques.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🌄 <strong>Utilisation du bruit de Perlin :</strong> Dans Minecraft, le bruit de Perlin est utilisé pour simuler les reliefs des terrains (collines, montagnes), répartir les biomes (déserts, forêts, océans) en répartissant l'humidité et la température, et générer des variations progressives et cohérentes dans le monde.
    </div>
    
    <div class="info-box">
        💡 <strong>Note : Bruit de Perlin</strong><br>
        Cette technique fonctionne en générant des "grilles" de valeurs qui sont mélangées et interpolées pour créer des transitions progressives. Cela permet de créer des terrains où une montagne peut doucement devenir une plaine, au lieu d'avoir des changements brusques.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 La notion de Turing-complet</h2>
    
    <div class="definition-box">
        <div class="definition-title">🧠 Système Turing-complet</div>
        <div class="definition-content">
            Un système est dit Turing-complet s'il peut exécuter tous les calculs possibles qu'un ordinateur peut réaliser, à condition de disposer de suffisamment de temps et de mémoire. Cela signifie qu'il peut simuler une machine théorique appelée machine de Turing.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🎮</div>
            <div class="model-name">Minecraft et la Redstone</div>
            <div class="model-description">
                Minecraft et la redstone sont considérés comme Turing-complets car il est possible, avec les composants du jeu (poudre de redstone, torches, leviers, etc.), de construire des circuits logiques capables d'effectuer des calculs complexes.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⚡</div>
            <div class="model-name">Capacités de calcul</div>
            <div class="model-description">
                Par exemple, il est possible de :
                <br>• Réaliser des additions ou des multiplications.
                <br>• Créer des mémoires pour stocker des données.
                <br>• Construire un ordinateur entier dans Minecraft capable de jouer à Minecraft !
            </div>
        </div>
    </div>
    
    <div class="info-box">
        💡 <strong>Astuce : Pourquoi est-ce important ?</strong><br>
        Être Turing-complet signifie que Minecraft avec la redstone peut être utilisé pour simuler n'importe quel calcul ou programme, tout comme un vrai ordinateur.
    </div>
    
    <div class="highlight-fact">
        🔬 <strong>Note : Notion de Turing-Complet</strong> La notion de Turing-complet est liée à l'idée de simuler une machine de Turing, un modèle théorique de calcul inventé par Alan Turing. Ce modèle, à proprement parler, n'est pas au programme du lycée, mais il est intéressant de savoir que Minecraft peut être aussi puissant, en théorie, qu'un ordinateur moderne.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Composants de redstone</h2>
    
    <div class="info-box">
        Il existe un bon nombre de composants en redstone mais uniquement 5 composants seront nécessaires pour ce TD.
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🔴</div>
            <div class="model-name">Poudre de redstone</div>
            <div class="model-description">
                La poudre de redstone est l'élément principal des circuits. Elle permet de réaliser tous les tracés et de relier les composants à l'instar d'un câble de cuivre ou d'un tracé fait sur une carte-mère.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Répéteur de redstone</div>
            <div class="model-description">
                Le répéteur de redstone permet de redonner de l'intensité au tracé de poudre de redstone créé. En effet, comme pour un vrai câble électrique, on peut retrouver des déperditions lors de longues distances.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">💡</div>
            <div class="model-name">Lampe de redstone</div>
            <div class="model-description">
                Comme son nom l'indique, la lampe de redstone est une représentation d'une ampoule que l'on peut relier à une platine comme lors des simulations de circuits électroniques au collège. Elle s'allume si elle reçoit un courant en entrée. Elle nous servira à analyser les résultats lors des tests.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔥</div>
            <div class="model-name">Torche de redstone</div>
            <div class="model-description">
                La torche de redstone permet d'alimenter un circuit.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎛️</div>
            <div class="model-name">Leviers ou boutons</div>
            <div class="model-description">
                Ces composants permettent au joueur de manipuler les entrées du circuits en leur donnant un état fixe (levier) ou temporaire (bouton).
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Objectifs de la séance</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Objectif principal</div>
        <div class="definition-content">
            L'objectif principal de la séance est la réalisation de circuits logiques dans Minecraft. Cela permet de se rendre compte de la difficulté de créer des circuits logiques compacts et qui sont entièrement fonctionnels (c'est à dire sans court-circuits par exemple).
        </div>
    </div>
    
    <div class="info-box">
        🔧 <strong>Compétences à développer :</strong> Il faudra ainsi savoir créer les différentes portes logiques vues dans les cours précédents (AND, OR, NOT) et de les mettre ensemble pour recréer des circuits logiques analysés dans les exercices.
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Portes logiques dans Minecraft</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚡ Réalisation des portes logiques</div>
        <div class="definition-content">
            Il est possible de réaliser toutes les portes logiques dans Minecraft.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Mécanique d'inversion</div>
            <div class="model-description">
                Pour se faire, il existe une mécanique importante dans Minecraft : l'inversion grâce à un bloc.
                <br><br>
                En adossant ou en posant une torche de redstone sur un bloc, si ce bloc reçoit en entrée un courant, celle-ci permet d'inverser le courant (comme une porte NOT).
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Exercices</h2>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🚫</div>
            <div class="model-name">Porte NOT</div>
            <div class="model-description">
                • Placez un levier, un bloc et une torche de redstone.<br>
                • Reliez une lampe au circuit.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔗</div>
            <div class="model-name">Porte AND</div>
            <div class="model-description">
                • Placez deux leviers comme entrées.<br>
                • Reliez-les à un circuit qui inclut deux torches de redstone sur 3 blocs et une poudre entre les deux pour relier les deux torches.<br>
                • Ajoutez une troisième torche sur un bloc pour produire la sortie.<br>
                <br>
                <div class="info-box">
                    ❓ <strong>Question :</strong> Quand la lampe s'allume-t-elle ?
                </div>
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔀</div>
            <div class="model-name">Porte OR</div>
            <div class="model-description">
                • Placez deux leviers.<br>
                • Reliez-les à un circuit commun avec de la poudre de redstone.<br>
                • Ajoutez une lampe en sortie.<br>
                <br>
                <div class="info-box">
                    ❓ <strong>Question :</strong> Quand la lampe s'allume-t-elle ?
                </div>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Circuits combinés</h2>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🚫🔗</div>
            <div class="model-name">Porte NAND</div>
            <div class="model-description">
                La porte NAND correspond à <strong>l'inverse d'une porte AND</strong>.
                <br><br>
                • Une lampe de redstone reliée à une porte NAND s'éteint uniquement si <strong>au moins une entrée est allumée</strong>, sinon s'allume.
                <br><br>
                <div class="info-box">
                    📋 <strong>Consigne :</strong><br>
                    1. Construisez une porte AND.<br>
                    2. Retirez la torche de redstone sur le bloc de sortie pour inverser le signal.
                </div>
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">⚡</div>
            <div class="model-name">Porte XOR</div>
            <div class="model-description">
                La porte XOR correspond au <strong>ou exclusif</strong>.
                <br><br>
                • Une lampe de redstone reliée à une porte XOR est une porte correspondant au <strong>ou exclusif</strong> : elle s'éteint si <strong>toutes les entrées sont activées ou fermées</strong> mais s'allume si une seule est activée.
                <br><br>
                <div class="info-box">
                    📋 <strong>Consigne :</strong><br>
                    1. Déduire le schéma logique sur papier.<br>
                    2. Réaliser la construction en jeu.
                </div>
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Schéma combiné</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔧 Expressions booléennes</div>
        <div class="definition-content">
            Réaliser les schémas logiques des expressions booléennes suivantes (indication : chacune des entrées A, B et C sont des leviers ou des boutons):
            <br><br>
            • A <strong>and</strong> <strong>not</strong> B<br>
            • A <strong>or</strong> C <strong>and</strong> <strong>B</strong>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Pour aller plus loin : Défis avancés</h2>
    
    <div class="definition-box">
        <div class="definition-title">🧮 Demi Additionneur</div>
        <div class="definition-content">
            Un demi additionneur est un circuit logique qui permet d'additionner deux bits.
            <br><br>
            Il prend en entrée deux bits A et B et produit en sortie :
            <br>
            • La somme S (bit de poids faible)<br>
            • La retenue C (carry, bit de poids fort)
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">📐</div>
            <div class="model-name">Schéma logique</div>
            <div class="model-description">
                • S = A XOR B<br>
                • C = A AND B
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎯</div>
            <div class="model-name">Consigne</div>
            <div class="model-description">
                Réaliser un demi additionneur dans Minecraft avec deux leviers en entrée (A et B) et deux lampes en sortie (S et C).
            </div>
        </div>
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 Correction</h2>
    
    <div class="highlight-fact">
        📚 Vous pouvez retrouver les corrections des exercices sur cette ressource externe : <a href="http://www.minecraft101.net/redstone/redstone-logic.html">Lien vers la correction</a>
    </div>
</div>