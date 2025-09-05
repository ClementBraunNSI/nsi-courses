<style>
/* Styles modernes pour le cours Entiers Binaires et Hexadécimaux */
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
    <h1 class="course-title">📚 💻 Architecture d'une machine : le modèle de Von Neumann</h1>
    <p class="course-subtitle">Comprendre les fondements de l'architecture informatique moderne</p>
</div>

<div class="timeline-section">
    <h2 class="section-title">📚 Définition et Histoire</h2>

    <div class="definition-box">
        <div class="definition-title">🎯 Qu'est-ce qu'un ordinateur ?</div>
        <div class="definition-content">
            On définit un ordinateur comme étant une machine qui réalise des calculs de manière ordonnée (on parlait d'ordonnateur). Il existe divers modèles pour créer des machines qui résolvent des calculs (comme la machine de Turing par exemple) mais celui qui a été retenu pour réaliser les machines que l'on utilise quotidiennement est celui de <strong>John Von Neumann</strong>.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">👨‍🔬</div>
            <div class="model-name">John Von Neumann</div>
            <div class="model-description">
                Mathématicien de la fin du XIXe - début XXe siècle dont le but était d'augmenter les puissances de calcul des machines déjà existantes à cause notamment de la seconde guerre mondiale.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🖥️</div>
            <div class="model-name">Projet EDVAC</div>
            <div class="model-description">
                Il reprend le modèle de calcul du projet <strong>EDVAC</strong> qui était une machine de calcul militaire (qui pouvait réaliser des opérations mathématiques en utilisant le binaire) mais y ajoute la notion de mémoire de programme pour créer son modèle.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Modèle séquentiel</div>
            <div class="model-description">
                Ce modèle réalise des calculs de manière séquentielle, ordonnée : on peut appeler ce modèle un <strong>modèle de calcul séquentiel</strong>.
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🖼️ <strong>Image historique :</strong> ![edvac](edvac.jpeg)
    </div>
</div>

<div class="timeline-section">
    <h2 class="section-title">📖 🔧 Les composants du modèle de Von Neumann</h2>
    
    <div class="definition-box">
        <div class="definition-title">🏗️ Architecture fondamentale</div>
        <div class="definition-content">
            Le modèle de Von Neumann est caractérisé par la présence de <strong>4 composants notables</strong>.
        </div>
    </div>

    <h3 class="section-title">🧮 UAL et UC</h3>
    
    <div class="definition-box">
        <div class="definition-title">🧠 Le cerveau de la machine</div>
        <div class="definition-content">
            Les composants qui réalisent les calculs, résolvent les algorithmes et les ordonnent : <strong>l'Unité Arithmético Logique</strong> et <strong>l'Unité de Contrôle</strong>
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🧮</div>
            <div class="model-name">Unité Arithmético-Logique (UAL)</div>
            <div class="model-description">
                Unité de traitement qui sert à réaliser des calculs et opérations de base. Elle peut réaliser des opérations mathématiques, des opérations de logique, de comparaisons ou des décalages. L'UAL peut aussi contenir un ensemble d'espaces de données nommé <strong>registres</strong>.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔌</div>
            <div class="model-name">Transistors</div>
            <div class="model-description">
                Cette unité est composée de milliards de transistors qui sont des composants électroniques qui servent à réaliser notamment des opérations et comparaisons suivant la logique booléenne. Cet ensemble de transistor peut être appelé <strong>circuit de portes logiques ou circuit logique</strong>.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎛️</div>
            <div class="model-name">Unité de Contrôle (UC)</div>
            <div class="model-description">
                Comme son nom l'indique, elle réalise la gestion des flux électriques provenant de la mémoire ou de l'Unité Arithmético-Logique. Elle permet de réaliser la séquence des opérations ; Elle est responsable de l'appellation de modèle séquentielle.
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🔄 Cycle de l'Unité de Contrôle</div>
        <div class="definition-content">
            Cette Unité de Contrôle suit un cycle précis pour organiser les programmes. Il est composé de 4 étapes :
            <br><br>
            <strong>1. 🔄 Fetch :</strong> L'UC récupère les instructions dans la mémoire.<br>
            <strong>2. 🔍 Decode :</strong> L'UC décode ces instructions en langage proche de la machine.<br>
            <strong>3. ⚡ Execute :</strong> L'UC transmet l'instruction à l'UAL et celle-ci lui renvoie le résultat.<br>
            <strong>4. 💾 Store :</strong> L'UC transmet le résultat dans la mémoire.
        </div>
    </div>
    
    <div class="highlight-fact">
        💻 <strong>Le Processeur :</strong> Cet ensemble d'unité est ce que l'on appelle le <strong>micro-processeur</strong> ou communément le <strong>processeur</strong>. Il existe divers types de processeurs qui peuvent réaliser des opérations en "quasi simultané" et qui sont cadencés par des signaux d'horloges : on parle de <strong>fréquence du processeur</strong>. Cette fréquence est en général exprimée en <em>GHz</em> (prononcé <em>Giga-Hertz</em>).
    </div>
    
    <div class="highlight-fact">
        🖼️ <strong>Image :</strong> ![proco](intelamd.jpeg)
    </div>

    <h3 class="section-title">💾 La mémoire</h3>
    
    <div class="definition-box">
        <div class="definition-title">💾 Qu'est-ce que la mémoire ?</div>
        <div class="definition-content">
            Tous les calculs, opérations et programmes ont besoin de valeurs pour fonctionner ou doivent renvoyer et stocker des résultats pour les utiliser. Les machines ont aussi besoin de mémoire pour stocker de manière temporaire des variables de programmes ou de stockage à long terme pour enregistrer des fichers par exemple.
            <br><br>
            Il existe divers types de mémoire qui permettent le bon fonctionnement d'une machine.
        </div>
    </div>

    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">⚡</div>
            <div class="model-name">Cache du processeur</div>
            <div class="model-description">
                Le cache du processeur est une mémoire d'accès très rapide, située entre le processeur et la RAM. Elle permet de stocker temporairement les instructions utilisées par le processeur pour éviter de tout le temps les calculer. Cela permet d'optimiser l'utilisation du processeur.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🔄</div>
            <div class="model-name">Mémoire volatile (RAM)</div>
            <div class="model-description">
                La mémoire volatile ou mémoire <strong>RAM (Random Access Memory)</strong> correspond à la mémoire court terme de la machine. Cette mémoire n'est pas aussi conséquente qu'une mémoire de stockage mais possède des fréquences d'accès très rapides (de l'ordre du <em>GHz</em>).
                <br><br>
                Cette mémoire permet de stocker temporairement les données à des programmes en cours d'exécution. Le fait de stocker ces données dans la RAM permet au processeur d'accéder à des données très rapidement.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📀</div>
            <div class="model-name">Mémoire morte (ROM)</div>
            <div class="model-description">
                La mémoire ROM <strong>(ou Read-Only Memory)</strong> est une mémoire qui est non-volatile. Elle est conservée même lorsque la machine est éteinte. Elle contient les instructions nécessaires au démarrage de l'ordinateur (BIOS ou firmware).
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">💿</div>
            <div class="model-name">Mémoire à long terme</div>
            <div class="model-description">
                La mémoire à long terme permet de stocker des données et des fichiers. Elle est celle qui correspond aux disques durs, clefs USB ou SSD. Elle permet de stocker le système d'exploitation, les applications ou les données (fichiers, programmes etc...).
            </div>
        </div>
    </div>

    <h3 class="section-title">🔌 Les bus et périphériques</h3>
    
    <div class="definition-box">
        <div class="definition-title">🔌 Les bus</div>
        <div class="definition-content">
            Les <strong>bus</strong> sont des ensembles de fils électriques qui permettent de faire circuler l'information entre les différents composants de l'ordinateur.
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">📊</div>
            <div class="model-name">Bus de données</div>
            <div class="model-description">
                Transporte les données entre les composants
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📍</div>
            <div class="model-name">Bus d'adresses</div>
            <div class="model-description">
                Indique où les données doivent être lues ou écrites
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎛️</div>
            <div class="model-name">Bus de contrôle</div>
            <div class="model-description">
                Transporte les signaux de contrôle (lecture, écriture, etc.)
            </div>
        </div>
    </div>
    
    <div class="definition-box">
        <div class="definition-title">🖥️ Les périphériques</div>
        <div class="definition-content">
            Les <strong>périphériques</strong> sont des composants externes qui permettent d'interagir avec l'ordinateur :
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">⌨️</div>
            <div class="model-name">Périphériques d'entrée</div>
            <div class="model-description">
                Clavier, souris, microphone, caméra
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🖨️</div>
            <div class="model-name">Périphériques de sortie</div>
            <div class="model-description">
                Écran, imprimante, haut-parleurs
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">📱</div>
            <div class="model-name">Périphériques d'entrée/sortie</div>
            <div class="model-description">
                Écran tactile, disque dur externe
            </div>
        </div>
    </div>
    
    <div class="highlight-fact">
        🖼️ <strong>Image :</strong> ![bus](bus.png)
    </div>

</div>

<div class="timeline-section">
    <h3 class="section-title">⚠️ La limite du modèle de Von Neumann</h3>
    
    <div class="definition-box">
        <div class="definition-title">⚠️ Problème principal</div>
        <div class="definition-content">
            Ce modèle est un modèle efficace et qui a fait ses preuves depuis les années 70. Cependant il souffre d'un gros problème : la communication entre les divers composants.
            <br><br>
            Les composants ont tous des fréquences de fonctionnement ou des débits différents. Le modèle de Von Neumann est confronté à un problème de <strong>goulots d'étranglements</strong> (ou connu sous le nom de <strong>bottleneck</strong> en anglais).
        </div>
    </div>
    
    <div class="model-grid">
        <div class="model-card">
            <div class="model-icon">🚰</div>
            <div class="model-name">Analogie de la plomberie</div>
            <div class="model-description">
                On peut imager cela comme un système de plomberie. Imaginons en entrée un tube de 100mm de diamètre qui est alimenté de manière complète. Si celui-ci est suivi d'un tube de 40mm, cette portion va ralentir le debit global.
                <br><br>
                Cela fonctionne pareil avec un ordinateur : si la mémoire fonctionne à une fréquence de 1 GHZ, le processeur à 1 GHz mais que les bus ne transmettent qu'à une fréquence de 20 MHz, l'ensemble de la machine sera ralenti.
            </div>
        </div>
        
        <div class="model-card">
            <div class="model-icon">🎮</div>
            <div class="model-name">Exemple concret : Gaming PC</div>
            <div class="model-description">
                <em>Pour ceux qui jouent sur PC :</em>
                <br><br>
                Il peut arriver qu'il y ait un bottleneck entre le processeur et la carte graphique. Si l'un des deux composants est trop faible comparé à l'autre, il peut ralentir de manière globale les performances en jeu.
            </div>
        </div>
    </div>
</div>