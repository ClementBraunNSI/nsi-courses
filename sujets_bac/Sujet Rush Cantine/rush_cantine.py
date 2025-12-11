distribution = {
    'Gare': {'Mairie': 30, 'Salle de sport': 45},
    'Mairie': {'Gare': 30, 'Lycée': 60, 'Musée': 20},
    'Salle de sport': {'Gare': 45, 'Médiathèque': 10},
    'Médiathèque': {'Salle de sport': 10, 'Lycée': 50},
    'Musée': {'Mairie': 20, 'Piscine': 120},
    'Lycée': {'Mairie': 60, 'Médiathèque': 50, 'Piscine': 15},
    'Piscine': {'Lycée': 15, 'Musée': 120}
}

# ==========================================
# QUESTION 1 : Modification du Graphe
# ==========================================
def ouvrir_raccourci(graphe):
    # graphe['Salle_Profs']['Cantine'] = 5
    pass



# ==========================================
# QUESTION 2 : Algorithme de parcours
# ==========================================
def calculer_duree(graphe, chemin):
#     temps_total = 0
#     for i in range(len(chemin) - 1):
#         depart = chemin[i]
#         arrivee = chemin[i+1]
#         temps_total += graphe[depart][arrivee]
#     return temps_total
    pass


# ==========================================
# QUESTION 3 : Tests et Robustesse
# ==========================================

def test_verification():
#     # Cas normal : Philo -> Escalier_A (30s)
#     assert calculer_duree(lycee, ['Philo', 'Escalier_A']) == 30
#     
#     # Cas limite : Trajet sur place (pas de boucle for) -> 0s
#     assert calculer_duree(lycee, ['Cantine']) == 0
#     
#     print("Tous les tests sont passés avec succès !")
    pass

def calculer_duree_robuste(graphe, chemin):
#     temps_total = 0
#     for i in range(len(chemin) - 1):
#         depart = chemin[i]
#         arrivee = chemin[i+1]
#         
#         # Vérification si la connexion existe
#         if arrivee not in graphe[depart]:
#             return -1
#             
#         temps_total += graphe[depart][arrivee]
#     return temps_total
    pass


# ==========================================
# QUESTION 4 : Dijkstra (Trous complétés)
# ==========================================
def temps_minimal_dijkstra(graphe, depart):
    dist = {sommet: float('inf') for sommet in graphe}
    dist[depart] = 0
    non_visites = list(graphe.keys())

    while len(non_visites) > 0:
        u = non_visites[0]
        for sommet in non_visites:
            if dist[sommet] < dist[u]:
                u = sommet
        
        non_visites.remove(u)

        for voisin in graphe[u]:
            temps_trajet = graphe[u][voisin]
            
            # --- CODE AJOUTÉ ICI ---
            
            # Condition A : Si passer par u est plus court que ce qu'on connaissait
            # Si la distance actuelle vers u + le temps du trajet
            # est inférieure à la distance déjà connue pour le voisin...
            if dist[u] - temps_trajet < non-visite[voisin]:
                
                # Instruction B : On met à jour la distance du voisin
                # ... on met à jour la distance du voisin
                dist[voisin] = dist[voisin] + temps_trajet
                
            # -----------------------
                
    return dist