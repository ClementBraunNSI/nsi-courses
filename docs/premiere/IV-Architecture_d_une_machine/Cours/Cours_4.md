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

# 📚 Ludopédagogie : Redstone dans Minecraft

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Pourquoi Minecraft ?</h3>
        <div class="course-content">
            Minecraft est un jeu vidéo sorti en 2009 qui met le joueur dans un mode en 3D créé aléatoirement en utilisant la méthode procédurale.<br><br>Pour faire court, la génération d'un monde Minecraft est aléatoire grâce à du pseudo-aléatoire au niveau de la création des terrains en utilisant un outil mathématique appelé le <strong>bruit de Perlin</strong>.<br><br>Le bruit de Perlin est une méthode mathématique utilisée pour générer des paysages réalistes dans les jeux vidéo, comme Minecraft. Il permet de créer des terrains qui semblent naturels, avec des montagnes, des vallées, et d’autres variations progressives.<br><br>Dans Minecraft, le bruit de Perlin est utilisé pour :<br>    - Simuler les reliefs des terrains (collines, montagnes).<br>    - Répartir les biomes (déserts, forêts, océans) en répartissant l'humidité et la température.<br>    - Générer des variations progressives et cohérentes dans le monde.<br><br>!!! note Bruit de Perlin<br>    Cette technique fonctionne en générant des “grilles” de valeurs qui sont mélangées et interpolées pour créer des transitions progressives. Cela permet de créer des terrains où une montagne peut doucement devenir une plaine, au lieu d’avoir des changements brusques.<br><br>Minecraft est un jeu particulier car il met le joueur dans un monde composé de <strong>*voxels</strong>* qui ne sont que des pixels dans un univers en 3 dimensions (pixels étant un élément dans un univers de 2 dimensions).<br><br>De plus, ce jeu ayant reçu énormément d'évolutions depuis, a rajouté une mécanique assez novatrice qu'est la <strong>redstone</strong>.<br><br>La redstone (ou poudre rouge en français) permet de simuler des circuits électriques et de réaliser des opérations logiques.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">La notion de Turing-complet</h3>
        <div class="course-content">
            Un système est dit Turing-complet s’il peut exécuter tous les calculs possibles qu’un ordinateur peut réaliser, à condition de disposer de suffisamment de temps et de mémoire. Cela signifie qu’il peut simuler une machine théorique appelée machine de Turing.<br><br>Minecraft et la redstone sont considérés comme Turing-complets car il est possible, avec les composants du jeu (poudre de redstone, torches, leviers, etc.), de construire des circuits logiques capables d’effectuer des calculs complexes. Par exemple, il est possible de :<br>    - Réaliser des additions ou des multiplications.<br>    - Créer des mémoires pour stocker des données.<br>    - Construire un ordinateur entier dans Minecraft capable de jouer à Minecraft !<br><br>!!! tip Pourquoi est-ce important ?<br>    Être Turing-complet signifie que Minecraft avec la redstone peut être utilisé pour simuler n’importe quel calcul ou programme, tout comme un vrai ordinateur.<br><br>!!! note Notion de Turing-Complet<br>    La notion de Turing-complet est liée à l’idée de simuler une machine de Turing, un modèle théorique de calcul inventé par Alan Turing. Ce modèle, à proprement parler, n’est pas au programme du lycée, mais il est intéressant de savoir que Minecraft peut être aussi puissant, en théorie, qu’un ordinateur moderne.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Composants de redstone</h3>
        <div class="course-content">
            Il existe un bon nombre de composants en redstone mais uniquement 5 composants seront necessaires pour ce TD.<br><br>| Composant          | Image | Explication                                                                                                                                                                                            |<br>|--------------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|<br>| Poudre de redstone |       | La poudre de redstone est l'élément principal des circuits. Elle permet de réaliser tous les tracés et de relier les composants à l'instar d'un cable de cuivre ou d'un tracé fait sur une carte-mère. |<br>| Répéteur de redstone |      | Le répéteur de redstone permet de redonner de l'intensité au tracé de poudre de redstone créé. En effet, comme pour un vrai câble électrique, on peut retrouver des déperditions lors de longues distances.|<br>| Lampe de redstone | | Comme son nom l'indique, la lampe de redstone est une représentation d'une ampoule que l'on peut relier à une platine comme lors des simulations de circuits électroniques au collège. Elle s'allume si elle reçoit un courant en entrée. Elle nous servira à analyser les résultats lors des tests.|<br>| Torche de redstone |       | La torche de redstone permet d'alimenter un circuit.|<br>| Leviers ou boutons |       | Ces composants permettent au joueur de manipuler les entrées du circuits en leur donnant un état fixe (levier) ou temporaire (bouton).|
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Objectifs de la séance</h3>
        <div class="course-content">
            L'objectif principal de la séance est la réalisation de circuits logiques dans Minecraft. Cela permet de se rendre compte de la difficulté de créer des circuits logiques compacts et qui sont entièrement fonctionnels (c'est à dire sans court-circuits par exemple).<br><br>Il faudra ainsi savoir créer les différentes portes logiques vues dans les cours précédents (AND, OR, NOT) et de les mettre ensemble pour recréer des circuits logiques analysés dans les exercices.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Portes logiques dans Minecraft</h3>
        <div class="course-content">
            Il est possible de réaliser toutes les portes logiques dans Minecraft.<br><br>Pour se faire, il existe une mécanique importante dans Minecraft : l'inversion grâce à un bloc.<br><br>En adossant ou en posant une torche de redstone sur un bloc, si ce bloc reçoit en entrée un courant, celle-ci permet d'inverser le courant (comme une porte NOT).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Exercices</h3>
        <div class="course-content">
            !!! redstone_exo Porte NOT<br><br>    - Placez un levier, un bloc et une torche de redstone.<br>    - Reliez une lampe au circuit.<br><br>!!! redstone_exo Porte AND<br><br>    - Placez deux leviers comme entrées.<br>    - Reliez-les à un circuit qui inclut deux torches de redstone sur 3 blocs et une poudre entre les deux pour relier les deux torches.<br>    - Ajoutez une troisième torche sur un bloc pour produire la sortie.<br>    - <strong>Question :</strong> Quand la lampe s’allume-t-elle ?<br><br>!!! redstone_exo Porte OR<br><br>    - Placez deux leviers.<br>    - Reliez-les à un circuit commun avec de la poudre de redstone.<br>    - Ajoutez une lampe en sortie.<br>    - <strong>Question :</strong> Quand la lampe s’allume-t-elle ?<br><br>---
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Circuits combinés</h3>
        <div class="course-content">
            !!! redstone_exo Porte NAND<br>    La porte NAND correspond à <strong>l'inverse d'une porte AND</strong>.<br>    - Une lampe de redstone reliée à une porte NAND s’éteint uniquement si <strong>au moins une entrée est allumée</strong>, sinon s'allume.<br>    - <strong>Consigne :</strong><br>      1. Construisez une porte AND.<br>      2. Retirez la torche de redstone sur le bloc de sortie pour inverser le signal.<br><br>---<br><br>!!! redstone_exo Porte XOR<br>    La porte XOR correspond au <strong>ou exclusif</strong>.<br>    - Une lampe de redstone reliée à une porte XOR est une porte correspondant au <strong>ou exclusif</strong> : elle s'éteint si <strong>toutes les entrées sont activées ou fermées</strong> mais s'allume si une seule est activée.<br>    - <strong>Consigne :</strong><br>      1. Déduire le schéma logique sur papier.<br>      2. Réaliser la construction en jeu.<br><br>---<br><br>!!! redstone_exo "Schéma combiné"<br>    Réaliser les schémas logiques des expressions booléennes suivantes (indication : chacune des entrées A, B et C sont des leviers ou des boutons):<br>    - A <strong>and</strong> <strong>not</strong> B<br>    - A <strong>or</strong> C <strong>and</strong> <strong>B</strong>
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Pour aller plus loin : Défis avancés</h3>
        <div class="course-content">
            !!! redstone_exo Demi Additionneur<br><br>    Un demi-additionneur produit deux sorties :<br>    - <strong>Somme (S)</strong> : s’allume si une seule des deux entrées est activée (utilisez une porte XOR).<br>    - <strong>Retenue (R)</strong> : s’allume si <strong>les deux</strong> entrées sont activées (utilisez une porte AND).<br>    - <strong>Consigne :</strong> Construisez un circuit avec deux leviers comme entrées, une lampe pour la somme, et une autre lampe pour la retenue.<br><br>    <strong>Aide:</strong><br><br>    Voici le schéma logique d'un demi-additionneur : <br><br>    ![demi-additionneur](./demi-additionneur.png)
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Correction</h3>
        <div class="course-content">
            Pour réaliser le demi-additionneur, il faudra que vous ayiez réussi à construire les deux portes précédentes.<br>Si besoin, voila la correction :<br><br>![Correction de l'exercice](http://www.minecraft101.net/redstone/redstone-logic.html)
        </div>
    </div>
    
</div>