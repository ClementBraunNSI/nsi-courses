# 🌳 Parcours d'Arbres

<div class="concept-section">
    <h2 class="section-title">🎯 Introduction aux Parcours</h2>
    
    <div class="definition-box">
        <div class="definition-title">🚶 Parcours d'arbre</div>
        <div class="definition-content">
            Un <strong>parcours d'arbre</strong> est une méthode systématique pour <strong>visiter tous les nœuds</strong> d'un arbre dans un ordre spécifique. Chaque parcours suit une stratégie différente selon l'ordre de visite des nœuds.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Objectif</div>
            <div class="concept-description">
                Traiter chaque nœud exactement une fois selon une stratégie définie.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Récursivité</div>
            <div class="concept-description">
                Les parcours utilisent la nature récursive des arbres pour une implémentation élégante.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Complexité</div>
            <div class="concept-description">
                Tous les parcours ont une complexité temporelle O(n) car chaque nœud est visité une fois.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔄 Types de Parcours</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">1️⃣</div>
            <div class="concept-name">Parcours Préfixe</div>
            <div class="concept-description">
                <strong>Racine → Gauche → Droite</strong><br>
                Visite d'abord la racine, puis le sous-arbre gauche, enfin le sous-arbre droit.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">2️⃣</div>
            <div class="concept-name">Parcours Infixe</div>
            <div class="concept-description">
                <strong>Gauche → Racine → Droite</strong><br>
                Visite le sous-arbre gauche, puis la racine, enfin le sous-arbre droit.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">3️⃣</div>
            <div class="concept-name">Parcours Postfixe</div>
            <div class="concept-description">
                <strong>Gauche → Droite → Racine</strong><br>
                Visite les sous-arbres gauche et droit avant la racine.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🌟 Applications Pratiques</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📋</div>
            <div class="concept-name">Parcours Préfixe</div>
            <div class="concept-description">
                <strong>Utilisations :</strong>
                <ul>
                    <li>Copie d'arbres</li>
                    <li>Sérialisation</li>
                    <li>Évaluation d'expressions préfixées</li>
                    <li>Création de structures hiérarchiques</li>
                </ul>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔢</div>
            <div class="concept-name">Parcours Infixe</div>
            <div class="concept-description">
                <strong>Utilisations :</strong>
                <ul>
                    <li>Tri d'arbres binaires de recherche</li>
                    <li>Évaluation d'expressions mathématiques</li>
                    <li>Affichage ordonné des données</li>
                    <li>Validation de propriétés ABR</li>
                </ul>
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🧮</div>
            <div class="concept-name">Parcours Postfixe</div>
            <div class="concept-description">
                <strong>Utilisations :</strong>
                <ul>
                    <li>Suppression d'arbres</li>
                    <li>Calcul de taille/hauteur</li>
                    <li>Évaluation d'expressions postfixées</li>
                    <li>Libération de mémoire</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">💻 Implémentations Python</h2>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">1️⃣ Parcours Préfixe</div>
            <div class="concept-description">
                Traite la racine avant ses enfants - idéal pour la copie et la sérialisation.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Préfixe</div>
                <pre><code>def parcours_prefixe(self, noeud=None, resultat=None):
    """
    Parcours préfixe : Racine → Gauche → Droite
    Retourne la liste des valeurs dans l'ordre de visite
    """
    if resultat is None:
        resultat = []
    
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        # 1. Traiter la racine
        resultat.append(noeud.valeur)
        
        # 2. Parcourir le sous-arbre gauche
        self.parcours_prefixe(noeud.gauche, resultat)
        
        # 3. Parcourir le sous-arbre droit
        self.parcours_prefixe(noeud.droite, resultat)
    
    return resultat</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">2️⃣ Parcours Infixe</div>
            <div class="concept-description">
                Traite la racine entre ses enfants - produit un ordre trié pour les ABR.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Infixe</div>
                <pre><code>def parcours_infixe(self, noeud=None, resultat=None):
    """
    Parcours infixe : Gauche → Racine → Droite
    Pour un ABR, produit les valeurs en ordre croissant
    """
    if resultat is None:
        resultat = []
    
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        # 1. Parcourir le sous-arbre gauche
        self.parcours_infixe(noeud.gauche, resultat)
        
        # 2. Traiter la racine
        resultat.append(noeud.valeur)
        
        # 3. Parcourir le sous-arbre droit
        self.parcours_infixe(noeud.droite, resultat)
    
    return resultat</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">3️⃣ Parcours Postfixe</div>
            <div class="concept-description">
                Traite la racine après ses enfants - idéal pour les calculs et la suppression.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Postfixe</div>
                <pre><code>def parcours_postfixe(self, noeud=None, resultat=None):
    """
    Parcours postfixe : Gauche → Droite → Racine
    Idéal pour calculer des propriétés ou supprimer l'arbre
    """
    if resultat is None:
        resultat = []
    
    if noeud is None:
        noeud = self.racine
    
    if noeud is not None:
        # 1. Parcourir le sous-arbre gauche
        self.parcours_postfixe(noeud.gauche, resultat)
        
        # 2. Parcourir le sous-arbre droit
        self.parcours_postfixe(noeud.droite, resultat)
        
        # 3. Traiter la racine
        resultat.append(noeud.valeur)
    
    return resultat</code></pre>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🧪 Exemple Complet</h2>
    
    <div class="tree-diagram">
        <h4 style="color: #2ecc71; margin-bottom: 1rem;">🌳 Arbre d'exemple</h4>
        <pre>       A
      / \
     B   C
    / \   \
   D   E   F</pre>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Résultats des Parcours</div>
            <div class="concept-description">
                <strong>Préfixe :</strong> A, B, D, E, C, F<br>
                <strong>Infixe :</strong> D, B, E, A, C, F<br>
                <strong>Postfixe :</strong> D, E, B, F, C, A
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">💻</div>
            <div class="concept-name">Code de Test</div>
            <div class="concept-description">
                <div class="code-example">
                    <div class="code-title">💻 Test des Parcours</div>
                    <pre><code># Construction de l'arbre
racine = NoeudBinaire('A')
racine.gauche = NoeudBinaire('B')
racine.droite = NoeudBinaire('C')
racine.gauche.gauche = NoeudBinaire('D')
racine.gauche.droite = NoeudBinaire('E')
racine.droite.droite = NoeudBinaire('F')

arbre = ArbreBinaire(racine)

# Tests des parcours
print("Préfixe :", arbre.parcours_prefixe())
print("Infixe :", arbre.parcours_infixe())
print("Postfixe :", arbre.parcours_postfixe())</code></pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">⚡ Analyse de Complexité</h2>
    
    <div class="definition-box">
        <div class="definition-title">📊 Complexité des Parcours</div>
        <div class="definition-content">
            <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
                <thead>
                    <tr style="background-color: #f8f9fa;">
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Parcours</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Complexité Temporelle</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Complexité Spatiale</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Remarques</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Préfixe</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(h)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">h = hauteur de l'arbre</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Infixe</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(h)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Ordre trié pour ABR</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Postfixe</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(h)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Idéal pour suppression</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="highlight-fact">
        💡 <strong>Important :</strong> La complexité spatiale O(h) correspond à la pile d'appels récursifs, où h est la hauteur de l'arbre.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Points Clés à Retenir</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Récursivité Naturelle</div>
            <div class="concept-description">
                Les parcours exploitent la structure récursive des arbres pour une implémentation élégante et intuitive.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Efficacité Optimale</div>
            <div class="concept-description">
                Complexité O(n) incontournable car chaque nœud doit être visité exactement une fois.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🎯</div>
            <div class="concept-name">Choix Stratégique</div>
            <div class="concept-description">
                Le choix du parcours dépend de l'application : préfixe pour copier, infixe pour trier, postfixe pour calculer.
            </div>
        </div>
    </div>
</div>