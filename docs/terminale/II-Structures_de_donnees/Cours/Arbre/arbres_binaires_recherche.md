# 🔍 Arbres Binaires de Recherche (ABR)

<div class="concept-section">
    <h2 class="section-title">🎯 Définition et Propriétés</h2>
    
    <div class="definition-box">
        <div class="definition-title">🔍 Arbre Binaire de Recherche</div>
        <div class="definition-content">
            Un <strong>Arbre Binaire de Recherche (ABR)</strong> est un arbre binaire qui respecte la <strong>propriété d'ordre</strong> :
            <ul>
                <li>Toutes les valeurs du sous-arbre <strong>gauche</strong> sont <strong>inférieures</strong> à la racine</li>
                <li>Toutes les valeurs du sous-arbre <strong>droit</strong> sont <strong>supérieures</strong> à la racine</li>
                <li>Cette propriété s'applique <strong>récursivement</strong> à tous les sous-arbres</li>
            </ul>
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Propriété d'Ordre</div>
            <div class="concept-description">
                La structure maintient automatiquement un ordre qui permet des recherches efficaces en O(log n).
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Efficacité</div>
            <div class="concept-description">
                Recherche, insertion et suppression en O(log n) dans le cas équilibré, O(n) dans le pire cas.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Parcours Infixe</div>
            <div class="concept-description">
                Le parcours infixe d'un ABR produit automatiquement les valeurs en ordre croissant.
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🔍 Opération de Recherche</h2>
    
    <div class="definition-box">
        <div class="definition-title">🎯 Principe de la Recherche</div>
        <div class="definition-content">
            La recherche exploite la propriété d'ordre pour <strong>éliminer la moitié</strong> des possibilités à chaque étape, similaire à la recherche dichotomique.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🔍 Recherche dans un ABR</div>
            <div class="concept-description">
                Algorithme récursif qui compare la valeur recherchée avec le nœud courant.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Recherche</div>
                <pre><code>def rechercher(self, valeur, noeud=None):
    """
    Recherche une valeur dans l'ABR
    Retourne True si trouvée, False sinon
    """
    if noeud is None:
        noeud = self.racine
    
    # Cas de base : nœud vide
    if noeud is None:
        return False
    
    # Valeur trouvée
    if valeur == noeud.valeur:
        return True
    
    # Recherche dans le sous-arbre approprié
    elif valeur < noeud.valeur:
        return self.rechercher(valeur, noeud.gauche)
    else:
        return self.rechercher(valeur, noeud.droite)</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">📍 Recherche avec Nœud</div>
            <div class="concept-description">
                Version qui retourne le nœud trouvé plutôt qu'un booléen.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Recherche Avancée</div>
                <pre><code>def rechercher_noeud(self, valeur, noeud=None):
    """
    Recherche et retourne le nœud contenant la valeur
    Retourne None si non trouvé
    """
    if noeud is None:
        noeud = self.racine
    
    if noeud is None or noeud.valeur == valeur:
        return noeud
    
    if valeur < noeud.valeur:
        return self.rechercher_noeud(valeur, noeud.gauche)
    else:
        return self.rechercher_noeud(valeur, noeud.droite)</code></pre>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">➕ Opération d'Insertion</h2>
    
    <div class="definition-box">
        <div class="definition-title">📥 Principe de l'Insertion</div>
        <div class="definition-content">
            L'insertion trouve la <strong>position correcte</strong> en suivant la propriété d'ordre, puis ajoute le nouveau nœud comme <strong>feuille</strong>.
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">➕ Insertion dans un ABR</div>
            <div class="concept-description">
                Algorithme récursif qui maintient la propriété d'ordre lors de l'ajout.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Insertion</div>
                <pre><code>def inserer(self, valeur, noeud=None):
    """
    Insère une valeur dans l'ABR en maintenant la propriété d'ordre
    Retourne la racine du sous-arbre modifié
    """
    # Premier appel : initialiser avec la racine
    if noeud is None and self.racine is not None:
        self.racine = self._inserer_recursif(valeur, self.racine)
        return
    
    # Arbre vide : créer la racine
    if self.racine is None:
        self.racine = NoeudBinaire(valeur)
        return
    
    self.racine = self._inserer_recursif(valeur, self.racine)

def _inserer_recursif(self, valeur, noeud):
    """
    Méthode auxiliaire récursive pour l'insertion
    """
    # Cas de base : position trouvée
    if noeud is None:
        return NoeudBinaire(valeur)
    
    # Insertion selon la propriété d'ordre
    if valeur < noeud.valeur:
        noeud.gauche = self._inserer_recursif(valeur, noeud.gauche)
    elif valeur > noeud.valeur:
        noeud.droite = self._inserer_recursif(valeur, noeud.droite)
    # Si valeur == noeud.valeur, on ne fait rien (pas de doublons)
    
    return noeud</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">🏗️ Exemple d'Insertion</div>
            <div class="concept-description">
                Construction progressive d'un ABR par insertions successives.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Construction d'ABR</div>
                <pre><code># Création et construction d'un ABR
abr = ArbreBinaireRecherche()

# Insertions successives
valeurs = [50, 30, 70, 20, 40, 60, 80]
for valeur in valeurs:
    abr.inserer(valeur)

# Résultat :
#       50
#      /  \
#     30   70
#    / \   / \
#   20 40 60 80

print("ABR construit avec succès")
print("Parcours infixe :", abr.parcours_infixe())  # [20, 30, 40, 50, 60, 70, 80]</code></pre>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">➖ Opération de Suppression</h2>
    
    <div class="definition-box">
        <div class="definition-title">🗑️ Principe de la Suppression</div>
        <div class="definition-content">
            La suppression est l'opération la plus complexe car elle doit <strong>maintenir la propriété d'ordre</strong> après avoir retiré un nœud. Trois cas distincts existent selon le nombre d'enfants du nœud à supprimer.
        </div>
    </div>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">1️⃣</div>
            <div class="concept-name">Cas 1 : Feuille</div>
            <div class="concept-description">
                <strong>Nœud sans enfants</strong><br>
                Suppression directe - le plus simple des trois cas.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">2️⃣</div>
            <div class="concept-name">Cas 2 : Un Enfant</div>
            <div class="concept-description">
                <strong>Nœud avec un seul enfant</strong><br>
                Remplacer le nœud par son unique enfant.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">3️⃣</div>
            <div class="concept-name">Cas 3 : Deux Enfants</div>
            <div class="concept-description">
                <strong>Nœud avec deux enfants</strong><br>
                Remplacer par le successeur (ou prédécesseur) dans l'ordre infixe.
            </div>
        </div>
    </div>
    
    <div class="method-grid">
        <div class="method-card">
            <div class="method-type">🗑️ Suppression Complète</div>
            <div class="concept-description">
                Implémentation gérant les trois cas de suppression.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Implémentation Suppression</div>
                <pre><code>def supprimer(self, valeur):
    """
    Supprime une valeur de l'ABR
    """
    self.racine = self._supprimer_recursif(valeur, self.racine)

def _supprimer_recursif(self, valeur, noeud):
    """
    Méthode auxiliaire récursive pour la suppression
    """
    # Cas de base : valeur non trouvée
    if noeud is None:
        return noeud
    
    # Recherche du nœud à supprimer
    if valeur < noeud.valeur:
        noeud.gauche = self._supprimer_recursif(valeur, noeud.gauche)
    elif valeur > noeud.valeur:
        noeud.droite = self._supprimer_recursif(valeur, noeud.droite)
    else:
        # Nœud trouvé - traiter les 3 cas
        
        # Cas 1 : Nœud feuille (aucun enfant)
        if noeud.gauche is None and noeud.droite is None:
            return None
        
        # Cas 2a : Seulement enfant droit
        elif noeud.gauche is None:
            return noeud.droite
        
        # Cas 2b : Seulement enfant gauche
        elif noeud.droite is None:
            return noeud.gauche
        
        # Cas 3 : Deux enfants
        else:
            # Trouver le successeur (minimum du sous-arbre droit)
            successeur = self._trouver_minimum(noeud.droite)
            
            # Remplacer la valeur du nœud par celle du successeur
            noeud.valeur = successeur.valeur
            
            # Supprimer le successeur
            noeud.droite = self._supprimer_recursif(successeur.valeur, noeud.droite)
    
    return noeud

def _trouver_minimum(self, noeud):
    """
    Trouve le nœud avec la valeur minimale dans un sous-arbre
    """
    while noeud.gauche is not None:
        noeud = noeud.gauche
    return noeud</code></pre>
            </div>
        </div>
        
        <div class="method-card">
            <div class="method-type">📝 Exemple de Suppression</div>
            <div class="concept-description">
                Démonstration des différents cas de suppression.
            </div>
            
            <div class="code-example">
                <div class="code-title">💻 Test de Suppression</div>
                <pre><code># ABR initial : [20, 30, 40, 50, 60, 70, 80]
#       50
#      /  \
#     30   70
#    / \   / \
#   20 40 60 80

# Cas 1 : Supprimer une feuille (20)
abr.supprimer(20)
print("Après suppression de 20 :", abr.parcours_infixe())  # [30, 40, 50, 60, 70, 80]

# Cas 2 : Supprimer un nœud avec un enfant (30)
abr.supprimer(30)
print("Après suppression de 30 :", abr.parcours_infixe())  # [40, 50, 60, 70, 80]

# Cas 3 : Supprimer un nœud avec deux enfants (50 - racine)
abr.supprimer(50)
print("Après suppression de 50 :", abr.parcours_infixe())  # [40, 60, 70, 80]</code></pre>
            </div>
        </div>
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">📊 Analyse de Complexité</h2>
    
    <div class="definition-box">
        <div class="definition-title">⚡ Complexités des Opérations ABR</div>
        <div class="definition-content">
            <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
                <thead>
                    <tr style="background-color: #f8f9fa;">
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Opération</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Cas Moyen</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Pire Cas</th>
                        <th style="padding: 0.75rem; border: 1px solid #dee2e6;">Remarques</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Recherche</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(log n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Arbre équilibré vs dégénéré</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Insertion</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(log n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Dépend de l'ordre d'insertion</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Suppression</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(log n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Cas 3 le plus complexe</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;"><strong>Parcours</strong></td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">O(n)</td>
                        <td style="padding: 0.75rem; border: 1px solid #dee2e6;">Visite tous les nœuds</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <div class="highlight-fact">
        ⚡ <strong>Avantage clé :</strong> Un ABR équilibré offre des opérations en O(log n), soit une efficacité comparable à la recherche dichotomique sur un tableau trié, mais avec l'avantage d'insertions et suppressions dynamiques efficaces.
    </div>
</div>

<div class="concept-section">
    <h2 class="section-title">🎯 Points Clés à Retenir</h2>
    
    <div class="concept-grid">
        <div class="concept-card">
            <div class="concept-icon">📊</div>
            <div class="concept-name">Propriété Fondamentale</div>
            <div class="concept-description">
                La propriété d'ordre (gauche < racine < droite) est la clé de l'efficacité des ABR et doit être maintenue à tout moment.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">⚡</div>
            <div class="concept-name">Performance Optimale</div>
            <div class="concept-description">
                Les ABR équilibrés offrent O(log n) pour les opérations principales, mais peuvent dégénérer en O(n) si mal construits.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🔄</div>
            <div class="concept-name">Tri Automatique</div>
            <div class="concept-description">
                Le parcours infixe d'un ABR produit automatiquement les valeurs en ordre croissant, offrant un tri efficace.
            </div>
        </div>
        
        <div class="concept-card">
            <div class="concept-icon">🗑️</div>
            <div class="concept-name">Suppression Complexe</div>
            <div class="concept-description">
                La suppression nécessite une attention particulière aux trois cas possibles pour maintenir la structure et les propriétés de l'ABR.
            </div>
        </div>
    </div>
</div>