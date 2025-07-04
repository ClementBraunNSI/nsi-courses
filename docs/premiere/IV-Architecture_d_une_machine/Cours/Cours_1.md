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

# 📚 💻 Architecture d'une machine : le modèle de Von Neumann

<div class="course-container">
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">📚 Définition et Histoire</h3>
        <div class="course-content">
            On définit un ordinateur comme étant une machine qui réalise des calculs de manière ordonnée (on parlait d'ordonnateur).<br>Il existe divers modèles pour créer des machines qui résolvent des calculs (comme la machine de Turing par exemple) mais celui qui a été retenu pour réaliser les machines que l'on utilise quotidiennement est celui de John Von Neumann.<br><br>👨‍🔬 John Von Neumann était un mathématicien de la fin du XIXe - début XXe siècle et son but était d'augmenter les puissances de calcul des machines déjà existantes à cause notamment de la seconde guerre mondiale.<br><br>Il reprend le modèle de calcul du projet <strong>EDVAC</strong> qui était une machine de calcul militaire (qui pouvait réaliser des opérations mathématiques en utilisant le binaire) mais y ajoute la notion de mémoire de programme pour créer son modèle.<br><br>![edvac](edvac.jpeg)<br><br>Ce modèle réalise des calculs de manière séquentielle, ordonnée : on peut appeler ce modèle un <strong>modèle de calcul séquentiel</strong>.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">🔧 Les composants du modèle de Von Neumann</h3>
        <div class="course-content">
            Le modèle de Von Neumann est caractérisé par la présence de 4 composants notables.<br><br>### 🧮 UAL et UC<br><br>Le cerveau de la machine, les composants qui réalisent les calculs, résolvent les algorithmes et les ordonnent : <strong>l'Unité Arithmético Logique</strong> et <strong>l'Unité de Contrôle</strong><br><br>L'Unité Arithmético-logique (ou UAL) est une unité de traitement qui sert à réaliser des calculs et opérations de base. Elle peut réaliser des opérations mathématiques, des opérations de logique, de comparaisons ou des décalages.<br>L'UAL peut aussi contenir un ensemble d'espaces de données nommé <strong>registres</strong>.<br><br>Cette unité est composé de milliards de transistors qui sont des composants électroniques qui servent à réaliser notamment des opérations et comparaisons suivant la logique booléenne. Cet ensemble de transistor peut être appelé <strong>circuit de portes logiques ou circuit logique</strong>.<br><br>🎛️ L'Unité de contrôle comme son nom l'indique réalise la gestion des flux électriques provenant de la mémoire ou de l'Unité Arithmético-Logique.<br>Elle permet de réaliser la séquence des opérations ; Elle est responsable de l'appellation de modèle séquentielle.<br><br>Cette Unité de Contrôle suit un cycle précis pour organiser les programmes.<br>Il est composé de 3 étapes :<br><br>1. 🔄 L'UC récupère les instructions dans la mémoire. (Fetch)<br>2. 🔍 L'UC décode ces instructions en langage proche de la machine. (Decode)<br>3. ⚡ L'UC transmet l'instruction à l'UAL et celle-çi lui renvoie le résultat. (Execute)<br>4. 💾 L'UC transmet le résultat dans la mémoire. (Store)<br><br>Cet ensemble d'unité est ce que l'on appelle le <strong>micro-processeur</strong> ou communément le <strong>processeur</strong>.<br>Il existe divers types de processeurs qui peuvent réaliser des opérations en "quasi simultané" et qui sont cadencés par des signaux d'horloges : on parle de <strong>fréquence du processeur</strong>.<br>Cette fréquence est en général exprimée en *GHz* (prononcé *Giga-Hertz*).<br><br>![proco](intelamd.jpeg)<br><br>### 💾 La mémoire<br><br>Tous les calculs, opérations et programmes ont besoin de valeurs pour fonctionner ou doivent renvoyer et stocker des résultats pour les utiliser. <br>Les machines ont aussi besoin de mémoire pour stocker de manière temporaire des variables de programmes ou de stockage à long terme pour enregistrer des fichers par exemple.<br><br>Il existe divers types de mémoire qui permettent le bon fonctionnement d'une machine.<br><br>#### ⚡ Le cache du processeur<br><br>Le cache du processeur est une mémoire d'accès très rapide, située entre le processeur et la RAM.<br>Elle permet de stocker temporairement les instructions utilisées par le processeur pour éviter de tout le temps les calculer. Cela permet d'optimiser l'utilisation du processeur.<br><br>#### 🔄 La mémoire volatile (RAM)<br><br>La mémoire volatile ou mémoire <strong>RAM (Random Access Memory)</strong> correspond à la mémoire court terme de la machine.<br>Cette mémoire n'est pas aussi conséquente qu'une mémoire de stockage mais possède des fréquences d'accès très rapides (de l'ordre du *GHz*).<br><br>Cette mémoire permet de stocker temporairement les données à des programmes en cours d'exécution.<br>Le fait de stocker ces données dans la RAM (qui est une mémoire d'accès très rapide) permet au processeur d'accéder à des données très rapidement et de réaliser d'autant plus rapidement les diverses opérations.<br><br>#### 📀 La mémoire morte (ROM)<br><br>La mémoire ROM <strong>(ou Read-Only Memory)</strong> est une mémoire qui est non-volatile. Elle est conservée même lorsque la machine est éteinte. Elle contient les instructions nécessaires au démarrage de l'ordinateur (BIOS ou firmware).<br><br>#### 💿 La mémoire à long terme<br><br>La mémoire à long terme permet de stocker des données et des fichiers. Elle est celle qui correspond aux disques durs, clefs USB ou SSD.<br>Elle permet de stocker le système d'exploitation, les applications ou les données (fichiers, programmes etc...).<br><br>### 🔌 Les bus et périphériques<br><br>On a vu précédemment l'utilité du processeur et de la mémoire mais comment tout cela interragit-il?<br><br>Les <strong>bus</strong> permettent de relier tous ces composants pour leur permettre de communiquer. Un bus au sens physique est un ensemble de câbles<br>Il existe divers bus :<br><br>* 🎮 Bus de contrôle : Transfère les signaux de contrôle et de commande entre les composants.<br>* 📊 Bus de données : Transfère les données entre le processeur, la mémoire et les périphériques.<br>* 🔍 Bus d'adresses : Transfère les adresses mémoire ou des périphériques pour avoir accès aux diverses données nécessaires à l'exécution de la machine.<br><br>Les périphériques font aussi partie de la machine.<br>Qu'ils soient d'entrée comme un clavier, un micro ou des capteures, de sortie comme des enceintes ou un écran, tous permettent de rajouter des fonctionnalités à une machine.<br>  <br>### ⚠️ La limite du modèle de Von Neumann<br><br>Ce modèle est un modèle efficace et qui a fait ses preuves depuis les années 70.<br>Cependant il souffre d'un gros problème : la communication entre les divers composants.<br><br>Les composants ont tous des fréquences de fonctionnement ou des débits différents. Le modèle de Von Neumann est confronté à un problème de <strong>goulots d'étranglements</strong> (ou connu sous le nom de <strong>bottleneck</strong> en anglais).<br><br>🚰 On peut imager cela comme un système de plomberie.<br>Imaginons en entrée un tube de 100mm de diamètre qui est alimenté de manière complète. Si celui-ci est suivi d'un tube de 40mm, cette portion va ralentir le debit global. <br>Cela fonctionne pareil avec un ordinateur : si la mémoire fonctionne à une fréquence de 1 GHZ, le processeur à 1 GHz mais que les bus ne transmettent qu'à une fréquence de 20 MHz, l'ensemble de la machine sera ralenti.<br><br>🎮 *Pour ceux qui jouent sur PC:*<br>Il peut arriver qu'il y ait un bottleneck entre le processeur et la carte graphique. Si l'un des deux composants est trop faible comparé à l'autre, il peut ralentir de manière globale les performances en jeu.
        </div>
    </div>
    
</div>