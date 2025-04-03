# Guide d'évaluation - Projet Application Bancaire

Ce document accompagne les fichiers d'évaluation `notes.csv` et `grille_evaluation.csv` et explique la méthodologie d'évaluation utilisée pour noter les copies des élèves sur le projet d'application bancaire.

## Critères d'évaluation

L'évaluation est basée sur les critères suivants, pour un total de 20 points :

### 1. Création de compte (4 points)
- Structure de données appropriée (dictionnaire) : 1 point
- Vérification de l'existence préalable du compte : 1 point
- Paramètres correctement typés et utilisés : 1 point
- Initialisation correcte des transactions : 1 point

### 2. Dépôt d'argent (3 points)
- Vérification de l'existence du compte : 1 point
- Mise à jour correcte du solde : 1 point
- Enregistrement de la transaction dans l'historique : 1 point

### 3. Retrait d'argent (3 points)
- Vérification de l'existence du compte : 1 point
- Vérification du solde suffisant : 1 point
- Mise à jour du solde et enregistrement de la transaction : 1 point

### 4. Vérification du solde (2 points)
- Vérification de l'existence du compte : 1 point
- Affichage correct du solde : 1 point

### 5. Historique des transactions (2 points)
- Vérification de l'existence du compte : 1 point
- Affichage correct de l'historique : 1 point

### 6. Interface utilisateur (4 points)
- Fonction d'affichage du menu conforme : 1 point
- Boucle principale fonctionnelle : 1 point
- Gestion des choix utilisateur : 1 point
- Possibilité de quitter proprement l'application : 1 point

### 7. Gestion des erreurs (2 points)
- Messages d'erreur explicites : 1 point
- Robustesse face aux entrées invalides : 1 point

## Barème détaillé

Pour chaque critère, l'attribution des points suit cette logique :
- **Implémentation complète et correcte** : 100% des points
- **Implémentation fonctionnelle avec des défauts mineurs** : 75% des points
- **Implémentation partiellement fonctionnelle** : 50% des points
- **Implémentation avec des erreurs importantes** : 25% des points
- **Implémentation absente ou non fonctionnelle** : 0 point

## Exemples d'évaluation

### Exemple pour la fonction de retrait

```python
def retirer(numero_compte: str, montant: float):
    if numero_compte not in comptes:
        print("Le compte n'existe pas.")
    elif comptes[numero_compte]["solde"] < montant:
        print("Fonds insuffisants.")
    else:
        comptes[numero_compte]["solde"] -= montant
        comptes[numero_compte]["transactions"].append("Retrait de " + str(montant) + "€")
        print(montant, "€ retirés du compte", numero_compte)
```

**Évaluation** : 3/3 points
- Vérification de l'existence du compte ✓
- Vérification du solde suffisant ✓
- Mise à jour du solde et enregistrement de la transaction ✓

### Exemple avec des défauts

```python
def retirer(nmr_compte:str,montant:float):
    if nmr_compte not in comptes:
        print("Le compte n'existe pas !")
        return None
    if comptes[nmr_compte]["solde"] < montant:
        print("Solde insuffisant !")
        return None
    if comptes[nmr_compte]["solde"] > montant:  # Condition redondante
        comptes[nmr_compte]["solde"] -= montant
    comptes[nmr_compte]["transactions"].append({"type":"retrait","montant":montant})
    print("Retrait effectué")
```

**Évaluation** : 2.5/3 points
- Vérification de l'existence du compte ✓
- Vérification du solde suffisant ✓
- Mise à jour du solde et enregistrement de la transaction ⚠️ (condition redondante)

## Utilisation pour le CAPES NSI

Cette grille d'évaluation peut être utilisée comme exemple pour :
1. Montrer comment évaluer des productions d'élèves de manière objective
2. Illustrer la création de barèmes détaillés pour des projets de programmation
3. Démontrer l'importance d'une évaluation par compétences spécifiques
4. Servir de base pour une discussion sur les critères d'évaluation en NSI