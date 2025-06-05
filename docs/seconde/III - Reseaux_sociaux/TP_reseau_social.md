# TP : Modéliser un réseau social en Python

Dans ce TP, tu vas utiliser des outils Python (appelés "classes") pour simuler un réseau social. Deux outils sont déjà prêts pour toi : `Utilisateur` (pour créer des personnes) et `ReseauSocial` (pour gérer le réseau). Ton travail sera d'utiliser ces outils pour ajouter des personnes et créer des liens d'amitié entre elles.

---

```python
# Voici les deux outils (classes) que tu vas utiliser :
# Tu n'as pas besoin de comprendre comment ils sont faits, juste comment les utiliser !

class Utilisateur:
    # Quand tu crées un Utilisateur, tu lui donnes un nom.
    # Il n'a pas encore d'amis au début.
    def __init__(self, nom: str):
        self.nom: str = nom
        self.amis: list['Utilisateur'] = []

    # Cette fonction permet d'ajouter un ami à un utilisateur.
    def ajouter_ami(self, autre_utilisateur: 'Utilisateur'):
        if autre_utilisateur not in self.amis:
            self.amis.append(autre_utilisateur)

    # Permet d'afficher l'utilisateur de manière simple (ex: Utilisateur(Alice))
    def __repr__(self) -> str:
        return f"Utilisateur({self.nom})"

class ReseauSocial:
    # Quand tu crées un ReseauSocial, il est vide au début.
    def __init__(self):
        self.utilisateurs: list['Utilisateur'] = []

    # Cette fonction permet d'ajouter un utilisateur au réseau social.
    def ajouter_utilisateur(self, utilisateur: 'Utilisateur'):
        if utilisateur not in self.utilisateurs:
            self.utilisateurs.append(utilisateur)

    # Cette fonction permet de créer un lien d'amitié entre deux utilisateurs.
    def lier_amis(self, utilisateur1: 'Utilisateur', utilisateur2: 'Utilisateur'):
        utilisateur1.ajouter_ami(utilisateur2)
        utilisateur2.ajouter_ami(utilisateur1)

    # Cette fonction affiche tous les utilisateurs du réseau et leurs amis.
    def afficher_reseau(self):
        for utilisateur in self.utilisateurs:
            print(f"{utilisateur.nom} a pour amis : {[ami.nom for ami in utilisateur.amis]}")
```

---

## Consignes : À toi de jouer !

Suis les étapes ci-dessous dans la partie "Exemple de code à compléter" :

1.  **Crée un réseau social** : Utilise `reseau = ReseauSocial()` pour commencer.
2.  **Crée trois personnes (utilisateurs)** : Donne-leur des noms comme "Alice", "Bob" et "Charlie" en utilisant `Utilisateur("Nom")`.
3.  **Ajoute ces personnes à ton réseau social** : Utilise la fonction `reseau.ajouter_utilisateur(*utilisateur*)` pour chaque personne.
4.  **Crée des liens d'amitié** : Utilise la fonction `reseau.lier_amis()` pour connecter Alice et Bob, puis Bob et Charlie.
5.  **Affiche le réseau** : Utilise `reseau.afficher_reseau()` pour voir qui est ami avec qui.

**Exemple de code à compléter :**

```python
# Étape 1 : Crée ton réseau social
reseau = ______

# Étape 2 : Crée trois personnes (utilisateurs) avec leurs noms
alice = Utilisateur("_____")
bob = Utilisateur("_____")
charlie = Utilisateur("_____")

# Étape 3 : Ajoute ces personnes à ton réseau social
reseau.ajouter_utilisateur(_____)
reseau.ajouter_utilisateur(_____)
reseau.ajouter_utilisateur(_____)

# Étape 4 : Crée des liens d'amitié entre eux
# Par exemple, Alice devient amie avec Bob
reseau.lier_amis(_____, _____)
# Et Bob devient ami avec Charlie
reseau.lier_amis(_____, _____)

# Étape 5 : Affiche le réseau pour voir les amitiés
reseau.afficher_reseau()
```

---

N'hésite pas à modifier les noms ou à ajouter d'autres utilisateurs pour tester !