<style>
/* Styles modernes pour le cours Architecture d'une machine */
.course-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
}

.course-header h1 {
    margin: 0;
    font-size: 2.5rem;
    font-weight: 700;
}

.timeline-section {
    margin: 2rem 0;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.section-title {
    color: #667eea;
    font-size: 1.8rem;
    margin-bottom: 1rem;
    font-weight: 600;
}

.definition-box {
    background: rgba(102, 126, 234, 0.1);
    border-left: 4px solid #667eea;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.definition-title {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.definition-content {
    line-height: 1.6;
    color: #333;
}

.highlight-fact {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 4px solid #fdcb6e;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(253, 203, 110, 0.3);
}

.component-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.component-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(102, 126, 234, 0.2);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.component-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
}

.component-type {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 1rem;
    font-size: 1.1rem;
    border-bottom: 2px solid #667eea;
    padding-bottom: 0.5rem;
}

.memory-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.memory-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    padding: 1.2rem;
    border: 1px solid rgba(102, 126, 234, 0.15);
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.memory-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
}

.memory-type {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 0.8rem;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.bus-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.bus-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    padding: 1.2rem;
    border: 1px solid rgba(102, 126, 234, 0.15);
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.bus-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
}

.bus-type {
    font-weight: 600;
    color: #667eea;
    margin-bottom: 0.8rem;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.warning-box {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.warning-title {
    font-weight: 600;
    color: #e74c3c;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.info-box {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
    backdrop-filter: blur(5px);
}

.info-title {
    font-weight: 600;
    color: #3498db;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.cycle-steps {
    background: rgba(46, 204, 113, 0.1);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    border: 1px solid rgba(46, 204, 113, 0.3);
}

.cycle-step {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem 0;
    border-left: 4px solid #2ecc71;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.step-number {
    font-weight: 600;
    color: #2ecc71;
    margin-right: 0.5rem;
}

/* Responsive design */
@media (max-width: 768px) {
    .component-grid, .memory-grid, .bus-grid {
        grid-template-columns: 1fr;
    }
    
    .course-header h1 {
        font-size: 2rem;
    }
    
    .timeline-section {
        padding: 1rem;
    }
}
</style>

<div class="course-header">
    <h1>📚 💻 Architecture d'une machine : le modèle de Von Neumann</h1>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Définition et Histoire</h2>

    <div class="definition-box">
        <div class="definition-title">💻 Qu'est-ce qu'un ordinateur ?</div>
        <div class="definition-content">
            On définit un ordinateur comme étant une machine qui réalise des calculs de manière ordonnée (on parlait d'ordonnateur).
            <br/><br/>
            Il existe divers modèles pour créer des machines qui résolvent des calculs (comme la machine de Turing par exemple) mais celui qui a été retenu pour réaliser les machines que l'on utilise quotidiennement est celui de <strong>John Von Neumann</strong>.
        </div>
    </div>
    
    <div class="info-box">
        <div class="info-title">👨‍🔬 John Von Neumann</div>
        <div class="definition-content">
            John Von Neumann était un mathématicien de la fin du XIXe - début XXe siècle et son but était d'augmenter les puissances de calcul des machines déjà existantes à cause notamment de la seconde guerre mondiale.
            <br/><br/>
            Il reprend le modèle de calcul du projet <strong>EDVAC</strong> qui était une machine de calcul militaire (qui pouvait réaliser des opérations mathématiques en utilisant le binaire) mais y ajoute la notion de mémoire de programme pour créer son modèle.
        </div>
    </div>
    
    <div style="text-align: center; margin: 2rem 0;">
        <img src="edvac.jpeg" alt="Machine EDVAC" style="max-width: 100%; border-radius: 10px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);">
    </div>
    
    <div class="highlight-fact">
        🔄 <strong>Modèle séquentiel :</strong> Ce modèle réalise des calculs de manière séquentielle, ordonnée : on peut appeler ce modèle un <strong>modèle de calcul séquentiel</strong>.
    </div>
</div>

## 📖 🔧 Les composants du modèle de Von Neumann

Le modèle de Von Neumann est caractérisé par la présence de 4 composants notables.

### 🧮 UAL et UC

Le cerveau de la machine, les composants qui réalisent les calculs, résolvent les algorithmes et les ordonnent : **l'Unité Arithmético Logique** et **l'Unité de Contrôle**

L'Unité Arithmético-logique (ou UAL) est une unité de traitement qui sert à réaliser des calculs et opérations de base. Elle peut réaliser des opérations mathématiques, des opérations de logique, de comparaisons ou des décalages.  
L'UAL peut aussi contenir un ensemble d'espaces de données nommé **registres**.

Cette unité est composé de milliards de transistors qui sont des composants électroniques qui servent à réaliser notamment des opérations et comparaisons suivant la logique booléenne. Cet ensemble de transistor peut être appelé **circuit de portes logiques ou circuit logique**.

🎛️ L'Unité de contrôle comme son nom l'indique réalise la gestion des flux électriques provenant de la mémoire ou de l'Unité Arithmético-Logique.  
Elle permet de réaliser la séquence des opérations ; Elle est responsable de l'appellation de modèle séquentielle.

Cette Unité de Contrôle suit un cycle précis pour organiser les programmes.  
Il est composé de 3 étapes :

1. 🔄 L'UC récupère les instructions dans la mémoire. (Fetch)
2. 🔍 L'UC décode ces instructions en langage proche de la machine. (Decode)
3. ⚡ L'UC transmet l'instruction à l'UAL et celle-çi lui renvoie le résultat. (Execute)
4. 💾 L'UC transmet le résultat dans la mémoire. (Store)

Cet ensemble d'unité est ce que l'on appelle le **micro-processeur** ou communément le **processeur**.  
Il existe divers types de processeurs qui peuvent réaliser des opérations en "quasi simultané" et qui sont cadencés par des signaux d'horloges : on parle de **fréquence du processeur**.  
Cette fréquence est en général exprimée en *GHz* (prononcé *Giga-Hertz*).

![proco](intelamd.jpeg)

### 💾 La mémoire

Tous les calculs, opérations et programmes ont besoin de valeurs pour fonctionner ou doivent renvoyer et stocker des résultats pour les utiliser.  
Les machines ont aussi besoin de mémoire pour stocker de manière temporaire des variables de programmes ou de stockage à long terme pour enregistrer des fichers par exemple.

Il existe divers types de mémoire qui permettent le bon fonctionnement d'une machine.

#### ⚡ Le cache du processeur

Le cache du processeur est une mémoire d'accès très rapide, située entre le processeur et la RAM.  
Elle permet de stocker temporairement les instructions utilisées par le processeur pour éviter de tout le temps les calculer. Cela permet d'optimiser l'utilisation du processeur.

#### 🔄 La mémoire volatile (RAM)

La mémoire volatile ou mémoire **RAM (Random Access Memory)** correspond à la mémoire court terme de la machine.  
Cette mémoire n'est pas aussi conséquente qu'une mémoire de stockage mais possède des fréquences d'accès très rapides (de l'ordre du *GHz*).

Cette mémoire permet de stocker temporairement les données à des programmes en cours d'exécution.  
Le fait de stocker ces données dans la RAM (qui est une mémoire d'accès très rapide) permet au processeur d'accéder à des données très rapidement et de réaliser d'autant plus rapidement les diverses opérations.

#### 📀 La mémoire morte (ROM)

La mémoire ROM **(ou Read-Only Memory)** est une mémoire qui est non-volatile. Elle est conservée même lorsque la machine est éteinte. Elle contient les instructions nécessaires au démarrage de l'ordinateur (BIOS ou firmware).

#### 💿 La mémoire à long terme

La mémoire à long terme permet de stocker des données et des fichiers. Elle est celle qui correspond aux disques durs, clefs USB ou SSD.  
Elle permet de stocker le système d'exploitation, les applications ou les données (fichiers, programmes etc...).

### 🔌 Les bus et périphériques

On a vu précédemment l'utilité du processeur et de la mémoire mais comment tout cela interragit-il?

Les **bus** permettent de relier tous ces composants pour leur permettre de communiquer. Un bus au sens physique est un ensemble de câbles  
Il existe divers bus :

* 🎮 Bus de contrôle : Transfère les signaux de contrôle et de commande entre les composants.
* 📊 Bus de données : Transfère les données entre le processeur, la mémoire et les périphériques.
* 🔍 Bus d'adresses : Transfère les adresses mémoire ou des périphériques pour avoir accès aux diverses données nécessaires à l'exécution de la machine.

Les périphériques font aussi partie de la machine.  
Qu'ils soient d'entrée comme un clavier, un micro ou des capteures, de sortie comme des enceintes ou un écran, tous permettent de rajouter des fonctionnalités à une machine.

### ⚠️ La limite du modèle de Von Neumann

Ce modèle est un modèle efficace et qui a fait ses preuves depuis les années 70.  
Cependant il souffre d'un gros problème : la communication entre les divers composants.

Les composants ont tous des fréquences de fonctionnement ou des débits différents. Le modèle de Von Neumann est confronté à un problème de **goulots d'étranglements** (ou connu sous le nom de **bottleneck** en anglais).

🚰 On peut imager cela comme un système de plomberie.  
Imaginons en entrée un tube de 100mm de diamètre qui est alimenté de manière complète. Si celui-ci est suivi d'un tube de 40mm, cette portion va ralentir le debit global.  
Cela fonctionne pareil avec un ordinateur : si la mémoire fonctionne à une fréquence de 1 GHZ, le processeur à 1 GHz mais que les bus ne transmettent qu'à une fréquence de 20 MHz, l'ensemble de la machine sera ralenti.

🎮 *Pour ceux qui jouent sur PC:*  
Il peut arriver qu'il y ait un bottleneck entre le processeur et la carte graphique. Si l'un des deux composants est trop faible comparé à l'autre, il peut ralentir de manière globale les performances en jeu.