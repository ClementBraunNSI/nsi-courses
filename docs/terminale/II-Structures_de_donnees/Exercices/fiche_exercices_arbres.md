<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercices - Arbres</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f7fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }
        
        .header p {
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 1.1em;
        }
        
        .section-tabs {
            display: flex;
            background-color: #f8f9fa;
            border-bottom: 1px solid #dee2e6;
            overflow-x: auto;
        }
        
        .section-tab {
            padding: 15px 25px;
            cursor: pointer;
            border: none;
            background: none;
            font-size: 16px;
            font-weight: 500;
            color: #6c757d;
            transition: all 0.3s ease;
            white-space: nowrap;
            border-bottom: 3px solid transparent;
        }
        
        .section-tab:hover {
            background-color: #e9ecef;
            color: #495057;
        }
        
        .section-tab.active {
            color: #667eea;
            border-bottom-color: #667eea;
            background-color: white;
        }
        
        .section-content {
            display: none;
            padding: 30px;
        }
        
        .exercise-cards {
            display: grid;
            gap: 20px;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        }
        
        .exercise-card {
            border: 2px solid #e9ecef;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s ease;
            background: white;
        }
        
        .exercise-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .exercise-card.intro {
            border-left: 5px solid #17a2b8;
        }
        
        .exercise-card.intro:hover {
            border-color: #138496;
            box-shadow: 0 10px 25px rgba(23,162,184,0.2);
        }
        
        .exercise-card.easy {
            border-left: 5px solid #28a745;
        }
        
        .exercise-card.easy:hover {
            border-color: #1e7e34;
            box-shadow: 0 10px 25px rgba(40,167,69,0.2);
        }
        
        .exercise-card.medium {
            border-left: 5px solid #ffc107;
        }
        
        .exercise-card.medium:hover {
            border-color: #d39e00;
            box-shadow: 0 10px 25px rgba(255,193,7,0.2);
        }
        
        .exercise-card.hard {
            border-left: 5px solid #dc3545;
        }
        
        .exercise-card.hard:hover {
            border-color: #bd2130;
            box-shadow: 0 10px 25px rgba(220,53,69,0.2);
        }
        
        .exercise-card.expert {
            border-left: 5px solid #6f42c1;
        }
        
        .exercise-card.expert:hover {
            border-color: #59359a;
            box-shadow: 0 10px 25px rgba(111,66,193,0.2);
        }
        
        .exercise-content-wrapper {
            padding: 25px;
        }
        
        .difficulty-badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 15px;
        }
        
        .difficulty-badge.intro {
            background-color: #d1ecf1;
            color: #0c5460;
        }
        
        .difficulty-badge.easy {
            background-color: #d4edda;
            color: #155724;
        }
        
        .difficulty-badge.medium {
            background-color: #fff3cd;
            color: #856404;
        }
        
        .difficulty-badge.hard {
            background-color: #f8d7da;
            color: #721c24;
        }
        
        .difficulty-badge.expert {
            background-color: #e2d9f3;
            color: #4a2c6a;
        }
        
        .exercise-title {
            margin: 0 0 15px 0;
            color: #2c3e50;
            font-size: 1.4em;
            font-weight: 600;
        }
        
        .exercise-content {
            color: #555;
            margin-bottom: 20px;
        }
        
        .exercise-content ul, .exercise-content ol {
            padding-left: 20px;
        }
        
        .exercise-content li {
            margin-bottom: 8px;
        }
        
        .toggle-solution {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .toggle-solution:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102,126,234,0.4);
        }
        
        .toggle-solution .arrow {
            transition: transform 0.3s ease;
        }
        
        .solution-wrapper {
            display: none;
        }
        
        .solution {
            background-color: #f8f9fa;
            border-top: 1px solid #dee2e6;
            padding: 25px;
        }
        
        .solution h4 {
            color: #495057;
            margin-top: 0;
        }
        
        .solution pre {
            background-color: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 14px;
            line-height: 1.5;
        }
        
        .solution code {
            font-family: 'Fira Code', 'Consolas', monospace;
        }
        
        .solution-modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            animation: fadeIn 0.3s ease;
        }
        
        .solution-content {
            background-color: white;
            margin: 2% auto;
            padding: 0;
            border-radius: 10px;
            width: 90%;
            max-width: 1000px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            animation: slideIn 0.3s ease;
        }
        
        .solution-close {
            position: absolute;
            top: 15px;
            right: 25px;
            color: #aaa;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            z-index: 1001;
        }
        
        .solution-close:hover {
            color: #000;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background-color: #f8f9fa;
            font-weight: 600;
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin: 15px 0;
            border-radius: 4px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🌳 Exercices - Arbres</h1>
        <p>Structures hiérarchiques et algorithmes de parcours</p>
    </div>
    
    <div class="section-tabs">
        <button class="section-tab active" onclick="showSection('concepts')">Concepts de base</button>
        <button class="section-tab" onclick="showSection('implementation')">Implémentation</button>
        <button class="section-tab" onclick="showSection('parcours')">Parcours</button>
        <button class="section-tab" onclick="showSection('abr')">Arbres binaires de recherche</button>
        <button class="section-tab" onclick="showSection('applications')">Applications</button>
    </div>

<div id="concepts-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card intro">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge intro">Introduction 🔵</div>
            <h4 class="exercise-title">Vocabulaire des arbres</h4>
            <div class="exercise-content">
                <p>Maîtrisez le vocabulaire fondamental des arbres.</p>
                <p><strong>À faire :</strong></p>
                <ul>
                    <li>Définir : nœud, racine, feuille, parent, enfant, ancêtre, descendant</li>
                    <li>Expliquer : hauteur, profondeur, niveau, degré d'un nœud</li>
                    <li>Distinguer : arbre binaire, arbre binaire complet, arbre binaire parfait</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Vocabulaire des arbres :</h4>
                
                <h5>Définitions de base :</h5>
                <ul>
                    <li><strong>Nœud</strong> : Élément de l'arbre contenant une valeur</li>
                    <li><strong>Racine</strong> : Nœud au sommet de l'arbre (pas de parent)</li>
                    <li><strong>Feuille</strong> : Nœud sans enfants</li>
                    <li><strong>Parent</strong> : Nœud directement au-dessus d'un autre</li>
                    <li><strong>Enfant</strong> : Nœud directement en-dessous d'un autre</li>
                    <li><strong>Ancêtre</strong> : Nœud sur le chemin de la racine au nœud</li>
                    <li><strong>Descendant</strong> : Nœud accessible en descendant</li>
                </ul>
                
                <h5>Mesures :</h5>
                <ul>
                    <li><strong>Hauteur</strong> : Distance maximale de la racine aux feuilles</li>
                    <li><strong>Profondeur d'un nœud</strong> : Distance de la racine à ce nœud</li>
                    <li><strong>Niveau</strong> : Ensemble des nœuds à même profondeur</li>
                    <li><strong>Degré d'un nœud</strong> : Nombre d'enfants du nœud</li>
                </ul>
                
                <h5>Types d'arbres binaires :</h5>
                <ul>
                    <li><strong>Arbre binaire</strong> : Chaque nœud a au plus 2 enfants</li>
                    <li><strong>Arbre binaire complet</strong> : Tous les niveaux sont remplis sauf le dernier (rempli de gauche à droite)</li>
                    <li><strong>Arbre binaire parfait</strong> : Tous les niveaux sont complètement remplis</li>
                </ul>
                
                <div class="highlight">
                    <strong>Exemple :</strong> Un arbre de hauteur 3 peut contenir au maximum 2³ - 1 = 7 nœuds (arbre parfait).
                </div>
            </div>
        </div>
    </div>

    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🟢</div>
            <h4 class="exercise-title">Propriétés des arbres binaires</h4>
            <div class="exercise-content">
                <p>Calculez les propriétés d'arbres binaires donnés.</p>
                <p><strong>Exercices :</strong></p>
                <ol>
                    <li>Pour un arbre binaire parfait de hauteur h, combien de nœuds ?</li>
                    <li>Pour un arbre binaire de n nœuds, quelle hauteur minimale et maximale ?</li>
                    <li>Combien de feuilles maximum dans un arbre binaire de hauteur h ?</li>
                    <li>Relation entre nombre de feuilles et nœuds internes ?</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Propriétés des arbres binaires :</h4>
                
                <h5>1. Arbre binaire parfait de hauteur h :</h5>
                <p><strong>Nombre de nœuds = 2^h - 1</strong></p>
                <ul>
                    <li>Niveau 0 (racine) : 1 nœud = 2^0</li>
                    <li>Niveau 1 : 2 nœuds = 2^1</li>
                    <li>Niveau k : 2^k nœuds</li>
                    <li>Total : 1 + 2 + 4 + ... + 2^(h-1) = 2^h - 1</li>
                </ul>
                
                <h5>2. Arbre binaire de n nœuds :</h5>
                <ul>
                    <li><strong>Hauteur minimale</strong> : ⌈log₂(n+1)⌉ (arbre complet)</li>
                    <li><strong>Hauteur maximale</strong> : n (arbre dégénéré = liste chaînée)</li>
                </ul>
                
                <h5>3. Feuilles maximum :</h5>
                <p><strong>2^(h-1) feuilles</strong> dans un arbre binaire parfait de hauteur h</p>
                
                <h5>4. Relation feuilles/nœuds internes :</h5>
                <p>Dans un arbre binaire : <strong>nb_feuilles = nb_nœuds_internes + 1</strong></p>
                
                <pre><code class="language-python"># Vérification avec du code
def proprietes_arbre_binaire(h):
    """Calcule les propriétés d'un arbre binaire parfait"""
    nb_noeuds = 2**h - 1
    nb_feuilles = 2**(h-1)
    nb_internes = nb_noeuds - nb_feuilles
    
    print(f"Arbre binaire parfait de hauteur {h}:")
    print(f"  Nombre de nœuds: {nb_noeuds}")
    print(f"  Nombre de feuilles: {nb_feuilles}")
    print(f"  Nombre de nœuds internes: {nb_internes}")
    print(f"  Vérification: {nb_feuilles} = {nb_internes} + 1 ? {nb_feuilles == nb_internes + 1}")

# Tests
for h in range(1, 5):
    proprietes_arbre_binaire(h)
    print()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Analyse d'arbres</h4>
            <div class="exercise-content">
                <p>Analysez des arbres binaires représentés sous différentes formes.</p>
                <p><strong>Données :</strong></p>
                <ul>
                    <li>Représentation par parenthésage : (A (B (D) (E)) (C (F)))</li>
                    <li>Parcours préfixe : A B D E C F</li>
                    <li>Parcours infixe : D B E A F C</li>
                </ul>
                <p><strong>Questions :</strong></p>
                <ol>
                    <li>Dessinez l'arbre correspondant</li>
                    <li>Calculez sa hauteur et le nombre de nœuds</li>
                    <li>Identifiez les feuilles et nœuds internes</li>
                    <li>Donnez le parcours postfixe</li>
                </ol>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <h4>Analyse de l'arbre :</h4>
                
                <h5>1. Structure de l'arbre :</h5>
                <pre><code>        A
       / \
      B   C
     / \   \
    D   E   F</code></pre>
                
                <h5>2. Propriétés :</h5>
                <ul>
                    <li><strong>Hauteur</strong> : 3 (A→B→D ou A→B→E ou A→C→F)</li>
                    <li><strong>Nombre de nœuds</strong> : 6</li>
                    <li><strong>Feuilles</strong> : D, E, F (3 feuilles)</li>
                    <li><strong>Nœuds internes</strong> : A, B, C (3 nœuds internes)</li>
                </ul>
                
                <h5>3. Vérification des parcours :</h5>
                <ul>
                    <li><strong>Préfixe (racine-gauche-droite)</strong> : A B D E C F ✓</li>
                    <li><strong>Infixe (gauche-racine-droite)</strong> : D B E A F C ✓</li>
                    <li><strong>Postfixe (gauche-droite-racine)</strong> : D E B F C A</li>
                </ul>
                
                <pre><code class="language-python"># Reconstruction de l'arbre à partir des parcours
def reconstruire_arbre(prefixe, infixe):
    """Reconstruit un arbre à partir des parcours préfixe et infixe"""
    if not prefixe or not infixe:
        return None
    
    # La racine est le premier élément du parcours préfixe
    racine = prefixe[0]
    
    # Trouver la position de la racine dans le parcours infixe
    pos_racine = infixe.index(racine)
    
    # Diviser les parcours pour les sous-arbres gauche et droit
    infixe_gauche = infixe[:pos_racine]
    infixe_droit = infixe[pos_racine + 1:]
    
    prefixe_gauche = prefixe[1:1 + len(infixe_gauche)]
    prefixe_droit = prefixe[1 + len(infixe_gauche):]
    
    # Construire récursivement les sous-arbres
    return {
        'valeur': racine,
        'gauche': reconstruire_arbre(prefixe_gauche, infixe_gauche),
        'droit': reconstruire_arbre(prefixe_droit, infixe_droit)
    }

def parcours_postfixe(arbre):
    """Effectue un parcours postfixe"""
    if arbre is None:
        return []
    
    resultat = []
    resultat.extend(parcours_postfixe(arbre['gauche']))
    resultat.extend(parcours_postfixe(arbre['droit']))
    resultat.append(arbre['valeur'])
    
    return resultat

# Test avec notre exemple
prefixe = ['A', 'B', 'D', 'E', 'C', 'F']
infixe = ['D', 'B', 'E', 'A', 'F', 'C']

arbre = reconstruire_arbre(prefixe, infixe)
postfixe = parcours_postfixe(arbre)

print(f"Parcours postfixe: {' '.join(postfixe)}")
# Résultat: D E B F C A</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="implementation-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card easy">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge easy">Facile 🟢</div>
            <h4 class="exercise-title">Classe NoeudBinaire</h4>
            <div class="exercise-content">
                <p>Implémentez une classe pour représenter un nœud d'arbre binaire.</p>
                <p><strong>Spécifications :</strong></p>
                <ul>
                    <li>Attributs : valeur, enfant_gauche, enfant_droit</li>
                    <li>Méthodes : est_feuille(), nb_enfants(), __str__()</li>
                    <li>Constructeur avec valeur obligatoire</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class NoeudBinaire:
    """Représente un nœud dans un arbre binaire"""
    
    def __init__(self, valeur):
        """Initialise un nœud avec une valeur"""
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None
    
    def est_feuille(self):
        """Vérifie si le nœud est une feuille"""
        return self.enfant_gauche is None and self.enfant_droit is None
    
    def nb_enfants(self):
        """Retourne le nombre d'enfants du nœud"""
        count = 0
        if self.enfant_gauche is not None:
            count += 1
        if self.enfant_droit is not None:
            count += 1
        return count
    
    def a_enfant_gauche(self):
        """Vérifie si le nœud a un enfant gauche"""
        return self.enfant_gauche is not None
    
    def a_enfant_droit(self):
        """Vérifie si le nœud a un enfant droit"""
        return self.enfant_droit is not None
    
    def ajouter_enfant_gauche(self, valeur):
        """Ajoute un enfant gauche avec la valeur donnée"""
        self.enfant_gauche = NoeudBinaire(valeur)
        return self.enfant_gauche
    
    def ajouter_enfant_droit(self, valeur):
        """Ajoute un enfant droit avec la valeur donnée"""
        self.enfant_droit = NoeudBinaire(valeur)
        return self.enfant_droit
    
    def __str__(self):
        """Représentation textuelle du nœud"""
        return f"Nœud({self.valeur})"
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return self.__str__()

# Tests de la classe
if __name__ == "__main__":
    # Création d'un nœud racine
    racine = NoeudBinaire('A')
    print(f"Racine: {racine}")
    print(f"Est feuille: {racine.est_feuille()}")
    print(f"Nombre d'enfants: {racine.nb_enfants()}")
    
    # Ajout d'enfants
    gauche = racine.ajouter_enfant_gauche('B')
    droit = racine.ajouter_enfant_droit('C')
    
    print(f"\nAprès ajout d'enfants:")
    print(f"Racine est feuille: {racine.est_feuille()}")
    print(f"Nombre d'enfants de la racine: {racine.nb_enfants()}")
    print(f"Enfant gauche: {racine.enfant_gauche}")
    print(f"Enfant droit: {racine.enfant_droit}")
    
    # Test des feuilles
    print(f"\nTests des feuilles:")
    print(f"B est feuille: {gauche.est_feuille()}")
    print(f"C est feuille: {droit.est_feuille()}")
    
    # Ajout d'un petit-enfant
    gauche.ajouter_enfant_gauche('D')
    print(f"\nAprès ajout de D sous B:")
    print(f"B est feuille: {gauche.est_feuille()}")
    print(f"D est feuille: {gauche.enfant_gauche.est_feuille()}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Classe ArbreBinaire</h4>
            <div class="exercise-content">
                <p>Créez une classe pour gérer un arbre binaire complet.</p>
                <p><strong>Méthodes à implémenter :</strong></p>
                <ul>
                    <li>hauteur() : calcule la hauteur de l'arbre</li>
                    <li>taille() : compte le nombre de nœuds</li>
                    <li>contient(valeur) : vérifie la présence d'une valeur</li>
                    <li>afficher() : affichage visuel de l'arbre</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class ArbreBinaire:
    """Classe pour gérer un arbre binaire"""
    
    def __init__(self, racine=None):
        """Initialise l'arbre avec une racine optionnelle"""
        if isinstance(racine, NoeudBinaire):
            self.racine = racine
        elif racine is not None:
            self.racine = NoeudBinaire(racine)
        else:
            self.racine = None
    
    def est_vide(self):
        """Vérifie si l'arbre est vide"""
        return self.racine is None
    
    def hauteur(self, noeud=None):
        """Calcule la hauteur de l'arbre (ou d'un sous-arbre)"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        hauteur_gauche = self.hauteur(noeud.enfant_gauche)
        hauteur_droite = self.hauteur(noeud.enfant_droit)
        
        return 1 + max(hauteur_gauche, hauteur_droite)
    
    def taille(self, noeud=None):
        """Compte le nombre de nœuds dans l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        return 1 + self.taille(noeud.enfant_gauche) + self.taille(noeud.enfant_droit)
    
    def contient(self, valeur, noeud=None):
        """Vérifie si une valeur est présente dans l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return False
        
        if noeud.valeur == valeur:
            return True
        
        return (self.contient(valeur, noeud.enfant_gauche) or 
                self.contient(valeur, noeud.enfant_droit))
    
    def nb_feuilles(self, noeud=None):
        """Compte le nombre de feuilles"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        if noeud.est_feuille():
            return 1
        
        return (self.nb_feuilles(noeud.enfant_gauche) + 
                self.nb_feuilles(noeud.enfant_droit))
    
    def afficher(self, noeud=None, niveau=0, prefixe="Racine: "):
        """Affiche l'arbre de manière visuelle"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            print(" " * (niveau * 4) + prefixe + str(noeud.valeur))
            
            if noeud.enfant_gauche is not None or noeud.enfant_droit is not None:
                if noeud.enfant_gauche is not None:
                    self.afficher(noeud.enfant_gauche, niveau + 1, "├── G: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "├── G: None")
                
                if noeud.enfant_droit is not None:
                    self.afficher(noeud.enfant_droit, niveau + 1, "└── D: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "└── D: None")
    
    def afficher_compact(self):
        """Affichage compact de l'arbre"""
        if self.est_vide():
            print("Arbre vide")
            return
        
        print(f"Arbre binaire:")
        print(f"  Racine: {self.racine.valeur}")
        print(f"  Hauteur: {self.hauteur()}")
        print(f"  Taille: {self.taille()}")
        print(f"  Nombre de feuilles: {self.nb_feuilles()}")
        print("\nStructure:")
        self.afficher()

# Tests de la classe ArbreBinaire
if __name__ == "__main__":
    # Création d'un arbre
    arbre = ArbreBinaire('A')
    
    # Construction manuelle de l'arbre
    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F
    
    arbre.racine.ajouter_enfant_gauche('B')
    arbre.racine.ajouter_enfant_droit('C')
    
    arbre.racine.enfant_gauche.ajouter_enfant_gauche('D')
    arbre.racine.enfant_gauche.ajouter_enfant_droit('E')
    
    arbre.racine.enfant_droit.ajouter_enfant_droit('F')
    
    # Tests des méthodes
    arbre.afficher_compact()
    
    print(f"\nTests de recherche:")
    for valeur in ['A', 'D', 'F', 'Z']:
        print(f"L'arbre contient '{valeur}': {arbre.contient(valeur)}")
    
    # Vérification des propriétés
    print(f"\nVérification: nb_feuilles = nb_nœuds_internes + 1")
    nb_feuilles = arbre.nb_feuilles()
    nb_internes = arbre.taille() - nb_feuilles
    print(f"Feuilles: {nb_feuilles}, Internes: {nb_internes}")
    print(f"Relation vérifiée: {nb_feuilles == nb_internes + 1}")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="parcours-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Parcours en profondeur (DFS)</h4>
            <div class="exercise-content">
                <p>Implémentez les trois types de parcours en profondeur.</p>
                <p><strong>À implémenter :</strong></p>
                <ul>
                    <li>Parcours préfixe (racine-gauche-droite)</li>
                    <li>Parcours infixe (gauche-racine-droite)</li>
                    <li>Parcours postfixe (gauche-droite-racine)</li>
                    <li>Versions récursive et itérative</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def parcours_prefixe_recursif(noeud, resultat=None):
    """Parcours préfixe récursif (racine-gauche-droite)"""
    if resultat is None:
        resultat = []
    
    if noeud is not None:
        resultat.append(noeud.valeur)  # Visiter la racine
        parcours_prefixe_recursif(noeud.enfant_gauche, resultat)  # Sous-arbre gauche
        parcours_prefixe_recursif(noeud.enfant_droit, resultat)   # Sous-arbre droit
    
    return resultat

def parcours_infixe_recursif(noeud, resultat=None):
    """Parcours infixe récursif (gauche-racine-droite)"""
    if resultat is None:
        resultat = []
    
    if noeud is not None:
        parcours_infixe_recursif(noeud.enfant_gauche, resultat)   # Sous-arbre gauche
        resultat.append(noeud.valeur)  # Visiter la racine
        parcours_infixe_recursif(noeud.enfant_droit, resultat)    # Sous-arbre droit
    
    return resultat

def parcours_postfixe_recursif(noeud, resultat=None):
    """Parcours postfixe récursif (gauche-droite-racine)"""
    if resultat is None:
        resultat = []
    
    if noeud is not None:
        parcours_postfixe_recursif(noeud.enfant_gauche, resultat)  # Sous-arbre gauche
        parcours_postfixe_recursif(noeud.enfant_droit, resultat)   # Sous-arbre droit
        resultat.append(noeud.valeur)  # Visiter la racine
    
    return resultat

# Versions itératives
def parcours_prefixe_iteratif(racine):
    """Parcours préfixe itératif avec pile"""
    if racine is None:
        return []
    
    resultat = []
    pile = [racine]
    
    while pile:
        noeud = pile.pop()
        resultat.append(noeud.valeur)
        
        # Ajouter d'abord l'enfant droit, puis le gauche
        # (car la pile est LIFO)
        if noeud.enfant_droit is not None:
            pile.append(noeud.enfant_droit)
        if noeud.enfant_gauche is not None:
            pile.append(noeud.enfant_gauche)
    
    return resultat

def parcours_infixe_iteratif(racine):
    """Parcours infixe itératif avec pile"""
    resultat = []
    pile = []
    noeud_actuel = racine
    
    while pile or noeud_actuel is not None:
        # Aller le plus à gauche possible
        while noeud_actuel is not None:
            pile.append(noeud_actuel)
            noeud_actuel = noeud_actuel.enfant_gauche
        
        # Traiter le nœud au sommet de la pile
        noeud_actuel = pile.pop()
        resultat.append(noeud_actuel.valeur)
        
        # Passer au sous-arbre droit
        noeud_actuel = noeud_actuel.enfant_droit
    
    return resultat

def parcours_postfixe_iteratif(racine):
    """Parcours postfixe itératif avec deux piles"""
    if racine is None:
        return []
    
    pile1 = [racine]
    pile2 = []
    
    # Première phase : remplir pile2 dans l'ordre inverse du postfixe
    while pile1:
        noeud = pile1.pop()
        pile2.append(noeud)
        
        # Ajouter d'abord l'enfant gauche, puis le droit
        if noeud.enfant_gauche is not None:
            pile1.append(noeud.enfant_gauche)
        if noeud.enfant_droit is not None:
            pile1.append(noeud.enfant_droit)
    
    # Deuxième phase : vider pile2 pour obtenir l'ordre postfixe
    resultat = []
    while pile2:
        resultat.append(pile2.pop().valeur)
    
    return resultat

# Ajout des méthodes à la classe ArbreBinaire
class ArbreBinaireAvecParcours(ArbreBinaire):
    """Extension de ArbreBinaire avec les méthodes de parcours"""
    
    def parcours_prefixe(self, iteratif=False):
        """Parcours préfixe de l'arbre"""
        if iteratif:
            return parcours_prefixe_iteratif(self.racine)
        else:
            return parcours_prefixe_recursif(self.racine)
    
    def parcours_infixe(self, iteratif=False):
        """Parcours infixe de l'arbre"""
        if iteratif:
            return parcours_infixe_iteratif(self.racine)
        else:
            return parcours_infixe_recursif(self.racine)
    
    def parcours_postfixe(self, iteratif=False):
        """Parcours postfixe de l'arbre"""
        if iteratif:
            return parcours_postfixe_iteratif(self.racine)
        else:
            return parcours_postfixe_recursif(self.racine)
    
    def tous_les_parcours(self):
        """Affiche tous les types de parcours"""
        print("Parcours de l'arbre:")
        print(f"  Préfixe (récursif):  {self.parcours_prefixe(False)}")
        print(f"  Préfixe (itératif):  {self.parcours_prefixe(True)}")
        print(f"  Infixe (récursif):   {self.parcours_infixe(False)}")
        print(f"  Infixe (itératif):   {self.parcours_infixe(True)}")
        print(f"  Postfixe (récursif): {self.parcours_postfixe(False)}")
        print(f"  Postfixe (itératif): {self.parcours_postfixe(True)}")

# Test des parcours
if __name__ == "__main__":
    # Créer l'arbre d'exemple
    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F
    
    arbre = ArbreBinaireAvecParcours('A')
    arbre.racine.ajouter_enfant_gauche('B')
    arbre.racine.ajouter_enfant_droit('C')
    arbre.racine.enfant_gauche.ajouter_enfant_gauche('D')
    arbre.racine.enfant_gauche.ajouter_enfant_droit('E')
    arbre.racine.enfant_droit.ajouter_enfant_droit('F')
    
    print("Structure de l'arbre:")
    arbre.afficher()
    print()
    
    # Tester tous les parcours
    arbre.tous_les_parcours()
    
    # Vérifier que les versions récursives et itératives donnent le même résultat
    print("\nVérification des implémentations:")
    print(f"Préfixe identique: {arbre.parcours_prefixe(False) == arbre.parcours_prefixe(True)}")
    print(f"Infixe identique: {arbre.parcours_infixe(False) == arbre.parcours_infixe(True)}")
    print(f"Postfixe identique: {arbre.parcours_postfixe(False) == arbre.parcours_postfixe(True)}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card medium">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge medium">Moyen 🟡</div>
            <h4 class="exercise-title">Parcours en largeur (BFS)</h4>
            <div class="exercise-content">
                <p>Implémentez le parcours en largeur et ses applications.</p>
                <p><strong>Fonctionnalités :</strong></p>
                <ul>
                    <li>Parcours niveau par niveau</li>
                    <li>Affichage par niveaux séparés</li>
                    <li>Recherche du niveau d'un élément</li>
                    <li>Vérification si l'arbre est complet</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">from collections import deque

def parcours_largeur(racine):
    """Parcours en largeur (BFS) simple"""
    if racine is None:
        return []
    
    resultat = []
    file = deque([racine])
    
    while file:
        noeud = file.popleft()
        resultat.append(noeud.valeur)
        
        # Ajouter les enfants à la file
        if noeud.enfant_gauche is not None:
            file.append(noeud.enfant_gauche)
        if noeud.enfant_droit is not None:
            file.append(noeud.enfant_droit)
    
    return resultat

def parcours_par_niveaux(racine):
    """Parcours en largeur avec séparation par niveaux"""
    if racine is None:
        return []
    
    niveaux = []
    file = deque([racine])
    
    while file:
        taille_niveau = len(file)
        niveau_actuel = []
        
        # Traiter tous les nœuds du niveau actuel
        for _ in range(taille_niveau):
            noeud = file.popleft()
            niveau_actuel.append(noeud.valeur)
            
            # Ajouter les enfants pour le niveau suivant
            if noeud.enfant_gauche is not None:
                file.append(noeud.enfant_gauche)
            if noeud.enfant_droit is not None:
                file.append(noeud.enfant_droit)
        
        niveaux.append(niveau_actuel)
    
    return niveaux

def trouver_niveau(racine, valeur_cherchee):
    """Trouve le niveau d'une valeur dans l'arbre"""
    if racine is None:
        return -1
    
    file = deque([(racine, 0)])  # (nœud, niveau)
    
    while file:
        noeud, niveau = file.popleft()
        
        if noeud.valeur == valeur_cherchee:
            return niveau
        
        # Ajouter les enfants avec le niveau suivant
        if noeud.enfant_gauche is not None:
            file.append((noeud.enfant_gauche, niveau + 1))
        if noeud.enfant_droit is not None:
            file.append((noeud.enfant_droit, niveau + 1))
    
    return -1  # Valeur non trouvée

def est_arbre_complet(racine):
    """Vérifie si l'arbre est complet"""
    if racine is None:
        return True
    
    file = deque([racine])
    noeud_incomplet_trouve = False
    
    while file:
        noeud = file.popleft()
        
        # Vérifier l'enfant gauche
        if noeud.enfant_gauche is not None:
            if noeud_incomplet_trouve:
                return False  # Un nœud incomplet a été trouvé avant
            file.append(noeud.enfant_gauche)
        else:
            noeud_incomplet_trouve = True
        
        # Vérifier l'enfant droit
        if noeud.enfant_droit is not None:
            if noeud_incomplet_trouve:
                return False  # Un nœud incomplet a été trouvé avant
            file.append(noeud.enfant_droit)
        else:
            noeud_incomplet_trouve = True
    
    return True

def largeur_max(racine):
    """Trouve la largeur maximale de l'arbre (niveau avec le plus de nœuds)"""
    if racine is None:
        return 0
    
    file = deque([racine])
    largeur_max = 0
    
    while file:
        taille_niveau = len(file)
        largeur_max = max(largeur_max, taille_niveau)
        
        # Traiter tous les nœuds du niveau actuel
        for _ in range(taille_niveau):
            noeud = file.popleft()
            
            if noeud.enfant_gauche is not None:
                file.append(noeud.enfant_gauche)
            if noeud.enfant_droit is not None:
                file.append(noeud.enfant_droit)
    
    return largeur_max

def afficher_arbre_visuel(racine):
    """Affichage visuel de l'arbre niveau par niveau"""
    if racine is None:
        print("Arbre vide")
        return
    
    niveaux = parcours_par_niveaux(racine)
    
    print("Arbre par niveaux:")
    for i, niveau in enumerate(niveaux):
        print(f"Niveau {i}: {' '.join(map(str, niveau))}")
    
    print(f"\nLargeur maximale: {largeur_max(racine)}")
    print(f"Arbre complet: {est_arbre_complet(racine)}")

# Extension de la classe ArbreBinaire
class ArbreBinaireComplet(ArbreBinaireAvecParcours):
    """Extension avec les méthodes de parcours en largeur"""
    
    def parcours_largeur(self):
        """Parcours en largeur de l'arbre"""
        return parcours_largeur(self.racine)
    
    def parcours_par_niveaux(self):
        """Parcours par niveaux séparés"""
        return parcours_par_niveaux(self.racine)
    
    def trouver_niveau(self, valeur):
        """Trouve le niveau d'une valeur"""
        return trouver_niveau(self.racine, valeur)
    
    def est_complet(self):
        """Vérifie si l'arbre est complet"""
        return est_arbre_complet(self.racine)
    
    def largeur_max(self):
        """Largeur maximale de l'arbre"""
        return largeur_max(self.racine)
    
    def afficher_par_niveaux(self):
        """Affichage par niveaux"""
        afficher_arbre_visuel(self.racine)

# Tests du parcours en largeur
if __name__ == "__main__":
    # Créer un arbre complet
    #       A
    #      / \
    #     B   C
    #    / \ / \
    #   D  E F  G
    
    arbre_complet = ArbreBinaireComplet('A')
    arbre_complet.racine.ajouter_enfant_gauche('B')
    arbre_complet.racine.ajouter_enfant_droit('C')
    arbre_complet.racine.enfant_gauche.ajouter_enfant_gauche('D')
    arbre_complet.racine.enfant_gauche.ajouter_enfant_droit('E')
    arbre_complet.racine.enfant_droit.ajouter_enfant_gauche('F')
    arbre_complet.racine.enfant_droit.ajouter_enfant_droit('G')
    
    print("=== ARBRE COMPLET ===")
    arbre_complet.afficher_par_niveaux()
    
    print(f"\nParcours en largeur: {arbre_complet.parcours_largeur()}")
    
    # Tests de recherche de niveau
    print("\nNiveaux des éléments:")
    for valeur in ['A', 'B', 'D', 'G', 'Z']:
        niveau = arbre_complet.trouver_niveau(valeur)
        if niveau >= 0:
            print(f"  '{valeur}' est au niveau {niveau}")
        else:
            print(f"  '{valeur}' non trouvé")
    
    # Créer un arbre non complet
    print("\n=== ARBRE NON COMPLET ===")
    arbre_incomplet = ArbreBinaireComplet('A')
    arbre_incomplet.racine.ajouter_enfant_gauche('B')
    arbre_incomplet.racine.ajouter_enfant_droit('C')
    arbre_incomplet.racine.enfant_gauche.ajouter_enfant_gauche('D')
    arbre_incomplet.racine.enfant_droit.ajouter_enfant_droit('E')
    
    arbre_incomplet.afficher_par_niveaux()</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

<div id="abr-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Arbre Binaire de Recherche (ABR)</h4>
            <div class="exercise-content">
                <p>Implémentez un Arbre Binaire de Recherche avec toutes ses opérations.</p>
                <p><strong>Opérations à implémenter :</strong></p>
                <ul>
                    <li>Insertion d'un élément</li>
                    <li>Recherche d'un élément</li>
                    <li>Suppression d'un élément (3 cas)</li>
                    <li>Minimum et maximum</li>
                    <li>Successeur et prédécesseur</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class ABR:
    """Arbre Binaire de Recherche"""
    
    def __init__(self):
        """Initialise un ABR vide"""
        self.racine = None
    
    def est_vide(self):
        """Vérifie si l'ABR est vide"""
        return self.racine is None
    
    def inserer(self, valeur):
        """Insère une valeur dans l'ABR"""
        self.racine = self._inserer_recursif(self.racine, valeur)
    
    def _inserer_recursif(self, noeud, valeur):
        """Insertion récursive"""
        if noeud is None:
            return NoeudBinaire(valeur)
        
        if valeur < noeud.valeur:
            noeud.enfant_gauche = self._inserer_recursif(noeud.enfant_gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.enfant_droit = self._inserer_recursif(noeud.enfant_droit, valeur)
        # Si valeur == noeud.valeur, on ne fait rien (pas de doublons)
        
        return noeud
    
    def rechercher(self, valeur):
        """Recherche une valeur dans l'ABR"""
        return self._rechercher_recursif(self.racine, valeur)
    
    def _rechercher_recursif(self, noeud, valeur):
        """Recherche récursive"""
        if noeud is None or noeud.valeur == valeur:
            return noeud
        
        if valeur < noeud.valeur:
            return self._rechercher_recursif(noeud.enfant_gauche, valeur)
        else:
            return self._rechercher_recursif(noeud.enfant_droit, valeur)
    
    def minimum(self, noeud=None):
        """Trouve le minimum de l'ABR ou d'un sous-arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return None
        
        while noeud.enfant_gauche is not None:
            noeud = noeud.enfant_gauche
        
        return noeud
    
    def maximum(self, noeud=None):
        """Trouve le maximum de l'ABR ou d'un sous-arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return None
        
        while noeud.enfant_droit is not None:
            noeud = noeud.enfant_droit
        
        return noeud
    
    def supprimer(self, valeur):
        """Supprime une valeur de l'ABR"""
        self.racine = self._supprimer_recursif(self.racine, valeur)
    
    def _supprimer_recursif(self, noeud, valeur):
        """Suppression récursive avec gestion des 3 cas"""
        if noeud is None:
            return noeud
        
        # Chercher le nœud à supprimer
        if valeur < noeud.valeur:
            noeud.enfant_gauche = self._supprimer_recursif(noeud.enfant_gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.enfant_droit = self._supprimer_recursif(noeud.enfant_droit, valeur)
        else:
            # Nœud trouvé, 3 cas de suppression
            
            # Cas 1: Nœud feuille (aucun enfant)
            if noeud.enfant_gauche is None and noeud.enfant_droit is None:
                return None
            
            # Cas 2: Nœud avec un seul enfant
            elif noeud.enfant_gauche is None:
                return noeud.enfant_droit
            elif noeud.enfant_droit is None:
                return noeud.enfant_gauche
            
            # Cas 3: Nœud avec deux enfants
            else:
                # Trouver le successeur (minimum du sous-arbre droit)
                successeur = self.minimum(noeud.enfant_droit)
                
                # Remplacer la valeur du nœud par celle du successeur
                noeud.valeur = successeur.valeur
                
                # Supprimer le successeur
                noeud.enfant_droit = self._supprimer_recursif(noeud.enfant_droit, successeur.valeur)
        
        return noeud
    
    def parcours_infixe(self):
        """Parcours infixe (donne les éléments triés)"""
        return parcours_infixe_recursif(self.racine)
    
    def afficher(self):
        """Affiche l'ABR"""
        if self.est_vide():
            print("ABR vide")
        else:
            self._afficher_recursif(self.racine, 0, "Racine: ")
    
    def _afficher_recursif(self, noeud, niveau, prefixe):
        """Affichage récursif de l'ABR"""
        if noeud is not None:
            print(" " * (niveau * 4) + prefixe + str(noeud.valeur))
            
            if noeud.enfant_gauche is not None or noeud.enfant_droit is not None:
                if noeud.enfant_gauche is not None:
                    self._afficher_recursif(noeud.enfant_gauche, niveau + 1, "├── G: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "├── G: None")
                
                if noeud.enfant_droit is not None:
                    self._afficher_recursif(noeud.enfant_droit, niveau + 1, "└── D: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "└── D: None")

# Tests de l'ABR
if __name__ == "__main__":
    abr = ABR()
    
    # Insertion d'éléments
    valeurs = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    print("Insertion des valeurs:", valeurs)
    
    for valeur in valeurs:
        abr.inserer(valeur)
    
    print("\nABR après insertions:")
    abr.afficher()
    
    print(f"\nParcours infixe (trié): {abr.parcours_infixe()}")
    
    # Tests de recherche
    print("\nTests de recherche:")
    for valeur in [25, 45, 90]:
        resultat = abr.rechercher(valeur)
        if resultat:
            print(f"  {valeur} trouvé")
        else:
            print(f"  {valeur} non trouvé")
    
    # Minimum et maximum
    print(f"\nMinimum: {abr.minimum().valeur}")
    print(f"Maximum: {abr.maximum().valeur}")
    
    # Tests de suppression
    print("\nTests de suppression:")
    
    # Supprimer une feuille
    print("Suppression de 10 (feuille):")
    abr.supprimer(10)
    print(f"Parcours après suppression: {abr.parcours_infixe()}")
    
    # Supprimer un nœud avec un enfant
    print("\nSuppression de 25 (un enfant):")
    abr.supprimer(25)
    print(f"Parcours après suppression: {abr.parcours_infixe()}")
    
    # Supprimer un nœud avec deux enfants
    print("\nSuppression de 30 (deux enfants):")
    abr.supprimer(30)
    print(f"Parcours après suppression: {abr.parcours_infixe()}")
    
    print("\nABR final:")
    abr.afficher()</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card hard">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge hard">Difficile 🔴</div>
            <h4 class="exercise-title">Validation d'un ABR</h4>
            <div class="exercise-content">
                <p>Implémentez des fonctions pour valider qu'un arbre binaire est bien un ABR.</p>
                <p><strong>Méthodes à implémenter :</strong></p>
                <ul>
                    <li>Validation par parcours infixe</li>
                    <li>Validation par bornes min/max</li>
                    <li>Correction d'un ABR invalide</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">def est_abr_infixe(racine):
    """Valide un ABR en vérifiant que le parcours infixe est trié"""
    parcours = parcours_infixe_recursif(racine)
    
    # Vérifier que la liste est triée
    for i in range(1, len(parcours)):
        if parcours[i] <= parcours[i-1]:
            return False
    
    return True

def est_abr_bornes(racine, min_val=float('-inf'), max_val=float('inf')):
    """Valide un ABR en vérifiant les bornes min/max récursivement"""
    if racine is None:
        return True
    
    # Vérifier que la valeur respecte les bornes
    if racine.valeur <= min_val or racine.valeur >= max_val:
        return False
    
    # Vérifier récursivement les sous-arbres avec les nouvelles bornes
    return (est_abr_bornes(racine.enfant_gauche, min_val, racine.valeur) and
            est_abr_bornes(racine.enfant_droit, racine.valeur, max_val))

def corriger_abr(racine):
    """Corrige un arbre binaire pour en faire un ABR valide"""
    if racine is None:
        return None
    
    # Récupérer tous les éléments par parcours infixe
    elements = []
    _collecter_elements(racine, elements)
    
    # Trier les éléments
    elements.sort()
    
    # Reconstruire l'ABR équilibré
    return _construire_abr_equilibre(elements, 0, len(elements) - 1)

def _collecter_elements(noeud, elements):
    """Collecte tous les éléments de l'arbre"""
    if noeud is not None:
        elements.append(noeud.valeur)
        _collecter_elements(noeud.enfant_gauche, elements)
        _collecter_elements(noeud.enfant_droit, elements)

def _construire_abr_equilibre(elements, debut, fin):
    """Construit un ABR équilibré à partir d'une liste triée"""
    if debut > fin:
        return None
    
    # Prendre l'élément du milieu comme racine
    milieu = (debut + fin) // 2
    racine = NoeudBinaire(elements[milieu])
    
    # Construire récursivement les sous-arbres
    racine.enfant_gauche = _construire_abr_equilibre(elements, debut, milieu - 1)
    racine.enfant_droit = _construire_abr_equilibre(elements, milieu + 1, fin)
    
    return racine

def trouver_erreurs_abr(racine):
    """Trouve les nœuds qui violent la propriété ABR"""
    erreurs = []
    _verifier_noeud(racine, float('-inf'), float('inf'), erreurs)
    return erreurs

def _verifier_noeud(noeud, min_val, max_val, erreurs):
    """Vérifie récursivement chaque nœud"""
    if noeud is None:
        return
    
    # Vérifier si le nœud viole les contraintes
    if noeud.valeur <= min_val or noeud.valeur >= max_val:
        erreurs.append({
            'noeud': noeud.valeur,
            'min_attendu': min_val,
            'max_attendu': max_val
        })
    
    # Vérifier récursivement les enfants
    _verifier_noeud(noeud.enfant_gauche, min_val, noeud.valeur, erreurs)
    _verifier_noeud(noeud.enfant_droit, noeud.valeur, max_val, erreurs)

# Tests de validation
if __name__ == "__main__":
    # Créer un ABR valide
    print("=== ABR VALIDE ===")
    abr_valide = ABR()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        abr_valide.inserer(val)
    
    abr_valide.afficher()
    print(f"Est ABR (infixe): {est_abr_infixe(abr_valide.racine)}")
    print(f"Est ABR (bornes): {est_abr_bornes(abr_valide.racine)}")
    
    # Créer un arbre binaire invalide
    print("\n=== ARBRE INVALIDE ===")
    racine_invalide = NoeudBinaire(50)
    racine_invalide.enfant_gauche = NoeudBinaire(30)
    racine_invalide.enfant_droit = NoeudBinaire(70)
    racine_invalide.enfant_gauche.enfant_gauche = NoeudBinaire(20)
    racine_invalide.enfant_gauche.enfant_droit = NoeudBinaire(60)  # ERREUR: 60 > 50
    
    print("Arbre invalide:")
    arbre_test = ArbreBinaire()
    arbre_test.racine = racine_invalide
    arbre_test.afficher()
    
    print(f"\nEst ABR (infixe): {est_abr_infixe(racine_invalide)}")
    print(f"Est ABR (bornes): {est_abr_bornes(racine_invalide)}")
    
    # Trouver les erreurs
    erreurs = trouver_erreurs_abr(racine_invalide)
    print(f"\nErreurs trouvées: {len(erreurs)}")
    for erreur in erreurs:
        print(f"  Nœud {erreur['noeud']} viole les contraintes")
        print(f"    Doit être > {erreur['min_attendu']} et < {erreur['max_attendu']}")
    
    # Corriger l'arbre
    print("\n=== CORRECTION ===")
    racine_corrigee = corriger_abr(racine_invalide)
    arbre_corrige = ArbreBinaire()
    arbre_corrige.racine = racine_corrigee
    
    print("Arbre corrigé:")
    arbre_corrige.afficher()
    print(f"\nEst ABR après correction: {est_abr_bornes(racine_corrigee)}")
     print(f"Parcours infixe: {parcours_infixe_recursif(racine_corrigee)}")</code></pre>
             </div>
         </div>
     </div>
</div>
</div>

<div id="applications-section" class="section-content">
<div class="exercise-cards">
    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">Expert 🟣</div>
            <h4 class="exercise-title">Arbre d'expression arithmétique</h4>
            <div class="exercise-content">
                <p>Implémentez un évaluateur d'expressions arithmétiques utilisant un arbre binaire.</p>
                <p><strong>Fonctionnalités :</strong></p>
                <ul>
                    <li>Construction d'un arbre à partir d'une expression postfixe</li>
                    <li>Évaluation de l'expression</li>
                    <li>Conversion vers les notations préfixe, infixe et postfixe</li>
                    <li>Simplification d'expressions</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">class NoeudExpression:
    """Nœud pour un arbre d'expression arithmétique"""
    
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
        self.est_operateur = valeur in ['+', '-', '*', '/', '^']
    
    def est_feuille(self):
        return self.gauche is None and self.droit is None

class ArbreExpression:
    """Arbre d'expression arithmétique"""
    
    def __init__(self):
        self.racine = None
    
    def construire_depuis_postfixe(self, expression_postfixe):
        """Construit l'arbre à partir d'une expression postfixe"""
        pile = []
        
        for token in expression_postfixe.split():
            noeud = NoeudExpression(token)
            
            if noeud.est_operateur:
                # Opérateur : prendre deux opérandes de la pile
                if len(pile) < 2:
                    raise ValueError(f"Expression invalide : pas assez d'opérandes pour {token}")
                
                noeud.droit = pile.pop()  # Deuxième opérande
                noeud.gauche = pile.pop()  # Premier opérande
            
            pile.append(noeud)
        
        if len(pile) != 1:
            raise ValueError("Expression postfixe invalide")
        
        self.racine = pile[0]
        return self.racine
    
    def evaluer(self, noeud=None):
        """Évalue l'expression représentée par l'arbre"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return 0
        
        # Si c'est une feuille (nombre), retourner sa valeur
        if noeud.est_feuille():
            try:
                return float(noeud.valeur)
            except ValueError:
                raise ValueError(f"Valeur invalide : {noeud.valeur}")
        
        # Évaluer récursivement les sous-arbres
        valeur_gauche = self.evaluer(noeud.gauche)
        valeur_droite = self.evaluer(noeud.droit)
        
        # Appliquer l'opérateur
        if noeud.valeur == '+':
            return valeur_gauche + valeur_droite
        elif noeud.valeur == '-':
            return valeur_gauche - valeur_droite
        elif noeud.valeur == '*':
            return valeur_gauche * valeur_droite
        elif noeud.valeur == '/':
            if valeur_droite == 0:
                raise ValueError("Division par zéro")
            return valeur_gauche / valeur_droite
        elif noeud.valeur == '^':
            return valeur_gauche ** valeur_droite
        else:
            raise ValueError(f"Opérateur inconnu : {noeud.valeur}")
    
    def vers_prefixe(self, noeud=None):
        """Convertit l'arbre en notation préfixe"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return ""
        
        if noeud.est_feuille():
            return noeud.valeur
        
        gauche = self.vers_prefixe(noeud.gauche)
        droite = self.vers_prefixe(noeud.droit)
        
        return f"{noeud.valeur} {gauche} {droite}"
    
    def vers_infixe(self, noeud=None, parentheses=True):
        """Convertit l'arbre en notation infixe avec parenthèses"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return ""
        
        if noeud.est_feuille():
            return noeud.valeur
        
        gauche = self.vers_infixe(noeud.gauche, parentheses)
        droite = self.vers_infixe(noeud.droit, parentheses)
        
        expression = f"{gauche} {noeud.valeur} {droite}"
        
        if parentheses and not noeud == self.racine:
            expression = f"({expression})"
        
        return expression
    
    def vers_postfixe(self, noeud=None):
        """Convertit l'arbre en notation postfixe"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None:
            return ""
        
        if noeud.est_feuille():
            return noeud.valeur
        
        gauche = self.vers_postfixe(noeud.gauche)
        droite = self.vers_postfixe(noeud.droit)
        
        return f"{gauche} {droite} {noeud.valeur}"
    
    def simplifier(self, noeud=None):
        """Simplifie l'expression (règles de base)"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is None or noeud.est_feuille():
            return noeud
        
        # Simplifier récursivement les sous-arbres
        noeud.gauche = self.simplifier(noeud.gauche)
        noeud.droit = self.simplifier(noeud.droit)
        
        # Appliquer les règles de simplification
        if noeud.gauche.est_feuille() and noeud.droit.est_feuille():
            try:
                val_g = float(noeud.gauche.valeur)
                val_d = float(noeud.droit.valeur)
                
                # Règles de simplification
                if noeud.valeur == '+' and (val_g == 0 or val_d == 0):
                    return noeud.droit if val_g == 0 else noeud.gauche
                elif noeud.valeur == '*' and (val_g == 0 or val_d == 0):
                    return NoeudExpression('0')
                elif noeud.valeur == '*' and (val_g == 1 or val_d == 1):
                    return noeud.droit if val_g == 1 else noeud.gauche
                elif noeud.valeur == '^' and val_d == 0:
                    return NoeudExpression('1')
                elif noeud.valeur == '^' and val_d == 1:
                    return noeud.gauche
            except ValueError:
                pass  # Pas des nombres, continuer
        
        return noeud
    
    def afficher_arbre(self, noeud=None, niveau=0, prefixe="Racine: "):
        """Affiche l'arbre visuellement"""
        if noeud is None:
            noeud = self.racine
        
        if noeud is not None:
            print(" " * (niveau * 4) + prefixe + str(noeud.valeur))
            
            if not noeud.est_feuille():
                if noeud.gauche is not None:
                    self.afficher_arbre(noeud.gauche, niveau + 1, "├── G: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "├── G: None")
                
                if noeud.droit is not None:
                    self.afficher_arbre(noeud.droit, niveau + 1, "└── D: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "└── D: None")

# Tests de l'arbre d'expression
if __name__ == "__main__":
    # Test avec une expression simple
    print("=== ARBRE D'EXPRESSION ===")
    
    arbre = ArbreExpression()
    
    # Expression : (3 + 4) * (2 - 1)
    # Postfixe : 3 4 + 2 1 - *
    expression_postfixe = "3 4 + 2 1 - *"
    
    print(f"Expression postfixe: {expression_postfixe}")
    
    arbre.construire_depuis_postfixe(expression_postfixe)
    
    print("\nArbre construit:")
    arbre.afficher_arbre()
    
    print(f"\nÉvaluation: {arbre.evaluer()}")
    
    print("\nConversions:")
    print(f"  Préfixe:  {arbre.vers_prefixe()}")
    print(f"  Infixe:   {arbre.vers_infixe()}")
    print(f"  Postfixe: {arbre.vers_postfixe()}")
    
    # Test de simplification
    print("\n=== SIMPLIFICATION ===")
    
    # Expression avec des zéros et des uns : x * 1 + 0 * y
    # Postfixe : x 1 * 0 y * +
    arbre_simple = ArbreExpression()
    arbre_simple.construire_depuis_postfixe("5 1 * 0 3 * +")
    
    print("Avant simplification:")
    arbre_simple.afficher_arbre()
    print(f"Infixe: {arbre_simple.vers_infixe()}")
    print(f"Évaluation: {arbre_simple.evaluer()}")
    
    arbre_simple.simplifier()
    
    print("\nAprès simplification:")
    arbre_simple.afficher_arbre()
    print(f"Infixe: {arbre_simple.vers_infixe()}")
    print(f"Évaluation: {arbre_simple.evaluer()}")
    
    # Tests d'erreurs
    print("\n=== TESTS D'ERREURS ===")
    
    try:
        arbre_erreur = ArbreExpression()
        arbre_erreur.construire_depuis_postfixe("3 +")  # Pas assez d'opérandes
    except ValueError as e:
        print(f"Erreur détectée: {e}")
    
    try:
        arbre_division = ArbreExpression()
        arbre_division.construire_depuis_postfixe("5 0 /")
        arbre_division.evaluer()  # Division par zéro
    except ValueError as e:
        print(f"Erreur détectée: {e}")</code></pre>
            </div>
        </div>
    </div>

    <div class="exercise-card expert">
        <div class="exercise-content-wrapper">
            <div class="difficulty-badge expert">Expert 🟣</div>
            <h4 class="exercise-title">Système de fichiers avec arbres</h4>
            <div class="exercise-content">
                <p>Simulez un système de fichiers hiérarchique avec des arbres.</p>
                <p><strong>Fonctionnalités :</strong></p>
                <ul>
                    <li>Création de dossiers et fichiers</li>
                    <li>Navigation dans l'arborescence</li>
                    <li>Recherche de fichiers</li>
                    <li>Calcul de la taille totale</li>
                    <li>Affichage de l'arborescence</li>
                </ul>
            </div>
            <button class="toggle-solution" onclick="toggleSolution(this)">
                <span class="arrow">→</span> Voir la correction
            </button>
        </div>
        <div class="solution-wrapper">
            <div class="solution">
                <pre><code class="language-python">from datetime import datetime

class NoeudFichier:
    """Représente un fichier ou dossier dans le système de fichiers"""
    
    def __init__(self, nom, est_dossier=False, taille=0):
        self.nom = nom
        self.est_dossier = est_dossier
        self.taille = taille if not est_dossier else 0
        self.date_creation = datetime.now()
        self.enfants = [] if est_dossier else None
        self.parent = None
    
    def ajouter_enfant(self, enfant):
        """Ajoute un enfant (fichier ou dossier)"""
        if not self.est_dossier:
            raise ValueError("Impossible d'ajouter un enfant à un fichier")
        
        # Vérifier que le nom n'existe pas déjà
        for child in self.enfants:
            if child.nom == enfant.nom:
                raise ValueError(f"Un élément nommé '{enfant.nom}' existe déjà")
        
        enfant.parent = self
        self.enfants.append(enfant)
    
    def supprimer_enfant(self, nom):
        """Supprime un enfant par son nom"""
        if not self.est_dossier:
            raise ValueError("Impossible de supprimer d'un fichier")
        
        for i, enfant in enumerate(self.enfants):
            if enfant.nom == nom:
                del self.enfants[i]
                return True
        
        return False
    
    def trouver_enfant(self, nom):
        """Trouve un enfant par son nom"""
        if not self.est_dossier:
            return None
        
        for enfant in self.enfants:
            if enfant.nom == nom:
                return enfant
        
        return None
    
    def taille_totale(self):
        """Calcule la taille totale (récursive pour les dossiers)"""
        if not self.est_dossier:
            return self.taille
        
        total = 0
        for enfant in self.enfants:
            total += enfant.taille_totale()
        
        return total
    
    def chemin_complet(self):
        """Retourne le chemin complet depuis la racine"""
        if self.parent is None:
            return "/" + self.nom if self.nom != "/" else "/"
        
        chemin_parent = self.parent.chemin_complet()
        if chemin_parent == "/":
            return "/" + self.nom
        else:
            return chemin_parent + "/" + self.nom

class SystemeFichiers:
    """Système de fichiers basé sur un arbre"""
    
    def __init__(self):
        self.racine = NoeudFichier("/", est_dossier=True)
        self.repertoire_courant = self.racine
    
    def pwd(self):
        """Affiche le répertoire courant"""
        return self.repertoire_courant.chemin_complet()
    
    def ls(self, repertoire=None):
        """Liste le contenu d'un répertoire"""
        if repertoire is None:
            repertoire = self.repertoire_courant
        
        if not repertoire.est_dossier:
            return [repertoire.nom]
        
        contenu = []
        for enfant in repertoire.enfants:
            if enfant.est_dossier:
                contenu.append(enfant.nom + "/")
            else:
                contenu.append(f"{enfant.nom} ({enfant.taille} octets)")
        
        return sorted(contenu)
    
    def mkdir(self, nom_dossier):
        """Crée un nouveau dossier"""
        nouveau_dossier = NoeudFichier(nom_dossier, est_dossier=True)
        self.repertoire_courant.ajouter_enfant(nouveau_dossier)
    
    def touch(self, nom_fichier, taille=0):
        """Crée un nouveau fichier"""
        nouveau_fichier = NoeudFichier(nom_fichier, est_dossier=False, taille=taille)
        self.repertoire_courant.ajouter_enfant(nouveau_fichier)
    
    def cd(self, chemin):
        """Change de répertoire"""
        if chemin == "/":
            self.repertoire_courant = self.racine
            return
        
        if chemin == "..":
            if self.repertoire_courant.parent is not None:
                self.repertoire_courant = self.repertoire_courant.parent
            return
        
        # Chercher le dossier dans le répertoire courant
        enfant = self.repertoire_courant.trouver_enfant(chemin)
        if enfant is None:
            raise ValueError(f"Répertoire '{chemin}' introuvable")
        
        if not enfant.est_dossier:
            raise ValueError(f"'{chemin}' n'est pas un répertoire")
        
        self.repertoire_courant = enfant
    
    def find(self, nom, repertoire=None):
        """Recherche récursive d'un fichier ou dossier"""
        if repertoire is None:
            repertoire = self.racine
        
        resultats = []
        
        # Vérifier le répertoire actuel
        if repertoire.nom == nom:
            resultats.append(repertoire.chemin_complet())
        
        # Rechercher dans les enfants
        if repertoire.est_dossier:
            for enfant in repertoire.enfants:
                resultats.extend(self.find(nom, enfant))
        
        return resultats
    
    def du(self, repertoire=None):
        """Calcule l'utilisation du disque"""
        if repertoire is None:
            repertoire = self.repertoire_courant
        
        return repertoire.taille_totale()
    
    def tree(self, repertoire=None, niveau=0, prefixe=""):
        """Affiche l'arborescence"""
        if repertoire is None:
            repertoire = self.racine
            print(repertoire.nom)
            niveau = 0
            prefixe = ""
        
        if repertoire.est_dossier:
            enfants = repertoire.enfants
            for i, enfant in enumerate(enfants):
                est_dernier = (i == len(enfants) - 1)
                
                if est_dernier:
                    print(prefixe + "└── " + enfant.nom + ("/" if enfant.est_dossier else f" ({enfant.taille} octets)"))
                    nouveau_prefixe = prefixe + "    "
                else:
                    print(prefixe + "├── " + enfant.nom + ("/" if enfant.est_dossier else f" ({enfant.taille} octets)"))
                    nouveau_prefixe = prefixe + "│   "
                
                if enfant.est_dossier:
                    self.tree(enfant, niveau + 1, nouveau_prefixe)
    
    def rm(self, nom):
        """Supprime un fichier ou dossier"""
        if not self.repertoire_courant.supprimer_enfant(nom):
            raise ValueError(f"'{nom}' introuvable")

# Tests du système de fichiers
if __name__ == "__main__":
    print("=== SYSTÈME DE FICHIERS ===")
    
    fs = SystemeFichiers()
    
    # Créer une structure de fichiers
    print("Création de la structure...")
    
    # Créer des dossiers
    fs.mkdir("home")
    fs.mkdir("usr")
    fs.mkdir("var")
    
    # Aller dans home
    fs.cd("home")
    fs.mkdir("user1")
    fs.mkdir("user2")
    
    # Aller dans user1
    fs.cd("user1")
    fs.mkdir("Documents")
    fs.mkdir("Images")
    fs.touch("readme.txt", 1024)
    fs.touch("config.json", 512)
    
    # Aller dans Documents
    fs.cd("Documents")
    fs.touch("rapport.pdf", 2048)
    fs.touch("notes.txt", 256)
    
    # Retour à la racine
    fs.cd("/")
    
    print("\nStructure créée:")
    fs.tree()
    
    print(f"\nRépertoire courant: {fs.pwd()}")
    print(f"Contenu: {fs.ls()}")
    
    # Navigation
    print("\n=== NAVIGATION ===")
    fs.cd("home")
    print(f"Répertoire courant: {fs.pwd()}")
    print(f"Contenu: {fs.ls()}")
    
    fs.cd("user1")
    print(f"\nRépertoire courant: {fs.pwd()}")
    print(f"Contenu: {fs.ls()}")
    
    # Recherche
    print("\n=== RECHERCHE ===")
    resultats = fs.find("readme.txt")
    print(f"Fichiers 'readme.txt' trouvés: {resultats}")
    
    resultats = fs.find("Documents")
    print(f"Dossiers 'Documents' trouvés: {resultats}")
    
    # Utilisation du disque
    print("\n=== UTILISATION DU DISQUE ===")
    fs.cd("/")
    print(f"Taille totale du système: {fs.du()} octets")
    
    fs.cd("home/user1")
    print(f"Taille du dossier user1: {fs.du()} octets")
    
    # Suppression
    print("\n=== SUPPRESSION ===")
    print("Avant suppression:")
    print(f"Contenu de user1: {fs.ls()}")
    
    fs.rm("config.json")
    print("\nAprès suppression de config.json:")
    print(f"Contenu de user1: {fs.ls()}")
    
    print(f"Nouvelle taille: {fs.du()} octets")</code></pre>
            </div>
        </div>
    </div>
</div>
</div>

</div>

<!-- Modal pour afficher les solutions -->
<div id="solutionModal" class="solution-modal">
    <div class="solution-content">
        <span class="solution-close" onclick="closeSolutionModal()">&times;</span>
        <div id="solutionText"></div>
    </div>
</div>

<script>
function toggleSolution(button) {
    const solutionWrapper = button.parentElement.nextElementSibling;
    const arrow = button.querySelector('.arrow');
    
    if (solutionWrapper.style.display === 'none' || solutionWrapper.style.display === '') {
        solutionWrapper.style.display = 'block';
        arrow.style.transform = 'rotate(90deg)';
        button.innerHTML = '<span class="arrow" style="transform: rotate(90deg)">→</span> Masquer la correction';
    } else {
        solutionWrapper.style.display = 'none';
        arrow.style.transform = 'rotate(0deg)';
        button.innerHTML = '<span class="arrow">→</span> Voir la correction';
    }
}

function closeSolutionModal() {
    document.getElementById('solutionModal').style.display = 'none';
}

function showSection(sectionName) {
    // Masquer toutes les sections
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    
    // Désactiver tous les onglets
    const tabs = document.querySelectorAll('.section-tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Afficher la section sélectionnée
    const targetSection = document.getElementById(sectionName + '-section');
    if (targetSection) {
        targetSection.style.display = 'block';
    }
    
    // Activer l'onglet correspondant
    event.target.classList.add('active');
}

// Afficher la première section par défaut
document.addEventListener('DOMContentLoaded', function() {
    showSection('concepts');
});

// Fermer la modal avec Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeSolutionModal();
    }
});
</script>

</body>
</html>