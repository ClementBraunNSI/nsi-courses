# Jour 1 🎊🦊🎉 : Gestion des invitations

Pour organiser une soirée du Nouvel An réussie, il faut d'abord bien gérer les invitations. Sarah organise une fête et doit s'assurer que tous ses amis reçoivent leur invitation et confirment leur présence.

Elle a une liste de contacts avec leurs informations et doit automatiser le processus d'invitation.

## Informations nécessaires

On considère :
- Une **invitation** est représentée par un **dictionnaire** contenant :
  - nom (str)
  - email (str)
  - telephone (str)
  - confirme (bool)

```python
invites = [
    {"nom": "Alice", "email": "alice@email.com", "telephone": "0123456789", "confirme": False},
    {"nom": "Bob", "email": "bob@email.com", "telephone": "0987654321", "confirme": True},
    {"nom": "Charlie", "email": "charlie@email.com", "telephone": "0147258369", "confirme": False},
    {"nom": "Diana", "email": "diana@email.com", "telephone": "0369258147", "confirme": True},
    {"nom": "Eve", "email": "eve@email.com", "telephone": "0258147369", "confirme": False},
    {"nom": "Frank", "email": "frank@email.com", "telephone": "0741852963", "confirme": True},
    {"nom": "Grace", "email": "grace@email.com", "telephone": "0852963741", "confirme": False},
    {"nom": "Henry", "email": "henry@email.com", "telephone": "0963741852", "confirme": True}
]
```

## Exercice Principal

!!! fox_correction "Compter les confirmations"
    **Écrire une fonction `compter_confirmations` qui prend en paramètre une liste d'invités et renvoie le nombre de personnes qui ont confirmé leur présence.**

    *La fonction doit parcourir la liste et compter les invités dont le champ 'confirme' est True.*

!!! fox_correction "Liste des non-confirmés"
    **Écrire une fonction `liste_non_confirmes` qui prend en paramètre une liste d'invités et renvoie une liste contenant les noms des personnes qui n'ont pas encore confirmé.**

    *La fonction doit retourner une liste de chaînes de caractères (les noms).*

!!! fox_correction "Relance par email"
    **Écrire une fonction `emails_relance` qui prend en paramètre une liste d'invités et renvoie une liste des adresses email des personnes à relancer.**

    *Cette fonction doit utiliser la fonction précédente pour identifier les non-confirmés et extraire leurs emails.*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec la liste d'invités fournie.**