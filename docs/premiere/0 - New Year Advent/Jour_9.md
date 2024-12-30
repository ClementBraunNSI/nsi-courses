
# Jour 9 🦊❄️🎉 : Le karaoké du Nouvel An

Pour animer la soirée, Jean veut organiser un karaoké. Il a une liste de chansons avec leurs paroles, mais il veut s'assurer que les chansons ne sont ni trop courtes ni trop longues.

## Informations nécessaires

On considère :
- Une **chanson** est représentée par un **dictionnaire** contenant :
  - titre (str)
  - artiste (str)
  - paroles (list de str)
  - difficulte (int de 1 à 5)

```python
    chansons_karaoke = [
    {
        "titre": "Diggy Diggy Hole",
        "artiste": "Wind Rose",
        "paroles": [
            "I am a dwarf and I'm digging a hole",
            "Diggy diggy hole, diggy diggy hole",
            "I am a dwarf and I'm digging a hole",
            "Diggy diggy hole, digging a hole"
        ],
        "difficulte": 3
    },
    {
        "titre": "I Want It That Way",
        "artiste": "Backstreet Boys",
        "paroles": [
            "You are my fire, the one desire",
            "Believe when I say, I want it that way",
            "But we are two worlds apart",
            "Can't reach to your heart",
            "When you say, that I want it that way"
        ],
        "difficulte": 2
    },
    {
        "titre": "All Star",
        "artiste": "Smash Mouth",
        "paroles": [
            "Somebody once told me the world is gonna roll me",
            "I ain't the sharpest tool in the shed",
            "She was looking kind of dumb with her finger and her thumb,"
            "In the shape of an L on her forehead"
        ],
        "difficulté" : 2
    }
    ]

```

## Exercice Principal

!!! fox_correction "Nombre de mots"
    **Écrire une fonction `compter_mots` qui prend en paramètre une chanson et renvoie le nombre total de mots dans les paroles.**

    *Indication : Vous pouvez utiliser la méthode `split()` pour séparer une chaîne en mots*

!!! fox_correction "Filtrer par difficulté"
    **Écrire une fonction `filtrer_difficulte` qui prend en paramètre une liste de chansons et un niveau de difficulté maximum (1-5) et renvoie la liste des chansons ne dépassant pas ce niveau.**

!!! fox_correction "Durée estimée"
    **Écrire une fonction `estimer_duree` qui estime la durée d'une chanson en secondes basée sur le nombre de mots.**

    *On considère qu'en moyenne on chante 2 mots par seconde*

**Pour valider cet exercice, vous devrez rendre à votre enseignant les trois fonctions ainsi qu'un exemple d'utilisation avec les chansons fournies.**
