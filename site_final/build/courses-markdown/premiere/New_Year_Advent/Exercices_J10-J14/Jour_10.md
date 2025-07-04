# Jour 10 🦊❄️🎉 : Le Quizz du Nouvel An

Jean veut organiser un quiz durant la soirée avec des questions simples sur l'année écoulée.

## Informations nécessaires

On considère :
- Une **question** est représentée par un **dictionnaire** contenant :
  - type (str) : "qcm" ou "vf"
  - categorie (str)
  - question (str)
  - options (list) pour les QCM
  - reponse (str ou bool selon le type)

```python
questions = [
    {
        "type": "qcm",
        "categorie": "culture",
        "question": "Quel film a gagné l'Oscar 2023 ?",
        "options": ["Oppenheimer", "Barbie", "Avatar 2"],
        "reponse": "Oppenheimer"
    },
    {
        "type": "vf",
        "categorie": "cinema",
        "question": "Avatar 2 est sorti en 2023",
        "reponse": False
    }
]
```

## Exercice Principal

!!! fox_correction "Filtrer par catégorie"
    **Écrire une fonction `questions_par_categorie` qui prend en paramètre la liste des questions et une catégorie, et renvoie toutes les questions de cette catégorie.**

!!! fox_correction "Mélanger les questions"
    **Écrire une fonction `melanger_questions` qui prend en paramètre la liste des questions et renvoie une nouvelle liste avec les questions dans un ordre aléatoire.**

    *Indication : Utilisez la fonction random.shuffle()*

!!! fox_correction "Vérifier réponse"
    **Écrire une fonction `verifier_reponse` qui prend en paramètre une question et une réponse donnée, et renvoie True si la réponse est correcte.**


!!! fox_correction_eval "Pour aller plus loin : Quiz"
    **Écrire une fonction `quiz` qui prend en paramètre la liste des questions et permet de jouer au jeu : on demandera à l'utilisateur la question, on associera chaque réponse à un chiffre (1 à 4) et affichera dans le terminal `Bonne réponse` si la réponse est bonne, `Mauvaise réponse, c'était [réponse]` si elle est fausse et à la fin de toutes les questions posées, le nombre de bonnes réponses données.**

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions (ou 4 avec la plus compliquée) ainsi qu'un exemple d'utilisation avec les questions fournies.**
